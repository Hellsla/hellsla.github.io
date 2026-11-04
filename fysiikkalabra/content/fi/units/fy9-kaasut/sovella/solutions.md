## fy9-kaasut-s1

### a)
**Annettu:** männän halkaisija $d = 0{,}200\,\text{m}$, auton ja lavan massa $m = 1800\,\text{kg}$, ulkoilman paine $p_0 = 101\,\text{kPa}$, nosto tasaisella nopeudella; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** sylinterin ylipaine $\Delta p$ eli sylinterin ilman ja ulkoilman paine-ero kilopascaleina
**Periaate:** Lava liikkuu tasaisella nopeudella, joten siihen vaikuttavat voimat ovat tasapainossa (luku *Newtonin toinen laki*). Männän alapuolelta sylinterin ilma työntää mäntää ylös voimalla $pA$ ja yläpuolelta ulkoilma alas voimalla $p_0A$. Niiden erotus $\Delta p\,A$ kannattaa painon $mg$. Paineen voima on kohtisuorassa männän pintaa vastaan eli pystysuora (luku *Paine ja hydrostaattinen paine*).
**Kaava:** $\Delta p\,A = mg$ ja $A = \pi r^2 = \pi \left(\dfrac{d}{2}\right)^2$, joten $\Delta p = \dfrac{mg}{\pi (d/2)^2}$
**Muunnokset:** Säde $r = 0{,}200\,\text{m} : 2 = 0{,}100\,\text{m}$. Lopuksi $1\,\text{Pa} = 0{,}001\,\text{kPa}$.
**Sijoitus:** $A = \pi \cdot (0{,}100\,\text{m})^2 = 0{,}031\,42\,\text{m}^2$, $mg = 1800\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 17\,658\,\text{N}$ ja $\Delta p = \dfrac{17\,658\,\text{N}}{0{,}031\,42\,\text{m}^2} = 562\,100\,\text{Pa} = 562\,\text{kPa}$
**Vastaus:** $\Delta p \approx 562\,\text{kPa}$, kolme merkitsevää numeroa kuten halkaisija $0{,}200\,\text{m}$.
**Järkevyys:** Ylipaine on pienempi kuin säiliön $900\,\text{kPa}$, joten säiliön ilma jaksaa työntää mäntää. Suuruusluokka: $18\,\text{kN}$ noin $0{,}03\,\text{m}^2$:n alalle on noin $600\,\text{kPa}$.

### b)
**Annettu:** $m = 1800\,\text{kg}$, nostokorkeus $h = 1{,}20\,\text{m}$, a-kohdan $\Delta p = 562{,}1\,\text{kPa}$ ja $A = 0{,}031\,42\,\text{m}^2$, ulkoilman paine $p_0 = 101\,\text{kPa}$
**Kysytty:** nostimen autoon ja lavaan tekemä työ $W$ kilojouleina, sama työ paine-erosta, ja miksi ilma tekee enemmän työtä
**Periaate:** Lava nousee tasaisella nopeudella, joten mäntä tekee siihen nostotyön, joka on voima kertaa matka (luku *Työ ja energia*). Voima on $\Delta p\,A$, ja $Ah$ on sylinterin ilman tilavuuden muutos, joten sama työ on $\Delta p\,\Delta V$. Sylinterin ilma itse työntää mäntää kokonaispaineella, ja sen työ on $p\,\Delta V$ (luku *Kaasun tekemä työ ja lämpövoimakone*).
**Kaava:** $W = mgh$ ja $W = \Delta p\,A h = \Delta p\,\Delta V$; ilman työ $W_\text{k} = (p_0 + \Delta p)\,\Delta V$
**Muunnokset:** $\Delta V = Ah = 0{,}031\,42\,\text{m}^2 \cdot 1{,}20\,\text{m} = 0{,}037\,70\,\text{m}^3 = 37{,}7\,\textsf{l}$, ja $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$.
**Sijoitus:** $W = 1800\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 1{,}20\,\text{m} = 21\,190\,\text{J}$ ja $\Delta p\,\Delta V = 562{,}1\,\text{kPa} \cdot 37{,}70\,\textsf{l} = 21\,190\,\text{J}$. Ilman työ $W_\text{k} = 663{,}1\,\text{kPa} \cdot 37{,}70\,\textsf{l} = 25\,000\,\text{J}$, josta $p_0\,\Delta V = 101\,\text{kPa} \cdot 37{,}70\,\textsf{l} = 3810\,\text{J}$.
**Vastaus:** $W \approx 21{,}2\,\text{kJ}$, kolme merkitsevää numeroa kuten nostokorkeus $1{,}20\,\text{m}$. Sylinterin ilma tekee työn $25{,}0\,\text{kJ}$, koska se työntää mäntää kokonaispaineella. Männän yläpuolella on ulkoilmaa, ja noston aikana mäntä työntää sitä pois tieltä: siihen kuluu $3{,}8\,\text{kJ}$, ja vain loput nostavat autoa.
**Järkevyys:** Kaksi eri tapaa antaa saman tuloksen, koska $\Delta p\,A$ on juuri painon suuruinen. Tulos on yhtä suuri kuin auton potentiaalienergian kasvu.

### c)
**Annettu:** säiliön tilavuus $V_\text{s} = 100\,\textsf{l}$, säiliön ylipaine aluksi $900\,\text{kPa}$, sylinterin kokonaispaine noston aikana $p_\text{c} = 101\,\text{kPa} + 562\,\text{kPa} = 663\,\text{kPa}$, sylinteriin tuleva tilavuus $\Delta V = 37{,}7\,\textsf{l}$; lämpötila vakio
**Kysytty:** säiliön mittarin lukema $\Delta p_2$ yhden noston jälkeen ja riittääkö ilma toiseen nostoon
**Periaate:** Ilmaa ei katoa: säiliön ilma jakautuu säiliöön ja sylinteriin. Vakiolämpötilassa saman ilmamäärän tulo $pV$ pysyy samana (luku *Kaasujen tilanmuutokset ja Boylen laki*), joten säiliön alkuperäisen ilman $pV$ on säiliöön jäävän ja sylinteriin siirtyneen ilman $pV$:n summa. Laskuissa käytetään kokonaispaineita. Ilma virtaa vain suuremmasta paineesta pienempään, joten nosto jatkuu vain niin kauan kuin säiliön paine on vähintään $p_\text{c}$.
**Kaava:** $p_1V_\text{s} = p_2V_\text{s} + p_\text{c}\,\Delta V$, joten $p_2 = p_1 - \dfrac{p_\text{c}\,\Delta V}{V_\text{s}}$ ja $\Delta p_2 = p_2 - p_0$
**Muunnokset:** Kokonaispaine aluksi $p_1 = 900\,\text{kPa} + 101\,\text{kPa} = 1001\,\text{kPa}$. Litrat supistuvat.
**Sijoitus:** $p_2 = 1001\,\text{kPa} - \dfrac{663{,}1\,\text{kPa} \cdot 37{,}70\,\textsf{l}}{100\,\textsf{l}} = 1001\,\text{kPa} - 250{,}0\,\text{kPa} = 751{,}0\,\text{kPa}$ ja $\Delta p_2 = 751{,}0\,\text{kPa} - 101\,\text{kPa} = 650\,\text{kPa}$. Toisen täyden noston jälkeen paine olisi $751{,}0\,\text{kPa} - 250{,}0\,\text{kPa} = 501\,\text{kPa}$.
**Vastaus:** Mittari näyttää noin $650\,\text{kPa}$, kolme merkitsevää numeroa kuten säiliön ja sylinterin luvut. Ilma ei riitä toiseen nostoon: säiliön paine putoaisi alle sylinterin tarvitseman $663\,\text{kPa}$:n, kun säiliöstä on mennyt sylinteriin $\dfrac{(751{,}0 - 663{,}1)\,\text{kPa} \cdot 100\,\textsf{l}}{663{,}1\,\text{kPa}} \approx 13{,}3\,\textsf{l}$ eli lava on noussut noin $13{,}3\,\textsf{l} : 31{,}4\,\textsf{l/m} \approx 0{,}42\,\text{m}$. Lava pysähtyy siihen, kunnes kompressori käynnistyy. Malli olettaa lämpötilan vakioksi. Todellisuudessa säiliöstä purkautuva ilma jäähtyy laajetessaan, joten paine on hetkellisesti vielä laskettua pienempi ja nosto jää aikaisemmin kesken.
**Järkevyys:** Yksi nosto vie säiliön paineesta $250\,\text{kPa}$, eli neljänneksen, koska sylinteriin siirtyvän ilman $pV$ on $663 \cdot 37{,}7 \approx 25\,000\,\text{kPa}\cdot\textsf{l}$ ja säiliön alkuperäinen $pV$ on noin $100\,000\,\text{kPa}\cdot\textsf{l}$.

