VERDICT: PASS
CONTENT-HASH: 59b9a9f4251795d9
Delta review (Johda itse round 2, 2026-11-12) of the version passed at e7dd805d9fd0ec2b.

## Blocking
(none)

## Polish
(none)

## Checked
1. `unit.md`: $H = \dot{H}t$ is back as a Lisätieto row with its condition (constant dose rate, $t$ defined); the removed Johda itse leaves no dangling reference.
2. `inquiry.json` [16]: point source, power spread over $4\pi r^2$, dose rate proportional to intensity, so $\dot{H}_2 = \dot{H}_1(r_1/r_2)^2$, times $(\tfrac12)^{d/d_{1/2}}$. Recomputed $16\,\mu\text{Sv/h}$. No air attenuation is stated in the unit's model sentence.
3. The en text says the same physics as fi in every changed place; numbers identical.
4. Judged: `git diff 3ec8cc24` of this unit-language (review/ ignored); nothing else changed.
