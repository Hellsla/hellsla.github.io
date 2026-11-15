VERDICT: PASS
CONTENT-HASH: 806a1f1affaa7986
Round 3 delta against cc5cfb996b96c940.

## Blocking
(none)

## Polish
- B-leaning, not blocking: the work row now reads "constant pressure, volume changes → work done, W = pΔV" (was "magnitude of the work"). The Kaava (line 321) names the same formula "work done by an expanding gas / on a compressed gas", with ΔV a magnitude (line 324), so the chart agrees with the Kaava; but the 1st-law row uses W for the work done on the gas, where an expansion gives W = −pΔV (line 330). "magnitude of the work" or "work (magnitude)" kept that sign explicit; the fi chart still says "työn suuruus".
- The aria-label still says "the magnitude of the work is pressure times the magnitude of the change of volume": same physics as the pill, only more precise than the visible label; aligning the wording is advised.
- Round-2 items stand: the 1st-law row does not name W as work done on the gas; the key "kaasuun tehty työ" is unused.

## Checked
- Diff: only the figures.json string "työn suuruus" and the matching chart label in unit.md changed; formula W = pΔV, other rows, Kaava and aria-label unchanged.
- Chart label vs Kaava lines 321–330: consistent as a magnitude statement.
- Hash at start and end: 806a1f1affaa7986.
