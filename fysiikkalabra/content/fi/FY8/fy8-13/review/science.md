VERDICT: PASS
CONTENT-HASH: e173669c713bd9b1

Follow-up review of the fix commit 2c31ff041 (delta from df595f23b2d33b59, whose full review is kept below). Change: exit-ticket.json:4, answer 1.

## Blocking

None.

## Polish

1. lesson.md:346 — "tyypillisellä kaukolennolla noin $3\,\mu\text{Sv/h}$": northern cruise rates are nearer $4$–$6\,\mu\text{Sv/h}$; "noin $3$–$6\,\mu\text{Sv/h}$" would be safer (C).

## Checked

- Earlier blocking item resolved: "…joten sen avulla arvioidaan pienten annosten pitkän aikavälin syöpäriskiä keskimääräiselle ihmiselle, ei yksilöllistä riskiä." Right by ICRP 103 usage.
- Consistency: grep of "syöpäriski"/"yksilö"/"koko kehon" — Ydinajatus (:300), example check (:622, "koko kehon säteilyhaittaa", detriment, fine) and misconception (:625) now agree with the exit ticket.
- Definitions: $D = E/m$ (Gy), $H_\text{T} = w_\text{R}D_\text{T}$, $H_\text{E} = \sum w_\text{T}H_\text{T}$ (Sv); $w_\text{R}$, $w_\text{T}$ match ICRP 103; deterministic effects in Gy.
- Recomputed: 1 Gy heats water $2{,}4\cdot10^{-4}\,\text{K}$; STUK-A263 shares (radon $68\,\%$, natural $86\,\%$); example $1{,}67\,\text{mGy}$, $33\,\text{mSv}$, $4{,}0\,\text{mSv}$; virhe $1{,}2\,\text{mSv}$; siirto $12{,}5\,\mu\text{Sv}$ (mistakes $37{,}5$, $25$, $50$, $750$); koe-1 $40/10/2{,}5\,\mu\text{Sv/h}$; koe-2 $40/20/10/5\,\mu\text{Sv/h}$; tarkistus-2 $5{,}0\,\text{cm}$. All agree with lesson-answers.py.
- Inverse-square law and half-value layer with their conditions; Cs-137 HVL $5{,}5\,\text{mm}$ Pb, $\approx 4\,\text{cm}$ concrete.
- Radon facts, reference levels (1044/2018) and dose limits (859/2018) right.
- Every choice has exactly one correct option; experiments isolate distance and lead thickness.
- Hash same at start and end.
