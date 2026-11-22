"""Flag links to blogs and self-publishing platforms in skill replies (R5.5).

A code check that backs up the Claude grader: it scans every reply.md under a
results folder and lists links whose address points to a blog or similar
platform. A flagged link isn't always a violation (R5.9 allows a blog post as
a labeled primary source the project analyzes), so read each one.

Usage: python3 tests/check_source_links.py RESULTS_DIR [RESULTS_DIR ...]
"""
import glob
import os
import re
import sys

BLOG = re.compile(
    r"(medium\.com|substack\.com|blogspot\.|wordpress\.|wikipedia\.org|tumblr\.com|quora\.com|"
    r"reddit\.com|linkedin\.com/pulse|weebly\.com|wixsite\.com|/blogs?/|//blogs?\.)",
    re.I)
LINK = re.compile(r"https?://[^\s)>\]]+")


def main(dirs):
    flagged = 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "**", "reply.md"), recursive=True)):
            for url in sorted(set(LINK.findall(open(f).read()))):
                if BLOG.search(url):
                    flagged += 1
                    print(f"{os.path.relpath(f, d)}: {url}")
    print(f"{flagged} flagged link(s)")


if __name__ == "__main__":
    main(sys.argv[1:] or ["."])
