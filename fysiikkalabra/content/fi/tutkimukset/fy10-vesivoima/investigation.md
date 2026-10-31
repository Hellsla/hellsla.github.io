# Vesivoimalaitoksen pienoismallin hyötysuhde

> **Tutkimuskysymys:** Kuinka suuri osa putoavan veden energiasta muuttuu pienoisvoimalaitoksessa sähköksi, ja miten hyötysuhde riippuu käyttötilanteesta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydän vieressä on korkea teline, jonka päällä on vesisäiliö. Säiliön pohjasta lähtee letku alas pienen vesiturbiinin luo. Turbiinin akselilla on generaattori, josta johdot kulkevat kuormavastukselle ja kahdelle yleismittarille, joiden näytöt ovat tyhjät. Turbiinin läpi kulkenut vesi valuu ämpäriin, joka on vaa&#x27;an päällä. Pöydällä on sekuntikello ja kuivausliina." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10vh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10vh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10vh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10vh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="130" y="150" width="16" height="320" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="274" y="150" width="16" height="320" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="120" y="140" width="180" height="16" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="146" y1="300" x2="274" y2="300" stroke="#8a96a3" stroke-width="4" stroke-linecap="butt"/>
  <rect x="140" y="40" width="140" height="100" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="143" y="62" width="134" height="75" rx="4" fill="#a9d1f0"/>
  <line x1="143" y1="62" x2="277" y2="62" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <path d="M262,140 C262,230 330,260 420,268 C470,272 500,268 510,262" fill="none" stroke="#1f2933" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M262,140 C262,230 330,260 420,268 C470,272 500,268 510,262" fill="none" stroke="#a9d1f0" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="668" y="352" width="48" height="118" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="560" cy="290" r="62" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <circle cx="560" cy="290" r="42" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="574" y1="294.5" x2="605" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="605" cy="304" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="567" y1="303" x2="582" y2="331.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="582" cy="331.5" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="555.5" y1="304" x2="546" y2="335" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="546" cy="335" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="547" y1="297" x2="518.5" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="518.5" cy="312" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="546" y1="285.5" x2="515" y2="276" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="515" cy="276" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="553" y1="277" x2="538" y2="248.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="538" cy="248.5" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="564.5" y1="276" x2="574" y2="245" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="574" cy="245" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="573" y1="283" x2="601.5" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="601.5" cy="268" r="5.46" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="560" cy="290" r="9.24" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="620" y="282" width="40" height="16" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="652" y="256" width="80" height="96" rx="10" fill="#4a6fa5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="662" y="270" width="60" height="10" rx="3" fill="#6f8fbf"/>
  <path d="M556,352 C556,370 558,388 560,404" fill="none" stroke="#2f74b5" stroke-width="8" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M500,392 L512,450 L608,450 L620,392 Z" fill="#e9ecef" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M505,416 L512,450 L608,450 L615,416 Z" fill="#a9d1f0" stroke-linejoin="round"/>
  <line x1="505" y1="416" x2="615" y2="416" stroke="#2f74b5" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="480" y="450" width="160" height="20" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="536" y="454" width="48" height="12" rx="2" fill="#e9f3e1" stroke="#1f2933" stroke-width="1.5"/>
  <path d="M730,280 C770,250 800,260 840,335" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round"/>
  <path d="M730,330 C770,370 800,400 840,375" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="820" y="330" width="110" height="50" rx="4" fill="#f1f3f5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="846" y="346" width="58" height="18" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="856" y="346" width="6" height="18" fill="#b8622d"/>
  <rect x="870" y="346" width="6" height="18" fill="#1f2933"/>
  <rect x="884" y="346" width="6" height="18" fill="#c92a2a"/>
  <rect x="960" y="300" width="96" height="130" rx="10" fill="#ffd43b" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="970" y="312" width="76" height="34" rx="3" fill="#e9f3e1" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1008" cy="378" r="18" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="1008" y1="378" x2="1018" y2="366" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="988" cy="416" r="6" fill="#1f2933"/>
  <circle cx="1028" cy="416" r="6" fill="#c92a2a"/>
  <rect x="1080" y="300" width="96" height="130" rx="10" fill="#ffd43b" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1090" y="312" width="76" height="34" rx="3" fill="#e9f3e1" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1128" cy="378" r="18" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <line x1="1128" y1="378" x2="1138" y2="366" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="1108" cy="416" r="6" fill="#1f2933"/>
  <circle cx="1148" cy="416" r="6" fill="#c92a2a"/>
  <path d="M930,345 C945,345 950,420 985,418" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round"/>
  <path d="M930,365 C960,365 1000,440 1028,418" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M904,330 C940,250 1080,250 1105,418" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round"/>
  <path d="M876,380 C900,460 1130,460 1148,418" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="794" y="472.5" width="11.5" height="8.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="797.5" y="480.5" width="5" height="5" fill="#6c757d"/>
  <circle cx="800" cy="520" r="36" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="800" cy="520" r="29.52" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="800" y1="495.5" x2="800" y2="492" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="812" y1="499" x2="814" y2="495.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="821" y1="508" x2="824.5" y2="506" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="824.5" y1="520" x2="828" y2="520" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="821" y1="532" x2="824.5" y2="534" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="812" y1="541" x2="814" y2="544.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="544.5" x2="800" y2="548" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="788" y1="541" x2="786" y2="544.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="779" y1="532" x2="775.5" y2="534" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="775.5" y1="520" x2="772" y2="520" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="779" y1="508" x2="775.5" y2="506" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="788" y1="499" x2="786" y2="495.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="800" y1="520" x2="800" y2="496" stroke="#c92a2a" stroke-width="2.52" stroke-linecap="round"/>
  <circle cx="800" cy="520" r="2.88" fill="#1f2933"/>
  <g transform="translate(980,530) rotate(-4)"><rect x="-90" y="-24" width="180" height="48" rx="8" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/><line x1="-70" y1="-24" x2="-70" y2="24" stroke="#ffffff" stroke-width="4"/><line x1="-35" y1="-24" x2="-35" y2="24" stroke="#ffffff" stroke-width="4"/><line x1="0" y1="-24" x2="0" y2="24" stroke="#ffffff" stroke-width="4"/><line x1="35" y1="-24" x2="35" y2="24" stroke="#ffffff" stroke-width="4"/><line x1="70" y1="-24" x2="70" y2="24" stroke="#ffffff" stroke-width="4"/></g>
