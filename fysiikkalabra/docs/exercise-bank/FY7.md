# FY7 Sähkömagnetismi ja valo: tehtäväpankin täydennys

Nyt 16 lukua × 12 tehtävää (5/4/3), lähes kaikki laskuja (fy7-1:ssä ja fy7-6:ssa 3 sanallista, ei yhtään aineisto-, käsite- tai virheanalyysitehtävää). Moduulin aineistopainotus (Lauri 2026-11-04): magneettikenttien ja induktion mittausaineistot; indusoituneen jännitteen kuvaajat ja muuttujien riippuvuudet; muuntajien mittaustulokset ja sähkömagneettisten aaltojen ominaisuudet; valon heijastumisen, taittumisen ja interferenssin kuva- ja mittausaineistot. Aineistot ovat malliaineistoja (kokeen kuvaus ja mittausjärjestely kerrotaan), ellei lähdettä ja vuotta ole mainittu. Rajaukset: ei itseinduktiota eikä para- tai diamagnetismia, polarisaatio vain kvalitatiivisesti ja Brewsterin laki; fotoni ja ionisoivan säteilyn vaikutukset kuuluvat FY8:aan (spektrin "säteilyn energia" ei siis kvantitoidu fotonin energiana). Olemassa olevat kuvaajatehtävät (fy7-5-L2-02, fy7-7-L2-02, fy7-9-L2-02, fy7-10-L2-04, fy7-11-L2-03) ja katalogin `*-task`-, `*-points`-, `*-fit`- ja `trace`-kuvat on jo käytetty; uusiin aineistoihin tehdään uudet taulukot tai kuvaajat, tai käytetään katalogin kuvaajia ("graph"-kuvat) uudella kysymyksellä. Tavoite 8/7/5.

### fy7-1 Magneetit, magneettinen dipoli ja magneettikenttä
P3. +3/+3/+2. Luvun aineistotehtävät jäävät niukoiksi: kenttä on vektorisumma, mutta mittausaineisto on pääosin kompassi- tai magnetometrilukemia.
- Taso 1: monivalinta "magneetti vetää kaikkia metalleja" ja ferromagnetismi (alumiini, kupari, rauta, nikkeli); monivalinta magneetin katkaisu ja alkeisalueet (kuvaa cut-magnet ei käytetä); lasku: kompassin poikkeama $\tan\varphi = B_m/B_h$ uudella magneetilla ja uudella etäisyydellä.
- Taso 2 (aineisto): taulukko kompassin poikkeamakulmasta magneetin etäisyyden funktiona (malliaineisto, 6 pistettä, $B_m \propto 1/r^3$ -tyyppinen lasku, Maan $B_h = 14\,\mu\text{T}$) → laske $B_m$ jokaisessa pisteessä ja päättele, miten kenttä heikkenee etäisyyden kasvaessa; älypuhelimen magnetometrin kolmikomponenttilukemat (taulukko) kolmessa paikassa huoneessa → kokonaiskenttä ja kulma, missä paikassa on rautaa lähellä. Kokeellinen: miten erotat Maan kentän magneetin kentästä kompassilla ja mitä virhettä aiheuttaa teräspöytä.
- Taso 3: aineisto Helsingin ja Rovaniemen inklinaatiosta ja kokonaiskentästä (malliaineisto tai World Magnetic Model, vuosi mainittu) → vaaka- ja pystykomponentti ja johtopäätös kompassin käytöstä; perustelutehtävä, miksi Maan magneettinen etelänapa on maantieteellisen pohjoisnavan lähellä ja mitä se tarkoittaa kompassin neulan navoille.

