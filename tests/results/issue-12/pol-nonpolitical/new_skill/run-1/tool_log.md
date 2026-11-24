# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; ls -R; cat references/phase-5-ongoing.md references/sources.md references/credibility-rubric.md references/research-types.md
4. Read: research-smarter/references/phase-5-ongoing.md
5. Read: research-smarter/references/sources.md
6. Read: research-smarter/references/credibility-rubric.md
7. Read: research-smarter/references/phase-4-research.md
8. Bash: cd <claude-temp> 2>/dev/null || mkdir -p <claude-temp>9. Bash: for d in 10.1073/pnas.91.10.4471 10.1242/jeb.022970 10.1073/pnas.1408039111 10.1098/rsbl.2023.0355; do echo "=== $d"; curl -sL "https://api.crossref.org/works/$d" | python3 -c "
import json,sys,re
m=j
10. Bash: curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24889633,19011213&rettype=abstract&retmode=text"; for d in 10.1073/pnas.91.10.4471 10.1242/jeb.022970 10.1073/pnas.14080
