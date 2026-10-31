# Liikemäärän säilyminen törmäyksissä

> **Tutkimuskysymys:** Säilyykö kahden vaunun kokonaisliikemäärä, kun vaunut törmäävät kimmoisasti tai tarttuvat törmäyksessä yhteen?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä on pitkä vaunurata, jonka kummassakin päässä on liikeanturi. Radalla kaksi vaunua liikkuu toisiaan kohti, ja vauhtiviivat näyttävät liikkeen. Vasemmanpuoleisessa vaunussa on lisäpunnus, ja oikeanpuoleinen, kevyempi vaunu liikkuu nopeammin. Vaunujen vastakkaisissa päissä on jousipuskurit. Pöydällä oleva kannettava tietokone näyttää anturien mittaamat kuvaajat." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10lh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10lh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10lh-wall)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy10lh-desk)"/>
  <line x1="0" y1="462" x2="1200" y2="458" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="484" x2="1200" y2="480" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="506" x2="1200" y2="502" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="528" x2="1200" y2="524" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="550" x2="1200" y2="546" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="568" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="440" x2="1200" y2="440" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="192" y="380" width="16" height="60" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="164" y="432" width="72" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="992" y="380" width="16" height="60" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="964" y="432" width="72" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="60" y="360" width="1080" height="20" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <line x1="64" y1="370" x2="1136" y2="370" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="60" y="334" width="16" height="26" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1124" y="334" width="16" height="26" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="80" y="264" width="70" height="96" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="143" y="291" width="8" height="42" rx="2" fill="#343a40" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="1050" y="264" width="70" height="96" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1049" y="291" width="8" height="42" rx="2" fill="#343a40" stroke="#1f2933" stroke-width="1.5"/>
  <g opacity="1">
  <rect x="375" y="282" width="150" height="54" rx="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="405" y="252.5" width="90" height="29.5" rx="4" fill="#ffc078" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="405" cy="348" r="11.88" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="495" cy="348" r="11.88" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M525,309 L527,303 L531,315.5 L535,303 L539,315.5 L543,303 L547,315.5 L549,309" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="549" y1="300" x2="549" y2="318" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  </g>
  <g opacity="1">
  <rect x="685" y="282" width="150" height="54" rx="5" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="715" cy="348" r="11.88" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="805" cy="348" r="11.88" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M685,309 L683,303 L679,315.5 L675,303 L671,315.5 L667,303 L663,315.5 L661,309" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="661" y1="300" x2="661" y2="318" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  </g>
  <line x1="300" y1="298" x2="355" y2="298" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="855" y1="298" x2="960" y2="298" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="312" y1="314" x2="355" y2="314" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="855" y1="314" x2="946" y2="314" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="324" y1="330" x2="355" y2="330" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <line x1="855" y1="330" x2="932" y2="330" stroke="#6b7480" stroke-width="3" stroke-linecap="round"/>
  <path d="M640,560 L960,560 L990,590 L610,590 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="660" y="440" width="280" height="120" rx="6" fill="#343a40" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="672" y="450" width="256" height="100" fill="#ffffff"/>
  <line x1="690" y1="540" x2="910" y2="540" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="690" y1="540" x2="690" y2="458" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="690" y1="520" x2="900" y2="490" stroke="#ffc078" stroke-width="4" stroke-linecap="butt"/>
  <line x1="690" y1="530" x2="900" y2="462" stroke="#6c757d" stroke-width="4" stroke-linecap="butt"/>
</svg>

Kun kaksi vaunua törmää radalla, kummankin nopeus muuttuu: vauhti voi kasvaa, pienentyä tai liikkeen suunta kääntyä. Tässä tutkimuksessa mittaat liikeantureilla vaunujen nopeudet ennen törmäystä ja sen jälkeen ja selvität, muuttuuko vaunujen yhteinen liikemäärä törmäyksessä. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** vaunujen kokonaisliikemäärä ennen törmäystä ja sen jälkeen useissa kimmoisissa ja täysin kimmottomissa törmäyksissä, joissa vaunujen massat tai alkunopeudet vaihtelevat, sekä se, ovatko kokonaisliikemäärät ennen ja jälkeen samat mittausepävarmuuden rajoissa.

