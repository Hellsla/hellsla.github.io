VERDICT: FAIL
CONTENT-HASH: 71b64b31921198eb

## Blocking
- exercises.json:136 (L1-11) — A: `"unit": "min"` on jäänne tehtävän vanhasta versiosta, joka kysyi kiertoaikaa. Tehtävä kysyy nyt putoamiskiihtyvyyttä ja vastaus on 1,45 m/s², joten sivu näyttäisi vastauksen "1,45 min". — Korjaa `"unit": "m/s²"`.

## Polish
- exercises.json (L1-11, hint) — "Arvot ovat" on monikossa, vaikka taulukosta haetaan nyt vain Kuun massa. — Kirjoita "Kuun massa on MAFY-taulukossa kohdassa *Aurinkokunta*."
- solutions.md (L1-10, Järkevyys) — "noin tuhannesosa" on karkea arvio: 5,93·10⁻³/9,81 ≈ 6·10⁻⁴. — Kirjoita "alle tuhannesosa".

## Checked
- Hash oli sama alussa ja lopussa. Kierros 5: arvioin muutetun tehtävän L1-11.
- L1-11: Kuun massa 7,346·10²² kg on mafy-arvot.tsv:n VERIFIED-riviltä. g = γM/r² = 1,448 m/s² → 1,45, kuten answers.py:ssä ja suomenkielisessä versiossa.
- Selkokielinen tehtäväteksti kertoo saman fysiikan: putoamiskiihtyvyys luotaimen radalla eli kiihtyvyys, jolla Kuun gravitaatio vetää luotainta.
- Toleranssi on 4 %. Pyöristysperusteena käytetään sädettä 1840 km, ja järkevyystarkistus 1,62·0,891 = 1,44 m/s² on oikein.
- Kaikkien tehtävien answer, unit ja tolerance ovat samat kuin suomenkielisessä versiossa. L1-10:n, L1-11:n ja L2-08:n ratkaisujen luvut ovat samat.
