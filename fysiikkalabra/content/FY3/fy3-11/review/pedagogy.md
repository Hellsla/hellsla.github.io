VERDICT: PASS
CONTENT-HASH: fe26daef07ff0e1c

## Blocking
(none)

## Polish
1. inquiry.json pred-1 / exp-1 — the prediction is a calculation with a formula the student has not met yet, and the experiment's model computes ΔV = 2Q/5p, so Wₖ = pΔV is confirmed arithmetic rather than emergent. Add a one-line cue in the prompt ("työ on voima kertaa matka, kuten (s, F)-kuvaajassa") so a guess is an argument, and keep the Wₖ-not-shown readout (it makes the student act).
2. inquiry.json pred-2 / exp-2 — two return methods can refute Aino but cannot prove that no method avoids Q₂. Say once in the exp-2 question feedback or the reflect prompt: "Simulaatio näyttää kaksi tapaa; toinen pääsääntö kertoo, ettei mikään tapa onnistu."
3. inquiry.json `suunnittele` — two simultaneous equations with η and a lämpökerroin, plus `siirto`, 12 exercises, 3 checks and exit ticket after 8 earlier activities: a long hour. Consider dropping `siirto` (L3-02 covers the heat pump) or making `suunnittele` optional.
4. sim energy bars after a cycle ("W + Q₂", one bar, orange 15 % and blue) — W and Q₂ differ by colour only, and the W segment is thin. The letters are colour-coded, but add a thin divider line or the value inside the segment.
5. lesson.md line 116 — "Kiertoprosesseja ei tällä kurssilla lasketa" sits beside exp-2, which computes W = (p₁ − p₂)ΔV; the slot says kiertoprosessit are not central. Keep as an idea only, and do not add more cycle calculation.

## Checked
- Learning path: hook → retrieval of ΔU = Q + W (sign flip to Wₖ explained in the feedback) → p ΔV → cycle needs Q₂ → η → yhteistuotanto, heat pump. The opening question is answered in the text and the reflect stage.
- Sim legibility (measured with Playwright at 360, 390, 768, 1280): KaTeX canvas labels 10.5–12.4 px rendered, none under 10 px; at 360 px (294 px canvas) the labels are small but readable.
- No overlaps in the sim in the heating phase (mode B) or after the cycle at 360 and 1280 px (graph, shelf weights, bars, "kierros" label). The readout wraps cleanly; Käyttöohje, Mallin oletukset and Laskennan selitys are closed boxes; the visible lead is under 30 words.
- Lab at 1280 px: the sim sits beside the experiments, nothing clipped. At 390 px each experiment carries the sim after its intro, and the locked controls show "(vako)".
- Figures 1–4 are legible, each placed right after its paragraph; widths are to scale and colour is paired with labels and hatching.
- Example is staged in 5 steps, symbolic first; it does not repeat the exercises. Exercise levels 5/4/3, with meaningful distractor feedback.
- Finnish checked in the lesson, inquiry and exit ticket: no errors found; case endings after number and unit are right (200 kPa:na, 45 kW:n teholla).
- Premature disclosure: option feedback refers to the experiment's values only after the commitment.
- Content hash unchanged at the end.
