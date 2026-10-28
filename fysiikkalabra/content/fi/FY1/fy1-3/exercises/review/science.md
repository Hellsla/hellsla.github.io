VERDICT: FAIL
CONTENT-HASH: 989e477708edb711

## Blocking
- solutions.md:117 (L3-02, Sijoitus and Vastaus) — the answer is an error estimate (virhe-arvio), yet it is given as "$2{,}0\,\mu\text{m}$, kaksi merkitsevää numeroa kuten asteikkovälissä". The teacher's rule, and L1-05 in this same set, give an error estimate one significant figure. Fix: write $0{,}002\,\text{mm} = 2\,\mu\text{m}$ and "Vastaus: $2\,\mu\text{m}$, yksi merkitsevä numero, kuten virhearvio ilmoitetaan". Set exercises.json answer to 2 (same tolerance).
- solutions.md:129 (L3-03 Järkevyys) — "Satunnaisvirheen arvio … $= 0{,}025\,\text{cm}$" writes an error estimate with two figures. Fix: "$\approx 0{,}03\,\text{cm}$, noin kymmenesosa systemaattisesta virheestä".

## Polish
- L2-02 Vastaus — "kolmen lukeman keskiarvo kantaa yhden numeron lisää" is not a sound rule. Justify $10{,}7\,\text{mm}$ from the millimetre readings, or give $11\,\text{mm}$ (open since round 2).
- L1-05 Järkevyys — "Virhe-arvio ei voi olla asteikkoväliä suurempi" is too absolute. Write "on tavallisesti enintään puoli asteikkoväliä" (open since round 2).
- L3-01 Järkevyys — "lähes kokonaan" overstates it: two thirds cancel. Write "suurimmaksi osaksi" (open since round 2).
- L1-02 Vastaus — the task asks for the sign, so write $+0{,}3\,\text{cm}$ (open since round 2).
- Spelling — L2-01 now writes "virhearvio", the rest of the set "virhe-arvio".

## Checked
- The round-3 change is L2-01's Vastaus: "$5\,\%$, one figure as in $0{,}09\,\text{s}$ (laskimen arvo $4{,}83\,\%$)". It is right, and tolerance 0.04 accepts 5 (3,5 % off).
- One script recomputed all 12 answers independently, and each matches answers.py exactly.
- L3-03's $\Delta x_\text{sys} = 0{,}26\,\text{cm}$ is a correction subtracted from readings, not an uncertainty, so keeping it at the data's precision is right.
- L1-03 gives the half-range $0{,}35\,\text{s}$ and states that, reported as an error estimate, it is $0{,}4\,\text{s}$. This is consistent with the rule.
- No ×, \times or ÷; \cdot in products; conversions by substitution ($1\,\text{m} = 100\,\text{cm}$, $1\,\text{mm} = 1000\,\mu\text{m}$); error symbols Δx, Δt_sys, ΔL_sys, Δh.
- Content hash is identical at the start and the end.
