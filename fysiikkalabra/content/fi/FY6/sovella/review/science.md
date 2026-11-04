VERDICT: FAIL
CONTENT-HASH: 6f3465d0e19501e5

## Blocking
1. **fy6-s1 d, rubric `error_sources` and Periaate (A, causality).** The rubric says discharging *and heating* make the later voltages too low. Heating lowers $R_\text{s}$, which raises $U$ under load, so it works the other way. The reported downward drift comes from discharging. Blame the too-large $R_\text{s}$ on discharging, and say that heating also changes $R_\text{s}$ during the series.
2. **fy6-s4 task text (B).** A small battery charges the capacitor to 300 V. In fy6-13 a capacitor charges only up to the source voltage. Add "jännitettä nostavan piirin avulla".
3. **fy6-s2 d, criterion `assumptions` (A, rule 7).** The question does not ask for assumptions, and the task text already gives the constant-resistance assumption. Replace it with something the question asks, such as the lamp voltage of 8.6 V or the cable power of 15 W.
4. **fy6-s2 b Vastaus (A, rounding reason).** It says "Kolme merkitsevää numeroa vastaa lähtötietojen tarkkuutta", but 0,80 Ω, 24 W and 12 V have two significant figures. Part a and the rubric use 17 W. Give about 17 W with the two-figure reason.

## Polish
- s1 b: it says "ei mittauspisteistä", but (0,10 A; 4,48 V) is a measured point.
- s4 a and b give inconsistent significant-figure reasons (300 V counted as three figures, 220 V as two).
- s3 c: the `assumptions` criterion repeats criterion 1, and "miksi malli silti sopi" is not asked.
- s2 c: criterion 3 also expects the cable power, which the question does not ask for.
- s4 d: the 10 kΩ discharge resistor takes 9 W at first. Mention that it needs a suitable power rating.
- s2 d (C): at 1,36 times its rating a real fuse may blow slowly. The wording is acceptable.

## Checked
- I recomputed every number independently: the s1 fit (slope −1,194, intercept 4,598, largest residual 0,020 V), s1 c and d, s2 a–d, s3 a–d and s4 a–d. All agree with the solutions and answers.py.
- The s3 magnitudes are plausible. The droplet radius is about 46 µm and its charge is 15 % of the Rayleigh limit. Drag at 5 m/s is about 2·10⁻⁷ N, roughly equal to qE, so the terminal-speed explanation in c holds.
- The points add up (15/15/16/14).
- Scope stays within FY6: the capacitor is treated qualitatively, with no exponential function and no capacitor connections.
- The data are labelled as made up, the s1 figure is correct, and the hash is unchanged.