### fy7-2 Varatun hiukkasen liike sähkö- ja magneettikentässä
P3. +3/+3/+2.
- Taso 1: monivalinta: magneettikenttä ei muuta hiukkasen vauhtia eikä liike-energiaa (virhekäsitys "kenttä kiihdyttää"); lasku: ympyräradan säde $r = mv/(qB)$ elektronille uudella vauhdilla; lasku: kierrosaika $T = 2\pi m/(qB)$ ja sen riippumattomuus vauhdista.
- Taso 2 (aineisto): sumukammiokuvan malliaineisto: taulukko kolmen hiukkasradan säteistä ja kaarevuudesta samassa kentässä → päättele varauksen merkki (kuva `track-sign`) ja suhde $m/q$; massaspektrometrin ilmaisimen osumakohtien taulukko isotoopeille (esim. neon 20 ja 22, malliaineisto) → massojen suhde ja isotooppien runsaussuhde osumamäärien perusteella. Virheanalyysi: väite "nopeampi hiukkanen kiertää ympyrän nopeammin ympäri".
- Taso 3: nopeusvalitsin + massaspektrometri yhdessä numeerisena mallinnuksena: eri $U_\text{kiihd}$ -arvoilla mitatut säteet (taulukko) → piirrä $r^2$ vs. $U$ ja päättele $m/q$; perustelutehtävä, miksi syklotronin kierrosaika pysyy vakiona ja milloin se lakkaa pitämästä paikkansa (suhteellisuusteoria mainittava vain sivulauseessa).

### fy7-3 Virtajohtimen ja käämin magneettikenttä
P2. +3/+3/+2. Luvun kokeen (magneettivuon tiheyden määritys käämin sisällä) aineistoon sopii kuva `coil-fit`.
- Taso 1: monivalinta oikean käden säännön tilanne (kaksi virran suuntaa, kenttä ympyrässä); lasku: käämin $B$ kun kierroksia lisätään samalla pituudella; lasku: johtimen ja käämin kenttä samalla virralla, kumpi on voimakkaampi.
- Taso 2 (aineisto): käämin $B(I)$ -mittaussarja (malliaineisto: magneettikenttäanturi, 7 pistettä, kierroslukumäärä ja pituus annettu, mukana Maan kentän $\approx 50\,\mu\text{T}$ offset) → sovita suora, päättele $\mu_0 N/l$ -arvo ja vertaa teoriaan; kuvaaja `wire-graph` ($B(r)$ kolmessa etäisyydessä) uudella kysymyksellä: päättele virta ja arvioi $B$ etäisyydellä 3 cm; kokeellinen: miten mittaat käämin sisäkentän ja mitä virheitä Maan kenttä ja anturin suunta aiheuttavat.
- Taso 3: kaksi johdinta ja kompassi: kompassin neulan poikkeamien taulukko eri virroilla → määritä virta vektorisummasta ja Maan vaakakomponentista; mallinnus: käämi, jonka langan pituus ja resistanssi rajoittavat virtaa ($R = \rho l/A$, $I = U/R$ FY6:sta) → suurin saavutettava $B$; perustelu virhekäsityksestä "kenttä kasvaa käämin ulkopuolella samaan tapaan kuin sisällä".

### fy7-4 Voima virtajohtimeen: sähkömoottori ja kaiutin
P2. +3/+3/+2.
- Taso 1: monivalinta voiman suunta ($\overline{F}$ johtimeen, oikean käden sääntö) neljässä kentän ja virran suunnassa; lasku: voima kulmalla $F = BIl\sin\alpha$ kun kulma on kaksinkertainen; lasku: kahden johtimen voima etäisyyden kaksinkertaistuessa.
- Taso 2 (aineisto): virtavaa'an mittaustaulukko (malliaineisto: $\Delta m$ vs. johtimen pituus $l$ eri käämeillä) → laske $B$ jokaisesta ja keskiarvo ± hajonta; kuvaaja `balance-points` uudella kysymyksellä (kuvaajan kulmakertoimesta $B$, kun $l$ annettu) tai kaiuttimen kelan mittaus: $F$ vs. $I$ -taulukko → $B$ ja kelan johtimen kokonaispituus. Virheanalyysi: opiskelija laski virtavaa'asta $B$:n käyttämällä koko johtimen pituutta, vaikka vain osa on kentässä.
- Taso 3: kiskoilla rullaava tanko, jota vetää virta ja jarruttaa kitka: kiihtyvyys, loppunopeus ja energia (yhdistää FY4:n dynamiikan); moottorin toiminta: perustele laadullisesti, miksi kommutaattori vaihtaa virran suunnan joka puolikierroksella, ja arvioi vääntömomentin suuruus numeerisesti suorakulmaiselle silmukalle.

