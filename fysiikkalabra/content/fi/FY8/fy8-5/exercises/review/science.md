VERDICT: PASS
CONTENT-HASH: 1c8a634f4609ffc4

## Blocking

## Polish
- solutions.md L2-04 Järkevyys — "juuri näkyvän alueen alapuolella, lähellä ultraviolettia": 365 nm is already ultraviolet (UVA), not near it. — Write "aallonpituus on lähellä ultraviolettia" → "aallonpituus on ultraviolettia, juuri näkyvän alueen ulkopuolella".

## Checked
- Round-1 polish is resolved: L1-01 now says "s, p, d, …" with "1, 3, 5, …", and its check uses the differences of 2, 8, 18, 32 instead of a fifth subshell.
- Recomputed independently in one script, agreeing with answers.py: L1 50, 5,2625 %, 300, 1,5111 eV, −0,544 eV; L2 102,57 nm, 8, 960, 364,70 nm; L3 n = 3,986 → 16 orbitals, 15 (P), 4235.
- L3-01: 1 → 4 is 97,25 nm with these constants, so 97,3 nm is the Lyman line and the rounding to n = 4 is safe.
- L3-03: an exact 2s isodensity region at 90 % gives an inner ball of 5,25 % of the 5,27 % inside the node, which justifies "käytännössä kokonaan". The exact count is 4237, so "noin 4240" is sound.
- L1-02: 421/8000 matches the model's 5,27 % (expected 421,2).
- L2-03: the radii 0,071 and 0,14 nm match the 1s radial distribution (0,0707 and 0,1408 nm).
- Solutions are symbolic first, with eV→J by substitution. The 3-significant-figure rounding follows from 13,6 eV, and the expected counts are called odotusarvo.
- The reasonableness checks are real comparisons: 122 nm for 2p→1s, E_4 against E_3 and E_5, argon as a noble gas, phosphorus.
- Within FY8 scope: E_n is given as data, with no de Broglie and no Schrödinger equation.
