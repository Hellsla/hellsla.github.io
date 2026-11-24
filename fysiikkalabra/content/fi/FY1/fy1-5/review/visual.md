VERDICT: FAIL
CONTENT-HASH: 5cd975f38e79ae36

## Blocking
- [Major] sim-390 / sim-1280, assets/sims/fy1/fy1-5/sim.js and inquiry.json `howto` — the pace select was renamed from "Toistonopeus" to "Nopeus", right under the physics slider "Nopeus $v = 2{,}0\,\text{m/s}$". Two controls now carry the same name. The howto sentence "*Nopeus* muuttaa vain toiston tahtia" cannot tell the student which one it means. A student can easily think the select changes $v$, and the lesson is about $v$ and the graph slope. The ambiguity is in the controls and the instruction text — fix: name the select "Toisto" or "Toiston nopeus" (not plain "Nopeus"), and use the same word in the howto sentence.

## Polish
- [Minor] sim-390 — the removed note line ("Lippu: alkupaikka. Nuoli: nopeus…") is fine. The howto still explains flag, arrow and markers, so no information is lost.

## Checked
- fy1-5-sim-390.png and fy1-5-sim-1280.png: the changed controls. Layout, KaTeX labels and readouts are clean and nothing is clipped. The only problem is the duplicate "Nopeus" label.
- fy1-5-intro-1280.png (new hero image): it reads clearly, the subject is in the middle third, no text. Good.
- fy1-5-fig-2-390.png (new motion image): clean, labels are LaTeX, units are upright, nothing is clipped.
- The deterministic layout checks at 360/390/768/1280 px are ok. I did not open the other captures, since the diff does not touch them.

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
