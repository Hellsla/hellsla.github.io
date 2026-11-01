VERDICT: FAIL
CONTENT-HASH: 03667762f34381de

Pedagogy review of fy14-iter-media (2026-11-01) against the brief's assignment *ITER: Promise, Progress and Reality*. Tested in Playwright over HTTP at 390 px:
- both predictions lock on commit with no feedback and open at `theory-thennow`;
- all 6 model answers stay closed until the student writes;
- no console errors.

The brief is covered:
- an article chosen and read (HS 2018, with two verified Yle alternatives);
- a writing task of about 300 words on all six content points, with seven observable criteria and a 301-word model;
- a comparison between historical reporting and verified current information (`compare`, point 5, the *Then and now* table).

## Blocking
1. **`pred-2018` gives its answer in the options and repeats a question the student has already answered twice.**
   - "2025, **in the plan of 2016**" against "2034, the same as today's plan" tells the student which plan was valid in 2018.
   - fy14-iter-project (`pred-schedule`, `check-3`) and fy14-iter-video (`pred-date`) have already asked for the same old-plan-against-2024-baseline fact.
   - Fix: replace it with a prediction the student can argue about and that the article and the table reveal. For example: "The Yle article of 2005 made several statements about the future (site, jobs, start of operation). How many of them do you think still hold in 2026?" Or: "Which will a 2018 article most likely get wrong: the goal, the physics, the Members or the schedule?" That second question is close to `pred-change`, so then merge the two predictions into one.
   - If 2025 stays, list bare years only.

## Polish
2. `notes`: the model shows notes on the Yle 2020 article. A student who reads that article can write one word and copy them. Show the model as a *format* (for example, two headings filled in) rather than the full content, or show it only after the `compare` task.
3. `claims` covers only the Yle articles. Students who read HS 2018 sort statements they have not read. Say in the prompt "even if you read HS, sort these Yle statements: they train the same skill".
4. Workload: reading a long Finnish multimedia story, taking notes under six headings and writing 300 words in English in one 75-minute lesson is a lot. `teacher.md` plans to finish the writing at home. State this on the page in the writing task as well ("start in class, finish at home"), so that students do not try to do everything in the lesson.

## Checked
- The hook, the Why line and the hero do not give the answer to `pred-change`.
- Word bank and sentence starters for the notes, the pair task, the writing, the peer feedback and the correction note.
- The pair discussion is set up across articles.
- Checks 1–3 target real misconceptions (plan vs result, newest primary source, fuel scarcity vs Coulomb barrier). Options are balanced.
- The French corner is present.
- `teacher.md` is honest that HS 2018 could not be read and gives the teacher a scoring scale.

## Shared issues
- None new.
