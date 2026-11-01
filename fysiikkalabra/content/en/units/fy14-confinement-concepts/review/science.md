VERDICT: FAIL
CONTENT-HASH: f99d2c16745c6793

## Blocking
1. **A, `unit.md` section *Inertial confinement*, paragraph 3.** "For the first time, a fusion experiment gave out more energy than the energy put into the fuel" is wrong twice. First, the $2.05\ \text{MJ}$ was laser energy delivered to the *target* (the hohlraum); the fuel absorbed only a small fraction of it. Second, NIF already passed "fuel gain" above 1 in 2013–2014 (Hurricane et al., *Nature* 2014). The 2022 first was fusion energy above the laser energy on target. Fix: "For the first time, a fusion experiment released more energy than the laser energy delivered to its target: the **target gain** was about 1.5."
2. **A/B, `unit.md` *Common misconception*.** "Ignition means that the fuel produced more fusion energy than the laser energy that reached it, $G > 1$" makes the same fuel/target confusion. Fix: "… more fusion energy than the laser energy delivered to the target, $G > 1$ (LLNL's working definition; physically, ignition means that the fusion alphas heat the fuel faster than it loses heat)."

## Polish
1. **`inquiry.json` nif-data table, 12 Feb 2024.** LLNL gives $5.2$ MJ as an *estimate*. Write "about $5.2$ (estimated)" so that a measured value and an estimate are not mixed without a label.
2. **`unit.md` *Inertial*, paragraph 4.** "NIF fires a few hundred shots a year": date it, and note that most shots are not ignition shots. Wikipedia's source gives one shot about every two days (2014).

## Checked
- Recomputed: $G = 3.15 : 2.05 = 1.54$; $3.15 : 300 = 1.05\ \%$; $2.05 : 300 = 0.68\ \%$; $300 : 3.15 = 95$ ("about a hundred"). 7 April 2025: $8.6 : 2.08 = 4.13$; the mistakes 0.242 and 6.52 are correct. Gain needed: $300 : 2.08 = 144$, which is 35 times 4.13.
- **NIF framing.** The worked example, prediction 2, the bar chart (drawn to scale), find-error and the summary all separate target gain from wall-plug electricity. Apart from Blocking 1–2 this is done well. LLNL page fetched 2026-11-01: 11 ignition shots up to 20 June 2026, highest gain 4.13 (7 Apr 2025). The table values match.
- **Company claims.** CFS/SPARC, Helion/Microsoft 2028 and General Fusion (25 % staff cut, 2025) are labelled as claims or targets and dated "as of November 2026". STEP 2040 and ITER D–T 2039 are labelled as public plans. "No device has produced net electricity" is dated. The claims sort has one correct category for each item.
- Physics: Z-pinch figure ($I$ to the right, field ⊙ above and ⊗ below, $J \times B$ inward) is correct; theta-pinch field along the axis; parallel currents attract. ZETA's 1958 neutrons were not thermonuclear; Scylla I 1958 was thermonuclear; START 1991; MAST-U 2020; MIT/CFS 20 T on 5 Sep 2021; HTS at about 20 K vs 4 K. Aspect-ratio figure: about 3.3 and 1.7.
