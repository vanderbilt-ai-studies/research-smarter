# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. ToolSearch: select:WebSearch
6. WebSearch: Beland Murphy 2016 "Ill Communication" technology distraction student performance Labour Economics
7. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Ill+Communication+Technology+Distraction+Student+Performance&rows=3&select=DOI,title,author,container-title,published,type" | head -c 3000
8. Bash: curl -s "https://api.crossref.org/works/10.1016/j.labeco.2016.04.004" | python3 -c "import sys,json;m=json.load(sys.stdin)['message'];print(m.get('volume'),m.get('page'),m.get('container-title'),m.get
9. Agent: 
10. WebFetch: https://www.sciencedirect.com/journal/labour-economics/about/aims-and-scope
11. WebFetch: https://doi.org/10.1016/j.labeco.2016.04.004
12. WebFetch: https://www.sciencedirect.com/journal/labour-economics
13. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0927537116300136
