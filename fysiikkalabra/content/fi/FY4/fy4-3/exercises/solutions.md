## fy4-3-L1-01
**Annettu:** lampun paino $G = 18\,\text{N}$, lamppu on paikallaan
**Kysytty:** johdon jännitysvoima $T$ yksikössä $\text{N}$
**Periaate:** Lamppu on levossa, joten Newtonin ensimmäisen lain mukaan siihen vaikuttavien voimien summa on nolla. Lamppuun vaikuttavat vain Maa ja johto.
**Voimakuvio:** Lamppu suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja johdon jännitysvoima $\overline{T}$ yläpinnasta ylös, yhtä pitkinä.
```voimakuvio
G 18
T 18 ylös
a 0
```
**Kaava:** $T - G = 0$, joten $T = G$
**Muunnokset:** Paino on newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $T = G = 18\,\text{N}$
**Vastaus:** $18\,\text{N}$, kaksi merkitsevää numeroa kuten painossa $18\,\text{N}$.
**Järkevyys:** Jos johto vetäisi vähemmän kuin $18\,\text{N}$, paino voittaisi ja lamppu lähtisi liikkeelle alaspäin; jos enemmän, se lähtisi ylöspäin. Paikallaan pysyminen vaatii täsmälleen painon suuruisen voiman. Johto vaikuttaa lamppuun ylöspäin, koska naru voi vain vetää.

## fy4-3-L1-02
**Annettu:** joukkueen A voima köyteen $F_A = 850\,\text{N}$ vasemmalle, köysi on paikallaan, köyden paino jätetään huomiotta
**Kysytty:** joukkueen B voima köyteen $F_B$ yksikössä $\text{N}$
**Periaate:** Köysi on levossa, joten Newtonin ensimmäisen lain mukaan siihen vaikuttavien voimien summa on nolla. Vaakasuunnassa köyteen vaikuttavat vain joukkueiden vedot.
**Voimakuvio:** Köysi pitkänä suorakulmiona, positiivinen suunta oikealle. Joukkueen A veto $\overline{F}_A$ köyden vasemmasta päästä vasemmalle ja joukkueen B veto $\overline{F}_B$ oikeasta päästä oikealle.
```voimakuvio
F_A 850 vasen
F_B 850 oikea
a 0
```
**Kaava:** $F_B - F_A = 0$, joten $F_B = F_A$
**Muunnokset:** Voima on newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_B = F_A = 850\,\text{N}$
**Vastaus:** $850\,\text{N}$, kolme merkitsevää numeroa kuten voimassa $850\,\text{N}$.
**Järkevyys:** Jos B vetäisi heikommin, köysi lähtisi liikkeelle vasemmalle. Köydenvedon voittaa se joukkue, joka saa maasta suuremman kitkavoiman jalkoihinsa, ei se, joka vetää köyttä lujemmin: köysi vetää kumpaakin joukkuetta yhtä suurella voimalla.

## fy4-3-L1-03
**Annettu:** luistelijan voima laitaan $F_{\text{LK}} = 90\,\text{N}$ laitaa kohti
**Kysytty:** laidan voima luistelijaan $F_{\text{KL}}$ yksikössä $\text{N}$
**Periaate:** Newtonin kolmas laki: luistelija ja laita vuorovaikuttavat, joten laita vaikuttaa luistelijaan yhtä suurella mutta vastakkaissuuntaisella voimalla. Laki pätee riippumatta siitä, liikkuuko kumpikaan.
**Voimakuvio:** Valitaan kappaleeksi luistelija, joka piirretään suorakulmiona; positiivinen suunta on laidasta poispäin. Luistelijaan vaikuttavat paino alas, jään tukivoima ylös ja laidan voima $\overline{F}_{\text{KL}}$ luistelijasta poispäin, päättyen luistelijan kylkeen. Hänen oma voimansa laitaan $\overline{F}_{\text{LK}}$ vaikuttaa laitaan, joten se ei kuulu hänen kuvioonsa vaan on kysytyn voiman vastavoima.
```voimakuvio
pinta 0
G 590
N 590
F_KL 90 oikea työntö
a oikea
```
**Kaava:** $\overline{F}_{\text{KL}} = -\overline{F}_{\text{LK}}$, joten suuruuksina $F_{\text{KL}} = F_{\text{LK}}$
**Muunnokset:** Voima on newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_{\text{KL}} = F_{\text{LK}} = 90\,\text{N}$
**Vastaus:** $90\,\text{N}$ luistelijasta poispäin laidasta, kaksi merkitsevää numeroa kuten voimassa $90\,\text{N}$.
**Järkevyys:** Luistelija lähtee liukumaan poispäin laidasta, joten häneen on vaikuttanut voima laidasta poispäin. Sen aiheuttaja on laita. Laita ei liiku, koska se on kiinni jäässä ja kaukalon rakenteissa, jotka vaikuttavat siihen omilla voimillaan.