**Päätät itse:** mitä törmäyksiä teet (massat, kumpi vaunu liikkuu ja mihin suuntaan), montako törmäystä kumpaakin tyyppiä teet, mikä suunta on positiivinen ja miten anturien lukemat muutetaan sen mukaisiksi, miten luet nopeudet anturien kuvaajista, miten esität liikemäärien vertailun ja miten arvioit epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, liike-energian muutos kummassakin törmäystyypissä, kuuluu työhösi. Se onnistuu samoista mittauksista, joten suunnittele mittaukset niin, että niistä saa laskettua myös liike-energiat.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kevyt vaunu törmää kimmoisasti levossa olevaan, paljon raskaampaan vaunuun. Mihin suuntaan kevyt vaunu liikkuu törmäyksen jälkeen, ja mitä raskaalle vaunulle tapahtuu?
2. Vaunu törmää levossa olevaan samanmassaiseen vaunuun, ja vaunut tarttuvat yhteen. Kuinka suuri on niiden yhteinen nopeus verrattuna törmäävän vaunun alkunopeuteen?
3. Kaksi vaunua liikkuu toisiaan kohti ja tarttuu yhteen. Voivatko ne pysähtyä kokonaan? Millä ehdolla?
4. Mikä mittauksessa voisi saada kokonaisliikemäärän näyttämään muuttuvan, vaikka se todellisuudessa säilyisi?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Liikemäärää ei voi lukea suoraan mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitkä suureet mittaamalla saat selville vaunujen kokonaisliikemäärän ennen törmäystä ja sen jälkeen?
2. Nopeus on vektori. Miten otat huomioon, mihin suuntaan kukin vaunu liikkuu?
3. Millä ehdolla kokonaisliikemäärän pitäisi säilyä, ja miten järjestät mittauksen niin, että ehto täyttyy mahdollisimman hyvin?

## Teoriaa lyhyesti

Kappaleen **liikemäärä** on $\overline{p} = m\overline{v}$, missä $m$ on kappaleen massa ja $\overline{v}$ sen nopeus. Liikemäärä on vektori, jonka suunta on sama kuin nopeuden. Kahden vaunun **kokonaisliikemäärä** on niiden liikemäärien vektorisumma $\overline{p}_\text{kok} = \overline{p}_1 + \overline{p}_2$.

Törmäyksessä vaunut työntävät toisiaan yhtä suurilla ja vastakkaissuuntaisilla voimilla yhtä kauan (Newtonin kolmas laki), joten toisen vaunun liikemäärän muutos on yhtä suuri ja vastakkaissuuntainen kuin toisen. Kokonaisliikemäärä säilyy, kun vaunuihin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni. Vaakasuoralla radalla paino ja tukivoima kumoavat toisensa, ja vierimisvastus on pieni. [[apua:fy4-10|Liikemäärän säilyminen ja törmäykset]]

Törmäys on **kimmoisa**, jos vaunujen yhteinen liike-energia on törmäyksen jälkeen yhtä suuri kuin ennen sitä. Jousipuskureilla törmäävät vaunut ovat lähellä tätä. Törmäys on **täysin kimmoton**, jos vaunut tarttuvat toisiinsa ja jatkavat yhdessä samalla nopeudella.

::: tuki O OO
Tarkista kirjauksesi tästä. Vaunuista mitataan massat $m_1$ ja $m_2$ sekä nopeudet ennen törmäystä ($v_1$ ja $v_2$) ja sen jälkeen ($v_1'$ ja $v_2'$). Koska vaunut liikkuvat samalla suoralla, valitaan yksi suunta positiiviseksi. Silloin jokainen nopeus on etumerkillinen luku: vastakkaiseen suuntaan liikkuvan vaunun nopeus on negatiivinen.

