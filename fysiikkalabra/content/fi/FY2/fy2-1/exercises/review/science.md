VERDICT: PASS
CONTENT-HASH: 370bd4ea91708a21

## Blocking

## Polish
- exercises/solutions.md:103 (L3-02) — The answer says "kuten taulukon energiat", but the task gives its data in the text, not in a table. — Write "kuten tehtävän energiat".
- exercises/solutions.md:54 (L2-01) — The reasonableness check credits "sähkömoottori", but the balance also counts battery and tyre losses. — Write "sähköpotkulaudalle" or "akulle ja sähkömoottorille".

## Checked
- I recomputed all 10 numeric answers independently in one script and compared them with answers.py and exercises.json. All match: 50, 239, 640, 510, 850 J; 3,0 kJ; 360 J; 29 000 J; 130 J; 0,20 J. The tolerance is relative, so data-precision roundings pass.
- Round-1 blockers are fixed. L1-02 is now a leaf with 6,0 J of 245 J to chemical energy (about 2 %, realistic for photosynthesis), and the lamp/radiation error is gone. L3-02 gives three energies and uses differences, not a product of retention factors.
- Round-1 polish is done: L1-03 is 20 % (realistic for current panels), and L2-03 asks for "yhteensä".
- Every solution has the seven parts. It names the system and why it is isolated, solves symbolically first, converts by substituting the prefix ($3{,}00 \cdot 1000\,\text{J}$, $2400 \cdot 0{,}001\,\text{kJ}$), justifies the rounding and checks by adding back.
- The word answers are right: L1-04 (chemical → thermal, radiant → electrical, potential → kinetic → electrical) and L3-03 (nuclear → thermal → kinetic → electrical; about two thirds to the sea and the surroundings, which is realistic for a light-water plant at about 33–37 %).
- The magnitudes are realistic: kettle 92 %, scooter about 72 %, swing and ball losses.
- Scope: no expressions for E_k or E_p, no work, no Q = cmΔT and no chain-efficiency product. \cdot and colon division are used throughout, with no ×, and every number with a unit is in LaTeX.
- No exercise claims a named data source.
