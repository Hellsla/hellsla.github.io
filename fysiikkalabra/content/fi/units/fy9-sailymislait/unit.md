# Mekaaninen energia ja liikemäärä

> **Miksi** kaksi yhteen kytkeytyvää junanvaunua jatkavat hitaammin kuin ennen kytkeytymistä, vaikka mikään ei jarruta niitä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen ratapiha metsän keskellä kirkkaana päivänä. Vasemmalla punaruskea katettu tavaravaunu rullaa oikealle, ja sen takana on liikeviivoja. Oikealla seisoo samanlainen vaunu, johon rullaava vaunu on kohta kytkeytymässä. Raiteiden yllä on sähköradan pylväitä ja ajojohdin, taustalla kuusimetsää ja lumipenkkoja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sailymislait-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Mekaniikan kokeen tehtävistä suuri osa ratkeaa kahdella säilymislailla. **Energia säilyy aina**: mekaaninen energia muuttuu sisäenergiaksi, kun kitka, ilmanvastus tai kappaleen muodonmuutos tekee työtä, mutta kokonaisenergia pysyy samana. **Liikemäärä säilyy**, kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni.

```pysahdy
Milloin liikemäärä säilyy, ja miksi mekaaninen energia voi silti vähentyä?
---
Liikemäärä säilyy, kun ulkoisten voimien summa on nolla tai niiden impulssi on merkityksettömän pieni. Mekaaninen energia vähenee, kun kitka, ilmanvastus tai muodonmuutos muuttaa sitä sisäenergiaksi; kokonaisenergia säilyy.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Katso ensin tehtävän tunnusmerkki. Ei kitkaa, vain painovoima: mekaaninen energia säilyy, eli alun potentiaali- ja liike-energian summa on yhtä suuri kuin lopun. Kitka tai moottori tekee työtä: energiaperiaate, jossa alun mekaaniseen energiaan lisätään muiden voimien työ. Kappale liikkuu: liike-energia on puolet m v toiseen. Korkeus muuttuu: potentiaalienergia on m g h. Törmäys tai räjähdys: liikemäärä säilyy, ennen on yhtä suuri kuin jälkeen. Kimmoisa törmäys: myös liike-energia säilyy, sen muutos on nolla. Voima vaikuttaa tietyn ajan: impulssi on liikemäärän muutos. Teho tai hyötysuhde kysytään: hyötysuhde on antoteho jaettuna ottotehoon." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{ensin tunnusmerkki, sitten laki}$</div></foreignObject>
  <line x1="14" y1="149" x2="30" y2="149" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{ei kitkaa, vain painovoima}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{mekaaninen energia säilyy}$</div></foreignObject>
  <rect x="132" y="171" width="230" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="136" y="174" width="222" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$</div></foreignObject>
  <line x1="14" y1="265" x2="30" y2="265" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="214" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="224.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kitka tai moottori tekee työtä}$</div></foreignObject>
  <line x1="40" y1="254" x2="362" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="259" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{energiaperiaate}$</div></foreignObject>
  <rect x="72" y="287" width="290" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="76" y="290" width="282" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$</div></foreignObject>
  <line x1="14" y1="366" x2="30" y2="366" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="330" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="340.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kappale liikkuu}$</div></foreignObject>
  <line x1="40" y1="370" x2="362" y2="370" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="375" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{liike-energia}$</div></foreignObject>
  <rect x="238" y="374" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="376" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{k} = \tfrac12 mv^2$</div></foreignObject>
  <line x1="14" y1="452" x2="30" y2="452" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="416" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="426.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{korkeus muuttuu}$</div></foreignObject>
  <line x1="40" y1="456" x2="362" y2="456" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="461" width="198" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{potentiaalienergia}$</div></foreignObject>
  <rect x="256" y="460" width="106" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="260" y="462" width="98" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{p} = mgh$</div></foreignObject>
  <line x1="14" y1="553" x2="30" y2="553" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="502" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="512.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{törmäys tai räjähdys}$</div></foreignObject>
  <line x1="40" y1="542" x2="362" y2="542" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="547" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{liikemäärä säilyy}$</div></foreignObject>
  <rect x="152" y="575" width="210" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="156" y="578" width="202" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\overline{p}_\text{ennen} = \overline{p}_\text{jälkeen}$</div></foreignObject>
  <line x1="14" y1="654" x2="30" y2="654" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="618" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="628.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kimmoisa törmäys}$</div></foreignObject>
  <line x1="40" y1="658" x2="362" y2="658" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="663" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{liike-energia säilyy}$</div></foreignObject>
  <rect x="262" y="662" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="664" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta E_\text{k} = 0$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{voima vaikuttaa tietyn ajan}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{impulssi}$</div></foreignObject>
  <rect x="246" y="748" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="750" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\overline{I} = \Delta\overline{p}$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{teho tai hyötysuhde kysytään}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{hyötysuhde}$</div></foreignObject>
  <rect x="238" y="834" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="836" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = P_\text{a}/P_\text{o}$</div></foreignObject>
</svg>

Ratkaisu alkaa siitä, että valitset lain tilanteen mukaan. Kun kysytään nopeutta tai korkeutta eri kohdissa ja tunnetaan voimien tekemä työ, käytä energiaperiaatetta. Kun kappaleet törmäävät tai työntävät toisiaan, käytä liikemäärän säilymistä. Kun kysytään voimaa ja tunnetaan aika, käytä impulssiperiaatetta. Moni tehtävä yhdistää ne: ensin energia, sitten törmäys, sitten taas energia.

Tästä saadaan myös vastaus alun kysymykseen. Kytkeytymisessä vaunujen voimat toisiinsa ovat sisäisiä, joten liikemäärä $32\,000\,\text{kg} \cdot 1{,}6\,\text{m/s} = 51\,200\,\text{kg} \cdot \text{m/s}$ säilyy. Se jakautuu kaksinkertaiselle massalle, joten nopeus puolittuu, $0{,}80\,\text{m/s}$. Liike-energia $\tfrac12 mv^2$ pienenee silloin $41\,\text{kJ}$:sta $20\,\text{kJ}$:iin: puolet siitä muuttuu puskurien ja kytkimien sisäenergiaksi ja ääneksi.

<svg data-fig="tormays" viewBox="0 0 420 560" role="img" aria-label="Kaavakuva, nopeudet ja palkit mittakaavassa. Ylhäällä ennen törmäystä: vasen vaunu liikkuu oikealle nopeudella 1,6 m/s, sininen nuoli, ja oikea vaunu on levossa. Sen alla törmäyksen jälkeen: vaunut ovat kiinni toisissaan ja liikkuvat yhdessä nopeudella 0,80 m/s, puolet lyhyempi nuoli. Alhaalla palkit. Kokonaisliikemäärä on ennen ja jälkeen sama, 51 200 kilogrammametriä sekunnissa. Liike-energia on ennen 41 kJ ja jälkeen 20 kJ; puuttuva puolikas on muuttunut puskurien ja kytkimien sisäenergiaksi." style="max-width:100%;font-size:20px">
  <foreignObject x="8" y="10" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{ennen}$</div></foreignObject>
  <line x1="0" y1="130" x2="420" y2="130" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="20" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="42" cy="114" r="9" fill="#1f2933"/>
  <circle cx="108" cy="114" r="9" fill="#1f2933"/>
  <rect x="290" y="60" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="312" cy="114" r="9" fill="#1f2933"/>
  <circle cx="378" cy="114" r="9" fill="#1f2933"/>
  <line x1="75" y1="44" x2="222" y2="44" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,44 L221,50.5 L221,37.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="119.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$1{,}6\,\text{m/s}$</div></foreignObject>
  <foreignObject x="327" y="29" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$v = 0$</div></foreignObject>
  <foreignObject x="8" y="148" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{jälkeen}$</div></foreignObject>
  <line x1="0" y1="260" x2="420" y2="260" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="100" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="122" cy="244" r="9" fill="#1f2933"/>
  <circle cx="188" cy="244" r="9" fill="#1f2933"/>
  <rect x="214" y="190" width="110" height="46" rx="4" fill="#c8735f" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="236" cy="244" r="9" fill="#1f2933"/>
  <circle cx="302" cy="244" r="9" fill="#1f2933"/>
  <rect x="208" y="206" width="8" height="10" fill="#1f2933"/>
  <line x1="155" y1="176" x2="222" y2="176" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M235,176 L221,182.5 L221,169.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="290" y="152" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$0{,}80\,\text{m/s}$</div></foreignObject>
  <line x1="10" y1="500" x2="410" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="40" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="110" y="340" width="52" height="160" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="230" y="340" width="52" height="160" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="420" width="52" height="80" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="340" width="52" height="80" fill="#dee2e6" stroke="#1f2933" stroke-width="1.5" stroke-dasharray="6 4"/>
  <foreignObject x="76" y="280" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_\text{kok}$</div></foreignObject>
  <foreignObject x="241.5" y="280" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="40" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="101" y="512" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="230" y="512" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="291" y="512" width="70" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="260" y="312" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#6b7480">$\text{sisäenergiaksi}$</div></foreignObject>
  <foreignObject x="39.5" y="308" width="123" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$51\,200\,\text{kg} \cdot \text{m/s}$</div></foreignObject>
  <foreignObject x="230" y="410" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$41\,\text{kJ}$</div></foreignObject>
  <foreignObject x="300" y="450" width="52" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$20\,\text{kJ}$</div></foreignObject>
</svg>

## Kaava: Mekaaninen energia ja liikemäärä

### Energia

```kaavat
liike-energia :: E_\text{k} = \tfrac{1}{2}\,mv^2
painovoimaan liittyvä potentiaalienergia maanpinnalla :: E_\text{p} = mgh
```

missä $m$ on massa ($\text{kg}$), $v$ nopeus ($\text{m/s}$), $g = 9{,}81\,\text{m/s}^2$ ja $h$ korkeus valitusta nollatasosta ($\text{m}$). $E_\text{p} = mgh$ pätee Maan pinnan lähellä. Energiaperiaate on

```kaavat
mekaniikan energiaperiaate :: E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}
```

missä indeksi $0$ tarkoittaa alkutilaa ja $W$ muiden voimien kuin painon tekemä työ ($\text{J}$). Vakiovoiman työ on $W = F_\parallel\,s$, missä $F_\parallel$ on voiman liikkeen suuntainen komponentti; kitkan ja ilmanvastuksen työ on negatiivinen. Kun $W = 0$, mekaaninen energia säilyy: $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$.

```pysahdy
Mikä on kitkan tekemän työn etumerkki energiaperiaatteessa, ja miksi?
---
Kitkan työ on negatiivinen, $W < 0$, koska kitkavoima on liikkeen suuntaa vastaan. Siksi se pienentää mekaanista energiaa, joka muuttuu sisäenergiaksi.
```

### Liikemäärä ja impulssi

```kaavat
liikemäärä :: \overline{p} = m\overline{v}
voiman impulssi :: \overline{I} = \overline{F}\Delta t
impulssi-liikemääräperiaate :: \overline{I} = \Delta\overline{p}
```

missä $\overline{p}$ on liikemäärä ($\text{kg} \cdot \text{m/s}$), $\overline{I}$ impulssi ($\text{N} \cdot \text{s}$) ja $\overline{F}$ vakiosuuruinen voima aikavälin $\Delta t$ ajan. Liikemäärän muutoksen aiheuttaa kokonaisvoiman impulssi, $\Sigma\overline{F}\,\Delta t = \Delta\overline{p}$. Muuttuvalle voimalle keskimääräinen voima on $F_\text{ka} = |\Delta p| : \Delta t$. Yhdessä ulottuvuudessa valitaan positiivinen suunta, ja vastakkaiseen suuntaan osoittavat nopeudet ovat negatiivisia. Kun ulkoisten voimien impulssi on merkityksettömän pieni,

```latex
m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'
```

Kimmoisassa törmäyksessä myös liike-energia säilyy. Täysin kimmottomassa kappaleet jatkavat yhteisellä nopeudella, $v_1' = v_2' = v'$, ja liike-energiaa muuttuu eniten sisäenergiaksi.

```pysahdy
Kaksi kappaletta törmää kimmottomasti ja jatkaa yhdessä. Mikä säilyy ja mikä ei?
---
Liikemäärä säilyy, koska ulkoisten voimien impulssi on merkityksettömän pieni. Liike-energiaa muuttuu sisäenergiaksi, joten se ei säily.
```

### Sovellukset

Auton pysähtymismatka $s_\text{p}$ ($\text{m}$) vaakasuoralla tiellä on reaktiomatkan ja jarrutusmatkan summa. Reaktioajan $t_\text{r}$ ($\text{s}$) auto kulkee vakionopeudella $v_0$ ($\text{m/s}$), ja jarrutuksessa nopeus pienenee nollaan vakiohidastuvuudella $a$ ($\text{m/s}^2$); lukkojarrutuksen rajalla $a = \mu g$.

<svg data-fig="pysahtyminen" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei lukuarvoja: auton nopeus v ajan t funktiona. Reaktioajan t r nopeus pysyy lähtönopeutena v 0, joten kuvaaja on vaakasuora, ja sen alla on sininen suorakulmio, reaktiomatka s r. Sitten jarrutuksen aikana t j nopeus pienenee tasaisesti nollaan, joten kuvaaja on laskeva suora, ja sen alla on hiekanvärinen kolmio, jarrutusmatka s j. Auto pysähtyy hetkellä t r + t j." style="max-width:100%;font-size:24px">
  <line x1="89" y1="300" x2="484" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,300 L483,306 L483,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="90,300 90,127.5 185,127.5 185,300" fill="#d0e6fb" fill-opacity="0.9"/>
  <polygon points="185,300 185,127.5 394,300" fill="#f1dfb5" fill-opacity="0.9"/>
  <polyline points="185,300 185,127.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="90,127.5 185,127.5 394,300" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="45" y="113" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="168.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r}$</div></foreignObject>
  <foreignObject x="359" y="311.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r} + t_\text{j}$</div></foreignObject>
  <foreignObject x="121" y="199" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$s_\text{r}$</div></foreignObject>
  <foreignObject x="238" y="228" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{j}$</div></foreignObject>
  <foreignObject x="97" y="93.5" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{reaktio}$</div></foreignObject>
  <foreignObject x="306.5" y="161.5" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{jarrutus}$</div></foreignObject>
</svg>

```johda
Auton nopeus on $v_0$, kun kuljettaja huomaa esteen. Johda pysähtymismatka $s_\text{p}$, kun reaktioaika on $t_\text{r}$ ja jarrutuksen hidastuvuus $a$ on vakio.
---
Reaktioajan auto liikkuu tasaisella nopeudella. Paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä antaa kiihtyvyydellä nolla reaktiomatkan:

$$s_\text{r} = v_0\,t_\text{r}$$

Jarrutuksessa kiihtyvyys on $-a$. Nopeus tasaisesti kiihtyvässä liikkeessä antaa jarrutusajan $t_\text{j}$, kun loppunopeus on nolla:

$$0 = v_0 - a\,t_\text{j} \quad\Rightarrow\quad t_\text{j} = \frac{v_0}{a}$$

Sijoitetaan jarrutusaika paikan lausekkeeseen. Jarrutusmatka on

$$s_\text{j} = v_0\,t_\text{j} - \tfrac12\,a\,t_\text{j}^2 = \frac{v_0^2}{a} - \frac{v_0^2}{2a} = \frac{v_0^2}{2a}$$

Pysähtymismatka on reaktiomatkan ja jarrutusmatkan summa:

$$s_\text{p} = s_\text{r} + s_\text{j} = v_0\,t_\text{r} + \frac{v_0^2}{2a}$$

Saman jarrutusmatkan antaa energiaperiaate: Newtonin 2. lain mukaan jarruttava kokonaisvoima on $ma$, ja sen työ $-ma\,s_\text{j}$ vie koko liike-energian $\tfrac12 mv_0^2$. Kuvaajassa matkat ovat pinta-aloja: reaktiomatka on suorakulmio ja jarrutusmatka kolmio, jonka ala on $\tfrac12\,v_0 t_\text{j}$.
```

Vesivoimalan sähköteho $P_\text{vesi}$ ($\text{W}$) on osa siitä potentiaalienergiasta, jonka putoava vesi menettää aikayksikössä, ja hyötysuhde $\eta$ kertoo, kuinka suuri osa. Vettä, jonka tiheys on $\rho$ ($\text{kg/m}^3$), virtaa voimalan läpi virtaamalla $Q$ ($\text{m}^3\text{/s}$) eli tilavuus sekunnissa, ja se putoaa putouskorkeuden $h$ ($\text{m}$).

```johda
Vesivoimalan läpi virtaa vettä virtaamalla $Q$, ja putouskorkeus on $h$. Johda voimalan sähköteho $P_\text{vesi}$, kun hyötysuhde on $\eta$.
---
Ajassa $\Delta t$ voimalan läpi virtaa vettä tilavuus $V = Q\,\Delta t$. Tiheyden määritelmän $\rho = \tfrac{m}{V}$ mukaan sen massa on

