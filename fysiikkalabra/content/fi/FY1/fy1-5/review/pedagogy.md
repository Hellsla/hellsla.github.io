VERDICT: PASS
CONTENT-HASH: 77065a1ef4a8e29d

## Blocking

## Polish
- lesson.md Esimerkki, last three paragraphs — "Ero 0,5 AU on tätä pienempi" appears without the difference ever being computed, and "tätä" points at the Earth-orbit paragraph, so a 17-year-old cannot follow the comparison — fix: "Malli ja JPL:n arvo eroavat $0{,}5\,\text{AU}$ ($143{,}05\,\text{AU} - 142{,}6\,\text{AU}$). Maan kierto muuttaa etäisyyttä jopa noin $1\,\text{AU}$, joten vertailu ei voi erottaa mallia tätä tarkemmasta."
- lesson.md Esimerkki stage 4 — the unit chain "… AU : (1/86 400 vrk)" uses a colon and nested fractions for a conversion that is hard to read; an easier route: $t = 2922 \cdot 86\,400\,\text{s}$, $\Delta s = vt$ in km, then convert to AU once.
- inquiry.json exit ticket — a 90 km/h to m/s style conversion that repeats the Yksiköt stop-and-think (also 90 km/h) and tests units, not the core idea; ask instead whether position or distance doubles when time doubles for a graph with $s_0 \neq 0$, or read a speed off a given line.
- inquiry.json — the position-versus-distance proportionality is hit six times (ennuste-2, koe-2, johtopäätös, virhekäsitys, Etsi virhe, tarkistus-1), while reading the slope as speed is tested only once (tarkistus-2). Etsi virhe largely repeats ennuste-2; mark it optional, and drop or merge one of the two concept checks (tarkistus-1, check-c2) so the checks are three, not four.
- inquiry.json koe-1 and koe-2 — the sim only evaluates $s = s_0 + vt$, so the table confirms the formula being predicted rather than letting something emerge; a short real data set (a cart's positions at equal times, with `source`) in one experiment would also exercise "mallin arvo vs mittaus".

## Checked
- Opening question and hook: the hook gives s0 and v, so only the constant-speed assumption is left to commit to; acceptable, answer kept for the reflect item.
- Slot goals (graphical and linear model, direct proportionality, s = vt) covered; no FY2 content (force, acceleration) enters.
- Predictions: ennuste-2 repairs the real misconception; each wrong option's feedback names the evidence; wording works when reopened after Tutki.
- Experiments lock s0 and v, vary t, min 3, quotient left to the student; the conclusion `after` both experiments with a model answer and criteria.
- Worked example arithmetic (2922 d, 0,0088602 AU/d, 144,89 AU, 142,6 AU for 15 Feb 2026) and the seven-stage form hold; model value vs measurement is stated.
- Siirto (390 m) and tarkistus-2 (s0 = 4,0 m) answers, hints and mistake values (1092, 270; 7, 3) recomputed and correct; solutions follow the seven steps.
- Etsi virhe: error and correction (33 m vs 23 m) correct; feedback repairs the misconception.
- Finnish: grammar, case after number and unit and glossary terms fine; MAFY label "keskivauhti" on $v = \Delta s/\Delta t$ sits next to text calling it nopeus, tolerable.
- Captures: 390 px sim, figures and example legible and unclipped; figures follow their paragraphs; the photo's caption ties it to the "not necessarily uniform" point.