## fy4-3-L1-04
**Annettu:** tien voima renkaisiin eteenpäin $F = 620\,\text{N}$, ilmanvastus $F_\text{i} = 380\,\text{N}$, nopeus on vakio ja tie suora
**Kysytty:** vierimisvastus $F_\text{r}$ yksikössä $\text{N}$
**Periaate:** Auto liikkuu suoraviivaisesti tasaisella nopeudella, joten Newtonin ensimmäisen lain mukaan kokonaisvoima on nolla myös liikkeen suunnassa: eteenpäin ja taaksepäin vaikuttavat voimat ovat yhtä suuret.
**Voimakuvio:** Auto suorakulmiona, positiivinen suunta eteenpäin. Vaakasuunnassa tien voima $\overline{F}$ eteenpäin, ilmanvastus $\overline{F}_\text{i}$ ja vierimisvastus $\overline{F}_\text{r}$ taaksepäin. Pystysuunnassa paino ja tien tukivoima kumoavat toisensa.
```voimakuvio
pinta 0
erikseen
G 12000
N 12000
F 620 oikea
F_i 380 vasen
F_r 240 vasen
a 0
```
**Kaava:** $F - F_\text{i} - F_\text{r} = 0$, joten $F_\text{r} = F - F_\text{i}$
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{r} = 620\,\text{N} - 380\,\text{N} = 240\,\text{N}$
**Vastaus:** $240\,\text{N}$, kymmenen newtonin tarkkuudella kuten annetut voimat, joten kaksi merkitsevää numeroa.
**Järkevyys:** Vastusten summa $380\,\text{N} + 240\,\text{N} = 620\,\text{N}$ on yhtä suuri kuin eteenpäin vievä voima, joten nopeus ei muutu. Vierimisvastus on pienempi kuin ilmanvastus, mikä sopii maantienopeuksiin, joilla ilmanvastus on autolle suurin vastus.

## fy4-3-L1-05
**Annettu:** kirjan massa $m = 0{,}65\,\text{kg}$, Maan voima kirjaan on kirjan paino; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kirjan voima Maahan $F$ yksikössä $\text{N}$
**Periaate:** Maa ja kirja vetävät toisiaan. Newtonin kolmannen lain mukaan kirja vetää Maata yhtä suurella voimalla kuin Maa kirjaa, mutta vastakkaiseen suuntaan eli ylöspäin. Maan voima kirjaan on paino $G = mg$.
**Voimakuvio:** Valitaan kappaleeksi kirja, joka piirretään suorakulmiona; positiivinen suunta on ylös. Kirjaan vaikuttavat paino $\overline{G}$ keskipisteestä alas ja pöydän tukivoima $\overline{N}$ alapinnasta ylös. Paino on Maan voima kirjaan, ja sen vastavoima on kirjan voima $\overline{F}$ Maahan, joka vaikuttaa Maahan eikä kuulu kirjan kuvioon.
```voimakuvio
pinta 0
G 6,3765
N 6,3765
a 0
```
**Kaava:** $F = G$ ja $G = mg$, joten $F = mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F = 0{,}65\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 6{,}3765\,\text{N}$
**Vastaus:** $6{,}4\,\text{N}$ ylöspäin kohti kirjaa, kaksi merkitsevää numeroa kuten massassa $0{,}65\,\text{kg}$.
**Järkevyys:** Kilogramman paino on noin $10\,\text{N}$, joten $0{,}65\,\text{kg}$:n kirjan paino on noin $6\,\text{N}$. Maa ei huomattavasti liiku tämän voiman vaikutuksesta, koska sen massa on valtava. Pöydän tukivoima ei ole painon vastavoima, vaan se kuuluu kirjan ja pöydän vuorovaikutukseen.

## fy4-3-L2-01
**Annettu:** alemman kirjan paino $G_1 = 8{,}0\,\text{N}$, ylemmän kirjan paino $G_2 = 5{,}0\,\text{N}$, kirjat ovat paikallaan
**Kysytty:** alemman kirjan voima pöytään $F$ yksikössä $\text{N}$
**Periaate:** Ylempi kirja on levossa, joten alempi kirja tukee sitä voimalla $G_2$ (ensimmäinen laki), ja kolmannen lain mukaan ylempi kirja painaa alempaa yhtä suurella voimalla alaspäin. Alempi kirja on myös levossa, joten pöydän tukivoima siihen on yhtä suuri kuin alaspäin vaikuttavat voimat yhteensä. Lopuksi alempi kirja painaa pöytää tukivoiman suuruisella voimalla (kolmas laki).
**Voimakuvio:** Alempi kirja suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}_1$ keskipisteestä alas, ylemmän kirjan voima $\overline{F}_2$ yläpinnasta alas ja pöydän tukivoima $\overline{N}$ alapinnasta ylös.
```voimakuvio
pinta 0
G_1 8,0
F_2 5,0 alas työntö
N 13
a 0
```
**Kaava:** $N - G_1 - F_2 = 0$ ja $F_2 = G_2$, joten $F = N = G_1 + G_2$
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F = 8{,}0\,\text{N} + 5{,}0\,\text{N} = 13\,\text{N}$
**Vastaus:** $13\,\text{N}$ alaspäin. Summa on kymmenesosanewtonin tarkkuudella kuten painot $8{,}0\,\text{N}$ ja $5{,}0\,\text{N}$, joten siinä on kaksi merkitsevää numeroa.
**Järkevyys:** Pöytä kannattelee molempia kirjoja, joten sen on tuettava niiden yhteistä painoa. Ylempi kirja ei kuitenkaan koske pöytää: sen paino välittyy pöytään alemman kirjan kautta voimaparien ketjuna.

