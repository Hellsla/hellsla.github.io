VERDICT: FAIL
CONTENT-HASH: d976b4674d500fd0

## Blocking
- inquiry.json:113 (exp-2 question, student-visible) — "Oppitunnilla fy3-8 ilman tilavuuden lämpötilakertoimeksi annettiin ..." names a lesson code; the owner's rule is to say the chapter, not the lesson id — fix: "Luvussa Lämpölaajeneminen ilman tilavuuden lämpötilakertoimeksi annettiin ...". Check the other student-visible text for lesson ids too; "Kertaa paineen tunnilta" (kertaus title) is fine but could name the chapter "Paine ja hydrostaattinen paine".

## Polish
- Figures 2-4 (lesson.md svg, captures fig-2..4): labels are plain upright text ("V ja p", "V/2 ja 2p", axis "p", "V", "1/V", "jatke", "273"); the owner's rule is LaTeX for all figure notations, so use italic/math symbols (p, V, T, 1/V) and "T = const" rather than "T vakio". The same applies to the simulation's own canvas text ("V = 50,0 ml", axis titles). Fig 4 also marks only 273 K although the points run to 373 K; add a 373 tick.
- inquiry.json sim "calc"/pred-3: the simulation's pressure comes from pV/T = vakio, and the lesson says so honestly; the collision flashes are decoration. The ruisku interpret item (noisy data, one row heated) is the only item where evidence can surprise the student. Acceptable, but a one-line pointer from exp-1 to that item ("oikeassa kokeessa pisteet eivät osu täsmälleen") would make the model/measurement gap visible.
- Workload: three predictions, two experiments, an interpret item, a reflection, an error-spotting item, a transfer task, exercises, three checks and the exit ticket is close to the limit of one lesson; the isobaric/isochoric half (pred-2, exp-2) could be trimmed if testing shows overrun.
- lesson.md: "Kireässä pussissa ilman paine pysyy hieman matkustamon painetta suurempana" is correct but abrupt; add "koska pussin kalvo kiristyy" so the cause of the hard bag is stated.

## Checked
- Opening question (bag swelling) is answered in Ydinajatus, in the example (0,80 l to 1,0 l) and in the reflection.
- Prediction options each repair a misconception; wrong options do not disclose the answer before commitment; pred-3 and exp-1 (min 3) can refute the prediction in the model.
- Round-1 blocker (feedback claiming measurements from a formula sim) is fixed: feedback now says "Mallin arvot".
- Worked example: five stages, one step each, units and sanity check; no exercise repeats it.
- Exercise numbers verified (L1-01..05, L2-01..04, L3-01..03, check-2, siirto, ruisku table pV values 5040/5430): consistent with answers; levels progress one idea to two.
- Exit ticket tests the core ideas (Boyle, 1/V graph, kelvin).
- Figures at 390 px legible, uncluttered, colour not the only cue; fig 3 shows curve vs line well.
- Simulation at 390 and 1280 px: controls and readout readable, nothing clipped; layout beside experiments works at 1280.
- Finnish reads at a 17-year-old's level; case after number+unit correct in checked text.
- Hash unchanged at start and end.
