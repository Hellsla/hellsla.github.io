VERDICT: PASS
CONTENT-HASH: 38c778f449b232fd

## Blocking

## Polish
- lang/fi.json `rivi_nakyvissa` — at $L=-17$ and $L=-34$ the readout says "Näkyvissä $1$ kohdetta" (seen live). — Singular form for $n=1$ ("Näkyvissä $1$ kohde"), or "Kohteita näkyvissä: $n$".
- inquiry.json:119 (sim `calc`) — "näkyy, kun sen koko on noin $\tfrac{1}{2000}$–$3$ kertaa näkymän leveys": the picture starts fading in at $0{,}25\,\text{px}$ ($\approx\tfrac{1}{2200}$), but the readout counts it as visible only from about $0{,}5\,\text{px}$ ($\approx\tfrac{1}{1200}$, `a >= 0.5`). — Say "noin $\tfrac{1}{1000}$–$3$" or "noin $10^{-3}$–$3$".

## Checked
- Round 1 Blocking fixed: in the rebuilt preview (Chromium, 12 values of $L$) the readout's object name, size, count and listed names all render as KaTeX, with no raw `$`.
- Round 1 polish applied: "… radan säde" (with a radius line), "gammasäteilyn aallonpituus", the slider in the exp-1 intro, "likimain" for $\Delta n$, and the `model` fragment removed.
- Live `simState` at every experiment value: $L=-9$ gives water ($n=-10$), $-9{,}4$ the hydrogen atom ($-10$), $-14{,}5$ the proton ($-15$), $-17$ the quark ($-18$); $7{,}7$ gives Earth ($7$), $9{,}7$ the Sun ($9$), $13{,}5$ Neptune's orbit ($13$), $21{,}5$ the Milky Way ($21$), $27{,}5$ the universe ($27$); $-34$ gives the Planck length ($-35$) and $-4$ the hair ($-4$). These match the predictions, the numeric answers 5 and −4 and the solutions.
- All 12 exercises recomputed with my own formulas: they match answers.py and exercises.json, and every answer rounded to the data stays inside its tolerance.
- Inquiry numbers right: siirto and its mistakes, check-2 and its inverse, the example, and the differences 8, 4, 6, 31, 42 and 62.
- Magnitudes: Sgr A* horizon $2{,}54\cdot10^{10}\,\text{m}$ from $4{,}3\cdot10^{6}\,M_\odot$, observable universe 93 Gly, Proxima 4,2 ly, Sun/Earth 109, Pb nucleus 14 fm.
- `calc` example: $62\,\text{px}$ at $L=-9$ is right. `kohdeExp = round(log10 m)` matches the glossary's rule of rounding at about 3.
- Worked example and all 12 solutions follow the seven steps: symbolic first, conversions, rounding justified, a real reasonableness check.
- Every correct option and its feedback in pred-1/2, exp-2, menetelmat, tunnista, vuorovaikutukset, virhe and check-1 is right, and so is the exit ticket.
- Lesson facts (heliopause $120\,\text{AU}$, Oort cloud, nucleus holding >99,9 % of the mass, beta decay, the range of the strong force, EM/gravity $10^{36}$) and the figures' numbers are correct. The content stays within FY1 scope and the 2026-10-28 brief.
