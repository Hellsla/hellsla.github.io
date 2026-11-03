VERDICT: PASS
CONTENT-HASH: d9f63abcfb924693

## Blocking

## Polish
- assets/sims/fy8/fy8-5/sim.js:200 — the scale bar is still hard-coded as `$0{,}1\,\text{nm}$`, so the English canvas shows "0,1 nm" with a decimal comma (review/shots/fy8-5-sim-1280.png). The other labels (orbital title, "hits") now come from lang/en.json. — Build the label with `tx(0.1, 1)`.

## Checked
- A script compared lesson.md, inquiry.json, exit-ticket.json and the exercise files with content/fi/FY8/fy8-5. Every number is identical once the decimal sign is normalized. So are every non-string JSON value (`correct`, `answer`, `tolerance`, `mistakes`, `initial`, `reveal.min`, `optional`) and every id and key. The only math changes are translated `\text{}` labels and subscripts (ylä→upper).
- The inquiry `unit` changed from kpl to hits, and the exercise units to electrons, hits and orbitals. All of these are correct for the quantities counted. No "kpl" is left in the English files.
- lang/en.json sims/fy8-5 now holds `osumia` → "hits" and `orbSuffix` → " orbital". Both are faithful to lang/fi.json, and the canvas in the 1280 px shot shows "1s orbital" and "hits".
- Recomputed in one script: 656.47 nm (3d→2p), 10.2 eV (2p→1s) and 2700 expected hits in the upper lobe. These match the text.
- Every condition from the round-1 check is still there: "in the hydrogen atom", "states of the same shape", "approximately", "on average every tenth", "expected value" and "not measured as directly".
- Every choice item still has exactly one correct option. The exit ticket for N is 1s² 2s² 2p³.
