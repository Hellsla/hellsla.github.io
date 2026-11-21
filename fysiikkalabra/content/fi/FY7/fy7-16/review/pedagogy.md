VERDICT: PASS
CONTENT-HASH: e4b1804ff1f23195

Scope (teacher 2026-11-20): only the three new ```pysahdy blocks and old content that stops them working.

## Blocking
(none)

## Polish
- lesson.md:156-160 (hob block) — the answer repeats the sentence just above and the caption ("Lasi ei johda sähköä, joten siihen ei synny virtoja"), so the student only recalls it. Ask for an application instead, e.g. "Mitä kattilan pohjassa pitää olla, jotta siihen syntyy pyörrevirtoja?", or leave as a light recall check.
- lesson.md:185-189 (attenuation block) — the answer jumps from $A = 9{,}0\,\text{dB}$ to $P/P_0 = 10^{-0{,}90}$; the inversion step is not shown. Add "$\lg(P_0/P) = A/(10\,\text{dB}) = 0{,}90$, joten $P/P_0 = 10^{-0{,}90}$". The paragraph just read has no $10^{-x}$ form; it appears only in the worked example.
- lesson.md:185 (attenuation block) — the question needs a calculator for $10^{-0{,}90}$ right after a conceptual section. Cheap alternative: a rounder case (30 km gives 5,4 dB; 55 km gives about 10 dB), or accept the calculator.

## Checked
- Charger block (138-142): placed right after its figure, answerable from the paragraphs above, answer correct and causal (fewer field lines, smaller flux, smaller voltage), matches koe-1 and the figure.
- Attenuation numbers: 0,18 dB/km · 50 km = 9,0 dB; 10^-0,9 = 0,126, about 13 %. Correct.
- Hob block: physics correct (no current in glass; glass warms only from the pot), consistent with Yleinen virhekäsitys.
- All three blocks are short, open on a button, gate nothing, add no field or storage; they match the pysahdy spec.
- None gives away a prediction: ennuste-kattila and ennuste-kuitu stay gated by `reveal`. The new blocks sit in Teoria, after the prediction stage.
- Numbers with units are in LaTeX; Finnish grammar and glossary terms (pyörrevirta, vaimennus, lähetinkäämi) correct.
- Workload: three short blocks, about one minute each; the lesson stays one lesson.
- No old content stops the blocks working.

## Vanhan sisällön löydökset
- Section "Kaava: Vaimennus desibeleinä" does not display the inverse $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$, although the transfer item and the worked example use it. Put it in the formula block (not fixed in this PR).
