# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; ls -R; cat references/phase-4-research.md references/sources.md references/credibility-rubric.md references/research-types.md
4. Read: research-smarter/references/phase-4-research.md
5. Read: research-smarter/references/sources.md
6. Read: research-smarter/references/credibility-rubric.md
7. Read: research-smarter/templates/research-log.md
8. ToolSearch: select:WebSearch
9. Bash: cd /tmp 2>/dev/null; q() { curl -s "https://api.openalex.org/works?search=$1&per-page=8&select=title,doi,publication_year,primary_location,cited_by_count,authorships" | python3 -I -c "
import sys,json
10. Bash: q() { curl -s "https://api.openalex.org/works?search=$1&per-page=7&select=title,doi,publication_year,primary_location,cited_by_count,authorships" | python3 -I -c "
import sys,json
d=json.load(sys.stdi
11. WebSearch: Pew Research teens ChatGPT schoolwork survey 2025
12. WebSearch: study high school students chatbot homework learning outcomes randomized 2025 2026
13. Bash: for d in 10.1073/pnas.2422633122 10.1073/pnas.2518204122 10.2139/ssrn.4941259 10.1111/bjet.13544 10.1016/j.chb.2024.108386 10.1016/j.compedu.2024.105224 10.1057/s41599-026-07019-z 10.1057/s41599-026-0
14. WebSearch: 26,000 Chinese students AI homework exam scores study paper learning behavior
15. WebSearch: Lehmann Cornelius Sting "AI meets the classroom" ChatGPT harm learning published journal
16. Agent: 
17. WebFetch: https://doi.org/10.1073/pnas.2422633122
18. WebFetch: https://www.pnas.org/doi/10.1073/pnas.2518204122
19. Agent: 
20. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
21. WebFetch: https://aclanthology.org/2025.acl-long.1502/
22. WebFetch: https://arxiv.org/abs/2409.09047
23. Agent: 
24. WebFetch: https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school
25. WebFetch: https://arxiv.org/html/2409.09047v2
26. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/
27. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
28. WebFetch: https://aclanthology.org/2025.acl-long.1502.pdf
29. Agent: 
30. WebFetch: https://doi.org/10.1007/s10648-026-10133-8
31. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
32. WebFetch: https://doi.org/10.1057/s41599-026-07019-z
33. WebFetch: https://doi.org/10.3389/frai.2024.1415782
34. WebFetch: https://doi.org/10.1111/bjet.13544
35. WebFetch: https://doi.org/10.1057/s41599-026-07310-z
36. WebFetch: https://doi.org/10.1016/j.chb.2024.108386
37. WebFetch: https://arxiv.org/abs/2606.08568
38. WebFetch: https://link.springer.com/10.1007/s10648-026-10133-8
39. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131524002380
40. WebFetch: https://www.nature.com/articles/s41599-026-07019-z
41. WebFetch: https://www.frontiersin.org/articles/10.3389/frai.2024.1415782/full
42. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
43. WebFetch: https://www.nature.com/articles/s41599-026-07310-z
44. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0747563224002541
45. Bash: for d in 10.1073/pnas.2422633122 10.1073/pnas.2518204122 10.1007/s10648-026-10133-8 10.1016/j.compedu.2024.105224 10.1057/s41599-026-07019-z 10.1111/bjet.13544 10.1057/s41599-026-07310-z 10.1016/j.chb
46. Agent: 
47. WebFetch: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6868618
48. WebFetch: https://arxiv.org/abs/2607.08849
49. Bash: for d in 10.2139/ssrn.6868618 10.2139/ssrn.6977138 10.48550/arxiv.2607.08849 10.48550/arxiv.2409.09047; do curl -s "https://api.openalex.org/works/doi:$d" | python3 -I -c "
import sys,json
w=json.load
50. Agent: 
51. WebFetch: https://www.thestar.com.my/tech/tech-news/2026/07/17/ai-homework-tools-cut-exam-scores-by-20-study-of-26000-chinese-students-finds
52. Bash: id=$(curl -s "https://api.openalex.org/works/doi:10.1073/pnas.2422633122" | python3 -I -c "import sys,json;print(json.load(sys.stdin)['id'].split('/')[-1])"); curl -s "https://api.openalex.org/works?f
53. Write: <work>