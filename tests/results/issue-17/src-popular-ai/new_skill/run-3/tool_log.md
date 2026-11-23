# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. Read: research-smarter/references/credibility-rubric.md
6. Read: research-smarter/references/research-types.md
7. ToolSearch: select:WebSearch
8. WebSearch: Bastani "Generative AI without guardrails can harm learning" PNAS high school
9. WebSearch: meta-analysis ChatGPT student learning performance experimental studies 2025 journal
10. WebSearch: Pew Research teens ChatGPT schoolwork survey 2025
11. WebSearch: study students LLM cognitive offloading mental effort depth learning Stadler Bannert Sailer Computers in Human Behavior
12. WebSearch: "metacognitive laziness" generative AI learners British Journal of Educational Technology Fan 2025
13. WebSearch: Lehmann Cornelius Sting "AI Meets the Classroom" when do large language models harm learning
14. WebSearch: OECD Digital Education Outlook 2026 generative AI students performance learning
15. WebSearch: secondary school students ChatGPT homework use patterns answer-seeking vs learning outcomes study journal
16. Agent: 
17. WebFetch: https://doi.org/10.1073/pnas.2422633122
18. WebFetch: https://arxiv.org/abs/2409.09047
19. Agent: 
20. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
21. WebFetch: https://doi.org/10.1057/s41599-025-04787-y
22. WebFetch: https://www.sciencedirect.com/science/article/pii/S0360131524002380
23. Agent: 
24. WebFetch: https://www.nature.com/articles/s41599-025-04787-y
25. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
26. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/114673
27. WebFetch: https://arxiv.org/abs/2412.09315
28. WebFetch: https://doi.org/10.1111/bjet.13544
29. WebFetch: https://link.springer.com/article/10.1007/s11858-026-01803-6
30. Agent: 
31. WebFetch: https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
32. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/
33. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
34. Bash: curl -s https://api.crossref.org/works/10.1073/pnas.2422633122 | python3 -I -c "import json,sys;m=json.load(sys.stdin)['message'];print(m['title'],m.get('container-title'),m.get('volume'),m.get('issue
35. Bash: for d in 10.1057/s41599-025-04787-y 10.1016/j.compedu.2024.105224 10.1073/pnas.2422633122; do curl -s "https://api.openalex.org/works/doi:$d" | python3 -I -c "
import json,sys;m=json.load(sys.stdin)
p
36. Bash: for d in 10.1016/j.compedu.2024.105224 10.1057/s41599-025-04787-y; do curl -s https://api.crossref.org/works/$d | python3 -I -c "import json,sys;m=json.load(sys.stdin)['message'];print(m['DOI'],m['tit
37. Bash: curl -s https://api.crossref.org/works/10.1787/062a7394-en | python3 -I -c "import json,sys;m=json.load(sys.stdin)['message'];print(m['DOI'],m['title'],m.get('publisher'),m.get('issued'),m.get('type')
38. Agent: 
39. WebFetch: https://api.crossref.org/works/10.1057/s41599-026-07310-z
40. WebFetch: https://api.crossref.org/works/10.1057/s41599-025-04787-y
41. Bash: for d in 10.1111/bjet.13544 10.1016/j.chb.2024.108386; do curl -s "https://api.openalex.org/works/doi:$d" | python3 -I -c "
import json,sys;m=json.load(sys.stdin)
print('==',m['doi'],'|',m['title'],'|
42. Bash: curl -s "https://api.openalex.org/works/doi:10.1007/s11858-026-01803-6" | python3 -I -c "
import json,sys;m=json.load(sys.stdin)
print('==',m['doi'],'|',m['title'],'|',m['publication_year'],'|',(m.get
43. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/114673
44. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
