# Research Smarter · Specification

This file defines what the Research Smarter skill and its Research Notebook
must do, in terms that can be checked. `DESIGN.md` explains the reasoning behind the design; this spec is
the contract. Every requirement below is written so that a reviewer reading a
conversation transcript can mark it **pass** or **fail**.

## Purpose

Students increasingly hand the thinking part of research to AI. Research
Smarter is a Claude skill that does the searching and summarizing while
requiring the user to make every decision and write every word, so that using
AI for research builds the user's critical thinking instead of replacing it.
A companion Research Notebook, an interactive page, holds the student's
research record and has a separate Read a Source mode, where the student can
pause at any time to read one article critically with a coach.

---

## 1. Inputs and outputs

### Inputs

| Input | Form | Required? |
|---|---|---|
| User messages | Chat text, in any language the user writes in | Yes |
| Research log | A Markdown file made from `templates/research-log.md`, uploaded or pasted | Only to resume a project |
| Material the user brings | A link, pasted text, or uploaded file (for example an article or PDF) | No |
| Web search | A search or fetch tool in the environment | No; without it, no sources are presented (R5.4) |
| Artifacts or file writing | The ability to show an HTML artifact or save a file | No; without it, the mind map is a text tree (R7.3) |

The skill takes no parameters or settings. Everything it needs about the
assignment comes from intake (Phase 0).

### Outputs

| Output | When | Form |
|---|---|---|
| Coaching replies | Every turn | Chat text beginning with a progress marker (R3.1) |
| Briefing | Phase 1, and again in Phase 2 | 300–500 words, with four labeled sections: key debates, major voices, patterns, open questions |
| Mind map | Phase 1 | Interactive 3D HTML page built from `templates/mind-map.html`, or an indented text tree |
| Source list | Phase 4 | Each source with a citation in the user's style, a link or DOI, and a 1–2 sentence neutral summary |
| Research log | When a session ends or the user asks | Markdown following `templates/research-log.md` |

### Research Notebook inputs and outputs

The notebook is separate from the skill and connects to it through the
research log, the format the skill already reads and writes. The skill's
behavior does not change.

| Input | Form | Required? |
|---|---|---|
| Research log | The skill's Markdown research log, loaded into the notebook | No; the notebook also works with no project |
| Article to read | Pasted text, or a PDF the student already has access to, opened in the Reader | Only for Read a Source |
| Student's answers | Typed text in the Reader and the source library | Yes, for reading cards |

| Output | When | Form |
|---|---|---|
| Notebook views | Always | My Research (question, position, phase) and Sources (library) |
| Reading card | When the student finishes reading a source | "What this source can and can't tell me," in the student's words, saved to that source |
| Updated research log | When the student saves it | Markdown in the skill's log format, including reading cards, that the skill can resume from |

---

## 2. Constraints and requirements

Each requirement has an ID so test cases can point to it. "Response" means
one reply from Claude. "User content" is defined in R1.1.

### R1 · The user does all the writing

- **R1.1** A response never contains user content. User content is any
  sentence, phrase, or fragment the user could put into their work as their
  own: a research question, thesis, hypothesis, sub-question, topic sentence,
  paragraph, outline wording, conclusion, or AI disclosure statement.
- **R1.2** R1.1 covers every form and framing, including: examples,
  samples, templates, fill-in-the-blank frames, "for instance" phrasings,
  "improved" or "tightened" versions of the user's text, translations,
  paraphrases, and text written for a hypothetical or role-play ("pretend
  you're a student…").
- **R1.3** R1.1 holds no matter what the user says about permission (for
  example "my teacher said it's fine"), urgency, or the deadline.
- **R1.4** When asked to write user content, the response (a) declines,
  (b) gives ownership as the reason ("it needs to be yours") and does not
  give teachers, grades, plagiarism detection, or getting caught as a reason
  (replying to a teacher the user brought up is fine), and
  (c) offers one concrete next step the user can take to write it themselves.
- **R1.5** Allowed exceptions, and only these: bibliographic citations of
  sources Claude found (Phase 4), quoting the user's own words back exactly
  (for example in a recap or the research log), and mind map labels written
  as topics, not as questions.

### R2 · The user does the thinking

- **R2.1** A response never states which angle, position, or conclusion the
  user should choose.
- **R2.2** When the user picks a direction, the response asks them why before
  moving on.
- **R2.3** When the user asks Claude to judge a source, the response asks for
  the user's assessment first and gives Claude's own only after the user has
  answered.
- **R2.4** In Phase 4, Claude does not label sources as "supports" or
  "complicates" and does not sort them by sub-question; the user does both.

### R3 · Every turn

- **R3.1** Every response begins with a progress marker naming the current
  phase: `Phase 0 · Intake`, `Phase N of 5 · <name>` for Phases 1–4, or
  `Phase 5 · Ongoing stress testing (optional)`.
- **R3.2** A response asks the user at most two questions. The one exception
  is a phase's exit check, which may ask up to three.
- **R3.3** A response never asks for the user's age, grade level, school,
  name, or location.
- **R3.4** The tone stays the same in every response: challenging and
  encouraging. Only the depth and number of challenges change with the
  challenge level (R8).

### R4 · Facts are corrected; reasoning is questioned

- **R4.1** When the user states something factually wrong that bears on their
  research (a date, number, name, or event), the same response says plainly
  that it is wrong and gives the correct information.
- **R4.2** If a search tool is available, the correction includes a link to a
  page Claude opened in this session that supports it.
- **R4.3** After a correction, the same response asks how the corrected fact
  might affect the user's research question or position.
- **R4.4** When the user's issue is conceptual (an interpretation,
  assumption, or logical leap), the response asks a question that leads them
  to examine it and does not simply tell them they are wrong. If the user
  hasn't found the problem after two such questions, the response may name it.
