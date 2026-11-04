# FY4 Voima ja liike: tehtäväpankin täydennys

Nyt 16 lukua × 12 tehtävää (5/4/3), kaikki numeerisia laskuja; voimakuviotehtävät (`"fbd"`) säilyvät.
Moduulin aineistopainotus (Lauri 2026-11-04): liikkeen videoanalyysi, paikka-, nopeus- ja kiihtyvyyskuvaajat;
voima-antureiden mittaustulokset, impulssi ja törmäykset. Nopeus, kiihtyvyys ja voima aina eri väreillä
(sääntö 12), vektorit $\overline{F}$ (sääntö 14). Videoanalyysi- ja anturiaineistot kuvataan Vernier Graphical
Analysis -työkaluilla tehdyiksi, kun työkalu mainitaan. Tavoite 8/7/5.

### fy4-1 Paikka, nopeus ja tasainen liike kuvaajina
P1. +3/+3/+2.
- Taso 1: monivalinta $(t,x)$-kuvaajan kulmakerroin ja etumerkki; nopeus kahdesta pisteestä; siirtymä vs. matka.
- Taso 2 (aineisto): videoanalyysin paikkataulukko → $(t,x)$-sovitus, nopeus ja alkupaikka; kahden kappaleen $(t,x)$-kuvaaja (figure) → kumpi nopeampi, kohtaaminen. Kuvaajan tulkinta: $(t,x)$ → $(t,v)$-kuvaajan piirtäminen.
- Taso 3: videoaineisto, jossa kameran perspektiivi tai mittakaava väärin → systemaattisen virheen arviointi; ennuste ja sen luotettavuus aineiston ulkopuolella.

### fy4-2 Kiihtyvyys ja tasaisesti kiihtyvä liike
P1. +3/+3/+2.
- Taso 1: monivalinta kiihtyvyyden suunta jarrutuksessa; $a = \Delta v/\Delta t$; matka $(t,v)$-kuvaajan pinta-alana.
- Taso 2 (aineisto): kaltevalla tasolla vierivän kärryn videoaineisto $(t, v)$ → kiihtyvyys sovituksesta; $(t,x)$-taulukko kiihtyvästä liikkeestä → paraabeli, linearisointi $(t^2, x)$. Kokeellinen: valoportit vs. videoanalyysi, kumpi tarkempi.
- Taso 3: auton kiihdytysaineisto (0–100 km/h, mittaussarja) → onko kiihtyvyys vakio, perustelu ja malli; YO-tyyppinen kuvaajan piirtäminen ja tulkinta $(t,v)$ → $(t,a)$ ja $(t,x)$ laadullisesti.

### fy4-12 Kahden kappaleen liikkeiden vertailu
P2. +3/+3/+2.
- Taso 1: monivalinta saman nopeuden hetki $(t,v)$-kuvaajassa ≠ kohtaaminen; kohtaamisen ehto; lähtöviive.
- Taso 2 (aineisto): kahden juoksijan videoanalyysitaulukko → kohtaamishetki ja -paikka; $(t,v)$-kuvaaja kahdesta autosta (figure) → etäisyys hetkellä $t$. Virheanalyysi: oppilas asettaa nopeudet yhtä suuriksi kohtaamista etsiessään.
- Taso 3: ohitustilanne aineistona (nopeudet, etäisyys, vastaantuleva auto) → riittääkö matka, perustelu; mallinna liikennevaloissa kiihdyttävä auto ja ohittava pyöräilijä.

### fy4-3 Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki
P1. +3/+3/+2.
- Taso 1: monivalinnat "liike vaatii voiman" ja voima–vastavoima-pari (eri kappaleisiin); voimaparin tunnistaminen kuvasta.
- Taso 2 (aineisto): kahden voima-anturin mittauskuvaaja vetokokeessa (figure) → voimat yhtä suuret joka hetki; kärryn nopeus–aika-aineisto kitkattomalla radalla → I laki. Virheanalyysi: väärin piirretty voimapari.
- Taso 3: perustelu hevonen–kärry-paradoksista; aineisto törmäävistä kärryistä anturilla → III laki ja selitys, miksi kevyempi kiihtyy enemmän.

