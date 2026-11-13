VERDICT: PASS
CONTENT-HASH: 97e11574a538b880
SCOPE: delta added-exercise from 3a2e90bccdbd2345 base 81db4a6fd727

## Blocking

## Polish
- content/fi/FY4/fy4-11/exercises/solutions.md (L3-06 Vastaus) — "kolmas numero säilytetään, ettei välitulosten pyöristys vääristä tulosta": 10,5 kN is the final answer, not an intermediate result. Better: "$11\,\text{kN}$ (kaksi merkitsevää numeroa); laskettu arvo $10{,}5\,\text{kN}$." Also "Massa" is capitalised after a comma.
- exercises.json L1-09 — the text names the braking distance $s$, while the chapter uses $s_\text{j}$. Carried over from round 1.

## Checked
- The round-2 blocking findings are fixed. solutions.md has no literal TAB left (grep over every language's file). The five units are `\text{m}`, `\text{kg}`, `\text{m/s}` and `\text{kN}` again.
- L1-09 Vastaus now leads with $s \approx 30\,\text{m}$ (calculated 31 m). The reason given is that μ = 0,8, the top of the MAFY range, has one significant figure. The answer and its reasoning now agree, and with tolerance 0,05 both 30 m (4,6 % off) and 31 m are accepted.
- L1-09 physics: level road, locked sliding wheels, air resistance left out, N = mg, so a = μg and s = v₀²/(2μg). The other end of the range, μ = 0,5, gives 50,3 m, as the solution says.
- Recomputed in one script (my formulas beside python -I answers.py): L1-09 31,46 m; L2-09 20 m + 25 m = 45 m; L3-06 17,5 kN − 7,0 kN = 10,5 kN. All agree with exercises.json.
- L3-06 tolerance 0,05 accepts 11 kN (4,8 %). The force ratio 2,5 equals the inverse ratio of the stopping times.
- Hash 97e11574a538b880 at the start and at the end.