### fy7-5 Sähkömagneettinen induktio
P1. +3/+3/+2. Moduulin aineistopainotuksen ydin: indusoituneen jännitteen kuvaajat.
- Taso 1: monivalinta induktiojännite syntyy vuon muutoksesta, ei vuosta itsestään (levossa oleva magneetti käämissä); lasku: $e = vBl$ uudella tangolla; lasku: kierrosluvun kaksinkertaistaminen ja induktiojännite.
- Taso 2 (aineisto): oskilloskoopin tallennus magneetin putoamisesta käämin läpi (taulukko 12 pisteestä $e(t)$, mallinnettu: kaksi vastakkaismerkkistä piikkiä) → piikkien suuruudet, nopeus käämissä ja jännitteen etumerkki Lenzin lakiin liittämättä (Lenz on fy7-6:ssa); kuvaaja `graph` ($\Phi(t)$ ja $e(t)$) uudella kysymyksellä: piirrä $e(t)$ annetusta paloittain lineaarisesta $\Phi(t)$:stä toisella käämillä ($N$ muutettu). Kokeellinen: miten tutkit induktiojännitteen riippuvuutta liikkeen nopeudesta (taulukko $e_\text{max}$ vs. $v$ → suoran sovitus).
- Taso 3: kääntökela Maan kentän mittaukseen: mittaustaulukko $e_\text{huippu}$ vs. kierrosnopeus kahdessa asennossa → $B$ ja inklinaatio; YO-tyyppinen: vaunu tai tanko liikkuu kiskoilla kiihtyvästi, $e(t)$ taulukkona → johda kiihtyvyys.

### fy7-6 Lenzin laki ja pyörrevirrat
P2. +3/+3/+2. Luvussa 3 sanallista, ei laskuaineistoja.
- Taso 1: monivalinta induktiovirran suunta kuparirenkaassa kun magneetti etääntyy; monivalinta miksi magneetti putoaa alumiiniputkessa hitaammin mutta ei muovipu­kissa; lasku: pyörrevirtajarrun tehonhäviö $P = Fv$.
- Taso 2 (aineisto): putoamisaikojen taulukko (malliaineisto: sama magneetti, putket eri materiaalista ja seinämävahvuudesta, 5 mittausta/ putki) → keskiarvo, hajonta ja johtopäätös materiaalin johtavuudesta; metallinilmaisimen/induktioliesi-aineisto: kattilan materiaali ja lämpenemisaika (taulukko) → mikä materiaali sopii ja miksi (kuva `hob` fy7-16 vältetään). Virheanalyysi: väite "induktiovirta pyrkii kasvattamaan vuon muutosta".
- Taso 3: magneetin putoaminen putkessa kuvaajan $v(t)$ pohjalta: aineisto, jossa nopeus lähestyy rajanopeutta → päättele jarruvoima ja energiahäviö; perustelutehtävä: laminoidun sydämen tehonhäviön pienentyminen (kuva `core`) verrattuna umpinaiseen.

### fy7-7 Generaattori ja vaihtovirta
P1. +3/+3/+2. Aineistoluku (kuvaajat $e(t)$).
- Taso 1: monivalinta jännitteen huippuarvo vs. tehollinen arvo; lasku: tehollinen arvo huippuarvosta ja päinvastoin kotitalouslaitteelle; lasku: taajuus pyörimisnopeudesta.
- Taso 2 (aineisto): oskilloskoopin lukemat (taulukko, $t$ ja $e$, 14 pistettä) → jaksonaika, taajuus, huippu- ja tehollinen arvo; kuvaaja `trace` ja `phi-e` uusilla kysymyksillä (kolme käämin pyörimisnopeutta, päättele $N B A$); kokeellinen: pyörimisnopeuden kaksinkertaistaminen → miten huippuarvo ja taajuus muuttuvat, ennuste ja mittaus.
- Taso 3: polkupyörän napadynamon mittaus (taulukko $f$ vs. $e_0$ eri nopeuksilla, mukana vakiotermi) → sovita suora, $NBA$; YO-tyyppinen: vastuksessa kehittyvä teho $P(t)$ ja keskiteho, kahden generaattorin vertailu (jännite, taajuus, teho).

