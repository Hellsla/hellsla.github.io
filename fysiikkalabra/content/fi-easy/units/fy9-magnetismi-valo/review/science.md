VERDICT: PASS
CONTENT-HASH: 27b6abb9d4641483
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: unit.md Ydinajatus: "Liikkuvaan varaukseen ... se kohdistaa voiman" holds when the velocity is not parallel to the field; the formula map already uses the perpendicular component, a clause here ("kun liike ei ole kentän suuntainen") would close it.
- A: s7 d, conclusion criterion: "Suihkun protonien yhteinen massa on silti alle nanogramman" is not asked in d; mark it as an extra remark, not a requirement.

## Checked
- Item 18 hunks: hook question, "Etsi virhe" prompt, s1 c (asked quantity, answer), unit.md (loss power in the cable, derivation text), figure "siirto" labels now "häviö 38 %" and "häviö 2,0 W = 0,005 %", aria texts. Numbers around them unchanged.
- s7 recomputed with own formulas: v = 11 245 · 26 659 m/s = 299 780 455 m/s; v/c = 0,99996; c − v = 12,0 km/s = 0,0040 %; rounding interval 2,99762e8 … 2,99799e8 m/s contains c; E1 = 1,0894e-6 J; classical v = 3,61e10 m/s = 120 c; N = 4,0e14; E = 435,7 MJ; mass 6,69e-13 kg; both beams 871 MJ; E_k = 0,5787 MJ; ratio 753 (760 with rounded values); wrong 7,5 MJ and 58. All agree with tasks.json, the solution and answers.py.
- s7 physics: the conclusion in a is the right one (the figures cannot resolve c − v; a particle with mass stays below c); classical E_k rejected for the proton, used for the car; magnetic force perpendicular to the velocity does no work; energy from the cavities' electric field; R = 0 in the superconducting state so RI^2 = 0. Points 3+2+3+3+4 = 15.
- `python scripts/practice.py check units/fy9-magnetismi-valo`: OK. Hash equal at start and end.
