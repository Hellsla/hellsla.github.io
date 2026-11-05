VERDICT: PASS
CONTENT-HASH: 2410c9996b853823

## Blocking
- (none)

## Polish
- solutions.md:196 fy7-4-L3-05 b) (B) — new sentence "Sivusuunnassa järjestely ei ole vakaa: sivuun siirtynyt johdin voisi kääntyä tai kaatua" names no mechanism and clashes with the task, where the wire "voi liikkua vain pystysuunnassa". Write: "Ilman sivuttaista ohjausta tasapaino olisi sivusuunnassa epävakaa: sivulle siirtyneeseen johtimeen kohdistuvalla hylkimisvoimalla on vaakakomponentti, joka työntää sitä kauemmas. Siksi tehtävässä johdin liikkuu vain pystysuunnassa."
- docs/exercise-bank/FY7.md:27 (carried over from round 1) — Taso 3 still names the terminal-velocity/energy rail task and the commutator + torque task; record that L3-04 (rail with friction, a(I) data) and L3-05 (levitating wire) were made instead.
- exercises.json fy7-4-L2-05 says "keksitty esimerkkiaineisto", the other data tasks "esimerkkiaineisto"; use one wording throughout.

## Checked
- Round 2. Round 1 had no Blocking items; the round-1 Polish items are fixed: L3-04 Periaate now "liikkuvan tangon kiihtyvyys on positiivinen vain, kun IlB > μmg"; L2-07 Järkevyys uses the lesson example's radius 1,3 cm (brief: r = 1,3 cm, N = 60): 5,27 m / (2π · 0,013 m) = 64,5 ≈ 65 turns, correct.
- Recomputed all 19 numeric answers in one script with my own formulas; all equal answers.py and exercises.json within tolerance (L3-03 with F_vert = IlB cos 74° → 1,81 kA; L2-07 LSQ through origin 5,795 N/A → 5,27 m; L3-04 slope 0,935, intercept −1,96 → B = 0,351 T, μ = 0,200).
- L3-05 Sijoitus rewritten in steps: μ₀l = 6,283 · 10⁻⁷ Vs/A, 2πrmg = 1,849 · 10⁻³ N·m, ratio 2943 A², I = 54,25 A; units consistent; renders cleanly at 1280 px (shot L3-1280-8).
- L1-06: correct option moved to third place, wording unchanged in physics; exactly one correct option, distractor feedback right.
- L1-08 Periaate wording "verrannollinen kulman siniin eikä itse kulmaan" correct.
- L2-05, L2-07, L3-04 captions shortened; data unchanged.
- Levels 8/7/5; scope FY7 + FY4 dynamics; notation matches the brief.
- Hash identical at start and end.
