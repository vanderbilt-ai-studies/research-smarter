"""Check that every link and DOI in a reply came from a page Claude opened (R5.1).

For each run folder (one with reply.md and opened.jsonl, written by
run_skill_eval.py), it reads every link and DOI in the reply and in any files
Claude created (outputs/, for example the mind map), then checks:

- a link (not a doi.org link) must be a page Claude opened (WebFetch, or curl
  through Bash), compared after normalizing (https, no trailing slash or
  punctuation);
- a DOI, written as text or as a doi.org link, must either have been opened
  itself or appear, character for character (case-insensitive, as DOIs are),
  in the text of a page Claude opened.

Search results don't count as opened pages.

Usage: python3 tests/check_links_opened.py RESULTS_DIR [RESULTS_DIR ...]
Prints each problem and a summary; exits 1 if any run has a problem.
"""
import glob
import json
import os
import re
import sys
from urllib.parse import unquote

LINK = re.compile(r"https?://[^\s)<>\]\"'`]+")
DOI = re.compile(r"\b10\.\d{4,9}/[^\s)<>\]\"'`,;]+")


def norm_url(u):
    u = unquote(u.strip()).rstrip(".,;:*_")
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://(www\.)?", "https://", u)
    return u.rstrip("/").lower()


def norm_doi(d):
    return unquote(d).rstrip(".,;:*_").lower()


def doi_of(url):
    m = re.match(r"https?://(dx\.)?doi\.org/(.+)", url.strip(), re.I)
    return norm_doi(m.group(2)) if m else None


def check_run(run_dir):
    texts = [open(os.path.join(run_dir, "reply.md")).read()]
    for f in glob.glob(os.path.join(run_dir, "outputs", "*")):
        texts.append(open(f, errors="replace").read())
    opened_urls, opened_text = set(), []
    path = os.path.join(run_dir, "opened.jsonl")
    if not os.path.exists(path):
        return None  # run made before pages were saved
    for line in open(path):
        page = json.loads(line)
        for u in page.get("urls", []):
            opened_urls.add(norm_url(u))
        # JSON from Crossref and OpenAlex writes "/" as "\/"; undo that.
        opened_text.append(page.get("text", "").replace("\\/", "/").lower())
    seen = "\n".join(opened_text)
    opened_dois = {doi_of(u) for u in opened_urls if doi_of(u)}

    def doi_ok(d):
        # The DOI must appear whole, not as the start of a longer DOI.
        return d in opened_dois or re.search(re.escape(d) + r"(?![0-9a-z./_-])", seen) is not None

    problems = []
    for text in texts:
        for u in sorted(set(LINK.findall(text))):
            d = doi_of(u)
            if d:
                if not doi_ok(d):
                    problems.append(f"DOI link not opened and not on an opened page: {u}")
            elif norm_url(u) not in opened_urls:
                problems.append(f"link not opened: {u}")
        stripped = LINK.sub(" ", text)  # DOIs written as text, outside links
        for d in sorted(set(DOI.findall(stripped))):
            if not doi_ok(norm_doi(d)):
                problems.append(f"DOI not opened and not on an opened page: {d}")
    return sorted(set(problems))


def main(dirs):
    runs = bad = skipped = 0
    for d in dirs:
        for reply in sorted(glob.glob(os.path.join(d, "**", "reply.md"), recursive=True)):
            run_dir = os.path.dirname(reply)
            problems = check_run(run_dir)
            if problems is None:
                skipped += 1
                continue
            runs += 1
            if problems:
                bad += 1
                print(os.path.relpath(run_dir, d))
                for p in problems:
                    print("   ", p)
    print(f"{runs} runs checked, {bad} with problems, {skipped} skipped (no opened.jsonl)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:] or ["."])
