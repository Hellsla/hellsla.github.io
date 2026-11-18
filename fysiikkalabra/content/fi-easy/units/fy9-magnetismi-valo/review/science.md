VERDICT: FAIL
CONTENT-HASH: 77f6edd72ebe61ef
SCOPE: delta: new Sovella tasks s8 (Laserkoe akryylilevyllä) and s9 (Käämin vuo ja induktiovirta) and the changed intro; s1-s7 untouched, not re-judged.

## Blocking
- s9, Yleisiä virheitä, line 2 (A, quantitative): "$\text{mWb}$ jää muuntamatta yksiköksi $\text{Wb}$, jolloin jännite on tuhannesosa oikeasta" is the wrong way round. Without the conversion, $120 \cdot 8{,}0 / 0{,}40 = 2400\,\text{V}$, which is a thousand times too large. Fix, for example: "Silloin jännite on tuhat kertaa liian suuri ($2400\,\text{V}$)." The standard Finnish text has the same error.

## Polish
- s8, Yleisiä virheitä, line 1: the inverted slope is $0{,}30 : 0{,}45 \approx 0{,}67$, not $0{,}30 : 0{,}44 = 0{,}68$. The conclusion holds.
- s8 b Periaate: "Taitekerroin kertoo, kuinka paljon hitaammin valo etenee aineessa" is correct as a ratio ($n = c/v$). The symbolic form follows straight after it, so this is no finding.
- The Yleisiä virheitä and Hyväksytään myös lines are word for word the standard Finnish ones, with long sentences. That is a language-level point for the pedagogy reviewer, not physics.

## Checked
- `units.py hash --lang fi-easy` gave 77f6edd72ebe61ef at the start and at the end. `practice.py check` OK.
- I read the fi-easy task text, parts, criteria and solutions of s8 and s9, and the intro.
- Numbers: every number in the s8/s9 solutions is the same as in the standard Finnish text (checked by script). My recomputation agrees:
  - s8: $n = 1{,}5$ from the line points $(0{,}30; 0{,}44)$ and $(0{,}60; 0{,}89)$, which my refit of the fy7-10 data confirms; $2{,}0 \cdot 10^8\,\text{m/s}$; $0{,}75\,\text{ns}$; $42^\circ$.
  - s9: $2{,}4$ and $1{,}8\,\text{V}$; $0{,}37\,\text{J}$; $0{,}25\,\text{s}$.
- The shorter sentences keep every physical step and condition:
  - TIR only from the denser medium, with the refraction angle $90^\circ$ at the critical angle.
  - Zero incidence gives zero refraction, so the line goes through the origin.
  - Both Lenz directions.
  - The voltage depends on the rate of change of the flux, not on its value.
- s8 c and s9 a are split into two sentences with the question last. The meaning is unchanged.
- Rubric points add up (s8 15, s9 12). The units and tolerances are as in fi.
- Intro: "Yhdeksän" and "Seitsemäs tehtävä on soveltava aineistotehtävä" are correct for the set.
