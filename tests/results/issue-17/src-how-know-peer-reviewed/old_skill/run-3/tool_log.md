# Tool log

1. Read: research-smarter-workspace/iteration-11/skill-snapshot/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter-workspace/iteration-11/skill-snapshot" && ls -R && cat references/phase-4-research.md references/sources.md references/credibility-rubr
4. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Beland+Murphy+Ill+Communication+technology+distraction+student+performance&rows=5" | python3 -c "import json,sys;d=json.load(sys.stdin);[pri
5. Bash: curl -s "https://api.crossref.org/works/10.1016/j.labeco.2016.04.004" | python3 -c "import json,sys;i=json.load(sys.stdin)['message'];print(i.get('volume'),i.get('page'),i.get('ISSN'),i.get('publisher
6. Bash: curl -sL -A "Mozilla/5.0" "https://www.sciencedirect.com/journal/labour-economics/about/aims-and-scope" | grep -oi "[^.<>]*peer[- ]review[^.<>]*" | head -5; curl -sL -A "Mozilla/5.0" "https://www.scie
7. Bash: for u in "https://www.elsevier.com/journals/labour-economics/0927-5371/guide-for-authors" "https://www.sciencedirect.com/journal/labour-economics"; do curl -sL -A "Mozilla/5.0" -o /dev/null -w "%{http
