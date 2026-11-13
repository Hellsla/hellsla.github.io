VERDICT: PASS
CONTENT-HASH: fbb3881a3468f340
SCOPE: delta added-exercise from 5cd3571020c4ddc7 base 81db4a6fd727

## Blocking

## Polish
- lessons/FY5/fy5-14/figures.py (beats_task, docstring) — docstringissä lukee 440 Hz ja 444 Hz, mutta tehtävä puhuu 523 Hz:n ääniraudasta. Kuvassa ei ole taajuuksia, joten oppilas ei näe ristiriitaa.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 4: arvioin tehtävät L1-10 ja L2-08.
- L2-08:n 531 Hz -vaihtoehdon palaute on korjattu. Arvo 8 Hz tulee nyt oikein siitä, että hiljaiset kohdat lasketaan voimakkaiksi (väli 0,125 s). Palaute selittää myös, miksi korkeampi taajuus ei sovi vahakokeeseen: erotus olisi pienentynyt ja huojunta hidastunut.
- L2-08: f_h = 1/0,25 s = 4 Hz. Vaha laskee taajuutta ja huojunta nopeutuu, joten f_x = 523 − 4 = 519 Hz. Tehtävässä on vain yksi oikea vaihtoehto, ja jokaisen väärän vaihtoehdon palaute on oikein.
- L1-10: f₁ = 200 Hz, joten f₇ = 1400 Hz. Inquiry ei kysy tätä suuretta, joten toistoa ei ole.
- Kuvien lukemat ja alt-tekstit vastaavat figures.py:n dataa (piikit 200·k Hz, verhokäyrä |cos(4πt)|).
