VERDICT: PASS
CONTENT-HASH: 989af167e9a36da4

## Blocking
(none)

## Polish
- inquiry.json hook/pred-1 — the hook already says the drinks stay cold for hours and then warm fast, so Cem's option in pred-1 nearly restates it; the prediction is only weakly arguable. Fix: drop "Muutaman tunnin ajan juomat ovat jääkylmiä ... eivät ole enää kylmiä" from the hook, or make pred-1 ask for the shape of the curve with a numeric or sketch element.
- inquiry.json pred-1, Cem's feedback — it says the graph "testaa tätä" but names no evidence. Fix: name it, e.g. "tasanne 0 °C:ssa ja t0, jossa käyrä alkaa nousta".
- inquiry.json virhe, option 1 feedback — it ends "Virhe on muualla: laskussa ei ole jään sulamista", which gives the answer to a student who picked the wrong option. Fix: "Tarkista, riittääkö veden energia sulattamaan kaiken jään."
- lesson.md "Yleinen virhekäsitys" — "energiaa siirtyy kaiken kaikkiaan lämpimästä kylmempään" is awkward for fi-easy. Fix: "energiaa siirtyy aina lämpimästä kylmempään".
- inquiry.json — the cooling circuit (P = c(m/t)ΔT) has only a pysahdy question and no task in the core path. Acceptable for a two-credit applied lesson; consider one optional interpret task if the exercises do not cover it.

## Checked
- The prerequisites fy3-6, fy3-7 and fy3-12 match the retrieval item (P = UAΔT), and the lesson combines all three, as the slot requires ("soveltava, ei kertausta").
- The predictions can be refuted: pred-1 by the graph (plateau, t0) and pred-2 by the Pt table; the "50 % shorter" distractor is rejected by the numbers. Feedback repairs the misconception and does not just restate the answer.
- The kayra and taulukko interpret tasks need the figure or table. I recomputed the numbers (333 kJ, Pt ≈ 334 kJ on every row, 85,7 %, 64,9 s, 213 kJ) and they match.
- The graph's aria-label gives a reader who cannot see it the same data (plateau, 28 °C, scale). The graph and the theory figure are legible at 390 px.
- Figures: the hero picture shows the Miksi situation. The cool-bag bar chart is to scale and labelled. The cooling-circuit diagram is uncluttered, and colour (T2 red, T1 blue) is paired with labels.
- Worked example: seven stages with symbolic solution first, then substitution, a sensible-result check and a limit note. Paragraphs are short.
- The model answer of johtopaatos is observable and honest about model values versus measurements ("esimerkkiarvot, eivät mittauksia").
- Workload is about an hour: 2 predictions, 3 core interpret tasks, 3 optional items. Check-3 and reflect are optional.
- Finnish: units are in LaTeX, case endings are right ($0\,^\circ\text{C}$:ssa) and the register suits fi-easy apart from the one item above. The hash matched at start and end.
- Not judged: the exercise set, which is reviewed apart from the lesson.
