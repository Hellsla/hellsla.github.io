VERDICT: PASS
CONTENT-HASH: 6a20ede240385bd9

## Blocking
(none)

## Polish
- inquiry.json virhe, vaihtoehto 3 — "tulosta noin $15\,\%$" : jättämällä $0{,}050\,\Omega$ pois opiskelijan virta kasvaisi $14/0{,}35 = 40$ A vs. $35$ A eli noin $14\,\%$; kirjoita "noin $14\,\%$".
- inquiry.json koe-2 intro — "Varaustaso alussa ($80\,\%$), latauksen kesto $0$ ja resistanssi pysyvät vakioina" on nyt kieliopillinen mutta kuiva; selkeämpi: "Pidä vakioina varaustaso alussa ($80\,\%$), latauksen kesto $0\,\text{h}$ ja resistanssi; muuta vain laturin jännitettä."
- Aiemmat Polish-kohdat (hookin kysymys paljastaa virran pienenemisen, koe-1:n kokonaisresistanssin laskuvihje, pienet akselin numerot 390 px:ssä) ovat ennallaan.

## Checked
- Hook: "noin puoleen" vastaa mallia (0,5 h antaa noin 44 %); aiempi ristiriita korjattu.
- Sim-malli: lisäys "kunnes lähdejännite on laskenut laturin jännitteeseen; vasta alle 3,40 V laturi tyhjentää" on fysikaalisesti oikein ja sopii kokeeseen 2 (80 %, E ≈ 4,04 V).
- Koe 2: tarkistuspiste 4,04 V ja ehdotetut jännitteet (3,6 / 4,0 / 4,2 / 4,6 V) kumoavat ennusteen.
- Siirto: Järkevyys "lähes kolmannes" (30 %) oikein; 1,68 ja 2,5 tarkistettu.
- Etsi virhe: oikea vastaus 4,0 A, sarjakytkentä-vaihtoehto ja sisäisen resistanssin vaihtoehto palautteineen korjaavat virhekäsityksen.
