# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Read: research-smarter/references/phase-4-research.md
4. Read: research-smarter/references/sources.md
5. Read: research-smarter/references/credibility-rubric.md
6. ToolSearch: select:WebSearch
7. WebSearch: Bastani "Generative AI without guardrails can harm learning" high school mathematics PNAS
8. WebSearch: "From chalkboards to chatbots" Nigeria secondary school English AI tutoring World Bank study
9. WebSearch: meta-analysis ChatGPT effect on students' learning performance journal 2025
10. WebSearch: Pew Research teens ChatGPT schoolwork survey 2025
11. WebSearch: "metacognitive laziness" generative AI learning British Journal of Educational Technology Fan
12. WebSearch: Lehmann Cornelius Sting "AI meets the classroom" when do large language models harm learning
13. WebSearch: Gerlich 2025 "AI Tools in Society" cognitive offloading critical thinking Societies
14. WebSearch: secondary school students ChatGPT homework study patterns of use learning outcomes peer-reviewed 2025 Computers & Education
15. WebSearch: Kestin "AI tutoring outperforms in-class active learning" Scientific Reports
16. WebSearch: Kosmyna "Your Brain on ChatGPT" essay writing cognitive debt arXiv
17. Agent: 
18. WebFetch: https://doi.org/10.1073/pnas.2422633122
19. WebFetch: https://openknowledge.worldbank.org/entities/publication/15e1ff08-15ae-4f7a-b2a8-d146e6c113ee/full
20. WebFetch: https://doi.org/10.1057/s41599-025-04787-y
21. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
22. WebFetch: https://www.irrodl.org/index.php/irrodl/article/view/8775
23. Agent: 
24. WebFetch: https://doi.org/10.1111/bjet.13544
25. WebFetch: https://arxiv.org/abs/2409.09047
26. WebFetch: https://doi.org/10.3390/soc15010006
27. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
28. WebFetch: https://doi.org/10.1038/s41598-025-97652-6
29. WebFetch: https://www.nature.com/articles/s41599-025-04787-y
30. WebFetch: https://arxiv.org/abs/2506.08872
31. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131524002380
32. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
33. Agent: 
34. WebFetch: https://www.mdpi.com/2075-4698/15/1/6
35. WebFetch: https://www.nature.com/articles/s41598-025-97652-6
36. WebFetch: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/
37. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
38. WebFetch: https://www.hh.se/english/information-english/news/news/2025-02-27-thoughtful-choices-when-upper-secondary-school-students-use-ai-in-their-schoolwork.html
39. WebFetch: https://www.sciencedirect.com/science/article/pii/S2666920X24001632?via%3Dihub
40. Bash: for d in 10.1073/pnas.2422633122 10.1057/s41599-025-04787-y 10.1016/j.compedu.2024.105224 10.1111/bjet.13544 10.3390/soc15010006 10.1038/s41598-025-97652-6 10.1016/j.caeai.2024.100360 10.19173/irrodl.
41. Bash: for d in 10.1073/pnas.2422633122 10.1016/j.compedu.2024.105224 10.1111/bjet.13544 10.3390/soc15010006 10.1038/s41598-025-97652-6 10.1016/j.caeai.2024.100360 10.19173/irrodl.v27i1.8775 10.1057/s41599-0
42. Bash: for d in 10.1073/pnas.2422633122 10.1016/j.compedu.2024.105224 10.1111/bjet.13544 10.3390/soc15010006 10.1038/s41598-025-97652-6 10.1016/j.caeai.2024.100360; do echo "== $d"; curl -s -A "research-clie
43. Bash: curl -s -A "research-client/1.0" "https://api.openalex.org/works?search=From%20Chalkboards%20to%20Chatbots%20Nigeria&per-page=3" | python3 -I -c 'import sys,json
for w in json.load(sys.stdin)["results
44. Bash: curl -s -L -A "Mozilla/5.0" https://econpapers.repec.org/paper/wbkwbrwps/11125.htm | python3 -I -c 'import sys,re,html;t=sys.stdin.read();t=re.sub(r"<[^>]+>"," ",t);t=html.unescape(re.sub(r"\s+"," ",t
