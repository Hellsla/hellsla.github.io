# Energian muuntuminen ja yksikkö joule

> **Miksi** polkupyörä liikkuu, mistä sen energia on lopulta peräisin ja miten energian määrän voi kertoa yhdellä luvulla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Aurinko paistaa kultaiselle viljapellolle. Oranssit nuolet kulkevat Auringosta viljaan, viljasta leipään ja leivästä pyöräilijään. Pyöräilijä ajaa maantiellä. Liikkeen energia on siis peräisin Auringosta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
### Energia muuttuu muodosta toiseen
Energia on suure. Sen avulla kuvataan, mitä systeemissä eli tarkasteltavassa kohteessa voi tapahtua. Esimerkiksi liikkuvalla pyörällä on energiaa. Siksi se voi lämmittää jarrut, kun jarrutat. Energia esiintyy eri muodoissa. Muotoja ovat esimerkiksi mekaaninen energia, kemiallinen energia, sähköenergia, lämpöenergia, säteily ja ydinenergia (luku *Energialajit ja energian säilyminen*). Arjessa energia on harvoin vain yhdessä muodossa. Se muuttuu muodosta toiseen monessa vaiheessa. Vaiheet seuraavat toisiaan kuin ketjun lenkit. Siksi puhutaan **energiaketjusta**.

Pyöräilijän ketju alkaa Auringosta. Kasvi ottaa talteen Auringon säteilyenergiaa ja muuttaa sen kemialliseksi energiaksi. Kemiallinen energia päätyy kauraan ja aamupuuroon. Lihakset muuttavat osan puuron kemiallisesta energiasta pyörän liikkeeksi. Kun pysähdyt, liike-energia muuttuu lopulta renkaiden, jarrujen ja ilman lämpöenergiaksi.

<svg data-fig="ketju" viewBox="0 0 600 370" role="img" aria-label="Kaavakuva: energiaketju Auringosta pyöräilyyn. Aurinko lähettää säteilyenergiaa. Kasvi (kaura) sitoo sen kemialliseksi energiaksi ruokaan. Lihakset muuttavat osan siitä pyörän liikkeeksi. Loppu muuttuu lämpöenergiaksi. Joka vaiheessa osa energiasta siirtyy lämpönä ympäristöön (oranssit nuolet alas). Lopuksi myös liike-energia muuttuu lämpöenergiaksi. Nuolten pituus ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-2-ketju.webp" x="0" y="-1.2" width="600" height="377.5" preserveAspectRatio="none"/>
  <foreignObject x="136" y="29.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kasvi}$</div></foreignObject>
  <foreignObject x="5" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <foreignObject x="5" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{säteily}$</div></foreignObject>
  <foreignObject x="155" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Puuro}$</div></foreignObject>
  <foreignObject x="155" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="305" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Pyöräily}$</div></foreignObject>
  <foreignObject x="305" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{liike}$</div></foreignObject>
  <foreignObject x="455" y="157.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Ympäristö}$</div></foreignObject>
  <foreignObject x="455" y="191.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lämpö}$</div></foreignObject>
  <foreignObject x="150" y="307.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpöä ympäristöön}$</div></foreignObject>
</svg>

Joka vaiheessa osa energiasta muuttuu lämpöenergiaksi. Lämpöenergia siirtyy lämpönä ympäristöön ja hajaantuu. Energiaa ei silti katoa. Luvussa *Energialajit ja energian säilyminen* todettiin, että ketjun alussa ja lopussa energiaa on yhtä paljon. Kuvan esimerkissä puuron $800\,\text{kJ}$ jakautuu liikkeeksi ja lämpöenergiaksi. Osat ovat yhteensä yhtä paljon kuin alussa. Lämpöenergia hajaantuu niin laajalle, ettei sitä ole enää helppo käyttää hyödyksi. Siksi energia tuntuu "kuluvan loppuun".