### Yleisiä virheitä
- a-kohdassa pinta-ala lasketaan halkaisijasta säteen sijasta, jolloin ylipaine tulee neljäsosaan.
- a-kohdan ylipaine sijoitetaan c-kohdan Boylen lakiin kokonaispaineen sijasta, tai säiliön mittarin lukema $900\,\text{kPa}$ käytetään ilman ilmanpainetta.
- b-kohdassa ilman työ $p\,\Delta V$ lasketaan kokonaispaineella ja sitä pidetään auton saamana energiana.
- c-kohdassa unohdetaan, että ilma ei virtaa säiliöstä sylinteriin, kun säiliön paine on pienempi kuin sylinterin.

### Hyväksytään myös
- c-kohdassa laskun voi tehdä ainemäärillä $n = pV/(RT)$; lämpötila supistuu, ja tulos on sama.

## fy9-kaasut-s2

### a)
**Annettu:** metaanin tilavuus tunnissa $V = 52{,}0\,\text{m}^3$, lämpötila $\theta = 25\,{}^\circ\text{C}$, paine $p = 104\,\text{kPa}$, moolimassa $M = 16{,}0\,\text{g/mol}$; $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Kysytty:** tunnissa poltetun metaanin massa $m$ kilogrammoina
**Periaate:** Mittarin kohdalla metaani on tavallisessa paineessa ja lämpötilassa, joten sitä voi kuvata ideaalikaasuna. Tilanyhtälöstä saadaan tunnissa virtaavan kaasun ainemäärä ja moolimassasta sen massa (luku *Ideaalikaasun tilanyhtälö $pV = nRT$*).
**Kaava:** $pV = nRT$ ja $n = \dfrac{m}{M}$, joten $m = \dfrac{pVM}{RT}$
**Muunnokset:** $p = 104 \cdot 1000\,\text{Pa} = 104\,000\,\text{Pa}$, $T = (25 + 273{,}15)\,\text{K} = 298{,}15\,\text{K}$ ja $M = 16{,}0 \cdot 0{,}001\,\text{kg/mol} = 0{,}0160\,\text{kg/mol}$
**Sijoitus:** $n = \dfrac{104\,000\,\text{Pa} \cdot 52{,}0\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 298{,}15\,\text{K}} = 2183\,\text{mol}$ ja $m = 2183\,\text{mol} \cdot 0{,}0160\,\tfrac{\text{kg}}{\text{mol}} = 34{,}9\,\text{kg}$
**Vastaus:** $m \approx 34{,}9\,\text{kg}$ tunnissa, kolme merkitsevää numeroa kuten tilavuus $52{,}0\,\text{m}^3$ ja moolimassa $16{,}0\,\text{g/mol}$.
**Järkevyys:** Metaanin tiheys on $34{,}9\,\text{kg} : 52{,}0\,\text{m}^3 \approx 0{,}67\,\text{kg/m}^3$, pienempi kuin ilman noin $1{,}2\,\text{kg/m}^3$, kuten moolimassojen suhde $16 : 29$ ennustaa.

### b)
**Annettu:** a-kohdan $m = 34{,}92\,\text{kg}$ ajassa $t = 1\,\text{h}$, lämpöarvo $H = 50{,}0\,\text{MJ/kg}$, sähköhyötysuhde $\eta_\text{s} = 36\,\%$
**Kysytty:** sähköteho $P_\text{s}$ kilowatteina
**Periaate:** Polttoaineteho on palamisessa vapautuva energia aikaa kohti, ja sähköhyötysuhde kertoo, kuinka suuri osa siitä saadaan sähkönä (luku *Energiantuotanto ja voimalaitosten hyötysuhde*).
**Kaava:** $P_0 = \dfrac{Hm}{t}$ ja $\eta_\text{s} = \dfrac{P_\text{s}}{P_0}$, joten $P_\text{s} = \dfrac{\eta_\text{s} H m}{t}$
**Muunnokset:** $H = 50{,}0 \cdot 10^{6}\,\text{J/kg}$, $t = 1\,\text{h} = 3600\,\text{s}$ ja $36\,\% = 0{,}36$
**Sijoitus:** $Hm = 50{,}0 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}} \cdot 34{,}92\,\text{kg} = 1{,}746 \cdot 10^{9}\,\text{J}$, $P_0 = \dfrac{1{,}746 \cdot 10^{9}\,\text{J}}{3600\,\text{s}} = 485\,100\,\text{W}$ ja $P_\text{s} = 0{,}36 \cdot 485{,}1\,\text{kW} = 174{,}6\,\text{kW}$
**Vastaus:** $P_\text{s} \approx 175\,\text{kW}$, kolme merkitsevää numeroa kuten massa; hyötysuhde $36\,\%$ on annettu kahdella numerolla, joten $170$–$180\,\text{kW}$ on yhtä hyvä vastaus.
**Järkevyys:** Polttoaineteho on noin $0{,}5\,\text{MW}$, ja sähköä saadaan reilu kolmannes, kuten pienessä moottorivoimalassa. Teho riittäisi kymmenien omakotitalojen sähkönkulutukseen.

