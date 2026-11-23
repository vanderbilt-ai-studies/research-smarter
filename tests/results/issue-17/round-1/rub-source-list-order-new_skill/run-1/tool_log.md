# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; ls -R; cat references/phase-4-research.md references/sources.md references/credibility-rubric.md
4. ToolSearch: select:WebSearch
5. WebSearch: Bastani "Generative AI without guardrails can harm learning" PNAS high school math
6. WebSearch: Pew Research Center teens ChatGPT schoolwork survey 2025
7. WebSearch: meta-analysis ChatGPT student learning performance experimental studies 2025 journal
8. WebSearch: Stadler Bannert Sailer "Cognitive ease at a cost" large language models student inquiry Computers in Human Behavior
9. WebSearch: "Beware of metacognitive laziness" generative AI learning British Journal of Educational Technology
10. WebSearch: OECD Digital Education Outlook 2026 generative AI students learning performance
11. WebSearch: Lehmann Cornelius Sting "AI Meets the Classroom: When Do Large Language Models Harm Learning"
12. WebSearch: Kestin "AI tutoring outperforms in-class active learning" Scientific Reports 2025
13. WebSearch: Gerlich 2025 "AI Tools in Society" cognitive offloading critical thinking Societies
14. Agent: 
15. WebFetch: https://doi.org/10.1073/pnas.2422633122
16. WebFetch: https://www.pnas.org/doi/10.1073/pnas.2422633122
17. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/
18. WebFetch: https://arxiv.org/abs/2409.09047
19. Agent: 
20. WebFetch: https://www.mdpi.com/2075-4698/15/1/6
21. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork/
22. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
23. WebFetch: https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
24. WebFetch: https://doi.org/10.1016/j.chb.2024.108386
25. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/114673
26. Agent: 
27. WebFetch: https://www.sciencedirect.com/science/article/pii/S0360131524002380
28. WebFetch: https://doi.org/10.1111/bjet.13544
29. WebFetch: https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-04787-y.html
30. WebFetch: https://doi.org/10.1057/s41599-025-04787-y
31. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
32. WebFetch: https://www.nature.com/articles/s41599-025-04787-y
33. WebFetch: https://arxiv.org/abs/2412.09315
34. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0747563224002541
35. Bash: for d in 10.1073/pnas.2422633122 10.3390/soc15010006 10.1016/j.chb.2024.108386 10.1016/j.compedu.2024.105224 10.1111/bjet.13544; do curl -s "https://api.crossref.org/works/$d" | python3 -I -c "import 
36. Bash: curl -s "https://api.crossref.org/works/10.1073/pnas.2422633122" | python3 -I -c "import sys,json; print(json.load(sys.stdin)['message'].get('updated-by'))"
for d in 10.1016/j.compedu.2024.105224 10.1
37. Agent: 
38. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/
39. WebFetch: https://doi.org/10.1787/062a7394-en
40. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC12403119/
41. WebFetch: https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
