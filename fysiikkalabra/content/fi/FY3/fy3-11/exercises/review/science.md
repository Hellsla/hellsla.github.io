VERDICT: PASS
CONTENT-HASH: 6c2b323c49e732b1
SCOPE: delta added-exercise from b06084335558b3a5 base 89bcb63b7431

## Blocking
(none)

## Polish
- L1-09 text — "laajenee ulkoilman paineessa … Paine pysyy vakiona" leaves implicit that the gas's own pressure equals the outside pressure (slow expansion, light frictionless piston). C-level simplification; "kaasun paine on koko ajan sama kuin ulkoilman paine" would make $p$ in $W_\text{k} = p\,\Delta V$ unambiguous.
- L2-09 — the physics asked is only $\Delta V = A\,\Delta s$; the 250 kPa on the graph goes unused. Optional: a second part asking $W_\text{k}$ (750 J) would tie the figure to the chapter's law.

## Checked
- Only L1-09 and L2-09 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $W_\text{k} = 101\,325\,\text{Pa} \cdot 0{,}0020\,\text{m}^3 = 202{,}65$ J → $2{,}0 \cdot 10^2$ J; answers.py 202,65; answer 200 with relative tolerance 0,04 accepts 202,65. MAFY value matches docs/mafy-arvot.tsv (VERIFIED).
- L1-09: constant pressure stated, so $W_\text{k} = p\,\Delta V$ applies; sign (expansion, positive work) right; two figures from 2,0 l; check (≈ 100 kPa · 2 l) real; the lifting comparison (2 kg, 10 m ≈ 196 J) is right and stays within FY3 ($W = Fs$, $G = mg$).
- L2-09 recomputed: $\Delta s = (4{,}0 - 1{,}0)\cdot 10^{-3}\,\text{m}^3 / 50\cdot 10^{-4}\,\text{m}^2 = 0{,}60$ m; answers.py 0,6.
- figures.py pv-isobaari: horizontal segment (1,0 l; 250 kPa)–(4,0 l; 250 kPa) on gridlines, axes from 0, to scale as stated; direction arrow matches "laajenee"; description gives the same end points; no area or work shown, so the figure gives nothing away.
- L2-09 conditions: constant cross-section stated (sylinteri, poikkipinta-ala); conversions cm² → m² and l → m³ right; reasonableness check (gas column 0,20 → 0,80 m) is an independent check.
- Both solutions complete (given/asked, principle with reason, symbolic before numbers, conversions, substitution with units, rounding reason, check); notation $W_\text{k}$, \textsf{l} as in the brief.
- Inside FY3 central content (mekaaninen työ, kaasun tilanmuutokset).
- Hash identical at start and end.
