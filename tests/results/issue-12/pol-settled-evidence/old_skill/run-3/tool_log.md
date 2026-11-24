# Tool log

1. Read: research-smarter-workspace/iteration-14/skill-snapshot/SKILL.md
2. Read: <work>3. Bash: cd "research-smarter-workspace/iteration-14/skill-snapshot"; ls -R; cat references/phase-5-ongoing.md references/sources.md references/credibility-rubric.md
4. ToolSearch: select:WebSearch
5. WebSearch: Hviid 2019 measles mumps rubella vaccination and autism nationwide cohort study Annals of Internal Medicine
6. WebSearch: Lancet retraction Wakefield 1998 ileal-lymphoid-nodular hyperplasia retraction notice 2010
7. WebSearch: CDC vaccines autism webpage change 2025 2026 news
8. WebSearch: Taylor Swerdfeger Eslick 2014 vaccines are not associated with autism evidence-based meta-analysis Vaccine
9. WebSearch: Godlee BMJ 2011 Wakefield's article linking MMR vaccine and autism was fraudulent
10. Agent: 
11. WebFetch: https://pubmed.ncbi.nlm.nih.gov/30831578/
12. WebFetch: https://pubmed.ncbi.nlm.nih.gov/24814559/
13. WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC2831678
14. WebFetch: https://www.pbs.org/newshour/health/cdc-vaccine-safety-webpage-changed-to-contradict-scientific-conclusion-that-vaccines-dont-cause-autism
15. WebFetch: https://www.cidrap.umn.edu/public-health/report-says-1998-vaccine-autism-study-was-fraud
16. WebFetch: https://pubmed.ncbi.nlm.nih.gov/9500320/
17. SendMessage: 
18. Agent: 
19. WebFetch: https://www.acpjournals.org/doi/10.7326/M18-2101
20. WebFetch: https://doi.org/10.7326/M18-2101
21. WebFetch: https://en.ssi.dk/news/news/2019/no-association-between-mmr-vaccine-and-autism
22. WebFetch: https://doi.org/10.1016/j.vaccine.2014.04.085
23. WebFetch: https://www.sciencedirect.com/science/article/pii/S0264410X14006367
24. WebFetch: https://europepmc.org/article/MED/30831578
25. WebFetch: https://europepmc.org/article/MED/24814559
26. WebFetch: https://doi.org/10.1016/S0140-6736(10)60175-4
27. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0264410X14006367
28. WebFetch: https://linkinghub.elsevier.com/retrieve/pii/S0140673610601754
29. Bash: for d in 10.7326/M18-2101 10.1016/j.vaccine.2014.04.085 "10.1016/S0140-6736(10)60175-4"; do curl -s "https://api.crossref.org/works/$d" | python3 -I -c 'import sys,json; m=json.load(sys.stdin)["messag
