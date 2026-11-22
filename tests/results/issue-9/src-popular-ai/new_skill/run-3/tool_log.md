# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. Read: research-smarter/references/research-types.md
6. ToolSearch: select:WebSearch
7. WebSearch: Bastani "Generative AI without guardrails can harm learning" high school PNAS
8. WebSearch: Lehmann Cornelius Sting "When does ChatGPT harm learning" study
9. WebSearch: Pew Research Center teens ChatGPT schoolwork 2025 survey
10. WebSearch: meta-analysis ChatGPT student learning performance journal 2025 Humanities and Social Sciences Communications
11. WebSearch: Gerlich 2025 AI tools cognitive offloading critical thinking Societies
12. WebSearch: "metacognitive laziness" generative AI learning British Journal of Educational Technology Fan 2025
13. WebSearch: Deng 2025 "Does ChatGPT enhance student learning" systematic review meta-analysis Computers & Education doi
14. WebSearch: OECD Digital Education Outlook 2026 generative AI learning students performance
15. WebSearch: secondary school students ChatGPT homework use learning outcomes study peer-reviewed 2025 copying answers vs explanations
16. WebSearch: Kosmyna "Your Brain on ChatGPT" essay writing EEG arXiv
17. Agent: 
18. WebFetch: https://doi.org/10.1073/pnas.2422633122
19. WebFetch: https://doi.org/10.3390/soc15010006
20. WebFetch: https://doi.org/10.1111/bjet.13544
21. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
22. Agent: 
23. WebFetch: https://doi.org/10.1016/j.compedu.2026.105701
24. WebFetch: https://arxiv.org/abs/2409.09047
25. WebFetch: https://arxiv.org/abs/2506.08872
26. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
27. WebFetch: https://doi.org/10.1080/10494820.2025.2450659
28. WebFetch: https://www.mdpi.com/2075-4698/15/1/6
29. WebFetch: https://doi.org/10.1007/s11858-026-01803-6
30. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
31. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131524002380
32. Agent: 
33. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131526001405
34. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
35. WebFetch: https://www.tandfonline.com/doi/full/10.1080/10494820.2025.2450659
36. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork
37. WebFetch: https://link.springer.com/10.1007/s11858-026-01803-6
38. WebFetch: https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
39. Bash: for d in 10.1073/pnas.2422633122 10.3390/soc15010006 10.1111/bjet.13544 10.1016/j.compedu.2024.105224 10.1016/j.compedu.2026.105701; do echo "== $d"; curl -s -A "research-client" "https://api.crossref
40. Bash: for d in 10.1080/10494820.2025.2450659 10.1007/s11858-026-01803-6; do echo "== $d"; curl -s -A "research-client" "https://api.crossref.org/works/$d" | python3 -I -c 'import json,sys,re; m=json.load(sy
41. Bash: for u in "https://arxiv.org/abs/2412.09315" "https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html" "https://doaj.org/article/d5c17dd91ce64775a065095d8af730ce" "https://papers.ssrn.com/abstr
42. Bash: curl -sL -A "Mozilla/5.0" "https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html" | python3 -I -c 'import sys,re,html; t=sys.stdin.read(); print(len(t)); print(re.sub(r"\s+"," ",html.unescap
43. Bash: curl -s -A "research-client" "https://api.crossref.org/works/10.1787/062a7394-en" | python3 -I -c 'import json,sys,re; m=json.load(sys.stdin)["message"]; print(m.get("title"), m.get("publisher"), m.ge
44. Bash: curl -s -A "research-client" "https://api.crossref.org/works/10.1057/s41599-025-04787-y" | python3 -I -c 'import json,sys; m=json.load(sys.stdin)["message"]; print(m.get("title"), m.get("container-tit
