# Kuuntele ja katso + Kirjavinkit: korjaukset ja kuvitus (4c, 2026-11-18)

**Tavutus.** `media-other`-laatikolla oli `lang="en"` (lähteen `other_lang.lang`) suomenkielisellä sivulla, joten selain tavutti suomen
englannin säännöillä. Laatikolla ei ole nyt omaa `lang`-attribuuttia (se perii sivun kielen); vain linkillä on `hreflang`. Sama kaikissa
kolmessa kielessä (fi, en, fi-easy). Muut `lang`-attribuutit tarkistettu: ohjelmien otsikkolinkit `lang` = ohjelman kieli (oikein), kielivalikon
"English" `lang="en"` (oikein). Kirjavinkit: ei vääriä `lang`-attribuutteja.

**Kielimuutokset** (`content/fi/podcastit.json`): johdanto "Tähän on koottu … linkki toimii" → "Tälle sivulle on koottu … joiden linkit toimivat";
fuusio-kuvaus "Tutustu siihen, miksi" → "Ohjelmassa selvitetään, miksi"; DART-kuvaus "sen rata muuttui" → "kuun rata muuttui" (viittaus selväksi).
Vinkkilaatikon teksti ja ohjelmien alkuperäisnimet (myös "ei oo") ennallaan. Muut tekstit luettu: ei muita virheitä.

**Kuvat** (uusia, odottavat opettajan hyväksyntää; ei merkitty hyväksytyiksi): inline-SVG `scripts/page_art.py` (FY1–FY8, `listen`, `read`),
48×48, ei tekstiä, `aria-hidden`. Moduulikuvat 48–56 px otsikon vieressä, yläkuva 64–88 px otsikon vieressä (podcastit ja lukuvinkit).
CSS `templates/site.css` (`.page-head`, `.page-art`, `.media-mod-h`).

**Tarkistukset:** test_media.py ja test_home.py läpi; oma Playwright fi/en/fi-easy × 360/390/768/1280, kumpikin sivu: ei sivuttaisvieritystä.
Kaappaukset: `podcastit-fi-390.png`, `podcastit-fi-1280.png`, `lukuvinkit-fi-390.png`, `lukuvinkit-fi-1280.png`.
