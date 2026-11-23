# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; cat references/phase-4-research.md references/sources.md references/credibility-rubric.md; ls -R
4. ToolSearch: select:WebSearch
5. WebSearch: Bastani "Generative AI without guardrails can harm learning" PNAS high school
6. WebSearch: Lehmann Cornelius Sting "AI meets the classroom" when do large language models harm learning
7. WebSearch: Pew Research teens using ChatGPT for schoolwork 2025 survey
8. WebSearch: Fan "Beware of metacognitive laziness" generative AI British Journal of Educational Technology
9. WebSearch: World Bank Nigeria secondary school generative AI tutoring English after-school randomized evaluation De Simone
10. WebSearch: Gerlich 2025 AI tools cognitive offloading critical thinking Societies journal
11. WebSearch: meta-analysis effect of ChatGPT on students' learning performance Humanities and Social Sciences Communications 2025
12. WebSearch: Kosmyna "Your Brain on ChatGPT" accumulation of cognitive debt essay writing arXiv
13. WebSearch: study high school students how they use ChatGPT homework self-regulated learning journal 2025 secondary students answers versus explanations
14. Agent: 
15. WebFetch: https://doi.org/10.1073/pnas.2422633122
16. WebFetch: https://doi.org/10.1111/bjet.13544
17. WebFetch: https://doi.org/10.3390/soc15010006
18. Agent: 
19. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
20. WebFetch: https://arxiv.org/abs/2409.09047
21. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
22. WebFetch: https://www.mdpi.com/2075-4698/15/1/6
23. WebFetch: https://openknowledge.worldbank.org/entities/publication/15e1ff08-15ae-4f7a-b2a8-d146e6c113ee/full
24. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
25. WebFetch: https://arxiv.org/abs/2506.08872
26. Agent: 
27. WebFetch: https://link.springer.com/article/10.1186/s40561-025-00385-2
28. WebFetch: https://journals-21.hulib.helsinki.fi/lumat/article/download/2877/2306/11219
29. WebFetch: https://doi.org/10.1016/j.compedu.2025.105224
30. Bash: cd <tmp>; for d in 10.1073/pnas.2422633122 10.1111/bjet.13544 10.3390/soc15010006; do echo "== $d"; curl -sL -o /dev/null -w "%{http_code} %{url_effective}\n" -A "Mozilla/5.0 (Macintosh; Intel 
31. Bash: UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 Safari/605.1.15"
for u in "https://papers.ssrn.com/abstract=4895486" "https://arxiv.org/abs/2412.09315" "https://openknowledge.wor
32. Bash: UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 Safari/605.1.15"; D=<claude-temp>33. Bash: D=<claude-temp>python3 -I - "$D" <<'EOF'
import sys,re,html,os
d
34. Bash: for d in 10.1016/j.compedu.2024.105224 10.1596/1813-9450-11125 10.1073/pnas.2422633122 10.3390/soc15010006; do echo "== $d"; curl -s "https://api.openalex.org/works/https://doi.org/$d" | python3 -I -c
35. Bash: curl -s "https://api.crossref.org/works/10.1596/1813-9450-11125" | python3 -I -c "import sys,json;m=json.load(sys.stdin)['message'];print([a.get('given','')+' | '+a.get('family','') for a in m.get('au
