VERDICT: PASS
CONTENT-HASH: a2773c26ca9d21a4

## Blocking

## Polish
- lesson.md Ydinajatus, 2nd paragraph (Lämpövoimakone muuttaa…) — about 140 words, over the ~120-word guide, and a long run of text on the phone; the 1st (~125) and the hyötysuhde paragraph (~120) are borderline too — split after "…yhteensä." and before "Mitä suurempi on…".
- lesson.md Kaava — lämpökerroin and the heat-pump balance have no display formula, yet the sim and L3-02 use them; add `\varepsilon = Q_\text{sisälle}/W` (and `Q_\text{sisälle} = Q_\text{ulko} + W`) with symbols named, so "enemmän lämpöä kuin sähköä" is shown once in LaTeX.
- lesson.md Ydinajatus — the heat-pump paragraph is the only part without a figure; a small three-arrow figure (sähkö + ulkoilman lämpö → sisälle) like the sim's would help before the student reaches the sim. "oppitunnin fy3-2 tapaan" cites a lesson that is not a listed prerequisite (fy3-5, fy3-9); write "työn W = Fs tapaan".
- Figure 1 (phone, 360 px): Q₁, Q₂, T₁, T₂ and W render at about 12 px; legible but small. Enlarge them.
- sim readout — heat-pump and cogeneration readouts wrap to 6–7 lines on a phone (spec says at most four short lines); shorten "Energia säilyy: sisään … = ulos …".

## Checked
- Opening question (why under half becomes electricity, where the rest goes) is answered in the hyötysuhde paragraph and by the cogeneration example.
- Learning path fits fy3-9/fy3-5; first-law sign convention (W = −pΔV for expansion) is stated and used in L2-03; second law stays qualitative; no cycles, as the slot requires.
- Example has five stages with bold lead-ins, one step each; symbolic before numeric; it differs from every exercise.
- Exercises: L1 five one-formula, L2 four (conversion, two-step, rearrangement), L3 three with reasoning; contexts are Finnish and varied. Exit ticket tests work, hyötysuhde and the heat-pump paradox.
- Finnish terms (lämpövoimakone, hyötysuhde, lämpökerroin, hukkalämpö, kaukolämpö, yhteistuotanto) match the glossary; grammar fine.
- Page 390/1280: figures sit beside their paragraphs; both SVGs readable at 360 px; no horizontal scroll at 360, 390 or 1280.
- Sim at 360/390/1280, all four situations: arrows, labels and legend unclipped; sliders and readout respond; the scale key changes with total power (e.g. 0,05 kW at the minimum), and the "Lisätietoja" text is sufficient.
- Heat pump picture: electricity plus ulkoilman lämpö merge into "lämpö sisälle" with the sums 1,00 + 2,00 = 3,00 kW, so the energy balance is visible and no conservation violation is implied.
- Speed select has hidas, normaali and nopea; the default pace is followable (arrow chevrons and fan drift gently). The canvas carries only labels and values.
- Screenshots: content/FY3/fy3-11/review/fy3-11-rev1-*.png.
