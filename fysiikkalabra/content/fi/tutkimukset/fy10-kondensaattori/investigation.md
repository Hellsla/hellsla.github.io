# Kondensaattorin kapasitanssin määrittäminen

> **Tutkimuskysymys:** Miten kondensaattorin jännite muuttuu, kun kondensaattori purkautuu tai varautuu vastuksen kautta, ja kuinka suuri on kondensaattorin kapasitanssi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on tasajännitelähde, jonka navoista johtimet kulkevat kytkentäalustalle. Alustalla on sininen sylinterin muotoinen elektrolyyttikondensaattori, jonka kyljessä on vaalea raita, sekä vastus ja vaihtokytkin. Jänniteanturin johdot ulottuvat kondensaattorin luo, ja anturi on kytketty kannettavaan tietokoneeseen, jonka näytöllä on tyhjä kuvaajaruudukko." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10kh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10kh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10kh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10kh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="60" y="300" width="250" height="170" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="85" y="325" width="130" height="56" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="262" cy="352" r="24" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="262" y1="352" x2="262" y2="332" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="110" cy="430" r="15" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="170" cy="430" r="15" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="400" y="420" width="400" height="50" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="416" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="426.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="437" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="447.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="458" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="468.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="479" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="489.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="500" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="510.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="521" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="531.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="542" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="552.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="563" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="573.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="584" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="594.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="605" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="615.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="626" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="636.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="647" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="657.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="668" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="678.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="689" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="699.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="710" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="720.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="731" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="741.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="752" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="762.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="773" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="783.5" cy="432" r="1.8" fill="#e3dccb"/>
  <circle cx="416" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="426.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="437" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="447.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="458" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="468.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="479" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="489.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="500" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="510.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="521" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="531.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="542" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="552.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="563" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="573.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="584" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="594.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="605" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="615.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="626" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="636.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="647" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="657.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="668" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="678.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="689" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="699.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="710" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="720.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="731" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="741.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="752" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="762.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="773" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="783.5" cy="444" r="1.8" fill="#e3dccb"/>
  <circle cx="416" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="426.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="437" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="447.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="458" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="468.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="479" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="489.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="500" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="510.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="521" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="531.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="542" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="552.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="563" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="573.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="584" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="594.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="605" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="615.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="626" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="636.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="647" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="657.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="668" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="678.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="689" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="699.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="710" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="720.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="731" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="741.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="752" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="762.5" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="773" cy="456" r="1.8" fill="#e3dccb"/>
  <circle cx="783.5" cy="456" r="1.8" fill="#e3dccb"/>
  <path d="M110,430 Q270,455 430,424" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round"/>
  <path d="M170,430 Q310,457 450,448" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <line x1="560" y1="420" x2="560" y2="404" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="590" y1="420" x2="590" y2="404" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <rect x="540" y="270" width="70" height="136" rx="8" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="586" y="272" width="16" height="132" fill="#d0e6fb"/>
  <line x1="590" y1="290" x2="598" y2="290" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="590" y1="314" x2="598" y2="314" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="590" y1="338" x2="598" y2="338" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="590" y1="362" x2="598" y2="362" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="590" y1="386" x2="598" y2="386" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <ellipse cx="575" cy="276" rx="33" ry="7" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M650,426 L650,392 L662,392" fill="none" stroke="#8a96a3" stroke-width="3" stroke-linejoin="round"/>
  <path d="M770,426 L770,392 L758,392" fill="none" stroke="#8a96a3" stroke-width="3" stroke-linejoin="round"/>
  <rect x="662" y="380" width="96" height="24" rx="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="678" y="382" width="7" height="20" fill="#b8622d"/>
  <rect x="693" y="382" width="7" height="20" fill="#1f2933"/>
  <rect x="708" y="382" width="7" height="20" fill="#c92a2a"/>
  <rect x="731" y="382" width="7" height="20" fill="#e9c98a"/>
  <rect x="460" y="380" width="54" height="40" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="487" y1="380" x2="474" y2="350" stroke="#1f2933" stroke-width="6" stroke-linecap="round"/>
  <rect x="850" y="400" width="110" height="60" rx="8" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="866" y="414" width="78" height="10" rx="3" fill="#ffffff"/>
  <path d="M860,440 Q713,469 566,418" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round"/>
  <path d="M870,450 Q733,490 596,420" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M930,470 L1170,470 L1150,452 L950,452 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="960" y="290" width="180" height="162" rx="6" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="970" y="300" width="160" height="140" fill="#ffffff"/>
  <line x1="970" y1="320" x2="1130" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="970" y1="340" x2="1130" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="970" y1="360" x2="1130" y2="360" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="970" y1="380" x2="1130" y2="380" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="970" y1="400" x2="1130" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="970" y1="420" x2="1130" y2="420" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="990" y1="300" x2="990" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1010" y1="300" x2="1010" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1030" y1="300" x2="1030" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1050" y1="300" x2="1050" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1070" y1="300" x2="1070" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1090" y1="300" x2="1090" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="1110" y1="300" x2="1110" y2="440" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="984" y1="430" x2="1124" y2="430" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="984" y1="430" x2="984" y2="310" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M960,440 Q945,457.5 930,455" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
