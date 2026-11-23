VERDICT: PASS
CONTENT-HASH: 94a61caa786b0a64
SCOPE: delta figure-words-added,numbers,reflow,teacher-figure from 9a921f891663b4d8 base 64d4935

## Blocking

## Polish
- solutions.md:197 (body-fat task, 30 days): the Kaava now writes $30 \cdot \Delta E = m \cdot H$ with "$H = 37\,\text{MJ/kg}$". In FY2, $H$ is a fuel's heating value (lämpöarvo, $E = Hm$). The guardrails keep food energy and fuel heating value apart, and the task calls the 37 MJ "rasvakilon kemiallinen energia". The number is right and so is the result. Fix: use a symbol of its own, for example "$30 \cdot \Delta E = m \cdot E_\text{kg}$, missä $E_\text{kg} = 37\,\text{MJ/kg}$ on rasvakilon kemiallinen energia".

## Checked
- solutions.md:176 (nut bag): writing direct proportionality as $E/m = E_{100}/m_{100}$, then solving for $E$, is the correct basic relation. $50/100 \cdot 2400\,\text{kJ} = 1200\,\text{kJ}$.
- solutions.md:183 (breakfast and walking distance): the same proportionality for each food, then the sum, then $E = s \cdot E_\text{km}$ solved for $s$. I recomputed $750 + 480 + 380 = 1610\,\text{kJ}$ and $1610 : 220 = 7{,}32 \approx 7{,}3\,\text{km}$.
- solutions.md:190 (graph task): $E = ks$ solved for $s$ is correct. The fitted line gives $k = (1260 - 8)/5{,}0 = 250{,}4 \approx 250\,\text{kJ/km}$ and $s = 1500 : 250 = 6{,}0\,\text{km}$.
- solutions.md:197: $10{,}35$ and $11{,}45\,\text{MJ}$, so the deficit is $1{,}10\,\text{MJ}$ a day and $33\,\text{MJ}$ over 30 days. $33 : 37 = 0{,}892 \approx 0{,}89\,\text{kg}$, which matches the task data (10,2 MJ, 5,0 km, 250 kJ/km, 37 MJ/kg).
- figures.json (the teacher-approved figure's words): the energies on the scale are consistent. An apple lifted 1 m is about 1 J. 50 L at 32 MJ/L is 1,6 GJ. OL3 at about 1,6 GW for one day is 138 TJ ≈ 140 TJ. "Pieni väli ×10, merkitty väli ×1000" matches the figure (one major tick every three decades).
- answers.py matches every numeric answer in exercises.json within its tolerance. No answer, unit or tolerance changed.
- Hash 94a61caa786b0a64 at the start and at the end.
