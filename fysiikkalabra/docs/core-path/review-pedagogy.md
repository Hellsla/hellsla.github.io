VERDICT: PASS

Pedagogy review of the module-level core path selection for FY1–FY8. This review stands in for re-reviewing each exercise set whose only change is a `"core": true` mark (reviews.py carry category `core-mark`). Checked against Lauri's brief of 2026-11-05.

The first pass covered FY1, FY2, FY3, FY4, FY6 and FY7. A second pass added FY8 (all 16 chapters, with the bank extended to 20 exercises per chapter) and FY5 (13 of 17 chapters).

The verdict does not cover fy5-5–fy5-8 yet. Their bank PR (#314) is still open and they carry no marks, so they still fall back to the default first two of levels 1 and 2. That makes their core calculations only (`core_path.py` lists them as the only calculation-only chapters left in FY1–FY8). Review these four chapters when they are marked.

## Blocking

None. I found no chapter whose core set clearly mismatches its learning goals or the brief:

- Every chapter has 4 core exercises (fy6-13 has 5, with a stated reason, and fy7-15 is the rework discussed below).
- All marked exercises are level 1–2 and already existed. No content was changed.
- No chapter's core is calculations only. Written reasoning, self-drawn graphs and investigation or data tasks are chosen where the goals ask for them. Force diagrams are core in the FY4 chapters whose goals name them (4–6, 13, 14, 16).
- The marking is the same everywhere: `"core": true` on an exercise or a non-optional lesson task, rendered with the same "Ydintehtävä" tag (build.py `exercise_html`, inquiry.py `act`).
- The fi, en and fi-easy files mark the same ids in all 80 chapters of the first pass and in all 33 chapters of FY5 and FY8. fy5-5–fy5-8 have no marks in any language.
- **FY5** (13 marked chapters): 4 core exercises per chapter, 5 in fy5-15 (with a stated reason). Force diagrams are core in fy5-4, the chapter whose goals name them: L2-01 and the error task L2-07, both with `fbd`. In fy5-2 the force-diagram goal is carried by the required lesson task *piirra* (explain, draw). fy5-11 has one calculation and three reasoning tasks, which suits its qualitative goals. FFT, beats and spectra in fy5-14 are covered by L2-06 together with the required lesson tasks *spektri*, *fft* and *huojunta-kuvaaja*.
- **FY8**: 4 core exercises in every chapter, none of them calculations only. Self-drawn or read graphs are chosen where a constant comes from a slope or a graph: fy8-1 (Planck), fy8-4 (Compton), fy8-6 (LED threshold, L2-05), fy8-8 (gamma calibration), fy8-12 (half-value thickness) and fy8-16 (Hubble). Chapters with explaining or classifying goals (fy8-11, fy8-14, fy8-15) have one plain calculation each, with reasoning and error-finding tasks in place of the rest.

**fy7-15 is enough.** The basic path leaves out Malus's and Brewster's laws (the theory box and the whole of level 2 are deepening content). So L1-01 (half the intensity through one polariser) and L1-06 (why polarised sunglasses cut glare) are the only level 1–2 exercises that fit the basic path. Explicit `"core": false` on L2-01 and L2-02 stops the default first-two rule from putting Malus calculations on the core path. The three marked lesson tasks cover the other goals:
- *johtopaatos*, together with the non-optional koe-1 and *mittaus*, covers goal 2 (one, two or three polarisers).
- *siirto-3d* and *tarkistus-3* cover goal 3 (glare, screens, 3D glasses).
- Goal 1 (transverse wave) is covered by the non-optional check-1.

That gives 2 exercises plus 3 written lesson outputs, about the same workload as the 4-exercise chapters and better matched to the goals.

## Polish

All optional. Each item swaps one existing exercise or adds a mark to an existing task, and none of them changes the verdict.

**Across modules: when a lesson task gets the mark.** FY1 and FY2 mark a lesson task when a goal is not covered by any core exercise (fy1-8 *suunnittele*, fy2-8 *perustele*), "so that it looks as important as the calculations". FY3, FY4, FY6 and FY7 mark no lesson tasks, on the grounds that non-optional lesson steps are already on the core path. Those steps get no tag in the page, though, and some chapters lean on them for a whole goal. Choose one rule. If "mark the lesson task that alone covers a goal" is the rule, these candidates fit it (all non-optional and of a type that may carry `core`):
- fy1-1 *vuorovaikutukset* (choice). It is the only task for the goal "tunnistamaan neljä perusvuorovaikutusta".
- fy3-3 *check-1* (choice, micro model). No core exercise covers "selittämään mikromallilla". *check-3* would fit better, but it is optional, so it cannot be marked without a content change.
- fy4-2 *putoaminen* (interpret). It is the only task for "sovittamalla toisen asteen polynomin".
- fy4-16 *piirra* (explain, draw). FY4.md names it as the spring-balance force diagram.

**Per chapter**

*Applied since the first pass:* fy1-1 L1-01→L1-04, fy3-1 L1-01→L1-07 and fy3-3 L1-01→L1-08 (FY1.md and FY3.md updated), and the `"core": false` note in FY7.md. I checked the new ids. They are the same in fi, en and fi-easy. The items below are kept for the record.

- **fy1-1** (applied): swap L1-01 (red blood cell in µm, a plain unit conversion that L2-01 and fy1-2 also practise) for L1-04 (atom and nucleus diameters). L1-04 practises powers of ten too, and it also touches the goal "aineen rakenne molekyyleistä kvarkkeihin", which no core exercise covers now.
- **fy2-8**: L2-05 (Mauna Loa CO₂ trend as a linear model) fits only loosely under "selittämään kasvihuoneilmiön … fossiilisten polttoaineiden polttaminen voimistaa sitä". It can stay as the chapter's data task. If a closer match is wanted, L2-07 (an error in the emission units) targets the calculation goal directly. That would leave the investigation skill to the lesson's *aineisto* task.
- **fy3-1** (applied): swap L1-01 (weight on Earth) for L1-07 (which bodies' interaction the weight G describes). L2-03 already practises the weight calculation, and L1-07 covers the first goal, "voima on vuorovaikutuksen voimakkuuden mitta", which has no core exercise now.
- **fy3-3** (applied, by the L1-08 swap): all three goals are conceptual, but three of the four core exercises are kelvin calculations (L1-01, L2-02, L2-04). Either mark lesson *check-1* (see above), or swap L1-01 for L1-08 (rigid vessel heated: which state variable stays the same). L2-04 still keeps the kelvin-ratio goal.
- **fy3-1 and fy3-9**: no swap needed. L2-05 in fy3-1 ("piirrä pisteet (m, G)-koordinaatistoon, sovita suora") and L2-03 in fy3-9 (a (1/V, p) straight line from measurements) are graph tasks. They have no `graph` in `kind`, so `core_path.py` counts them as *tutkimus* or *lasku* and understates FY3's graph count (2). Adding `"graph"` to their `kind` would make the report accurate. That is a metadata change, not a core-mark change.
- **fy4-15**: both core calculations are hydro power (L1-01, L2-04). The wind-power calculation appears only inside the error task L2-07. If an explicit wind calculation is wanted for the goal "vesi- ja tuulivoimalan tehon …", swap L2-04 for L1-04 (wind power ½ρAv³).
- **fy6-10**: the goal "kuvailemaan pistevarauksen sähkökenttää kenttäviivojen avulla" has no task at all in this chapter. There is no level 1–2 exercise, and the lesson mentions field lines only in the simulation and theory text. FY6.md says the goal "jää oppitunnin varaan", but the lesson has no field-line task either. This cannot be fixed with a core mark. Either note it as a content gap for the exercise bank, or point to fy6-11 L1-06 (field-line density), which comes in the next chapter.
- **fy2-4**: as FY2.md already says, the goal "lukemaan energiavirtakuviota" has only L3-03 and no lesson task. This is the same kind of content gap as fy6-10. Note it for the exercise bank.
- **fy7-15** (applied): the explicit `"core": false` on L2-01 and L2-02 is the only use of `false` in the repository. It is correct and needed (see Blocking), and it is now documented in FY7.md.
- **fy8-16** (fix the rationale): FY8.md says "Alkuaineiden syntyä käsitellään oppitunnin johtopäätöksessä". It isn't. *johtopaatos* asks only about the Hubble graph, H₀ and 1/H₀. The only task on element synthesis is *tarkistus-3* (the origin of gold, using the binding-energy curve), and it is `optional`. As things stand, the goal "selittämään, missä vaiheissa vety, helium ja raskaammat alkuaineet syntyivät" is not on the core path. Either correct the sentence in FY8.md to name the gap, or do an fy7-15-style rework: make *tarkistus-3* required and mark it `"core": true`. The rework is a content change, not a core mark, so it needs its own review.
- **fy8-3**: the goal "arvioimaan Bohrin mallin onnistumisia ja puutteita" has no level 1–2 exercise. Its only task is the optional *tarkistus-3* (what the Bohr model got right and why it was abandoned). This is the same kind of gap as fy8-16, and the same two options apply. FY8.md does not mention it.
- **fy5-14**: optionally swap L1-03 (third overtone) for L1-05 (classify infrasound, audible sound and ultrasound). The infra/ultra classification in goal 1 has no core task, while the harmonic series is also met in L2-06's FFT spectra. Keep L1-03 if the calculation weighs more.
- **fy5-2**: the goal "laskemaan tukivoimia voimakuvion … avulla" has no core exercise with `fbd` (the chapter's bank has none at levels 1–2). It is carried by the required lesson task *piirra* (explain, draw). This is a candidate for the lesson-mark rule above.
- **fy5-5–fy5-8**: select and review once PR #314 is merged. Their goals call for a graph and a sine fit (fy5-7) and for a spring constant from a slope (fy5-8). The current default core does neither.

## Checked

- Read `docs/core-path/summary.md` and the rationale in FY1.md–FY8.md.
- Ran `python scripts/core_path.py` (the summary) and `python scripts/core_path.py FY1 … FY7` (per chapter) for all six modules. Compared the goals with the core exercises and the lesson's core tasks chapter by chapter.
- Read the level 1–2 exercise text and `kind` in `content/fi/<FY>/<id>/exercises/exercises.json` for 26 chapters:
  - FY1: fy1-1, fy1-2, fy1-4, fy1-8
  - FY2: fy2-3, fy2-4, fy2-8
  - FY3: fy3-1, fy3-3, fy3-9, fy3-11, fy3-13
  - FY4: fy4-2, fy4-3, fy4-12, fy4-15, fy4-16 (fy4-4, 4-5, 4-6, 4-13 and 4-14 through the report's force-diagram tags)
  - FY6: fy6-1, fy6-5, fy6-10, fy6-11, fy6-16
  - FY7: fy7-1, fy7-5, fy7-7, fy7-15
- Second pass: ran `python scripts/core_path.py FY5` and `FY8` and the summary. Read the level 1–2 exercise text in 12 chapters:
  - FY5: fy5-2, fy5-4, fy5-11, fy5-14
  - FY8: fy8-3, fy8-5, fy8-6, fy8-9, fy8-11, fy8-14, fy8-15, fy8-16
  - Also read the lesson activities of fy8-3 and fy8-16.
  - Re-read the core ids of fy1-1, fy3-1 and fy3-3 after the swaps.
- Ran the same consistency script over FY5 and FY8 (33 chapters): fi, en and fi-easy core ids match, every mark is in level 1 or 2, and the count is 4 except fy5-15 (5) and fy5-5–fy5-8 (0, unmarked). No `inquiry.json` in FY5 or FY8 carries `core`. The first-pass check still passes on all 80 chapters after the swaps.
- Read the lesson activities (`inquiry.json`, including the `optional` flags) for fy1-1, fy1-2, fy1-8, fy2-4, fy2-8, fy3-3, fy6-10 and fy7-15.
- Ran a script over all 80 chapters of the six modules. It confirmed that:
  - the ordered list of core ids in fi equals the list in en and in fi-easy;
  - every marked exercise is in level 1 or 2;
  - the count is 4 in each chapter, except fy6-13 (5) and fy7-15 (2).
- Ran `grep -c '"core": true'` on `inquiry.json` and `exercises.json` for fy1-8, fy2-8 and fy7-15 in fi, en and fi-easy. The counts match (1/4, 1/4, 3/2). Marked lesson tasks exist only in these three chapters.
- Checked that marked lesson tasks are non-optional and of a type that may carry the mark (inquiry.py `CORE_TYPES`). Checked that build.py and inquiry.py render exercises and lesson tasks with the same core tag.
- Checked the brief's point that a written or graphical core task needs no numeric check field. No selection was skipped or bent for lack of one.