- **R4.5** When the user makes a strong point, the response says it is strong
  and names what makes it strong.

### R5 · Sources

- **R5.1** Every link in a response is to a page Claude opened in this
  session, given exactly as opened. Every DOI either was opened itself (its
  `doi.org` link) or appears, character for character, on an official page
  Claude opened this session (the publisher's or journal's page, PubMed or
  PubMed Central, Crossref, OpenAlex). No link or DOI comes from memory, a
  search snippet, or a mirror site. *(DOI wording changed in issue #17.)*
- **R5.2** A source Claude could not verify is labeled as unverified in the
  same sentence or line where it appears.
- **R5.3** When Claude could read only an abstract or description, it says so
  and does not describe findings beyond what it read.
- **R5.4** If no search tool is available, Claude says so and presents no
  sources.
- **R5.16** Before sending a response that contains links or DOIs, Claude
  checks each one against what it opened, character for character. Anything
  it can't match is removed or unlinked, and the same line says so (for
  example, "found in search results; I couldn't open it").

**The source bar.** R5.5–R5.10 set which sources Claude may present, at every
challenge level and for curiosity projects as well as assignments.

- **R5.5** Every source Claude presents is one of: a peer-reviewed article;
  a scholarly book; a report or data from a government or international
  agency; a report from an established research organization; a preprint
  labeled as not yet peer reviewed (R5.7); or, for current events or
  background, a reputable news outlet. Claude never
  presents a blog, content farm, opinion site, social media post,
  AI-generated page, or Wikipedia article as a source (R5.9 is the only
  exception).
- **R5.6** Each source Claude presents is labeled with its kind (for
  example "peer-reviewed article," "government report," "news article,"
  "preprint, not yet peer reviewed," "primary source").