### fy7-8 Muuntaja ja sähköenergian siirto
P1. +3/+3/+2. Aineistoluku (muuntajan mittaustulokset).
- Taso 1: monivalinta miksi muuntaja ei toimi tasajännitteellä; lasku: ideaalisen muuntajan virta toisiopuolella; lasku: siirtohäviön osuus kun jännite kaksinkertaistuu.
- Taso 2 (aineisto): koulun muuntajamittaus (taulukko: $N_1$, $N_2$, $U_1$, $U_2$, $I_1$, $I_2$, 6 mittausta, 1–5 % virhe, hajonta) → suhteiden $U_2/U_1$ vs. $N_2/N_1$ vertailu ja muuntajan hyötysuhde; siirtojohdon mittaus: jännite vs. häviö eri jännitteillä (taulukko) → päättele $1/U^2$ ja kuvaaja `loss-graph` uudella kysymyksellä (häviö 300 kV:lla). Virheanalyysi: väite "muuntaja kasvattaa tehoa".
- Taso 3: Fingridin 400 kV:n verkko (lähde, vuosi): siirrettävä teho ja johdon resistanssi annettuna → tehohäviön osuus eri jännitteillä ja vuosihäviön energia ja kustannus; kuormitetun muuntajan lämpenemä: sisääntuloteho vs. ulostuloteho taulukkona → hyötysuhde ja häviöteho.

### fy7-9 Sähkömagneettinen säteily ja mustan kappaleen spektri
P2. +3/+3/+2. Ei fotonia: aallonpituuden ja taajuuden yhteys, spektrin alueet, Wienin laki.
- Taso 1: monivalinta aallon rakenne ($\overline{E} \perp \overline{B} \perp$ etenemissuunta); lasku: radioaallon kulkuaika Kuusta/satelliitista; lasku: mikroaaltojen aallonpituus uudella taajuudella.
- Taso 2 (aineisto): kolmen lähteen (taulukko: kynttilän liekki, hehkulanka, Aurinko) spektrihuippuaallonpituudet → lämpötilat ja säteilyn väri; kuvaaja `curves` uudella kysymyksellä (kuvaajasta lämpötila ja huipun siirtymä) ja `spectrum` (taajuus–alue-päättely). Kokeellinen: miten mittaat säteilyn lämpötilan lämpökameralla ja mitä virhettä emissiviteetti aiheuttaa (laadullisesti).
- Taso 3: kosminen taustasäteily (malliaineisto, Wien: huippu $1{,}06\,\text{mm}$) → lämpötila ja mihin sähkömagneettisen spektrin alueeseen huippu kuuluu; YO-tyyppinen: kahden tähden spektrikuvaajista huippuaallonpituudet → lämpötilat ja lämpötilojen suhde, värin perustelu. (Stefan–Boltzmann ei kuulu sisältöihin; teho ja säteilyn energia pois.)

### fy7-10 Valon heijastuminen ja taittuminen
P1. +3/+3/+2. Aineistoluku (taittumiskokeen mittaus).
- Taso 1: monivalinta valo taittuu kohti normaalia siirryttäessä optisesti tiheämpään; lasku: aallonpituus lasissa; lasku: taitekulma uudelle parille.
- Taso 2 (aineisto): puolisylinterikoe (taulukko $\alpha_1$, $\alpha_2$, 7 pistettä, lukematarkkuus $\pm 0{,}5^\circ$) → $\sin\alpha_1$ vs. $\sin\alpha_2$, kulmakerroin ja $n$, epävarmuus; kuvat `fit` ja `protractor` uusilla kysymyksillä (kulmakerroin; kulmanmittarin lukeminen). Virheanalyysi: opiskelija laski taitekulman kulmista suoraan jakamalla $\alpha_1/\alpha_2$.
- Taso 3: näennäinen syvyys ja kuva: mittausaineisto (altaan syvyys ja näennäinen syvyys eri katselukulmilla) → $n$; YO-tyyppinen: kolmen kerroksen rajapinta (ilma–lasi–vesi) ja sädeleveys.

