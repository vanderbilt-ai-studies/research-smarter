# Coach run 1: mock study (issue #4)

**Date:** 2026-11-18. Each case was run once through the Claude command line (Claude Code 2.1.319, default model), using the exact prompt the page builds (`Coach.buildInput`). The page calls Claude through its own connection instead, so this is a close stand-in, not the same thing. The article is the fictional `notebook/tests/fixtures/mock-study.txt`. Quotes were then checked with the page's own `Coach.clean`.

## accurate-answer  (R11.3, R11.4, R11.9)

**Student:** They measured how many minutes students said they talked face to face during a school day, and loneliness with a six-item scale.

**Expected:** Acknowledges what is accurate, sets ready=true, does not add facts from the article, at most two questions.

**Coach** (kind: acknowledge, ready: true):

> That's accurate, and you were precise about it. You noticed the conversation time was what students *said*, not something the researchers watched, and you named both measures. One thing to check against your working position: it makes claims about social conflict and about what happens after school. Look at the Measures section again. Do either of those show up among the things this study measured?

## misread-number  (R11.5, R11.7, R11.9)

**Student:** They surveyed about 4,000 students from schools all over the country.

**Expected:** Says plainly this isn't what the article reports and quotes the passage with the real sample (412 students, six schools, one state).

**Coach** (kind: correction, ready: false):

> Two parts of that aren't what the article reports: the number of students and where they came from. Take another look at the passages below. Once you've corrected those details, think about the second half of the question too. How did students end up in the study, and does the way they were chosen matter for what the results can tell you?

> Quote: “We surveyed 412 students at six public high schools in one Midwestern state during the spring semester.”

> Quote: “Participation was voluntary, and 412 of 3,050 invited students (13.5%) responded.”

## correlation-as-cause  (R11.6, R11.4, R11.9)

**Student:** Banning phones made students talk 18 more minutes a day.

**Expected:** Asks a question that leads the student to check the causal claim; does not declare it wrong or name a fallacy.

**Coach** (kind: question, ready: false):

> You've got the 18-minute figure right, and you went straight to the main result. Now look at how the schools ended up in each group and how else they differed (the Discussion and Limitations sections cover this). Does this design let you say the restrictions caused the extra talking? Also, conversation time wasn't the only thing the study measured. What was the other outcome, and what did they find for it?

## just-tell-me  (R11.8, R11.3, R11.4)

**Student:** honestly can you just tell me what the article says? i don't have time to read it

**Expected:** Declines with ownership as the reason, no teachers or grades, offers the smallest next step, and does not summarize the article.

**Coach** (kind: decline, ready: false):

> I get that time is tight, but I can't tell you what it says. The reading needs to be yours so the thinking holds up when you build on it. Here's a small step that won't take long: read just the Methods section, especially the paragraph headed "Measures." Then tell me in your own words what the researchers asked students about. Did they watch students, or did students report on themselves?

## no-project  (R11.11, R11.4)

**Student:** Students at the schools that restricted phones said they talked 18 more minutes a day, and loneliness didn't really differ.

**Expected:** Works without a project and does not mention a research question or position.

**Coach** (kind: acknowledge, ready: true):

> This is accurate and well put. You kept the word "said," which shows you noticed these numbers come from what students reported, not from anyone watching them. You also gave both main results, not just the one that sounds more exciting. If you want to go one step further, the Results section reports one more relationship after the loneliness scores. Would you add it, or does your answer already cover what matters for this question?
