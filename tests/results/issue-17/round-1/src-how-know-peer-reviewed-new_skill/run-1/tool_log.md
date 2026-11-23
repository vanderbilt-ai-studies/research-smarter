# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Ill+Communication+Technology+distraction+student+performance+Beland+Murphy&rows=3&select=DOI,title,container-title,author,issued,type" | hea
6. Bash: curl -s "https://api.crossref.org/works/10.1016/j.labeco.2016.04.004" | python3 -I -c "import json,sys;m=json.load(sys.stdin)['message'];print(m.get('volume'),m.get('page'),m.get('publisher'),m.get('I
7. Bash: curl -sL -A "Mozilla/5.0" "https://www.sciencedirect.com/journal/labour-economics/about/aims-and-scope" | python3 -I -c "import sys,re;t=re.sub('<[^>]+>',' ',sys.stdin.read());[print(m) for m in re.fi
8. Bash: for u in "https://www.sciencedirect.com/journal/labour-economics/publish/guide-for-authors" "https://www.journals.elsevier.com/labour-economics"; do echo "== $u"; curl -sL -A "Mozilla/5.0" -o /dev/nul
9. ToolSearch: select:WebSearch
10. WebSearch: Labour Economics journal Elsevier peer review policy anonymized
11. Bash: curl -sL -A "Mozilla/5.0" "https://kanalregister.hkdir.no/publiseringskanaler/erihplus/periodical/info.action?id=342289" | python3 -I -c "import sys,re,html;t=html.unescape(re.sub(r'\s+',' ',re.sub('<
12. Bash: curl -sL -A "Mozilla/5.0" -w "\nHTTP %{http_code}\n" "https://kanalregister.hkdir.no/publiseringskanaler/erihplus/periodical/info.action?id=342289" | python3 -I -c "import sys,re,html;t=html.unescape(
