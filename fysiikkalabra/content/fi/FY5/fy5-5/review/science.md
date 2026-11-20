VERDICT: PASS
CONTENT-HASH: ad5c1ea54563fc5f

## Blocking

## Polish
- lesson.md:296 (block 3): the graph's visible tick labels are every 600 µN, so 417 µN and 104 µN cannot be read off it precisely: they are only in the aria-label. "The graph shows the same value" is a bit strong. Fix: "about 100 µN, as the graph shows".
- lesson.md:200 (block 1): the answer uses the fact that the Moon has the smaller mass, but the paragraph does not give it. This is common knowledge and not blocking; the answer could add "(about 1/81 of the Earth's mass)".

## Checked
- Hash the same at the start and at the end. Scope: only the three new `pysahdy` blocks (teacher 2026-11-20, work queue 20); the the split of the worked example's *Tunnetut ja kysytty* stage (no number changed) and the inquiry.json reflow carries.
- Block 1 (Earth and Moon): a = F/m with equal third-law forces; M_Earth/M_Moon = 81, so the Moon's acceleration is about 81 times the Earth's. Correct, and answerable from the apple/Earth paragraph just before it.
- Block 2 (r on the surface): r is measured from the centre, R = 6378 km, which matches the paragraph before it, the transfer task and Etsi virhe. It gives nothing away that is not already in the paragraph, and Etsi virhe comes later, after the theory.
- Block 3 (graph): γ·(1,0·10⁴ kg)²/r² gives 417,1 µN at 4 m and 104,3 µN at 8 m, which matches the figure's data (figures.py) and the inverse-square paragraph. It extends the figure's 2 m to 4 m example without repeating it.
- Deterministic checks are green, including layout at 360 px with the answers open.

## Vanhan sisällön löydökset
- inquiry.json:343 (siirto, mistake 6378): the reasoning uses "g ∝ 1/r²" where the task speaks of the force; "F ∝ 1/r²" would fit better (from the previous round).
- lesson.md:685: "kentän voimakkuus ... 8,9 m/s²" is still the only core-path sentence that gives a field strength (from the previous round).