### c)
**Annettu:** $P_0 = 485{,}1\,\text{kW}$, $P_\text{s} = 174{,}6\,\text{kW}$, lämmöstä talteen $75\,\%$
**Kysytty:** miksi kaikkea polttoainetehoa ei saada sähköksi, ja kokonaishyötysuhde $\eta_\text{kok}$
**Periaate:** Moottori on lämpövoimakone. Se voi muuttaa lämpöä työksi vain, jos se luovuttaa osan lämmöstä kylmempään ympäristöön: pakokaasujen ja jäähdytysveden mukana (luku *Kaasun tekemä työ ja lämpövoimakone*). Energia säilyy, joten luovutettu lämpöteho on polttoainetehon ja sähkötehon erotus. Kokonaishyötysuhteessa hyödyksi lasketaan sähkö ja talteen otettu lämpö.
**Kaava:** $P_2 = P_0 - P_\text{s}$, $P_\text{l} = 0{,}75\,P_2$ ja $\eta_\text{kok} = \dfrac{P_\text{s} + P_\text{l}}{P_0}$
**Muunnokset:** Ei tarvita: tehot ovat kilowatteina, ja $75\,\% = 0{,}75$.
**Sijoitus:** $P_2 = 485{,}1\,\text{kW} - 174{,}6\,\text{kW} = 310{,}5\,\text{kW}$, $P_\text{l} = 0{,}75 \cdot 310{,}5\,\text{kW} = 232{,}9\,\text{kW}$ ja $\eta_\text{kok} = \dfrac{174{,}6\,\text{kW} + 232{,}9\,\text{kW}}{485{,}1\,\text{kW}} = 0{,}840$
**Vastaus:** $\eta_\text{kok} \approx 84\,\%$, kaksi merkitsevää numeroa kuten hyötysuhteet $36\,\%$ ja $75\,\%$. Kitkattomankin moottorin on luovutettava lämpöä kylmempään, joten sähkön osuus jää selvästi alle $100\,\%$:n. Kokonaishyötysuhde on suuri, koska luovutettu lämpö käytetään lämmitykseen; sähköä ei saada siitä yhtään enempää.
**Järkevyys:** Hukaksi jää $485\,\text{kW} - 175\,\text{kW} - 233\,\text{kW} \approx 78\,\text{kW}$ eli $16\,\%$, sama kuin $25\,\%$ lämpötehosta. Tulos on samaa suuruusluokkaa kuin yhteistuotantolaitosten $85$–$90\,\%$.

### Yleisiä virheitä
- a-kohdassa lämpötila sijoitetaan celsiusasteina, jolloin ainemääräksi tulee yli kymmenkertainen $26\,000\,\text{mol}$.
- Moolimassa jätetään grammoiksi, jolloin massaksi tulee tuhatkertainen luku.
- b-kohdassa tunnissa vapautuva energia megajouleina tulkitaan suoraan tehoksi jakamatta sekunneilla.
- c-kohdassa vastataan, että sähköä ei saada enempää ”kitkan takia”; kitkan poistaminen ei poista lämpöä, jonka lämpövoimakone luovuttaa kylmempään.

### Hyväksytään myös
- b-kohdassa sähkötehon voi laskea myös energiana tunnissa: $0{,}36 \cdot 1746\,\text{MJ} \approx 629\,\text{MJ}$ tunnissa, ja $629\,\text{MJ} : 3600\,\text{s} \approx 175\,\text{kW}$.

## fy9-kaasut-s3

### a)
**Kysytty:** ilman tilavuus $V$ lämpötilan $\theta$ funktiona kuvaajana ja siihen sovitettu malli
**Kuvaaja:** Vaaka-akselilla on lämpötila $\theta\ ({}^\circ\text{C})$ ja pystyakselilla tilavuus $V\ (\text{ml})$. Pystyakseli alkaa tässä $36\,\text{ml}$:sta, jotta pisteiden vaihtelu näkyy; b-kohdan jatkamista varten piirretään toinen kuvaaja, jossa akselit alkavat nollasta. Jokaiseen pisteeseen on merkitty epävarmuusjana $\pm 0{,}3\,\text{ml}$.

<svg data-fig="fy9-kaasut-s3-graph" viewBox="0 0 420 360" role="img" aria-label="Kuvaaja: ruiskun ilman tilavuus V lämpötilan θ funktiona, kun θ on 0–80 °C. Pystyakseli alkaa 36 millilitrasta. Kahdeksan mustaa pistettä lämpötiloissa 5, 15, …, 75 °C, ja jokaisella pystysuora epävarmuusjana ±0,3 ml. Pisteisiin on sovitettu nouseva suora, joka kulkee pisteiden lomitse. Suoralta on ympyröity kaksi kaukana toisistaan olevaa pistettä, (0 °C; 37,7 ml) ja (80 °C; 48,5 ml), joista kulmakerroin luetaan: noin 0,135 ml asteelta." style="max-width:100%;font-size:24px">
  <line x1="94" y1="306" x2="94" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="125.5" y1="306" x2="125.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="157" y1="306" x2="157" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189" y1="306" x2="189" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="221" y1="306" x2="221" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="252.5" y1="306" x2="252.5" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="284" y1="306" x2="284" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316" y1="306" x2="316" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="271" x2="316" y2="271" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="236.5" x2="316" y2="236.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="201.5" x2="316" y2="201.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="166.5" x2="316" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="131.5" x2="316" y2="131.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="97" x2="316" y2="97" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="62" x2="316" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="61" y1="306" x2="330" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M342,306 L329,312 L329,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="62" y1="307" x2="62" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,36 L68,49 L56,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="94" y1="306" x2="94" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="125.5" y1="306" x2="125.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="157" y1="306" x2="157" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="189" y1="306" x2="189" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="221" y1="306" x2="221" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="252.5" y1="306" x2="252.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="284" y1="306" x2="284" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="316" y1="306" x2="316" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="55" y1="271" x2="62" y2="271" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="236.5" x2="62" y2="236.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="222" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="55" y1="201.5" x2="62" y2="201.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="166.5" x2="62" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="152" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$44$</div></foreignObject>
  <line x1="55" y1="131.5" x2="62" y2="131.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="55" y1="97" x2="62" y2="97" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="17" y="82.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="55" y1="62" x2="62" y2="62" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="52" y="5.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <polyline points="62,276 316,88" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="78" y1="273" x2="78" y2="262.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="74" y1="273" x2="82" y2="273" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="74" y1="262.5" x2="82" y2="262.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="78" cy="267.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="109.5" y1="243.5" x2="109.5" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="105.5" y1="243.5" x2="113.5" y2="243.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="105.5" y1="233" x2="113.5" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="109.5" cy="238" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="141.5" y1="222.5" x2="141.5" y2="212" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="222.5" x2="145.5" y2="222.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="137.5" y1="212" x2="145.5" y2="212" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="141.5" cy="217" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="173" y1="198" x2="173" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="169" y1="198" x2="177" y2="198" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="169" y1="187.5" x2="177" y2="187.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="173" cy="192.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="205" y1="175.5" x2="205" y2="165" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="175.5" x2="209" y2="175.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="165" x2="209" y2="165" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="205" cy="170" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="236.5" y1="152.5" x2="236.5" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="232.5" y1="152.5" x2="240.5" y2="152.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="232.5" y1="142" x2="240.5" y2="142" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="236.5" cy="147.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="268.5" y1="128" x2="268.5" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="264.5" y1="128" x2="272.5" y2="128" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="264.5" y1="118" x2="272.5" y2="118" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="268.5" cy="123" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="300" y1="105.5" x2="300" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="296" y1="105.5" x2="304" y2="105.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="296" y1="95" x2="304" y2="95" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="300" cy="100.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="62" cy="276.5" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="316" cy="88" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="71.5" y="96" width="145" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$k \approx 0{,}135\,\text{ml}/{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="78" y="276" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$(0;\ 37{,}7)$</div></foreignObject>
  <foreignObject x="176" y="58" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$(80;\ 48{,}5)$</div></foreignObject>
</svg>

Kuvaajassa ympyröidyt kohdat ovat ne kaksi suoran pistettä, joista b-kohdan kulmakerroin luetaan.

**Mallivastaus:** Pisteet ovat lähes suoralla: tilavuus kasvaa yhtä paljon jokaista lämpötilan astetta kohti. Pisteisiin sovitetaan yksi nouseva suora, joka kulkee pisteiden lomitse ja jokaisen epävarmuusjanan kautta. Pisteitä ei yhdistetä murtoviivaksi. Todellisissa mittaussarjoissa pisteet eivät yleensä ole täsmälleen samalla suoralla mittausepävarmuuden vuoksi.

