VERDICT: PASS
CONTENT-HASH: 57b913a6fc66f29e

## Blocking

## Polish
- inquiry.json:112 (sim howto) — the glow is `S.Ps / 0.5` in sim.js, i.e. the power R_s I² (a rate), but the text says "kuinka paljon sähköenergiaa muuttuu … sisäenergiaksi" (an amount). Write "kuinka nopeasti sähköenergiaa muuttuu" or "kuinka suuri teho muuttuu".
- lesson.md:281 — "ei päädy määriteltyyn hyödylliseen käyttötarkoitukseen" is the guardrail sentence; the next sentence makes it concrete, but naming the useful part here ("akkuun kemialliseksi energiaksi") would tie the general rule to η = W_akku : W_lat directly.
- inquiry.json:16 (hook, carried from round 2) — "lähes yhtä kauan kuin koko alkuosa" is CC/CV behaviour; the lesson's constant-voltage model gives 18 min for 90 → 100 % against 30 min for 10 → 52 %.

## Checked
- Diff since the last science PASS (d18a4faa, after 8520f10b): only the efficiency paragraph and the sim howto changed; no number, formula or symbol.
- Efficiency: "enintään 100 %", "usein alle 100 %" now matches the guardrail wording; "Latauksessa näin käy aina, koska virta lämmittää resistansseja R ja R_s" is right in the lesson's model (R, R_s > 0 whenever I ≠ 0) and consistent with "loput muuttuvat resistanssien R ja R_s sisäenergiaksi, joka siirtyy lämpönä ympäristöön" two lines up and the energy-flow figure (1,1 + 0,3 Wh).
- η = 7,6 Wh : 9,0 Wh = 0,844 ≈ 84 %; W_lat = 4,5 V · 2,0 Ah = 9,0 Wh recomputed.
- Howto energy wording: sähköenergia → sisäenergia in R_s, no "lämmöksi"; glow indeed tracks R_s I² in the cell.
- Unchanged numbers rely on my earlier recomputation (round 2): 2,2 A; 0,88/0,22/3,40 V; 3,62 V; koe-1..3 values; worked example 2,0 A, 3,90 V; virhe, siirto, check 2, exit ticket 9000 C.
- Predictions, experiments, simState keys and model answers unchanged; one correct option each still holds.
- Deterministic checks all ok; no physics lint warnings listed.
