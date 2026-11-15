VERDICT: PASS
CONTENT-HASH: 570b93738d02c5c4
Mode: delta (round 2, commit ccaa3b7: fy4-k3 c Vastaus and d Järkevyys)

## Blocking

## Polish
- fy4-k6 b Mallivastaus says the curve drops under the weight line "noin hetkestä $0{,}33\,\text{s}$". Linear interpolation of the table gives $0{,}34\,\text{s}$, and both fit "noin". Optional.

## Checked
- The round-1 Blocking item is fixed. fy4-k3 c now compares two decelerations: $5{,}0\,\text{m/s}^2$ is more than "suurin hidastuvuus $3{,}9\,\text{m/s}^2$, jonka lähtökitka voi laatikolle antaa" ($\mu_0 g$). The units now agree, and the term rule is followed.
- fy4-k3 d Järkevyys now says "Liukukitka on pienempi kuin lähtökitka". This is a correct force comparison ($\mu N < \mu_0 N$), and it follows that the sliding crate's deceleration is smaller than $3{,}9\,\text{m/s}^2$.
- The diff touches only these two lines in the exam files. tasks.json, answers.py and figures.py are unchanged, so every number recomputed in round 1 still holds. The rubrics and the points are unchanged.
- No "liikekitka" is left in the exam. Lähtökitka is introduced in k1 f as "täysin kehittynyt lepokitka eli lähtökitka" and later called "lähtökitka".
- The hash was identical at the start and the end.