### b)
**Annettu:** a-kohdan suora ja siltä luetut pisteet; lukeman epävarmuus $\pm 0{,}3\,\text{ml}$
**Kysytty:** lämpötila $\theta_0$, jossa suoran mukaan $V = 0$, sen epävarmuus ja vertailu arvoon $-273{,}15\,{}^\circ\text{C}$
**Periaate:** Vakiopaineessa harvan kaasun tilavuus on suoraan verrannollinen kelvinlämpötilaan, joten $(\theta, V)$-kuvaaja on suora, jonka jatke osuu nollaan absoluuttisessa nollapisteessä (luku *Kaasujen tilanmuutokset ja Boylen laki*). Suoraa jatketaan mittausalueen ulkopuolelle eli ekstrapoloidaan. Epävarmuus arvioidaan jyrkimmän ja loivimman suoran avulla, jotka vielä kulkevat kaikkien epävarmuusjanojen kautta (luku *Absoluuttisen nollapisteen määrittäminen*).
**Kuvaajan lukeminen:** Suoralta luetaan kaksi kaukana toisistaan olevaa pistettä, ei mittauspisteitä: $(0\,{}^\circ\text{C};\ 37{,}7\,\text{ml})$ ja $(80\,{}^\circ\text{C};\ 48{,}5\,\text{ml})$. Ääriviivat kulkevat janojen päiden kautta: jyrkin pisteiden $(15\,{}^\circ\text{C};\ 39{,}6\,\text{ml})$ ja $(75\,{}^\circ\text{C};\ 48{,}1\,\text{ml})$, loivin pisteiden $(5\,{}^\circ\text{C};\ 38{,}5\,\text{ml})$ ja $(75\,{}^\circ\text{C};\ 47{,}5\,\text{ml})$ kautta.

<svg data-fig="fy9-kaasut-s3-extra" viewBox="0 0 420 350" role="img" aria-label="Kuvaaja: sama suora koko alueella θ = −300…100 °C ja V = 0…50 ml. Mittauspisteet ovat vain alueella 5–75 °C. Sovitettua suoraa on jatkettu katkoviivana, ja se leikkaa lämpötila-akselin noin kohdassa −279 °C. Kaksi harmaata ääriviivaa, jyrkin ja loivin suora, jotka vielä kulkevat kaikkien epävarmuusjanojen kautta, leikkaavat akselin kohdissa noin −265 °C ja −294 °C. Hyväksytty arvo −273 °C on niiden välissä." style="max-width:100%;font-size:24px">
  <line x1="88" y1="300" x2="88" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120.5" y1="300" x2="120.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="153" y1="300" x2="153" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="185" y1="300" x2="185" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217" y1="300" x2="217" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="249.5" y1="300" x2="249.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="282" y1="300" x2="282" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="314" y1="300" x2="314" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="252" x2="314" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="204" x2="314" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="156" x2="314" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="108" x2="314" y2="108" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="60" x2="314" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="55" y1="300" x2="328" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M340,300 L327,306 L327,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="56" y1="301" x2="56" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M56,34 L62,47 L50,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="88" y1="300" x2="88" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="120.5" y1="300" x2="120.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="309.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${-}200$</div></foreignObject>
  <line x1="153" y1="300" x2="153" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="185" y1="300" x2="185" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="156" y="309.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${-}100$</div></foreignObject>
  <line x1="217" y1="300" x2="217" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="249.5" y1="300" x2="249.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="239.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="282" y1="300" x2="282" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="314" y1="300" x2="314" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="291.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="49" y1="252" x2="56" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="49" y1="204" x2="56" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="11" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="49" y1="156" x2="56" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="49" y1="108" x2="56" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="11" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="49" y1="60" x2="56" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="46" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <line x1="249.5" y1="300" x2="249.5" y2="60" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <polyline points="79,300 301,65.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="4 5"/>
  <polyline points="59.5,300 301,69" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="4 5"/>
  <polyline points="69.5,300 252.5,116" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="252.5,116 298,70.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="252.5" cy="116.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="259" cy="108.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="265.5" cy="102.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="272" cy="96" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="278.5" cy="90" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="285" cy="83.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="291.5" cy="77" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298" cy="70.5" r="4" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="75.5" y1="296" x2="117.5" y2="281" stroke="#e8590c" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="69.5" cy="300" r="6" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="119" y="264" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\theta_0 \approx {-}279\,{}^\circ\text{C}$</span></div></foreignObject>
  <foreignObject x="61" y="69.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ääriviivat:}$</div></foreignObject>
  <foreignObject x="61" y="98.5" width="165" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">${-}265\ \text{ja}\ {-}294\,{}^\circ\text{C}$</div></foreignObject>
</svg>

**Kaava:** $k = \dfrac{V_2 - V_1}{\theta_2 - \theta_1}$ ja $V = V_0 + k\theta$; kun $V = 0$, $\theta_0 = -\dfrac{V_0}{k}$, ja $\Delta\theta_0 = \dfrac{\theta_{0,\text{max}} - \theta_{0,\text{min}}}{2}$
**Muunnokset:** Ei tarvita: millilitrat supistuvat, ja tulos saadaan celsiusasteina.
**Sijoitus:** $k = \dfrac{48{,}5\,\text{ml} - 37{,}7\,\text{ml}}{80\,{}^\circ\text{C} - 0\,{}^\circ\text{C}} = 0{,}135\,\text{ml}/{}^\circ\text{C}$ ja $\theta_0 = -\dfrac{37{,}7\,\text{ml}}{0{,}135\,\text{ml}/{}^\circ\text{C}} = -279\,{}^\circ\text{C}$. Jyrkin suora: $k = 0{,}1417\,\text{ml}/{}^\circ\text{C}$, $V_0 = 37{,}48\,\text{ml}$, $\theta_0 = -264{,}5\,{}^\circ\text{C}$; loivin: $k = 0{,}1286\,\text{ml}/{}^\circ\text{C}$, $V_0 = 37{,}86\,\text{ml}$, $\theta_0 = -294{,}4\,{}^\circ\text{C}$. $\Delta\theta_0 = \dfrac{-264{,}5\,{}^\circ\text{C} - (-294{,}4\,{}^\circ\text{C})}{2} = 15\,{}^\circ\text{C}$
**Vastaus:** $\theta_0 \approx (-279 \pm 15)\,{}^\circ\text{C}$. Tulos ilmoitetaan kokonaisina asteina, koska epävarmuus on kymmeniä asteita. Hyväksytty arvo $-273{,}15\,{}^\circ\text{C}$ on välin $-294$…$-265\,{}^\circ\text{C}$ sisällä, joten tulos sopii yhteen sen kanssa, eikä ero $6\,\text{K}$ ole merkittävä. Väli on arvio, ei taattu raja: se ei kerro, pysyykö riippuvuus suorana mittausalueen ulkopuolella.
**Järkevyys:** Suoraa jatketaan noin $280\,\text{K}$, lähes neljä kertaa mittausalueen pituuden $70\,\text{K}$ verran, joten pienikin kulmakertoimen ero kasvaa jatkossa kymmeniksi asteiksi. Pienimmän neliösumman suora antaa saman: $k = 0{,}1351\,\text{ml}/{}^\circ\text{C}$ ja $\theta_0 = -279\,{}^\circ\text{C}$.

