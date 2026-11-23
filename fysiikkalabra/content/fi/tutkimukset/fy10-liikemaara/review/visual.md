VERDICT: FAIL
CONTENT-HASH: 1d06f92ebbede882

## Blocking
- [Critical] captures — visual verification incomplete: screenshots are missing and cannot be made here (playwright is not installed, `screenshot.py` fails), so the changed passage and the model figure were not seen as rendered — a visual review never passes from source alone — run `python3 scripts/screenshot.py fy10-liikemaara --if-stale` where playwright exists and re-run this delta (source reading found no defects).

## Polish
- [Minor] investigation.md ~l.240 — the new passage is correct in notation and Finnish ($p_\text{kok}$, `>`/`<` in LaTeX); it is two long sentences. Optional: "Vastakkaisessa törmäyksessä" could read "Kun vaunut liikkuvat toisiaan kohti,", echoing the sentence above.
- [Minor] fig 7 aria-label — "Mallikuvaaja … funktiona mallin mukaan" repeats "malli"; "Mallikuvaaja: … funktiona, jos liikemäärä säilyy" says the same. Earlier polish items (axis units, dashed continuation to p < 0) still stand.

## Checked
- Delta read from change.diff and the packet: investigation.md deviation passage, teacher.md bullet (same wording, consistent), model figure aria-label (figures.py and SVG match).
- No capture opened: none exist (see Blocking). The drawing is unchanged by the diff.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