## fy4-3-L2-02
**Annettu:** uimarin voima veteen $F_{\text{UV}} = 65\,\text{N}$ taaksepäin, uimarin paino $720\,\text{N}$ ja veden noste yhtä suuri, uimari ui suoraan vaakasuunnassa tasaisella nopeudella
**Kysytty:** veden vastus uimariin $F_\text{v}$ yksikössä $\text{N}$
**Periaate:** Kolmannen lain mukaan vesi työntää uimaria eteenpäin yhtä suurella voimalla $F_{\text{VU}} = 65\,\text{N}$; se vie uimaria eteenpäin. Uimari liikkuu tasaisella nopeudella, joten ensimmäisen lain mukaan vaakasuuntaisten voimien summa on nolla. Paino ja noste ovat pystysuoria eivätkä vaikuta vaakasuuntaiseen tasapainoon, joten niitä ei tarvita: veden vastus taaksepäin on yhtä suuri kuin veden työntö eteenpäin.
**Voimakuvio:** Uimari suorakulmiona, positiivinen suunta eteenpäin. Veden työntö $\overline{F}_{\text{VU}}$ eteenpäin ja veden vastus $\overline{F}_\text{v}$ taaksepäin. Pystysuunnassa noste ja paino kumoavat toisensa.
```voimakuvio
G 720
F_n 720 ylös
F_VU 65 oikea
F_v 65 vasen
a 0
```
**Kaava:** $F_{\text{VU}} - F_\text{v} = 0$ ja $F_{\text{VU}} = F_{\text{UV}}$, joten $F_\text{v} = F_{\text{UV}}$
**Muunnokset:** Voima on newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{v} = F_{\text{UV}} = 65\,\text{N}$
**Vastaus:** $65\,\text{N}$ taaksepäin, kaksi merkitsevää numeroa kuten voimassa $65\,\text{N}$.
**Järkevyys:** Uimari pääsee eteenpäin vain siksi, että vesi työntää häntä; ilman vastavoimaa käsien vetäminen ei liikuttaisi häntä mihinkään. Jos hän työntäisi vettä lujemmin, eteenpäin vievä voima kasvaisi ja hän kiihtyisi, kunnes vastus kasvaisi yhtä suureksi.

## fy4-3-L2-03
**Annettu:** massa varusteineen $m = 85\,\text{kg}$, nopeus on vakio ja suoraan alas; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** ilmanvastus $F_\text{v}$ yksikössä $\text{N}$
**Periaate:** Hyppääjä laskeutuu suoraviivaisesti tasaisella nopeudella, joten Newtonin ensimmäisen lain mukaan kokonaisvoima on nolla. Häneen vaikuttavat Maa (paino alas) ja ilma (vastus ylös, liikettä vastaan).
**Voimakuvio:** Hyppääjä ja varjo suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas ja ilmanvastus $\overline{F}_\text{v}$ ylös, yhtä pitkinä. Nopeus alas piirretään erikseen, ei voimaksi.
```voimakuvio
G 833,85
F_v 833,85 ylös
a 0
v alas
```
**Kaava:** $F_\text{v} - G = 0$ ja $G = mg$, joten $F_\text{v} = mg$
**Muunnokset:** Massa on kilogrammoina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{v} = 85\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 833{,}85\,\text{N}$
**Vastaus:** $830\,\text{N}$ eli $8{,}3\cdot 10^{2}\,\text{N}$ ylöspäin, kaksi merkitsevää numeroa kuten massassa $85\,\text{kg}$.
**Järkevyys:** $85\,\text{kg}$:n paino on noin $850\,\text{N}$, ja ilmanvastus on yhtä suuri. Liike alaspäin ei vaadi alaspäin vaikuttavaa kokonaisvoimaa: hyppääjä liikkuu alas jatkavuuden takia, ja voimat ovat tasapainossa.