### c)
**Annettu:** b-kohdan kulmakerroin $k = 0{,}135\,\text{ml}/{}^\circ\text{C}$, paine $p = 101{,}3\,\text{kPa}$; $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Kysytty:** ruiskun ilman ainemäärä $n$
**Periaate:** Ilman määrä ja paine pysyvät samoina, joten tilanyhtälön mukaan tilavuus on suoraan verrannollinen kelvinlämpötilaan, ja suoran kulmakerroin on $nR/p$ (luku *Ideaalikaasun tilanyhtälö $pV = nRT$*). Yhden celsiusasteen muutos on sama kuin yhden kelvinin muutos, joten kulmakerroin on sama kummallakin asteikolla.
**Kuvaajan lukeminen:** Kulmakerroin luetaan a-kohdan suoralta kuten b-kohdassa: $k = 10{,}8\,\text{ml} : 80\,{}^\circ\text{C} = 0{,}135\,\text{ml}/{}^\circ\text{C}$.
**Kaava:** $pV = nRT$, joten $V = \dfrac{nR}{p}\,T$ ja $k = \dfrac{\Delta V}{\Delta T} = \dfrac{nR}{p}$, josta $n = \dfrac{pk}{R}$
**Muunnokset:** $k = 0{,}135\,\text{ml/K} = 0{,}135 \cdot 10^{-6}\,\text{m}^3/\text{K}$, koska $1\,\text{ml} = 10^{-6}\,\text{m}^3$, ja $p = 101{,}3 \cdot 1000\,\text{Pa} = 101\,300\,\text{Pa}$
**Sijoitus:** $n = \dfrac{101\,300\,\text{Pa} \cdot 0{,}135 \cdot 10^{-6}\,\text{m}^3/\text{K}}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}} = 1{,}65 \cdot 10^{-3}\,\text{mol}$
**Vastaus:** $n \approx 1{,}65\,\text{mmol}$, kolme merkitsevää numeroa kuten kulmakerroin $0{,}135\,\text{ml}/{}^\circ\text{C}$.
**Järkevyys:** Yksi mittauspiste antaa lähes saman: $n = \dfrac{pV}{RT} = \dfrac{101\,300\,\text{Pa} \cdot 41{,}1 \cdot 10^{-6}\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 298{,}15\,\text{K}} = 1{,}68\,\text{mmol}$. Ero johtuu siitä, että kulmakertoimen kautta laskettu tulos ei käytä oletusta, että suora kulkee absoluuttisen nollapisteen kautta. Suuruusluokka sopii: $40\,\text{ml}$ ilmaa on noin $1{,}7\,\text{mmol}$, kun mooli kaasua vie huoneenlämmössä noin $24\,\textsf{l}$.

### d)
**Kysytty:** miten hauteen ulkopuolelle jäävä $1{,}5\,\text{ml}$:n ilmamäärä muuttaa suoraa ja nollapisteen arviota, ja poistavatko toistot virheen
**Periaate:** Letkun ilma pysyy huoneenlämmössä ja samassa paineessa, joten sen tilavuus ei muutu hauteen lämmetessä. Mittauksessa luettu tilavuus on hauteessa olevan ilman tilavuus ja letkun vakiotilavuus yhteensä. Systemaattinen virhe siirtää kaikkia tuloksia samaan suuntaan, eikä sitä voi poistaa toistamalla (luku *Absoluuttisen nollapisteen määrittäminen*).
**Mallivastaus:** Jokaiseen lukemaan tulee lähes sama lisä $1{,}5\,\text{ml}$, joten suora siirtyy ylöspäin mutta sen kulmakerroin ei juuri muutu: kulmakertoimen määrää vain hauteessa oleva ilma. Nollakohta on silloin $\theta_0 = -\dfrac{V_0 + 1{,}5\,\text{ml}}{k}$, eli arvio siirtyy kylmemmäksi noin $\dfrac{1{,}5\,\text{ml}}{0{,}135\,\text{ml}/{}^\circ\text{C}} \approx 11\,\text{K}$: tämän ryhmän tulos olisi noin $-290\,{}^\circ\text{C}$. Virhe on systemaattinen, joten useammat toistot tai useampi mittauspiste eivät poista sitä. Koko ilmamäärä on pidettävä hauteessa, tai letkun tilavuus mitataan ja vähennetään jokaisesta lukemasta.

### Yleisiä virheitä
- Kuvaajan pisteet yhdistetään murtoviivaksi tai suora pakotetaan kulkemaan origon kautta, vaikka vaaka-akseli on celsiusasteina.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä eikä sovitetusta suorasta.
- b-kohdassa tulosta $-279\,{}^\circ\text{C}$ pidetään epäonnistuneena, koska se ei ole $-273\,{}^\circ\text{C}$, tai ekstrapolointia ei mainita.
- c-kohdassa millilitroja ei muunneta kuutiometreiksi, jolloin ainemäärä tulee miljoonakertaiseksi.
- d-kohdassa oletetaan, että toistot poistavat letkun aiheuttaman virheen.

### Hyväksytään myös
- Silmämääräisesti sovitetun suoran kulmakerroin $0{,}132$…$0{,}138\,\text{ml}/{}^\circ\text{C}$ ja sen mukaiset tulokset: b-kohdassa $-290$…$-268\,{}^\circ\text{C}$, c-kohdassa $1{,}61$…$1{,}68\,\text{mmol}$.
- b-kohdassa epävarmuuden arvio $\pm 10$…$\pm 20\,{}^\circ\text{C}$, kun se on perusteltu ääriviivoilla.

## fy9-kaasut-s4

### a)
**Kysytty:** mikä esitteessä pitää paikkansa ja mikä ei
**Periaate:** Energian säilymislaki sallii vain muutokset, joissa energia ei synny eikä katoa (luku *Sisäenergia, lämpömäärä ja energian säilyminen*). Lämpövoimakoneelle on lisäksi raja: se voi muuttaa lämpöä työksi vain, jos se luovuttaa osan lämmöstä kylmempään ympäristöön (luku *Kaasun tekemä työ ja lämpövoimakone*).
**Mallivastaus:** Esitteen energiaa koskeva osa pitää: meren sisäenergia voisi energian puolesta muuttua laivan liikkeeksi, ja jos meri jäähtyy saman verran kuin työtä tehdään, energia säilyy. Moottori ei silti voi toimia. Lämpövoimakone tekee työtä vain, kun lämpöä siirtyy kuumasta kylmempään ja osa siitä luovutetaan kylmempään ympäristöön. Esitteen moottorilla on vain yksi lämpötila, $15\,{}^\circ\text{C}$:n meri, eikä mitään kylmempää, jonne lämpö voisi mennä. Kaikkea lämpöä ei voi muuttaa työksi, olipa kone kuinka kitkaton tahansa. Esitteen väite, ettei moottori riko yhtään luonnonlakia, on siis väärä, eikä hanketta kannata rahoittaa.

