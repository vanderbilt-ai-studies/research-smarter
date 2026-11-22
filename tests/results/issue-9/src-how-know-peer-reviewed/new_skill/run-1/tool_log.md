# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; ls -R; cat references/phase-4-research.md references/sources.md templates/research-log.md
4. ToolSearch: select:WebSearch
5. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Ill+Communication+technology+distraction+student+performance+Beland+Murphy&rows=3" | python3 -I -c "import json,sys;d=json.load(sys.stdin);[
6. Agent: 
7. WebFetch: https://doi.org/10.1016/j.labeco.2016.04.004
8. WebFetch: https://www.sciencedirect.com/journal/labour-economics/about/aims-and-scope
9. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0927537116300136
10. Bash: curl -s "https://api.openalex.org/works/doi:10.1016/j.labeco.2016.04.004" | python3 -I -c "import json,sys;d=json.load(sys.stdin);print(d['title'],d['publication_year'],[a['author']['display_name'] fo
11. Bash: for u in "https://www.sciencedirect.com/journal/labour-economics/publish/guide-for-authors" "https://www.elsevier.com/journals/labour-economics/0927-5371/guide-for-authors" "https://researchonline.lse