## fy4-3-L2-04
**Annettu:** korin paino $G_\text{k} = 5{,}8\,\text{kN}$, matkustajien massa $m = 320\,\text{kg}$, hissi nousee tasaisella nopeudella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** kaapelin jännitysvoima $T$ yksikössä $\text{kN}$
**Periaate:** Kori ja matkustajat liikkuvat yhdessä tasaisella nopeudella, joten ensimmäisen lain mukaan niihin vaikuttavien voimien summa on nolla. Kun kori ja matkustajat ajatellaan yhdeksi kappaleeksi, kaapeli kannattelee niiden yhteistä painoa.
**Voimakuvio:** Kori matkustajineen suorakulmiona, positiivinen suunta ylös. Kaapelin jännitysvoima $\overline{T}$ yläpinnasta ylös, korin paino $\overline{G}_\text{k}$ ja matkustajien paino $\overline{G}_\text{m}$ alas.
```voimakuvio
T 8939,2 ylös
G_k 5800
G_m 3139,2
a 0
```
**Kaava:** $T - G_\text{k} - mg = 0$, joten $T = G_\text{k} + mg$
**Muunnokset:** $5{,}8\,\text{kN} = 5800\,\text{N}$; lopuksi newtonit muunnetaan kilonewtoneiksi jakamalla luvulla $1000$.
**Sijoitus:** $T = 5800\,\text{N} + 320\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 = 5800\,\text{N} + 3139{,}2\,\text{N} = 8939{,}2\,\text{N}$
**Vastaus:** $8{,}9\,\text{kN}$, kaksi merkitsevää numeroa kuten korin painossa $5{,}8\,\text{kN}$.
**Järkevyys:** Matkustajien paino on noin $3\,\text{kN}$, ja $5{,}8\,\text{kN} + 3\,\text{kN} \approx 9\,\text{kN}$. Tasaisessa nousussa jännitysvoima on täsmälleen sama kuin paikallaan seisovassa hississä, koska nopeus ei muutu.

## fy4-3-L3-01
**Annettu:** yhteinen paino $G = 4{,}62\,\text{kN}$, noste $F_\text{n} = 4{,}35\,\text{kN}$, pallo laskeutuu suoraan alas tasaisella nopeudella
**Kysytty:** ilmanvastus $F_\text{v}$ yksikössä $\text{kN}$ ja sen suunta
**Periaate:** Pallo liikkuu tasaisella nopeudella, joten ensimmäisen lain mukaan kokonaisvoima on nolla. Ilmanvastus on liikettä vastaan, ja pallo liikkuu alas, joten vastus osoittaa ylös. Noste ei yksin riitä kumoamaan painoa, joten ilmanvastus kannattelee loput.
**Voimakuvio:** Pallo koreineen suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas, noste $\overline{F}_\text{n}$ ylös ja ilmanvastus $\overline{F}_\text{v}$ ylös. Nopeus alas erikseen, ei voimaksi.
```voimakuvio
G 4620
F_n 4350 ylös
F_v 270 ylös
a 0
v alas
```
**Kaava:** $F_\text{n} + F_\text{v} - G = 0$, joten $F_\text{v} = G - F_\text{n}$
**Muunnokset:** Kaikki voimat ovat kilonewtoneina ja vastaus pyydetään kilonewtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{v} = 4{,}62\,\text{kN} - 4{,}35\,\text{kN} = 0{,}27\,\text{kN}$
**Vastaus:** $0{,}27\,\text{kN}$ ylöspäin. Erotuksessa on kaksi merkitsevää numeroa, koska annetut voimat ovat sadasosakilonewtonin tarkkuudella.
**Järkevyys:** Jos ilmanvastusta ei olisi, painon ja nosteen erotus $0{,}27\,\text{kN}$ alaspäin muuttaisi pallon liikettä ja se laskeutuisi yhä nopeammin. Tasainen laskeutuminen tarkoittaa, että ilmanvastus on kasvanut juuri tämän erotuksen suuruiseksi. Ilmanvastus osoittaa ylös, vaikka liike on alas.