$$m = \rho V = \rho Q\,\Delta t$$

Kun tämä vesi putoaa korkeuden $h$, sen painovoimaan liittyvä potentiaalienergia pienenee määrän

$$\Delta E = mgh = \rho Q\,\Delta t\,gh$$

Veden nopeus on putouksen alussa ja lopussa likimain sama, joten tämä energia tulee voimalalle. Teho on energian muutos aikayksikköä kohden, joten vesi tuo voimalaan tehon

$$P_\text{o} = \frac{\Delta E}{\Delta t} = \rho Qgh$$

Hyötysuhde $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ kertoo, mikä osa tästä tehosta saadaan sähkönä:

$$P_\text{vesi} = \eta P_\text{o} = \eta\rho Qgh$$
```

Tuulivoimalan sähköteho $P_\text{tuuli}$ ($\text{W}$) on vastaavasti osa siitä liike-energiasta, jonka ilma tuo roottorin läpi aikayksikössä. Ilma, jonka tiheys on $\rho$, virtaa nopeudella $v$ ($\text{m/s}$) kohtisuoraan roottorin pyyhkäisemän pinta-alan $A$ ($\text{m}^2$) läpi.

<svg data-fig="tuuli" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva sivulta, ei lukuarvoja. Oikealla tuulivoimala: torni, konehuone ja kolme lapaa. Roottorin pyyhkäisemä pinta-ala A on piirretty soikiona. Tuuli puhaltaa vasemmalta nopeudella v, siniset nuolet. Roottorin vasemmalla puolella on vaaleansininen ilmalieriö, jonka pohja on ala A ja pituus v kertaa delta t: se ilma, joka kulkee roottorin läpi ajassa delta t." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sailymislait-tuuli.webp" x="1.2" y="0" width="597" height="422.9" preserveAspectRatio="none"/>
  <foreignObject x="235" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="458" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="256" y="335.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v\,\Delta t$</div></foreignObject>
  <foreignObject x="146" y="44" width="143" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{ilmaa ajassa } \Delta t$</div></foreignObject>
</svg>

```johda
Tuuli puhaltaa nopeudella $v$ kohtisuoraan roottoria vastaan, ja roottorin pyyhkäisemä pinta-ala on $A$. Johda tuulivoimalan sähköteho $P_\text{tuuli}$, kun hyötysuhde on $\eta$.
---
Ajassa $\Delta t$ ilma kulkee matkan $v\,\Delta t$. Roottorin läpi kulkee siis ilmalieriö, jonka pohjan ala on $A$ ja pituus $v\,\Delta t$ (kuva). Tiheyden määritelmän mukaan sen massa on