<svg data-fig="setup" viewBox="0 0 600 330" role="img" aria-label="Kaaviokuva sivulta. Vaakasuoran radan vasemmassa päässä on anturi 1 ja oikeassa päässä anturi 2, ja kumpikin osoittaa radan keskelle. Radalla ovat vaunu 1, jonka massa on m1, ja vaunu 2, jonka massa on m2. Vaunun 1 nopeus v1 osoittaa oikealle ja vaunun 2 nopeus v2 vasemmalle; nopeusnuolet ovat sinisiä. Radan alla on valittu positiivinen suunta, oikealle. Harmaat nuolet anturien alla näyttävät, mihin suuntaan kukin anturi mittaa nopeuden positiiviseksi: anturi 1 oikealle ja anturi 2 vasemmalle, eli anturin 2 suunta on vastakkainen valittuun positiiviseen suuntaan nähden." style="max-width:100%;font-size:24px">
  <rect x="20" y="190" width="560" height="14" rx="2" fill="#c4ccd4" stroke="#8a96a3" stroke-width="2"/>
  <line x1="24" y1="197" x2="576" y2="197" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="28" y="126" width="44" height="64" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="65" y="144" width="8" height="28" rx="2" fill="#343a40" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="528" y="126" width="44" height="64" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="527" y="144" width="8" height="28" rx="2" fill="#343a40" stroke="#1f2933" stroke-width="1.5"/>
  <g opacity="1">
  <rect x="140" y="120" width="120" height="50" rx="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="164" cy="180" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="236" cy="180" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M260,145 L261.5,139 L265,151 L268,139 L271,151 L274.5,139 L277.5,151 L279,145" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="279" y1="136" x2="279" y2="154" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  </g>
  <g opacity="1">
  <rect x="340" y="120" width="120" height="50" rx="5" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="364" cy="180" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="436" cy="180" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M340,145 L338.5,139 L335,151 L332,139 L329,151 L325.5,139 L322.5,151 L321,145" fill="none" stroke="#6c757d" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="321" y1="136" x2="321" y2="154" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  </g>
  <foreignObject x="183.5" y="130.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="383.5" y="130.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="160" y1="70" x2="246" y2="70" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M260,70 L245,77 L245,63 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="187.5" y="25.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <line x1="440" y1="70" x2="374" y2="70" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M360,70 L375,63 L375,77 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="377.5" y="25.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <line x1="30" y1="232" x2="99" y2="232" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,232 L98,237.5 L98,226.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="70" y="246" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{anturi 1: }+$</div></foreignObject>
  <line x1="570" y1="232" x2="501" y2="232" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,232 L502,226.5 L502,237.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="428" y="246" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{anturi 2: }+$</div></foreignObject>
  <line x1="230" y1="300" x2="357" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M370,300 L356,306.5 L356,293.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="27" y="288" width="195" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{positiivinen suunta}$</div></foreignObject>
  <foreignObject x="378" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
</svg>

Liikemäärän säilyminen tulee yhdessä ulottuvuudessa muotoon

```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```

missä vasen puoli on kokonaisliikemäärä $p_\text{kok}$ ennen törmäystä ja oikea puoli kokonaisliikemäärä $p_\text{kok}'$ törmäyksen jälkeen ($\text{kg}\cdot\text{m/s}$). Täysin kimmottomassa törmäyksessä vaunuilla on törmäyksen jälkeen yhteinen nopeus, joten $v_1' = v_2'$.

