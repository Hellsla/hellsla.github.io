VERDICT: PASS
CONTENT-HASH: 7013f5c43b745e8d
SCOPE: delta, Sovella s4 b after commit 6b08a5f2cf (task text, solution Kysytty and model answer, rubric assumptions detail, common-mistake line)

## Blocking
None.

## Polish
- Wording only: the rubric's transfer criterion says "ampeerien suuruisen virran", and the model answer gives $1{,}2\,\text{A}$ (one ampere). It still means "of the order of amperes", so this is not a contradiction.

## Checked
- `units.py hash fy9-sahkokentta` at the start and the end: 7013f5c43b745e8d. `practice.py check: OK`.
- My previous blocking item is fixed. The task now asks "enintään kuinka pitkän ilmavälin yli läpilyönti tapahtuu varmasti". The solution's Kysytty line says "pisin ilmaväli, jonka yli läpilyönti tapahtuu varmasti". The model answer says "pisin väli, jonka yli läpilyönti tapahtuu varmasti, on $d = U/E_\text{max} \approx 4\,\text{mm}$".
  - Physics: in the uniform-field model, breakdown happens when $U/d \ge E_\text{max}$, that is when $d \le U/E_\text{max}$. So 4 mm is the longest gap that certainly breaks down. This holds as an upper bound for "certain" because the field near the thin conductor and the rod tip is stronger than $U/d$. Breakdown at longer gaps is possible, and the text says so.
- Internal consistency (item 6): four texts now agree.
  - The assumptions detail: "turvaetäisyyden alaraja, ei turvallinen etäisyys … valokaari voi syttyä selvästi pidemmästäkin välistä".
  - The solution's paragraph: "alaraja turvaetäisyydelle eikä turvallinen etäisyys".
  - The common-mistake line: "4 mm esitetään turvallisena etäisyytenä, vaikka se on vain väli, jonka yli läpilyönti tapahtuu varmasti tasaisen kentän mallissa".
  - The math criterion (4 mm from 12 kV, not 20 kV).

  No phrase with "pienin" or "lyhyen" remains in any language's s4 b. I grepped fi, en and fi-easy sovella.
- Recomputed, all agreeing with the solution and answers.py:
  - $20/\sqrt3 = 11{,}55\,\text{kV} \approx 12\,\text{kV}$
  - $d = 12\,\text{kV}/(3\,\text{MV/m}) = 4{,}0\,\text{mm}$ (3,85 mm from 11,55 kV, so "about 4 mm" is right either way)
  - Voltage across the bird's feet: $0{,}30\,\Omega/\text{km} \cdot 0{,}05\,\text{m} \cdot 100\,\text{A} = 1{,}5\,\text{mV}$
  - Current: $12\,\text{kV}/10\,\text{k}\Omega = 1{,}2\,\text{A}$
- Assessment (item 7): the s4 b points still add up to 5 (1+2+1+1). Every criterion asks only for what the task gives and asks.
- Not judged again: the rest of s4, s1–s3 and s5–s8. They are unchanged since my earlier PASS.