## fy4-3-L3-02
**Annettu:** kummankin magneetin paino $G = 0{,}30\,\text{N}$, ylempi magneetti leijuu paikallaan, kitka ja tikun voima jätetään huomiotta
**Kysytty:** pöydän tukivoima alempaan magneettiin $N$ yksikössä $\text{N}$
**Periaate:** Ylempi magneetti on levossa, joten alemman magneetin hylkimisvoima siihen on ylös ja yhtä suuri kuin sen paino (ensimmäinen laki). Kolmannen lain mukaan ylempi magneetti hylkii alempaa yhtä suurella voimalla alaspäin, vaikka magneetit eivät kosketa toisiaan. Alempi magneetti on levossa, joten pöydän tukivoima kumoaa sen painon ja tämän voiman.
**Voimakuvio:** Alempi magneetti suorakulmiona, positiivinen suunta ylös. Paino $\overline{G}$ keskipisteestä alas, ylemmän magneetin voima $\overline{F}_\text{m}$ yläpinnasta alas ja pöydän tukivoima $\overline{N}$ alapinnasta ylös.
```voimakuvio
pinta 0
G 0,30
F_m 0,30 alas työntö
N 0,60
a 0
```
**Kaava:** $N - G - F_\text{m} = 0$ ja $F_\text{m} = G$, joten $N = 2G$
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $N = 2\cdot 0{,}30\,\text{N} = 0{,}60\,\text{N}$
**Vastaus:** $0{,}60\,\text{N}$, kaksi merkitsevää numeroa kuten painossa $0{,}30\,\text{N}$.
**Järkevyys:** Pöytä kantaa molempien magneettien painon, aivan kuin ylempi magneetti lepäisi alemman päällä. Leijuva magneetti ei ole painoton: sen paino siirtyy pöytään magneettisen voimaparin kautta.

## fy4-3-L3-03
**Annettu:** omenan paino $G_\text{o} = 1{,}5\,\text{N}$, alemman vaa'an paino $G_\text{v} = 0{,}40\,\text{N}$, kaikki on paikallaan
**Kysytty:** ylemmän vaa'an lukema eli voima $F$, jolla alempi vaaka vetää ylemmän koukkua, yksikössä $\text{N}$
**Periaate:** Omena on levossa, joten alemman vaa'an koukku vetää sitä ylös $1{,}5\,\text{N}$:n voimalla (ensimmäinen laki), ja kolmannen lain mukaan omena vetää koukkua alas yhtä suurella voimalla. Alempi vaaka on levossa, joten ylemmän vaa'an koukun on vedettävä sitä ylös omenan voiman ja vaa'an oman painon verran. Kolmannen lain mukaan alempi vaaka vetää ylempää alas yhtä suurella voimalla, ja sen ylempi vaaka näyttää.
**Voimakuvio:** Alempi vaaka suorakulmiona, positiivinen suunta ylös. Ylemmän vaa'an koukun voima $\overline{F}$ yläpinnasta ylös, paino $\overline{G}_\text{v}$ keskipisteestä alas ja omenan voima $\overline{F}_\text{o}$ alapinnasta alas.
```voimakuvio
F 1,9 ylös
G_v 0,40
F_o 1,5 alas
a 0
```
**Kaava:** $F - G_\text{v} - F_\text{o} = 0$ ja $F_\text{o} = G_\text{o}$, joten $F = G_\text{o} + G_\text{v}$
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F = 1{,}5\,\text{N} + 0{,}40\,\text{N} = 1{,}9\,\text{N}$
**Vastaus:** $1{,}9\,\text{N}$, kymmenesosanewtonin tarkkuudella kuten omenan paino $1{,}5\,\text{N}$, eli kaksi merkitsevää numeroa.
**Järkevyys:** Alempi vaaka näyttää omenan painon $1{,}5\,\text{N}$, ja ylempi kannattelee lisäksi alempaa vaakaa, joten sen lukeman on oltava suurempi. Lukemien erotus $0{,}40\,\text{N}$ on juuri alemman vaa'an paino.

## fy4-3-L1-06
**Kysytty:** mikä väite kiekkoon vaikuttavista voimista on oikein, kun kiekko liukuu tasaisella nopeudella eikä kitkaa tai ilmanvastusta ole.
**Periaate:** Newtonin ensimmäisen lain mukaan kappaleen nopeus pysyy samana silloin ja vain silloin, kun kokonaisvoima on nolla. Voimaa tarvitaan nopeuden muuttamiseen, ei sen ylläpitämiseen.
**Mallivastaus:** Kiekon nopeus ja suunta pysyvät samoina, joten kokonaisvoima on nolla. Pystysuunnassa paino ja jään tukivoima kumoavat toisensa, ja vaakasuunnassa ei vaikuta mikään voima, koska kitka ja ilmanvastus puuttuvat. Eteenpäin työntävää voimaa ei tarvita eikä sellaista ole: lyönnin voima loppui, kun maila irtosi kiekosta. Jos kokonaisvoima osoittaisi liikkeen suuntaan, kiekko kiihtyisi, ja jos taaksepäin, se hidastuisi.

## fy4-3-L1-07
**Kysytty:** mikä voima on pöydän kirjaan kohdistaman tukivoiman vastavoima.
**Periaate:** Newtonin kolmannen lain mukaan vuorovaikutuksessa kumpikin osapuoli vaikuttaa toiseen yhtä suurella ja vastakkaissuuntaisella voimalla. Vastavoima vaikuttaa siis eri kappaleeseen kuin alkuperäinen voima ja on samaa lajia.
**Mallivastaus:** Tukivoima on pöydän voima kirjaan, joten sen vastavoima on kirjan voima pöytään: kirja painaa pöytää alaspäin. Kirjan paino ei ole vastavoima, koska se vaikuttaa samaan kappaleeseen kuin tukivoima; ne ovat yhtä suuret, koska kirja on levossa (ensimmäinen laki). Maan vetovoima kirjaan on kirjan paino ja kuuluu Maan ja kirjan vuorovaikutukseen. Pöydän paino lattiaan kuuluu pöydän ja lattian vuorovaikutukseen.

