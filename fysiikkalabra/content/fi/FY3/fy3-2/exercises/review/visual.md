VERDICT: PASS
CONTENT-HASH: ca2d81baf5a67f35
ROUND: 3
Mode: delta

## Blocking
(none) Earlier Blocking: none. Round-1 Polish resolved: L2-05 now shows W1..W4 on separate rows, L3-05 uses plain "6,52 m/8,0 s" instead of nested fractions, and the d) check no longer an identity (fitted-line work against the table's last point, 28,8 kJ vs 28,7 kJ, arithmetic verified).

## Polish
- [Minor] Task tables (L2-05, L2-06, L3-04, L3-05, 1280 px) — header centred, numbers left or right aligned — align both the same way.
- [Minor] L2-07 (open-exercises-L2-1280-8) — the Mallivastaus appears above Kysytty and Periaate, unlike the other solutions — optional: place it after Sijoitus.
- [Minor] L2-05 Kaava — "0,5 ·" replaces the fraction 1/2 in the formula (an intentional change); a reader may still expect \tfrac{1}{2}; fine as is, only keep it consistent in the other FY3 work chapters.
- [Minor] No 360 px captures of the new tasks (only stage-exercises-390); check_layout 360 is clean.

## Checked
- open-exercises-L2-1280-6: L2-05 (formula line, four trapezoid rows, answer 55 J) and the start of L2-06 (stairs, table).
- open-exercises-L2-1280-8: L2-07 (error task, model answer, Sijoitus block, Järkevyys).
- open-exercises-L3-1280-7: L3-05 (a) to d), aligned Sijoitus, Vastaus, Järkevyys).
- Diff of the MC reorder in L1 read; no clipping or overflow at 1280.

## Checked in round 3
- Delta (HEAD): split rows read well in source: each continuation "\\ &= result" aligns under the first "=" of its aligned block, the Finnish decimal comma / English point and unit spacing are unchanged. check_layout.py 360 px --site is OK for fy3-2 (the site still serves the previous version of the formulas, so this does not yet prove the new rows). No 360 px solution captures exist in review/shots (only 390 and 1280 shots), so the 360 px result is judged from the source: rows are now at most about one line of text at 360 px.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