<svg data-fig="sailyminen" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva mittakaavassa (esimerkki): pyöräilijän aamupuuron kemiallisesta energiasta on 800 kJ. Lihakset muuttavat siitä liikkeeksi 200 kJ ja lämpöenergiaksi 600 kJ. Nuolten leveys on verrannollinen energiaan. Haarojen yhteinen leveys on yhtä suuri kuin alkuperäisen nuolen leveys." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-2-sailyminen.webp" x="0" y="0" width="600" height="358.8" preserveAspectRatio="none"/>
  <foreignObject x="100" y="23.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800\,\text{kJ} = 200\,\text{kJ} + 600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="61" y="117.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="61" y="153.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800\,\text{kJ}$</div></foreignObject>
  <foreignObject x="290" y="59.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{liike: }200\,\text{kJ}$</div></foreignObject>
  <foreignObject x="290" y="281.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö: }600\,\text{kJ}$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="460" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nuolen leveys kuvaa energian määrää}$</div></foreignObject>
</svg>

```pysahdy
Puurosta saatavasta $500\,\text{kJ}$:sta lihakset muuttavat liikkeeksi $120\,\text{kJ}$. Kuinka paljon energiaa muuttuu lämpöenergiaksi? Onko se sen jälkeen kadonnut?
---
Lämpöenergiaksi muuttuu $500\,\text{kJ} - 120\,\text{kJ} = 380\,\text{kJ}$. Energiaa ei ole kadonnut. Se on hajaantunut lämpöenergiana ympäristöön.
```

### Joule
Energian symboli on $E$. Energian yksikkö on joule, ja sen merkki on J. Yksi joule on pieni energia. Sen verran energiaa tarvitaan suunnilleen siihen, että nostat omenan metrin verran ylöspäin. Omena painaa noin $0{,}1\,\text{kg}$. Tässä luvussa opit joulen suuruuden esimerkkien avulla.

<figure class="unit-photo"><img src="pics/fy2/artemis-i-launch.webp" alt="Raketti nousee yöllä. Sen alla on kirkas liekki ja iso savupilvi."><figcaption>Artemis I -raketti lähti Floridasta marraskuussa 2022. Polttoaineen kemiallinen energia muuttuu liike-energiaksi, lämpöenergiaksi, valoksi ja ääneksi.</figcaption></figure>

## Kaava: Energian yksikkö ja kerrannaisyksiköt
Arjen energiat ovat jouleina isoja lukuja. Siksi käytetään etuliitteitä (luku *Suureet, yksiköt ja SI-järjestelmä*): kilo (k), mega (M), giga (G) ja tera (T). Jokainen etuliite on tuhatkertainen edelliseen verrattuna:
```latex
\begin{aligned}
1\,\text{kJ} &= 1000\,\text{J} \\
1\,\text{MJ} &= 1000\,\text{kJ} \\
1\,\text{GJ} &= 1000\,\text{MJ} \\
1\,\text{TJ} &= 1000\,\text{GJ}
\end{aligned}
```
missä J on joule, kJ kilojoule, MJ megajoule, GJ gigajoule ja TJ terajoule. Megajoulessa on siis $1000 \cdot 1000\,\text{J} = 1\,000\,000\,\text{J}$.

Muunnos tehdään näin: korvaa etuliite sen arvolla. Esimerkki: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J} = 2500\,\text{J}$. Toiseen suuntaan luku kirjoitetaan etuliitteen avulla: $3000\,\text{J} = 3 \cdot 1000\,\text{J} = 3\,\text{kJ}$. Energioita lasketaan yhteen vain samassa yksikössä. Muunna ne siis ensin samaan yksikköön.

```pysahdy
Kuinka monta joulea on $4{,}2\,\text{kJ}$? Kuinka monta megajoulea on $3000\,\text{kJ}$?
---
$4{,}2\,\text{kJ} = 4{,}2 \cdot 1000\,\text{J} = 4200\,\text{J}$. Koska $1\,\text{MJ} = 1000\,\text{kJ}$, niin $3000\,\text{kJ} = 3\,\text{MJ}$.
```