</svg>

Suomessa vesivoimalaitokset muuttavat putoavan veden energiaa sähköksi. Pienoismallissa periaate on sama: vesi putoaa, pyörittää turbiinia, ja turbiinin akselilla oleva generaattori tuottaa sähköä. Tässä tutkimuksessa selvität mittaamalla, kuinka suuri osa veden energiasta päätyy pienoismallissa sähköksi ja muuttuuko osuus, kun voimalaitosta käytetään eri tavoin. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mikä on pienoisvoimalaitoksen hyötysuhde epävarmuuksineen ja miten se muuttuu, kun veden virtaamaa tai putouskorkeutta muutetaan. Selvitä myös, mitä energiaa tai tehoa järjestelmään syötetään, mitä siitä saadaan hyödyksi ja mitä suureita näiden määrittämiseksi on mitattava.

**Päätät itse:** mitä järjestelmään luet kuuluvaksi ja mistä mihin putouskorkeus mitataan, muutatko virtaamaa vai putouskorkeutta ja millä arvoilla, miten mittaat veden määrän ja ajan, mittauspisteiden ja toistojen määrän, kuvaajan, jolla esität tulokset, sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

Opettajan pienoismalli voi poiketa tämän sivun kuvista: sovella suunnitelmasi siihen laitteeseen, joka teillä on käytössä.

::: tuki I
**Itsenäinen työtapa.** Laajennus, kuorman vaikutus sähkötehoon ja hyötysuhteeseen, kuuluu työhösi, jos pienoismallin kuormaa voi vaihtaa.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kuinka suuri osa veden energiasta arvelet päätyvän pienoismallissa sähköksi: lähes kaikki, noin puolet vai pieni osa? Miksi?
2. Mihin se osa veden energiasta joutuu, joka ei muutu sähköksi? Luettele ainakin kolme kohdetta.
3. Jos veden teho kaksinkertaistuu, kaksinkertaistuuko myös sähköteho? Pysyykö hyötysuhde samana?
4. Minkä suureen mittaaminen on todennäköisesti vaikeinta, ja miten voisit helpottaa sitä?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Energiaa tai tehoa ei voi lukea suoraan mistään mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitä energiaa järjestelmään syötetään, ja mistä suureista sen teho saadaan?
2. Mitä energiaa järjestelmästä saadaan hyödyksi, ja mistä suureista sen teho saadaan?
3. Missä järjestelmä alkaa ja mihin se päättyy? Esimerkiksi: kuuluuko veden putoaminen turbiinin alapuolella keräysastiaan järjestelmään?

