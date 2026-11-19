VERDICT: FAIL
CONTENT-HASH: c6f2cf5ffc5539fa

## Blocking
- inquiry.json exp-1 `question` (answer 9,81 kPa) + simulation readout (390 px capture) — the readout prints "kulmakerroin $\rho g$ = 9,81 kPa/m" and "Kokonaispaine on 1,97 kertaa ilmanpaine" as soon as the sim opens, so the numeric question "lue se mittauksistasi" is answered without any measurement and the pred-1 comparison is shown ready-made; the slope-from-data skill (slot goal: line with constant term) is never practised — fix: drop the slope line and the ratio line from the readout (keep them in "Laskennan selitys") or show them only after the experiment's rows are recorded.

## Polish
- inquiry.json (pred-1, exp-1, johtopäätös, reflect) — "Mittauksesi", "mittaustesi" for simulation values; the brief says model values (the criteria already say "Erotin mallin laskemat arvot"); write "mallin arvot".
- inquiry.json (pred-3) — "Teoriatiivistelmä(ssä)" three times; the stage is called Teoria.
- lesson.md (Esimerkki, Järkevyys stage) — closing paragraph on the diver's body not being squashed is off the reasonableness check; move it out or cut.
- lesson.md (Mistä paine syntyy?) — the derivation paragraph runs long (ρ, V, m, G, p in one block); split before "Paine ei ole voima".
- inquiry.json (pred-2, exp-2) — both optional; fine, but then the density dependence is met only in theory text.

## Checked
- Path: G = mg (fy3-1) and particles-hitting-wall (fy3-3) → p = F/A → p = ρgh → p₀ as constant term; opening dam question answered after the ylipaine paragraph.
- Slot's "force as scalar" handled by the perpendicular-force statement.
- Predictions have real misconceptions (proportional total, density, vessel width); pred-3 compares models.
- Experiments lock the right variable (ρ / h).
- Worked example: seven stages, SI conversion of cm² explicit.
- Checks: orientation of gauge, vessel shape, slope from graph, explanation with criteria.
- Phone: sim legible at 390 px.
