VERDICT: PASS
CONTENT-HASH: 6dfb464fbab8578b

## Blocking

## Polish
- answers.py:15 (L2-04) — `round(..., 1)` gives 4.0, but the solution now says 4,00 with three figures. The value is the same and inside the tolerance, but the code and the stated precision disagree. — Use `round(..., 2)` and update the comment.
- inquiry.json:881 (siirto, Järkevyys) — "$0{,}20 \cdot 101\,\text{kPa} \approx 21\,\text{kPa}$": 0,20 · 101 is 20,2. The 21 comes from 60/293 = 0,205. — Write $0{,}205 \cdot 101 \approx 21$, or "noin 20 kPa, eli noin 121–122 kPa".
- inquiry.json:940 (check-2) — The lead-in still says "Kuvaajan lukeminen", but the body now correctly reads from the table ("Taulukosta luetaan"). — Rename the lead-in to "Taulukon lukeminen".

## Checked
- Round-1 Blocking L2-03 is fixed (solutions.md:79). The Vastaus line now says Δp = 27 kPa has two figures, so k = 0,39 kPa/°C, kΔθ ≈ 23 kPa and 110 − 23 = 87 kPa to the whole kPa. That is the difference rule, applied correctly.
- Round-1 Blocking L2-04 is fixed (solutions.md:89). The answer is now 4,00, because whole degrees give 100 K and 400 K to the kelvin, three figures each. That is correct, and 3,9955 → 4,00.
- The round-1 Polish items are addressed: L2-02 justifies by Δp = 33 kPa; L1-03 and L1-05 note the decimal-rule alternative; L3-03 says "pienimmillään (mallissa nolla)"; the exit ticket gives −273,15 °C.
- I recomputed every answer in one script, and all twelve match answers.py: 294,15; 76,85; −195,75; 25; −270,45; 59,85; 101,55; 86,86; 3,9955; 320,82; 127,05; −126,575.
- Worked example: −100/0,37 = −270,27 → −270 °C, with two figures from the 2-figure slope (Δp = 37 kPa). The independent check 100 · 373,15/273,15 = 136,6 vs 137 kPa is real.
- Reasonableness checks recomputed: L2-03 by p ∝ T gives 86,7 kPa; L3-01 gives 20/288 · 300 ≈ 21 kPa; L3-02 gives p/T = 0,49975 both times and 36 °C by the Celsius ratio; L3-03 gives 283,15/293,15 = 0,966.
- Numeric tasks: siirto 121,67 → 122 kPa, and its mistakes 404 and 83,84 are correct. check-2 gives −273 °C, with the correct 3-figure reason. virhe gives 128,19 kPa.
- Every stated principle applies to its task: constant V and n means p ∝ T in kelvins, and the equal degree size means ΔT = Δθ. Every conversion is right, and every unknown is solved in symbols before substitution.
- sim.js is unchanged in its physics: wall-impulse pressure ∝ N v²/(Wc·Hc), vRel = √(T/300), and the window runs on simulated time. exp-1 and exp-2 lock V and T respectively, and the predictions' numbers (100→200, 50→100, 1,41² ≈ 2) agree with the model.
- Scope is inside FY3's contents "termodynaaminen systeemi ja tilanmuuttujat" and "lämpötila". The figures are to scale as stated.
