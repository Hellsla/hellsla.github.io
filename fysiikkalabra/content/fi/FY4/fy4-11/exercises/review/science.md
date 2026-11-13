VERDICT: FAIL
CONTENT-HASH: a3d98dd8add4fb25

## Blocking
- content/fi/FY4/fy4-11/exercises/solutions.md:279 and :301 — (A, units) four units contain a literal TAB character where `\t` should be: `$30\,<TAB>ext{m}$`, `$31\,<TAB>ext{m}$` (L1-09), `$70\,<TAB>ext{kg}$`, `$15\,<TAB>ext{m/s}$` and `$11\,<TAB>ext{kN}$` (L3-06). A tab is only whitespace in TeX, so these render as italic "extm", "extkg" and so on, and the student sees no unit. — Fix: replace each TAB + "ext" with `\text`, and look for the same problem wherever the round-2 edit was written.
- content/fi/FY4/fy4-11/exercises/solutions.md:279 (L1-09 Vastaus) — (A, internal consistency of the rounding) the line gives the answer as $31\,\text{m}$, then argues that μ = 0,8 has one significant figure so "tulos on noin 30 m", then says "ilmoitettuna 31 m" with no reason. A one-figure argument gives 30 m (3 · 10¹ m), so the stated answer and its reasoning disagree. — Fix: lead with $30\,\text{m}$ (one significant figure, as μ = 0,8), and give 31,5 m only as the calculated value. If two figures are kept, give the reason, for example the comparison with the other end of the range, 50 m. With tolerance 0,05 both 30 m (4,6 % off) and 31 m are accepted, so exercises.json can stay as it is.

## Polish
- content/fi/FY4/fy4-11/exercises/solutions.md:301 (L3-06 Vastaus) — "kolmas numero säilytetään, ettei välitulosten pyöristys vääristä tulosta": 10,5 kN is the final answer, not an intermediate result. Better: "Vastaus 11 kN (kaksi merkitsevää numeroa); laskettu arvo 10,5 kN." Also "Massa" is capitalised after a comma.
- exercises.json L1-09 — the text names the braking distance $s$; the chapter uses $s_\text{j}$. Carried over from round 1.

## Checked
- The round-1 blocking findings on tolerance are fixed: L1-09 and L3-06 now have tolerance 0,05. A student who rounds to 30 m (4,6 %) or to 11 kN (4,8 %) is accepted.
- L1-09 Periaate now says "jarrutusmatka saadaan kaavasta v₀² = 2as", which is the right term.
- Recomputed in one script (my formulas beside python -I answers.py): L1-09 s_j = (22,22 m/s)²/(2 · 0,8 · 9,81 m/s²) = 31,46 m; L2-09 20 m + 25 m = 45 m; L3-06 17,5 kN − 7,0 kN = 10,5 kN. All agree with exercises.json.
- The model's conditions (a level road, locked sliding wheels, air resistance left out, N = mg) are stated in L1-09.
- Hash a3d98dd8add4fb25 at the start and at the end.
