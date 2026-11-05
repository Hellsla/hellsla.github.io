VERDICT: PASS
CONTENT-HASH: 554d2c2e0c21f9e2

Follow-up review of the fix commit 2c31ff041 (delta from e22087d91fe1b760, whose full review is kept below). Change: inquiry.json:471, `virhe` distractor "Kerroin $\tfrac{1}{2}$ on turha" feedback now starts "Kun tyhjä kondensaattori ladataan vakiojännitelähteellä, lähde antaa energian $QU$ …".

## Blocking

None.

## Polish

1. lesson.md Esimerkki, Tulos — "noin $6{,}8\,\text{J}$ … kaksi merkitsevää numeroa": $W$ depends only on $C = 150\,\mu\text{F}$ and $U = 300\,\text{V}$, so $6{,}75\,\text{J}$ is justified; only $P$ is limited by $t = 1{,}0\,\text{ms}$.

## Checked

- New feedback: the half holds for an empty capacitor charged from an ideal constant-voltage source (dissipated $\tfrac12QU$ independent of $R$); the condition matches lesson.md:333 ("aluksi varaamaton … vakiojännitelähteestä … resistanssia", "ei yleinen laki").
- Consistency: grep of "puolet"/"$QU$" — lesson.md:333, siirto hints, mistakes and solution (:490–507, "tyhjää … paristolla … vastuksen kautta") and this feedback all state the same model.
- Misconception paragraph agrees with Ydinajatus ("kokonaisuutena sähköisesti neutraali", $Q$ = one plate's charge) and Tiivistelmä.
- Recomputed: $C = \varepsilon_0 A/d = 88{,}5\,\text{pF}$; koe-1 $44{,}3/88{,}5\,\text{nC}$, $11{,}1/44{,}3\,\mu\text{J}$; koe-2 $C \propto 1/d$; koe-3 glass $0{,}179\,\text{kV}$, $7{,}9\,\mu\text{J}$; koe-5 breakdown $3{,}0\,\text{kV}$ over 1,0 mm. All agree with lesson-answers.py and the sim's formulas.
- Example $W = 6{,}75\,\text{J}$, $P = 6{,}75\,\text{kW}$, $Q = 0{,}045\,\text{C}$, $\approx 3{,}4\,\text{s}$ at 2 W; paper $160\,\text{V}$; virhe $0{,}0338\,\text{J}$; siirto $190\,\mu\text{J}$ (mistakes 381, 0, 42,3); TV $12\,\text{J}$; exit $1{,}2\,\text{mC}$.
- Dielectric table (connected / disconnected, field pulls the slab in): correct; ennuste-2 one correct option.
- Plate formula conditions stated in Kaava and the sim's model box; photo captions correct.
- Hash same at start and end.
