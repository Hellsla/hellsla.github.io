VERDICT: PASS
CONTENT-HASH: 6a20ede240385bd9

## Blocking
(none)

## Polish
- [Minor] inquiry.json koe-2 intro — "latauksen kesto $0$" ilman yksikköä, kun kortin Alkutila-laatikossa lukee $0\,\text{h}$; kirjoita "Pidä vakioina varaustaso alussa ($80\,\%$), latauksen kesto $0\,\text{h}$ ja resistanssi; muuta vain laturin jännitettä."
- [Minor] inquiry.json virhe, vaihtoehto 3 — "noin $15\,\%$": $14/0{,}35 = 40\,\text{A}$ vs. $35\,\text{A}$ on noin $14\,\%$; kirjoita "noin $14\,\%$".
- [Minor] Aiemmat Minor-kohdat (sim-1280:n liukusäätimen otsikon rivitys, "= 0 h" -alkutilan teksti ilman matematiikkaa, inline-yhtälön rivinvaihto) ovat ennallaan; koe-2:n Alkutila-laatikossa "= 0,4 Ω" on yhä tavallista tekstiä (mallipohjan asia).

## Checked
- Hash alussa ja lopussa.
- stage-herata-390: hook "noin puoleen" eheä.
- exp-koe-2-390-1 ja lab-1280-1: uusi koe-2-intro renderöityy, sim ja Alkutila-laatikko ehjät, kuvaaja ja virran suunta luettavissa.
- stage-sovella-390-2 (Etsi virhe, kolme vaihtoehtoa) ja -3 (siirto-tehtävä): asettelu ehjä; ratkaisun muutos ("lähes kolmannes") ei vaikuta asetteluun.
- Mallikuvaus (sim "Mallin oletukset") luettu lähteestä: yksiköt LaTeXissa, sijamuodot ($3{,}40\,\text{V}$:n) oikein.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