## fy4-3-L1-08
**Annettu:** lapsen voima köyteen $F = 38\,\text{N}$, kelkka liikkuu tasaisella nopeudella, köyden paino jätetään huomiotta
**Kysytty:** köyden voima lapseen $F_\text{KL}$ yksikössä $\text{N}$
**Periaate:** Newtonin kolmannen lain mukaan lapsi ja köysi vuorovaikuttavat, joten köysi vetää lasta yhtä suurella mutta vastakkaissuuntaisella voimalla kuin lapsi köyttä. Laki pätee, vaikka kelkka liikkuu tasaisella nopeudella. Valitaan kappaleeksi lapsi. Köyden voima $\overline{F}_\text{KL}$ osoittaa lapsesta kelkkaa kohti eli lasta vastaan, ja lapsen oma voima köyteen vaikuttaa köyteen eikä kuulu lapsen kuvioon.
**Kaava:** $\overline{F}_\text{KL} = -\overline{F}_\text{LK}$, joten suuruuksina $F_\text{KL} = F_\text{LK}$
**Muunnokset:** Voima on newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{KL} = F_\text{LK} = 38\,\text{N}$
**Vastaus:** $38\,\text{N}$ kelkkaa kohti, kaksi merkitsevää numeroa kuten voimassa $38\,\text{N}$.
**Järkevyys:** Kelkan liike ei vaikuta voimien suuruuteen: sama $38\,\text{N}$ olisi, jos kelkka seisoisi. Tasainen nopeus kertoo vain, että köyden voima kelkkaan on yhtä suuri kuin kelkkaan kohdistuva vastus, $38\,\text{N}$.

## fy4-3-L2-05
**Annettu:** köysi on paikallaan; taulukosta anturin A suurin lukema $F_\text{A} = 4{,}8\,\text{N}$ hetkellä $t = 1{,}0\,\text{s}$, jolloin anturi B näyttää $4{,}8\,\text{N}$
**Kysytty:** seinän voima köyteen $F_\text{S}$ yksikössä $\text{N}$ hetkellä, jolloin $F_\text{A}$ on suurin
**Periaate:** Köysi on levossa, joten ensimmäisen lain mukaan siihen vaikuttavien voimien summa on nolla: seinän voima köyteen on yhtä suuri kuin oppilaan voima köyteen. Kolmannen lain mukaan köysi vetää anturia A ja seinää yhtä suurilla voimilla kuin ne köyttä, joten antureiden lukemat ovat yhtä suuret joka hetki.
**Kuvaajan lukeminen:** Taulukosta luetaan rivi, jolla $F_\text{A}$ on suurin: $t = 1{,}0\,\text{s}$, $F_\text{A} = 4{,}8\,\text{N}$. Samalla rivillä $F_\text{B} = 4{,}8\,\text{N}$. Muilla riveillä lukemat eroavat enintään $0{,}1\,\text{N}$, mikä on mittauksen satunnaisvaihtelua, ei fysikaalista eroa.
**Kaava:** $F_\text{S} - F_\text{A} = 0$, joten $F_\text{S} = F_\text{A}$
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $F_\text{S} = F_\text{A} = 4{,}8\,\text{N}$
**Vastaus:** $4{,}8\,\text{N}$, kaksi merkitsevää numeroa kuten taulukon lukemissa.
**Järkevyys:** Anturien lukemat eroavat kaikilla viidellä hetkellä enintään $0{,}1\,\text{N}$, kun lukemat vaihtelevat välillä $0{,}9\,\text{N}$–$4{,}8\,\text{N}$. Erot vaihtelevat suunnaltaan, joten ne ovat satunnaista mittausvaihtelua: kevyen köyden molemmat päät vetävät yhtä suurella voimalla joka hetki.

