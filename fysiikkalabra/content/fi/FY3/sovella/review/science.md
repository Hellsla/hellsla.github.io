VERDICT: PASS
CONTENT-HASH: 2bcc336fe1b09523

## Blocking
None.

## Polish
- s3 c: the Kaava writes the tank states as p_1 and p_2, but in s3 a and b, p_1 and p_2 mean the pressure at depth and at the surface. A subscript such as p_alku and p_loppu, or "absolute tank pressure" named in Annettu, would avoid the clash. The Periaate already says that the total-pressure difference equals the gauge difference, so the physics is clear.
- s3 c: the litre is \textsf{l} in V_s, V and the task text, but the consumption is still `20\,\text{l/min}` in Annettu, Sijoitus and Vastaus. s3 d (`20\,\text{l/min}`) does the same.
- From round 1, still open: s1 c keeps 800 W/m² as a number inside the symbolic chain. The s3 c substitution uses V and then t, not the single final form t = Δp_s V_s/(p q).

## Checked
- The round-1 Blocking item is fixed. The s3 c Kaava now starts from the tank's two states, p_1 V_s = n_1 RT and p_2 V_s = n_2 RT, and defines Δp_s = p_1 − p_2 and Δn = n_1 − n_2. From these it gets Δp_s V_s = Δn RT. With pV = Δn RT at depth (same T, as the task states), this gives V = Δp_s V_s/p and t = V/q.
  - Each step is correct, and the condition (same amount Δn, same T) is now visible.
  - The step agrees with the rubric criterion "kokonaispaineet tai perustelu" and with the Periaate (the air pressure cancels).
- My own script recomputed from the task data, using absolute tank pressures (200 bar + p_0, 50 bar + p_0) and Δn explicitly:
  - p = 248,15 kPa
  - V = 725,4 l
  - t = 36,27 min (answer 36 min, tolerance 5 %)
  - 89,1 min at the surface
  - 14,74 l and 10,32 cm³ for b and a

  All agree with answers.py and the solutions.
- The other changed Kaava steps (s1 b–d, s2 a, c, d, s3 a) are unchanged in physics since round 1 and still correct.
- Changing the litre to \textsf{l} changes no number or unit.
- Scope stays in FY3, and the significant-figure reasons are unchanged.
- The content hash is the same at the start and at the end (2bcc336fe1b09523).