**Anturien suunnat.** Kumpikin liikeanturi mittaa etäisyyttä omasta paikastaan lähimpään vaunuun. Radan vasemmassa päässä oleva anturi näyttää positiivista nopeutta, kun vaunu loittonee siitä eli liikkuu oikealle. Oikeassa päässä oleva anturi näyttää positiivista nopeutta, kun vaunu loittonee siitä eli liikkuu vasemmalle. Jos positiiviseksi suunnaksi valitaan oikea, oikeanpuoleisen anturin nopeuksien etumerkki on siis vaihdettava. Tarkista asia ennen mittauksia: työnnä vaunua hitaasti oikealle ja katso, mitä kumpikin anturi näyttää.

Vaakasuora rata ja pieni vierimisvastus ovat ehto sille, että ulkoisten voimien impulssi jää pieneksi. Jos rata on kalteva, painon radan suuntainen osa on ulkoinen voima, joka muuttaa vaunujen liikemäärää koko ajan.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä törmäyksiä teet, mitä mittaat ja mitä pidät vakiona. Tarkista, että rata on vaakasuorassa.

::: tuki O
**Ohjattu.** Tee ainakin kolme kimmoista törmäystä, joissa jousipuskurit osuvat toisiinsa, ja ainakin kolme täysin kimmotonta törmäystä, joissa vaunut tarttuvat yhteen. Käytä kummassakin tyypissä esimerkiksi näitä tilanteita:

- vaunut ovat yhtä raskaat, ja vaunu 2 on aluksi levossa
- vaunuun 2 on lisätty punnuksia, ja se on aluksi levossa
- vaunut liikkuvat toisiaan kohti.

Punnitse kumpikin vaunu lisäpunnuksineen vaa'alla. Valitse oikea positiiviseksi suunnaksi. Työnnä vaunua rauhallisesti ja päästä siitä irti hyvissä ajoin ennen törmäystä, jotta käsi ei vaikuta vaunuun törmäyksen aikana.

**Radan vaakasuoruus.** Aseta vaunu radalle levossa: se ei saa lähteä liikkeelle itsestään. Tönäise vaunua sitten kevyesti kumpaankin suuntaan ja katso anturin nopeuskuvaajasta, että nopeus pienenee kumpaankin suuntaan suunnilleen yhtä hitaasti.
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, mitä massoja ja alkunopeuksia käytät, montako törmäystä teet kumpaakin tyyppiä ja miten tarkistat radan vaakasuoruuden. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten saat vaunut tarttumaan toisiinsa niin, että ne jatkavat varmasti yhdessä?
- Miten varmistat, että käsi ei ole kosketuksissa vaunuun törmäyksen aikana?
- Näkeekö kumpikin anturi koko ajan oman vaununsa? Pysyvätkö vaunut anturien mittausalueella koko mittauksen ajan?
- Millä tavalla tarkistat, että muutit oikeanpuoleisen anturin lukemat oikein yhteisen positiivisen suunnan mukaisiksi?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: massat, törmäyksen tyyppi ja anturien nopeudet sellaisina kuin luit ne. Kirjaa erikseen nopeudet, jotka on muutettu yhteisen positiivisen suunnan mukaisiksi.

Anturit tallentavat vaunujen paikan ajan funktiona. Nopeus ennen törmäystä ja sen jälkeen luetaan niistä kuvaajan osista, joissa vaunut eivät kosketa toisiaan. [[apua:fy4-1|Nopeus paikan kuvaajan kulmakertoimena]]

::: tuki O OO
Vierimisvastus pienentää vaunujen nopeutta hitaasti koko ajan, joten lue nopeus mahdollisimman läheltä törmäystä: juuri ennen kosketusta ja heti sen jälkeen, kun vaunut ovat irronneet toisistaan tai alkaneet liikkua yhdessä.