Arjen energioiden suuruusluokat on koottu kuvaan. Kuvassa jokainen pieni väli on kymmenkertainen ja jokainen merkitty väli tuhatkertainen (luku *Fysiikka tieteenä ja maailmankaikkeuden mittasuhteet*). Joskus kahden energian suuruusluokka on hyvin erilainen. Silloin vertailuun riittää yksi jakolasku. Esimerkki: bensiinilitran $32\,\text{MJ}$ ja päivän ruoan $10\,\text{MJ}$ suhde on $32\,\text{MJ} : 10\,\text{MJ} \approx 3$.

<svg data-fig="tikapuut" viewBox="0 0 600 372" role="img" aria-label="Kuvaaja mittakaavassa: energia jouleina kymmenpotenssiasteikolla 1 J:sta 10 TJ:iin ja yli. Jokainen pieni väli on kymmenkertainen ja jokainen merkitty väli tuhatkertainen. Omena metrin ylös on noin 1 J. Palava tulitikku on noin 1 kJ. Päivän ruoka on noin 10 MJ. 50 litran bensiinitankki on noin 1,6 GJ. Ydinvoimala Olkiluoto 3 tuottaa vuorokaudessa noin 140 TJ sähköä." style="max-width:100%;font-size:24px">
  <line x1="66" y1="292" x2="574" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,292 L573,298 L573,286 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="292" x2="96" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="129" y1="292" x2="129" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="162.5" y1="292" x2="162.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="195.5" y1="292" x2="195.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="229" y1="292" x2="229" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="262" y1="292" x2="262" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="295" y1="292" x2="295" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="328.5" y1="292" x2="328.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361.5" y1="292" x2="361.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="292" x2="395" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428" y1="292" x2="428" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="292" x2="461" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="494.5" y1="292" x2="494.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="527.5" y1="292" x2="527.5" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="561" y1="292" x2="561" y2="298" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="51" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{J}$</div></foreignObject>
  <foreignObject x="150.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="250" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{MJ}$</div></foreignObject>
  <foreignObject x="350" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{GJ}$</div></foreignObject>
  <foreignObject x="449.5" y="307.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{TJ}$</div></foreignObject>
  <foreignObject x="80" y="339.5" width="440" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{pieni väli ×10, merkitty väli ×1000}$</div></foreignObject>
  <line x1="96" y1="30" x2="96" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="96" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="106" y="27.5" width="234" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{omena metrin ylös}$</div></foreignObject>
  <foreignObject x="106" y="55.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1\,\text{J}$</div></foreignObject>
  <line x1="565.5" y1="30" x2="565.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="565.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="347.5" y="27.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Olkiluoto 3, vrk}$</div></foreignObject>
  <foreignObject x="445.5" y="55.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$140\,\text{TJ}$</div></foreignObject>
  <line x1="401.5" y1="92" x2="401.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="401.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="171.5" y="89.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{bensiinitankki}$</div></foreignObject>
  <foreignObject x="281.5" y="117.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}6\,\text{GJ}$</div></foreignObject>
  <line x1="328.5" y1="154" x2="328.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="328.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="118.5" y="151.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{päivän ruoka}$</div></foreignObject>
  <foreignObject x="208.5" y="179.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10\,\text{MJ}$</div></foreignObject>
  <line x1="195.5" y1="216" x2="195.5" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="195.5" cy="292" r="7" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="205.5" y="213.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tulitikku}$</div></foreignObject>
  <foreignObject x="205.5" y="241.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1\,\text{kJ}$</div></foreignObject>
</svg>

```pysahdy
Bensiinitankin energia on noin $1{,}6\,\text{GJ}$. Päivän ruoan energia on noin $10\,\text{MJ}$. Kuinka moninkertainen tankin energia on ruoan energiaan verrattuna?
---
Muunna ensin samaan yksikköön: $1{,}6\,\text{GJ} = 1600\,\text{MJ}$. Suhde on $1600\,\text{MJ} : 10\,\text{MJ} = 160$. Tankissa on noin 160-kertainen energia.
```

Energian määrä ei vielä kerro, kuinka nopeasti energiaa käytetään. Sitä kuvataan seuraavassa luvussa *Teho*.

