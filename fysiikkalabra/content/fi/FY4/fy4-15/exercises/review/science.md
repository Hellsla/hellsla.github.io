VERDICT: PASS
CONTENT-HASH: cede2e1f33731164
## Blocking

## Polish
1. lessons/FY4/fy4-15/answers.py, L2-01 comment says 96,56 m³/s; the value is 96,53 (the solution's 96,5 is right). Carried over.

## Checked
- L2-09 Järkevyys, new sentence: "Energia on tehon ja ajan tulo vain, koska tuuli on oletettu tasaiseksi: vaihtelevassa tuulessa teho muuttuu koko ajan, eikä keskinopeudesta luettu teho anna oikeaa energiaa." Correct: $E = Pt$ needs a constant power, and since the power grows roughly as $v^3$, the power at the mean wind speed is not the mean power.
- The sentence agrees with the task (the wind blows steadily at $7\,\text{m/s}$ for $120\,\text{h}$) and with the solution's Periaate (steady wind, constant power).
- Recomputed: $0{,}511\,\text{MW} \cdot 120\,\text{h} = 61{,}32\,\text{MWh}$, as in exercises.json; the estimate $0{,}5\,\text{MW} \cdot 100\,\text{h} = 50\,\text{MWh}$ is a real order-of-magnitude check.
- exercises.json: only the marker (esimerkkiaineisto) left the captions. No number, symbol, unit or answer changed.
- Hash cede2e1f33731164 at the start and at the end.
