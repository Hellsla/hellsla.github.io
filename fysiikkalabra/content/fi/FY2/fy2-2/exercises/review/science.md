VERDICT: PASS
CONTENT-HASH: 4e7c5cec5ef77cce
SCOPE: delta numbers,reflow from 5d123ece9cf19afa base 64d4935

## Blocking

## Polish
- solutions.md:235 (L3-05 Kaava) — the new symbol $H$ for "energy per kilogram of fat" is the heating-value symbol of the later chapter on fuels, and the guardrails keep a food's energy content apart from a fuel's heating value; this chapter's brief never defines $H$. Write the relation in the task's own words ("rasvakilon energia $E_\text{kg} = 37\,\text{MJ/kg}$", $30 \cdot \Delta E = m \cdot E_\text{kg}$) or name $H$ explicitly as energy per kilogram (C, the physics is right).
- solutions.md L1-10 Vastaus: the thermochemical kilocalorie (4,184 J) point from earlier is still open (0,07 %, C).

## Checked
- Hash 4e7c5cec5ef77cce at the start and the end; only solutions.md changed (four Kaava lines), exercises.json and answers.py untouched.
- L1-07: $E/m = E_{100}/m_{100}$ is the right proportionality, $E = 0{,}50 \cdot 2400\,\text{kJ} = 1200\,\text{kJ}$.
- L2-05: the proportionality per food and $E = s \cdot E_\text{km}$ give $1610\,\text{kJ}$ and $s = 7{,}3\,\text{km}$ (recomputed 7,32).
- L2-07: $E = k s$ from the fitted line, $k = (1260 - 8)\,\text{kJ} : 5{,}0\,\text{km} \approx 250\,\text{kJ/km}$, $s = 6{,}0\,\text{km}$; a fitted line not through the origin is still fine at this precision (8 kJ offset ≪ 1500 kJ).
- L3-05: energy balance $30\,\Delta E = m \cdot 37\,\text{MJ/kg}$, $\Delta E = 11{,}45 - 10{,}35 = 1{,}10\,\text{MJ}$, $m = 0{,}892 \approx 0{,}89\,\text{kg}$; 37 MJ/kg is a realistic value for fat.
- Recomputed all 21 numeric answers in one script: every answers.py value agrees with exercises.json within its tolerance (L1-02 2,27 → 2,3; L2-04 954,5 → 950; L3-02 3194 → 3200; L3-03 1,16·10⁷ → 1,2·10⁷ l within 5 %).
- No unit, tolerance or answer changed; every changed Kaava solves symbolically before substitution.
