VERDICT: PASS
CONTENT-HASH: f6e0c13fb90edba1
SCOPE: delta wording from 1d2e344571e5d8dc base 63ede90

## Blocking

## Polish

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end. Both times it was f6e0c13fb90edba1, the same as in the packet.
- Both Polish items from my previous report are fixed. solutions.md:144 (L1-07) now reads "Conservation of energy $E_\text{o} = E_\text{a} + E_\text{h}$, so $E_\text{h} = E_\text{o} - E_\text{a}$", and solutions.md:154 (L1-08) reads "Definition of efficiency $\eta = P_\text{a}/P_\text{o}$, so $P_\text{o} = P_\text{a}/\eta$".
- The diff changes only the Finnish words in these two Formula lines. The symbols, the equations, the substitutions and the answers (9.0 kJ, 200 kW) are the same as in the version I passed.
- L1-07: $36 - 27 = 9.0\,\text{kJ}$. L1-08: $180/0.90 = 200\,\text{kW}$. Both are correct.
- The Formula lines still start from the basic principle (conservation, or the definition of efficiency) and are solved symbolically before substitution. No guardrail break.
