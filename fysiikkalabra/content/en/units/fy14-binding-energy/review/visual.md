VERDICT: FAIL
CONTENT-HASH: c4cb2276f3c98102

## Blocking
1. [Major] Binding Energy Explorer, *Whole curve* at 390 px (`fx-be-explorer`; shared `fx/binding.js`). Most of the earlier finding is fixed:
   - $^{56}\text{Fe}$ now stands over the peak.
   - Nothing is preselected.
   - The reaction steps are stacked, with no overflow in any of the four reactions.

   The helium label is still misleading on a phone. Automatic placement puts "$^{4}\text{He}$" at about $A = 18$, $B/A = 7.3$, inside the cluster of C, N and O points. Those points cover the "4" and the leader line, so the student reads "He" next to nuclei with $A \approx 12$–$16$. Helium-4 is the unit's worked example and the first point the explorer question sends them to. The same happens to the "235" of $^{235}\text{U}$ in the fission view, and to the "f" of "fusion", which sits under a data point. At 1280 the leader line shows and the labels are readable.

   Fix in `binding.js`:
   - draw the label layer above the points, with a white halo (`paint-order: stroke` or a background box);
   - on narrow plots, place the He-4 label above and right of its own point (about $A = 8$, $B/A = 7.8$), not in the cluster;
   - move "fusion" below its arrow, away from the Li and Be points.

## Polish
1. [Minor] The explorer's light-nuclei view and the D–T, D–D and Li-6 reactions are clear at both widths; no change needed. The reaction table now writes "$3 \cdot {}^{1}_{0}\text{n}$": resolved.

## Checked
- Fresh build and captures for this hash (stamp c4cb2276f3c98102).
- I opened the worked example with all steps at 390: the substitution is split one term per line, and the Given is braced. Answer: $0.0304\ \text{u}$, with a clear significant-figure reason.
- Ladder and qbars label sizes at 390 and 1280 (smallest 14.3 px).
- The explorer at 390 and 1280 in the start state and with each of the four reactions. I zoomed the 390 graph.
- Playwright: no display overflow in the page or the explorer, no label outside the plot, no KaTeX errors, no raw `$`, no console errors.
- Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English/French 4 · accessibility 3

## Shared issues
- `fx/binding.js`: the label layer sits under the points and has no halo on narrow plots (Blocking 1).
