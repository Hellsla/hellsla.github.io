VERDICT: FAIL
CONTENT-HASH: 760578538cb329ae
Round: 1 (YO-skill task)

Scope: the new task L2-08 (prediction of change, added 2026-11-05). The rest of the set and answers.py are unchanged since the round-3 PASS.

## Blocking
- solutions.md L2-08 last sentence, "Kolminkertainen muutos jäisi saamatta vain, jos sauvat olisivat yhtä pitkiä." This is false (A): with equal lengths the ratio would be exactly 3, so the threefold change is reached, not missed. It contradicts the line above it. — Fix: "Kolminkertainen muutos saataisiin vain, jos sauvat olisivat yhtä pitkiä."

## Polish
- solutions.md L2-08, "Lyhyempi sauva pitenee enemmän, koska sen lämpötila nousee kolminkertaisesti". This names only half of the cause. Fix: "…koska lämpötilan nousu kolminkertaistuu, mikä on enemmän kuin pituuden puolittuminen pienentää ($0{,}5 \cdot 3 = 1{,}5 > 1$)."

## Checked
- My own script gives ΔL_A = 12·10⁻⁶ · 4,0 · 10 = 0,48 mm, ΔL_B = 0,72 mm, and a ratio of 1,5. The correct option, the answer string and the Arvio values (0,5 and 0,7 mm) agree.
- The conditions are stated: the same steel, so α cancels, the same initial temperature, and free expansion. A ΔT of 10–30 K is well within the linear range.
- There is exactly one correct option. The 3× option (only ΔT counted), the "same" option (only the material) and the 0,5× option (only L₀) are each really wrong, and each feedback names its mistake correctly. The 3× distractor catches the lesson's stressed point that ΔL ∝ L₀ ("kaksi kertaa enemmän hiukkasvälejä").
- The correct option is not identifiable by form. All four options have the pattern "Kasvaa/Pienenee/Pysyy samana: …" and similar length.
- Inline chains: the longest is "ΔL_B/ΔL_A = 0,5 · 3 = 1,5", about 200 px, so it fits.
- Renders: I viewed review/shots/fy3-8-open-exercises-L2-1280-12.png and -13.png (after the commit). The options, the feedback and the solution render. I checked the phone width from the text only.
- The hash was the same at the start and at the end.