## Teoriaa lyhyesti

**Hyötysuhde** $\eta$ on laitteen antaman hyötytehon ja laitteeseen otetun tehon suhde [[apua:fy2-4|Hyötysuhde]]:

```latex
\eta = \frac{P_\text{s}}{P_\text{o}}
```

missä $P_\text{s}$ on tässä työssä generaattorin kuormalle antama sähköteho ja $P_\text{o}$ veden voimalaitokselle tuoma teho. Energia säilyy, joten hyötysuhde on enintään $100\,\%$.

**Teho** on energian muutos jaettuna ajalla, jossa muutos tapahtuu: $P = \dfrac{\Delta E}{\Delta t}$ [[apua:fy2-3|Teho]]. Kun vesi laskeutuu korkeuden $h$ verran, sen **potentiaalienergia** pienenee määrällä $mgh$ [[apua:fy4-7|Potentiaalienergia]]. Oikea vesivoimala käyttää juuri tätä energiaa [[apua:fy4-15|Vesi- ja tuulivoima]].

**Sähköteho.** Kun generaattori syöttää sähkövirtaa kuormaan, esimerkiksi vastukseen, kuorman saama sähköteho on

```latex
P_\text{s} = UI
```

missä $U$ on kuorman napojen välinen jännite (yksikkö voltti, $\text{V}$) ja $I$ kuorman läpi kulkeva sähkövirta (yksikkö ampeeri, $\text{A}$). Teho saadaan watteina, koska $1\ \text{V} \cdot 1\ \text{A} = 1\ \text{W}$. Jännite mitataan jännitemittarilla, joka kytketään kuorman rinnalle, ja sähkövirta virtamittarilla, joka kytketään sarjaan kuorman kanssa, niin että sama virta kulkee molempien läpi. Sähkötehoa käsitellään tarkemmin moduulissa FY6.

Kysy opettajalta, antaako pienoismallin generaattori tasa- vai vaihtojännitettä, ja aseta molemmat mittarit sen mukaan. Vaihtojännitteellä $P_\text{s} = UI$ lasketaan mittarien näyttämistä tehollisarvoista, ja se pätee, kun kuormana on vastus.

::: tuki OO
Tarkista kirjauksesi tästä. Rajataan järjestelmäksi vesi, turbiini ja generaattori siitä, kun vesi lähtee ylemmän astian vedenpinnalta, siihen, kun se on kulkenut turbiinin läpi. **Putouskorkeus** $h$ mitataan ylemmän astian vedenpinnasta turbiinin tasolle, esimerkiksi turbiinin akselin tasolle, sama kohta jokaisessa mittauksessa. Turbiinin alapuolinen putoaminen keräysastiaan ei pyöritä turbiinia, joten se jää järjestelmän ulkopuolelle.

