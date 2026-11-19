VERDICT: PASS
CONTENT-HASH: 9bad1c8d565e8cfc
Mode: full, round 1 (lesson.md, inquiry.json, exit-ticket.json, sim-spec.md and the captures; exercises not judged)

## Blocking

## Polish
- inquiry.json `check-c2` — the lesson has four checks (Käsite, Resoluutio ja epävarmuus, Laskeminen, Selitä); the form is three (concept, calculation, explanation). The resolution item is good but belongs in the core path as optional, or replaces the concept check's overlap — mark `check-c2` `"optional": true`. The same applies to the core path: `pr-numerot`, `reflect` and `check-3` are not optional although the 2026-10-26 rule makes retrieval, reflect and a third check optional unless the goal needs them. Workload is close to two lessons.
- inquiry.json `exp-2` / `pred-2` — the prediction's premise ("näyttää 0,30 s liikaa") already contains the answer, the correct option is the longest of four, and the numeric question's answer equals the slider the student set. The experiment confirms the model's arithmetic. Stronger: hide the offset in the sim (or reuse the thermometer idea), so the student finds it by comparing with T. Same length cue in `karkea` (the correct option is far the longest) and `check-c2`.
- inquiry.json `johtopaatos` — criterion 3 and the model answer need the thermometer data, but `after` lists only exp-1 and exp-2. Add `"data"` to `after`. Also `pr-numerot` option 4 feedback ("kello näyttää joka kerta saman verran liikaa") hands over the systematic-error idea that the hook's second question asks for, before any commitment: cut it to "Numerot kertovat lukeman tarkkuudesta, eivät siitä, onko kello oikeassa."
- lesson.md:108 — "Kerran kello käynnistetään vahingossa vasta…" reads as one past event. Corrected: "Joskus kello käynnistetään vahingossa vasta, kun kuula on jo liikkeellä." Fi-easy: "vaimentaa" (keskiarvo vaimentaa satunnaisvirhettä, used about eight times, also in the summary) is never explained for S2 readers; write "vaimentaa eli pienentää" at first use or say "pienentää" (the glossary's word).
- lesson.md:105, 135 — both photos sit after paragraphs they do not explain (caliper after the intro, LIGO after a Pysähdy); the LIGO caption does not say what it teaches about uncertainty. Move each beside the sentence it supports or tie the caption to resolution and reliability. lesson.md:219 and inquiry `siirto` solution: a display `$$…$$` in mid-sentence leaves ". Sijoitetaan" starting a line; check the capture or give the sum its own line.

## Checked
- Opening question is answered in the lesson: the spread is random error, the shared offset is systematic and found only against a known value; reflect returns to the class.
- Prediction, experiment, data and conclusion order follows the form; reveal `min` 3 equals the rows asked for; wrong-option feedback repairs the misconception.
- Example arithmetic checked (sum 19,09 s, mean 3,18 s, Δt 0,12 s, ε 3,8 %, five of six within the interval); seven stages, one step each, symbolic first.
- karkea, siirto, check-2, exit ticket and data-table numbers recomputed and correct; tolerances are relative, so rounded answers (2 %, 6,2) stay inside.
- Mistake lists in `siirto` and `check-2` match real slips; hints progress without giving the answer early.
- Exit ticket tests the core idea (systematic vs random, mean, relative uncertainty).
- Phone captures (sim 390, exp-3): nothing clipped; readout and labelled controls understandable.
- Slot goals covered; extras (resolution, relative uncertainty, rounding) stay within "luotettavuuden arviointi".
