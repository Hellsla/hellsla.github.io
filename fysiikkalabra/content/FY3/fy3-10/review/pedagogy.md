VERDICT: FAIL
CONTENT-HASH: 58242d5b3c115dce

## Blocking
- exit-ticket.json (q 1-3 and all three answers) — symbols are plain text, not maths: "R = 8,31 J/(mol·K)", "n = pV/(RT)", "T = (27 + 273,15) K", "p = nRT/V", "T:hen", "p on verrannollinen T:hen"; the 390 px capture shows upright text, against the rule "symbols in prose as maths" and "solutions in LaTeX" — write them as $n$, $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$, $n = \dfrac{pV}{RT}$, "lämpötilaan $T$" etc.
- inquiry.json exp-1/exp-2 (intro, "Alkutila:", "Vakiona:"), check-2 prompt, sim text in lesson.md ("N = 50, 100 ja 200", "N = 100, T = 300 K, V = 100 %") — the quantities N, T, V are plain text while neighbouring items use $N$, $T$; the page mixes italic maths and upright letters for the same symbol (captures tutki-1280, ennusta-390) — put every quantity symbol in $...$ (the "Alkutila/Vakiona" line is generated: fix in the template or via names).

## Polish
- lesson.md Esimerkki — the example recomputes the helium balloon already worked in Ydinajatus (0,83 g, 0,207 mol), so it adds nothing new; use another gas or ask for pressure or volume.
- fig-3 (paine-ja-tekijat) at 360-390 px — labels "N, T, V" and "2T" are about 10 px; enlarge the figure text or give the four panels more width on phones.
- inquiry.json punnitus — "Mooli on aina sama, tietty hiukkasmäärä" comes before the student knows the term; "Mooli on tietty hiukkasmäärä (6,022 · 10²³), ja moolimassa $M$ on yhden moolin massa" reads better.
- solutions.md L2-01 Järkevyys — the sentence "tulos on arvio (tehtävä pyysi ideaalikaasun arvoa, ...)" is muddled; say plainly: "Ideaalikaasumallin antama arvo; todellinen paine on muutaman prosentin pienempi."
- exp-1 intro is long (about 90 words) for a half-width column; move the "Nollaa mittaus" instructions into a short list.

## Checked
- Figures 1-3 (390 px): labels in LaTeX type, print-clean, uncluttered; colour paired with text, bars in fig 2 to scale; the speed ratio 2,7 : 1 = $\sqrt{29/4}$ is correct.
- New theory figures answer the opening question and p ∝ NT/V where they sit in the text.
- Learning path: hook, retrieval, prediction, weighing, simulation, experiments, theory, example, exercises; slot goals met, one lesson's workload.
- Chapter names used instead of lesson ids; exit ticket headed "Exit ticket".
- Numbers rechecked: m/M, R ≈ 8,3, example, balloon (2640 kg), exercise answers and solutions agree.
- Experiments can refute their predictions (pressure emerges from counted hits; exp-2 forces p ∝ NT); table pV/(NT) arithmetic is right.
- Sim at 390 and 1280 px: controls and readout legible, wide layout puts the sim beside the experiments.
- Finnish: grammar and case endings fine; glossary terms used.
- Exercises L1-L3 solutions are in LaTeX, symbolic first, with Järkevyys.
