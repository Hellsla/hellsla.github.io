VERDICT: PASS
CONTENT-HASH: 42d45a82e2ac2a0e

## Blocking

## Polish
- solutions.md:266 (L3-04) and solutions.md:299 (L3-05): both distances come from a limit value (55 dB, 70 dB). Rounding 315 m → 3,2·10² m and 44,6 m → 45 m is up, and up is the safe side, as P7c asks. The solutions justify the rounding only by significant figures. Add half a sentence such as "pyöristetään ylöspäin, turvalliselle puolelle".
- solutions.md:310 (L1-09): "kaksi merkitsevää numeroa kuten kuulokynnys" leans on the agreed reference I₀. The level read from the figure, 74,0 dB, would support 2,51·10⁻⁵ W/m². Name the real reason, or give three figures. Both are inside the tolerance.

## Checked
- The hash was the same at the start and at the end.
- One script recomputed all 21 numeric answers. It used L = 10 dB·lg(I/I₀), I = I₀·10^(L/10 dB), I = P/(4πr²), and added the intensities of independent sources. Each value matches answers.py and exercises.json within the tolerance.
- L3-04: my own powers are 0,405, 0,379, 0,428 and 0,366 W, with mean 0,394 W, which gives r = 315 m. The ±0,5 dB range of 297–334 m is right.
- L3-05: I = 2,487·10⁻⁴ + 6,25·10⁻⁵ W/m² gives L = 84,9 dB and r = 44,6 m. L3-01: 12 000 shouts give 82,8 dB, and adding the 80 dB system gives 84,6 dB → 85 dB.
- L2-06: the model gives 67,94 dB, so the difference is +3,96 dB, a factor of 2,5 in intensity. The steps are 5,9, 5,1 and 3,1 dB, so the reflection explanation fits the data. In L2-05 the steps are 6,1, 5,8, 6,1 and 6,1 dB, close to the model's 6,02 dB.
- L2-07: the offsets 4,1, 3,8, 4,2 and 3,9 dB average 4,0 dB, a factor of 2,51. At 90 dB the reading is −1,4 dB instead of +4 dB, so it does not follow the others; microphone overload is a plausible cause, stated as "todennäköisesti".
- L3-03: −5 dB gives I = 3,2·10⁻¹³ W/m². That the hearing threshold depends on the listener and the frequency (it is below 0 dB near 3 kHz) is correct and agrees with the lesson's summary.
- Figure kuvaaja-tehtava: P = 1,6π·10⁻³ W gives 80,0, 73,98 and 67,96 dB, labelled 80,0, 74,0 and 68,0. It shows no power or intensity.
