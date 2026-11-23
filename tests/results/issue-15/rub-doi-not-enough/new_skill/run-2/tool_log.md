# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter/references"; cat phase-5-ongoing.md sources.md credibility-rubric.md research-types.md
4. Bash: curl -sI -m 20 "https://doi.org/10.99999/gjuse.2025.0412" | head -5; echo ---; curl -s -m 20 "https://api.crossref.org/works/10.99999/gjuse.2025.0412" | head -c 300; echo; echo ---; curl -s -m 20 "htt
5. Bash: curl -s -m 20 "https://api.openalex.org/sources?search=Global%20Journal%20of%20Universal%20Science%20Excellence" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['meta'].get('count'),[s['d
