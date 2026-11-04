VERDICT: PASS
CONTENT-HASH: 141c2ca7c9b3b1f4

Follow-up review of the fix commit 2c31ff041 (delta from 898bd317b4c1c97d, whose full review is kept below). Change: exit-ticket.json:4, answer 1.

## Blocking

None.

## Polish
- inquiry.json transfer (siirto, :309): "three significant figures like $1.80\,\text{mSv/h}$; the ratios … are exact", but $1.0\,\text{m}$, $3.0\,\text{m}$, $15\,\text{min}$, $6.0\,\text{mm}$ carry two figures; give the data three figures or justify differently.
- Lesson :346: "about $3\,\mu\text{Sv/h}$ on a typical long-haul flight" is at the low end; "a few µSv/h" would be safer (C).

## Checked
- Earlier blocking item resolved: "…so it is used to estimate the long-term cancer risk of small doses for an average person, not an individual's exact risk." Right by ICRP 103 usage.
- Consistency: grep of "cancer risk"/"individual"/"whole body" — Key idea (:300), worked example's "radiation detriment to the whole body" (:622) and misconception (:625) agree with it.
- Recomputed: $1\,\text{Gy}$ warms water $0.00024\,\text{K}$; natural 86 %, radon 68 %; tissue factors sum to 1; example $1.67\,\text{mGy}$, $33\,\text{mSv}$, $4.0\,\text{mSv}$; predictions $10.0$, $2.50$, $20.0$/$10.0$/$5.00\,\mu\text{Sv/h}$; error item $1.2\,\text{mSv}$; transfer $12.5\,\mu\text{Sv}$ (mistakes 37.5, 25, 50, 750); check 2 $5.0\,\text{cm}$. All agree with lesson-answers.py.
- Facts: STUK-A263, Rn-222 $3.82\,\text{d}$, Po-218/214, ~300 lung cancers, $94\,\text{Bq/m}^3$, 300/200 Bq/m³, 20/1 mSv, $w_\text{R}$, Cs-137 HVL: correct.
- Inverse-square and half-value models stated with conditions; sim model box agrees.
- Every choice has exactly one correct option; experiments lock all but the varied parameter.
- Hash at start and end: 141c2ca7c9b3b1f4.
