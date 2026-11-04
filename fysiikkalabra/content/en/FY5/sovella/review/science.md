VERDICT: PASS
CONTENT-HASH: 2c7cc76823c0c1d0

## Blocking
(none left)

## Fixed
- fy5-s4 d (tasks.json criteria, solutions.md ×4): the Finnish subscript $t_\text{sall}$ is now $t_\text{perm}$, as in the English fy5-16.
- fy5-s3 c (tasks.json, solutions.md): "larger than the mass of the weight" is now "larger than the hanging mass alone". "Weight" is a force, so the old wording was ambiguous. The fy5-s3-graph alt text was changed the same way (figures.json and the solutions SVG).

## Polish
- fy5-s1: $m_\text{p}, r_\text{p}, m_\text{v}, r_\text{v}$ keep the Finnish initials (puomi, vastapaino). They match the crane figure, whose labels figures.py draws in every language, and they are defined under **Given**. An English subscript (j/cw) would need a per-language label in lessons/FY5/sovella/figures.py.
- fy5-s4 c: same as fi. The solution claims one significant figure but stores 5.2.

## Checked
- Compared every string of tasks.json (intro, source notes, texts, 18 parts, 64 criteria, details), all of solutions.md (31 sections) and figures.json with content/fi/FY5/sovella.
- Answers, units, tolerances, criteria keys, points and links are identical (practice.py check: 64 points). All formulas are identical once \text words are set aside (check_i18n: en 0 errors). The decimal point is used throughout.
- Physics terms: moment, lever arm, line of action, centre of mass, counter-jib, tension, centripetal acceleration (normaalikiihtyvyys), centrifugal force, orbital speed, rotation period, spring constant, intercept, elastic potential energy, antinode/node, fundamental, sound intensity level, upper action value, A-weighted. Moon names are in English form (Ganymede, Callisto).
- Physics content is unchanged: crane 21 m, 2.6 t, 412/608 kNm, 1.9 t, 3.1 t, 0.60°, 0.16 m. Jupiter: 1.27·10¹⁷, 1.9·10²⁷ kg, 1.6·10⁸ m. Spring: 19.9 N/m, 14 g, 20.0 and 18.9 N/m, 0.45 m/s. Organ: 250 Hz, 0.686 m, 5.2 Hz, 94 dB, 1 h. These agree with the answers.py output.
- The ground-frame "no centrifugal force" and the ideal-model assumptions (point source, reflections, circular orbit, m ≪ M) are carried over intact.
- practice.py figures FY5 --lang en: up to date. Hash: f330caf239bff423 at the start, 2c7cc76823c0c1d0 at the end, after my fixes.
