VERDICT: PASS
CONTENT-HASH: b1e8c35e57ad6a01

## Blocking
None. The round-2 item (fy6-s2 c, cable heating) is fixed: the solution's *Kaapeli* paragraph gives $0{,}80\,\Omega \cdot (1{,}76\,\text{A})^2 = 2{,}49 \approx 2{,}5\,\text{W}$, against $5{,}0\,\text{W}$ before, and criterion 2 now grades it. Solution, rubric and question agree. The reason given (power depends on $I^2$) is correct.

## Polish
- s2 d: the key `calculation` now appears twice (current, and lamp voltage).
- s3 c: the `conclusion` criterion repeats "energia ei häviä" from criterion 3.
- s4 a: the rounding reason ("enintään kaksi tai kolme numeroa") is muddled.
- s1 d (C): the 0,03 V drift measured at 0,10 A stands in for the drift at higher currents. That is a fair simplification for the level.

## Checked
- **Round-1 items 1–4 are fixed.**
  - s1 d: the drift is attributed to discharging, and heating to a change in $R_\text{s}$ of uncertain direction.
  - s4: the text now names the voltage-raising circuit.
  - s2 d: the assumptions point is replaced by the lamp voltage, which the question now asks for.
  - s2 b: 17 W with the two-figure reason.
- **s1 drift, recomputed.** The repeat at 0,10 A gives 4,45 V against 4,48 V. Time and current grew together, so a linear drift of at most 0,03 V tilts the slope by at most $0{,}03 : 0{,}50 = 0{,}06\,\Omega$. The corrected slope is about 1,14 Ω and the intercept moves by only 0,006 V. "1,1…1,2 Ω, 1,2 pikemmin yläraja" follows. The $R_\text{s}$ tolerance of 0,09 matches the accepted range 1,1…1,3 Ω.
- **s2 d:** $R_\text{r} I = 2{,}0 \cdot 4{,}286 = 8{,}57 \approx 8{,}6\,\text{V}$, dimmer than 10,0 V. The fuse wording now states its simplification.
- **s4:**
  - Discharge resistor: $300^2 : 10^4 = 9\,\text{W}$, with $\tau = 3{,}3\,\text{s}$.
  - Stored energy: $E \approx 15\,\text{J}$ (14,85 J). $\Delta E = 6{,}86\,\text{J}$, 46 %.
  - Safety: the "älä yritä itse" note is appropriate.
- **s3 figure:** the droplet now starts at the nozzle plate, consistent with "lähtee levossa".
- Round 3 changed only s2 c (verified with git show HEAD). All other numbers are unchanged from round 1 and still agree with my independent recomputation and with answers.py. The points still add up, and practice.py check is OK. The hash is the same at the start and at the end.