## Esimerkki
Pyöräilijä syö banaanin. Banaanin kemiallinen energia on $0{,}45\,\text{MJ}$. Lihakset muuttavat siitä pyöräilyn liikkeeksi $110\,\text{kJ}$. Loppu muuttuu lämpöenergiaksi. Kuinka paljon energiaa muuttuu lihaksissa ja kehossa lämpöenergiaksi? Anna vastaus kilojouleina.

<!-- vaihe -->

**Tunnetut ja kysytty.** Kemiallinen energia alussa on $E_\text{alussa} = 0{,}45\,\text{MJ}$. Liikkeeksi muuttunut energia on $E_\text{liike} = 110\,\text{kJ}$.

Kysytään lämpöenergiaa $E_\text{lämpö}$ kilojouleina.

<!-- vaihe -->

**Periaate.** Energia säilyy. Banaanin kemiallinen energia ei katoa. Se muuttuu kokonaan liikkeeksi ja lämpöenergiaksi. Alun energia on siis yhtä suuri kuin liikkeeksi ja lämpöenergiaksi muuttuneiden energioiden summa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E_\text{alussa} = E_\text{liike} + E_\text{lämpö} \\
&E_\text{lämpö} = E_\text{alussa} - E_\text{liike}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Energiat lasketaan samassa yksikössä. Korvaa megajoulen etuliite sen arvolla: $0{,}45\,\text{MJ} = 0{,}45 \cdot 1000\,\text{kJ} = 450\,\text{kJ}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E_\text{lämpö} &= E_\text{alussa} - E_\text{liike} \\
&= 450\,\text{kJ} - 110\,\text{kJ} \\
&= 340\,\text{kJ}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lämpöenergiaksi muuttuu $340\,\text{kJ}$. Vähennyslaskussa tarkkuuden ratkaisee epätarkin tieto. Alkuenergia $0{,}45\,\text{MJ} = 450\,\text{kJ}$ on tunnettu kymmenen kilojoulen tarkkuudella. Siksi erotus ilmoitetaan kymmenen kilojoulen tarkkuudella ja pyöristetään tulokseen $340\,\text{kJ}$.

<!-- vaihe -->

**Järkevyys.** Lämpöenergiaksi muuttuu enemmän energiaa kuin liikkeeksi. Näin on ihmisen lihasten toiminnassa yleensä: keho lämpenee pyöräillessä. Summa tarkistuu: $110\,\text{kJ} + 340\,\text{kJ} = 450\,\text{kJ}$. Se on sama kuin alussa.

## Yleinen virhekäsitys
Moni ajattelee, että energia kuluu loppuun, kun vauhti hidastuu tai akku tyhjenee. Energia ei kulu eikä katoa. Se muuttaa muotoa. Suuri osa päätyy lämpönä ympäristöön. Sitä ei enää helposti saa sieltä takaisin hyötykäyttöön.

Toinen virhe on laskea yhteen energioita eri yksiköissä. Esimerkiksi $1{,}5\,\text{MJ} + 300\,\text{kJ} = 301{,}5$ on väärin. Etuliite on kerroin. Muunna energiat siis ensin samaan yksikköön.

## Tiivistelmä
- Energia muuttuu ketjussa muodosta toiseen, esimerkiksi säteily, kemiallinen energia, liike-energia ja lämpöenergia.
- Energia säilyy (luku *Energialajit ja energian säilyminen*). Osa muuttuu joka vaiheessa lämpöenergiaksi, ja lämpöenergia siirtyy lämpönä ympäristöön.
- Energian yksikkö on joule (J). Etuliitteet: $1\,\text{kJ} = 1000\,\text{J}$, $1\,\text{MJ} = 1000\,\text{kJ}$, $1\,\text{GJ} = 1000\,\text{MJ}$ ja $1\,\text{TJ} = 1000\,\text{GJ}$.
- Etuliite korvataan arvollaan: $2{,}5\,\text{kJ} = 2{,}5 \cdot 1000\,\text{J}$. Energioita lasketaan yhteen samassa yksikössä.
- Arjen energiat ovat jouleista terajouleihin. Vertailu tehdään kymmenpotensseina.