</svg>

Kameran salama, sydäniskuri ja monen laitteen virtapiiri tarvitsevat kondensaattoria: se varastoi sähkövarausta ja luovuttaa sen sopivalla hetkellä. Kondensaattorin kylkeen on painettu sen kapasitanssi, mutta kuinka hyvin merkintä pitää paikkansa? Tässä tutkimuksessa mittaat, miten kondensaattorin jännite muuttuu sen purkautuessa tai varautuessa vastuksen kautta, etsit mittaustuloksiin sopivan mallin ja määrität sen avulla kapasitanssin. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten kondensaattorin jännite muuttuu ajan funktiona, kun kondensaattori purkautuu tai varautuu vastuksen kautta, millainen matemaattinen malli kuvaa muutosta, kuinka suuret ovat piirin aikavakio ja kondensaattorin kapasitanssi epävarmuuksineen, ja miten vastuksen resistanssi vaikuttaa purkautumiseen tai varautumiseen. Tee mittaus vähintään kahdella eri resistanssilla ja vertaa saamaasi kapasitanssia kondensaattoriin merkittyyn arvoon.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** tutkitko purkautumista vai varautumista, kytkennän, vastusten resistanssit, mittausvälineen ja sen, kuinka usein ja kuinka kauan jännite mitataan, toistojen määrän, tavan, jolla sovitat mallin mittaustuloksiin, sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää useimmat näistä valinnoista; mittausvälineen ja epävarmuuden arviointitavan valitset sivun antamista vaihtoehdoista. Osittain ohjatussa työtavassa sivu antaa esimerkkikytkennän, kysymyksiä ja vaihtoehtoja, joista valitset, ja itsenäisessä työtavassa suunnittelet ja perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, kapasitanssi aikavakion ja resistanssin kuvaajasta, kuuluu työhösi.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kun varattu kondensaattori purkautuu vastuksen kautta, pieneneekö sen jännite tasaisesti vai jollakin muulla tavalla? Piirrä ennustekuvaaja jännitteestä ajan funktiona.
2. Oletetaan, että jännitteen puolittumiseen kuluu tietty aika. Kuluuko puolikkaasta neljäsosaan sama aika, lyhyempi vai pidempi aika?
3. Miten purkautuminen muuttuu, jos vastuksen resistanssi kaksinkertaistetaan?
4. Mitkä tekijät voisivat saada mittaamasi kapasitanssin poikkeamaan kondensaattoriin merkitystä arvosta?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

Sähköopin kurssin FY6 luvut eivät ole vielä tällä sivustolla, joten tässä on se, mitä tarvitset.

**Kondensaattori** koostuu kahdesta johteesta, joiden välissä on eriste. Kun kondensaattori varataan, toiseen johteeseen kertyy varaus $+Q$ ja toiseen $-Q$, ja johteiden välille syntyy jännite $u$. Varaus on suoraan verrannollinen jännitteeseen:

