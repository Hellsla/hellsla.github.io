VERDICT: PASS
CONTENT-HASH: 678dc353273487b6

Round 2 (delta review of round 1 fixes; round 1 hash fc0aa5da26550049). Science review of fy9-ympyraliike.

## Round 1 Blocking: verified fixed
1. unit.md, "Tasainen ympyräliike": now says that $a_\text{n} = \tfrac{v^2}{r}$ holds at one instant when the speed changes, and that at the highest and lowest points there is no tangential force, so the net force points to the centre. This covers s6 b–d and tarkistus-1. solutions.md s6 b Periaate adds "Pohjalla tangentin suuntaista kokonaisvoimaa ei ole". The physics is correct, and it stays within the fy5-4 "hetken ympyräradalla" treatment. Seen rendered in the preview at 390.
2. inquiry.json lumilapio, Sijoitus: now "takakäden suhteen", which matches the Periaate and the hints. The number (142,8 N) is unchanged.

## Polish: verified
- teacher.md Nopeat: asks "millä nopeudella"; $\sqrt{gr} = 9{,}90\,\text{m/s}$ for r = 10 m (recomputed).
- tarkistus-1 feedback: $F - G = m\tfrac{v^2}{r}$, so the period symbol $T$ no longer clashes.
- s2 d: "43 kertaa korkeammalla" (35 786/830 = 43,1), and the slant distance "yli 38 000 km". Recomputed: 39 400 km at 60° N and 40 400 km at 70° N on the satellite's meridian, so the claim is correct. The rubric says "yli 40 kertaa kauempana", which is consistent.
- Tutki tolerance 0,07 accepts 11,1–12,8 h. A coarse reading of 26 000 km and 4,0 km/s gives 11,3 h and is now accepted.
- s3 d answer 0,4948 s, tolerance 0,04. Without the intercept $\sqrt{1{,}95/8{,}0} = 0{,}494$ s, and both values are accepted.

## No new problems
The other numbers are unchanged from round 1. `practice.py check` passes (6 tasks, 95 points). The preview builds with 0 `.katex-error` and no console errors.

## Polish (optional)
- unit.md: "tangentin suuntaista voimaa ei ole" assumes no friction. "kokonaisvoimalla ei ole tangentin suuntaista osaa" would be more exact. This is not blocking.
