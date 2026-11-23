VERDICT: PASS
CONTENT-HASH: 7a46917d3f0bf707

## Blocking

## Polish
- exercises/solutions.md:350 (fy8-6-L2-06) — "menee vielä hieman yli" is right, but the overshoot is $0{,}07\,\text{V}$, nearly as large as the $0{,}09\,\text{V}$ gap it cancels. — If wanted, give the number: "ja menee noin $0{,}07\,\text{V}$ yli" ($2{,}04\,\text{V} - 1{,}97\,\text{V}$).
- exercises/solutions.md:422 (fy8-6-L3-04) — the single-LED clause still reads "Yhden LEDin $eU_\text{k} = hf$". As a definition of the single-LED estimate this is acceptable, but $\approx$ would match the line's new opening. — Write $eU_\text{k} \approx hf$ there too.
- exercises/solutions.md:194 (fy8-6-L3-01) — the Kaava still has "$k = \tfrac{h}{e}$" with an equals sign (carried over). — Write $k \approx \tfrac{h}{e}$.
- exercises/solutions.md:99, 270 (L2-01, L1-07) — "$eU_\text{k} = E$" in the Kaava rows; "likimain" would match their Periaate (carried over).

## Checked
- Hash 7a46917d3f0bf707 at the start and at the end. This was a delta review of the two changed lines.
- L2-06: $\tfrac{hc}{e\lambda} = 1{,}968\,\text{V}$ at $630\,\text{nm}$. Eero's reading is $0{,}088\,\text{V}$ below it and Salla's $0{,}072\,\text{V}$ above it. Salla's extra over Eero is $0{,}160\,\text{V}$, so the new wording ("kumoaa … ja menee vielä hieman yli") is correct. The old "kumoaa osan" was wrong, because it described a reading that stays below the true value.
- L2-06: Salla's $h = 6{,}868 \cdot 10^{-34}\,\text{J}\,\text{s}$ ($+3{,}65\,\%$) against Eero's $-4{,}48\,\%$, so "osuu sattumalta lähemmäs" holds. Aino gets $-11{,}6\,\%$. All were recomputed.
- L3-04: the Kaava now opens with $eU_\text{k} \approx hf$, so "joten $U_\text{k} \approx \tfrac{h}{e}f + b$" follows. It matches the task's Periaate and the lesson's Kaava. This fixes my earlier Polish item.
- The diff touches no number, no answer, nothing in exercises.json and nothing in answers.py.
