# Tool log

1. Read: research-smarter-workspace/iteration-10/skill-snapshot/SKILL.md
2. Read: <work>3. Read: research-smarter-workspace/iteration-10/skill-snapshot/references/phase-4-research.md
4. Read: research-smarter-workspace/iteration-10/skill-snapshot/references/sources.md
5. ToolSearch: select:WebSearch
6. WebSearch: Bastani "Generative AI without guardrails can harm learning" PNAS high school
7. WebSearch: Pew Research teens ChatGPT schoolwork 2025 survey
8. WebSearch: Stadler Bannert Sailer "Cognitive ease at a cost" large language models student scientific inquiry Computers in Human Behavior
9. WebSearch: Fan "Beware of metacognitive laziness" generative AI British Journal of Educational Technology
10. WebSearch: Lehmann Cornelius Sting "AI Meets the Classroom: When Do Large Language Models Harm Learning"
11. WebSearch: Zhai Wibowo Li systematic review over-reliance AI dialogue systems students cognitive abilities Smart Learning Environments
12. WebSearch: Wang Fan 2025 meta-analysis effect of ChatGPT on students' learning performance Humanities and Social Sciences Communications
13. WebSearch: Kestin Miller "AI tutoring outperforms in-class active learning" Scientific Reports 2025
14. WebSearch: RAND report 2025 high school students AI use homework survey
15. WebSearch: secondary school students ChatGPT homework self-regulated learning verification study peer-reviewed 2025
16. Agent: 
17. WebFetch: https://doi.org/10.1073/pnas.2422633122
18. WebFetch: https://doi.org/10.1016/j.chb.2024.108386
19. WebFetch: https://doi.org/10.1111/bjet.13544
20. Agent: 
21. WebFetch: https://doi.org/10.1186/s40561-024-00316-7
22. WebFetch: https://doi.org/10.1038/s41598-025-97652-6
23. WebFetch: https://doi.org/10.1186/s40561-025-00385-2
24. WebFetch: https://arxiv.org/abs/2409.09047
25. WebFetch: https://pnas.org/doi/10.1073/pnas.2422633122
26. WebFetch: https://journals.helsinki.fi/lumat/article/download/2877/2306/11219
27. Agent: 
28. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0747563224002541
29. WebFetch: https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13544
30. WebFetch: https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/
31. WebFetch: https://slejournal.springeropen.com/articles/10.1186/s40561-024-00316-7
32. WebFetch: https://www.rand.org/news/press/2026/03/student-use-of-ai-for-homework-rises-as-concerns-grow.html
33. WebFetch: https://link.springer.com/article/10.1186/s40561-024-00316-7
34. WebFetch: https://www.rand.org/pubs/research_reports/RRA4742-1.html
35. WebFetch: https://www.nature.com/articles/s41598-025-97652-6
36. WebFetch: https://slejournal.springeropen.com/articles/10.1186/s40561-025-00385-2
37. WebFetch: https://link.springer.com/article/10.1186/s40561-025-00385-2
38. Bash: for d in 10.1073/pnas.2422633122 10.1016/j.chb.2024.108386 10.1111/bjet.13544 10.1186/s40561-024-00316-7 10.1038/s41598-025-97652-6 10.1186/s40561-025-00385-2; do curl -s "https://api.crossref.org/wor
39. Bash: cd <claude-temp> 2>/dev/null || true; P=~/.claude/pro
40. Agent: 
41. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/
42. WebFetch: https://arxiv.org/abs/2412.09315
43. WebFetch: https://slejournal.springeropen.com/counter/pdf/10.1186/s40561-024-00316-7.pdf
44. WebFetch: https://slejournal.springeropen.com/counter/pdf/10.1186/s40561-025-00385-2.pdf
45. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/files/114673/114673.pdf
46. WebFetch: https://www.pnas.org/doi/full/10.1073/pnas.2422633122
47. WebFetch: https://journals.helsinki.fi/lumat/article/view/2877
48. WebFetch: https://doi.org/10.1016/j.compedu.2024.105224
49. WebFetch: https://link.springer.com/content/pdf/10.1186/s40561-024-00316-7.pdf
50. WebFetch: https://link.springer.com/content/pdf/10.1186/s40561-025-00385-2.pdf
51. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/files/114673/114673.pdf
52. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0360131524002380
53. WebFetch: https://papers.ssrn.com/abstract=4895486
54. Bash: for d in 10.1073/pnas.2422633122 10.1186/s40561-024-00316-7 10.1186/s40561-025-00385-2 10.1016/j.chb.2024.108386 10.1016/j.compedu.2024.105224; do echo "== $d"; curl -s "https://api.openalex.org/works
