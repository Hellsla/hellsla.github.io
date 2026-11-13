VERDICT: PASS
CONTENT-HASH: eed3551ade27dd66

## Blocking

## Polish
- lesson.md:94 / inquiry.json check-1 (line 452 on) — with the √10 sentence gone, the lesson defines suuruusluokka only as "lähinnä kymmenpotenssien akselilla". Its two examples (1,7 → 10⁰, 8,8·10³ → 10⁴) cannot tell the log-axis nearest from the linear nearest. check-1 (4,0·10¹⁶ → 10¹⁷) needs the log reading, and the threshold "yli noin 3" now appears only in that feedback and in the glossary. This is not an error: the definition is correct and the Ydinajatus axis figure is logarithmic and to scale. Optional fix: add an example with a coefficient between 3 and 10 that rounds up (e.g. 4·10ⁿ → 10ⁿ⁺¹), or a clause saying the axis is the one in the figure, so a student can answer check-1 from the theory alone.
- lesson.md (Sgr A*) — the text gives "noin neljä miljoonaa", the sim's Mallin oletukset 4,3 miljoonaa. They agree as rounded values. (Carried from the previous report.)

## Checked
- Diff 9e7b1d7fb8 (fi lesson.md:94): the removed rule (a < √10 → 10ⁿ) and the remaining definition are the same thing (nearest on a log axis). Both examples are right: log₁₀ 1,7 = 0,23 → 10⁰ and log₁₀ 8 800 = 3,94 → 10⁴.
- The rule is still the same everywhere: the glossary ("alle/yli noin 3"), check-1's options and feedback (log₁₀ 4,0·10¹⁶ = 16,60 → 10¹⁷), the Tiivistelmä ("lähin kymmenpotenssi") and the sim's kohdeExp = round(log₁₀ m).
- The sim and the experiments, recomputed: mainObj with the −log₁₀(560/150) offset gives water / Earth / universe at L = −9 / 7,7 / 27,5. kohdeExp is atom −10, proton −15, Neptune 13, Milky Way 21, Planck −35, universe 27 and hair −4, so the exp-1 answer is 5, the exp-2 answer 8 and the exp-3 answer −4.
- Recomputed in one script: example k = 6,47·10⁴ (Δn = 5), check-2 5,79·10⁴, siirto d = 12 732 km (C 40 000, r 6 366, 111 km/°). All match inquiry.json and lesson-answers.py.
- Magnitudes: Sgr A* horizon 2,54·10¹⁰ m from 4,3·10⁶ M☉; 93 Gly = 8,80·10²⁶ m; light-year 9,46·10¹⁵ m; Proxima 4,0·10¹⁶ m; e/g force ratio for two protons 1,2·10³⁶; neutron star 20–25 km; heliopause about 120 AU; Oort cloud 2 000–100 000 AU.
- Every choice item has exactly one correct option, and its distractors' feedback is right (pred-1, pred-2, exp-2, menetelmat, tunnista, vuorovaikutukset, virhe, check-1, check-c2).
- The four interactions are right: residual strong force, β⁻ by the weak force, charge neutrality as the reason gravity dominates at large scales. The text stays within the FY1 scope note.
- The check-3 model answer (31 decades) and the exit ticket agree with the theory.
- The simulation's limits are stated in Mallin oletukset (rounded sizes, nucleus drawn too large, orbit radius labelled, horizon not a surface).
- The hash was the same at the start and at the end.
