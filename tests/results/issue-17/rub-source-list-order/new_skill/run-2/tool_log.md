# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. Read: research-smarter/references/credibility-rubric.md
6. ToolSearch: select:WebSearch
7. WebSearch: Bastani "Generative AI without guardrails can harm learning" high school mathematics PNAS
8. WebSearch: meta-analysis ChatGPT student learning performance Computers & Education 2025
9. WebSearch: Pew Research teens use ChatGPT for schoolwork 2025 survey
10. WebSearch: Lehmann Cornelius Sting "AI Meets the Classroom: When Do Large Language Models Harm Learning"
11. WebSearch: Stadler Bannert Sailer "Cognitive ease at a cost" large language models student scientific inquiry
12. WebSearch: "metacognitive laziness" generative AI learners British Journal of Educational Technology Fan
13. WebSearch: OECD Digital Education Outlook 2026 generative AI learning performance gains not learning
14. WebSearch: secondary school students ChatGPT homework randomized study learning outcomes journal 2025
15. WebSearch: Gerlich 2025 "AI Tools in Society" cognitive offloading critical thinking Societies
16. Agent: 
17. WebFetch: https://doi.org/10.1073/pnas.2422633122
18. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
19. WebFetch: https://doi.org/10.1057/s41599-025-04787-y
20. Agent: 
21. WebFetch: https://doi.org/10.1016/j.chb.2024.108386
22. WebFetch: https://arxiv.org/abs/2409.09047
23. WebFetch: https://arxiv.org/abs/2412.09315
24. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
25. WebFetch: https://aclanthology.org/2025.acl-long.1502/
26. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131524002380
27. WebFetch: https://www.mdpi.com/2075-4698/15/1/6
28. WebFetch: https://www.nature.com/articles/s41599-025-04787-y
29. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0747563224002541
30. Agent: 
31. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/
32. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
33. WebFetch: https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
34. WebFetch: https://cepr.org/voxeu/columns/generative-ai-learning-penalty-secondary-school
35. Bash: for d in 10.1073/pnas.2422633122 10.1016/j.compedu.2024.105224 10.1057/s41599-025-04787-y 10.1016/j.chb.2024.108386; do curl -s -A "research-client" "https://api.crossref.org/works/$d" | python3 -I -c
36. Bash: for d in 10.1016/j.compedu.2024.105224 10.1016/j.chb.2024.108386; do curl -s -A "research-client" "https://api.openalex.org/works/https://doi.org/$d" | python3 -I -c "
import sys,json; m=json.load(sys
37. Bash: for d in 10.1111/bjet.13544 10.18653/v1/2025.acl-long.1502 10.1787/062a7394-en; do echo "== $d"; curl -s -A "research-client" "https://api.crossref.org/works/$d" | python3 -I -c "import sys,json; m=js
38. Bash: for d in 10.3390/soc15010006 10.1787/062a7394-en; do curl -s -A "research-client" "https://api.openalex.org/works/https://doi.org/$d" | python3 -I -c "
import sys,json; m=json.load(sys.stdin); inv=m.g