<svg data-fig="setup" viewBox="0 0 600 470" role="img" aria-label="Kaaviokuva. Vasemmalla ylhäällä on vesiastia. Sen pohjasta letku vie veden alas turbiinille. Putouskorkeus h on merkitty astian vedenpinnasta turbiinin akselin tasolle. Turbiinin läpi kulkenut vesi valuu keräysastiaan, joka on vaa&#x27;an päällä. Turbiinin akselilla on generaattori G. Generaattorin virtapiirissä on kuormavastus R, sen kanssa sarjassa virtamittari A ja sen rinnalla jännitemittari V." style="max-width:100%;font-size:24px">
  <rect x="80" y="40" width="130" height="90" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="82" y="70" width="126" height="58" rx="3" fill="#a9d1f0"/>
  <line x1="82" y1="70" x2="208" y2="70" stroke="#2f74b5" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M190,130 L190,236 Q190,262 216,264" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round"/>
  <path d="M190,130 L190,236 Q190,262 216,264" fill="none" stroke="#a9d1f0" stroke-width="6" stroke-linejoin="round"/>
  <circle cx="255" cy="300" r="36" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="267.5" y1="302.5" x2="294.5" y2="308" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="294.5" cy="308" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="262" y1="310.5" x2="277.5" y2="333.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="277.5" cy="333.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="252.5" y1="312.5" x2="247" y2="339.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="247" cy="339.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="244.5" y1="307" x2="221.5" y2="322.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="221.5" cy="322.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="242.5" y1="297.5" x2="215.5" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="215.5" cy="292" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="248" y1="289.5" x2="232.5" y2="266.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="232.5" cy="266.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="257.5" y1="287.5" x2="263" y2="260.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="263" cy="260.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="265.5" y1="293" x2="288.5" y2="277.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="288.5" cy="277.5" r="4.68" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <circle cx="255" cy="300" r="7.92" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="90" y="337.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{turbiini}$</div></foreignObject>
  <path d="M255,346 L255,382" fill="none" stroke="#2f74b5" stroke-width="5" stroke-linejoin="round"/>
  <path d="M205,372 L215,430 L295,430 L305,372" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M210,400 L215,430 L295,430 L300,400 Z" fill="#a9d1f0" stroke-linejoin="round"/>
  <rect x="195" y="430" width="120" height="16" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="322" y="423.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{vaaka}$</div></foreignObject>
  <line x1="30" y1="70" x2="78" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="30" y1="300" x2="214" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="48" y1="185" x2="48" y2="85" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M48,74 L53.5,86 L42.5,86 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="48" y1="185" x2="48" y2="285" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M48,296 L42.5,284 L53.5,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="58" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <rect x="291" y="295" width="54" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="372" y1="160" x2="372" y2="274" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="326" x2="372" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="160" x2="500" y2="160" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="400" x2="500" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="500" y1="160" x2="500" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="500" y1="320" x2="500" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="488" y="240" width="24" height="80" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="462" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R$</div></foreignObject>
  <line x1="500" y1="210" x2="566" y2="210" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="500" y1="350" x2="566" y2="350" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="566" y1="210" x2="566" y2="258" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="566" y1="302" x2="566" y2="350" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="500" cy="210" r="4.5" fill="#1f2933"/>
  <circle cx="500" cy="350" r="4.5" fill="#1f2933"/>
  <circle cx="372" cy="300" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="362" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$G$</div></foreignObject>
  <circle cx="436" cy="160" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="426" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <circle cx="566" cy="280" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="556" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V$</div></foreignObject>
</svg>

Kun ajassa $\Delta t$ turbiinin läpi virtaa veden massa $\Delta m$, veden potentiaalienergia pienenee määrällä $\Delta m \cdot g h$. Veden voimalaitokselle tuoma teho on siis

```latex
P_\text{o} = \frac{\Delta m}{\Delta t} \cdot g h
```

missä $\dfrac{\Delta m}{\Delta t}$ on massavirta eli sekunnissa turbiinin läpi kulkeva veden massa ($\text{kg/s}$), $g$ putoamiskiihtyvyys ja $h$ putouskorkeus. Malli edellyttää, että

- vesi on ylemmän astian pinnalla lähes levossa ja virtaa alas pelkän painovoiman vaikutuksesta. Jos pienoismalliin tulee vettä vesijohdosta tai pumpulta, putouskorkeus ei yksin kerro veden energiaa: kysy opettajalta, miten järjestely tehdään.
- putouskorkeus pysyy mittauksen ajan lähes samana. Jos ylemmän astian pinta laskee mittauksen aikana selvästi, käytä pinnan korkeuden keskiarvoa ja ota pinnan lasku huomioon epävarmuudessa.

Turbiinista lähtevällä vedellä on vielä liike-energiaa. Se ei muutu sähköksi, joten tässä rajauksessa se on yksi häviöistä.

Hyötysuhde on tällöin

```latex
\eta = \frac{P_\text{s}}{P_\text{o}} = \frac{UI}{\dfrac{\Delta m}{\Delta t} \cdot g h}
```
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Kirjaa järjestelmän rajaus perusteluineen.

