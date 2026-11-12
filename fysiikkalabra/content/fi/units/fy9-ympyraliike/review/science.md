VERDICT: PASS
CONTENT-HASH: c2a116adf76021a5
Delta review (Johda itse round 2, 2026-11-12) of the version passed at 427c1e163f3869cd.

## Blocking
(none)

## Polish
1. `unit.md`, first Johda itse: it says *keskeiskiihtyvyys* while the theory sentence above says *normaalikiihtyvyys*; one word would keep the term consistent (teacher's call, not an error).

## Checked
1. `unit.md`: the first Johda itse ($\Sigma F = ma_\text{n} = mv^2/r$, uniform motion, $m$, $v$, $r$ defined) and the second (flat curve: $N = mg$, friction the only horizontal force, $F_\mu = mv^2/r \le \mu_0 mg$, $v_\text{max} = \sqrt{\mu_0 gr}$) are each complete; the second uses the first's result explicitly. The figure `kaarre` is unchanged and still matches the second task. "Ilmanvastus jätetään huomioimatta" adds the right condition to the free-fall statement.
2. `inquiry.json` [15] [16]: Newton's 2nd law with $a_\text{n} = v^2/r$; recomputed $27.6\,\text{km/h}$, $v = 7512\,\text{m/s}$, $T = 98.4\,\text{min}$.
3. Judged: `git diff 3ec8cc24` of this unit-language (review/ ignored); nothing else changed.
