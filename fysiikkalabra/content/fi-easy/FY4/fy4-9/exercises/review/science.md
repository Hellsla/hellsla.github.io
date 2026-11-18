VERDICT: PASS
CONTENT-HASH: 84dec66598eb69d3
Mode: delta (round 2)

## Blocking

## Polish
- content/fi-easy/FY4/fy4-9/exercises/solutions.md:185 (L3-04 Kaava) — "pysähtymisaika on $\Delta t_\text{e} = 25\,\text{ms}$" puts a number into the symbolic step. Naming the symbol is enough; the value belongs in Annettu or Muunnokset.
- solutions.md:195 (L3-05 Kaava) — still open: a full stop is missing after "$v_1 = -g\,t_\text{putoaminen}$". Also say that the ball starts at rest, $v_0 = 0$.
- solutions.md:174, 185 — still open: $\Sigma F$ here is the sum of the interior forces, not the net force.

## Checked
- Hash 84dec66598eb69d3 at the start and the end.
- The round 1 Blocking item is fixed. L3-04 Kaava now gives the stopping time on the rigid obstacle its own symbol: $\Delta t_\text{e}$, with $I = F_\text{ka}\,\Delta t_\text{e}$ and $F_\text{ka} = I/\Delta t_\text{e}$.
- Sijoitus c uses $\Delta t_\text{e} = 0{,}025\,\text{s}$. $\Delta t = 10\,\text{ms}$ stays the strip width in $I = \Delta t \cdot \Sigma F$ and in Muunnokset. The last symbolic form now matches what is substituted.
- L3-04 numbers recomputed: $981 / 70 = 14{,}01\,\text{m/s} = 50{,}45\,\text{km/h}$, $981 / 0{,}025 = 39\,240\,\text{N}$, and $981 / 0{,}100 = 9{,}81\,\text{kN}$. All unchanged.
- The other Kaava lines start from $I = \Delta p$, $I = F\,\Delta t$ and $p = mv$, as in round 1. The signs are unchanged.
- The packet's "$\dfrac{F\,\Delta t}{\Delta v} m$" in L2-09 c is a line-join artifact of the packet. The file (lines 244, 252) reads $m = \dfrac{F\,\Delta t}{\Delta v}$.
- The L2-09 and L1-06 hunks only split paragraphs, word for word the same.
- Captures opened: none. I judged from the diff, the file on disk and the packet.
