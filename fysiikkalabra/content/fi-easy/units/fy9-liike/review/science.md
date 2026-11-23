VERDICT: PASS
CONTENT-HASH: 99ae4e4b048c0906
SCOPE: full review of unit fy9-liike (fi-easy): unit.md, unit.json, inquiry.json, teacher.md, Sovella s1-s8; the three new ```pysahdy boxes judged first against the Finnish unit.

## Blocking
- (none)

## Polish
- inquiry `tangentti`, feedback for the correct option: "Kun kappale kiihtyy levosta, sen nopeus on kaksi kertaa niin suuri kuin keskinopeus" holds only for *uniform* acceleration from rest. The figure is a parabola, so in context no wrong picture is left, and the Finnish text says the same ("Levosta kiihtyvällä …"). Adding "tasaisesti" in both languages would state the condition.
- s8 d (carried from the last review): $14{,}7\,\text{m}$ could be "noin $15\,\text{m}$", which fits the two-figure data.

## Checked
- **Pysähdy boxes** (Ydinajatus; Tasaisesti kiihtyvä liike; Kulmakerroin ja pinta-ala): each question and answer has the same physics as the Finnish box: slope of $(t,x)$ = velocity, area of $(t,v)$ = displacement; positive $v$ with negative $a$ means opposite directions, so the speed falls; area below the axis counts as negative and makes the displacement smaller. Each answer agrees with the paragraph above it, with the Virheet list ("Negatiivinen kiihtyvyys luetaan aina hidastumiseksi") and with lt-4 and lt-6.
- The rest of the diff: the hero SVG became a webp image with the same aria-label (it shows no quantities), and the `tarkistus-3` model answer was split into paragraphs with no word changed.
- One script recomputed every number from the task text with my own formulas: tram $450\,\text{m}$ (distractors $600$, $300$); scooter $22{,}5\,\text{m}$ ($35$, $12{,}5$, $1$); moose $46{,}77\,\text{m}$ ($30{,}77$, $77{,}54$, $16$); dog $8{,}0\,\text{s}$ ($2{,}0$, $4{,}0$, $5{,}12$); pesäpallo $-1{,}81\,\text{m/s}$ and apex at $0{,}82\,\text{s}$; lift $16{,}0\,\text{m}$ ($19{,}2$, $12{,}8$, $14{,}4$); cyclist $30\,\text{km/h}$; tangent $4{,}0\,\text{m/s}$; moped meets the car at $8\,\text{s}$.
- The same script for Sovella: s1 $12{,}0\,\text{s}$, $1{,}25\,\text{m/s}^2$, $t = 6{,}0\,\text{s}$, $d_\text{min} = 17{,}5\,\text{m}$, gap $40\,\text{m}$ at the end of the lane, d) $15{,}4\,\text{s}$, $77\,\text{m}$, $307\,\text{m}$. s2 $8{,}84\,\text{m}$, $0{,}625\,\text{s}$, $7{,}08\,\text{m}$, Moon $8{,}68\,\text{m}$, $+5{,}87$ and $-6{,}13\,\text{m/s}$. s3: my least-squares fit of the points from $12\,\text{s}$ on gives $-0{,}642\,\text{m/s}^2$, braking start $9{,}8\,\text{s}$, stop $48{,}8\,\text{s}$ and $486\,\text{m}$; this is inside the accepted $450$–$520\,\text{m}$. s4 $81{,}8\,\text{km/h}$, $135\,\text{s}$, $0{,}6$ and $18\,\text{km/h}$. s5 $0{,}9375$ ($0{,}741$–$1{,}224$). s6 $8{,}88 \pm 0{,}10$, $\times 1{,}10 = 9{,}77\,\text{m/s}^2$; the two-point method gives $8{,}92$; the fit reproduces the table to $\pm 3\,\text{mm}$. s7 and s8 agree. All answers agree within their tolerances.
- Physics, models and conditions: constant acceleration stated where it is used, no air resistance, a circular argument (s5), perspective scale error (s6), extrapolation (s3 d). Scope is FY1/FY4 kinematics.
- Assessment: every choice item has exactly one correct option, and each distractor's feedback is right. Part points equal the sum of the criterion points (124 in total), each criterion asks only what its part asks, and the Hyväksytään myös methods are valid. Every data set is labelled an invented example.
- `practice.py check` OK; hash identical at start and end.
