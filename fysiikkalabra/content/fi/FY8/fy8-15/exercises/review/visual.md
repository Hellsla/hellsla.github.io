VERDICT: PASS
CONTENT-HASH: 3154ca5d6bf1cdf0

## Blocking
(none)

## Polish
- [Minor] solutions.md fy8-15-L3-01, Kaava (open-exercises-L3-1280-1) — rivi "$q_\text{alku} = q_\text{loppu}$, $B_\text{alku} = B_\text{loppu}$ ja $Q = \ldots > 0$" rikkoutuu: ensimmäinen yhtälö jää tekstiriville ja kaksi muuta menevät omaan laatikkoonsa, jossa "$> 0$" putoaa omalle rivilleen. Fix: kirjoita kolme ehtoa kolmeksi sisäkkäiseksi riviksi (`aligned`) tai erota kolme ehtoa pilkuin kokonaan tekstiriville ja $Q$ omaan lohkoonsa.
- [Minor] solutions.md fy8-15-L3-01, Sijoitus — reaktiossa (2) lasketaan $(1672{,}45 - 1192{,}642 - 493{,}677)\,\text{MeV}$ ilman yksikköä $\tfrac{\text{MeV}}{c^2}$ ja $c^2$, reaktiossa (3) yksikköjen kanssa; tuloksena yhtenäisyys puuttuu. Fix: käytä molemmissa samaa muotoa (esimerkin tapaan yksikkö $\tfrac{\text{MeV}}{c^2} \cdot c^2$) tai vain lukuja ja yksi yksikkö lopussa. Lisäksi tulos $63{,}090\,\text{MeV}$ ja vastaus $63{,}09\,\text{MeV}$: pyöristys sanotaan, joten vain huomautus.
- [Minor] exercises.json fy8-15-L3-01 — tehtäväteksti on yksi pitkä kappale (viisi hiukkasta massoineen, kolme reaktiota, kvarkkien varaukset); puhelimella sitä on raskas lukea ja kysymys "Päättele … ja laske …" on keskellä. Fix: jaa kahteen kappaleeseen (tilanne ja reaktiot; hiukkaset ja massat) ja pidä kysymys viimeisenä virkkeenä; kvarkkien varaukset ennen kysymystä.
- [Minor] exercises.json fy8-15-L2-03 (open-exercises-L2-1280-3) — vakiolause tuli tehtäväkortissa samaan kappaleeseen kuin kysymys, ja kysymystä korostava lihavointi ulottuu myös vakioihin ("Vakiot: …"). Fix: varmista, että tyhjä rivi tuottaa oman kappaleen, tai siirrä vakiot ennen kysymystä, jotta kysymys on viimeinen.
- [Minor] solutions.md fy8-15-L3-01, Järkevyys — luku $1232\,\tfrac{\text{MeV}}{c^2}$ ($\Delta^-$) on tehtävän ulkopuolelta; lisää "kirjallisuusarvo" tai poista, koska muu lause kestää ilman sitä.

## Checked
- Deltan kaikki muutokset: L1-01 ja L1-02 (sulkeet, miinus pysyy $d$:n ja $s$:n varauksen mukana: aiempi huomautus korjattu), L2-02 Periaate (leptoniluku), L2-03 (vakiot), L2-04 ($p$ → $x$, aiempi huomautus korjattu), L3-01 kokonaan uusi (teksti, ratkaisu, vastaus).
- open-exercises-1280-1 (L1-01 teksti ja ratkaisu), open-exercises-L2-1280-3 (L2-03), open-exercises-L3-1280-1 ja -2 (L3-01 ja L3-02) täydellä koolla.
- Typografia: desimaalipilkku, ohut väli, yksiköt pystyssä, murtoluvut luettavia, $K^- = s\,\bar{u}$ ja $\Lambda^0 = u\,d\,s$ oikein; L3-02:n vastausyksikkö "$10^{14}\,\text{J}$" renderöityy nyt oikein.
- Ei tehtäväkohtaisia kuvia.

## Scores
illustrations n/a · typography 4 · Finnish 4 · accessibility 4