```latex
Q = Cu
```

missä $C$ on kondensaattorin **kapasitanssi**. Sen yksikkö on faradi, $1\ \text{F} = 1\ \tfrac{\text{C}}{\text{V}}$. Koulun kondensaattoreiden kapasitanssit ilmoitetaan yleensä mikrofaradeina, $1\ \mu\text{F} = 10^{-6}\ \text{F}$. **Elektrolyyttikondensaattorilla** on suuri kapasitanssi pieneen kokoon nähden, mutta sillä on napaisuus: sen plusnapa on kytkettävä korkeampaan potentiaaliin kuin miinusnapa. Kondensaattorin kylkeen on merkitty kapasitanssi, suurin sallittu jännite ja yleensä miinusnavan puoli.

**Vastuksen** läpi kulkeva sähkövirta noudattaa Ohmin lakia $I = \dfrac{u}{R}$, missä $u$ on vastuksen yli oleva jännite ja $R$ sen resistanssi.

**Purkautuminen.** Kun varatun kondensaattorin navat yhdistetään vastuksen kautta, kondensaattorin jännite on myös vastuksen yli, ja vastuksen läpi kulkee virta $I = \dfrac{u}{R}$. Lyhyessä ajassa $\Delta t$ virta siirtää varauksen $\Delta Q = I \cdot \Delta t$, joten kondensaattorin varaus ja samalla jännite pienenevät. Koska $u = \dfrac{Q}{C}$, jännitteen muutos on

```latex
\Delta u = -\frac{\Delta Q}{C} = -\frac{u}{RC}\cdot\Delta t
```

Tulo $RC$ on piirin **aikavakio** $\tau = RC$. Sen yksikkö on sekunti, koska $\Omega \cdot \text{F} = \tfrac{\text{V}}{\text{A}} \cdot \tfrac{\text{C}}{\text{V}} = \tfrac{\text{C}}{\text{A}} = \text{s}$. Jännitteen muutosnopeus on siis jännite jaettuna aikavakiolla:

```latex
\frac{\Delta u}{\Delta t} = -\frac{u}{\tau}
```

Muutosnopeus riippuu siitä, kuinka suuri jännite kondensaattorissa sillä hetkellä on. Varautumisessa kondensaattori kytketään vastuksen kautta jännitelähteeseen, jonka jännite on $U_0$. Silloin vastuksen yli on jännite $U_0 - u$, ja samalla päättelyllä kondensaattorin jännitteen kasvunopeus on $\dfrac{U_0 - u}{\tau}$.

Päättely olettaa, että purkaus- tai varausvirta kulkee kokonaan vastuksen $R$ kautta: jännitemittarin läpi ei kulje merkittävää virtaa, kondensaattori ei vuoda varausta eristeensä läpi eikä johtimien ja lähteen resistanssi ole merkittävä vastuksen resistanssiin verrattuna.

Mittaustuloksistasi etsit funktion, joka kuvaa kondensaattorin jännitettä ajan funktiona. Kun malli on löytynyt, perustele, mikä sen parametri vastaa aikavakiota $\tau$. Kapasitanssi saadaan aikavakiosta ja resistanssista: $C = \dfrac{\tau}{R}$.

::: tuki O
**Malli.** Edellä johdetun muutosnopeuden toteuttaa eksponenttifunktio. Purkautuvan kondensaattorin jännite on

```latex
u = U_0\,\mathrm{e}^{-t/\tau}
```