<svg data-fig="velocity" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: yhden vaunun nopeus v ajan t funktiona mallin mukaan. Ennen törmäystä nopeus pienenee hyvin hitaasti vierimisvastuksen takia. Törmäyksen aikana, joka on merkitty varjostetulla alueella, nopeus muuttuu nopeasti pienemmäksi. Törmäyksen jälkeen nopeus taas pienenee hitaasti. Nopeus v1 luetaan juuri ennen törmäystä ja nopeus v1 pilkku heti törmäyksen jälkeen. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="257,280 257,69 295,69 295,280" fill="#e3dccb" fill-opacity="0.6"/>
  <polyline points="97.5,113 99,113.5 100.5,113.5 101.5,113.5 103,113.5 104,113.5 105.5,113.5 107,113.5 108,114 109.5,114 111,114 112,114 113.5,114 115,114 116,114 117.5,114 119,114.5 120,114.5 121.5,114.5 123,114.5 124,114.5 125.5,114.5 127,114.5 128,115 129.5,115 131,115 132,115 133.5,115 135,115 136,115 137.5,115.5 139,115.5 140,115.5 141.5,115.5 143,115.5 144,115.5 145.5,115.5 147,116 148,116 149.5,116 151,116 152,116 153.5,116 155,116 156,116 157.5,116.5 159,116.5 160,116.5 161.5,116.5 163,116.5 164,116.5 165.5,116.5 167,117 168,117 169.5,117 171,117 172,117 173.5,117 174.5,117 176,117.5 177.5,117.5 178.5,117.5 180,117.5 181.5,117.5 182.5,117.5 184,117.5 185.5,118 186.5,118 188,118 189.5,118 190.5,118 192,118 193.5,118 194.5,118.5 196,118.5 197.5,118.5 198.5,118.5 200,118.5 201.5,118.5 202.5,118.5 204,118.5 205.5,119 206.5,119 208,119 209.5,119 210.5,119 212,119 213.5,119 214.5,119.5 216,119.5 217.5,119.5 218.5,119.5 220,119.5 221.5,119.5 222.5,119.5 224,120 225.5,120 226.5,120 228,120 229.5,120 230.5,120 232,120 233.5,120.5 234.5,120.5 236,120.5 237,120.5 238.5,120.5 240,120.5 241,120.5 242.5,120.5 244,121 245,121 246.5,121 248,121 249,121 250.5,121 252,121 253,121.5 254.5,121.5 256,121.5 257,121.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="257,121.5 257.5,121.5 258,121.5 258,121.5 258.5,122 259,122 259,122 259.5,122 259.5,122.5 260,122.5 260.5,123 260.5,123.5 261,123.5 261.5,124 261.5,124.5 262,125 262.5,125.5 262.5,126 263,126.5 263,127 263.5,127.5 264,128 264,128.5 264.5,129.5 265,130 265,130.5 265.5,131.5 266,132 266,133 266.5,133.5 266.5,134.5 267,135 267.5,136 267.5,137 268,138 268.5,138.5 268.5,139.5 269,140.5 269,141.5 269.5,142.5 270,143.5 270,144.5 270.5,145.5 271,146.5 271,147.5 271.5,148.5 272,150 272,151 272.5,152 272.5,153 273,154 273.5,155.5 273.5,156.5 274,157.5 274.5,158.5 274.5,160 275,161 275,162 275.5,163.5 276,164.5 276,165.5 276.5,166.5 277,168 277,169 277.5,170 278,171.5 278,172.5 278.5,173.5 278.5,174.5 279,176 279.5,177 279.5,178 280,179 280.5,180.5 280.5,181.5 281,182.5 281.5,183.5 281.5,184.5 282,185.5 282,186.5 282.5,187.5 283,188.5 283,189.5 283.5,190.5 284,191.5 284,192.5 284.5,193.5 285,194 285,195 285.5,196 285.5,196.5 286,197.5 286.5,198.5 286.5,199 287,200 287.5,200.5 287.5,201 288,202 288,202.5 288.5,203 289,203.5 289,204.5 289.5,205 290,205.5 290,206 290.5,206 291,206.5 291,207 291.5,207.5 291.5,208 292,208 292.5,208.5 292.5,208.5 293,209 293.5,209 293.5,209 294,209.5 294,209.5 294.5,209.5 295,209.5 295,209.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="295,209.5 296.5,209.5 298,209.5 299,210 300.5,210 302,210 303,210 304.5,210 306,210 307,210 308.5,210.5 310,210.5 311,210.5 312.5,210.5 314,210.5 315,210.5 316.5,210.5 318,211 319,211 320.5,211 322,211 323,211 324.5,211 326,211 327,211.5 328.5,211.5 330,211.5 331,211.5 332.5,211.5 334,211.5 335,211.5 336.5,211.5 338,212 339,212 340.5,212 342,212 343,212 344.5,212 345.5,212 347,212.5 348.5,212.5 349.5,212.5 351,212.5 352.5,212.5 353.5,212.5 355,212.5 356.5,213 357.5,213 359,213 360.5,213 361.5,213 363,213 364.5,213 365.5,213.5 367,213.5 368.5,213.5 369.5,213.5 371,213.5 372.5,213.5 373.5,213.5 375,214 376.5,214 377.5,214 379,214 380.5,214 381.5,214 383,214 384.5,214 385.5,214.5 387,214.5 388.5,214.5 389.5,214.5 391,214.5 392.5,214.5 393.5,214.5 395,215 396.5,215 397.5,215 399,215 400.5,215 401.5,215 403,215 404.5,215.5 405.5,215.5 407,215.5 408,215.5 409.5,215.5 411,215.5 412,215.5 413.5,216 415,216 416,216 417.5,216 419,216 420,216 421.5,216 423,216.5 424,216.5 425.5,216.5 427,216.5 428,216.5 429.5,216.5 431,216.5 432,216.5 433.5,217 435,217 436,217 437.5,217 439,217 440,217 441.5,217 443,217.5 444,217.5 445.5,217.5 447,217.5 448,217.5 449.5,217.5 451,217.5 452,218 453.5,218 455,218" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="90" y1="121.5" x2="257" y2="121.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="47" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_1$</div></foreignObject>
  <line x1="90" y1="209.5" x2="295" y2="209.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="35" y="195" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_1'$</div></foreignObject>
  <foreignObject x="138.5" y="72" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="228.5" y="32.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{törmäys}$</div></foreignObject>
  <foreignObject x="331.5" y="168.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
