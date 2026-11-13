VERDICT: FAIL
CONTENT-HASH: 7c11a520814a1acb

## Blocking
- exercises.json:315–316 (L2-08, vaihtoehto 531 Hz) — A, arviointi: palaute selittää virheen väärin. "Voimakkaiden hetkien välit kahden kappaleen välein" antaisi jaksoksi 0,50 s ja huojuntataajuudeksi 2 Hz, ei 8 Hz. Arvo 8 Hz syntyy, jos myös hiljaiset kohdat lasketaan voimakkaiksi hetkiksi (väli 0,125 s) tai jos huojuntataajuudeksi oletetaan 2Δf. Lisäksi palaute ei käsittele vaihtoehdon toista väitettä, että ääniraudan taajuus oli korkeampi. — Korjaus: "Tämä tulee, kun myös hiljaiset kohdat lasketaan voimakkaiksi hetkiksi. Voimakkaiden hetkien väli on 0,25 s, joten f_h = 4 Hz. Lisäksi vaha laskee taajuutta, ja huojunta nopeutui, joten äänirauta oli matalampi kuin 523 Hz."

## Polish
- lessons/FY5/fy5-14/figures.py (beats_task, docstring) — docstringissä lukee 440 Hz ja 444 Hz, mutta tehtävä puhuu 523 Hz:n ääniraudasta. Kuvassa ei ole taajuuksia, joten oppilas ei näe ristiriitaa.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-10 ja L2-08 (kierros 3).
- L1-10: piikit ovat kohdissa 200·k Hz, joten f₁ = 200 Hz ja f₇ = 1400 Hz. Tulos on sama kuin answers.py:ssä. Tehtävä kysyy nyt suuretta, jota inquiry-tarkistus ei kysy (siellä spektri-f1…f5 ja suhde), joten toistoa ei ole.
- L2-08 on nyt valintatehtävä. Huojuntataajuus 4 Hz (inquiryssä huojunta-fh) on vain välivaihe. Ratkaisevaa on vahaehto: vaha laskee taajuutta f_x, ja huojunta nopeutui, joten f_x < 523 Hz ja f_x = 519 Hz. Fysiikka on oikein, ja tehtävässä on vain yksi oikea vaihtoehto.
- Vaihtoehdon 527 Hz ja vaihtoehdon 523 Hz palautteet ovat oikein.
- Kuvan voimakkaat hetket ovat kohdissa 0; 0,25; …; 1,00 s, koska verhokäyrä on |cos(4πt)|. Alt-tekstissä on samat hetket.
- L1-10:n merkitsevät numerot ja toleranssi 2 % sopivat. Järkevyystarkistus (1000 Hz + 2·200 Hz) on oikein.
