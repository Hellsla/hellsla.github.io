VERDICT: FAIL
CONTENT-HASH: f5b9b9db4c7f7ede

## Blocking
- lesson.md, figure 3 (Kaavan kuvaaja) — the filled dot at $T_\text{v}=20\,{}^\circ\text{C}$ is labelled "esimerkki", but it is the opening case (0,30 kg, 20 °C, 0-asteinen jää 0,10 kg). The worked example (0,250 kg, 24,0 °C, −8,0 °C ice) is a different case and sits off this graph, and the graph comes before the example, so the label sends the student to the wrong place — rename the dot (e.g. "alun kysymys" / "kuvan 1 tilanne") or plot the example's own point.
- lesson.md, figure 2 (Energiataseen palkit) — the bars silently use ice at −10 °C (ice needs 35,5 kJ: 2,1 kJ warming + 33,4 kJ melting), while figure 1, figure 3, the misconception text and the simulation all use 0 °C ice (33,4 kJ, 24,7 g left). The visible figure never says −10 °C (only the aria-label does), so 35,5 kJ looks like a contradiction of 33,4 kJ; the "jäätä jää" bracket is also 10,4 kJ, not the 8,3 kJ the other pages imply — state "jää −10 °C, 0,10 kg; vesi 20 °C, 0,30 kg" in the figure, or draw it with 0 °C ice.

## Polish
- Koe tables at 390 px: the third column header ("jäätä jäljellä (g)") is clipped and needs a sideways scroll, although the student needs that column; shorten the headers (e.g. "jää (g)").
- Simulation bars use a fixed 0–250 kJ scale, so at the default values the decisive comparison (25,1 vs 33,4 kJ) is about 10 % of the chart height and the gap is a few pixels; an autoscaled axis would show the idea itself.
- Hook and Ennuste 1 pose the same scenario (0,30 kg, 20 °C, 0,10 kg, 0 °C), so Pohdinta does not raise a separate question; the hook could use a different glass or ask for the reasoning only. Ennuste 2's correct option "Vain vähän enemmän" is vague (5,9 g → 18,5 g is threefold); say "noin 4 kJ:n verran vähemmän jäätä sulaa".
- Esimerkki, vaihe 4: "6,05 K ≈ 6,0 K" should be "6,05 °C ≈ 6,0 °C", since T is a temperature, not a change.
- Workload is on the long side: two predictions, two experiments, error item, transfer task, 12 exercises, three checks and an exit ticket; level 2 task 1 is the worked example with 0 °C ice, close to repeating it.

## Checked
- Opening question is answered (theory, example, reflect, check 3); prior learning retrieved with chapter names, no lesson ids.
- Predictions can be refuted: Koe 1 (T_v at 10/20/40 °C) refutes 15 °C and "slightly above 0 °C"; Koe 2 refutes "no extra ice" and "does not melt".
- Variables locked correctly; sliders step 0,5 °C, tolerance 5 % relative, so 26,6 °C is findable.
- Recomputed example (6,05 °C), figure 3 line (40 °C at 80 °C), all exit-ticket, transfer and sample exercise answers: correct.
- Example is staged in 5 steps, symbolic first; exercise levels 5/4/3; feedback repairs the misconception.
- Simulation text sits behind Käyttöohje, Mallin oletukset, Laskennan selitys; 1280 px layout puts the sim beside the experiments and figure 1 beside its paragraph.
- Finnish reads correctly; glossary terms used; formulas and labels are LaTeX.
