VERDICT: FAIL
CONTENT-HASH: 42433b757b13505f
## Blocking
- content/en/FY4/fy4-8/exercises/solutions.md:65, 87, 145, 198 — the new Formula labels call $E_{\text{k}0} + W = E_\text{k}$ (and $W = \Delta E_\text{k}$) the "Work–energy principle", but the chapter calls that law the **work principle** (lesson "work principle :: $E_{\text{k}0} + W = E_\text{k}$") and keeps "work–energy principle" for $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$; the same name now stands for two different equations — label these "Work principle:" (the Finnish has Työperiaate).
- content/en/FY4/fy4-8/exercises/solutions.md:77, 99, 111, 183, 212, 273 — the new label "Energy principle:" names $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$ differently from the lesson ("work–energy principle of mechanics") and from these tasks' own Principle lines (e.g. 74, 96, 108: "so we use the work–energy principle") — label them "Work–energy principle:" (Finnish Energiaperiaate).

## Polish
- content/en/FY4/fy4-8/exercises/solutions.md:290 — older text, same mix-up: "the work–energy principle $E_{\text{k}0} + W = E_\text{k}$" — "the work principle" (fix together with the labels above).

## Checked
- Captures opened: none (text and formula changes only; judged from the files and the packet).
- Physics of every rewritten Formula step is right: conservation tasks start from $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$ with the zero level named, the mass cancels, $v = \sqrt{2gh}$, $h = v^2/(2g)$, $v_2 = \sqrt{v_1^2 + 2gh}$, $h = (E_{\text{k}0} - E_\text{k})/(mg)$.
- Friction and resistance: $W = -F_\mu s$ or $-F_\text{res}s$ against the motion; $s = mv_1^2/(2F_\mu)$, $F_\text{res} = [\tfrac{m}{2}(v_1^2 - v_2^2) + mgh]/s$, $h_2 = h_1 + v_1^2/(2g) - F_\text{res}s/(mg)$, snowboarder $F = mgh/(L + s_\text{mean})$ and $v = \sqrt{2(mgh - FL)/m}$: correct.
- Lift at constant speed $W = mgh$; stick $v_2 = \sqrt{2Fs/m}$; data lines $g = k/2$ and $F_\mu = m/(2k)$; bounce shares $r_n = h_{n+1}/h_n$.
- Substitutions, answers and significant figures unchanged; paragraph splits change no claim.
- answers.py run: every numeric answer agrees with exercises.json within rounding; answers, units and tolerances identical to content/fi; git diff origin/main touches no task text, answer, unit, tolerance, id or answers.py.