missä $U_0$ on jännite hetkellä $t = 0$ ja $\mathrm{e} \approx 2{,}718$ on Neperin luku. Jokaisen aikavakion $\tau$ pituisen ajan kuluessa jännite pienenee samaan osuuteen, $\mathrm{e}^{-1} \approx 0{,}37$, siitä mitä se oli jakson alussa. Alkuhetken tangentti leikkaa aika-akselin kohdassa $t = \tau$. Varautuvan kondensaattorin jännite on $u = U_0\left(1 - \mathrm{e}^{-t/\tau}\right)$, eli erotus $U_0 - u$ pienenee samalla tavalla kuin purkautuvan kondensaattorin jännite.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: kondensaattorin jännite u ajan t funktiona purkautumisen mallin mukaan. Jännite alkaa arvosta U nolla ja pienenee ensin nopeasti, sitten yhä hitaammin kohti nollaa. Alkuhetken tangentti leikkaa aika-akselin kohdassa tau. Hetkellä tau jännite on noin 0,37 kertaa U nolla. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="166" y1="290" x2="166" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="156" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\tau$</div></foreignObject>
  <line x1="83" y1="81.5" x2="90" y2="81.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="67" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_0$</div></foreignObject>
  <foreignObject x="60" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$u$</div></foreignObject>
  <polyline points="90,81.5 93,90 96.5,98 99.5,106 102.5,113.5 106,120.5 109,127.5 112,134 115.5,140.5 118.5,146.5 121.5,152.5 125,158 128,163.5 131,168.5 134.5,173.5 137.5,178.5 140.5,183 144,187 147,191.5 150,195.5 153.5,199.5 156.5,203 159.5,206.5 163,210 166,213 169,216.5 172.5,219.5 175.5,222 178.5,225 182,227.5 185,230 188,232.5 191.5,235 194.5,237 197.5,239.5 201,241.5 204,243.5 207,245.5 210.5,247 213.5,249 216.5,250.5 220,252 223,253.5 226,255 229.5,256.5 232.5,258 235.5,259.5 239,260.5 242,262 245,263 248.5,264 251.5,265 254.5,266 258,267 261,268 264,269 267.5,270 270.5,270.5 273.5,271.5 277,272 280,273 283,273.5 286.5,274 289.5,275 292.5,275.5 296,276 299,276.5 302,277 305.5,277.5 308.5,278 311.5,278.5 315,279 318,279.5 321,280 324.5,280.5 327.5,281 330.5,281 334,281.5 337,282 340,282 343.5,282.5 346.5,283 349.5,283 353,283.5 356,283.5 359,284 362.5,284 365.5,284.5 368.5,284.5 372,285 375,285 378,285.5 381.5,285.5 384.5,285.5 387.5,286 391,286 394,286 397,286.5 400.5,286.5 403.5,286.5 406.5,287 410,287 413,287 416,287 419.5,287.5 422.5,287.5 425.5,287.5 429,287.5 432,287.5 435,288 438.5,288 441.5,288 444.5,288 448,288 451,288 454,288.5 457.5,288.5 460.5,288.5 463.5,288.5 467,288.5 470,288.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,81.5 166,290" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <line x1="166" y1="213" x2="166" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="213" x2="166" y2="213" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="166" cy="213" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="180" y="180.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0{,}37\cdot U_0$</div></foreignObject>
  <foreignObject x="259" y="112.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$u = U_0\,\mathrm{e}^{-t/\tau}$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ennen kuin kytket mitään, ja näytä kytkentä opettajalle ennen kuin kytket jännitelähteen päälle.

Tarkista ennen kytkemistä kaksi asiaa. Elektrolyyttikondensaattorin plusnapa kytketään sille puolelle, joka on yhteydessä jännitelähteen plusnapaan. Jännitelähteen jännite säädetään kondensaattoriin merkityn suurimman sallitun jännitteen alapuolelle; jos merkintää ei näy tai et ole varma, kysy raja opettajalta. Tarkista myös, että jännite mahtuu jänniteanturin tai mittarin mittausalueelle. Pura kondensaattori vastuksen kautta aina ennen kuin muutat kytkentää, äläkä oikosulje sen napoja johtimella.

::: tuki O OO
Yksi mahdollinen kytkentä: vaihtokytkimen asennossa A kondensaattori varautuu jännitelähteestä vastuksen kautta, ja asennossa B se purkautuu saman vastuksen kautta. Jännitemittari tai jänniteanturi on kytketty kondensaattorin rinnalle.