### fy7-11 Dispersio: prisma ja sateenkaari
P2. +3/+3/+2.
- Taso 1: monivalinta miksi violetti taittuu enemmän kuin punainen; lasku: aallonpituus lasissa eri taitekertoimella; lasku: taitekulma kahdelle värille.
- Taso 2 (aineisto): taulukko $n(\lambda)$ kolmelle lasityypille (kruunu-, flintti- ja akryylilasi, tyypilliset arvot) → poikkeamakulmien ero punaiselle ja violetille samalla prismalla; kuvaaja `n-graph` uudella kysymyksellä (arvioi $n$ 600 nm:llä ja valon nopeus). Virheanalyysi: väite "sateenkaaressa punainen on sisäreunalla".
- Taso 3: pisaran taitekulmaan perustuva sateenkaarimalli: taulukko $\theta(\alpha)$ eri tulokulmilla (kuva `theta-graph`) → ääriarvo ja sateenkaaren kulma, kahden värin ero; YO-tyyppinen: prisman huippukulman optimointi spektrometrille.

### fy7-12 Kokonaisheijastuminen ja valokuitu
P2. +3/+3/+2.
- Taso 1: monivalinta kokonaisheijastumisen ehdot; lasku: rajakulma uudelle parille; lasku: valon kulkuaika kuidussa.
- Taso 2 (aineisto): kokeen mittaussarja: rajakulmat eri muoveille (taulukko) → $n$ ja vertailu taulukkoarvoihin; kuvaaja `graph` uudella kysymyksellä (onko aine X vai Y), tai pulssinvääristymä valokuidussa taulukkona (aika ja intensiteetti) → kulkuaikaero.
- Taso 3: valokuidun käyttö: ytimen ja kuoren taitekertoimilla suurin tulokulma ja vastaanottokulma, YO-tyyppinen; timantin hionta ja sädekulku (kuva `diamond`) numeerisena.

### fy7-13 Valon interferenssi ja diffraktio
P1. +3/+3/+2. Aineistoluku; kokeena laserin aallonpituuden määritys hilalla (curriculum `kokeet`).
- Taso 1: monivalinta rakoa kavennettaessa kuvio levenee; lasku: maksimin kulma uudella hilalla; lasku: suurin kertaluku.
- Taso 2 (aineisto): laserin aallonpituuden mittaus (taulukko: $k$, $x_k$, $L$ vakio, 8 pistettä) → $\sin\theta_k$ vs. $k$, kulmakerroin ja $\lambda$; kuvat `pattern`, `setup` ja `white` uusilla kysymyksillä. Virheanalyysi: $\sin\theta$ korvataan $\tan\theta$:lla suurella kulmalla, kuinka suuri virhe.
- Taso 3: kaksoisraon intensiteettikuvaaja (malliaineisto, rakoväli ja varjostimen etäisyys annettu) → $\lambda$ ja ensimmäisten maksimien paikat, vertaa hilaan samalla $d$:llä; YO-tyyppinen: CD- tai DVD-levyn urien väli mittausaineistosta ja heijastushilan geometria.

