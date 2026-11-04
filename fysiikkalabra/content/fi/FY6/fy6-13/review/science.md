VERDICT: PASS
CONTENT-HASH: e22087d91fe1b760

Full review (scope: a changed line carries a symbol). Changes of this round: the half-energy paragraph now limits the result to charging an initially uncharged capacitor from a constant-voltage source through resistance and says it is that model's result, not a law for every charging method; the misconception now states the misconception (net charge) and corrects it with $+Q$/$-Q$, total charge zero and energy in the field between the plates.

## Blocking

None.

## Polish

1. lesson.md Esimerkki, Tulos — "noin $6{,}8\,\text{J}$ … kaksi merkitsevää numeroa": $W$ depends only on $C = 150\,\mu\text{F}$ and $U = 300\,\text{V}$, so $6{,}75\,\text{J}$ (three figures) is justified; only $P$ is limited to two figures by $t = 1{,}0\,\text{ms}$. Say which datum limits which result.

## Checked

- New half-energy text: true for a capacitor charged from zero by an ideal constant-voltage source through any series resistance (source gives $QU$, stored $\tfrac12QU$, dissipated $\tfrac12QU$ independent of $R$); the condition now stated agrees with `siirto` ("tyhjää … vastuksen kautta … paristolla", "vastuksen suuruutta ei tarvittu") and the `virhe` distractor feedback.
- Misconception paragraph now agrees with Ydinajatus ("kokonaisuutena sähköisesti neutraali", $Q$ = one plate's charge) and Tiivistelmä.
- Recomputed: $C = \varepsilon_0 A/d = 88{,}5\,\text{pF}$ (200 cm², 2,0 mm); koe-1 $44{,}3/88{,}5\,\text{nC}$, $11{,}1/44{,}3\,\mu\text{J}$, $Q:U = 88{,}5\,\text{nC/kV}$; koe-2 $C \propto 1/d$; koe-3 glass $U = 0{,}179\,\text{kV}$, $W = 7{,}9\,\mu\text{J}$; koe-5 air breakdown at $3{,}0\,\text{kV}$ over 1,0 mm. All agree with lesson-answers.py and the sim's formulas.
- Example $W = 6{,}75\,\text{J}$, $P = 6{,}75\,\text{kW}$, $Q = 0{,}045\,\text{C}$, $\approx 3{,}4\,\text{s}$ at 2 W; paper $0{,}010\,\text{mm}$: $160\,\text{V}$; virhe $0{,}0338\,\text{J}$; siirto $190\,\mu\text{J}$ (mistakes 381, 0, 42,3); TV $12\,\text{J}$; exit $1{,}2\,\text{mC}$.
- Dielectric table (connected: $U$ same, $Q$, $W$ up; disconnected: $Q$ same, $U$, $W$ down, field does work pulling the slab in): correct; ennuste-2 one correct option, distractor feedback right.
- Plate formula conditions (small $d$, edge effects ignored, dielectric fills the gap) stated in Kaava and the sim's model box.
- Charging/discharging qualitative description and tarkistus-2: correct.
- Photo captions (MKP film capacitor, 275 VAC rating; capacitor bank hazard): correct.
- Hash same at start and end.
