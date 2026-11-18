VERDICT: PASS
CONTENT-HASH: 2f9de8817eb2638d
SCOPE: delta (round 2), new Sovella tasks fy9-kaasut-s8 and s9 (text, figures fy3-10/pt-suorat and fy3-11/pv-isobaari, model answers, rubrics) and the changed intro; s1-s7 not re-judged. Language: en.

## Blocking
(none)

## Polish
- [Minor] pt-suorat: the two lines are solid from 100 K although data points exist only at 200 K and 400 K; the stretch below 200 K is extrapolation and could be dashed. Description gives the two real points per gas.
- [Minor] Axis tick labels in both figures render at about 9-10 px at 360 px; legible, figure correctly scaled inside its card.

## Checked
- Round 1 (visual) had no blocking items; the PASS stands. Round-1 content fixes verified in the current text: s9 piston is movable with weights holding the pressure constant (task text and the isobaric graph agree); s9 c answer tolerance 3 % matches the two-significant-figure model answer 1,2 * 10^3 K (1173 K); the intro no longer calls the last task the source task (s8, s9 are plain figure tasks, source note says invented examples); s9 c reasonableness line (4 * 293 K, about 900 C) consistent.
- Own 360 px captures of s8 and s9 (en page, model answer opened): no horizontal overflow (page scrollWidth 360, task cards 326/326); check_layout --width 360 OK for fi, en, fi-easy.
- Calculation rows aligned at =, units LaTeX with thin space, litre as \textsf{l}, decimal points (en), boxed answers, fractions legible; the s8 c) chain breaks one step per row without clipping.
- Figures sit inside the card; aria-label gives the data points and grid step; axes carry quantity and unit; s9 shows the isobar as a horizontal line with direction arrow and end markers.
