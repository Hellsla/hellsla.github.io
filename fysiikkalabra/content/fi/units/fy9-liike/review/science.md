VERDICT: FAIL
CONTENT-HASH: a160a51a52b7e3ef
Review of the recognition chart (queue 9c) and the term change against the version passed at 62a144b4944a81b5; full on the chart, delta on the rest.

## Blocking
- B (row 4 and ARIA_KARTTA): "ei kiihtyvyyttä tiedossa → keskinopeus, Δx = (v_0 + v)/2 · t". The mean of the initial and final velocities is the average velocity only in uniformly accelerated motion; the unit's Kaava and its johda block say so ("Tasaisesti kiihtyvässä liikkeessä keskinopeus on siis alku- ja loppunopeuden keskiarvo"). The sign states the opposite of a condition (the acceleration is unknown), which invites the formula for any motion with given end speeds. Fix: e.g. "kiihtyvyys vakio, mutta a ei tiedossa" in the chart and "Kiihtyvyys on vakio, mutta sitä ei tiedetä" in the aria-label.

## Polish
- C: "nopeus paikkakuvaajasta → v = Δx/Δt": for a curved (t, x) graph the instantaneous velocity is the slope of the tangent (Kaava); "tangentin kulmakerroin" in the choice would match.
- C: "kiihtyvyys on vakio, matka? → x = x_0 + v_0t + ½at²" gives position; distance equals |x − x_0| only if the motion does not reverse.
- Note for pedagogy: the keskinopeus result is the Johda itse result of the Kaava section.

## Checked
- Rows against the Kaava section: constant velocity → x = x_0 + vt; constant acceleration → v = v_0 + at and x = x_0 + v_0t + ½at²; keskinopeus (above); slopes v = Δx/Δt and a = Δv/Δt; distance from the (t, v) graph → area (as total unsigned area this is the distance; the Kaava's signed area is the displacement; both consistent).
- Symbols agree with kaavanimet.tsv; nothing outside FY9.
- ARIA_KARTTA: same seven rows, same order and physics.
- teacher.md: only "tunnistuskaavio". unit.md: only the old map figure replaced (its polylines removed).
