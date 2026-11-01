VERDICT: FAIL
CONTENT-HASH: 5a08794ae859a389

## Blocking
- [Critical] simulation in Tutki and Koe 1–3 at 390 px (`stage-tutki-390-1`, `exp-exp-1-390-1`, `exp-exp-2-390-1`, `exp-exp-3-390-1`) — the canvas is cropped: only the left slope shows (the valley floor, the right slope and the $h_2$ the student must read are missing), and the energy-bar panel is gone completely; its labels are drawn at desktop size and pile up over each other ("Energia" on top of $E_\text{p}$; $E_\text{k}$, $E_\text{mek}$, $W_\text{muut}$ stacked into an unreadable blot). `sim-390` draws the same sim correctly, so the fault is the sizing inside the stage or experiment card. — On a phone this is where the student runs the experiments, and the bars show $\Delta E_\text{mek} = W_\text{muut}$. — Fix: re-measure and redraw the canvas at the card's width when the stage or card becomes visible (to match `sim-390`), then recapture at 390 px.

## Polish
- [Minor] `lab-1280-1`, `sim-1280` — in the sticky side panel at a 900 px high window, the last readout line ($W_\text{muut}$, $\Delta E_\text{mek}$, the very quantity Koe 2 compares) starts below the panel's fold and only shows after an inner scroll. — Fix: put $\Delta E_\text{mek}$ on an earlier readout line, or shorten the energy canvas a little.
- [Minor] lesson.md, Kitka muuttaa… second paragraph — "Painon eli painovoiman ja kitkan eron muistat luvusta …: paino on konservatiivinen voima." reads clumsily. — Fix: "Luvusta *Liike-energia, potentiaalienergia ja mekaaninen energia* muistat, että paino eli painovoima on **konservatiivinen voima** mutta kitka ei."
- [Minor] lesson.md, Energiaperiaate — "(…, esimerkiksi kuljetinhihna kantaa laatikkoa.)" is missing its link word. — Fix: "esimerkiksi kun kuljetinhihna kantaa laatikkoa".
- [Minor] sim readout — $h = 10{,}00\,\text{m}$ but $s = 0{,}0\,\text{m}$. — Fix: same decimals for both lengths.

## Checked
- contact-1…6 for triage; `fig-6-390` is a stray inline $\sqrt{2gh}$ crop, not a figure.
- Figures at full size: hero (`top-390`, `intro-1280`), `fig-3-390` laakso, `fig-4-390` työ (colours: force red, velocity blue), `fig-5-390` palkit.
- `theory-1280-2`, `theory-1280-3` (aligned derivations, energy principle, misconceptions).
- `example-390-1` plus the example in contact-1 (#9): substitution chain and the colon division.
- `sim-390`, `sim-1280`, `lab-1280-1/2`.
- `stage-tutki-390-1`, `exp-exp-1-390-1`, `exp-exp-2-390-1` (the defect) and exp-3 on contact-3.
- `open-tarkista-1280-2`; ennusta, tarkista and exit thumbnails on contact-1, -3, -4 and -5.
- Plain-quantity scan of the prose (lesson, inquiry, exit ticket): none found.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 2