<svg data-fig="circuit" viewBox="0 0 600 330" role="img" aria-label="Kytkentäkaavio. Vasemmalla on tasajännitelähde, jonka jännite on U nolla. Vaihtokytkimen asennossa A lähde, vastus R ja kondensaattori C ovat samassa virtapiirissä, jolloin kondensaattori varautuu. Asennossa B lähde on irti, ja kondensaattori purkautuu vastuksen R kautta. Jännitemittari V on kytketty kondensaattorin rinnalle. Kondensaattorin plusnapa on vastuksen puolella, joka on asennossa A kytketty lähteen plusnapaan." style="max-width:100%;font-size:24px">
  <line x1="80" y1="60" x2="80" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="54" y1="150" x2="106" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="68" y1="166" x2="92" y2="166" stroke="#1f2933" stroke-width="6" stroke-linecap="butt"/>
  <line x1="80" y1="166" x2="80" y2="290" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="13" y="143.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_0$</div></foreignObject>
  <foreignObject x="112" y="121.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="112" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <line x1="80" y1="60" x2="230" y2="60" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="80" y1="290" x2="470" y2="290" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="230" y1="130" x2="230" y2="290" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="230" cy="60" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="230" cy="130" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="290" cy="95" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="286" y1="91" x2="236" y2="64" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="194" y="45.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="194" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{B}$</div></foreignObject>
  <circle cx="230" cy="290" r="5" fill="#1f2933"/>
  <line x1="296" y1="95" x2="320" y2="95" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="320" y="80" width="90" height="30" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="410" y1="95" x2="470" y2="95" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="355" y="41.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <line x1="470" y1="95" x2="470" y2="180" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="444" y1="180" x2="496" y2="180" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M444,202 Q470,190 496,202" fill="none" stroke="#1f2933" stroke-width="5" stroke-linejoin="round"/>
  <line x1="470" y1="196" x2="470" y2="290" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="416" y="176.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="500" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <circle cx="470" cy="140" r="5" fill="#1f2933"/>
  <circle cx="470" cy="250" r="5" fill="#1f2933"/>
  <line x1="470" y1="140" x2="550" y2="140" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="550" y1="140" x2="550" y2="171" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="550" cy="195" r="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="540" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <line x1="550" y1="219" x2="550" y2="250" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="550" y1="250" x2="470" y2="250" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
</svg>
:::

::: tuki O
**Ohjattu.** Tutki purkautumista. Mittaat kondensaattorin jännitettä $u$ ajan $t$ funktiona. Muutat vastuksen resistanssia: valitse opettajan antamista vastuksista kaksi, joista toisen resistanssi on noin kaksinkertainen toiseen verrattuna. Arvioi aikavakio etukäteen kondensaattoriin merkitystä kapasitanssista, $\tau \approx R \cdot C_\text{merkitty}$, ja valitse vastukset niin, että aikavakio on vähintään muutama sekunti, jos käytät anturia, ja vähintään noin puoli minuuttia, jos luet mittaria käsin. Vakiona pidät kondensaattorin, jännitelähteen jännitteen, mittarin ja kytkennän. Mittaa kummallakin vastuksella kaksi purkautumista.
:::

::: tuki OO
**Osittain ohjattu.** Päätä, tutkitko purkautumista vai varautumista, ja perustele valintasi. Päätä, mitkä vastukset käytät, mittaatko anturilla vai mittarilla ja kellolla, kuinka usein jännite luetaan, kuinka kauan mittaus kestää ja montako kertaa toistat sen. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Kuinka pitkä aikavakio on, kun arvioit sen kondensaattoriin merkitystä kapasitanssista ja vastuksen resistanssista? Ehditkö lukea mittaria tarpeeksi usein?
- Miten saat varmasti selville vastuksen resistanssin? Voit lukea sen vastuksen merkinnöistä tai mitata yleismittarilla, kun vastus on irti piiristä.
- Kuinka suuri on jännitemittarin tai anturin oma sisäinen resistanssi verrattuna vastukseen? Selvitä se mittarin ohjeesta tai kysy opettajalta.
- Mistä tiedät, että kondensaattori on varautunut täyteen ennen purkautumisen alkua?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset heti mittauksen aikana: jokaisesta mittauksesta vastuksen resistanssi ja jännite ajan funktiona. Anturilla mitatut tulokset tallennetaan tiedostoon, ja tiedoston nimi kirjataan muistiinpanoihin. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

