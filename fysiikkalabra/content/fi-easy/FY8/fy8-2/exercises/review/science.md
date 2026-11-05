VERDICT: PASS
CONTENT-HASH: b2a560c9fc804fdc

## Blocking

## Polish
- exercises/solutions.md fy8-2-L3-04 (Järkevyys) — "Peilikuvatasot" is a rather difficult word for selkosuomi; the Finnish source has a similar term, so left unchanged.

## Checked
- Scripted diff against content/fi: same ids, kinds, answers, units, tolerances, correct flags, choices, table captions, columns and every table cell for all 8 new tasks; no differences.
- Every number in task texts, choice feedback and solutions equals the Finnish (decimal comma normalised, token lists equal for all 20 solution sections).
- Decimal comma in text and LaTeX (1{,}51 style) throughout; JSON table cells keep the decimal point exactly as in fi.
- Split sentences keep every datum and assumption (L2-05 all three lines compared, L3-04 sixth line longest and undetected, L3-05 one photon per absorbed photon and rest to heat).
- Recomputed new answers: 2,27 eV; -0,85 eV; 497 nm; 1127 nm (1130 within tolerance); 22,1 % (D: 477 nm); all match.
- L1-06/L1-08: one correct choice each; the absorb-vs-emit reasoning is stated correctly.
- The earlier Polish about "tässä siirtymässä" no longer applies (L3-02 text checked).
- check_i18n.py fi-easy: 0 errors.