### fy7-14 Ohuen kalvon interferenssi
P2. +3/+3/+2.
- Taso 1: monivalinta puolen aallonpituuden vaihesiirto (kumpi heijastus, ilma–kalvo vai kalvo–ilma); lasku: pienin paksuus, jolla kalvo heijastaa vihreää voimakkaasti (uusi $n$); lasku: aallonpituus kalvossa ja matkaero.
- Taso 2 (aineisto): taulukko saippuakalvon (malliaineisto, $n = 1{,}33$) paksuuden ja havaitun heijastuneen värin (aallonpituus) suhteesta → päättele kertaluku $m$ ja paksuus kunkin rivin kohdalla; kuvaaja `graph` ($R(\lambda)$ linssin pinnoitteelle) uudella kysymyksellä: mille aallonpituudelle pinnoite on optimoitu ja miksi linssi näyttää purppuraiselta. Virheanalyysi: oppilas jättää puolen aallonpituuden siirtymän huomiotta ja saa tummaksi kohdan, joka on kirkas.
- Taso 3: öljykalvo vedellä (ilma $1{,}00$ / öljy $1{,}47$ / vesi $1{,}33$, ei vaihesiirtoa alapinnalla): paksuus, jolla kalvo on tumma (numeerinen tulos), ja ensimmäiset kolme heijastuvaa aallonpituutta tietyllä paksuudella (taulukon vertailu spektriin); perustelutehtävä: miksi kalvon värit muuttuvat, kun se ohenee valuessaan, ja miksi ylin osa muuttuu mustaksi.

### fy7-15 Valon polarisaatio
P2. +3/+3/+2. Polarisaatio on vain kvalitatiivista sekä Malus ja Brewster.
- Taso 1: monivalinta polaroidut aurinkolasit ja vedenpinnan kiilto (tärkeä lasien suuntaus); lasku: Malus $I = I_0\cos^2\theta$ uudella kulmalla; lasku: Brewsterin kulma uudelle aineelle.
- Taso 2 (aineisto): polarisaattorikoe (malliaineisto, valoanturi, $\theta$ ja $E$ luxeina, 10 pistettä, tausta noin 8 lx) → vähennä tausta, sovita $E$ vs. $\cos^2\theta$ ja päättele $E_0$; kuva `graph` uudella kysymyksellä (kulma, jossa intensiteetti on 40 % maksimista). Virheanalyysi: Brewsterin kulma laskettu taitekertoimien käänteisellä suhteella tai aineen sisältä katsottuna.
- Taso 3: kolme polarisaattoria, keskimmäinen kulmassa $\theta$ ensimmäiseen ja $90^\circ - \theta$ viimeiseen: läpäisevä intensiteetti $\theta$:n funktiona ja suurin arvo ($\theta = 45^\circ$, tulos murtolukuna), tulos taulukkona; perustelu, miksi ristissä olevien polarisaattorien väliin lisätty kolmas päästää valoa läpi.

### fy7-16 Soveltava luku: langaton lataus, induktioliesi ja kuituyhteys
P3. +3/+3/+2. Luvussa on jo lähteellisiä mittauksia (Ravenscraft 2020, Cinia 2016); uudet aineistot ovat malliaineistoja.
- Taso 1: monivalinta miksi induktioliesi ei lämmitä lasia tai alumiinia samalla tavalla kuin terästä; lasku: kuidun teho desibeleistä ($P/P_0 = 10^{-\text{dB}/10}$) uudelle pituudelle; lasku: langattoman laturin hyötysuhde ja häviöteho.
- Taso 2 (aineisto): langattoman laturin vastaanottimen jännite ja hyötysuhde etäisyyden funktiona (taulukko 3–25 mm, malliaineisto) → missä kohdassa hyötysuhde putoaa alle 50 %, ja perustelu kuvan `charger` avulla; kuituyhteyden vaimennusmittaus (taulukko: pituus ja vastaanotettu teho dBm:nä) → vaimennuskerroin dB/km sovittamalla suora. Virheanalyysi: desibelit laskettu suoraan prosentteina tehosta.
- Taso 3: kuituyhteyden vahvistinvälien suunnittelu (lähetysteho, herkkyys, vaimennus 0,18 dB/km, liitoshäviöt): kuinka monta vahvistinta 600 km:n linkkiin; perustelutehtävä: induktioliesi, jossa kattilan materiaalin muutos muuttaa pyörrevirran tehoa, ja arvio siitä, mitä taajuuden nosto tekee.
