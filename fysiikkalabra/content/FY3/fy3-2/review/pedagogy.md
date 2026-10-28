VERDICT: PASS
CONTENT-HASH: a0884c77f1e7ec8a

## Blocking
(none)

## Polish
1. sim.js canvas (fy3-2-sim-390.png) — at 366 px the KaTeX tick labels ("0 m, 5 m, 10 m, 15 m, 20 m", "10,0", "0 J", "600 J", "F (N)") render at roughly 8-9 px, noticeably smaller than the readout under the canvas; legible but strained, and the 5 m–20 m ticks sit close together. Raise the canvas label size on narrow widths, or drop the 5 m and 15 m ticks on a phone. No overlaps at 390 or 1280 px.
2. sim readout — "Tehty työ tähän mennessä: 0 J, aikaa kulunut 0,0 s" and the labels "Nopeus" and "Vedä" are plain text while the rest is KaTeX; the numbers inside are KaTeX but the sentence is not. Fine for readability, but it is not the "kaikki latexilla" the teacher asked for; the mix of KaTeX serif numbers and sans words in one line looks slightly uneven.
3. inquiry.json pred-2, third option — feedback says "mittausten mukaan", while the rest of the lesson calls the sim's numbers "mallin arvot" (the lesson rule: model values vs. measurements). Change to "mallin arvojen mukaan".
4. exp-1 / exp-2 — the sim computes W = Fs and P = W/t directly, so the experiments confirm the formula's arithmetic rather than letting a result emerge. They can still refute a wrong prediction, so acceptable; the Joule table carries the real empirical content. Also exp-1 intro at 390 px wraps with a stray line start (". Muutetaan: s.") after "Vakiona: F, t".
5. Finnish/exercises — fy3-2-L3-01 "voiman matkan suhteen keskimääräinen suuruus" is clumsy: "voiman keskiarvo matkan suhteen (matkan yli keskiarvoistettuna)". L3-02 answer shown as 590 J while the solution gives 588,6 J (three s.f. would be 589 J); tolerance covers it.

## Checked
- Learning path: hook, retrieval of G = mg, three predictions, sim, Joule table, theory, example, error spotting, transfer; the opening question is answered in Ydinajatus and revisited in reflect. Slot goals (W = Fs, Joule, graphical integration) covered; no FY4 content (no E_k, E_p, cos α).
- Predictions 1 and 2 are refutable by exp-1 and exp-2 (revealed after min 2); pred-3 is argued from the figure, and the prompt says openly that the sim does not test it. Wrong-option feedback repairs the misconception without disclosing the answer early.
- Sim at 390 and 1280 px: picture, controls, readout understandable; locked sliders show "(vakio)"; Käyttöohje and Mallin oletukset closed; no Laskennan selitys box, which is fine since there is no computation beyond W = Fs.
- 1280 px lab: sim beside the experiments, readable, no clipping.
- Figures (fig-3, example graph): clean, colour plus labels and hatching, legible on a phone.
- Worked example: five stages, symbolic first, units on substitution, sanity check by average force.
- Exercise levels 5/4/3 per rubric; none repeats the spring example; exit ticket tests carrying (W = 0), area and work, work vs. power.
- Workload is on the heavy side (3 predictions, 2 experiments, 12 exercises, 3 checks) but fits one lesson.
- Finnish and glossary terms (työ, teho, joule, energia) correct; case forms after number+unit correct.
