VERDICT: FAIL
CONTENT-HASH: 38596abe4b9293cb

## Blocking
- inquiry.json:351 (siirto solution): "**Kaava:** $s_\text{AU} = \dfrac{vt}{1\,\text{AU}}$" and dividing by "$1{,}496\cdot10^{8}\,\text{km/AU}$" is a conversion-factor formula. Teacher's rule: convert by substitution, as the lesson's Kaava section teaches. Round 1 rated this polish; the rule makes it blocking. Fix: keep $s = vt$ as the formula, then count how many AU fit, $4{,}842\cdot10^{8}\,\text{km} : 1{,}496\cdot10^{8}\,\text{km} = 3{,}236$, so $s = 3{,}236\,\text{AU}$ in a year.
- inquiry.json:338, :339, :344 (siirto hints 2–3 and the first mistake's feedback): "jakamalla luvulla … km/AU" and "$\dfrac{4{,}842\cdot10^{8}\,\text{km}}{1{,}496\cdot10^{8}\,\text{km/AU}}$" teach the same conversion factor. Fix: "montako AU:ta ($1{,}496\cdot10^{8}\,\text{km}$) matkaan mahtuu", with ":" between the two lengths.
- inquiry.json:409 (tarkistus-2 solution) and :402 (mistake 193): "$\dfrac{193{,}1\,\text{s}}{60\,\text{s/min}}$" and "jaa vielä luvulla $60\,\text{s/min}$" use a conversion factor. Fix: substitute $1\,\text{s} = \tfrac{1}{60}\,\text{min}$, i.e. $193{,}1\,\text{s} = 193{,}1\cdot\tfrac{1}{60}\,\text{min} = 3{,}219\,\text{min}$. In the feedback, say that a minute is $60\,\text{s}$, so the number of minutes is $193 : 60$.

## Polish
- lesson.md, Esimerkki Sijoitus: "$\frac{1{,}502\cdot10^{4}}{3600}\,\text{h}$" is better written as a substitution: $1\,\text{s} = \tfrac{1}{3600}\,\text{h}$, so $1{,}502\cdot10^{4}\cdot\tfrac{1}{3600}\,\text{h}$.
- inquiry.json:283, :295 (virhe feedback): "muunnoskerroin" names the factor rule. Say "neliökilometri on $(1000\,\text{m})^2 = 10^{6}\,\text{m}^2$" instead.
- sim.js (slider label vs view), still open from round 1: at the Sun the label reads $d = 10^{6{,}00}\,\text{km}$ while the readout reads $d = 0\,\text{km}$. Mark the label as the slider's lower limit.

## Checked
- One script recomputed everything: worked example ($4{,}503\cdot10^{9}\,\text{km}$, $4{,}17\,\text{h}$), 1 AU = 499 s = 8,32 min, ennuste-2/koe-1 (33,4; 334; 3340 s), Voyager table (119,7/132,6/145,6/158,5 AU; 16,6/18,4/20,2/22,0 h), 1.1.2026 (142,9 AU, 19,8 h, ratio 143), February 2026 ≈ 143,3 AU, 7,2 AU/h, 1212 AU/week, 63 000 AU/ly, siirto 3,236, Merkurius 3,22 min with mistakes 193 and 0,0536, sim scale (Sun 401 px, Earth 3,7 px, Neptune 1,29·10⁶ px). All agree.
- The Voyager model matches the brief. Its values are labelled as model values, with the Sun-versus-Earth caveat.
- Round 1 blockers fixed: sim calc uses $t = s : c$; johtopäätös, tarkistus-3 and their criteria now say "yksikön paikalle kirjoitetaan sen arvo"; pohdi says "yksikkömuunnoksiin".
- No ×, \times or ÷; multiplication is \cdot; divisions written as operations use ":" or \frac.
- simState gives n, dAU, tLight, pvm, vAU, vTh. Koe 1 locks the date and varies only n.
- Significant figures, the SI table, prefixes and scale examples are correct.
- The SVG figures' numbers are correct; the ruler figure is to scale.
