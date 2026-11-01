VERDICT: PASS
CONTENT-HASH: 52dad39318ce6af1

Science re-review of fy14-quantum-tunnelling, 2026-11-01. It covers the fixes in commit cdc675d6.

## Previous findings
All are resolved:
1. **Strong force and the slow Sun.**
   - The strong nuclear force now only "acts" within a few femtometres. The text and the sunbarrier aria-label both say so.
   - The Sun section says that tunnelling only lets two protons get close.
   - It says that two protons alone cannot stay together, and that one must turn into a neutron ($\text{p} + \text{p} \to \text{d} + \text{e}^+ + \nu$, the weak interaction). That slow step is why the average proton waits about 9 billion years.
   - check-3's feedback says the same. This now agrees with `fy14-fusion-reactions` and with Wikipedia *Proton–proton chain*.
2. **Gamow:** the Sun section now says "Gamow's tunnelling (1928)".
3. **Electron biprism:** the text now says "an electron biprism, which acts like two slits".
4. **Turning distance:** check-explain's model answer says "roughly 1000 fm".

## Changes since the last review
- **pred-tunnel** now asks what happens when the barrier is made twice as wide.
  - The correct option ("far more rarely through the wide one") is the only right one.
  - The numbers in the feedback agree with the table: 7.7 % → 0.60 %, a factor of 12.8 ≈ 13.
  - The "half as often" option is correctly called wrong, because the fall is exponential.
- **proton-wave, Reasonableness:** it compares 779 fm with about 1000 fm, and both values are right.
- **Worked example:** only the unit typesetting changed. The numbers are unchanged (0.123 nm, v = 5.9·10⁶ m/s).

## Blocking
None.

## Polish
None.
