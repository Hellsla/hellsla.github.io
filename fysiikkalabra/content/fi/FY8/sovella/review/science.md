VERDICT: FAIL
CONTENT-HASH: 728e3c7733d30aee

## Blocking
1. **B (assessment), fy8-s5 d, criterion 4** ("Kertoo, mihin Onkalon turvallisuus perustuu: kuparikapseli, bentoniittisavi ja syvä kallio…", 1 p of 4). The task asks only how Oklo shows whether plutonium stayed in place and to evaluate the claim; nothing in the task text gives or asks for Onkalo's barriers. A complete, correct evaluation loses a point. Either add the question to the task ("Mihin Onkalon turvallisuus perustuu?") or replace the criterion with one the task asks.
2. **B (assessment), fy8-s4 a, criterion 4** requires the mediator ("…jonka välittäjähiukkanen on $W^-$-bosoni"). The task asks only "mikä vuorovaikutus aiheuttaa sen". Make the criterion "heikko vuorovaikutus" (W⁻ as an optional addition), or ask for the mediator in the task.

## Polish
- fy8-s2 c, criterion 4: "kestävänä keraamina kapseleissa" is not in the task data; accept "polttoaine ei saa päästä pölynä ympäristöön / kapselien on kestettävä onnettomuus" in the criterion's wording.
- fy8-s3 a, conclusion criterion: "todennäköisin syy" is not asked ("Mitä kuvaajasta voi päätellä?"); the model answer rightly says "esimerkiksi". Word the criterion the same way.
- fy8-s3 d: $r \approx 36\,\text{cm}$ is an extrapolation past the measured range ($2$–$20\,\text{cm}$); say so in one clause (guardrail "Fits").
- Rounding reason missing in the answers of fy8-s1 b ($\approx 1200$ from "noin $5\,\text{keV}$"), s1 d, s2 d ($1790\,\text{W}$ from $14\,\text{a}$: three figures are generous) and s3 d.
- fy8-s1 b Järkevyys: "synnyttää satoja fotoneja, mikä selittää, miksi revontulet ovat kirkkaita" is not supported by the calculation (an upper bound for one level); soften.

## Checked
- Recomputed every number from the task text with an own script; all agree with tasks.json, solutions.md and answers.py: s1 $2{,}22$ / $1{,}97\,\text{eV}$, $296\,\text{nm}$, $1193$, $1107\,\text{nm}$, $0{,}83\,\text{eV}$; s2 $Q = 5{,}594\,\text{MeV}$, $A = 2{,}23 \cdot 10^{15}\,\text{Bq}$, $3{,}52\,\text{kg}$, $83\,\%$, $1791\,\text{W}$, $98{,}5\,\text{W}$, $0{,}566\,\text{mSv}$, Po $0{,}16$, U ratio $5{,}1 \cdot 10^{7}$ (hundreds of millions of kg holds); s3 net rates, $Rr^2$, least-squares $d = 1{,}31\,\text{cm}$, read line $k = 5{,}63 \cdot 10^{-3}$, $K = 3{,}15 \cdot 10^{4}$, $36{,}2\,\text{cm}$, $0{,}23$ and $0{,}27\,\mu\text{Sv/h}$, $\pm 9{,}9$ ($14\,\%$), $6\,\%$; s4 $0{,}782\,\text{MeV}$, $7{,}16$, $0{,}8575$, $135$ / $136\,\text{s}$, $1:5 \to 271\,\text{s}$; s5 $3{,}67\,\%$, $3{,}49\,\text{a}$, $4{,}7 \cdot 10^{17}\,\text{J}$, $5{,}8\,\text{t}$, $83\,000$.
- Points: every part's criteria sum to its points (15, 20, 17, 16, 16).
- Physics and models: transitions and lifetimes of O I, collisional quenching, photon-energy threshold; atomic masses with electrons cancelling; $A = \lambda N$, decay law, dose chain $D \to H_\text{T} \to H_\text{E}$ with stated assumptions; inverse-square with detector offset and its linearisation, counting statistics; neutron decay, quark change, helium mass fraction model with assumptions named; Oklo enrichment back-calculation, moderator feedback, Pu-239 → U-235.
- Source data plausible (NIST, AME2020, MMRTG, PDG, STUK $5{,}9\,\text{mSv}$, OL3 $4300\,\text{MW}$, Oklo 15 GW·a); s3 data declared as generated, not measured.
- Scope: inside FY8 central contents; no de Broglie, no later-course physics.
- Figures: levels to scale; both s3 graphs drawn from the task data, origin line and read points agree with the solution.
- Hyväksytään myös covers alternative methods; their numbers ($559$ / $629\,\text{nm}$, $0{,}56\,\text{mSv}$, $0{,}038$) recomputed.