</svg>

Nopeuden saat kahdella tavalla: sovita suora paikan kuvaajan siihen osaan, joka on juuri ennen törmäystä tai heti sen jälkeen, ja käytä suoran kulmakerrointa, tai lue nopeuskuvaajasta samojen kohtien keskiarvo.
:::

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Kirjoita nopeuksiin etumerkki, joka vastaa yhteistä positiivista suuntaa.

| törmäys | $m_1\ (\text{kg})$ | $m_2\ (\text{kg})$ | $v_1\ (\text{m/s})$ | $v_2\ (\text{m/s})$ | $v_1'\ (\text{m/s})$ | $v_2'\ (\text{m/s})$ |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Täysin kimmottomassa törmäyksessä kumpikin anturi mittaa yhteen tarttuneiden vaunujen nopeutta. Jos muutit etumerkit oikein, $v_1'$ ja $v_2'$ ovat lähes samat: tämä on hyvä tarkistus.
:::

Muista mittausepävarmuus ja kirjaa ylös, miten arvioit sen.

::: tuki O OO
Arvioi, kuinka tarkasti vaaka antaa massan ja kuinka tarkasti luet nopeuden kuvaajasta, ja kirjaa arviot ylös.
:::

## Käsittele tulokset

Laske jokaisesta törmäyksestä kummankin vaunun liikemäärä sekä kokonaisliikemäärä ennen törmäystä ja sen jälkeen. Esitä vertailu niin, että siitä näkee yhdellä silmäyksellä, säilyykö kokonaisliikemäärä kummassakin törmäystyypissä. Laskuissa voit käyttää esimerkiksi taulukkolaskentaa.