::: tuki O
1. Käännä kytkin asentoon A ja odota, kunnes kondensaattorin jännite ei enää muutu. Kirjaa tämä jännite.
2. Käynnistä mittaus ja käännä kytkin asentoon B. Kondensaattori alkaa purkautua.
3. Mittaa, kunnes jännite on pudonnut alle kymmenesosaan alkuarvostaan. Jos luet mittaria käsin, toinen lukee jännitteen tasaisin väliajoin ja toinen kirjaa, niin että aikavakion aikana saat vähintään viisi lukemaa.
4. Toista mittaus samalla vastuksella, vaihda sitten toinen vastus ja tee sillä kaksi mittausta. Pura kondensaattori ennen vastuksen vaihtamista: jätä kytkin asentoon B, kunnes jännite on lähes nolla.

Mittauksen aikana voit käyttää tällaista taulukkoa (käsin luettaessa):

| $t\ (\text{s})$ | $u\ (\text{V})$ |
|---|---|
| | |
| | |
| | |

Tulokset kokoat tällaiseen taulukkoon, yksi rivi kutakin mittausta kohti:

| mittaus | $R\ (\text{k}\Omega)$ | $\tau\ (\text{s})$ | $C = \dfrac{\tau}{R}\ (\mu\text{F})$ |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti mittari tai anturi näyttää jännitteen ja kuinka tarkasti tunnet vastuksen resistanssin. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä jokaisesta mittauksesta kuvaaja, jossa on kondensaattorin jännite ajan funktiona. Merkitse akseleille suureet ja yksiköt, piirrä mittauspisteet äläkä yhdistä niitä murtoviivalla. Etsi malli, joka sopii pisteisiin, määritä siitä aikavakio $\tau$ ja laske kapasitanssi $C = \dfrac{\tau}{R}$ jokaisesta mittauksesta. [[apua:fy1-4|Graafinen esitys ja suoran sovittaminen]]

::: tuki OO
Kokeile ohjelmassa useita funktiotyyppejä ja vertaa, mikä niistä kulkee pisteiden kautta.
:::

Vastaa ensin mallista:

1. Millainen funktio kuvaa mittauspisteitä? Perustele mittaustuloksilla, miksi juuri se eikä esimerkiksi suora.
2. Mikä mallin parametri vastaa aikavakiota $\tau$? Perustele teoriaosan muutosnopeuden avulla.

::: tuki OO
**Tarkista mallisi.** Teoriaosan muutosnopeuden toteuttaa eksponenttifunktio. Purkautuvan kondensaattorin jännite on

```latex
u = U_0\,\mathrm{e}^{-t/\tau}
```

missä $U_0$ on jännite hetkellä $t = 0$ ja $\mathrm{e} \approx 2{,}718$ on Neperin luku. Jokaisen aikavakion $\tau$ pituisen ajan kuluessa jännite pienenee samaan osuuteen, $\mathrm{e}^{-1} \approx 0{,}37$, siitä mitä se oli jakson alussa, ja alkuhetken tangentti leikkaa aika-akselin kohdassa $t = \tau$. Varautuvan kondensaattorin jännite on $u = U_0\left(1 - \mathrm{e}^{-t/\tau}\right)$, eli erotus $U_0 - u$ pienenee samalla tavalla kuin purkautuvan kondensaattorin jännite. Vastasiko tämä sitä, mitä löysit mittaustuloksistasi?
:::

::: tuki O OO
**Kaksi tapaa määrittää aikavakio.**