::: tuki OO
**Osittain ohjattu.** Valitse, muutatko virtaamaa, esimerkiksi letkun hanalla tai suuttimen koolla, vai putouskorkeutta, eli ylemmän astian korkeutta. Pidä toinen niistä ja kuorma vakiona. Tee mittaus ainakin viidellä eri arvolla. Jokaisessa mittauksessa mittaat veden massan $\Delta m$, joka kulkee turbiinin läpi ajassa $\Delta t$, putouskorkeuden $h$ sekä kuorman jännitteen $U$ ja sähkövirran $I$ samana aikana. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Miten mittaat massan $\Delta m$? Punnitsetko keräysastian ennen ja jälkeen vai mittaatko veden tilavuuden ja käytät veden tiheyttä? Jos osa turbiinin läpi kulkeneesta vedestä roiskuu keräysastian ohi, $\Delta m$ jää liian pieneksi ja hyötysuhde liian suureksi.
- Kuinka pitkä keräysaika $\Delta t$ tarvitaan, jotta ajanoton aloitus ja lopetus eivät vaikuta paljon tulokseen?
- Pysyykö ylemmän astian vedenpinta paikallaan, vai pitääkö sitä täyttää mittauksen aikana tai seurata pinnan laskua?
- Heilahtelevatko jännite ja virta? Miten luet niistä edustavan arvon samalta ajalta kuin veden keräys?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös, kuinka tarkasti luit kunkin suureen, ja huolehdi, että jokainen mittaus tehdään mahdollisimman samalla tavalla. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

::: tuki OO
Voit käyttää esimerkiksi tällaista taulukkoa:

| $h\ (\text{m})$ | $\Delta m\ (\text{kg})$ | $\Delta t\ (\text{s})$ | $U\ (\text{V})$ | $I\ (\text{A})$ | $P_\text{o}\ (\text{W})$ | $P_\text{s}\ (\text{W})$ | $\eta$ |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Jos punnitset keräysastian ennen ja jälkeen, kirjaa molemmat lukemat omiin sarakkeisiinsa ja laske $\Delta m$ niiden erotuksena. Aloita veden keräys vasta, kun turbiinin pyörimisnopeus ja mittarien lukemat ovat asettuneet. Toista ainakin yksi mittaus, niin näet, kuinka hyvin tulos toistuu.
:::

## Käsittele tulokset

Laske jokaisesta mittauksesta veden teho, sähköteho ja hyötysuhde. Esitä tulokset kuvaajana, josta näkyy, miten hyötysuhde tai sähköteho muuttuu käyttötilanteen mukana. Merkitse akseleille suureet ja yksiköt. [[apua:fy1-4|Graafinen esitys]]

Vastaa:

1. Onko hyötysuhde sama kaikissa mittauksissa? Jos ei, millä tavalla se muuttuu?
2. Onko sähköteho suoraan verrannollinen veden tehoon?
3. Millä käyttötavalla pienoismalli toimii parhaiten, ja mistä arvelet sen johtuvan?

::: tuki OO
**Kuvaajan valinta.** Kaksi luontevaa kuvaajaa ovat hyötysuhde $\eta$ muutetun suureen funktiona sekä sähköteho $P_\text{s}$ veden tehon $P_\text{o}$ funktiona. Jälkimmäisessä kuvaajassa hyötysuhde on origosta mittauspisteeseen piirretyn suoran kulmakerroin. Jos kaikki pisteet ovat samalla origon kautta kulkevalla suoralla, hyötysuhde on sama kaikissa mittauksissa. Jos pisteet eivät ole sellaisella suoralla, hyötysuhde muuttuu. Mieti, mitä kuvaajan muoto kertoo häviöistä.

<svg data-fig="eta" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja: vaaka-akselilla veden teho P o ja pystyakselilla sähköteho P s, samassa mittakaavassa. Katkoviiva origosta on suora, jolla hyötysuhde on yksi eli sata prosenttia; sen yläpuolelle ei voi päätyä, koska energia säilyy. Toinen origon kautta kulkeva suora näyttää, että kaikilla saman origon kautta kulkevan suoran pisteillä on sama hyötysuhde. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="149" y1="330" x2="424" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M436,330 L423,336 L423,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="150" y1="331" x2="150" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M150,44 L156,57 L144,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="120" y="335.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="442" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o}$</div></foreignObject>
  <foreignObject x="140" y="13.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{s}$</div></foreignObject>
  <polygon points="150,330 410,70 150,70" fill="#c9c2b2" fill-opacity="0.35"/>
  <polyline points="150,330 410,70" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="165.5" y="92" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{mahdoton alue}$</div></foreignObject>
  <foreignObject x="332" y="162" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\eta = 1$</div></foreignObject>
  <polyline points="150,330 410,200" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="418" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sama } \eta$</div></foreignObject>
</svg>
:::