::: tuki O
Lisää taulukkoon sarakkeet $p_\text{kok} = m_1 v_1 + m_2 v_2$, $p_\text{kok}' = m_1 v_1' + m_2 v_2'$ ja niiden erotus $p_\text{kok}' - p_\text{kok}$. Piirrä lisäksi kuvaaja, jonka pystyakselilla on kokonaisliikemäärä törmäyksen jälkeen ja vaaka-akselilla kokonaisliikemäärä ennen törmäystä. Merkitse kimmoiset ja täysin kimmottomat törmäykset eri merkeillä.
:::

Vastaa:

1. Ovatko kokonaisliikemäärät ennen ja jälkeen yhtä suuret? Onko erotuksissa jokin järjestelmällinen suunta, esimerkiksi onko liikemäärä jälkeen useimmiten pienempi kuin ennen?
2. Eroavatko kimmoiset ja täysin kimmottomat törmäykset toisistaan liikemäärän säilymisen kannalta?
3. Laske kummankin vaunun liikemäärän muutos törmäyksessä. Tukevatko mittauksesi sitä, että muutokset ovat yhtä suuret ja vastakkaissuuntaiset, kuten Newtonin kolmannesta laista seuraa?

::: tuki O OO
**Miksi juuri tämä kuvaaja?** Jos kokonaisliikemäärä säilyy, jokaisen törmäyksen piste on suoralla $p_\text{kok}' = p_\text{kok}$, joka kulkee origon kautta ja jonka kulmakerroin on $1$. Suora on piirretty kuvaajaan mallina: siinä ei ole mittauspisteitä. Kun vaunut liikkuvat toisiaan kohti, kokonaisliikemäärä voi olla negatiivinen, joten akseleita voi joutua jatkamaan origon toiselle puolelle.

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: kokonaisliikemäärä törmäyksen jälkeen kokonaisliikemäärän ennen törmäystä funktiona, jos liikemäärä säilyy. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on yksi. Kuvassa näkyy positiivisten liikemäärien osa: jos liikemäärän suuruus pienenee törmäyksessä, piste on suoran alapuolella. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="478" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,280 L477,286 L477,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,30 L96,43 L84,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="496" y="265.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p_\text{kok}$</div></foreignObject>
  <foreignObject x="80" y="-0.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p_\text{kok}'$</div></foreignObject>
  <polyline points="90,280 451,61.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="170" y="74.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p_\text{kok}' = p_\text{kok}$</div></foreignObject>
  <line x1="379" y1="114.5" x2="379" y2="170" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M379,179 L374.5,169 L383.5,169 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="297" y="190" width="164" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{suuruus pienenee}$</div></foreignObject>
</svg>

Jos ulkoinen voima, kuten vierimisvastus, on pienentänyt kokonaisliikemäärän suuruutta (itseisarvoa), tai nopeudet on luettu liian kaukaa törmäyksestä, pisteet poikkeavat suoralta järjestelmällisesti: kun $p_\text{kok} > 0$, ne ovat suoran alapuolella, ja kun $p_\text{kok} < 0$, suoran yläpuolella.
:::

## Epävarmuus ja luotettavuus

Perustele jokaisen törmäyksen kohdalla, onko kokonaisliikemäärien erotus $p_\text{kok}' - p_\text{kok}$ pienempi kuin erotuksen epävarmuus, ja kerro, miten arvioit epävarmuuden.

::: tuki O OO
Kokonaisliikemäärän epävarmuuden voit arvioida jommallakummalla tavalla:

