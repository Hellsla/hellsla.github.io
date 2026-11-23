# FY10-kuvasääntöraportti (2026-11-23, vain havainnot, ei muutoksia)

Työjono 4, opettajan rajaus 2026-11-23. Tarkistettu FY10-tutkimusten kuvat (assets/pics/fy10/, #797) neljää kriteeriä vasten. **Kuviin ei ole kosketettu**; opettaja päättää, mitä korjataan.

## Menetelmä ja rajaukset
- Kuvat ovat `investigation.md`:n SVG-kuvia: rasterikuva (webp) tai kaavio, jonka päällä nimiöt ovat `foreignObject`-elementeissä. Nimiön koko 390 px:n leveällä näytöllä = nimiön `font-size` × kuvan piirtoleveys / viewBox-leveys. Piirtoleveys mitattu Chromiumilla 390 px:n näkymässä: **343 px** (kuva pääsarakkeessa) tai **307 px** (kuva tuki-lohkossa).
- Pienenä pidetään alle 12 px:n nimiötä (nimiön koko 24 / 22 / 20 / 18 → 343 px:n kuvassa 13,7 / 12,6 / 11,4 / 10,3 px ja 307 px:n kuvassa 12,3 / 11,3 / 10,2 / 9,2 px). Alaindeksit ovat KaTeX:ssä vielä pienempiä; niitä ei ole laskettu erikseen.
- Rasterikuvien sisään piirretty teksti (jos on) ja avauskuvat (`hero`, 1200 px, ei nimiöitä) jäivät mittaamatta.
- Kuvateksti = SVG:n `aria-label`, sillä lähteessä ei ole näkyvää `figcaption`-tekstiä. Kriteerit 3 ja 4 arvioitu siitä.
- Kaappaukset: `site/`-sivujen kuvat 390 px:n näkymässä (laite-skaala 1), kansiossa `docs/audits/2026-11-23-fy10-kuvasaanto/`. Ne ovat repon `site/`-kopiosta, joka voi olla jäljessä mainista; mitat ja tekstit tarkistettu lähteestä.

## Yhteenveto
| Kriteeri | Poikkeavia kuvia |
|---|---|
| 1. Nimiöt vähintään noin 12 px | 24 kuvaa (7 rajalla 11,3–11,4 px; 17 alle 11 px, pienin 9,2 px hyppy/model) |
| 2. Mallikuvaajan akseleilla suure ja yksikkö | 38 mallikuvaajaa; vain kaasu/isokoori kirjoittaa yksikön (T (K)), ja siinäkin vain vaaka-akselilla |
| 3. Kaaviokuvan kuvateksti sanoo sen kaaviokuvaksi | 2 kuvaa |
| 4. Luonnoskuvaaja merkitty malliksi | 4 kuvaajaa ja yleishuomautus (ei näkyvää merkintää kuvassa) |

## 1. Nimiöt vähintään noin 12 px (390 px:n leveys)

| Kuva | Kriteeri | Havainto | Kaappaus |
|---|---|---|---|
| aanennopeus/setup | 1 | 1 nimiötä alle 12 px (pienin 11.3 px, kuva 307 px leveä): `keräin` | [aanennopeus-setup.png](2026-11-23-fy10-kuvasaanto/aanennopeus-setup.png) |
| aanennopeus/signal | 1 | 2 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `mikrofoni 1`, `mikrofoni 2` | [aanennopeus-signal.png](2026-11-23-fy10-kuvasaanto/aanennopeus-signal.png) |
| aanennopeus/model | 1 | 1 nimiötä alle 12 px (pienin 11.3 px, kuva 307 px leveä): `vakiovirhe matkassa` | [aanennopeus-model.png](2026-11-23-fy10-kuvasaanto/aanennopeus-model.png) |
| hissi/vaiheet | 1 | 4 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `liikkeellelähtö`, `tasainen nopeus`, `hidastuminen`, `hissi kulkee ylöspäin` | [hissi-vaiheet.png](2026-11-23-fy10-kuvasaanto/hissi-vaiheet.png) |
| hissi/malli | 1 | 2 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `\Delta v`, `pinta-ala = s` | [hissi-malli.png](2026-11-23-fy10-kuvasaanto/hissi-malli.png) |
| hissi/ryominta | 1 | 2 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `ilman virhettä`, `nollakohdan virhe` | [hissi-ryominta.png](2026-11-23-fy10-kuvasaanto/hissi-ryominta.png) |
| hiuksen-paksuus/pattern | 1 | 1 nimiötä alle 12 px (pienin 11.4 px, kuva 343 px leveä): `kaaviokuva, ei mittakaavassa` | [hiuksen-paksuus-pattern.png](2026-11-23-fy10-kuvasaanto/hiuksen-paksuus-pattern.png) |
| hyppy/model | 1 | 6 nimiötä alle 12 px (pienin 9.2 px, kuva 307 px leveä): `1`, `2`, `3`, `4`, `5`, `6` | [hyppy-model.png](2026-11-23-fy10-kuvasaanto/hyppy-model.png) |
| lammonjohtuminen/emission | 1 | 5 nimiötä alle 12 px (pienin 11.4 px, kuva 343 px leveä): `kiiltävä`, `matta`, `ympäristöstä`, `sama lämpötila koko kappalee`, `lämpökamera` | [lammonjohtuminen-emission.png](2026-11-23-fy10-kuvasaanto/lammonjohtuminen-emission.png) |
| lammonjohtuminen/setup | 1 | 4 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `teipatut sauvat`, `kuuma vesi`, `eristävä kansi`, `lämpökamera` | [lammonjohtuminen-setup.png](2026-11-23-fy10-kuvasaanto/lammonjohtuminen-setup.png) |
| lammonjohtuminen/model | 1 | 2 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `lämpö etenee nopeasti`, `lämpö etenee hitaasti` | [lammonjohtuminen-model.png](2026-11-23-fy10-kuvasaanto/lammonjohtuminen-model.png) |
| liikemaara/setup | 1 | 3 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `anturi 1: +`, `anturi 2: +`, `positiivinen suunta` | [liikemaara-setup.png](2026-11-23-fy10-kuvasaanto/liikemaara-setup.png) |
| liikemaara/model | 1 | 1 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `suuruus pienenee` | [liikemaara-model.png](2026-11-23-fy10-kuvasaanto/liikemaara-model.png) |
| muotokerroin/model | 1 | 3 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `\Delta t`, `\Delta s`, `v_r = \dfrac{\Delta s{\Delta` | [muotokerroin-model.png](2026-11-23-fy10-kuvasaanto/muotokerroin-model.png) |
| muuntaja/setup | 1 | 3 nimiötä alle 12 px (pienin 11.4 px, kuva 343 px leveä): `rautasydän`, `ensiökäämi`, `toisiokäämi` | [muuntaja-setup.png](2026-11-23-fy10-kuvasaanto/muuntaja-setup.png) |
| paristo/model | 1 | 1 nimiötä alle 12 px (pienin 11.4 px, kuva 343 px leveä): `kuorma` | [paristo-model.png](2026-11-23-fy10-kuvasaanto/paristo-model.png) |
| paristo/circuit | 1 | 3 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `kytkin`, `säädettävä vastus`, `suojavastus` | [paristo-circuit.png](2026-11-23-fy10-kuvasaanto/paristo-circuit.png) |
| planck/setup | 1 | 8 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `tasa-`, `jännite-`, `lähde`, `+`, `-`, `\mathrm{A` … | [planck-setup.png](2026-11-23-fy10-kuvasaanto/planck-setup.png) |
| planck/iu | 1 | 1 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `jyrkän osan suora` | [planck-iu.png](2026-11-23-fy10-kuvasaanto/planck-iu.png) |
| planck/grating | 1 | 3 nimiötä alle 12 px (pienin 10.3 px, kuva 343 px leveä): `LED`, `hila`, `silmä` | [planck-grating.png](2026-11-23-fy10-kuvasaanto/planck-grating.png) |
| taitekerroin/model | 1 | 2 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `\Delta(\sin\alpha)`, `\Delta(\sin\beta)` | [taitekerroin-model.png](2026-11-23-fy10-kuvasaanto/taitekerroin-model.png) |
| uppokuumennin/setup | 1 | 8 nimiötä alle 12 px (pienin 11.4 px, kuva 343 px leveä): `virtalähde`, `-`, `+`, `lämpömittari`, `kalorimetri`, `uppokuumennin` … | [uppokuumennin-setup.png](2026-11-23-fy10-kuvasaanto/uppokuumennin-setup.png) |
| valaistus/setup | 1 | 1 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `herkkä pinta lamppua kohti` | [valaistus-setup.png](2026-11-23-fy10-kuvasaanto/valaistus-setup.png) |
| valaistus/model | 1 | 1 nimiötä alle 12 px (pienin 10.2 px, kuva 307 px leveä): `E_tausta` | [valaistus-model.png](2026-11-23-fy10-kuvasaanto/valaistus-model.png) |

## 2. Mallikuvaajan akseleilla suure ja yksikkö

Kaikissa alla olevissa kuvaajissa akselinimiössä on vain suureen symboli (esim. `T²`, `l`), ei yksikköä; mallin mukaan piirretty, joten lukuarvoja ei ole. Isokoori-kuvaajassa on vaaka-akselilla `T (K)`, y-akselilla vain `p`.

| Kuva | Kriteeri | Havainto (akselinimiöt) | Kaappaus |
|---|---|---|---|
| aanennopeus/model | 2 | suure ilman yksikköä: `t_2 - t_1`, `d` | [aanennopeus-model.png](2026-11-23-fy10-kuvasaanto/aanennopeus-model.png) |
| heiluri/model | 2 | suure ilman yksikköä: `l`, `T^2`, `\Delta l`, `\Delta (T^2)` | [heiluri-model.png](2026-11-23-fy10-kuvasaanto/heiluri-model.png) |
| hissi/malli | 2 | suure ilman yksikköä: `a`, `t`, `v`, `t`, `s` | [hissi-malli.png](2026-11-23-fy10-kuvasaanto/hissi-malli.png) |
| hissi/ryominta | 2 | suure ilman yksikköä: `v`, `t`, `s`, `t`, `v_\text{loppu}` | [hissi-ryominta.png](2026-11-23-fy10-kuvasaanto/hissi-ryominta.png) |
| hitausmomentti/model | 2 | suure ilman yksikköä: `h`, `v^2` | [hitausmomentti-model.png](2026-11-23-fy10-kuvasaanto/hitausmomentti-model.png) |
| hiuksen-paksuus/model | 2 | suure ilman yksikköä: `m`, `x_m`, `\Delta m`, `\Delta x_m` | [hiuksen-paksuus-model.png](2026-11-23-fy10-kuvasaanto/hiuksen-paksuus-model.png) |
| hyppy/model | 2 | suure ilman yksikköä: `t`, `N`, `G`, `\boldsymbol{-}`, `\boldsymbol{+}` | [hyppy-model.png](2026-11-23-fy10-kuvasaanto/hyppy-model.png) |
| induktio/pulse | 2 | suure ilman yksikköä: `t`, `U`, `U_\text{max}`, `S`, `\text{toinen pulssi}` | [induktio-pulse.png](2026-11-23-fy10-kuvasaanto/induktio-pulse.png) |
| jaahtyminen/model | 2 | suure ilman yksikköä: `t`, `T`, `T_\text{huone}`, `T_0`, `t_{1/2}` | [jaahtyminen-model.png](2026-11-23-fy10-kuvasaanto/jaahtyminen-model.png) |
| jaahtyminen/linear | 2 | suure ilman yksikköä: `t` | [jaahtyminen-linear.png](2026-11-23-fy10-kuvasaanto/jaahtyminen-linear.png) |
| jousivakio/model | 2 | suure ilman yksikköä: `x`, `F`, `\Delta x`, `\Delta F` | [jousivakio-model.png](2026-11-23-fy10-kuvasaanto/jousivakio-model.png) |
| jousivakio/oscillation | 2 | suure ilman yksikköä: `m`, `T^2`, `\text{vakiotermi}` | [jousivakio-oscillation.png](2026-11-23-fy10-kuvasaanto/jousivakio-oscillation.png) |
| kaasu/boyle | 2 | suure ilman yksikköä: `\dfrac{1}{V}`, `p` | [kaasu-boyle.png](2026-11-23-fy10-kuvasaanto/kaasu-boyle.png) |
| kaasu/isokoori | 2 | suure ilman yksikköä: `273`, `373`, `T\ (\text{K})`, `p`, `\text{mittausalue}` | [kaasu-isokoori.png](2026-11-23-fy10-kuvasaanto/kaasu-isokoori.png) |
| kondensaattori/model | 2 | suure ilman yksikköä: `\tau`, `U_0`, `t`, `u`, `0{,}37\cdot U_0` | [kondensaattori-model.png](2026-11-23-fy10-kuvasaanto/kondensaattori-model.png) |
| kondensaattori/linear | 2 | suure ilman yksikköä: `t`, `\ln u` | [kondensaattori-linear.png](2026-11-23-fy10-kuvasaanto/kondensaattori-linear.png) |
| lammonjohtuminen/model | 2 | suure ilman yksikköä: `t`, `T`, `T_0` | [lammonjohtuminen-model.png](2026-11-23-fy10-kuvasaanto/lammonjohtuminen-model.png) |
| leikkiauto/model-v | 2 | suure ilman yksikköä: `h`, `v`, `v = \sqrt{2gh}` | [leikkiauto-model-v.png](2026-11-23-fy10-kuvasaanto/leikkiauto-model-v.png) |
| leikkiauto/model-v2 | 2 | suure ilman yksikköä: `h`, `v^2`, `v^2 = 2gh`, `v^2 = kh,\ k < 2g` | [leikkiauto-model-v2.png](2026-11-23-fy10-kuvasaanto/leikkiauto-model-v2.png) |
| liikemaara/velocity | 2 | suure ilman yksikköä: `t`, `v`, `v_1`, `v_1'`, `\text{ennen}` | [liikemaara-velocity.png](2026-11-23-fy10-kuvasaanto/liikemaara-velocity.png) |
| liikemaara/model | 2 | suure ilman yksikköä: `p_\text{kok}`, `p_\text{kok}'` | [liikemaara-model.png](2026-11-23-fy10-kuvasaanto/liikemaara-model.png) |
| liukukitka/model | 2 | suure ilman yksikköä: `s`, `\tfrac{1}{2}v_0^2`, `\Delta s` | [liukukitka-model.png](2026-11-23-fy10-kuvasaanto/liukukitka-model.png) |
| liukukitka/velocity | 2 | suure ilman yksikköä: `t`, `v`, `v_0`, `\text{pysähtyy}`, `\Delta t` | [liukukitka-velocity.png](2026-11-23-fy10-kuvasaanto/liukukitka-velocity.png) |
| mikroaaltouuni/model | 2 | suure ilman yksikköä: `k`, `x_k`, `d` | [mikroaaltouuni-model.png](2026-11-23-fy10-kuvasaanto/mikroaaltouuni-model.png) |
| muotokerroin/model | 2 | suure ilman yksikköä: `t`, `s`, `\Delta t`, `\Delta s`, `t` | [muotokerroin-model.png](2026-11-23-fy10-kuvasaanto/muotokerroin-model.png) |
| muotokerroin/mass | 2 | suure ilman yksikköä: `v_\text{r}^2`, `m` | [muotokerroin-mass.png](2026-11-23-fy10-kuvasaanto/muotokerroin-mass.png) |
| muuntaja/model | 2 | suure ilman yksikköä: `N_2/N_1`, `U_2/U_1` | [muuntaja-model.png](2026-11-23-fy10-kuvasaanto/muuntaja-model.png) |
| paristo/curve | 2 | suure ilman yksikköä: `I`, `U`, `E`, `I_\text{k}`, `\Delta I` | [paristo-curve.png](2026-11-23-fy10-kuvasaanto/paristo-curve.png) |
| planck/model | 2 | suure ilman yksikköä: `\dfrac{1}{\lambda}`, `U_\text{k}` | [planck-model.png](2026-11-23-fy10-kuvasaanto/planck-model.png) |
| planck/iu | 2 | suure ilman yksikköä: `U`, `I`, `U_\text{k}` | [planck-iu.png](2026-11-23-fy10-kuvasaanto/planck-iu.png) |
| pomppukorkeus/model | 2 | suure ilman yksikköä: `h_0`, `h_1`, `h_1 = h_0`, `h_1 = a h_0` | [pomppukorkeus-model.png](2026-11-23-fy10-kuvasaanto/pomppukorkeus-model.png) |
| resonanssi/model | 2 | suure ilman yksikköä: `n`, `L`, `\dfrac{\lambda}{2}` | [resonanssi-model.png](2026-11-23-fy10-kuvasaanto/resonanssi-model.png) |
| resonanssi/frequency | 2 | suure ilman yksikköä: `\dfrac{1}{f}`, `\lambda` | [resonanssi-frequency.png](2026-11-23-fy10-kuvasaanto/resonanssi-frequency.png) |
| taitekerroin/model | 2 | suure ilman yksikköä: `\sin\alpha`, `\sin\beta`, `\Delta(\sin\alpha)`, `\Delta(\sin\beta)` | [taitekerroin-model.png](2026-11-23-fy10-kuvasaanto/taitekerroin-model.png) |
| uppokuumennin/model | 2 | suure ilman yksikköä: `E`, `Q`, `Q = E`, `\Delta E`, `\Delta Q` | [uppokuumennin-model.png](2026-11-23-fy10-kuvasaanto/uppokuumennin-model.png) |
| uppokuumennin/heating | 2 | suure ilman yksikköä: `t`, `T`, `T_0`, `\Delta t`, `\Delta T` | [uppokuumennin-heating.png](2026-11-23-fy10-kuvasaanto/uppokuumennin-heating.png) |
| valaistus/model | 2 | suure ilman yksikköä: `1/r^2`, `E`, `E_\text{tausta}` | [valaistus-model.png](2026-11-23-fy10-kuvasaanto/valaistus-model.png) |
| vesivoima/eta | 2 | suure ilman yksikköä: `P_\text{o}`, `P_\text{s}`, `\text{mahdoton alue}`, `\eta = 1`, `\text{sama } \eta` | [vesivoima-eta.png](2026-11-23-fy10-kuvasaanto/vesivoima-eta.png) |

## 3. Kaaviokuvan kuvateksti sanoo sen kaaviokuvaksi

| Kuva | Kriteeri | Havainto | Kaappaus |
|---|---|---|---|
| hyppy/forces | 3 | Kuvateksti alkaa "Kaksi voimakuviota, hyppääjä suorakulmiona"; ei sana kaaviokuva | [hyppy-forces.png](2026-11-23-fy10-kuvasaanto/hyppy-forces.png) |
| liukukitka/forces | 3 | Kuvateksti alkaa "Voimakuvio: …"; ei sana kaaviokuva | [liukukitka-forces.png](2026-11-23-fy10-kuvasaanto/liukukitka-forces.png) |

Muut kaaviot alkavat sanalla Kaaviokuva tai Kytkentäkaavio; avauskuvat ovat Kuvitus-alkuisia.

## 4. Luonnoskuvaaja merkitty malliksi

| Kuva | Kriteeri | Havainto | Kaappaus |
|---|---|---|---|
| jaahtyminen/model | 4 | Kuvateksti sanoo "Newtonin jäähtymislain mukaan", ei "mallin" eikä mallikuvaajaa | [jaahtyminen-model.png](2026-11-23-fy10-kuvasaanto/jaahtyminen-model.png) |
| jaahtyminen/linear | 4 | Sama: "Newtonin jäähtymislain mukaan" | [jaahtyminen-linear.png](2026-11-23-fy10-kuvasaanto/jaahtyminen-linear.png) |
| liikemaara/model | 4 | Kuvateksti: "jos liikemäärä säilyy"; ei sana malli | [liikemaara-model.png](2026-11-23-fy10-kuvasaanto/liikemaara-model.png) |
| vesivoima/eta | 4 | Kuvateksti ei sano mallia eikä luonnosta; kuvaaja alkaa "vaaka-akselilla …" | [vesivoima-eta.png](2026-11-23-fy10-kuvasaanto/vesivoima-eta.png) |
| kaikki mallikuvaajat | 4 | Merkintä "mallin mukaan" / "Mallikuvaaja" on vain kuvatekstissä (`aria-label`); kuvassa itsessään ei ole näkyvää sanaa malli tai luonnos, joten silmin lukija ei näe, ettei kuvaaja ole mitattua dataa (poikkeus: aanennopeus/signal sanoo kuvatekstissä "ei mittausdataa") | – |

## Päätettävää opettajalle
1. Hyväksytäänkö 11,3–11,4 px rajatapauksena vai nostetaanko nimiöt isommiksi?
2. Vaaditaanko mallikuvaajan akselille yksikkö vai riittääkö suureen symboli (aiemmissa auditoinneissa "mallille hyväksyttävä")?
3. Lisätäänkö näkyvä "malli"-merkintä kuvaan vai riittääkö kuvateksti?

## Opettajan päätökset (2026-11-23, koordinaattorin chatissa "Go with recommendations"; välitetty koordinaattorin kautta)
1. **Nimiöt:** 11 px ja yli hyväksytään rajatapauksina. Alle 11 px:n kuvat (esim. hyppy/model 9,2 px) jätetään nyt ennalleen ja kirjataan myöhemmäksi kohdaksi; uusi piirros vaatii opettajan hyväksynnän.
2. **Mallikuvaajan akseli:** suureen symboli riittää, yksikköä ei vaadita.
3. **Malli- ja kaaviokuvamerkintä:** kuvateksti riittää. Puuttuvat sanat lisättiin kuvatekstiin (vain tekstimuutos, kuvia ei muutettu; lähde `lessons/tutkimukset/<id>/figures.py`, kuvat uudelleen generoitu): `Kaaviokuva` hyppy/forces ja liukukitka/forces; `Mallikuvaaja` / `mallin mukaan` jaahtyminen/model ja /linear, liikemaara/model, vesivoima/eta. Katselmoinnit ajettu normaalisti.
