VERDICT: PASS
CONTENT-HASH: bc5536b6e38b6e01

## Blocking
None.

## Polish
- Round-1 points handled: a) model answer now has two ramp points and the 0,4 s point on the line; b) accepts t ≥ 0,4 s or t ≥ 0,6 s; c) mentions sub-pixel centroids; d) stays qualitative.
- The fit range is now inconsistent in places. The solution uses 0,4–2,0 s, but `answers.py` (comment and `floor` filter) still fits t ≥ 0,6 s. A fit on 0,4–2,0 s gives v = 0,7998 m/s and s0 = −0,1609 m, so c's "0,799 m/s" is the t ≥ 0,6 s value. Either range gives 0,80 m/s, −0,16 m and 7,8 m, so nothing changes at the stated precision. Align answers.py (or write "noin 0,80 m/s" in c).
- figures.py alt text still says "Kolme ensimmäistä pistettä ovat rampilta ja kaartuvat ylöspäin". The figure colours only two points (t < 0,3) and the model answer says two, so update the alt text.

## Checked
- Recomputed both fits: t ≥ 0,4 s gives k = 0,7998 m/s, s0 = −0,1609 m, s(10 s) = 7,84 m, residuals within ±2 mm. t ≥ 0,6 s gives 0,7993 / −0,1601 / 7,83. Read-off points (0,6; 0,32) and (2,0; 1,44) give 0,80 m/s. Both ramp points lie above the floor line (+0,16 m and +0,04 m), as the model answer says.
- d criterion "testattu vain 0,4–2,0 s", tagged transfer, matches the solution (1,6 s span, more than 6× extrapolation).
- s2 edits (tuhannesosasekunnit, split flaws list, vacuum sentence removed) leave the numbers unchanged: 2,37 ± 0,08 s, 2,40 ± 0,07 s, difference 0,03 s. The half-range convention is fine, and the SEM alternative is accepted.
- Points unchanged: 12 / 15 / 14. Criteria sum to each part's points.
- Scope unchanged (FY1 only). Data still labelled as examples.
- Content hash bc5536b6e38b6e01 at start and end.