Tee laskut ja kuvaajat Graphical Analysis Pro -ohjelmalla. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita hyötysuhde epävarmuuksineen ainakin yhdessä käyttötilanteessa ja perustele, miten arvioit epävarmuuden. Pohdi myös, mitkä mitatuista suureista vaikuttavat tulokseen eniten.

::: tuki OO
Hyötysuhde lasketaan viiden mitatun suureen tuloista ja osamääristä. Silloin tuloksen suhteellinen epävarmuus on likimain mitattujen suureiden suhteellisten epävarmuuksien summa:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} \approx {} & \frac{\Delta U}{U} + \frac{\Delta I}{I} \\
& + \frac{\Delta (\Delta m)}{\Delta m} + \frac{\Delta (\Delta t)}{\Delta t} \\
& + \frac{\Delta h}{h}
\end{aligned}
```

Jos $\Delta m$ on kahden punnituksen erotus, sen epävarmuus on punnitusten epävarmuuksien summa. Jos jännite ja virta heilahtelevat, käytä epävarmuutena heilahtelun puolikasta. Jos vedenpinta laskee mittauksen aikana, käytä putouskorkeutena keskiarvoa ja epävarmuutena puolta pinnan laskusta. Laske jokaisen termin osuus erikseen: suurin termi kertoo, mitä mittausta kannattaa parantaa ensimmäisenä.

Pyöristä $\Delta \eta$ yhteen merkitsevään numeroon ja $\eta$ samaan tarkkuuteen.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet hyötysuhdetta? Muuttaisiko toisenlainen järjestelmän rajaus tulosta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Kuinka suuri on pienoismallin hyötysuhde, ja miten se riippuu käyttötilanteesta? Mitkä ovat tärkeimmät energiahäviöt, ja mihin energia niissä muuttuu? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

Halutessasi arvioi yhden häviön suuruus, esimerkiksi turbiinista lähtevän veden liike-energia sekunnissa: mitä sinun pitäisi mitata, ja kuinka suuren osan veden tehosta se vie?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja tausta:** mitä energiaa järjestelmään syötetään, mitä siitä saadaan hyödyksi ja miten tehot lasketaan mitatuista suureista.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, järjestelmän rajaus, mistä mihin putouskorkeus mitattiin, miten virtapiiri kytkettiin ja miten työturvallisuus huomioitiin.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan ja lasketut tehot ja hyötysuhde niiden oikealla puolella.
- **Tulos:** hyötysuhde epävarmuuksineen oikein pyöristettynä ja kuvaaja sen riippuvuudesta käyttötilanteesta.
- **Luotettavuus:** suurimmat epävarmuuden lähteet ja tärkeimmät energiahäviöt.

## Laajennus: kuorman vaikutus

Generaattorin antama sähköteho ei riipu pelkästään vedestä vaan myös siitä, mihin generaattori on kytketty. Mitä suurempi virta generaattorin läpi kulkee, sitä enemmän generaattori jarruttaa turbiinia.

Pidä veden virtaama ja putouskorkeus vakiona ja vaihda kuormaa, esimerkiksi eri suuruisiin vastuksiin. Ennen kuin mittaat, pohdi lausekkeen $P_\text{s} = UI$ avulla: mitä sähköteholle tapahtuu, jos kuorman resistanssi on hyvin suuri, jolloin virta on lähes nolla? Entä jos kuorma on lähes oikosulku, jolloin jännite on lähes nolla? Mittaa sitten sähköteho usealla kuormalla, esitä tulos kuvaajana ja päättele, millä kuormalla pienoismalli antaa suurimman sähkötehon ja suurimman hyötysuhteen. Vertaa tulosta päämittauksen tulokseen: kumpi vaikuttaa hyötysuhteeseen enemmän, päämittauksessa muuttamasi suure vai kuorma?

::: tuki OO
**Vihjeitä.** Kirjaa jokaisesta kuormasta, mikä se oli, esimerkiksi vastuksen resistanssi. Aloita suurimmasta resistanssista: kun resistanssi pienenee, virta kasvaa, joten tarkista ennen jokaista mittausta, että virtamittarin mittausalue riittää. Laske hyötysuhde jokaisella kuormalla samalla tavalla kuin päämittauksessa. Pohdi myös: miksi kuorma, jolla sähköteho on suurin, antaa myös suurimman hyötysuhteen, kun veden teho pysyy vakiona?
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
