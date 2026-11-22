# Tool log

1. Read: research-smarter/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter"; ls -R; cat references/phase-4-research.md references/sources.md; cat references/research-types.md templates/research-log.md
4. ToolSearch: select:WebSearch
5. WebSearch: school smartphone ban face-to-face interaction adolescents study journal
6. WebSearch: school mobile phone ban bullying cyberbullying effect study peer-reviewed
7. WebSearch: Goodyear 2025 Lancet Regional Health Europe restrictive school smartphone policies SMART Schools
8. WebSearch: Abrahamsson smartphone bans Norway bullying journal published
9. WebSearch: Böttger Zierer "To Ban or Not to Ban" smartphone schools social well-being Education Sciences
10. WebSearch: phone-free school students socializing lunch qualitative study secondary school phone ban
11. WebSearch: Bar 2025 Computers in Human Behavior students perceptions school phone ban South Australia open-ended
12. WebSearch: van Luydt 2026 disconnect smartphone ban Dutch schools well-being bullying social connectedness journal
13. WebSearch: Beneito Vicente-Chirivella banning mobile phones schools Spain bullying journal
14. WebSearch: schools with mobile phone bans greater victimization harassment study 2022 online harassment outside school hours
15. WebSearch: SMART Schools qualitative Social Science & Medicine 2026 phone policies bullying face-to-face
16. WebSearch: Reynolds Esfandiari O'Higgins Norman 2025 smartphone ban students experiences Ireland journal
17. Agent: 
18. WebFetch: https://doi.org/10.3390/educsci14080906
19. WebFetch: https://doi.org/10.1108/AEA-05-2021-0112
20. WebFetch: https://doi.org/10.1007/s10964-025-02313-6
21. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC11737419/
22. Agent: 
23. WebFetch: https://research.birmingham.ac.uk/en/publications/school-phone-policies-and-their-association-with-mental-wellbeing/
24. WebFetch: https://research.birmingham.ac.uk/en/publications/how-school-phone-policies-influence-adolescent-phone-use-and-well/
25. WebFetch: https://www.birmingham.ac.uk/news/2026/school-phone-bans-or-not-digital-lives-of-students-affect-the-school-day
26. WebFetch: https://researchnow-admin.flinders.edu.au/ws/portalfiles/portal/152076210/Bar_Student_P2025.pdf
27. Agent: 
28. WebFetch: https://jhr.uwpress.org/keyword/bullying
29. WebFetch: https://econpapers.repec.org/RePEc:hhs:nhheco:2024_001
30. WebFetch: https://antibullyingcentre.ie/wp-content/uploads/2025/06/Restriction-or-Resilience_Report_June_2025_ABC.pdf
31. WebFetch: https://www.education-ni.gov.uk/sites/default/files/2026-08/Lockable%20Smartphone%20Pouches%20in%20Northern%20Ireland%20Post%20Primary%20Schools%20%E2%80%93%20A%20Cohort%20Study_0.pdf
32. WebFetch: https://www.mdpi.com/2227-7102/14/8/906
33. WebFetch: http://www.emerald.com/aea/article/30/90/153-175/59588
34. WebFetch: https://link.springer.com/10.1007/s10964-025-02313-6
35. WebFetch: https://doi.org/10.1016/j.lanepe.2025.101211
36. WebFetch: https://doi.org/10.1016/j.socscimed.2026.119094
37. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S2666776225000031
38. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S027795362600170X
39. WebFetch: https://doi.org/10.3368/jhr.0224-13403R2
40. WebFetch: https://www.dcu.ie/antibullyingcentre/restriction-or-resilience
41. WebFetch: http://jhr.uwpress.org/lookup/doi/10.3368/jhr.0224-13403R2
42. Bash: D=<claude-temp>; S=<claude-temp>43. Bash: D=<claude-temp>; S=<claude-temp>44. Read: <claude-temp>45. Read: <claude-temp>46. Agent: 
47. WebFetch: https://news.flinders.edu.au/blog/2025/09/18/benefits-of-school-phone-bans/
48. WebFetch: https://researchnow.flinders.edu.au
49. WebFetch: https://doaj.org/article/8b3371303a5a4d2c88dd26e236f64089
50. WebFetch: https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/115172
51. WebFetch: https://cris.maastrichtuniversity.nl/en/publications/disconnect-to-reconnect-how-variations-between-types-of-smartphon/
52. WebFetch: https://www.dcu.ie/antibullyingcentre/restriction-or-resilience
53. WebFetch: https://doi.org/10.1007/s10964-025-02313-6
54. WebFetch: https://www.sciencedirect.com/science/article/pii/S0747563225000500
55. WebFetch: https://doi.org/10.1016/j.chb.2025.108767
56. WebFetch: https://www.dcu.ie/antibullyingcentre/restriction-or-resilience
57. WebFetch: https://www.education-ni.gov.uk/
58. WebFetch: https://link.springer.com/10.1007/s10964-025-02313-6
59. WebFetch: https://doi.org/10.1111/eip.13517
60. WebFetch: https://www.dcu.ie/antibullyingcentre/restriction-or-resilience
61. WebFetch: https://www.education-ni.gov.uk/publications
62. WebFetch: https://www.education-ni.gov.uk/consultations/public-consultation-measures-support-mobile-phone-free-schools-northern-ireland
63. WebFetch: https://www.education-ni.gov.uk/sites/default/files/2026-08/Lockable%20Smartphone%20Pouches%20in%20Northern%20Ireland%20Post%20Primary%20Schools%20%E2%80%93%20A%20Cohort%20Study_0.pdf
64. Bash: curl -s "https://api.crossref.org/works?query.bibliographic=Student+perspectives+on+banning+mobile+phones+in+South+Australian+secondary+schools&rows=2&select=DOI,title,container-title,author,published
65. Bash: curl -s "https://api.crossref.org/works/10.3390/educsci14080906" | python3 -I -c "import json,sys;m=json.load(sys.stdin)['message'];print(m['title'],m['container-title'],m.get('volume'),m.get('issue')
66. Bash: for d in 10.1556/2006.2024.00058 10.1016/j.lanepe.2025.101211 10.3390/educsci14080906; do curl -s -o /dev/null -w "$d %{http_code} %{redirect_url}\n" https://doi.org/$d; done; curl -s "https://api.cro
