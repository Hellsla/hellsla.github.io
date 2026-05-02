# Simulaatioiden ulkoasuaudit (FY03)

Tavoite: yhtenäinen visuaalinen ilme kaikille FY03-simulaatioille.

## Yhteenveto

Suurin osa simulaatioista käyttää jo samaa väripalettia, typografiaa ja "pill"-tyylisiä nappeja. Selkein poikkeama on `FY03_kiintea_laajeneminen.html`, jossa rakenne ja ohjainten asettelu poikkeavat muista merkittävästi.

## Havaitut erot

### 1) Layout-rakenne
- Useimmat käyttävät `main.slide` + 16:9-kehystä (`FY03_isobaarinen.html`, `FY03_isokoorinen.html`, `FY03_isoterminen.html`, `FY03_ideaalikaasulaki.html`, `FY03_Avogadro.html`).
- Osa käyttää koko viewportin rakennetta ilman `slide`-kehystä (`FY03_kiintea_laajeneminen.html`, `FY03_kaasu_laajeneminen.html`, `FY03_neste_laajeneminen.html`, `FY03_faasikaavio.html`).

**Ehdotus:** standardoi kaikki 16:9 `slide`-kehykseen, jotta mittasuhteet ja komponenttien sijainti pysyvät samoina projektorin, läppärin ja puhelimen välillä.

### 2) Kontrollipaneelin sijoittelu
- Osa käyttää absoluuttisesti alareunaan ankkuroitua `.controls`-palkkia.
- Osa käyttää `flex`-pohjaista, dokumenttivirtauksen mukana tulevaa kontrollialuetta.

**Ehdotus:** valitse yksi malli (suositus: absoluuttinen alareunan paneeli `left/right + bottom`, koska se on jo monessa tiedostossa) ja ota sama spacing (`gap`, `padding`, `font-size`) kaikkialle.

### 3) Sliderin leveys ja responsiivisuus
- Sliderin leveydet vaihtelevat (esim. `width: 100%`, `min(390px,54vw)`, `58vw`).

**Ehdotus:** yksi yhteinen sääntö:
- desktop: `width: min(420px, 48vw)`
- mobiili: `width: 100%` kontrollikortin sisällä

### 4) Typografia ja painot
- Fonttiperhe on pääosin yhtenäinen.
- Fonttikoot ja -painot vaihtelevat hieman (`font-weight: 520`, `620`, `clamp(...)` eri arvoilla).

**Ehdotus:** määritä tokenit:
- `--font-ui: clamp(15px, 2vw, 21px)`
- `--font-small: clamp(13px, 1.5vw, 17px)`
- `--weight-regular: 500`, `--weight-strong: 620`

### 5) Väri- ja viivatyylit
- Väripaletti on pääosin yhtenäinen (`#3F3D39`, `#2E86A6`, `#D84A62`, `#F28C28`, `#FFD95A`).
- Joissain tiedostoissa viivapaksuudet ja opasiteetit poikkeavat tuntuvasti.

**Ehdotus:** määritä yhteiset tokenit (`--stroke-main`, `--stroke-thin`, `--opacity-muted`) ja käytä niitä jokaisessa simulaatiossa.

## Priorisoitu muutoslista

1. **Korkea prioriteetti:** konvertoi `FY03_kiintea_laajeneminen.html` samaan `slide` + absoluuttinen `.controls` -rakenteeseen.
2. **Korkea prioriteetti:** yhtenäistä `FY03_kaasu_laajeneminen.html` ja `FY03_neste_laajeneminen.html` kontrollipaneelin leveys- ja spacing-säännöt.
3. **Keskitaso:** lisää kaikkiin tiedostoihin sama CSS-muuttujapaketti (typografia, spacing, viivapaksuudet).
4. **Keskitaso:** vakioi mobiilimediaquery breakpointiin `max-width: 760px`.

## Ehdotettu toteutustapa

- Luo yhteinen tiedosto `simulaatio-theme.css`.
- Siirrä siihen:
  - värit
  - fonttitokenit
  - `slide`-container
  - controls-, button- ja range-tyylit
- Jätä tiedostokohtaisesti vain simulaation omat SVG- ja animaatiotyylit.

Tällä tavalla ylläpito helpottuu ja ulkoasu pysyy aidosti yhtenäisenä uusissa simulaatioissa.
