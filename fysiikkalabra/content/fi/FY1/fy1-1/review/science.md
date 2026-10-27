VERDICT: PASS
CONTENT-HASH: 854339dfffa32b9d

## Blocking

## Polish
- lesson.md:46 — "Pienimmäksi mielekkääksi pituudeksi kutsutaan Planckin pituutta" claims more than is known. The Planck length is the scale at which current theories are expected to fail, not a proven smallest length. — Fix: "Planckin pituus, noin 1,6·10^-35 m, on mittakaava, jolla nykyiset teoriat lakkaavat toimimasta."
- inquiry.json exp-2 hint 3 — "Aseta L lähelle tulosta" is ambiguous. mainObj picks the object nearest L + log10(150/560) ≈ L − 0,57, so the ×10 steps from 27,5 land on L = −4,5, where the nearest object is the red blood cell (n = −5). A student who records that row and types its n is marked wrong. — Fix: "Aseta $L = -4$" (the hair, n = −4).

## Checked
- Round-1 blocking item fixed: the Milky Way is at exponent 21 in figures.py and lesson.md (marker x = 476,5 ≈ X(21) = 476,6; the aria-label says 21). It now agrees with check-3 and the sim (9,5·10^20 m).
- Round-1 polish fixed. The exp-2 mistake is now 4,4·10^26, my recomputed mean of the sizes in metres. L2-04 gives 1,31 million with three figures (109,45³ = 1,311·10^6). The menetelmat item reads "Maan radan säde (1 AU)". helio and oort have the radius line (radiusLine at R = S/2, ext = 2m, so it matches the radius label). The refactored orbitPicture call is unchanged in behaviour.
- New L1-04: Venus–Earth at closest approach, 4,10·10^10 m, is realistic (about 38–43 Gm). t = s/c = 136,7 s → 137 s (3 s.f.), as in answers.py and the solution. The symbolic step, the units and the reasonableness check (shorter than the Sun's 500 s) are correct.
- exp-2 with min 3: at L = −4 the nearest object is the hair (log 7,0·10^-5 = −4,15, round to −4), so the solution's "hius, n = −4" and the answer −4 hold. The initial states and the controlled settings are unchanged.
- Planck length 1,6·10^-35 m, "laskettu luonnonvakioista, ei mitattu suoraan": correct (√(ħG/c³)).
- answers.py rerun: every value is unchanged except L1-04. Exercise and inquiry answers match.
- The light-time figure (Moon 1,28 s, Sun 8,3 min, Proxima 4,2 a) is still correct.
- check-3 marked optional: its physics is unchanged.
- Hash unchanged at the start and the end.
