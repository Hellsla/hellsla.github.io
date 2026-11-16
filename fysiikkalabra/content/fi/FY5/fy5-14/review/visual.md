VERDICT: PASS
CONTENT-HASH: 7deeed8682ce9bf7
ROUND: 3

## Blocking

## Polish
- [Minor] inquiry.json 400 (transfer task, Sijoitus) — the dot that now ends the first inline piece sits tight against the unit ("2000 Hz·") at both widths, because a trailing `\cdot` has no right-hand operand; `\cdot{}` at the end of the piece (and `{}=` at the start of the third) restores the operator spacing without touching a number, sign or unit.
- [Minor] same place — this chain is unboxed inline text while the v_L substitution of the same step is a boxed aligned block, and at 390 px the numerator sits close under the first line; the house form `&\quad \cdot …` in one aligned block would set the step uniformly when the file is next edited.

## Checked
- Delta, round 3b: inquiry.json 400 only; the dot moved from the start of the second inline piece to the end of the first. Same tokens in the same order.
- Own captures from the rebuilt preview/fy5-14.html?ratkaisut=1, every details open, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-13/: fy5-14-390-doppler-ctx-3b.png (390 px, dpr 2) and fy5-14-1280-doppler-ctx-3b.png, each with the steps around the chain.
- 390 px: "f = 2000 Hz·" | fraction 340 m/s : (340 m/s − 12,566 m/s) | "= 2076,8 Hz". The first line now ends in a visible multiplication dot, so the fraction reads as its continuation; no line begins with a bare dot against the fraction bar. Round 3's blocking item is gone.
- 1280 px: one row, "f = 2000 Hz · fraction = 2076,8 Hz".
- Nothing clipped; the fraction ends at about 247 of 336 px at 390 px; the steps before and after (v_L block, Vastaus box) unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
