# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter" && ls -R && cat references/phase-4-research.md references/sources.md references/credibility-rubric.md
4. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Beland+Murphy+Ill+Communication+technology+distraction+student+performance&rows=5" | python3 -c "import json,sys;d=json.load(sys.stdin);[pri
5. Bash: curl -sIL "https://doi.org/10.1016/j.labeco.2016.04.004" | grep -iE "^(HTTP|location)"; echo ---; curl -s "https://api.crossref.org/works/10.1016/j.labeco.2016.04.004" | python3 -c "import json,sys;m=
6. Agent: 
7. WebFetch: https://www.sciencedirect.com/journal/labour-economics
8. WebFetch: https://www.sciencedirect.com/journal/labour-economics/publish/guide-for-authors
9. Bash: for u in "https://www.elsevier.com/journals/labour-economics/0927-5371/guide-for-authors" "https://www.sciencedirect.com/journal/labour-economics/publish/guide-for-authors"; do echo "== $u"; curl -sL 
10. Bash: curl -s "https://api.openalex.org/works?search=Ill%20Communication%20technology%20distraction%20student%20performance&per-page=6" | python3 -c "import json,sys;[print(w['display_name'],'|',w.get('publ
