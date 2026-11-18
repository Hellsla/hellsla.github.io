VERDICT: FAIL
CONTENT-HASH: e09f46511f4167f8
SCOPE: delta: new tasks s8, s9 and intro; older tasks untouched

## Blocking
- [Major] s9 b) model solution, Substitution (en exercises-390-79) — the row `= 0.72 W · 0.40 s + 0.405 W · 0.20 s` is clipped at the right edge at 390 px (last `s` cut; worse at 360 px) — a clipped formula is unreadable and breaks the "nothing to scroll" rule although check_layout did not flag it — put `+ 0.405 W · 0.20 s` on its own aligned row, or compute W_1 and W_3 separately first.

## Polish
- [Minor] s9 b) — intermediate 0.405 W has three figures while Reasonableness says 0.41 W; make consistent.
- [Minor] s9 b) Reasonableness — unit chain `V²/Ω s = W s = J` splits over two rows with a lone `= J`; keep on one row.
- [Minor] s9 intervals "0.60–0.80 s" can break after the dash at a line end; use a non-breaking form.

## Checked
- en exercises-390-78, -79 (s9 solution a, b with substitution, reasonableness); en text of s8 and s9 in the packet compared with the Finnish: same numbers, units, ids, the figures' symbols ($\sin\alpha_1$, $\sin\alpha_2$, $\Phi$, $t$) match the task text; decimal point correct in English; unit fields language-neutral; "internal energy" wording right.
- Layout of the s8 task and figure taken from the Finnish captures (same shared figures, same structure); 1280 px not opened.

## Scores
illustrations 4 · typography 3 · English 4 · accessibility 4
