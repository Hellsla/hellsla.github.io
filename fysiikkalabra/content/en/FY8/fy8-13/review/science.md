VERDICT: FAIL
CONTENT-HASH: 898bd317b4c1c97d

## Blocking
- exit-ticket.json:4 (answer to question 1) — **B**: "so it describes the long-term cancer risk to the whole body" is the unconditioned claim this round removed from the lesson. The Key idea now says the effective dose estimates the long-term cancer risk of small doses for an average person, not anyone's individual risk, and the misconception paragraph says the same effective dose does not guarantee the same individual risk. Fix: "… so it is used to estimate the long-term cancer risk of small doses for an average person (radiation detriment), not an individual's exact risk."

## Polish
- inquiry.json transfer (siirto): the answer reasons "three significant figures like $1.80\,\text{mSv/h}$; the ratios of the distances … are exact numbers", but $1.0\,\text{m}$, $3.0\,\text{m}$, $15\,\text{min}$ and $6.0\,\text{mm}$ are data with two figures, so a student who writes $13\,\mu\text{Sv}$ is 4 % off and gets "close". Give the data three figures ($1.00\,\text{m}$, $3.00\,\text{m}$, $15.0\,\text{min}$) or justify differently.
- Lesson: "about $3\,\mu\text{Sv/h}$ on a typical long-haul flight" is at the low end (northern routes are often 4–6 µSv/h); "a few µSv/h" would be safer.

## Checked
- New wording: effective dose for small doses and an average person (Key idea), same effective dose ≠ identical individual risk (Common misconception), radiation sickness assessed in grays (Formula): correct and consistent with each other and with the worked example's "radiation detriment".
- Recomputed in one script: $1\,\text{Gy}$ warms water $0.00024\,\text{K}$; natural share 86 %, radon 68 % (two thirds), radon/health care 5; ICRP 103 tissue factors sum to 1; worked example $1.67\,\text{mGy}$, $33\,\text{mSv}$, $4.0\,\text{mSv}$; predictions $10.0$, $2.50$, $20.0$/$10.0$/$5.00\,\mu\text{Sv/h}$, $1.25$ at 30 mm; error item $1.2\,\text{mSv}$; transfer $12.5\,\mu\text{Sv}$ (mistakes 37.5, 25, 50, 750); check 2 $5.0\,\text{cm}$, $2.5\,\mu\text{Sv/h}$ at 25 cm. All agree with lesson-answers.py.
- Facts: STUK-A263 figures, Rn-222 $3.82\,\text{d}$, Po-218/Po-214 alpha, ~300 lung cancers, $94\,\text{Bq/m}^3$, reference levels 300/200 (STM 1044/2018), dose limits 20/1 mSv (859/2018), $w_\text{R}$ table, Cs-137 half-value thickness 5.5 mm lead / ~4 cm concrete: correct.
- Inverse-square law and half-value model stated with their conditions (point source, little air attenuation, scattered photons ignored); the sim's model box says the same and sim-spec matches.
- Every choice has exactly one correct option with right feedback; experiments lock all but the varied parameter.
- Hash at start and end: 898bd317b4c1c97d.