- **Eksponenttimallin sovitus.** Sovita pisteisiin ohjelmalla malli $u = A\,\mathrm{e}^{-Bt} + D$. Vertaa sitä malliin $u = U_0\,\mathrm{e}^{-t/\tau}$: parametri $B$ on $\dfrac{1}{\tau}$, joten $\tau = \dfrac{1}{B}$. Vakiotermi $D$ ottaa huomioon mittarin mahdollisen nollakohdan virheen, ja purkautumisessa sen pitäisi olla lähellä nollaa. Varautumisessa sovitetaan sama malli, ja silloin $A$ on negatiivinen ja $D$ on lähellä jännitettä $U_0$.
- **Linearisointi.** Ota mallista $u = U_0\,\mathrm{e}^{-t/\tau}$ luonnollinen logaritmi: $\ln u = \ln U_0 - \dfrac{1}{\tau}\cdot t$. Kun pystyakselille valitaan $\ln u$ ja vaaka-akselille $t$, pisteiden pitäisi asettua suoralle, jonka kulmakerroin on $-\dfrac{1}{\tau}$. Laske logaritmi jännitteen lukuarvosta voltteina. Varautumisessa linearisoidaan erotus $U_0 - u$, ei jännitettä $u$; käytä jännitteenä $U_0$ mitattua loppujännitettä, jota kondensaattorin jännite ei enää ylitä. (Eksponenttimallin sovituksessa vakiotermi $D$ hoitaa tämän itse.) Jätä pois lopun pienet jännitteet, joissa mittarin lukematarkkuus on jo suuri osa jännitteestä.

<svg data-fig="linear" viewBox="0 0 600 320" role="img" aria-label="Kuvaaja: jännitteen luonnollinen logaritmi ln u ajan t funktiona purkautumisen mallin mukaan. Kuvaaja on laskeva suora, jonka kulmakerroin on miinus yksi jaettuna tau:lla. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="271" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\ln u$</div></foreignObject>
  <polyline points="90,76.5 451,243.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="211.5" y="74" width="183" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } -\dfrac{1}{\tau}$</div></foreignObject>
</svg>

Kummallakaan tavalla ei ole väliä, mihin kohtaan valitset hetken $t = 0$: eksponenttifunktio pienenee samassa suhteessa jokaisen yhtä pitkän ajan kuluessa, joten aikavakio ei riipu alkuhetken valinnasta.
:::

::: tuki O
Käytä eksponenttimallin sovitusta ohjelmalla. Jos ohjelmassa ei ole sitä, käytä linearisointia ja sovita suora.
:::

Kirjoita sovitetun mallin yhtälö ja vastaa:

- Miten aikavakio muuttui, kun resistanssi muuttui? Vastaako muutos yhtälöä $\tau = RC$?
- Saitko eri resistansseilla saman kapasitanssin?

Mallin sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita kapasitanssi muodossa $C = (C \pm \Delta C)\ \mu\text{F}$ ja perustele, miten arvioit epävarmuuden. Kapasitanssi on kahden suureen osamäärä, joten sen suhteellinen epävarmuus on aikavakion ja resistanssin suhteellisten epävarmuuksien summa:

```latex
\frac{\Delta C}{C} = \frac{\Delta \tau}{\tau} + \frac{\Delta R}{R}
```

::: tuki O OO
Aikavakion epävarmuuden $\Delta \tau$ voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat parametrin keskivirheen. Jos $\tau = \dfrac{1}{B}$, suhteellinen epävarmuus on sama: $\dfrac{\Delta \tau}{\tau} = \dfrac{\Delta B}{B}$.
- **Toistomittausten hajonta.** Jos mittasit samalla vastuksella useita kertoja, arvioi epävarmuus aikavakioiden vaihteluvälin puolikkaana: $\Delta \tau = \dfrac{\tau_\text{max} - \tau_\text{min}}{2}$.

Resistanssin epävarmuus $\Delta R$ saadaan yleismittarin tarkkuudesta tai, jos käytät vastuksen merkintää, sen toleranssista. Pyöristä $\Delta C$ yhteen merkitsevään numeroon ja $C$ samaan tarkkuuteen.
:::

