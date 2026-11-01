VERDICT: PASS
CONTENT-HASH: 849e390d8423fd52

Science re-review of fy14-big-machines, 2026-11-01. It covers the changes in commit 3ed55db3 and what they touch.

## Previous findings
1. Resolved. The Geneva quotation now reads "for the benefit for all mankind", as in the Reagan Library text, with a note on the wording. The `statement` model quotes it the same way.
2. Resolved. Vienna in March 1987 "launched conceptual design studies", and the conceptual design ran 1988–1990. The order item is "The ITER conceptual design begins" (1988), and the three statements now agree.
3. Resolved. The JET dates match the EUROfusion JET report (JETP98054): Culham chosen on 25 October 1977, the Council on 30 May 1978, and the Joint Undertaking working from 1 June 1978.

## New content
- **`machines` table.** I checked each row against the Wikipedia infoboxes on 2026-11-01:

  | Machine | Major radius R (m) | Minor radius a (m) |
  | --- | --- | --- |
  | PLT | 1.32 | 0.4 |
  | TFTR | 2.52 | 0.87 |
  | JET | 2.96 | 1.25 |
  | JT-60, original | 3 | 0.85–0.95 |
  | T-15, original | 2.43 | 0.7 |

  All are correct. The start years are as before.
- **The feedback's claims:**
  - JET's tube is "three times as thick": 1.25/0.40 = 3.1.
  - JET's volume is "more than twenty times PLT's". With circular sections the ratio is $R a^2$ = 21.9. With JET's real 100 m³ against PLT's $2\pi^2 R a^2$ = 4.2 m³, it is 24.
  - Exactly one option is correct, and the distractors' feedback is right.
- **The radius definitions and the reason for size** (heat must travel further): correct at this level.
- **The heating figure:** the injector now sits outside the ring and the beam atoms end inside the plasma band. That is physically right.
- **"Million kelvin"** in place of "degrees" is correct throughout.
- **Rebalanced options** (`review`, `pred-heat`, `check-1`): the same physics, with exactly one correct option each.

## Blocking
None.

## Polish
None.

## Re-check 2026-11-01: photographs
The T-15 stamp is correct: the stamp reads "термоядерная система ТОКАМАК 1987", Wikipedia's T-15 article uses it as "T-15 tokamak on a 1987 USSR stamp", and T-15's first plasma in 1988 matches the text. JET 1991 is the first D–T experiment (9 Nov 1991). Fixed: the JET caption said "The vacuum vessel inside is 6 metres across". The vessel's outer diameter is about 8.5 m (R = 2.96 m, a = 1.25 m). The caption now reads "Its D-shaped vacuum chamber is 4.2 metres high and 2.5 metres wide" (Wikipedia, Joint European Torus). The photos.json caption still has the old sentence.
