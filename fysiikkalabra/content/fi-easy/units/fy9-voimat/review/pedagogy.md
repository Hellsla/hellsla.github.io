VERDICT: PASS
CONTENT-HASH: d37f9e53fcc1656e
SCOPE: delta: round 2, fi-easy; only change since round 1 is s7 "Yleisiä virheitä" last bullet, a one-row aligned block became inline $100 : 75 \cdot 48\,\text{m/s} \approx 64\,\text{m/s}$ (same numbers, units, meaning); s1-s6, s8 not re-judged.

## Blocking
- (none)

## Polish
- s7 a, units_precision and solution Vastaus: "two significant figures like the speeds read" is not accurate for $a_1$: the speeds $18{,}6$ and $40{,}4\,\text{m/s}$ have three figures. Say instead that the difference $6{,}0\,\text{m/s}$ (and the time $4\,\text{s}$) limit $a_2$ to two figures; $a_1$ is then given to two figures by the same rule.
- s7 d: the criterion rounds $k \approx 0{,}31\,\text{kg/m}$ but the substitution uses $0{,}315$; the model solution uses $0{,}3147$. Use one value (for example $0{,}31$ everywhere, or "$0{,}3147$ kept unrounded in the calculator").
- s8 b, Sijoitus and criterion: the shown chain $-1{,}14 \cdot 2{,}0 = -2{,}29$ does not multiply out ($-2{,}28$); the unrounded $a$ was used. Show $a = -1{,}143\,\text{m/s}^2$ or add "(laskimessa tarkka arvo)". Part c repeats $-2{,}29$ and calls the $0{,}02\,\text{m/s}$ a rounding difference, which is honest and fine.
- s8 d criterion: $t_1$ and $t_2$ in $s = \tfrac{1}{2}(t_1+t_2)|v|$ are defined only in the full solution; add "(puolisuunnikkaan yhdensuuntaiset sivut)" to the criterion too.
- s7 a/b answer tolerance is 3 %, but the points are read from a graph with a 5 m/s grid; the "Hyväksytään myös" row already allows $1{,}4\ldots 1{,}6\,\text{m/s}^2$, so keep the page's checker no stricter than that.
- The listed captures (shots.md) show the lesson stages only; the Sovella itsenäisesti page with s7/s8 and their open solutions is not among them, so 360 px layout of these two is left to the visual reviewer.

## Checked
- Task texts s7 and s8 (fi-easy): situation first, questions last; no "three phases" or "twice" style hints; s7 d and s8 e ask for justification by calculation or explanation; the $F_\text{v} = kv^2$ model is given as an assumption, which a YO task does.
- Numbers re-computed: $a_1 = 9{,}3$, $a_2 = 1{,}5\,\text{m/s}^2$, $F_\text{v} = 623\,\text{N}$ (85 % of $736\,\text{N}$), $v_\text{r} = 48{,}4$, second jumper $55{,}8\,\text{m/s}$ (ratio $1{,}155$); s8: $-1{,}143$, $-2{,}29$, $0{,}857\,\text{m/s}^2$, $2{,}7\,\text{s}$ stops the lift, $12{,}2\,\text{m}$ equals the piecewise sum $12{,}25\,\text{m}$. answers.py matches tasks.json.
- Results rounded to the data's precision with the reason stated (apart from the first Polish item); reasonableness checks present in every calculation part.
- Figures: hyppy-vt-points (points only, no curve) and ex-hissi are catalogued "safe"; their alt texts give the same values as the criteria and use the task's names ($t$, $v$, $N$).
- Calculation chains are aligned rows starting with the quantity; solutions open with Annettu, Kysytty, Periaate, Kaava symbolic first.
- Intro sentence now includes air resistance and counts eight tasks; matches the eight tasks of the set.
- Language neutrality: same numbers, points and criteria in fi, en and fi-easy (compared field by field); fi-easy sentences short and clear.

## Checked
- Git diff of the unit's content since round 1 shows only that formatting change in sovella/solutions.md (6 lines, same in all three languages); all other differences are review files.
- The inline formula reads correctly in the bullet and the point (v proportional to sqrt(m), not m) is unchanged.
- No new issue; round 1 Polish items above remain recorded and unchanged.
