VERDICT: PASS
CONTENT-HASH: 9b97de86157d65a5

## Blocking

## Polish
- content/fi/FY4/fy4-8/exercises/solutions.md:274 (fy4-8-L2-10 a) — exact speeds and a mass of $1500\,\text{kg}$ (four significant figures, trailing zeros count) would give four figures; "kolme numeroa ei lupaa liikaa" is true but not the usual rule — either give $52{,}08\,\text{kJ}$, $144{,}7\,\text{kJ}$, $468{,}8\,\text{kJ}$ or keep three and say plainly that three are enough for the comparison.
- solutions.md:248 — $30 : 3{,}6\,\text{m/s} = 8{,}333\,\text{m/s}$ and $13{,}889\,\text{m/s}$ are rounded values: "≈", not "=".
- solutions.md (L2-10 e) — $7716\,\text{J} : 0{,}05\,\text{m} = 154\,\text{kN}$ is shown as "noin $150\,\text{kN}$"; fine with one-figure distance $0{,}05\,\text{m}$, could say so.

## Checked
- All 21 numeric answers recomputed with my own formulas (least-squares fits included): agree with exercises.json and answers.py inside each tolerance.
- L2-10 quotation ("Ajoneuvon törmäysenergia nelinkertaistuu, kun törmäysnopeus kaksinkertaistuu."), $80\,\text{kg}$, $50\,\text{km/h}$, "$3\,000\,\text{kg}$", $12\,000\,\text{kg}$ at $100\,\text{km/h}$ and the pedestrian risk above $60\,\text{km/h}$: the same as the coordinator's record of the Liikenneturva page; dated 16.11.2026; every number needed is quoted in the task, so the task does not depend on a moving value.
- L2-10 a: $52\,083\,\text{J}$, $144\,676\,\text{J}$, $468\,750\,\text{J}$; b: factor 4 for $2v$, $9{,}00$ for 90 against 30 km/h.
- L2-10 c: negative work of the obstacle's force, energy to deformation and internal energy, then to the surroundings as heat; never "muuttuu lämmöksi".
- L2-10 d: "kg" read as the weight of $3000\,\text{kg}$ is said in the task; $F = 29\,430\,\text{N}$, $E_{\text{k}0} = 7716\,\text{J}$, $s = m_\text{i}v^2/(2F) = 0{,}2622\,\text{m}$; work principle of this chapter, constant force stated, symbolic first; answer 0.26, two figures from $80\,\text{kg}$ and $50\,\text{km/h}$.
- L2-10 checks: $a = 368\,\text{m/s}^2 = 37{,}5\,g$; same distance at $100\,\text{km/h}$ gives exactly the weight of $12\,000\,\text{kg}$; $7{,}7\,\text{kN}$ over $1{,}0\,\text{m}$, twenty-fold over $0{,}05\,\text{m}$.
- L2-10 e: energy fixes only $Fs$; the constant force is a mean value (model limit stated).
- L2-05 proofreading fix: $0{,}10\,\text{m}$ is in the data and has two significant figures.
- Notation ($E_{\text{k}0} + W = E_\text{k}$, $W = Fs$) as in the brief; scope FY4.
- Hash the same at the start and the end.