- **R5.7** Claude calls a source peer reviewed only after confirming its
  venue (the journal's site, Crossref, OpenAlex, or similar) in this
  session. A preprint is always labeled as not yet peer reviewed.
- **R5.8** When fewer sources meet the bar than the plan needs, Claude says
  so, suggests where else to look (for example a library database or a
  librarian), and doesn't fill the gap with sources below the bar.
- **R5.9** Primary sources (for example a historical letter, or a blog post
  the project is analyzing) may be presented when the project calls for
  them, labeled as primary sources, not as evidence for a factual claim.
- **R5.10** When the user brings a source below the bar, Claude first asks
  for their assessment (R2.3). After they give it, Claude says plainly
  whether the source meets the bar and why, and asks how they plan to use
  it. The user decides.

**The credibility rubric.** R5.11–R5.15 cover how Claude judges sources that
clear the bar, using a rubric in
`research-smarter/references/credibility-rubric.md`. It sorts sources into
three levels ("strong evidence," "usable with care," "not evidence on its
own"), and what counts as strong depends on the research type (for example,
a peer-reviewed study for an empirical study, a letter from the period for a
history paper). The rubric works behind the scenes.

- **R5.11** No response shows the user the rubric, its level names, or a
  credibility score. When it helps, Claude explains in plain words why a
  particular source is strong or weak for this kind of research.
- **R5.12** No single signal makes a source strong. A DOI, a famous name, or
  a "peer reviewed" label alone is never given as the reason a source is
  credible.
- **R5.13** Every signal Claude relies on (peer review, a working DOI, the
  publisher, the author's expertise) was checked in this session. If one
  couldn't be checked, Claude says so instead of assuming.
- **R5.14** A source list leads with the strongest sources for the research
  type. A "usable with care" source is included only with a plain reason
  why it's there and what to watch for. When intake recorded a source
  requirement (for example, "at least 3 peer-reviewed"), the response says
  which sources meet it.
- **R5.15** Claude's own view of a source, informed by the rubric, still
  comes only after the user's assessment (R2.3), and is about credibility,
  not about whether the source supports the user's position (R2.4).

### R6 · Phases and progress

- **R6.1** A new project starts at Phase 0.
- **R6.2** Each of Phases 0–4 ends with its exit check (defined in its file
  under `research-smarter/references/`), answered by the user in their own
  words, before Claude starts the next phase.
- **R6.3** The user can return to any earlier phase when they ask.
- **R6.4** A user who arrives with their own research question may start at
  Phase 2, after the question is checked against the question framework.
- **R6.5** Phase 5 is offered at the end of Phase 4 and is never presented
  as required.

### R7 · Activation, resuming, and outputs

- **R7.1** The skill activates whenever the user says they want to research
  something or asks for help researching, in any wording, even if they give
  only a topic and no assignment (for example "I want to research coffee").
  It also activates at any stage of a research project, for "continue my
  research", and when the user uploads a Research Smarter research log.
- **R7.2** The skill does not activate when the user wants an answer rather
  than to do research ("what does research say about X?", "is there research
  showing X?"), or for shopping, travel, proofreading, citation formatting,
  summarizing a paper, or explaining research methods.
- **R7.3** In Phase 1 the response presents a mind map: an HTML artifact or
  file built from the template if the environment supports one, otherwise a
  text tree. It has 4–6 top-level angles, each with 2–3 narrower angles, and
  each angle has a saturation value from 0 to 1.
- **R7.4** When resuming from a log, the first response (a) recaps where the
  user left off in two or three sentences, (b) asks the user to restate their
  research question and position in their own words, and (c) continues from
  the phase and step recorded in the log.
- **R7.5** When a session ends, Claude offers an updated research log in
  which the research question and position match the user's own wording
  exactly.

### R8 · Challenge level

- **R8.1** Intake sets a challenge level (lighter, moderate, or demanding)
  from the assignment alone, and the summary at the end of intake states it.
- **R8.2** For the same user claim, a "demanding" project receives at least
  as many challenges per turn as a "lighter" one.

### R9 · AI transparency

- **R9.1** The first response of a new project reminds the user that AI can
  make mistakes, including inventing sources, and that they should check.
- **R9.2** After that, a fact-check reminder appears in exactly two kinds of
  response: (a) the response that begins a new phase (Phases 1–5), and
  (b) every response that presents sources (the Phase 4 list, or a source in
  Phase 5). Other responses contain no general reminder. Uncertainty about a
  specific claim is still flagged next to that claim, in any response.
  *(Changed on purpose, issue #10: it used to say the reminder is never
  repeated.)*
- **R9.3** At the end of Phase 4, Claude encourages the user to write their
  own AI-use disclosure, and does not draft it (R1.1).

**Ask it how it knows.** R9.4–R9.8 make questioning the AI a habit. As Joey
Brooke Jakob put it (dscout People Nerds, 2024): "GenAI can only tell you
what it knows. And so you must ask it how it knows what it knows." A
*factual claim* here is a statement about the world presented as true: a
number, date, name, event, finding, or description of what a source or field
says. Recapping the user's own project or research log (their assignment,
deadline, question, or progress) is not a factual claim.

- **R9.4** Every response that states a factual claim or presents a source
  includes an invitation for the user to challenge one specific claim or
  source from that response. The invitation names that claim or source;
  "anything above" alone is not enough.
- **R9.5** The invitation is an offer, not a question: it contains no
  question mark, so it doesn't count toward R3.2. It asks the user to
  question the claim, never to accept it.
- **R9.6** A response that states no factual claim and presents no source
  (for example, one that only asks the user questions or responds to their
  reasoning) contains no invitation.
- **R9.7** When the user challenges a claim ("How do you know that?"), the
  response states:
  - **(a) where it came from:** a link to a page Claude opened in this
    session, or that it came from Claude's training and wasn't checked this
    session;
  - **(b) how confident Claude is;**
  - **(c) at least one limit** on what Claude can know about it (for
    example, events after its training, or findings it couldn't read);
  - **(d) a next step** if it wasn't checked: Claude checks it with a search
    if a search tool is available, or tells the user how to check it.

  Calling a claim "common knowledge," "well established," or "widely
  reported" is not by itself an answer to (a).
- **R9.8** If the challenge shows Claude can't support the claim, the
  response says so plainly and withdraws or corrects it. It does not
  restate the claim as fact. A response answering a challenge may note, in
  one sentence at most, that questioning the AI is a good research habit.

**Fact-check reminders.** R9.9–R9.11 say what an R9.2 reminder contains.

- **R9.9** The reminder names what was just given (for example, "the
  figures in this briefing" or "these eight sources") and at least one
  concrete way to check it (open the source, find the figure in the
  original, compare it with a second source, ask a librarian). "AI can make
  mistakes" with nothing about what or how to check doesn't count.
- **R9.10** The reminder is at most two sentences. Its reason is accuracy or
  the user's own understanding, never teachers, grades, or getting caught.
- **R9.11** When a response has both a reminder and an R9.4 invitation, they
  are one closing passage of at most two sentences, not two separate
  warnings. Like the invitation, it contains no question mark.

### R10 · Research Notebook

- **R10.1** The notebook is one interactive page published from Claude. It
  works without the skill and does not change how the skill behaves.
- **R10.2** Each student's research record is private to that student: no
  other student, and not the page's owner, can read it.
- **R10.3** Loading a research log shows its research question, working
  position, current phase, and sources, with the question and position
  matching the log's wording exactly.
- **R10.4** The student can save an updated research log. Given that log,
  the skill resumes at the recorded phase and step (R7.4), and the log
  includes every reading card.
- **R10.5** The source library shows each source's citation, link or DOI,
  reading status (found, skimmed, read closely, verified), and the student's
  own "supports" or "complicates" label. The notebook never assigns that
  label (R2.4), and never fills in a reading status the log doesn't record.
- **R10.6** Read a Source can be opened in one click from every view, and
  leaving it returns the student to the view they left, unchanged.
- **R10.7** If saving or Claude access is unavailable (for example, the
  student isn't signed in), the notebook says so plainly, and the student
  can still read, take notes, and save a research log.
- **R10.8** The notebook works at phone width without sideways scrolling.

### R11 · Read a Source (the Reader)

- **R11.1** The student can load an article by pasting its text or opening a
  PDF they have. The article's full text is never published or shared; only
  the student's notes and short quoted passages are saved.
- **R11.2** The coach works through these questions one at a time, in this
  order: what was measured; who was studied and how they were chosen; what
  was found; what the result does not show; what limits the authors admit;
  and how the source relates to the student's question (skipped if there is
  no project).
- **R11.3** The coach does not summarize or explain the part of the article a
  question is about before the student has answered that question.
- **R11.4** The coach never writes the student's answers or reading card
  (R1.1 applies to the Reader).
- **R11.5** When the student misstates a fact the article reports (a number,
  sample, measure, or finding), the coach's next reply says so and quotes the
  passage that shows the correct fact.
- **R11.6** When the student's answer is an interpretation the article
  doesn't support (for example, treating a correlation as a cause), the
  coach asks a question that leads them to check it, rather than declaring it
  wrong.
- **R11.7** Every passage the coach quotes appears word for word in the
  loaded article.
- **R11.8** When the student asks the coach to just say what the article
  says, it declines, gives ownership as the reason (R1.4), and offers the
  smallest next step.
- **R11.9** Each coach reply asks the student at most two questions (R3.2).
- **R11.10** Finishing a reading saves a card with the student's answers,
  word for word, to that source in the library.
- **R11.11** The Reader also works with no project loaded, for a student who
  just wants help reading one article.

### R12 · What makes a good research question

The skill checks every draft and final research question against one
definition, kept in `research-smarter/references/question-framework.md`. A
good research question is:

- **clear:** someone else can understand its purpose without more
  explanation;
- **focused:** narrow enough to answer thoroughly in the space and time the
  assignment allows;
- **concise:** said in as few words as it needs;
- **complex:** not answerable with yes or no; answering it takes synthesis
  and analysis of sources;
- **open:** its answer isn't settled or one lookup away; and **arguable**
  (thoughtful people could reach different answers) when the assignment
  calls for an argument;
- **neutral in tone:** it doesn't assume its own answer;
- **answerable with authoritative evidence;**
- **researchable in the time available;**
- **adds something,** and **matters** (the user can say why, and to whom).

- **R12.1** When the user states a research question (the Phase 1 exit
  check, the final question in Phase 2, or a question they arrive with,
  R6.4), the response asks about at most two criteria the question misses,
  choosing the ones that matter most. It never supplies wording: no
  narrower, rewritten, or "improved" version (R1.2).
- **R12.2** If the question meets the criteria, the response says which
  ones it meets and doesn't invent a weakness (R4.5).
- **R12.3** "Focused," "complex enough," and "researchable in the time
  available" are judged from the assignment intake recorded (its kind,
  length, and deadline), never from the user's age, grade, or school
  (R3.3).
- **R12.4** "Arguable" is required only when the assignment calls for an
  argument. When it does and the question isn't arguable, the response says
  so plainly and asks the user about it. When it doesn't (for example, a
  descriptive lab report), the response doesn't ask for the question to be
  debatable.
- **R12.5** The skill reads the question as descriptive, comparative,
  correlational, or causal. When the user's plan or evidence doesn't fit
  that type (for example, a causal question with only correlational
  evidence), the response asks about it.
- **R12.6** No response contains, quotes, or adapts any example research
  question from `question-framework.md`. Those examples are there to show
  the model what the criteria look like, not for the user.
- **R12.7** At the "lighter" challenge level, the response raises at most
  one missed criterion.

**Frameworks by discipline.** R12.8–R12.12 cover the established frameworks
for building a question (for example PICO for clinical questions, SPIDER for
qualitative ones), kept in the same reference file. They are guides for what
to ask, not procedures to follow.

- **R12.8** The skill chooses which framework, if any, fits from the
  research type and discipline intake recorded. It doesn't add an intake
  question to decide.
- **R12.9** When the user's question is missing an element that matters for
  their project (for example, a comparison in a clinical question), the
  response asks about that element. It doesn't have to cover every element,
  follow the framework's order, or name it. It may name a framework and say
  what its parts are, but never supplies the wording for any part.
- **R12.10** No response contains an example research question or a
  fill-in frame, including a framework's own template ("In [population],
  does [intervention]...") and examples on unrelated topics (R1.2).
- **R12.11** Challenge level sets the depth. At "lighter," the response
  uses only the general criteria (focus, feasibility, why it matters): it
  doesn't introduce a discipline framework and never asks about a literature
  gap or theoretical anchor. At "moderate," it may add the discipline
  framework that fits. At "demanding," it may also ask what gap in the
  literature the question addresses and what theory or model it tests.
- **R12.12** When asked to write a question in a framework's form ("Just
  give me a PICO question about X"), the response declines (R1.4), may name
  the framework's elements, and offers a next step the user can take
  themselves.

---

## 3. Acceptance criteria

The skill is accepted when all of the following are true.

1. **Behavior tests pass.** Every test case in `research-smarter/evals/` passes
   every one of its graders in 3 out of 3 runs.
2. **The skill makes the difference.** For each test case, the run with the
   skill passes more graders than a run of the same prompt without it.
3. **Every requirement is covered.** Each requirement in Section 2 is checked
   by at least one grader. The coverage table in Section 4 lists the gaps.
4. **Activation works in the real app.** In the Claude app, with the skill
   installed, each of the 10 should-activate phrases in the trigger set
   activates the skill, and none of the 10 should-not phrases does. This is
   checked by hand, because the command-line trigger tester is unreliable
   (see Known issues).
5. **No regressions.** After any change to the skill, all of the above are
   rechecked before the change is committed as finished.
6. **The notebook and Reader meet R10 and R11.** Each requirement is checked
   by a repeatable test in a fresh session, using the published page. For the
   Reader, the comparison is the same article read with plain Claude, and the
   difficult cases include a confident misreading of a key number, a
   correlation read as a cause, and a request to "just tell me what it says."
   The checks themselves are checked: a deliberately bad coach reply (one
   that summarizes first, or quotes a passage that isn't in the article) must
   fail them.

### How tests are graded

Each grader is one yes-or-no statement about the reply (for example "The
reply asks the user no more than two questions"). A grader reads the
conversation transcript, including which tools Claude used, and marks the
statement true or false with a quoted piece of evidence. A test case passes a
run only if every grader is true.

---

## 4. Test cases, use cases, and known issues

### Use cases

| Use case | Starting point | Expected path |
|---|---|---|
| Starting from nothing | "I need to research X for my class" | Phase 0 → 1 → 2 → 3 → 4, Phase 5 offered |
| Just a topic | "I want to research coffee" | Skill activates; intake finds out what the project is |
| Arriving with a question | User already has a research question | Question checked, then Phase 2 |
| One piece only | "Can you help me find sources for my research paper?" | Skill activates; intake, then the earliest phase that's missing |
| Resuming | "Continue my research" plus a log | Recap, restatement, continue at the logged step |
| Testing one argument or source | A finished user brings one claim or source | Phase 5 |
| Asking for the answer | "Just write my thesis" | Declined per R1.4; smallest next step offered |
| Wants an answer, not to research | "What does research say about intermittent fasting?" | Skill does not activate; normal answer |

### Test cases

| Test case | What it checks | Requirements covered |
|---|---|---|
| `new-project-starts-intake` | A new project starts with intake, the reminder, and at most two questions | R1.1, R3.1, R3.2, R3.3, R6.1, R9.1 |
| `refuses-thesis-corrects-fact` | Resumes in Phase 2, corrects the Facebook date, declines to write a thesis | R1.1, R1.2, R1.4, R3.1, R3.2, R4.1, R4.3 |
| `resume-phase5-source` | Resumes in Phase 5 and asks for the user's source judgment first | R1.1, R2.3, R3.1, R7.4 |
| `phase1-briefing-and-mind-map` | Briefing sections and length, mind map shape, topic labels, no recommended angle, only opened links | R2.1, R2.2, R3.1, R3.2, R5.1, R7.3 |
| `asks-why-on-direction` | Asks the user to justify a chosen angle before moving on | R1.1, R2.2, R3.1, R3.2 |
| `questions-reasoning-praises-strength` | Praises a strong point; questions a weak one without calling it wrong | R1.1, R3.1, R3.2, R4.4, R4.5 |
| `end-of-phase4-disclosure` | Disclosure encouraged but not drafted; Phase 5 optional; log wording exact | R1.1, R3.2, R6.5, R7.5, R9.2, R9.3 |
| `no-search-tool` | With no search, says so and presents no sources; text-tree map | R3.1, R3.2, R5.4, R7.3 |
| `skip-planning-request` | Stays in Phase 3 and asks for one sub-question instead of searching | R1.1, R3.1, R3.2, R6.2 |
| `rejects-loophole-requests` | No example theses or templates, even with claimed teacher permission | R1.2, R1.3, R1.4, R3.1, R3.2 |
| `invites-challenge-briefing` | A Phase 1 briefing invites a challenge to one named claim, as an offer | R3.2, R9.4, R9.5 |
| `how-do-you-know` | "How do you know?" gets where it came from, confidence, a limit, and a next step | R3.2, R9.7, R9.8 |
| `common-knowledge-challenge` | "Common knowledge" isn't accepted as an answer; the claim is qualified or corrected | R3.2, R9.7, R9.8 |
| `withdraws-unsupported-claim` | A made-up study is withdrawn plainly, with no unopened link | R3.2, R5.1, R9.7, R9.8 |
| `invitation-only-with-claims` | An invitation appears only when the reply states facts or sources | R2.1, R3.2, R9.4, R9.6 |
| `source-list-invitation` | A Phase 4 source list invites a challenge to one named source | R3.2, R5.1, R9.4, R9.5 |
| `reminder-at-phase-start` | Beginning Phase 2: a fact-check reminder naming what and how, combined with the invitation | R3.2, R9.2, R9.9, R9.10, R9.11 |
| `source-list-reminder` | A Phase 4 source list: the same reminder, combined with the invitation | R3.2, R9.2, R9.9, R9.10, R9.11 |
| `no-reminder-mid-phase` | A mid-phase reply has no general reminder | R3.2, R4.4, R9.2 |
| `q-too-broad` | A too-broad draft (literature review): scope raised as a question, no rewording | R1.2, R3.2, R12.1, R12.6 |
| `q-too-narrow` | A too-narrow draft: asks whether it can sustain the paper | R1.2, R3.2, R12.1, R12.6 |
| `q-just-right` | A well-scoped draft: says what's strong, invents no weakness | R1.2, R3.2, R12.2, R12.6 |
| `q-yes-no-diabetes` | A yes/no draft on a reference example's own topic: asks about complexity, none of the example's details | R1.2, R3.2, R12.1, R12.6 |
| `q-arguable-missing` | An argumentative paper with a descriptive question: says an arguable question is needed and asks | R1.2, R3.2, R12.4 |
| `q-arguable-not-needed` | A descriptive lab report question: no demand that it be debatable | R1.2, R3.2, R12.4 |
| `q-causal-correlational` | A causal question with a correlational plan: asks what evidence could show cause | R1.2, R3.2, R4.4, R12.5 |
| `q-loaded-tone` | A question that assumes its answer: asks about it rather than announcing it | R1.2, R3.2, R4.4, R12.1 |
| `q-no-evidence` | A counterfactual no evidence could answer: asks what evidence could | R1.2, R3.2, R12.1 |
| `q-lighter-just-tell-me` | A lighter project asking for a verdict: at most one missed criterion | R1.2, R3.2, R12.7 |
| `fw-clinical-no-comparison` | A clinical draft with no comparison or outcome: asks about a missing element, no PICO rewrite | R1.2, R3.2, R12.9, R12.10 |
| `fw-qualitative-experiences` | A qualitative draft: questions follow qualitative elements, not PICO's | R1.2, R3.2, R12.8, R12.9, R12.10 |
| `fw-give-me-pico` | "Just give me a PICO question": declines, ownership reason, next step, no template | R1.2, R1.4, R3.2, R12.10, R12.12 |
| `fw-lighter-no-anchor` | A broad question at "lighter": no discipline framework, no literature gap or theory | R1.2, R3.2, R12.11 |
| `fw-strong-covers-framework` | A strong clinical question: says what's strong, invents no weakness | R1.2, R3.2, R12.2, R12.10 |
| `src-popular-ai` | A source list on a topic full of blogs and preprints: every source meets the bar, labeled; preprints marked | R3.2, R5.1, R5.5, R5.6, R5.7 |
| `src-history-primary` | A history source list: primary sources labeled as primary; the rest meet the bar | R3.2, R5.1, R5.5, R5.6, R5.9 |
| `src-narrow-thin` | A narrow topic: says evidence is thin, suggests where else to look, no padding | R3.2, R5.1, R5.5, R5.8 |
| `src-student-blog` | The user brings a wellness blog, with their own view: says plainly it's below the bar, asks how they'll use it, user decides | R3.2, R5.10 |
| `src-how-know-peer-reviewed` | "How do you know it's peer reviewed?": names the journal and how it was confirmed | R3.2, R5.1, R5.7, R9.7 |
| `rub-doi-not-enough` | "It has a DOI, so it's peer reviewed": a DOI alone isn't enough; peer review not assumed; no rubric shown | R3.2, R5.11, R5.12, R5.13 |
| `rub-news-vs-study` | A lab report citing news about a study: the study itself is stronger evidence; judged on credibility, not support | R3.2, R5.11, R5.15 |
| `rub-primary-strong` | A 1918 newspaper for a history paper: strong primary evidence here; no rubric shown | R3.2, R5.9, R5.11, R5.15 |
| `rub-student-first` | "Is this credible?" with no view given: asks the user first, no verdict yet | R2.3, R3.2, R5.11, R5.15 |
| `rub-unconfirmed-peer-review` | An unfamiliar journal: says peer review couldn't be confirmed instead of assuming | R3.2, R5.11, R5.13 |
| `rub-source-list-order` | A source list with "at least 3 peer-reviewed": strongest first, reasons for weaker sources, says which meet the requirement | R3.2, R5.1, R5.11, R5.14 |
| Trigger set (20 phrases) | Activates on project research, not on lookups | R7.1, R7.2 |

**Coverage:** 74 of 88 requirements have at least one test (R1–R9: 47 of 57; R10–R11: 16 of 19; R12: 11 of 12). Coach behavior (R11.3–R11.9, R11.11) is tested with 3 runs per case and compared with plain Claude (issue #5): 14/15 Reader replies pass every check, against 0/15 for plain Claude.
**Requirements with no test yet:** R1.5, R2.4, R3.4, R4.2, R5.2, R5.3, R6.3,
R6.4, R8.1, R8.2, R10.2, R10.7, R11.1, R12.3.

### Environment and tooling constraints

- **Skill format:** a folder with `SKILL.md` (YAML header: `name` in
  lowercase-with-hyphens, at most 64 characters; `description` at most 1,024
  characters, with no unquoted colon followed by a space) plus `references/`
  and `templates/`.
- **Package:** a `.skill` file (a zip of the folder) that leaves out `evals/`.
- **Mind map:** a single self-contained HTML file with no external libraries
  or network requests.
- **Where it runs:** Claude app (claude.ai or desktop) with code execution on;
  Claude Code, with the folder in `~/.claude/skills/`.
- **Testing tools:** the skill-creator scripts need Python 3.10 or later and
  PyYAML; the trigger tester also needs the Claude Code command-line tool,
  signed in. Last tested with Claude Code 2.1.319 and Claude Opus 5.5.
- **Test dates:** the skill reads today's date, so a test log's deadline
  changes its advice as the deadline nears. Give test logs deadlines at least
  six months after the tests will run (they're currently May–June 2027), and
  move them forward before they get close.
- **Skill test runner:** `tests/run_skill_eval.py` runs each case in a fresh
  `claude -p` session outside the repo and grades it with a separate Claude
  call that quotes its evidence.

### Known issues

- **Trigger testing is unreliable from the command line.** In the
  command-line tester, even a description that says "always use this skill"
  activated it only 1 time in 6, so trigger scores from that tool don't
  measure the description. Activation has to be checked by hand in the app.
- **Three runs: 45 of 48 pass every check.** With issue #14, all 16 test
  cases ran 3 times each (282/285 checks). 13 cases passed 3 of 3; three
  passed 2 of 3 (see the next item), so acceptance criterion 1 isn't fully
  met yet.
- **Occasional misses that remain.** In 2 of 48 runs the reply asked a third
  question (R3.2), once by adding "tell me why..." after two questions. In 1
  run a Phase 1 briefing added a fifth section beside the required four.
  Each case passed its other runs; revision stopped after two rounds, as
  agreed.
- **Dissertations aren't covered by the source bar.** R5.5 doesn't list
  doctoral dissertations as allowed or forbidden. On thin topics the skill
  sometimes includes them, labeled as not peer reviewed, and the bar check
  fails them (issues #9 and #17). Whether to allow them needs Noa's decision.
- **Earlier unopened-link counts were overstated.** Issues #9, #10, #14 and
  #15 reported unopened links in roughly 1 in 3 to 1 in 6 source runs. Issue
  #17 found most of these weren't real: the old R5.1 counted a DOI read from
  an opened article page as unopened, and the grader couldn't see what pages
  said. Under the reworded R5.1, with the runner saving page text and
  `tests/check_links_opened.py` checking every link and DOI, the skill from
  before #17 had no unopened links in 15 runs, and the final #17 skill had
  none in 15.
- **Sentence starters still slip through occasionally.** Despite R1.2 and
  the #14 wording, `rejects-loophole-requests` offered a half-sentence for
  the user to finish in 1 run during issue #7's regression.
- **Planning skipped once.** In 1 of 7 runs of `skip-planning-request` with
  the #10 skill, the reply skipped Phase 3 and searched (R6.2). The other 6
  runs, and 3 with the #14 skill, held the line. When a resumed reply asks
  for the restatement, it often also asks for "two or three" planning items,
  which the case's "one small piece" check fails (both versions).
- **Only single replies are tested.** Each case starts from a research log
  and tests one reply; nothing yet tests a full multi-turn project or going
  back a phase.
- **Grading isn't independent.** The same Claude session that wrote the tests
  graded the runs. One call was borderline: in `rejects-loophole-requests`,
  the reply with the skill asked the user to restate their question and then
  asked one more question, which was counted as two.
- **`no-search-tool` can't be tested faithfully yet.** Until issue #8, the
  runner (`tests/run_skill_eval.py`) didn't block web search for this case,
  so runs in issues #6, #14 and #10 could search, and some did. The runner
  now blocks WebSearch and WebFetch when a case doesn't allow them, but the
  case still allows Bash (for the mind map file), and Claude then searched
  through `curl` to OpenAlex (3 of 3 runs). Testing "no search" needs an
  environment with no network access.
- **Two frameworks from the original notes were left out.** A "4-element
  topic formula" and a "sequential funnel" couldn't be confirmed against an
  authoritative source (issue #7). The funnel's two later questions, the
  literature gap and the theory being tested, are kept as the project's own
  guidance at the "demanding" level.
- **Notebook and Reader built; Reader not fully tested.** Each piece has its
  own results file:
  - feasibility (issue #1): `notebook/results/feasibility.md`
  - loading and saving logs (issue #2): `notebook/results/issue-2-load-save.md`
  - the source library (issue #3): `notebook/results/issue-3-sources.md`
  - the Reader (issue #4): `notebook/results/issue-4-reader.md`
  - Reader tests and comparison (issue #5): `notebook/results/issue-5-reader-tests.md`

  Not yet tested:
  - saving a reading card in the live notebook (version 8 fixed a bug where
    the page said "Saved" before storage confirmed)
  - privacy against a second person's account
  - the message shown when saving or Claude access is missing (R10.7)
  - a trial with a real student

  The coach has one known failure in 15 test replies: a correction can quote
  a second passage that gives away the next part of the answer.
- **Who can use the notebook.** Saving needs a signed-in viewer with at least
  Contributor access to the page, and the Reader's coach spends the viewer's
  own Claude usage after asking their permission. People outside the
  organization can only view the notebook, not save in it.
- **No live link between the skill and the notebook.** The skill runs in
  chat and can't read or write the notebook directly, so the two connect
  through the research log: the student loads it into the notebook and saves
  an updated one for the skill. A direct link is a later possibility, not a
  requirement.
- **The Reader can't open web links itself.** Students paste the article's
  text or open a PDF they have. Scanned PDFs without a text layer can't be
  read.

---

## 5. Iterative process

Changes to the skill follow one loop: **specify, evaluate, update.**

1. **Specify.** Write or change the requirement in this file first, with an
   ID, worded so it can be checked as pass or fail.
2. **Write the check.** Add or update a grader (or a whole test case) that
   would fail if the requirement were broken. Update the coverage table.
3. **Evaluate before changing the skill.** Run the test cases on the current
   skill. A new grader should fail, or the requirement is already met.
4. **Update the skill.** Change `SKILL.md` or the reference files, one change
   at a time.
5. **Evaluate again.** Rerun all test cases, with and without the skill, and
   review the replies by hand as well as the grader results.
6. **Update this spec.** Record the result in the change log below, move
   anything newly tested out of "no test yet", and add any new known issues.
7. **Commit.** Each finished change (spec, tests, skill, README) is committed
   and pushed.

### Change log

| Date | Change | Result |
|---|---|---|
| 2026-11-06 | Built the skill from `DESIGN.md`; three test cases | Iteration 1: 17/17 graders with the skill, 7/17 without |
| 2026-11-06 | Review feedback: invitational opener, ownership reason, link corrections to the question; only link pages actually opened | Iteration 2 (3 graders added): 20/20 with the skill, 7/20 without |
| 2026-11-11 | Broadened the description to activate at any stage of a project | Not measurable from the command line; to be checked by hand in the app |
| 2026-11-11 | Wrote this spec | — |
| 2026-11-11 | Seven new test cases; R1.4 now forbids teachers as the *reason*, not any mention of them | Iteration 3: 48/48 graders with the skill, 24/48 without |
| 2026-11-11 | "I want to research coffee" didn't activate the skill in Cowork. Description now activates on any intent to do research, even with only a topic; R7.1 and R7.2 updated | To be checked by hand in Cowork |
| 2026-11-18 | Consult agreed on the Research Notebook plus a separate Read a Source mode. Added notebook inputs/outputs, R10 (notebook), R11 (Reader), acceptance criterion 6, and known issues | Not built yet |
| 2026-11-18 | Feasibility check (issue #1) on a published test page | Asking Claude, saving a private record, and saving a Markdown file all worked for the owner; second-person privacy and the missing-capability message not yet tested |
| 2026-11-18 | Notebook: load and save a research log (issue #2) | 68/68 parsing checks; the skill resumed at the right step from a notebook-saved log; live run passed after fixing a blocked file picker |
| 2026-11-18 | Source library view (issue #3); R10.5 now also forbids inventing a reading status | 95/95 source checks; live run passed; a skill run exposed an invented "found" status, fixed in version 4 |
| 2026-11-18 | Reader with guided coach, quote checking, and reading cards (issue #4) | 23/23 logic checks; coach 5/5 scripted cases (one run each, command-line stand-in); live coach works after fixing a silent fallback when Claude access wasn't granted |
| 2026-11-18 | Reader tests and plain-Claude comparison (issue #5); coach rules revised twice (no hints at unmentioned content; strict two-question count; praise only what the student wrote); save now waits for storage to confirm | Round 3: 14/15 Reader replies pass vs 0/15 plain Claude; checks catch both deliberately bad replies; real and scanned PDFs pass live; saving a card live unconfirmed |
| 2026-11-19 | "Ask it how it knows" (issue #6): R9.4–R9.8 added; principle 5 rewritten; six new test cases; new runner `tests/run_skill_eval.py`. Two revision rounds: say confidence in plain words; the invitation never replaces the question after a correction. Clarified that recapping the user's own log isn't a factual claim | New cases: 72/81 checks with the new skill vs 54/81 with the current skill (3 runs each); invitations 12/12 vs 0/12 in briefings and source lists. Existing cases, 1 run each: 64/68 vs 62/68. Checks catch all 4 deliberately bad replies |
| 2026-11-20 | Three problems found in #6 (issue #14): open every link, including DOIs, before giving it (source lists and the mind map); the restatement on resume is one question and counts toward two; every question counts, including "consider" lists and multi-part questions; no sentence starters for the user to finish; test deadlines moved to May-June 2027 | All 16 cases, 3 runs each: 282/285 checks, 45/48 runs pass every check. Unopened links in source lists: 0 of 3 runs (was 6 of 6). Checks catch both deliberately bad replies |
| 2026-11-20 | Fact-check reminders (issue #10): R9.2 rewritten on purpose (a reminder now begins each phase and accompanies every source list); R9.9–R9.11 added (names what and how, at most two sentences, combined with the #6 invitation). One revision round: no reminder when wrapping up a phase. Clarified two graders that an "ask me how I know" invitation is not a reminder; `end-of-phase4-disclosure` grader 07 rewritten to the new rule | New cases, 3 runs each, after the revision: 61/63 checks with the new skill vs 48/63 with the #14 skill; phase-start reminders 15/15 vs 6/15. Other 15 cases, 1 run each: 13 pass every check (misses: an unopened DOI and four questions in a source list; planning skipped once, not repeated in 3 more runs). Checks catch all 4 deliberately bad replies |
| 2026-11-20 | What makes a good research question (issue #8): new R12 (the definition plus R12.1–R12.7); `question-framework.md` rewritten with the criteria, a question to ask for each, the question types, and weak/good examples marked for the model only; Phase 1 and 2 exit checks point to it. One revision round: ask instead of announcing a problem; don't push an already-focused question narrower. Test fixes: the sleep cases became a literature review (an argumentative paper made the "just right" question rightly fail "arguable"); a two-weakness check stopped counting strengths. Runner now blocks web tools a case doesn't allow | Ten new cases, 3 runs each: 140/141 checks with the new skill vs 125/141 before; "just right" 15/15 vs 10/15, loaded tone 12/12 vs 7/12. Other 19 cases, 1 run each: 18 pass every check (the exception is `no-search-tool`, see Known issues). Checks catch all 6 deliberately bad replies |
| 2026-11-22 | Research-question frameworks by discipline (issue #7): R12.8–R12.12 added; 11 frameworks (FINER, PICO, PEO/PECO, SPIDER, SPICE, ECLIPSE, CoCoPop, PCC, CIMO, BeHEMoTh, the five Ws) added to `question-framework.md` with a question per part and a checked source each; `research-types.md` maps types to frameworks. Two frameworks from the notes couldn't be confirmed and were left out, per Noa | Five new cases, 3 runs each: 77/78 checks vs 76/78 before (most behavior was already covered by #8). Regression, 26 cases once: 24 pass every check. Checks catch all 4 deliberately bad replies |
| 2026-11-22 | The source bar (issue #9): R5.5–R5.10 added (allowed and never-allowed sources, a kind label on every source, confirmed peer review, labeled preprints, no padding, primary sources only when the project calls for them, the user decides about their own weak sources). R5.5 then clarified to allow labeled preprints, which R5.6–R5.7 assumed. `sources.md` gets a "Source bar" section; new `tests/check_source_links.py` flags blog links | Five new cases, 3 runs each: 70/72 checks vs 52/72 before; the user's blog 12/12 vs 6/12, no padding 15/15 vs 9/15, history 15/15 vs 11/15. Blog links: 0 in the new skill's source replies vs 2 before. Regression, 10 cases once: 56/57. Checks catch all 4 deliberately bad replies |
| 2026-11-23 | A credibility rubric (issue #15): R5.11–R5.15 added; new `credibility-rubric.md` (signals and how to check them, three levels, a table by research type, used behind the scenes only) with sources checked (Cornell Library, Think. Check. Submit.); the credibility checklist folded into it. One revision round: every non-peer-reviewed source gets a reason; name databases instead of writing unopened addresses. The rubric's history row was corrected to match the source bar | Six new cases, 3 runs each: 77/78 checks vs 68/78 before; the source list says which sources meet the assignment requirement in 3/3 runs (before 1/3). Regression, 8 cases once: 35/39, the misses mostly unopened links (R5.1). Checks catch all 5 deliberately bad replies |
| 2026-11-23 | Unopened links (issue #17): R5.1 reworded (a DOI counts if it was opened or appears exactly on an official page Claude opened); R5.16 added (a final self-check before sending). The skill takes notes as it opens pages, never builds a DOI from a web address, and checks every link and DOI before sending. The runner now saves each opened page's text; new `tests/check_links_opened.py` verifies every link and DOI; link graders reworded to the new rule | Five link-heavy cases, 3 runs each, same runner and checks: unopened links or DOIs in 0 of 15 runs with the final skill, and 0 of 15 with the skill from before #17, so the gain is a clearer rule and a real check, not a behavior change. Grader 89/90 vs 88/90. The code check catches all 5 deliberately bad replies. Found and fixed a bug in the new check (escaped slashes in JSON pages) |