### fy4-4 Newtonin toinen laki
P1. +3/+3/+2.
- Taso 1: monivalinta kokonaisvoima ja kiihtyvyyden suunta; $F = ma$; massan ratkaiseminen.
- Taso 2 (aineisto): kärrymittaus eri vetovoimilla $(F, a)$ → massa kulmakertoimesta; mittaus eri massoilla samalla voimalla $(1/m, a)$ → linearisointi. Kokeellinen: vakioitavat muuttujat ja kitkan vaikutus vakiotermiin.
- Taso 3: aineisto, jossa sovitettu suora ei kulje origon kautta → kitkavoiman arvio vakiotermistä; YO-tyyppinen hissikuvaaja $(t,a)$ → tukivoima eri vaiheissa.

### fy4-5 Voimakuvio ja voimien yhteisvaikutus
P1. +3/+3/+2. Voimakuviotyypit (`fbd`) mukaan uusiin.
- Taso 1: monivalinta oikea voimakuvio (`fbd: select`); kokonaisvoiman lasku kahdesta voimasta; voimien tunnistus (`identify`).
- Taso 2 (aineisto): voima-anturilla mitatut kolmen köyden voimat tasapainossa → komponentit ja tarkistus; virheellinen voimakuvio (`error`) → korjaus. Kokeellinen: miten mittaat kahden vinon voiman summan.
- Taso 3: piirrettävä voimakuvio (`draw`) monivaiheisessa tilanteessa ja liikeyhtälö; perustelu: miksi tukivoima ei aina ole $mg$.

### fy4-13 Liikeyhtälö kytketyille kappaleille
P2. +3/+3/+2.
- Taso 1: monivalinta narun jännitys vs. riippuvan kappaleen paino kiihtyvässä systeemissä; systeemin kiihtyvyys; jännitys.
- Taso 2 (aineisto): Atwoodin koneen mittaukset eri massaeroilla → $a$ vs. $\Delta m$-kuvaaja ja $g$; pöydällä kärry + punnus -mittaustaulukko → kitkan arvio. Virheanalyysi: koko systeemin massa unohdettu.
- Taso 3: mallinna junan vaunujen kytkentävoimat; perustelu: mitä tapahtuu jännitykselle, jos massat vaihdetaan.

### fy4-6 Paino, kitka ja kalteva taso
P1. +3/+3/+2.
- Taso 1: monivalinta lepokitka vs. liukukitka; $F_\mu = \mu N$; tukivoima kaltevalla tasolla.
- Taso 2 (aineisto): voima-anturilla vedetyn puupalan kuvaaja (figure, lepokitkan huippu) → $\mu_0$ ja $\mu$; kitkavoima vs. normaalivoima -mittaussarja → $\mu$ kulmakertoimesta. Kokeellinen: kitkakertoimen mittaus kaltevaa tasoa kallistamalla.
- Taso 3: aineisto kitkakertoimista eri pinnoilla (märkä/kuiva asfaltti) → jarrutusmatkat ja perustelu; virheanalyysi: $N = mg$ kaltevalla tasolla.

### fy4-14 Ilmanvastus ja putoaminen ilmassa
P2. +3/+3/+2.
- Taso 1: monivalinta rajanopeuden ehto; voimakuvio putoavasta kappaleesta; rajanopeuden riippuvuus massasta laadullisesti.
- Taso 2 (aineisto): kahvinsuodattimien putoamisen videoaineisto (1–4 sisäkkäin) → rajanopeudet ja $F \propto v^2$ -testi; $(t,v)$-kuvaaja laskuvarjohypystä (figure) → vaiheet. Kuvaajan tulkinta: kiihtyvyys pienenee.
- Taso 3: linearisointi $(v_\text{raja}^2, m)$ ja ilmanvastusmallin arviointi; perustelu: miksi sadepisarat eivät ole vaarallisia.

### fy4-7 Liike-energia, potentiaalienergia ja mekaaninen energia
P2. +3/+3/+2.
- Taso 1: monivalinta nopeuden kaksinkertaistuminen → liike-energia nelinkertaiseksi; $E_k$; $E_p$.
- Taso 2 (aineisto): pudotetun pallon videoaineisto → $E_k$, $E_p$ ja summa ajan funktiona; energiapylväskuvaaja (figure) → tunnista tilanne. Virheanalyysi: nollatason valinta.
- Taso 3: aineisto, jossa mekaaninen energia pienenee → häviöiden arvio ja syy; perustelu nollatason vapaasta valinnasta.