## fy4-3-L2-06
**Annettu:** taulukosta nopeudet $0{,}51$; $0{,}50$; $0{,}49$; $0{,}50$; $0{,}51$ ja $0{,}49\,\text{m/s}$, aika $\Delta t = 6{,}0\,\text{s}$
**Kysytty:** a) miksi eteenpäin työntävää voimaa ei tarvita; b) kärryn kulkema matka $s$ yksikössä $\text{m}$
**Periaate:** Newtonin ensimmäisen lain mukaan kappale liikkuu tasaisella nopeudella, kun kokonaisvoima on nolla, eikä voimaa tarvita ylläpitämään liikettä. Nopeus on kaikissa lukemissa lähes sama, joten liike on tasaista ja matka on nopeuden ja ajan tulo.
**Kuvaajan lukeminen:** Taulukosta nähdään, että nopeus pysyy välillä $0{,}49$–$0{,}51\,\text{m/s}$ eikä kasva tai pienene. Vaihtelu on mittauksen satunnaisvaihtelua. Nopeuden keskiarvo $v_\text{ka}$ kuvaa tasaista nopeutta.
**Kaava:** $v_\text{ka} = \dfrac{\Sigma v}{n}$ ja $s = v_\text{ka}\,\Delta t$
**Muunnokset:** Nopeus on yksikössä $\text{m/s}$ ja aika sekunteina, joten muunnoksia ei tarvita.
**Sijoitus:** Nopeuksien summa on $3{,}00\,\text{m/s}$ ja lukemia on $6$, joten $v_\text{ka} = \dfrac{3{,}00\,\text{m/s}}{6} = 0{,}500\,\text{m/s}$. Matka on
$s = 0{,}500\,\text{m/s}\cdot 6{,}0\,\text{s} = 3{,}0\,\text{m}$.
**Vastaus:** a) Nopeus ei muutu, joten kokonaisvoima on nolla: pieni ilmanvastus on hyvin pieni ja pystysuunnassa paino ja tukivoima kumoavat toisensa, joten eteenpäin työntävää voimaa ei tarvita. b) $3{,}0\,\text{m}$, kaksi merkitsevää numeroa kuten ajassa $6{,}0\,\text{s}$.
**Järkevyys:** Nopeus on noin $0{,}5\,\text{m/s}$, joten $6\,\text{s}$:ssa kuljetaan noin $3\,\text{m}$. Radan pituuden on siis oltava vähintään tämän verran.

## fy4-3-L2-07
**Kysytty:** mikä virhe oppilaan päättelyssä on.
**Periaate:** Newtonin kolmannen lain voima ja vastavoima ovat yhtä suuret ja vastakkaissuuntaiset, mutta ne vaikuttavat eri kappaleisiin. Kappaleen liikkeen ratkaisee vain siihen itseensä vaikuttavien voimien summa.
**Mallivastaus:** Oppilas ottaa huomioon kaksi voimaa, nyrkin voiman seinään ja seinän voiman nyrkkiin, mutta ne vaikuttavat eri kappaleisiin. Nyrkin voima seinään vaikuttaa seinään, joten se ei kumoa mitään nyrkkiin vaikuttavaa. Nyrkkiin vaikuttaa seinän voima, ja se on nyrkin liikettä vastaan, joten nyrkki hidastuu ja pysähtyy. Voimat ovat silti yhtä suuret, vaikka seinä ei liiku, ja ne syntyvät yhtä aikaa. Liikkeen ylläpitämiseen ei tarvita voimaa.

## fy4-3-L3-04
**Annettu:** kärryn vierimisvastus $F_\text{r} = 410\,\text{N}$, ilmanvastus kärryyn $F_\text{k} = 40\,\text{N}$, ilmanvastus hevoseen $F_\text{h} = 30\,\text{N}$, nopeus on vakio ja suoraan eteenpäin, esimerkkiaineisto
**Kysytty:** a) köyden voima kärryyn $T$; b) tien voima hevosen kavioihin $F_\text{t}$ yksikössä $\text{N}$; c) miksi voimat eivät kumoa toisiaan
**Periaate:** Sekä kärry että hevonen liikkuvat tasaisella nopeudella, joten kummankin kokonaisvoima on nolla (ensimmäinen laki). Kärrystä saadaan köyden voima. Kolmannen lain mukaan kärry vetää hevosta taaksepäin yhtä suurella voimalla $T$ kuin köysi kärryä eteenpäin, ja sitä käytetään hevosen tasapainossa. Tien voima kavioihin on ulkoinen voima, joka vie parin eteenpäin.
**Voimakuvio:** Piirrä kärrylle: köyden voima $\overline{T}$ eteenpäin, vierimisvastus ja ilmanvastus taaksepäin. Hevoselle: tien voima $\overline{F}_\text{t}$ eteenpäin, köyden voima $\overline{T}$ ja ilmanvastus taaksepäin. Hevosen ja kärryn voimat ovat eri kuvioissa.
```voimakuvio
pinta 0
T 450 oikea
F_r 410 vasen
F_k 40 vasen
a 0
```
```voimakuvio
pinta 0
F_t 480 oikea kitka
T 450 vasen
F_h 30 vasen
a 0
```
**Kaava:** Kärry: $T - F_\text{r} - F_\text{k} = 0$, joten $T = F_\text{r} + F_\text{k}$. Hevonen: $F_\text{t} - T - F_\text{h} = 0$, joten $F_\text{t} = T + F_\text{h}$.
**Muunnokset:** Voimat ovat newtoneina, joten muunnoksia ei tarvita.
**Sijoitus:** $T = 410\,\text{N} + 40\,\text{N} = 450\,\text{N}$ ja
$F_\text{t} = 450\,\text{N} + 30\,\text{N} = 480\,\text{N}$.
**Vastaus:** a) $450\,\text{N}$ ja b) $480\,\text{N}$ eteenpäin, kaksi merkitsevää numeroa kuten annetuissa voimissa. c) Hevosen voima kärryyn ja kärryn voima hevoseen ovat yhtä suuret ja vastakkaissuuntaiset, mutta ne vaikuttavat eri kappaleisiin, joten ne eivät kumoa toisiaan. Kärryn liikkeen ratkaisevat vain kärryyn vaikuttavat voimat, ja hevosen liikkeen vain hevoseen vaikuttavat. Hevonen pääsee liikkeelle, koska tie työntää sen kavioita eteenpäin voimalla, joka on suurempi kuin kärryn voima hevoseen.
**Järkevyys:** Tien voima $480\,\text{N}$ on yhtä suuri kuin kaikkien vastusten summa $410\,\text{N} + 40\,\text{N} + 30\,\text{N} = 480\,\text{N}$, joten koko järjestelmä liikkuu tasaisella nopeudella. Kitka tien ja kavioiden välillä osoittaa eteenpäin, koska se vastustaa kavion liukumista taaksepäin.

