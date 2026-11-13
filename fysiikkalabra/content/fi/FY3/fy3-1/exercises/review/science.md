VERDICT: PASS
CONTENT-HASH: 803fbf1569f6cbbf
SCOPE: delta added-exercise from 0fe3461097d29d49 base c52e6381769f

## Blocking

## Polish
- exercises/solutions.md (fy3-1-L2-08, Kuvaajan lukeminen) — "vastaus $58$–$62\,\text{N}$ hyväksytään" is a little wider than the stored tolerance 0,03 (58,2–61,8 N), and since the points sit exactly on grid crossings and the answer comes from $g$, no reading spread is involved — say "vastaus lasketaan suoran kulmakertoimesta" or quote the real range.
- exercises/solutions.md (fy3-1-L2-08) — "$G/m = 5\,\text{N/kg}$": the house rule writes $g$ in m/s² only; the solution does convert in Muunnokset, but writing $5{,}0\,\text{m/s}^2$ straight away would be more consistent.

## Checked
- Figure generator: five points $(m, 5m)$ for m = 2…10 kg, on the 2 kg / 10 N grid; the description lists the same points and gives no $g$ or answer.
- Recomputed: $g = 50/10 = 20/4 = 5{,}0\,\text{m/s}^2$, $G = 12 \cdot 5{,}0 = 60\,\text{N}$; answers.py gives 60, so it matches.
- Model $G = mg$ with the same $g$ for every body at one surface; extrapolating to 12 kg (just past the range of the data) is justified by proportionality, as the solution says. FY3 scope, no Newton's laws.
- Unit N; two significant figures justified by 12 kg; the reasonableness check (1,2 × 50 N) really checks the result.
- Solution complete: given, principle, how the graph is read, formula in symbols, conversions, substitution with units, rounding, check.
- $g = 5\,\text{m/s}^2$ is a plausible value for an imagined celestial body.
- Rest of the set unchanged since PASS (packet: added_exercises verified).
- Hash same at start and end.