$$m = \rho V = \rho A v\,\Delta t$$

Ilmalieriön liike-energia on

$$E_\text{k} = \tfrac12\,mv^2 = \tfrac12\,\rho A v\,\Delta t \cdot v^2$$

Sievennetään:

$$E_\text{k} = \tfrac12\,\rho A v^3\,\Delta t$$

Teho on energia aikayksikköä kohden, joten ilma tuo roottorille tehon

$$P_\text{o} = \frac{E_\text{k}}{\Delta t} = \tfrac12\,\rho A v^3$$

Hyötysuhteen $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ avulla sähköteho on

$$P_\text{tuuli} = \eta P_\text{o} = \tfrac12\,\eta\rho A v^3$$

Nopeus on kolmannessa potenssissa, koska nopeampi tuuli tuo roottorin läpi sekä enemmän ilmaa että enemmän energiaa jokaista ilmakilogrammaa kohden. Tulos olettaa hyötysuhteen vakioksi, joten se pätee, kun voimala toimii nimellistehoaan pienemmällä teholla.
```

## Yleisiä virheitä {Virheet}

- **Liike-energia ja liikemäärä sekaisin.** Törmäyksessä liikemäärä säilyy, liike-energia vain kimmoisassa törmäyksessä. Liikemäärä ei muutu sisäenergiaksi: sisäenergiaksi muuttuu liike-energiaa.
- **Etumerkit unohtuvat.** Kimpoava pallo muuttaa liikemääräänsä enemmän kuin pysähtyvä: samalla nopeudella kimpoavalle pallolle $\Delta p = -mv - mv = -2mv$.
- **Kitka katoaa energiaperiaatteesta.** Kitkan työ on negatiivinen, ja se muuttaa mekaanista energiaa sisäenergiaksi; se ei synnytä eikä hävitä energiaa.
- **Kilometrit tunnissa sijoitetaan suoraan.** $72\,\text{km/h} = 72 \cdot \tfrac{1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$, ennen kuin nopeus korotetaan toiseen.
- **Nopeuden neliö unohtuu.** Kaksinkertainen nopeus nelinkertaistaa liike-energian ja jarrutusmatkan, ja tuulen teho kasvaa kahdeksankertaiseksi.
- **Liikemäärän säilyminen ilman ehtoa.** Kerro, miksi ulkoiset voimat eivät muuta liikemäärää törmäyksen aikana.

## Kertaa tarvittaessa {Kertaa}

- Energialajit ja nollataso: [*Liike-energia, potentiaalienergia ja mekaaninen energia*](fy4-7.html). Työ ja energiaperiaate: [*Mekaanisen energian säilyminen ja energiaperiaate*](fy4-8.html).
- Voimalat: [*Vesi- ja tuulivoima energian muuntajina*](fy4-15.html).
- Liikemäärä, impulssi ja keskimääräinen voima: [*Liikemäärä ja impulssi*](fy4-9.html). Törmäykset: [*Liikemäärän säilyminen ja yksiulotteiset törmäykset*](fy4-10.html).
- Pysähtymismatka ja turvavarusteet: [*Liikenneturvallisuus: jarrutus, turvavyö ja turvatyyny*](fy4-11.html).
