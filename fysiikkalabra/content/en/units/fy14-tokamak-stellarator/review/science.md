VERDICT: PASS
CONTENT-HASH: 398b2cfa18a413c4

## Blocking
None.

## Polish
1. **C→B, `unit.md` *Pulsed or steady?*, first bullet.** "fast neutral atoms shot into the plasma push its charges round the ring": the atoms are ionised in the plasma, and the fast ions they become circulate round the ring and carry the current. Write "fast neutral atoms enter the plasma, become fast ions and carry current round the ring".
2. **`inquiry.json` pulse-data table.** EAST's 1066 s of 20 January 2025 is in `unit.json` sources but not in the table, which shows only EAST 2021 (1056 s). Add the row or a note, so that the table shows the current state of the records.
3. **`unit.md` Summary, last bullet.** "Wendelstein 7-X shows that optimised stellarators can compete" is an evaluative claim with no date. Write "in 2025 Wendelstein 7-X set a record triple product for long pulses, on a par with tokamaks". This is what `reactors.js` says.

## Checked
- Recomputed: $N = 2412$; $B = \mu_0 N I/(2\pi R) = 5.29$ T at 6.2 m, 7.81 T at 4.2 m, 4.00 T at 8.2 m (figure labels 7.8 / 5.3 / 4.0 T). The mistakes 5.29, 4.0 and 0.434 are correct. Check-2 gives 3.0 T. $1337 : 390 = 3.43$, and the mistake 947 is correct. 5.3 T is about $10^{5}$ times the Earth's field.
- **Non-inductive current drive.** The theory, prediction 2, misconception, check items and `reactors.js` all say that inductive drive alone gives pulses and that NBI, RF (LH, ECCD) and the bootstrap current allow long pulses or steady operation. WEST 1337 s on 12 Feb 2025 with LHCD was verified (Wikipedia WEST page, 2026-11-01). Tore Supra 6 min 30 s (2003).
- Twist physics: the grad-B and curvature drift, charge separation and outward $E \times B$ drift. The `reactors.js` drift panel's directions were recomputed: with $\overline{B}$ ⊗ and the axis on the left, ions drift up, $\overline{E}$ points down, and $E \times B$ points outward. Poloidal field from $I_\text{p}$; CS as a transformer; 15 MA for 300–500 s; peak 11.8 T.
- Facts: Tamm–Sakharov early 1950s; Spitzer 1951; W7-X has 50 non-planar and 20 planar coils, first plasma 10 Dec 2015, about 8 min in Feb 2023, 20 coils with insulation faults (Wikipedia, verified).

## Shared issues
- `assets/units/fy14/fx/reactors.js`: physics checked, nothing blocking. The step cards, comparison table and checks are correct, including non-inductive drive and the drift directions. Polish: the "May 2025" W7-X record: Wikipedia gives only the OP2.3 campaign (Feb–May 2025). Keep the date if IPP's press release confirms it.
