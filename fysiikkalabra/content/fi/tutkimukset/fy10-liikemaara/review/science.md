VERDICT: FAIL
CONTENT-HASH: 1d06f92ebbede882

## Blocking

1. **B: teacher.md, first bullet on velocities, first sentence.** It still says, with no condition, that "vierimisvastus näkyy siinä, että kokonaisliikemäärän itseisarvo pienenee järjestelmällisesti". The new third sentence of the same bullet says that in a head-on collision the direction of the deviation depends on the masses, so the two sentences contradict each other. Counterexample: $m_1 = 0{,}5$ kg at $+0{,}40$ m/s and $m_2 = 1{,}0$ kg at $-0{,}10$ m/s, read 0,5 s early with $a = 0{,}02\ \text{m/s}^2$. The measured $p_\text{kok}$ is 0,095 instead of 0,100 kg·m/s, so its magnitude grows towards the collision. Wording I accept for the first sentence: "Nopeuksia luetaan liian kaukaa törmäyksestä, jolloin vierimisvastus näkyy järjestelmällisenä erona kokonaisliikemäärissä ennen törmäystä ja sen jälkeen." The rest of the bullet can stay as it is.

## Polish

- In the last sentence (both files), "riippuu vaunujen massoista" could read "riippuu vaunujen massoista ja nopeuksista". After the collision, the friction impulse also depends on which way each cart moves.
- investigation.md line 218: "onko liikemäärä jälkeen useimmiten pienempi kuin ennen?" is only an example question. "suuruus" would fit the negative case.
- Model graph slope drawn at about 31° (carried from the previous report).

## Checked

- New wording at investigation.md line 240 is correct. If each cart moves along $p_\text{kok}$ or is at rest before the collision, the net rolling-resistance force before the collision opposes $p_\text{kok}$. After the collision it opposes $p_\text{kok}$ too: a cart can bounce back only if it is the lighter one, and this holds for $0 \le e \le 1$. So $|p'_\text{kok}| < |p_\text{kok}|$, which puts the points below the line for $p>0$ and above it for $p<0$. I checked this in a script over 200 000 random same-direction or target-at-rest cases ($e$ from 0 to 1, read 0,5 s off the collision, stopping cart clamped at zero) and found 0 violations. The bounce case $m_1<m_2$ with the target at rest also decreases: 0,205 → 0,195.
- Head-on statement: the friction impulses partly cancel ($\propto m_1-m_2$ before the collision) and the sign can go either way. Correct.
- The first sentence at line 240 ("poikkeavat järjestelmällisesti", no sign) is correct.
- Model-figure aria-label ("Mallikuvaaja … mallin mukaan"): matches the figure. Its claim that a point lies below the line when the magnitude decreases is limited to the positive quadrant shown, so it is correct.
- I found no other sign claim on this point in investigation.md, teacher.md or investigation.json (lines 125, 164 and 256 are only qualitative).
