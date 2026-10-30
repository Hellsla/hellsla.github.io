VERDICT: PASS
CONTENT-HASH: 9d2d77c8c89ec9d5

## Blocking
None.

## Polish
- teacher.md, first misconception: "pienen vakiotermin (pallon halkaisija)" reads as if the intercept equals the diameter $d$. When both heights are measured to the top of the ball, $H_1 = a H_0 + (1-a)d$, so the intercept is $(1-a)d$, about half the diameter for a tennis ball. The slope is still $a$, as the text says. Suggested wording: "pienen vakiotermin $(1-a)d$". The student text ("koska pallon halkaisija sisältyy kumpaankin korkeuteen") gives the cause and is correct.

## Checked (revision to 8c220426bdaae50d)
- All three earlier polish points are applied correctly. The theory says to measure to the ball's bottom or subtract the diameter; the axes block notes the small intercept from top-to-top measuring; teacher.md now names the speed ratio as the restitution coefficient (iskuluku), $e = \sqrt{a}$.
- Restructure. The all-modes energy paragraph is correct: with little air resistance, potential energy turns into kinetic energy and back, and the bounce turns energy into internal energy and sound. The new section "Tutkimuskysymyksestä mitattaviksi suureiksi" makes no physics claims. The derivation $E_1/E_0 = h_1/h_0$, $h_1 = a h_0$ and its stated conditions (release from rest, small air resistance, the floor at the ball's bottom as the zero level, possible deviations from air resistance or impact speed) are unchanged inside `tuki O OO`. Raportoi still asks every mode why the height ratio is the energy ratio; this fits the independent mode, where students justify the model themselves.
- Setup figure: the drop from rest is now vertical, and the ball drifts only after the bounce. Both heights run from the floor to the ball's bottom ($h_1/h_0 \approx 0.64$). The dashed path's apex matches the ball's bottom.
- Hero (recomputed from the code and the SVG): free fall from rest with constant time steps. Gaps grow by about 11 px per frame, with the first step equal to $g/2$. The rise has the same acceleration and its first step equals $\sqrt{2gh_1} - g/2$. Rise over drop is 0.60. The scale sits behind the ball, which helps when reading heights, and the phone at about bounce height matches teacher.md.
- Model graph, extension $h_{n+1} = a h_n$ (conditional on constant $a$), uncertainty methods, consistency with fy10-jousivakio, and house rules (no \vec, $\bar{h}_1$, \cdot, no invented data): unchanged and correct.
- `scripts/reviews.py hash` does not cover investigations, so this review uses the hash given.
- Revision to 9d2d77c8c89ec9d5 checked: teacher.md now gives the intercept as $(1-a)d$ (correct). The new Ennusta Q2 (proportional growth, very small drop heights) is an open prediction and asserts no physics.