### b)
**Annettu:** merivedestä otettu lämpöteho $P_1 = 500\,\text{kW}$, työteho $P_W = 30\,\text{kW}$; meri $3\,{}^\circ\text{C}$, pakkasilma $-20\,{}^\circ\text{C}$
**Kysytty:** hyötysuhde $\eta$, pakkasilmaan luovutettu lämpöteho $P_2$ ja miksi hyötysuhde on pieni
**Periaate:** Kone on lämpövoimakone, jonka kuuma lähde on meri ja kylmä ympäristö pakkasilma. Energia säilyy, joten meren lämpö jakautuu työksi ja kylmään luovutetuksi lämmöksi. Hyötysuhde on työn osuus otetusta lämmöstä, ja sen voi laskea tehoista (luku *Kaasun tekemä työ ja lämpövoimakone*).
**Kaava:** $\eta = \dfrac{P_W}{P_1}$ ja $P_1 = P_W + P_2$, joten $P_2 = P_1 - P_W$
**Muunnokset:** Ei tarvita laskussa. Vertailua varten kelvineinä meri on $3 + 273 = 276\,\text{K}$ ja ilma $253\,\text{K}$.
**Sijoitus:** $\eta = \dfrac{30\,\text{kW}}{500\,\text{kW}} = 0{,}060 = 6{,}0\,\%$ ja $P_2 = 500\,\text{kW} - 30\,\text{kW} = 470\,\text{kW}$
**Vastaus:** $\eta \approx 6{,}0\,\%$ ja $P_2 \approx 470\,\text{kW}$, kaksi merkitsevää numeroa kuten työteho $30\,\text{kW}$. Hyötysuhde on pieni, koska lämpötilaero $23\,\text{K}$ on pieni verrattuna kuuman lähteen lämpötilaan $276\,\text{K}$: mitä pienempi tämä suhde on, sitä pienempi osa lämmöstä voi muuttua työksi.
**Järkevyys:** Energia säilyy: $30\,\text{kW} + 470\,\text{kW} = 500\,\text{kW}$. Kone ei riko lakeja, koska se luovuttaa lähes kaiken lämmön kylmempään. Hyötysuhde on paljon pienempi kuin voimalaitoksen noin $40\,\%$, jossa höyry on satoja asteita kuumempaa kuin lauhdutin.

### c)
**Kysytty:** miksi lämpöpumppu voi lämmittää hyttejä merivedellä, vaikka esitteen moottori ei voi toimia
**Periaate:** Lämpöpumppu toimii päinvastoin kuin lämpövoimakone: se käyttää sähköenergiaa ja siirtää sen avulla lämpöä kylmästä lämpimään. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja sähköenergian summa (luku *Kaasun tekemä työ ja lämpövoimakone*).
**Mallivastaus:** Lämpöpumppu ei muuta lämpöä työksi. Se siirtää lämpöä kylmästä $3\,{}^\circ\text{C}$:n merivedestä lämpimiin hytteihin, ja siihen tarvitaan työtä, tässä sähkötehoa $10\,\text{kW}$. Energia säilyy: hytteihin tulee merivedestä otettu $35\,\text{kW} - 10\,\text{kW} = 25\,\text{kW}$ ja sähkön $10\,\text{kW}$, yhteensä $35\,\text{kW}$. Suhde $35 : 10 = 3{,}5$ on lämpökerroin eikä hyötysuhde: se voi olla yli $1$, koska suurin osa lämmöstä siirretään merestä eikä tehdä sähköstä. Mitään ei synny tyhjästä. Ero esitteen moottoriin on suunnassa ja hinnassa: lämpöpumppu tarvitsee ulkopuolista työtä siirtääkseen lämpöä kylmästä lämpimään, kun taas esitteen moottori lupaa työtä merestä ilman kylmempää ympäristöä.

### Yleisiä virheitä
- a-kohdassa todetaan vain, että ”energiaa ei synny tyhjästä”, vaikka esite ei väitäkään niin: virhe on toisessa rajassa, kylmemmän ympäristön puuttumisessa.
- b-kohdassa hyötysuhde lasketaan jakamalla työ kylmään luovutetulla lämmöllä, $30 : 470$, eikä otetulla lämmöllä.
- c-kohdassa lämpökerrointa $3{,}5$ kutsutaan hyötysuhteeksi $350\,\%$ ja päätellään, että pumppu tuottaa energiaa.

## fy9-kaasut-s5

### a)
**Annettu:** raportista massa ennen $m_1 = 52{,}36\,\text{g}$ ja jälkeen $m_2 = 55{,}64\,\text{g}$, pumpun mittarin ylipaine $\Delta p = 210\,\text{kPa}$, pullon tilavuus $V = 1{,}5\,\textsf{l}$, lämpötila $\theta = 21\,{}^\circ\text{C}$; $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$
**Kysytty:** ryhmän laskema moolimassa $M$
**Periaate:** Pullon tilavuus ja lämpötila ovat ryhmän oletuksessa ennen ja jälkeen pumppauksen samat. Tilanyhtälön mukaan ainemäärä on silloin verrannollinen paineeseen, joten lisätyn ilman ainemäärä saadaan paineen kasvusta, joka on mittarin näyttämä ylipaine (luku *Ideaalikaasun tilanyhtälö $pV = nRT$*). Moolimassa on lisätyn ilman massa jaettuna sen ainemäärällä.
**Kaava:** $\Delta n = n_2 - n_1 = \dfrac{(p_0 + \Delta p)V}{RT} - \dfrac{p_0V}{RT} = \dfrac{\Delta p\,V}{RT}$ ja $M = \dfrac{m_2 - m_1}{\Delta n}$
**Muunnokset:** $\Delta p = 210 \cdot 1000\,\text{Pa} = 210\,000\,\text{Pa}$, $V = 1{,}5 \cdot 0{,}001\,\text{m}^3 = 0{,}0015\,\text{m}^3$ ja $T = (21 + 273{,}15)\,\text{K} = 294{,}15\,\text{K}$
**Sijoitus:** $\Delta n = \dfrac{210\,000\,\text{Pa} \cdot 0{,}0015\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 294{,}15\,\text{K}} = 0{,}1289\,\text{mol}$ ja $M = \dfrac{55{,}64\,\text{g} - 52{,}36\,\text{g}}{0{,}1289\,\text{mol}} = \dfrac{3{,}28\,\text{g}}{0{,}1289\,\text{mol}} = 25{,}4\,\text{g/mol}$
**Vastaus:** $M \approx 25\,\text{g/mol}$, kaksi merkitsevää numeroa kuten tilavuus $1{,}5\,\textsf{l}$. Ryhmän luku on laskettu oikein.
**Järkevyys:** Jos moolimassa olisi taulukon $29{,}0\,\text{g/mol}$, pulloon olisi pitänyt tulla $29{,}0\,\tfrac{\text{g}}{\text{mol}} \cdot 0{,}1289\,\text{mol} \approx 3{,}74\,\text{g}$ ilmaa. Punnittu $3{,}28\,\text{g}$ on noin $12\,\%$ pienempi.

### b)
**Kysytty:** onko johtopäätös perusteltu, tärkeimmät virhelähteet ja niiden vaikutuksen suunta
**Periaate:** Johtopäätös on perusteltu vain, jos ero taulukkoarvoon on suurempi kuin tuloksen epävarmuus (luku *Mittaaminen ja mittauksen luotettavuus*). Virhelähteen vaikutus arvioidaan laskemalla tulos uudelleen muutetulla arvolla. Moolimassa on $\Delta m : \Delta n$, joten liian suuri $\Delta n$ tai liian pieni $\Delta m$ pienentää tulosta.
**Mallivastaus:** Johtopäätös ei ole perusteltu. Tulos on yhden mittauksen varassa, ja tärkeimmät virhelähteet vievät sitä samaan suuntaan, alaspäin.
- *Lämmin ilma.* Pumpattu ilma lämpenee puristuessaan, ja mittari luettiin heti. Lämpimän ilman paine on suurempi kuin samalla ilmamäärällä huoneenlämmössä, joten $\Delta n$ laskettiin liian suureksi ja tulos liian pieneksi. Jos ilma oli $30\,{}^\circ\text{C}$:ista, tulos olisi noin $27\,\text{g/mol}$.
- *Pumpun mittari.* Se mittaa letkun painetta pumppauksen aikana ja on tehty karkeaan käyttöön. Jos pullon todellinen ylipaine oli $10\,\text{kPa}$ pienempi, tulos olisi $27\,\text{g/mol}$; virhe voi olla kumpaan suuntaan tahansa.
- *Karkaava ilma.* Pumppua irrotettaessa ja venttiilin kautta karkaa ilmaa ennen punnitusta, joten $\Delta m$ on liian pieni ja tulos liian pieni.
- *Pullon tilavuus.* Merkintä $1{,}5\,\textsf{l}$ on juoman tilavuus. Pullo on hieman suurempi ja pullistuu paineessa, joten todellinen $\Delta n$ on laskettua suurempi. Tämä suurentaa laskettua tulosta, eli se ei selitä liian pientä arvoa.