Vertaa tulosta kondensaattoriin merkittyyn arvoon. Kondensaattorin merkintöihin kuuluu usein toleranssi, joka kertoo, kuinka paljon todellinen kapasitanssi saa valmistajan mukaan poiketa merkitystä; lue se kondensaattorin kyljestä tai kysy opettajalta. Jos väli $C \pm \Delta C$ ja merkityn arvon toleranssiväli ovat päällekkäin, tulos on sopusoinnussa merkinnän kanssa. Se ei todista, että arvot ovat täsmälleen samat.

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät aiheuttivat mittausepävarmuutta, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet kapasitanssia? Palaa teoriaosan oletuksiin: toteutuivatko ne mittauksessasi? Miten parantaisit mittausta?

::: tuki O OO
Mieti ainakin näitä:

- Kulkiko purkausvirta kokonaan vastuksen kautta, vai kulkiko osa siitä jännitemittarin kautta? Miten se olisi vaikuttanut aikavakioon ja siitä laskettuun kapasitanssiin?
- Voiko kondensaattori vuotaa varausta eristeensä läpi?
- Kuinka tarkasti tunsit vastuksen resistanssin?
:::

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Millainen malli kuvaa kondensaattorin jännitettä, ja miten vastuksen resistanssi vaikutti purkautumiseen tai varautumiseen? Perustele vastauksesi mittaustuloksilla ja viittaa kuvaajiin, esimerkiksi "kuvaajasta 2 nähdään, että …". Kuinka hyvin saamasi kapasitanssi vastaa merkittyä arvoa? Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki yhdeksän osaa. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria (osa 2):** yhtälöt $Q = Cu$ ja $I = \dfrac{u}{R}$, aikavakio $\tau = RC$ ja mallin oletukset.
- **Koejärjestely ja menetelmä (osa 3):** kytkentäkaavio ja työturvallisuus: miten varmistit napaisuuden, jännitteen rajan ja kondensaattorin purkamisen.
- **Tulosten käsittely ja graafinen analyysi (osa 5):** jännitteen kuvaaja ajan funktiona, sovitettu malli ja perustelu sille, miten aikavakio saadaan mallista.
- **Tulos (osa 6):** $C = (C \pm \Delta C)\ \mu\text{F}$ oikein pyöristettynä, kaikki eri resistansseilla saadut arvot näkyvissä.
- **Luotettavuus ja mittausepävarmuus (osa 8):** vertailu merkittyyn arvoon ja konkreettiset epävarmuuden lähteet vaikutuksen suuntineen.

## Laajennus: kapasitanssi aikavakion ja resistanssin kuvaajasta

Yhtälön $\tau = RC$ mukaan aikavakio on suoraan verrannollinen resistanssiin, kun kondensaattori pysyy samana. Mittaa aikavakio usealla, esimerkiksi viidellä, eri resistanssilla; perusmittausten kaksi resistanssia voivat olla niistä kaksi. Piirrä kuvaaja, jossa on aikavakio resistanssin funktiona. Jos malli pätee, pisteet asettuvat suoralle, jonka kulmakerroin on kapasitanssi $C$. Sovita suora, jolla saa olla vakiotermi: jos piirissä on vastuksen lisäksi muuta sarjaresistanssia $r$, esimerkiksi johtimissa tai kytkimessä (varattaessa myös jännitelähteessä), aikavakio on $\tau = (R + r)\cdot C$. Silloin suora ei kulje origon kautta, mutta kulmakerroin on silti $C$.

Määritä kapasitanssi kulmakertoimesta epävarmuuksineen ja vertaa sitä yksittäisistä mittauksista laskettuun arvoon. Kumpi tulos on luotettavampi, ja miksi? Poikkeavatko pisteet suoralta suurilla tai pienillä resistansseilla? Palaa teoriaosan oletuksiin ja mieti, mikä oletus voisi lakata pätemästä kummassakin päässä.

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi ja kytkentäkaaviosi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
