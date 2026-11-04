VERDICT: FAIL
CONTENT-HASH: df595f23b2d33b59

Full review (scope: a changed line carries a symbol). Changes of this round: effective dose is now used to estimate long-term cancer risk for an average person, not anyone's individual risk (Ydinajatus); the example's check says the factor 0,12 gives the effective dose describing whole-body detriment; the misconception says the same effective dose does not guarantee the same individual risk.

## Blocking

1. exit-ticket.json:4 (answer 1) — **B.** "…joten se kuvaa koko kehon pitkän aikavälin syöpäriskiä." This is the unqualified wording the round removed from the theory: it presents effective dose as the person's risk. The exit ticket now disagrees with Ydinajatus and the misconception. Fix: "…joten sen avulla arvioidaan pienten annosten pitkän aikavälin syöpäriskiä keskimääräiselle ihmiselle, ei yksilöllistä riskiä."

## Polish

1. lesson.md Taustasäteily — "tyypillisellä kaukolennolla noin $3\,\mu\text{Sv/h}$": typical cruise-altitude rates at northern latitudes are nearer $4$–$6\,\mu\text{Sv/h}$; "noin $3$–$6\,\mu\text{Sv/h}$" would be safer. Not wrong in magnitude (C).

## Checked

- New theory wording (average person, not individual risk; detriment; origin of radiation not decisive) is right by ICRP 103 usage and consistent within lesson.md.
- Definitions: $D = E/m$ (Gy), $H_\text{T} = w_\text{R}D_\text{T}$, $H_\text{E} = \sum w_\text{T}H_\text{T}$ (Sv); $w_\text{R}$ and $w_\text{T}$ tables match ICRP 103 ($\sum w_\text{T} = 1$); effective dose limited to low doses, deterministic effects in Gy.
- Recomputed: 1 Gy heats water $2{,}4\cdot10^{-4}\,\text{K}$; STUK-A263 shares (radon $68\,\%$, natural $86\,\%$, radon/medical $5$); example $D = 1{,}67\,\text{mGy}$, $H_\text{T} = 33\,\text{mSv}$, $H_\text{E} = 4{,}0\,\text{mSv}$; virhe $1{,}2\,\text{mSv}$; siirto $12{,}5\,\mu\text{Sv}$ (mistakes $37{,}5$, $25$, $50$, $750$); koe-1 $40/10/2{,}5\,\mu\text{Sv/h}$; koe-2 $40/20/10/5\,\mu\text{Sv/h}$; tarkistus-2 $5{,}0\,\text{cm}$. All agree with lesson-answers.py.
- Inverse-square law with its conditions (point source, little air attenuation) and half-value layer as a simplified model (scatter/build-up noted); Cs-137 HVL $5{,}5\,\text{mm}$ Pb, $\approx 4\,\text{cm}$ concrete — right.
- Radon facts: Rn-222 $3{,}82\,\text{d}$, Po-218/214 alpha, $\approx 300$ lung cancers/yr, $94\,\text{Bq/m}^3$, reference levels $300/200\,\text{Bq/m}^3$ (STM 1044/2018), limits $20$ and $1\,\text{mSv/a}$ (859/2018) — right.
- Every choice has exactly one correct option with right feedback; experiments isolate distance and lead thickness.
- Hash same at start and end.
