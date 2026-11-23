# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-5-ongoing.md
4. Read: research-smarter/references/sources.md
5. Read: research-smarter/references/credibility-rubric.md
6. Read: research-smarter/references/research-types.md
7. Bash: curl -sS -o /dev/null -w "%{http_code} %{redirect_url}\n" https://doi.org/10.99999/gjuse.2025.0412; curl -sS -w "\n%{http_code}\n" https://api.crossref.org/works/10.99999/gjuse.2025.0412 | head -c 400
8. Bash: curl -sS "https://api.openalex.org/sources?search=Global%20Journal%20of%20Universal%20Science%20Excellence" | head -c 400; echo; curl -sS "https://api.openalex.org/works?search=Intermittent%20fasting%
9. Bash: curl -sS "https://api.openalex.org/sources?search=Global%20Journal%20of%20Universal%20Science%20Excellence" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['meta']['count'],[s['display_na