### fy4-8 Mekaanisen energian säilyminen ja energiaperiaate
P1. +3/+3/+2. Luvussa jo kaksi aineistolaskua.
- Taso 1: monivalinta nopeus ei riipu radan muodosta; nopeus pudotuskorkeudesta; korkeus nopeudesta.
- Taso 2 (aineisto): heilurin nopeus alimmassa kohdassa eri korkeuksilta → $(h, v^2)$ ja $g$; vuoristoradan mittausaineisto → kitkahäviöt. Kokeellinen: valoportti heilurin alakohdassa.
- Taso 3: YO-tyyppinen energiaperiaatetehtävä kitkatyön kanssa (pulkka mäessä, aineisto matkoista); perustelu: säilyykö energia pomppivassa pallossa (aineisto pomppukorkeuksista).

### fy4-15 Vesi- ja tuulivoima energian muuntajina
P3. +3/+3/+2.
- Taso 1: monivalinta putouskorkeuden merkitys; vesivoiman teho; tuulen liike-energia.
- Taso 2 (aineisto): tuulivoimalan tehokäyrä (figure) → teho eri tuulennopeuksilla ja vuosienergia annetulla jakaumalla; joen virtaama kuukausittain → vesivoimalan tuotannon vaihtelu. Virheanalyysi: teho verrannollinen nopeuteen eikä sen kuutioon.
- Taso 3: mallinna tuulen tehon riippuvuus nopeudesta ($P \propto v^3$) aineistosta; perustelu pumppuvoimalan energiavarastosta.

### fy4-9 Liikemäärä ja impulssi
P1. +3/+3/+2.
- Taso 1: monivalinta liikemäärän suunta; $p = mv$; impulssi $F\Delta t$.
- Taso 2 (aineisto): voima-anturin törmäyskuvaaja (figure) → impulssi pinta-alana ja nopeuden muutos; pallon potku -mittaustaulukko → keskimääräinen voima. Kokeellinen: miten turvatyyny pienentää voimaa (sama impulssi, pidempi aika).
- Taso 3: kahden törmäyksen voimakuvaajat (pehmeä/kova) → vertailu ja perustelu; YO-tyyppinen impulssitehtävä pomppaavasta pallosta (suunnanmuutos).

### fy4-10 Liikemäärän säilyminen ja yksiulotteiset törmäykset
P1. +3/+3/+2.
- Taso 1: monivalinta kimmoisa vs. kimmoton; yhteen tarttuvat kärryt; rekyyli.
- Taso 2 (aineisto): kärrytörmäyksen videoanalyysi (nopeudet ennen ja jälkeen) → säilyykö liikemäärä ja liike-energia; törmäysten taulukko → luokittele kimmoisuus. Virheanalyysi: etumerkki unohtunut vastakkaisissa nopeuksissa.
- Taso 3: liikennetutkinta: jarrutusjäljistä ja massoista törmäysnopeus (monivaiheinen); aineisto, jossa liikemäärä ei säily → ulkoinen voima (kitka) ja sen arvio.

### fy4-11 Liikenneturvallisuus: jarrutus, turvavyö ja turvatyyny
P2. +3/+3/+2.
- Taso 1: monivalinta reaktiomatka vs. jarrutusmatka; pysähtymismatka; nopeuden vaikutus jarrutusmatkaan.
- Taso 2 (aineisto): pysähtymismatkataulukko eri nopeuksilla → $(v, s)$ ja $(v^2, s_\text{jarru})$ -linearisointi; törmäystestin kiihtyvyyskuvaaja (figure) → suurin hidastuvuus g:nä. Virheanalyysi: väite "nopeuden kaksinkertaistuessa jarrutusmatka kaksinkertaistuu".
- Taso 3: YO-tyyppinen tienpitotehtävä märällä tiellä aineistosta; perustelu turvavyön ja turvatyynyn yhteisvaikutuksesta impulssin kautta.

### fy4-16 Soveltava tunti: hissi, laskuvarjo ja kelkkamäki
P3. +3/+3/+2.
- Taso 1: monivalinnat hissin vaa'an lukemasta eri vaiheissa; yksi lasku.
- Taso 2 (aineisto): puhelimen kiihtyvyysanturin hissiaineisto (figure) → vaiheet, kiihtyvyydet, kerrosväli; kelkkamäen videoaineisto → kitkakerroin. Kokeellinen: oma anturimittaus ja sen epävarmuudet.
- Taso 3: avoin YO-tyyppinen mallinnus (kelkkamäen turvallinen pituus pysähtymiselle); aineisto laskuvarjohypystä → ilmanvastuskertoimen arvio.
