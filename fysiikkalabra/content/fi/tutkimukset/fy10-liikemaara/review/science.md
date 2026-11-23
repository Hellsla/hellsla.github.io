VERDICT: PASS
CONTENT-HASH: 2554de77f83e90de

## Blocking
None.

## Polish

- investigation.md line 218: the example question "onko liikemäärä jälkeen useimmiten pienempi kuin ennen?" would fit the negative case better with "suuruus".
- Model graph: the slope is drawn at about 31° (carried from the previous report). Equal axis scales would show "kulmakerroin 1" more clearly.

## Checked

- teacher.md, first velocity bullet: the first sentence now reads "vierimisvastus näkyy järjestelmällisenä erona kokonaisliikemäärissä ennen törmäystä ja sen jälkeen". It claims no sign, so it is correct, and it no longer contradicts the conditioned sign rule that follows it.
- Sign rule at investigation.md line 240 and in teacher.md: if each cart moves along $p_\text{kok}$ or is at rest before the collision, the net rolling-resistance force before and after the collision opposes $p_\text{kok}$.
  - After the collision, only the lighter cart can bounce back, for any $0 \le e \le 1$.
  - So $|p'_\text{kok}| < |p_\text{kok}|$ in the measurement: the points lie below the line for $p>0$ and above it for $p<0$.
  - My script checked 200 000 random collisions of this kind (read 0,5 s off the collision, a stopping cart clamped at zero) and found 0 violations.
  - Bounce case with the target at rest and $m_1<m_2$: 0,205 → 0,195, still a decrease.
- Head-on case: before the collision the friction impulses partly cancel ($\propto m_1-m_2$). After it, they depend on the directions of the velocities. "riippuu vaunujen massoista ja nopeuksista" is correct in both files.
- The first sentence at line 240 ("poikkeavat järjestelmällisesti", no sign) is correct.
- The model-figure aria-label ("Mallikuvaaja … mallin mukaan") matches the figure. Its claim that a point lies below the line when the magnitude decreases covers only the positive quadrant shown, so it is correct.
- I found no other sign claim on this point in investigation.md, teacher.md or investigation.json; lines 125, 164 and 256 are only qualitative.