- **Toistot.** Tee sama törmäys samoilla massoilla ainakin kolme kertaa. Laske jokaisesta suhteellinen erotus $\dfrac{p_\text{kok}' - p_\text{kok}}{p_\text{kok}}$ ja katso, kuinka paljon se vaihtelee toistosta toiseen.
- **Ääriarvot.** Laske vaunun liikemäärä ensin massan ja nopeuden pienimmillä mahdollisilla arvoilla ja sitten suurimmilla. Liikemäärän virhe-arvio on tulosten erotuksen puolikas. Kokonaisliikemäärän virhe-arvio on vaunujen liikemäärien virhe-arvioiden summa. Erotuksen $p_\text{kok}' - p_\text{kok}$ virhe-arvio on $\Delta p_\text{kok} + \Delta p_\text{kok}'$: jos erotus on sitä pienempi, kokonaisliikemäärät ovat sopusoinnussa. [[apua:fy1-3|Virhe-arvio ja suhteellinen virhe]]

Kun vaunut liikkuvat toisiaan kohti, kokonaisliikemäärä voi olla lähellä nollaa. Silloin suhteellinen erotus on harhaanjohtava, ja erotusta kannattaa verrata suoraan erotuksen virhe-arvioon $\Delta p_\text{kok} + \Delta p_\text{kok}'$.
:::

Pohdi sitten luotettavuutta konkreettisesti: olivatko erot satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet muuttivat tulosta? Mieti ainakin vierimisvastusta, radan kaltevuutta, käden vaikutusta ja sitä, mistä kuvaajan kohdasta nopeudet luettiin. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Säilyikö kokonaisliikemäärä kimmoisissa törmäyksissä? Entä täysin kimmottomissa? Ovatko erot mittausepävarmuuden rajoissa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Viittaa taulukkoon tai kuvaajaan, esimerkiksi "taulukosta 2 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** millä ehdolla kokonaisliikemäärä säilyy, ja miten kimmoisa ja täysin kimmoton törmäys eroavat toisistaan.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, jossa näkyvät anturit, vaunut ja valittu positiivinen suunta, sekä se, miten anturien lukemat muutettiin tämän suunnan mukaisiksi ja miten radan vaakasuoruus tarkistettiin.
- **Mittaustulokset:** massat ja nopeudet sellaisina kuin ne luettiin sekä etumerkillisinä yhteisen suunnan mukaan.
- **Tulos:** kokonaisliikemäärät ennen ja jälkeen jokaisessa törmäyksessä epävarmuuksineen.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: liike-energia kahdessa törmäystyypissä

Liikemäärän lisäksi voit tutkia samoista mittauksista vaunujen yhteistä liike-energiaa. Vaunun liike-energia on $E_\text{k} = \tfrac12 mv^2$. Se ei riipu nopeuden suunnasta, joten etumerkillä ei ole siinä merkitystä. [[apua:fy4-7|Liike-energia]]

Laske jokaisesta törmäyksestä vaunujen yhteinen liike-energia ennen törmäystä ja sen jälkeen sekä se, kuinka suuri osa liike-energiasta hävisi törmäyksessä. Vertaa kimmoisia ja täysin kimmottomia törmäyksiä toisiinsa epävarmuuksineen: kummassa liike-energiaa häviää enemmän, ja onko häviö kimmoisissa törmäyksissä nolla mittausepävarmuuden rajoissa? Mihin hävinnyt energia joutuu?

Johda lopuksi liikemäärän säilymislaista, kuinka suuri osa liike-energiasta säilyy täysin kimmottomassa törmäyksessä, kun vaunu 2 on aluksi levossa. Ilmaise tulos vaunujen massojen avulla ja vertaa sitä mittaamiisi arvoihin.

::: tuki O OO
**Vihjeitä.** Ratkaise ensin yhteinen nopeus $v'$ liikemäärän säilymislaista, kun $v_2 = 0$. Kirjoita sitten liike-energia ennen törmäystä ja sen jälkeen ja jaa jälkimmäinen edellisellä. Nopeus supistuu pois. Liike-energian epävarmuus on suhteellisesti suurempi kuin nopeuden, koska nopeus on kaavassa toisessa potenssissa: laske se ääriarvoilla samalla tavalla kuin liikemäärän.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella, myös anturien suunnat ja etumerkit?
- Perustuuko johtopäätöksesi mittaustuloksiin ja niiden epävarmuuksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
