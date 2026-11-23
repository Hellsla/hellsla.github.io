VERDICT: PASS
CONTENT-HASH: b2479eab4e3b1226
SCOPE: full request; the diff since the passed hash (b3bdcca4582a92f4) touches only unit.md (three new `pysahdy` boxes, hero and ketju figures now pictures). inquiry.json, tasks.json, solutions.md and exit ticket are unchanged, so the earlier PASS for them stands and they were not re-judged.

## Blocking
- (none)

## Polish
- Box 1 (after Ydinajatus): "Tehtävässä kysytään..." does not say which task. "Koetehtävässä" would match the paragraph above. The answer is the two sentences just before the box, so it tests recall of the paragraph, not understanding. That is acceptable as a warm-up. A box that asked the student to sort a made-up question ("Kuinka kauan lataus kestää?" teho, "Kuinka suuri osa tulee hyödyksi?" hyötysuhde) would make the student apply the idea.
- Box 2 (kWh): the display formula `1 kWh = 3,6 MJ` is directly above the box, so the student only reads it back. Putting the box before the formula, or asking "Laite on päällä 2 tuntia teholla 1 kW. Onko tulos kW vai kWh?", would test more.
- Box 3 (ketju): it comes after the johda derivation, whose last sentence already says the same (alle 1, siksi pienempi). Put it before the derivation as a prediction: the student argues first, then sees the proof. The number question (0,90 · 0,45 · 0,98) matches the figure.
- Plain-language reading level: all three boxes are fine. They use short sentences and no new difficult words, and "suureet", "hyötyteho" and "tulo" are known from the unit. "Tulo on pienempi kuin pienin luku" holds only because every factor is under 1, and the box says so.

## Checked
- The three boxes fit the lesson. They are short, in the right place, with a question first and the answer behind `---`. They add no stage and no heading. Numbers and units are LaTeX and use a decimal comma. The wording matches the Finnish unit; the physics (teho/energia, kWh = 3,6 MJ, kerrotaan, alle 1) is correct.
- The energy-into-heat rule is not touched. The "Häviöt" mistake already says sisäenergia and lämpönä.
- Misconception coverage: boxes 2 and 3 address two of the listed "Yleisiä virheitä" (teho/energia, hyötysuhteiden yhteenlasku). This is real support.
- Workload: three one-line boxes add under 3 minutes to the 75-minute unit.
- The hero and ketju figures are now pictures. Their alt texts and labels (foreignObject) are unchanged and give the same data. Looks and legibility go to the visual reviewer.
- Unchanged parts: the earlier PASS covers the inquiry, the nine Sovella tasks and the solutions. The packet's deterministic check (`practice.py check`) is OK.
- Hash identical at start and end (b2479eab4e3b1226).