Vaa'an tarkkuus $0{,}01\,\text{g}$ on alle $1\,\%$ massan kasvusta $3{,}28\,\text{g}$, joten se ei ole merkittävä. Lämpötilan ja mittarin virheet ovat kumpikin noin $5$–$7\,\%$, joten epävarmuus on samaa suuruusluokkaa kuin ero taulukkoarvoon. Mittaus ei osoita taulukkoarvoa vääräksi.

### c)
**Kysytty:** koesuunnitelma, jolla ilman moolimassa saadaan luotettavammin
**Periaate:** Suureet mitataan mahdollisimman suoraan ja silloin, kun oletukset pätevät (sama lämpötila ennen ja jälkeen). Mittaus toistetaan usealla arvolla, ja tulos määritetään kuvaajan kulmakertoimesta, jolloin yksittäisen mittauksen virhe painaa vähemmän (luku *Graafinen esitys ja suoran sovittaminen*).
**Mallivastaus:**
- *Tilavuus.* Pullon tilavuus mitataan täyttämällä se vedellä ja punnitsemalla vesi ($1\,\text{g} \approx 1\,\text{ml}$).
- *Paine ja lämpötila.* Pulloon liitetään tarkka painemittari, ja ylipaine luetaan vasta, kun pullo on seissyt muutaman minuutin ja ilma on jäähtynyt huoneenlämpöön. Huoneen lämpötila mitataan lämpömittarilla.
- *Massa.* Pullo punnitaan heti painelukeman jälkeen niin, ettei venttiiliin kosketa välissä.
- *Toistot ja kuvaaja.* Mittaus tehdään usealla ylipaineella, esimerkiksi $50$, $100$, $150$, $200$ ja $250\,\text{kPa}$, samalla pullolla ja venttiilillä. Tulokset esitetään kuvaajana $(\Delta p, \Delta m)$. Tilanyhtälön mukaan $\Delta m = \dfrac{MV}{RT}\,\Delta p$, joten pisteisiin sovitetaan origon kautta kulkeva suora, ja moolimassa saadaan kulmakertoimesta: $M = \dfrac{kRT}{V}$.

Jos pisteet ovat suoralla mutta suora ei kulje origon kautta, se paljastaa systemaattisen virheen, esimerkiksi irrotuksessa joka kerta karkaavan ilman.

### Yleisiä virheitä
- a-kohdassa ainemäärä lasketaan kokonaispaineella $311\,\text{kPa}$ eikä paineen kasvulla, jolloin tulos on kolmasosa.
- b-kohdassa todetaan vain ”mittausvirheitä oli” nimeämättä virhelähdettä tai sen vaikutuksen suuntaa.
- b-kohdassa pullon pullistuminen nimetään syyksi liian pieneen tulokseen, vaikka se vaikuttaa päinvastoin.
- c-kohdassa ehdotetaan vain ”tarkempia mittareita” kertomatta, mitä mitataan ja miten.

### Hyväksytään myös
- b-kohdassa voi mainita myös, että pullistuva pullo syrjäyttää enemmän ilmaa, jolloin noste kasvaa ja vaaka näyttää noin $0{,}06\,\text{g}$ liian vähän (pienentää tulosta vähän), kun perustelu on oikein.

## fy9-kaasut-s6

### a)
**Annettu:** lasilevyn mitat $2{,}40\,\text{m}$, $1{,}20\,\text{m}$ ja $10\,\text{mm}$, tiheys $\rho = 2500\,\text{kg/m}^3$, laikan sisähalkaisija $d = 300\,\text{mm}$, kiihtyvyys ylös $a = 1{,}2\,\text{m/s}^2$; $g = 9{,}81\,\text{m/s}^2$
**Kysytty:** levyn voimakuvio ja pienin alipaine $\Delta p$ laikan alla kilopascaleina
**Periaate:** Ulkoilma painaa levyä joka puolelta, mutta laikan alla paine on $\Delta p$ pienempi. Siksi ulkoilman voima levyn alapintaan on laikan kohdalla $\Delta p\,A$ suurempi kuin ilman voima yläpintaan, ja nettovoima $F_\text{p} = \Delta p\,A$ osoittaa kohtisuoraan pintaa vastaan eli ylös (luku *Paine ja hydrostaattinen paine*). Lisäksi levyyn vaikuttavat paino ja laikan reunan tukivoima, joka painaa levyä alas. Pienimmällä alipaineella reunan tukivoima on nolla: levy on irtoamisen rajalla. Levy kiihtyy ylös, joten Newtonin toisen lain mukaan voimien summa on $ma$ ylöspäin (luku *Newtonin toinen laki*).

<svg data-fig="fy9-kaasut-s6-vaaka" viewBox="0 0 420 270" role="img" aria-label="Voimakuvio: vaakasuora lasilevy kapeana suorakulmiona, kun nosto kiihtyy ylöspäin ja alipaine on pienin mahdollinen. Paino G lähtee levyn keskipisteestä suoraan alas. Paine-eron voima F p lähtee levyn yläpinnasta laikan kohdalta ylös, ja se on painoa pidempi, koska levy kiihtyy ylöspäin. Laikan reunan tukivoima on tässä rajatapauksessa nolla. Erillään oranssi kiihtyvyysnuoli a ylöspäin." style="max-width:100%;font-size:24px">
  <rect x="50" y="125" width="260" height="20" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="180" y1="135" x2="180" y2="195.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,212.5 L172,194.5 L188,194.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="189.5" y="202" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="180" y1="125" x2="180" y2="55" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M180,38 L188,56 L172,56 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="187.5" y="29.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{p}$</div></foreignObject>
  <line x1="370" y1="165" x2="370" y2="107" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M376.5,118 L370,105 L363.5,118" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="373.5" y="94.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

**Kaava:** $F_\text{p} - mg = ma$ ja $F_\text{p} = \Delta p\,A$, missä $m = \rho\,l\,b\,h$ ja $A = \pi \left(\dfrac{d}{2}\right)^2$, joten $\Delta p = \dfrac{m(g + a)}{\pi (d/2)^2}$
**Muunnokset:** $10\,\text{mm} = 10 \cdot 0{,}001\,\text{m} = 0{,}010\,\text{m}$ ja $d/2 = 300\,\text{mm} : 2 = 150\,\text{mm} = 0{,}150\,\text{m}$
**Sijoitus:** $m = 2500\,\tfrac{\text{kg}}{\text{m}^3} \cdot 2{,}40\,\text{m} \cdot 1{,}20\,\text{m} \cdot 0{,}010\,\text{m} = 72{,}0\,\text{kg}$, $A = \pi \cdot (0{,}150\,\text{m})^2 = 0{,}070\,69\,\text{m}^2$ ja $\Delta p = \dfrac{72{,}0\,\text{kg} \cdot (9{,}81 + 1{,}2)\,\text{m/s}^2}{0{,}070\,69\,\text{m}^2} = \dfrac{792{,}7\,\text{N}}{0{,}070\,69\,\text{m}^2} = 11\,210\,\text{Pa}$
**Vastaus:** $\Delta p \approx 11{,}2\,\text{kPa}$, kolme merkitsevää numeroa kuten levyn mitat; kiihtyvyys $1{,}2\,\text{m/s}^2$ on annettu kahdella numerolla, mutta se on vain pieni osa summasta $g + a$.
**Järkevyys:** Ilman kiihtyvyyttä tarvittaisiin $706\,\text{N} : 0{,}0707\,\text{m}^2 \approx 10\,\text{kPa}$, joten kiihtyvyys lisää tarvetta noin $12\,\%$, kuten suhde $1{,}2 : 9{,}81$ kertoo. Nostimen $60\,\text{kPa}$ on yli viisinkertainen.

