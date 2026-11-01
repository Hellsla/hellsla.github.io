VERDICT: FAIL
CONTENT-HASH: 339ff2bfdf81959e

## Blocking
- inquiry.json activities[4] and [6] (experiment 1 and 2) / lang/en.json sims.fy3-11 — the measurement table of experiment 2 shows the varied setting "piston return" with the raw sim values `sama paine` / `jäähdytys ensin` (Finnish words in English text; templates/inquiry.js runs the value through the sim's `values`, and lang/en.json sims.fy3-11 has none) — add `"values": {"sama paine": "at the same pressure", "jäähdytys ensin": "cool first"}` to sims.fy3-11 in lang/en.json (as sims.fy3-9 has for isoterminen). Not fixable in content/en: check_i18n requires the same keys as the Finnish inquiry.json, which has no `values`.

## Fixed
- none needed

## Polish
- The sim's heating readout shows `ΔV = 0,001 l` with a decimal comma in the English page (sim.js `tx` writes `{,}`); the same convention is in other FY3 sims, so a platform matter, not this chapter's text.

## Checked
Same activity order, predictions, experiments, hints, mistakes, feedback, solutions and exit ticket as the Finnish; nothing added or dropped. Natural English; terms (efficiency, coefficient of performance, heat engine) consistent; units and symbols as in the Finnish. Figure labels and descriptions use W_g / E_el. Exp-2 390 px capture checked (that is where the Finnish value shows).
