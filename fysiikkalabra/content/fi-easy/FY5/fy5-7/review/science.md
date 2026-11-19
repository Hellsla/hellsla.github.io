VERDICT: PASS
CONTENT-HASH: faab333e7dcf81ff

## Blocking

## Polish
- lesson.md:149 — "Tämän luvun laskutehtävissä ajanotto alkaa aina näin" is now true: every calculation that uses the sine model starts at an upward pass (Esimerkki, siirto, tarkistus-2, tarkistus-3 with $C \approx 0$, and the exercises L1-09, L2-01, L3-01, L3-02, L3-05; the figures for L2-01 and tarkistus-2 start at $x = 0$ going up). The optional "vaihe" task is a choice task, so it no longer contradicts the sentence. Optional: "laskutehtävissä, joissa käytetään sinimallia" would also cover the many tasks where only $f = 1/T$ is used and timing does not matter.

## Checked
- Round-1 Blocking item resolved: the claim is limited to calculation tasks, and the vaihe task ($C = \tfrac{\pi}{2}$, release at the extreme) is consistent with the glossary and the GA Pro paragraph.
- Recomputed in one script: Esimerkki arg $2{,}618$, $x = 2{,}0\,\text{cm}$ (degree mode $0{,}183\,\text{cm}$); siirto $3{,}804\,\text{cm}$, degree mode $0{,}0877$, f used as T $-3{,}80$; tarkistus-2 $0{,}556\,\text{Hz}$ (mistakes $1{,}11$, $0{,}185$; $L \approx 0{,}81\,\text{m}$ plausible); tarkistus-3 $T = 0{,}800\,\text{s}$, $f = 1{,}25\,\text{Hz}$, range $0{,}378$–$0{,}482\,\text{m}$; Etsi virhe $1{,}11$ / $2{,}22\,\text{Hz}$; kertaus, exit ticket $2{,}0\,\text{Hz}$.
- Sim data regenerated (Park–Miller, same seeds as sim.js): koe-1 $d = 1{,}85 / 0{,}13 / 3{,}70\,\text{cm}$ for $A = 3, 6, 12\,\text{cm}$; koe-2 $N = 6, 3$, $f = 1{,}25$, $0{,}625\,\text{Hz}$; koe-3 grid best $A = 8{,}5\,\text{cm}$, $T = 2{,}20\,\text{s}$, $d = 0{,}13\,\text{cm}$; max error $0{,}2499\,\text{cm}$ ≤ stated $0{,}25$; load state $d = 3{,}92$ matches the 1280 px capture.
- Experiments isolate their parameter (aineisto and T locked in koe-1, aineisto and A in koe-2); simState exposes d, N, f, A.
- sim.js implements $x = A\sin(2\pi t/T)$, $d$ as mean absolute deviation, $N = \lfloor 5/T \rfloor$, as the calc box says; model box states no damping, upward positive, simulated values.
- Predictions: exactly one correct option each; distractor feedback correct (amplitude vs $2A$, $T$ vs $f$, half period).
- Figures: fig 3 marks $T$ peak-to-peak and between upward crossings (0,8 s), $A$ from $x = 0$; fig 4 circle point at about 150° matches the graph point (about $0{,}42T$, $0{,}5A$); fig 5 $3T = 3{,}6\,\text{s}$, $A \approx 3\,\text{cm}$; fig 12 three periods in 5,4 s.
- Sinusoidal shape conditioned (spring, small-swing pendulum, reason deferred to later chapters); radian mode stated; within FY5 central contents.
- Hash identical at start and end.