### b)
**Annettu:** $m = 72{,}0\,\text{kg}$, $A = 0{,}070\,69\,\text{m}^2$, $a = 1{,}2\,\text{m/s}^2$ ylös, kuivan lasin lepokitkakerroin $\mu_0 = 0{,}60$
**Kysytty:** pystysuoran levyn voimakuvio ja pienin alipaine $\Delta p$
**Periaate:** Paine-eron voima on kohtisuorassa lasin pintaa vastaan, ja nyt pinta on pystysuora, joten voima $F_\text{p} = \Delta p\,A$ on vaakasuora ja painaa levyä laikkaa vasten. Laikan reuna työntää levyä takaisin tukivoimalla $N$. Vaakasuunnassa levy ei kiihdy, joten $N = F_\text{p}$. Painoa ja kiihdyttävää voimaa vastaan levyä kannattaa vain laikan reunan lepokitka, joka on enintään $\mu_0 N$ (luku *Paino, kitka ja kalteva taso*). Pienimmällä alipaineella lepokitka on suurimmillaan.

<svg data-fig="fy9-kaasut-s6-pysty" viewBox="0 0 420 400" role="img" aria-label="Voimakuvio: pystyasentoon käännetty lasilevy kapeana pystysuorana suorakulmiona, laikka levyn vasemmalla pinnalla. Paino G keskipisteestä suoraan alas. Paine-eron voima F p työntää levyä oikealta vaakasuoraan vasemmalle kohti laikkaa. Laikan reunan tukivoima N työntää levyä vasemmalta vaakasuoraan oikealle; se on yhtä suuri kuin F p. Lepokitka F μ0 lähtee levyn vasemmasta yläkulmasta ylös, ja se on painoa pidempi, koska levy kiihtyy ylöspäin. N on noin 1,7 kertaa kitkan pituinen, koska kitka on pienimmillä alipaineella 0,60 kertaa tukivoima. Erillään oranssi kiihtyvyysnuoli a ylöspäin." style="max-width:100%;font-size:24px">
  <rect x="188" y="85" width="24" height="250" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="210" x2="200" y2="253" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M200,270 L192,252 L208,252 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="211.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="324.5" y1="190" x2="229" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M212,190 L230,182 L230,198 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="326" y="153.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{p}$</div></foreignObject>
  <line x1="75.5" y1="230" x2="171" y2="230" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M188,230 L170,238 L170,222 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="35" y="193.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="188" y1="85" x2="188" y2="34.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M188,17.5 L196,35.5 L180,35.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="129" y="11" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu 0}$</div></foreignObject>
  <line x1="385" y1="265" x2="385" y2="207" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M391.5,218 L385,205 L378.5,218" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="388.5" y="194.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

**Kaava:** vaakasuunnassa $N - F_\text{p} = 0$ ja pystysuunnassa $F_{\mu 0} - mg = ma$, missä $F_{\mu 0} \le \mu_0 N = \mu_0\,\Delta p\,A$, joten $\Delta p = \dfrac{m(g + a)}{\mu_0 A}$
**Muunnokset:** Ei tarvita: a-kohdan suureet ovat perusyksiköissä.
**Sijoitus:** $\Delta p = \dfrac{72{,}0\,\text{kg} \cdot (9{,}81 + 1{,}2)\,\text{m/s}^2}{0{,}60 \cdot 0{,}070\,69\,\text{m}^2} = \dfrac{792{,}7\,\text{N}}{0{,}042\,41\,\text{m}^2} = 18\,690\,\text{Pa}$
**Vastaus:** $\Delta p \approx 18{,}7\,\text{kPa}$, kolme merkitsevää numeroa kuten a-kohdassa; kitkakerroin on suuntaa antava kahden numeron arvo, joten noin $19\,\text{kPa}$ on yhtä hyvä vastaus.
**Järkevyys:** Tulos on a-kohdan tulos jaettuna kitkakertoimella: $11{,}2\,\text{kPa} : 0{,}60 \approx 18{,}7\,\text{kPa}$. Pystyasento vaatii enemmän, koska kitka on pienempi kuin sen aiheuttava tukivoima.

### c)
**Kysytty:** täyttääkö pystynosto märällä lasilla valmistajan ohjeen
**Periaate:** Varmuuskerroin on nostimen alipaineen ja noston vaatiman alipaineen suhde, ja ohjeen mukaan sen on oltava vähintään $2$. Märkänä lepokitkakerroin on $0{,}30$, joten b-kohdan tulos kaksinkertaistuu (luku *Paino, kitka ja kalteva taso*).
**Mallivastaus:** Märällä lasilla tarvitaan $\Delta p = \dfrac{792{,}7\,\text{N}}{0{,}30 \cdot 0{,}070\,69\,\text{m}^2} \approx 37\,\text{kPa}$. Nostimen $60\,\text{kPa}$ riittää siis juuri ja juuri pitämään levyn, mutta varmuuskerroin on vain $60 : 37 \approx 1{,}6$, alle ohjeen vaatiman kahden. Kuivana pystynosto täyttää ohjeen, $60 : 18{,}7 \approx 3{,}2$, ja vaakanosto selvästi, $60 : 11{,}2 \approx 5{,}4$. Pystyasento on vaativampi, koska paineen voima on kohtisuorassa lasin pintaa vastaan eli vaakasuora. Se ei kannata painoa lainkaan, vaan painon kantaa kitka, joka on enintään $\mu_0$ kertaa tukivoima. Asentaja ei saa nostaa märkää levyä pystyssä tällä nostimella: lasi on kuivattava, tai käytetään kahta laikkaa, jolloin ala kaksinkertaistuu.

### Yleisiä virheitä
- a-kohdassa pinta-ala lasketaan halkaisijasta säteen sijasta, tai levyn paksuus jätetään millimetreiksi.
- a-kohdassa unohdetaan kiihtyvyys ja lasketaan pelkkä paino.
- b-kohdassa paine-eron voima piirretään ylöspäin kannattamaan levyä, vaikka paineen voima on aina kohtisuorassa pintaa vastaan.
- b-kohdassa kitka lasketaan painosta, $\mu_0 mg$, eikä tukivoimasta $N = \Delta p\,A$.
- c-kohdassa vastataan, että nosto onnistuu, koska $60\,\text{kPa}$ on enemmän kuin $37\,\text{kPa}$, ja unohdetaan varmuuskerroin.

### Hyväksytään myös
- a- ja b-kohdassa voimakuvioon voi piirtää myös laikan reunan tukivoiman, kun vastaus kertoo, että se on pienimmällä alipaineella nolla (a) tai yhtä suuri kuin paine-eron voima (b).