## fy4-3-L3-05
**Annettu:** taulukosta nopeus ja köyden voima; hetkillä $t = 4{,}0\,\text{s}$, $5{,}0\,\text{s}$ ja $6{,}0\,\text{s}$ nopeudet $0{,}70$; $0{,}71$ ja $0{,}70\,\text{m/s}$ sekä voimat $3{,}4$; $3{,}5$ ja $3{,}3\,\text{N}$; alussa $F = 5{,}1\,\text{N}$ ja $v = 0$ (esimerkkiaineisto)
**Kysytty:** a) milloin kokonaisvoima on nolla; b) kitkavoima $F_\text{k}$ yksikössä $\text{N}$; c) miksi alussa $F > F_\text{k}$
**Periaate:** Kun kärryn nopeus on vakio, ensimmäisen lain mukaan kokonaisvoima on nolla, joten köyden voima ja kitka ovat yhtä suuret. Jos nopeus muuttuu, kokonaisvoima ei ole nolla. Kolmannen lain mukaan kärry vetää köyttä ja oppilasta yhtä suurella voimalla kuin köysi kärryä.
**Kuvaajan lukeminen:** Nopeus kasvaa hetkestä $t = 0$ alkaen arvosta $0$ arvoon $0{,}69\,\text{m/s}$ ja pysyy sitten hetkistä $t = 4{,}0\,\text{s}$ alkaen lähes samana, noin $0{,}70\,\text{m/s}$. Kokonaisvoima on nolla hetkistä $t = 4{,}0\,\text{s}$ alkaen. Näiden kolmen hetken anturilukemat ovat $3{,}4\,\text{N}$, $3{,}5\,\text{N}$ ja $3{,}3\,\text{N}$.
**Kaava:** $F_\text{k} = F_\text{ka}$ ja $F_\text{ka} = \dfrac{\Sigma F}{n}$
**Muunnokset:** Voimat ovat newtoneina ja nopeus yksikössä $\text{m/s}$, joten muunnoksia ei tarvita.
**Sijoitus:** Voimien summa on $10{,}2\,\text{N}$ ja lukemia on $3$, joten
$F_\text{k} = \dfrac{10{,}2\,\text{N}}{3} = 3{,}40\,\text{N}$.
**Vastaus:** b) $3{,}4\,\text{N}$, kaksi merkitsevää numeroa kuten anturin lukemissa. a) Kokonaisvoima on nolla siitä alkaen, kun nopeus on vakio, eli neljännestä sekunnista. c) Alussa nopeus kasvaa, joten kokonaisvoima ei ole nolla: köysi vetää kärryä eteenpäin enemmän kuin kitka vastustaa, ja alussa köysi vetää kärryä $5{,}1\,\text{N}$:n voimalla. Kolmannen lain mukaan kärry vetää köyttä ja oppilasta samalla $5{,}1\,\text{N}$:n voimalla taaksepäin, vaikka kärry kiihtyy.
**Järkevyys:** Voima pienenee $5{,}1\,\text{N}$:sta kohti $3{,}4\,\text{N}$:a samalla, kun kiihtyminen loppuu. Kitka $3{,}4\,\text{N}$ on pienempi kuin alun voima, joten kärry on kiihtynyt, ja yhtä suuri kuin tasaisen vauhdin voima, joten nopeus ei enää muutu.
