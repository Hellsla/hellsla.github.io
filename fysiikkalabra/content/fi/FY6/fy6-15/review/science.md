VERDICT: PASS
CONTENT-HASH: a362da4bacf76398
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- Suojamaadoitus (lesson, summary, inquiry explain model and criterion, figure maadoitus aria-label and figures.py): in the TN system the fault current returns through the protective conductor to the supply; fuse or MCB trips; RCD may also trip; scope stated as the TN system. Correct; the person-to-earth path without PE is also right (returns via the supply earthing).
- Maallikon sähkötyöt (lesson, summary, exit ticket): fixed installations for professionals; laypeople only specifically permitted minor work and only if they can do it safely; examples within Tukes's list; uncertain cases to a professional.
- P = UI condition (in-phase / power factor ≈ 1, active power depends on phase in general); 230 · 10 = 2300 W, 230 · 16 = 3680 W recomputed.
- Lint: no physics warnings.
- Round 3 (hash 17a65fd2157d29ea): layman paragraph and summary bullet checked against the Tukes list the teacher pasted; FAIL because "yksivaiheisen" was missing from the cord examples.
- Round 4 (git diff HEAD, hash a362da4bacf76398): lesson.md:461 now says "yksivaiheisen jatkojohdon korjaaminen, sähkölaitteen rikkoutuneen yksivaiheisen liitäntäjohdon ja pistotulpan vaihtaminen"; the exit ticket says "korjata yksivaiheisen jatkojohdon"; the summary bullet (line 578) says "varsinaiset sähköasennustyöt kuuluvat sähköalan ammattilaisille", matching the paragraph. Every example is now on the Tukes list with its condition; Blocking resolved.
