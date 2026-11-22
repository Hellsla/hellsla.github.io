# Ohuen kalvon interferenssi

> **Miksi** saippuakuplan pinnassa näkyy kirkkaita väriraitoja, vaikka saippuavesi on väritöntä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: aurinkoisena päivänä puutarhan yllä leijuu kolme saippuakuplaa. Suurimman kuplan pinnassa on vaakasuoria väriraitoja. Ylhäällä on harmaata ja valkoista, sitten keltaista, oranssia, purppuraa, sinistä ja vihreää. Alempana on taas keltaista ja purppuraa. Pöydällä on kulho saippuavettä ja kuplarengas. Värit on laskettu saippuakalvon paksuudesta. Paksuus kasvaa kuplan yläosasta alaosaan." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Kaksi heijastusta
Luvussa *Valon interferenssi ja diffraktio* nähtiin, että valo on aaltoliikettä. Kaksi valoaaltoa voi vahvistaa tai heikentää toisiaan. Tätä sanotaan interferenssiksi. **Ohut kalvo** on läpinäkyvä kerros, joka on yhtä ohut kuin valon aallonpituus, noin $100$–$1000\,\text{nm}$. Esimerkkejä ovat saippuakuplan seinämä, öljykalvo vedessä ja linssin pinnoite. Kun valo osuu kalvoon, pieni osa heijastuu kalvon yläpinnasta. Toinen pieni osa menee kalvon sisään ja heijastuu alapinnasta. Nämä kaksi heijastunutta aaltoa etenevät samaan suuntaan ja **interferoivat**. Tässä luvussa valo tulee kalvoon aina kohtisuoraan.

<svg data-fig="reflections" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva, ei mittakaavassa: saippuakalvo poikkileikkauksena, ilmaa molemmin puolin. Kalvon paksuus d on kuvassa suurennettu. Säteet on piirretty vinoon, jotta ne erottuvat. Luvussa valo tulee kuitenkin kohtisuoraan. Ylhäältä tuleva säde heijastuu osittain kalvon yläpinnasta. Tämä on säde 1. Siinä heijastunut aalto saa puolen aallonpituuden siirtymän, koska valo heijastuu aineeseen, jolla on suurempi taitekerroin. Osa valosta menee kalvoon ja heijastuu alapinnasta ilmaa vasten. Siinä ei ole siirtymää. Heijastunut valo palaa yläpinnan läpi ilmaan. Tämä on säde 2. Säde 2 kulkee kalvossa lisämatkan, joka on kaksi kertaa kalvon paksuus. Heikko osa valosta jatkaa alapinnan läpi alas." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-reflections.webp" x="-1.3" y="0" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="273" y="19.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="320" y="19.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="89" y="103.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}\lambda\ \text{siirtymä}$</div></foreignObject>
  <foreignObject x="121" y="251.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ei siirtymää}$</div></foreignObject>
  <foreignObject x="106" y="175.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="435" y="69.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ilma},\ n = 1{,}00$</div></foreignObject>
  <foreignObject x="335" y="175.5" width="249" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{saippuakalvo},\ n = 1{,}33$</div></foreignObject>
  <foreignObject x="435" y="285.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ilma},\ n = 1{,}00$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/soap-bubble-reflection.webp" alt="Saippuakupla ilmassa. Kuplassa näkyy heijastunut kuva puista ja taivaasta."><figcaption>Saippuakupla heijastaa ympäristöä. Kuplan reunoilla on värejä. Valo heijastuu kalvon ulkopinnasta ja sisäpinnasta. Heijastuneet aallot interferoivat.</figcaption></figure>

### Matkaero kalvossa
Alapinnasta heijastunut aalto 2 kulkee kalvon läpi alas ja takaisin ylös. Se kulkee siksi lisämatkan $2d$, kun $d$ on kalvon paksuus. Kalvossa valo etenee hitaammin, nopeudella $c : n$. Valon taajuus ei kuitenkaan muutu. Siksi aallonpituus on kalvossa $n$ kertaa lyhyempi kuin ilmassa. Esimerkiksi saippuakalvossa ($n = 1{,}33$) aallonpituus $550\,\text{nm}$ lyhenee arvoon $413{,}5\,\text{nm}$, koska $550\,\text{nm} : 1{,}33 = 413{,}5\,\text{nm}$. Lisämatkaan $2d$ mahtuu siksi yhtä monta aallonpituutta kuin ilmassa matkaan $2nd$. Alapinnasta heijastunut säde kulkee siis kalvossa geometrisesti ylimääräisen matkan $2d$. Valo etenee kalvossa hitaammin kuin ilmassa. Siksi vastaava **optinen matkaero** on $2nd$. Sitä verrataan aallonpituuteen ilmassa.

### Puolen aallonpituuden siirtymä heijastuksessa
Matkaero ei yksin ratkaise interferenssiä. Luvussa *Aalto kohtaa esteen tai raon* köyden pulssi kääntyi heijastuessaan kiinteästä päästä, mutta ei vapaasta päästä. Valolle on vastaava sääntö: **kun valo heijastuu rajapinnasta, jonka takana on aine, jolla on suurempi taitekerroin, heijastunut aalto kääntyy.** Silloin harja palaa pohjana. Kääntyminen vastaa puolen aallonpituuden siirtymää. Jos takana on aine, jolla on pienempi taitekerroin, aalto ei käänny. Saippuakalvossa yläpinnan heijastus tapahtuu ilmasta kalvoon ($1{,}00 \to 1{,}33$), joten aalto 1 kääntyy. Alapinnan heijastus tapahtuu kalvosta ilmaan ($1{,}33 \to 1{,}00$), joten aalto 2 ei käänny.

```pysahdy
Valo etenee lasissa ($n = 1{,}52$) ja heijastuu lasin ja ilman rajapinnasta ($1{,}52 \to 1{,}00$). Kääntyykö heijastunut aalto?
---
Ei käänny. Rajapinnan takana on ilma, ja sen taitekerroin on pienempi. Aalto kääntyy vain, kun takana on aine, jolla on suurempi taitekerroin.
```

### Hyvin ohut kalvo on musta
Oletetaan, että saippuakalvo on paljon ohuempi kuin aallonpituus. Silloin matkaero on lähes nolla. Aalto 1 on kuitenkin kääntynyt ja aalto 2 ei. Aallot ovat siksi vastakkaisessa vaiheessa ja kumoavat toisensa. Ihannetilanteessa hyvin ohut saippuakalvo heijastaa vain hyvin vähän valoa. Siksi se näyttää heijastuneessa valossa tummalta tai lähes mustalta. Siksi saippuakuplan yläosaan ilmestyy musta laikku juuri ennen puhkeamista. Kun kalvo on niin paksu, että $2nd = \tfrac{1}{2}\lambda$, aalto 2 jää puoli aallonpituutta jälkeen. Se vastaa kääntymistä. Silloin aallot ovat samassa vaiheessa ja vahvistavat toisiaan.

<svg data-fig="phase" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva: kalvosta heijastuneet aallot 1 ja 2 sekä niiden summa kahdessa tapauksessa. Vasemmalla kalvo on paljon ohuempi kuin aallonpituus. Aalto 1 on kääntynyt yläpinnan heijastuksessa, aalto 2 ei. Aalto 2 ei ole jäänyt jälkeen. Aallot ovat siksi vastakkaisessa vaiheessa: harja kohtaa pohjan. Summa on vaakasuora suora, eli heijastunutta valoa ei ole. Oikealla kalvo on niin paksu, että aalto 2 kulkee puoli aallonpituutta pidemmän matkan. Silloin aallot ovat samassa vaiheessa. Summa on kaksinkertainen aalto, eli heijastus on voimakas." style="max-width:100%;font-size:24px">
  <foreignObject x="69.5" y="21.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hyvin ohut kalvo}$</div></foreignObject>
  <line x1="95" y1="72" x2="95" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M70,100 L72,102.5 L73.5,105 L75.5,107.5 L77,109.5 L79,111.5 L80.5,113.5 L82.5,115.5 L84.5,117 L86,118.5 L88,120 L89.5,121 L91.5,121.5 L93,122 L95,122 L97,122 L98.5,121.5 L100.5,121 L102,120 L104,118.5 L105.5,117 L107.5,115.5 L109,114 L111,112 L113,109.5 L114.5,107.5 L116.5,105 L118,102.5 L120,100 L121.5,97.5 L123.5,95 L125.5,93 L127,90.5 L129,88.5 L130.5,86.5 L132.5,84.5 L134,83 L136,81.5 L138,80 L139.5,79.5 L141.5,78.5 L143,78 L145,78 L146.5,78 L148.5,78.5 L150,79 L152,80 L154,81.5 L155.5,82.5 L157.5,84.5 L159,86 L161,88 L162.5,90.5 L164.5,92.5 L166.5,95 L168,97.5 L170,100 L171.5,102.5 L173.5,104.5 L175,107 L177,109.5 L179,111.5 L180.5,113.5 L182.5,115.5 L184,117 L186,118.5 L187.5,119.5 L189.5,120.5 L191.5,121.5 L193,122 L195,122 L196.5,122 L198.5,121.5 L200,121 L202,120 L204,119 L205.5,117.5 L207.5,115.5 L209,114 L211,112 L212.5,110 L214.5,107.5 L216,105 L218,102.5 L220,100.5 L221.5,98 L223.5,95.5 L225,93 L227,90.5 L228.5,88.5 L230.5,86.5 L232.5,84.5 L234,83 L236,81.5 L237.5,80.5 L239.5,79.5 L241,78.5 L243,78 L245,78 L246.5,78 L248.5,78.5 L250,79 L252,80 L253.5,81 L255.5,82.5 L257,84 L259,86 L261,88 L262.5,90 L264.5,92.5 L266,95 L268,97 L269.5,99.5 L271.5,102 L273.5,104.5 L275,107 L277,109 L278.5,111.5 L280.5,113.5 L282,115.5 L284,117" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M70,170 L72,167.5 L73.5,165 L75.5,162.5 L77,160.5 L79,158.5 L80.5,156.5 L82.5,154.5 L84.5,153 L86,151.5 L88,150 L89.5,149 L91.5,148.5 L93,148 L95,148 L97,148 L98.5,148.5 L100.5,149 L102,150 L104,151.5 L105.5,153 L107.5,154.5 L109,156 L111,158 L113,160.5 L114.5,162.5 L116.5,165 L118,167.5 L120,170 L121.5,172.5 L123.5,175 L125.5,177 L127,179.5 L129,181.5 L130.5,183.5 L132.5,185.5 L134,187 L136,188.5 L138,190 L139.5,190.5 L141.5,191.5 L143,192 L145,192 L146.5,192 L148.5,191.5 L150,191 L152,190 L154,188.5 L155.5,187.5 L157.5,185.5 L159,184 L161,182 L162.5,179.5 L164.5,177.5 L166.5,175 L168,172.5 L170,170 L171.5,167.5 L173.5,165.5 L175,163 L177,160.5 L179,158.5 L180.5,156.5 L182.5,154.5 L184,153 L186,151.5 L187.5,150.5 L189.5,149.5 L191.5,148.5 L193,148 L195,148 L196.5,148 L198.5,148.5 L200,149 L202,150 L204,151 L205.5,152.5 L207.5,154.5 L209,156 L211,158 L212.5,160 L214.5,162.5 L216,165 L218,167.5 L220,169.5 L221.5,172 L223.5,174.5 L225,177 L227,179.5 L228.5,181.5 L230.5,183.5 L232.5,185.5 L234,187 L236,188.5 L237.5,189.5 L239.5,190.5 L241,191.5 L243,192 L245,192 L246.5,192 L248.5,191.5 L250,191 L252,190 L253.5,189 L255.5,187.5 L257,186 L259,184 L261,182 L262.5,180 L264.5,177.5 L266,175 L268,173 L269.5,170.5 L271.5,168 L273.5,165.5 L275,163 L277,161 L278.5,158.5 L280.5,156.5 L282,154.5 L284,153" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <line x1="70" y1="250" x2="284" y2="250" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="38" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="38" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="13" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1 + 2$</div></foreignObject>
  <foreignObject x="94.5" y="315.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heikentävä}$</div></foreignObject>
  <foreignObject x="411.5" y="21.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2nd = \tfrac{1}{2}\lambda$</div></foreignObject>
  <line x1="387" y1="72" x2="387" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M362,100 L364,102.5 L365.5,105 L367.5,107.5 L369,109.5 L371,111.5 L372.5,113.5 L374.5,115.5 L376.5,117 L378,118.5 L380,120 L381.5,121 L383.5,121.5 L385,122 L387,122 L389,122 L390.5,121.5 L392.5,121 L394,120 L396,118.5 L397.5,117 L399.5,115.5 L401,114 L403,112 L405,109.5 L406.5,107.5 L408.5,105 L410,102.5 L412,100 L413.5,97.5 L415.5,95 L417.5,93 L419,90.5 L421,88.5 L422.5,86.5 L424.5,84.5 L426,83 L428,81.5 L430,80 L431.5,79.5 L433.5,78.5 L435,78 L437,78 L438.5,78 L440.5,78.5 L442,79 L444,80 L446,81.5 L447.5,82.5 L449.5,84.5 L451,86 L453,88 L454.5,90.5 L456.5,92.5 L458.5,95 L460,97.5 L462,100 L463.5,102.5 L465.5,104.5 L467,107 L469,109.5 L471,111.5 L472.5,113.5 L474.5,115.5 L476,117 L478,118.5 L479.5,119.5 L481.5,120.5 L483.5,121.5 L485,122 L487,122 L488.5,122 L490.5,121.5 L492,121 L494,120 L496,119 L497.5,117.5 L499.5,115.5 L501,114 L503,112 L504.5,110 L506.5,107.5 L508,105 L510,102.5 L512,100.5 L513.5,98 L515.5,95.5 L517,93 L519,90.5 L520.5,88.5 L522.5,86.5 L524.5,84.5 L526,83 L528,81.5 L529.5,80.5 L531.5,79.5 L533,78.5 L535,78 L537,78 L538.5,78 L540.5,78.5 L542,79 L544,80 L545.5,81 L547.5,82.5 L549,84 L551,86 L553,88 L554.5,90 L556.5,92.5 L558,95 L560,97 L561.5,99.5 L563.5,102 L565.5,104.5 L567,107 L569,109 L570.5,111.5 L572.5,113.5 L574,115.5 L576,117" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M362,170 L364,172.5 L365.5,175 L367.5,177.5 L369,179.5 L371,181.5 L372.5,183.5 L374.5,185.5 L376.5,187 L378,188.5 L380,190 L381.5,191 L383.5,191.5 L385,192 L387,192 L389,192 L390.5,191.5 L392.5,191 L394,190 L396,188.5 L397.5,187 L399.5,185.5 L401,184 L403,182 L405,179.5 L406.5,177.5 L408.5,175 L410,172.5 L412,170 L413.5,167.5 L415.5,165 L417.5,163 L419,160.5 L421,158.5 L422.5,156.5 L424.5,154.5 L426,153 L428,151.5 L430,150 L431.5,149.5 L433.5,148.5 L435,148 L437,148 L438.5,148 L440.5,148.5 L442,149 L444,150 L446,151.5 L447.5,152.5 L449.5,154.5 L451,156 L453,158 L454.5,160.5 L456.5,162.5 L458.5,165 L460,167.5 L462,170 L463.5,172.5 L465.5,174.5 L467,177 L469,179.5 L471,181.5 L472.5,183.5 L474.5,185.5 L476,187 L478,188.5 L479.5,189.5 L481.5,190.5 L483.5,191.5 L485,192 L487,192 L488.5,192 L490.5,191.5 L492,191 L494,190 L496,189 L497.5,187.5 L499.5,185.5 L501,184 L503,182 L504.5,180 L506.5,177.5 L508,175 L510,172.5 L512,170.5 L513.5,168 L515.5,165.5 L517,163 L519,160.5 L520.5,158.5 L522.5,156.5 L524.5,154.5 L526,153 L528,151.5 L529.5,150.5 L531.5,149.5 L533,148.5 L535,148 L537,148 L538.5,148 L540.5,148.5 L542,149 L544,150 L545.5,151 L547.5,152.5 L549,154 L551,156 L553,158 L554.5,160 L556.5,162.5 L558,165 L560,167 L561.5,169.5 L563.5,172 L565.5,174.5 L567,177 L569,179 L570.5,181.5 L572.5,183.5 L574,185.5 L576,187" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round"/>
  <path d="M362,250 L364,255 L365.5,260 L367.5,264.5 L369,269 L371,273.5 L372.5,277.5 L374.5,281 L376.5,284.5 L378,287 L380,289.5 L381.5,291.5 L383.5,293 L385,293.5 L387,294 L389,293.5 L390.5,293 L392.5,291.5 L394,289.5 L396,287.5 L397.5,284.5 L399.5,281 L401,277.5 L403,273.5 L405,269 L406.5,264.5 L408.5,260 L410,255 L412,250 L413.5,245.5 L415.5,240.5 L417.5,235.5 L419,231 L421,227 L422.5,222.5 L424.5,219 L426,215.5 L428,213 L430,210.5 L431.5,208.5 L433.5,207 L435,206.5 L437,206 L438.5,206 L440.5,207 L442,208.5 L444,210 L446,212.5 L447.5,215.5 L449.5,218.5 L451,222.5 L453,226.5 L454.5,230.5 L456.5,235 L458.5,240 L460,244.5 L462,249.5 L463.5,254.5 L465.5,259.5 L467,264 L469,268.5 L471,273 L472.5,277 L474.5,281 L476,284 L478,287 L479.5,289.5 L481.5,291.5 L483.5,293 L485,293.5 L487,294 L488.5,294 L490.5,293 L492,291.5 L494,290 L496,287.5 L497.5,284.5 L499.5,281.5 L501,278 L503,274 L504.5,269.5 L506.5,265 L508,260.5 L510,255.5 L512,250.5 L513.5,245.5 L515.5,241 L517,236 L519,231.5 L520.5,227 L522.5,223 L524.5,219.5 L526,216 L528,213 L529.5,210.5 L531.5,208.5 L533,207 L535,206.5 L537,206 L538.5,206 L540.5,207 L542,208.5 L544,210 L545.5,212.5 L547.5,215 L549,218.5 L551,222 L553,226 L554.5,230.5 L556.5,235 L558,239.5 L560,244.5 L561.5,249.5 L563.5,254 L565.5,259 L567,264 L569,268.5 L570.5,273 L572.5,277 L574,280.5 L576,284" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="330" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="330" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="305" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1 + 2$</div></foreignObject>
  <foreignObject x="386.5" y="315.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vahvistava}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="340" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
</svg>

### Miksi kalvo on värikäs
Auringonvalo on valkoista valoa. Siinä on kaikkia näkyvän valon aallonpituuksia, noin $400$–$700\,\text{nm}$. Samanpaksuisessa kalvossa matkaero $2nd$ vahvistaa joitakin aallonpituuksia ja heikentää toisia. Heijastuneesta valosta puuttuu silloin osa väreistä, ja kalvo näyttää värikkäältä. Esimerkiksi $200\,\text{nm}$:n paksuisessa saippuakalvossa matkaero on $532\,\text{nm}$. Vihreä valo, jonka aallonpituus on $532\,\text{nm}$, kumoutuu. Punaista ja violettia valoa kuitenkin heijastuu, joten kalvo näyttää purppuralta.

Saippuakupla ei ole joka kohdasta yhtä paksu. Painovoima valuttaa saippuavettä alaspäin, joten kalvo ohenee ylhäältä ja paksunee alhaalla. Jokainen väriraita on kohta, jossa kalvo on yhtä paksu. Raidat liikkuvat, kun kalvo valuu ja haihtuu.

Veden pinnalla olevassa öljykalvossa ($n \approx 1{,}5$) on samat ehdot kuin saippuakalvossa. Yläpinnan heijastus tapahtuu ilmasta öljyyn, ja se kääntää aallon. Alapinnan heijastus tapahtuu öljystä veteen ($n = 1{,}33$), ja se ei käännä aaltoa.

Paksussa kalvossa, kuten ikkunalasissa, värejä ei näy. Jo $5\,\mu\text{m}$:n saippuakalvossa näkyvän valon alueella on $14$ aallonpituutta, jotka vahvistuvat. Niiden väliin jää lähes yhtä monta aallonpituutta, jotka heikentyvät. Värit sekoittuvat siksi valkoiseksi.

<svg data-fig="bands" viewBox="0 0 600 300" role="img" aria-label="Kuva lasketuista väreistä: valkoisessa valossa saippuakalvosta heijastuneen valon väri kalvon paksuuden mukaan. Saippuakalvon taitekerroin on 1,33, ja valo tulee kohtisuoraan. Yläpuolella on kiilan muotoinen kalvo poikkileikkauksena. Sen paksuus kasvaa vasemmalta oikealle nollasta 1000 nanometriin. Paksuus on kuvassa suurennettu. Värinauha alkaa vasemmalta mustana. Sitten se muuttuu harmaansiniseksi, valkoiseksi, keltaiseksi ja oranssiksi. Noin 200 nanometrin kohdalla väri on purppura. Sen jälkeen tulevat sininen, vihreä, keltainen ja taas purppura. Mitä paksumpi kalvo, sitä haaleammiksi värit muuttuvat. Värien kirkkaus on vahvistettu, koska todellinen heijastus on vain muutamia prosentteja." style="max-width:100%;font-size:24px">
  <path d="M40,116 L500,60 L500,116 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="40" y="130" width="4.5" height="60" fill="#0a0d12"/>
  <rect x="43.5" y="130" width="4.5" height="60" fill="#2d3542"/>
  <rect x="47.5" y="130" width="4.5" height="60" fill="#4c586b"/>
  <rect x="51" y="130" width="4.5" height="60" fill="#68778e"/>
  <rect x="54.5" y="130" width="4.5" height="60" fill="#8193ad"/>
  <rect x="58.5" y="130" width="4.5" height="60" fill="#98abc7"/>
  <rect x="62" y="130" width="4.5" height="60" fill="#adc1dc"/>
  <rect x="66" y="130" width="4.5" height="60" fill="#bfd3ec"/>
  <rect x="69.5" y="130" width="4.5" height="60" fill="#cfe2f7"/>
  <rect x="73" y="130" width="4.5" height="60" fill="#ddeefe"/>
  <rect x="77" y="130" width="4.5" height="60" fill="#e9f7ff"/>
  <rect x="80.5" y="130" width="4.5" height="60" fill="#f2fdfd"/>
  <rect x="84" y="130" width="4.5" height="60" fill="#f9fff5"/>
  <rect x="88" y="130" width="4.5" height="60" fill="#fdffe9"/>
  <rect x="91.5" y="130" width="4.5" height="60" fill="#fffbd7"/>
  <rect x="95" y="130" width="4.5" height="60" fill="#fff4c1"/>
  <rect x="99" y="130" width="4.5" height="60" fill="#feeaa5"/>
  <rect x="102.5" y="130" width="4.5" height="60" fill="#f9dd84"/>
  <rect x="106" y="130" width="4.5" height="60" fill="#f3cc5d"/>
  <rect x="110" y="130" width="4.5" height="60" fill="#e9b829"/>
  <rect x="113.5" y="130" width="4.5" height="60" fill="#dea000"/>
  <rect x="117.5" y="130" width="4.5" height="60" fill="#cf8400"/>
  <rect x="121" y="130" width="4.5" height="60" fill="#be6539"/>
  <rect x="124.5" y="130" width="4.5" height="60" fill="#aa3f68"/>
  <rect x="128.5" y="130" width="4.5" height="60" fill="#92008e"/>
  <rect x="132" y="130" width="4.5" height="60" fill="#7600ae"/>
  <rect x="135.5" y="130" width="4.5" height="60" fill="#5400c8"/>
  <rect x="139.5" y="130" width="4.5" height="60" fill="#1e3ede"/>
  <rect x="143" y="130" width="4.5" height="60" fill="#0064ee"/>
  <rect x="146.5" y="130" width="4.5" height="60" fill="#0084fa"/>
  <rect x="150.5" y="130" width="4.5" height="60" fill="#00a0ff"/>
  <rect x="154" y="130" width="4.5" height="60" fill="#00b8ff"/>
  <rect x="158" y="130" width="4.5" height="60" fill="#2ecdff"/>
  <rect x="161.5" y="130" width="4.5" height="60" fill="#5ddef9"/>
  <rect x="165" y="130" width="4.5" height="60" fill="#7eecec"/>
  <rect x="169" y="130" width="4.5" height="60" fill="#9af6db"/>
  <rect x="172.5" y="130" width="4.5" height="60" fill="#b3fdc6"/>
  <rect x="176" y="130" width="4.5" height="60" fill="#c8ffab"/>
  <rect x="180" y="130" width="4.5" height="60" fill="#daff8c"/>
  <rect x="183.5" y="130" width="4.5" height="60" fill="#eafe68"/>
  <rect x="187" y="130" width="4.5" height="60" fill="#f7f83b"/>
  <rect x="191" y="130" width="4.5" height="60" fill="#ffee00"/>
  <rect x="194.5" y="130" width="4.5" height="60" fill="#ffe000"/>
  <rect x="198" y="130" width="4.5" height="60" fill="#ffcf2b"/>
  <rect x="202" y="130" width="4.5" height="60" fill="#ffbb5b"/>
  <rect x="205.5" y="130" width="4.5" height="60" fill="#ffa481"/>
  <rect x="209.5" y="130" width="4.5" height="60" fill="#ff89a1"/>
  <rect x="213" y="130" width="4.5" height="60" fill="#ff6bbc"/>
  <rect x="216.5" y="130" width="4.5" height="60" fill="#f34bd2"/>
  <rect x="220.5" y="130" width="4.5" height="60" fill="#e327e4"/>
  <rect x="224" y="130" width="4.5" height="60" fill="#ce0af1"/>
  <rect x="227.5" y="130" width="4.5" height="60" fill="#b525fa"/>
  <rect x="231.5" y="130" width="4.5" height="60" fill="#9648fe"/>
  <rect x="235" y="130" width="4.5" height="60" fill="#6e68fd"/>
  <rect x="238.5" y="130" width="4.5" height="60" fill="#2d85f8"/>
  <rect x="242.5" y="130" width="4.5" height="60" fill="#009fef"/>
  <rect x="246" y="130" width="4.5" height="60" fill="#00b6e1"/>
  <rect x="250" y="130" width="4.5" height="60" fill="#00cad0"/>
  <rect x="253.5" y="130" width="4.5" height="60" fill="#00dabc"/>
  <rect x="257" y="130" width="4.5" height="60" fill="#00e7a4"/>
  <rect x="261" y="130" width="4.5" height="60" fill="#00f18b"/>
  <rect x="264.5" y="130" width="4.5" height="60" fill="#29f772"/>
  <rect x="268" y="130" width="4.5" height="60" fill="#6dfb5d"/>
  <rect x="272" y="130" width="4.5" height="60" fill="#95fa53"/>
  <rect x="275.5" y="130" width="4.5" height="60" fill="#b4f759"/>
  <rect x="279" y="130" width="4.5" height="60" fill="#cef16b"/>
  <rect x="283" y="130" width="4.5" height="60" fill="#e4e782"/>
  <rect x="286.5" y="130" width="4.5" height="60" fill="#f5db9a"/>
  <rect x="290" y="130" width="4.5" height="60" fill="#ffcdb0"/>
  <rect x="294" y="130" width="4.5" height="60" fill="#ffbcc3"/>
  <rect x="297.5" y="130" width="4.5" height="60" fill="#ffaad3"/>
  <rect x="301.5" y="130" width="4.5" height="60" fill="#ff97df"/>
  <rect x="305" y="130" width="4.5" height="60" fill="#ff85e8"/>
  <rect x="308.5" y="130" width="4.5" height="60" fill="#ff74ed"/>
  <rect x="312.5" y="130" width="4.5" height="60" fill="#ff68ee"/>
  <rect x="316" y="130" width="4.5" height="60" fill="#f863ec"/>
  <rect x="319.5" y="130" width="4.5" height="60" fill="#e867e6"/>
  <rect x="323.5" y="130" width="4.5" height="60" fill="#d472dd"/>
  <rect x="327" y="130" width="4.5" height="60" fill="#bc81d1"/>
  <rect x="330.5" y="130" width="4.5" height="60" fill="#a192c4"/>
  <rect x="334.5" y="130" width="4.5" height="60" fill="#80a3b5"/>
  <rect x="338" y="130" width="4.5" height="60" fill="#58b3a5"/>
  <rect x="342" y="130" width="4.5" height="60" fill="#03c298"/>
  <rect x="345.5" y="130" width="4.5" height="60" fill="#00ce8d"/>
  <rect x="349" y="130" width="4.5" height="60" fill="#00d887"/>
  <rect x="353" y="130" width="4.5" height="60" fill="#00e088"/>
  <rect x="356.5" y="130" width="4.5" height="60" fill="#00e58e"/>
  <rect x="360" y="130" width="4.5" height="60" fill="#00e898"/>
  <rect x="364" y="130" width="4.5" height="60" fill="#4ee9a4"/>
  <rect x="367.5" y="130" width="4.5" height="60" fill="#76e7b1"/>
  <rect x="371" y="130" width="4.5" height="60" fill="#95e4bd"/>
  <rect x="375" y="130" width="4.5" height="60" fill="#afdec8"/>
  <rect x="378.5" y="130" width="4.5" height="60" fill="#c5d7d0"/>
  <rect x="382" y="130" width="4.5" height="60" fill="#d7ced7"/>
  <rect x="386" y="130" width="4.5" height="60" fill="#e5c5da"/>
  <rect x="389.5" y="130" width="4.5" height="60" fill="#f0badc"/>
  <rect x="393.5" y="130" width="4.5" height="60" fill="#f9b0da"/>
  <rect x="397" y="130" width="4.5" height="60" fill="#fea6d6"/>
  <rect x="400.5" y="130" width="4.5" height="60" fill="#ff9ed0"/>
  <rect x="404.5" y="130" width="4.5" height="60" fill="#ff97c9"/>
  <rect x="408" y="130" width="4.5" height="60" fill="#fc93c1"/>
  <rect x="411.5" y="130" width="4.5" height="60" fill="#f691b8"/>
  <rect x="415.5" y="130" width="4.5" height="60" fill="#ed93b0"/>
  <rect x="419" y="130" width="4.5" height="60" fill="#e297a9"/>
  <rect x="422.5" y="130" width="4.5" height="60" fill="#d69da4"/>
  <rect x="426.5" y="130" width="4.5" height="60" fill="#c7a4a2"/>
  <rect x="430" y="130" width="4.5" height="60" fill="#b7aca2"/>
  <rect x="434" y="130" width="4.5" height="60" fill="#a6b4a6"/>
  <rect x="437.5" y="130" width="4.5" height="60" fill="#94bcab"/>
  <rect x="441" y="130" width="4.5" height="60" fill="#83c3b2"/>
  <rect x="445" y="130" width="4.5" height="60" fill="#74c9b9"/>
  <rect x="448.5" y="130" width="4.5" height="60" fill="#68cec0"/>
  <rect x="452" y="130" width="4.5" height="60" fill="#61d2c6"/>
  <rect x="456" y="130" width="4.5" height="60" fill="#62d5ca"/>
  <rect x="459.5" y="130" width="4.5" height="60" fill="#6ad7ce"/>
  <rect x="463" y="130" width="4.5" height="60" fill="#76d7cf"/>
  <rect x="467" y="130" width="4.5" height="60" fill="#84d6cf"/>
  <rect x="470.5" y="130" width="4.5" height="60" fill="#94d4ce"/>
  <rect x="474" y="130" width="4.5" height="60" fill="#a3d1ca"/>
  <rect x="478" y="130" width="4.5" height="60" fill="#b1cdc6"/>
  <rect x="481.5" y="130" width="4.5" height="60" fill="#bfc8c1"/>
  <rect x="485.5" y="130" width="4.5" height="60" fill="#cac2bc"/>
  <rect x="489" y="130" width="4.5" height="60" fill="#d4bdb7"/>
  <rect x="492.5" y="130" width="4.5" height="60" fill="#dcb7b2"/>
  <rect x="496.5" y="130" width="4.5" height="60" fill="#e2b2af"/>
  <rect x="40" y="130" width="460" height="60" fill="none" stroke="#1f2933" stroke-width="2"/>
  <line x1="40" y1="190" x2="40" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="201.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="132" y1="190" x2="132" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="224" y1="190" x2="224" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="201.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="316" y1="190" x2="316" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="408" y1="190" x2="408" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385.5" y="201.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="500" y1="190" x2="500" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="471" y="201.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1000$</div></foreignObject>
  <line x1="86" y1="190" x2="86" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="178" y1="190" x2="178" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="190" x2="270" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362" y1="190" x2="362" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="454" y1="190" x2="454" y2="195" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="512" y="145.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{nm})$</div></foreignObject>
  <foreignObject x="40" y="19.5" width="249" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{saippuakalvo},\ n = 1{,}33$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/soap-bubble-colours.webp" alt="Saippuakalvo läheltä. Siinä on oransseja, sinisiä ja violetteja pyörteitä."><figcaption>Saippuakalvon värit. Kalvo on eri kohdista eri paksu. Siksi eri kohdissa vahvistuu eri väri.</figcaption></figure>

```pysahdy
Miksi ikkunalasissa ei näy värejä, vaikka sekin heijastaa valoa kahdesta pinnasta?
---
Lasi on niin paksu, että näkyvällä alueella on hyvin monta aallonpituutta, jotka vahvistuvat, ja hyvin monta, jotka heikentyvät. Värit sekoittuvat valkoiseksi.
```

## Kaava: Ohuen kalvon interferenssi
Kun valo tulee kohtisuoraan kalvoon, kalvon kahdesta pinnasta heijastuneiden aaltojen optinen matkaero on
```latex
\Delta s = 2nd
```
missä $n$ on kalvon taitekerroin, $d$ kalvon paksuus ja $\lambda$ valon aallonpituus ilmassa (lähes sama kuin tyhjiössä). Ehdot riippuvat siitä, kuinka moni heijastus kääntää aallon. Tarkastellaan ensin saippuakalvoa ilmassa. Sen molemmin puolin on aine, jolla on pienempi taitekerroin. Silloin vain yläpinnan heijastus kääntää aallon, ja
```latex
\begin{aligned}
&\text{vahvistava:} \\
&2nd = (k + \tfrac{1}{2})\lambda \\[6pt]
&\text{heikentävä:} \\
&2nd = k\lambda
\end{aligned}
```
missä $k = 0, 1, 2, \ldots$

```pysahdy
Saippuakalvon ($n = 1{,}33$) paksuus on $125\,\text{nm}$. Valo tulee kohtisuoraan ilmasta. Mikä aallonpituus vahvistuu, kun $k = 0$?
---
Matkaero on $2nd = 2 \cdot 1{,}33 \cdot 125\,\text{nm} = 332{,}5\,\text{nm}$. Ehdosta $2nd = (k + \tfrac{1}{2})\lambda$ ja $k = 0$ saadaan $\lambda = 665\,\text{nm}$. Punainen valo vahvistuu.
```

Toinen tapaus on linssin pinnoite. Sen taitekerroin on ilman ja lasin välissä, joten kumpikin heijastus kääntää aallon. Käännökset kumoavat toisensa. Silloin ehdot vaihtavat paikkaa: $2nd = k\lambda$ on vahvistava ja $2nd = (k + \tfrac{1}{2})\lambda$ on heikentävä. Sama pätee, kun kumpikaan heijastus ei käännä aaltoa.

### Heijastuksenestopinnoite
Tavallinen lasi ($n = 1{,}52$) heijastaa kummastakin pinnastaan noin $4\,\%$ kohtisuoraan tulevasta valosta. Kameran objektiivissa on monta linssiä. Heijastukset heikentävät kuvaa ja tekevät siihen haamukuvia. Silmälaseissa heijastus näkyy kiiltona.

**Heijastuksenestopinnoite** on ohut kalvo, joka höyrystetään lasin pinnalle. Se voi olla esimerkiksi magnesiumfluoridia $\text{MgF}_2$. Sen taitekerroin on $1{,}38$ aallonpituudella $550\,\text{nm}$ (Dodge, *Applied Optics*, 1984). Pinnoitteen kumpikin heijastus tapahtuu aineeseen, jolla on suurempi taitekerroin ($1{,}00 \to 1{,}38 \to 1{,}52$). Siksi heikentävä ehto on $2nd = (k + \tfrac{1}{2})\lambda$. Ohuimmalla pinnoitteella $k = 0$. Silloin pinnoitteen paksuus on neljäsosa aallonpituudesta pinnoitteessa:
```latex
d = \frac{\lambda}{4n}
```
Pinnoite mitoitetaan yleensä näkyvän valon keskelle, koska silmä on herkin sille. Kun $\lambda = 550\,\text{nm}$, paksuus on $99{,}6\,\text{nm}$. Heijastus pienenee silloin pinnasta noin $4{,}3\,\%$:sta noin $1{,}3\,\%$:iin.

Täydellinen kumoutuminen vaatisi, että kaksi heijastunutta aaltoa olisivat yhtä voimakkaat. Kohtisuorassa tulossa näin käy, kun pinnoitteen taitekerroin on $\sqrt{n_\text{lasi}}$. Lasille se on $\sqrt{1{,}52} \approx 1{,}23$. Näin pientä taitekerrointa ei ole kestävillä pinnoiteaineilla, ja $\text{MgF}_2$ on lähimpiä. Pinnoite ei myöskään kumoa kaikkia aallonpituuksia yhtä hyvin. Violettia ja punaista heijastuu enemmän kuin vihreää, joten pinnoitettu linssi kiiltää purppuraisena. Valo ei katoa: mitä vähemmän valoa heijastuu, sitä enemmän sitä pääsee lasin läpi. Nykyaikaisissa objektiiveissa on usein monta kerrosta päällekkäin.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: kohtisuoraan tulevasta valosta heijastuvan valon osuus R prosentteina aallonpituuden mukaan välillä 400–700 nm. Pinnoittamaton lasi, jonka taitekerroin on 1,52, heijastaa kaikilla aallonpituuksilla noin 4,3 prosenttia. Se on vaakasuora musta viiva. Lasin pinnalla on magnesiumfluoridikerros. Sen taitekerroin on 1,38 ja paksuus 99,6 nanometriä. Paksuus on neljäsosa aallonpituudesta 550 nanometriä kalvossa. Silloin vihreä käyrä laskee pienimpään arvoonsa, noin 1,3 prosenttiin, 550 nanometrin kohdalla. Reunoilla käyrä nousee: 400 nanometrin kohdalla noin 2,2 prosenttiin ja 700 nanometrin kohdalla noin 1,6 prosenttiin. Taitekertoimien riippuvuutta aallonpituudesta ei ole otettu huomioon." style="max-width:100%;font-size:24px">
  <line x1="158.5" y1="286" x2="158.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220.5" y1="286" x2="220.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="286" x2="283" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345.5" y1="286" x2="345.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407.5" y1="286" x2="407.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="286" x2="470" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="241.5" x2="470" y2="241.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197" x2="470" y2="197" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="153" x2="470" y2="153" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="108.5" x2="470" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="470" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="484" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,286 L483,292 L483,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="158.5" y1="286" x2="158.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220.5" y1="286" x2="220.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="198" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="283" y1="286" x2="283" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="345.5" y1="286" x2="345.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="323" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="407.5" y1="286" x2="407.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="286" x2="470" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="89" y1="241.5" x2="96" y2="241.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="227" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="197" x2="96" y2="197" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="182.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="153" x2="96" y2="153" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="138.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="108.5" x2="96" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="94" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="49.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="502" y="271.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R\ (\%)$</div></foreignObject>
  <foreignObject x="73.5" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <foreignObject x="60" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,97 470,97" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,188 99,189.5 102,191.5 105.5,193 108.5,194.5 111.5,196 114.5,197.5 118,199 121,200.5 124,201.5 127,203 130.5,204 133.5,205.5 136.5,206.5 139.5,208 143,209 146,210 149,211 152,212 155,213 158.5,214 161.5,215 164.5,216 167.5,216.5 171,217.5 174,218.5 177,219 180,220 183.5,220.5 186.5,221 189.5,222 192.5,222.5 195.5,223 199,223.5 202,224 205,224.5 208,225 211.5,225.5 214.5,226 217.5,226.5 220.5,226.5 224,227 227,227.5 230,227.5 233,228 236,228 239.5,228.5 242.5,228.5 245.5,229 248.5,229 252,229.5 255,229.5 258,229.5 261,229.5 264.5,230 267.5,230 270.5,230 273.5,230 277,230 280,230 283,230 286,230 289,230 292.5,230 295.5,230 298.5,230 301.5,230 305,229.5 308,229.5 311,229.5 314,229.5 317.5,229.5 320.5,229 323.5,229 326.5,229 330,228.5 333,228.5 336,228.5 339,228 342,228 345.5,227.5 348.5,227.5 351.5,227.5 354.5,227 358,227 361,226.5 364,226.5 367,226 370.5,226 373.5,225.5 376.5,225 379.5,225 382.5,224.5 386,224.5 389,224 392,224 395,223.5 398.5,223 401.5,223 404.5,222.5 407.5,222 411,222 414,221.5 417,221 420,221 423,220.5 426.5,220 429.5,220 432.5,219.5 435.5,219 439,219 442,218.5 445,218 448,217.5 451.5,217.5 454.5,217 457.5,216.5 460.5,216 464,216 467,215.5 470,215" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="283" y1="230" x2="283" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="230" x2="283" y2="230" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="283" cy="230" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="262" y="60.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ilman pinnoitetta}$</span></div></foreignObject>
  <foreignObject x="316.5" y="245" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{MgF}_2\text{-pinnoite}$</span></div></foreignObject>
</svg>

## Esimerkki
Saippuakuplan seinämän paksuus on eräässä kohdassa $380\,\text{nm}$, ja saippuaveden taitekerroin on $1{,}33$. Valkoinen valo tulee kohtisuoraan kalvoon. Mitkä näkyvän valon ($400$–$700\,\text{nm}$) aallonpituudet heijastuvat voimakkaimmin?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kalvon paksuus on $d = 380\,\text{nm}$ ja taitekerroin $n = 1{,}33$. Kalvon molemmin puolin on ilmaa.

Kysytään ne aallonpituudet $\lambda$ välillä $400$–$700\,\text{nm}$, joilla interferenssi on vahvistava.

<!-- vaihe -->

**Periaate.** Yläpinnan heijastus ilmasta kalvoon kääntää aallon. Alapinnan heijastus kalvosta ilmaan ei käännä. Heijastuksissa on siis yksi puolen aallonpituuden siirtymä. Siksi vahvistavan interferenssin ehto on $2nd = (k + \tfrac{1}{2})\lambda$. Lasketaan aallonpituus eri $k$:n arvoilla ja valitaan ne, jotka ovat näkyvän valon alueella.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&2nd = (k + \tfrac{1}{2})\lambda \\[6pt]
&\lambda = \frac{2nd}{k + \frac{1}{2}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Paksuus ja aallonpituus ovat kumpikin nanometreinä, ja taitekerroin on yksikötön.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\lambda = \frac{2nd}{k + \frac{1}{2}} \\[6pt]
&k = 1:\ \lambda = \frac{2 \cdot 1{,}33 \cdot 380\,\text{nm}}{1{,}5} \\
&= 673{,}9\,\text{nm} \\[6pt]
&k = 2:\ \lambda = \frac{2 \cdot 1{,}33 \cdot 380\,\text{nm}}{2{,}5} \\
&= 404{,}3\,\text{nm}
\end{aligned}
```
Matkaero on $2nd = 1010{,}8\,\text{nm}$. Arvolla $k = 0$ saadaan $2021{,}6\,\text{nm}$ (infrapunaa). Arvolla $k = 3$ saadaan $288{,}8\,\text{nm}$ (ultraviolettia). Ne eivät ole näkyvää valoa.

<!-- vaihe -->

**Tulos.** Voimakkaimmin heijastuvat punainen valo, jonka aallonpituus on $674\,\text{nm}$, ja violetti valo, jonka aallonpituus on $404\,\text{nm}$. Vastaukset on annettu kolmella merkitsevällä numerolla, koska taitekerroin ja paksuus on annettu niin. Näiden välissä heikentävä ehto $2nd = 2\lambda$ kumoaa vihreänsinisen valon, $1010{,}8\,\text{nm} : 2 = 505\,\text{nm}$. Kalvo näyttää tässä kohdassa punertavan purppuralta.

<!-- vaihe -->

**Järkevyys.** Tarkistus: $(1 + \tfrac{1}{2}) \cdot 673{,}9\,\text{nm} = 1010{,}8\,\text{nm}$ ja $(2 + \tfrac{1}{2}) \cdot 404{,}3\,\text{nm} = 1010{,}8\,\text{nm}$. Kaksi vahvistuvaa aallonpituutta ovat peräkkäiset kertaluvut. Niiden välissä on siksi täsmälleen yksi heikentyvä aallonpituus, kuten pitääkin. Ohuemmassa kalvossa vahvistuvia aallonpituuksia olisi näkyvällä alueella vähemmän ja paksummassa enemmän.

## Yleinen virhekäsitys
Moni ajattelee, että saippuakuplan värit syntyvät samalla tavalla kuin prisman tai sateenkaaren värit, kun valo taittuu eri suuntiin. Kuplan värit syntyvät kuitenkin interferenssistä. Samanpaksuinen kalvo vahvistaa joitakin aallonpituuksia ja heikentää toisia. Väri riippuu siis kalvon paksuudesta.

Toinen virhe on unohtaa heijastuksen puolen aallonpituuden siirtymä. Silloin päätellään, että hyvin ohut kalvo heijastaa voimakkaasti, koska matkaero on nolla.

Kolmas virhe on luulla, että heijastuksenestopinnoite imee heijastuvan valon itseensä. Pinnoite on läpinäkyvä. Heikentävässä interferenssissä valoa heijastuu vähemmän, ja sitä pääsee enemmän lasin läpi.

## Tiivistelmä
- Ohuen kalvon kahdesta pinnasta heijastuneet aallot interferoivat. Kun valo tulee kohtisuoraan, niiden optinen matkaero on $2nd$, koska aallonpituus kalvossa on $\lambda : n$.
- Heijastunut aalto kääntyy eli saa puolen aallonpituuden siirtymän, kun valo heijastuu aineeseen, jolla on suurempi taitekerroin.
- Saippuakalvossa ilmassa on yksi siirtymä. Vahvistava ehto on $2nd = (k + \tfrac{1}{2})\lambda$ ja heikentävä $2nd = k\lambda$. Hyvin ohut kalvo näyttää siksi heijastuneessa valossa lähes mustalta.
- Valkoisessa valossa kalvo näyttää värikkäältä, koska osa aallonpituuksista kumoutuu. Väri vaihtuu kalvon paksuuden mukana.
- Heijastuksen estävässä pinnoitteessa on kaksi siirtymää. Ohuin heikentävä pinnoite on $d = \lambda : (4n)$. Esimerkiksi $\text{MgF}_2$:lla se on $99{,}6\,\text{nm}$ aallonpituudelle $550\,\text{nm}$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: sateen jälkeen asfaltilla on lätäkkö, ja sen pinnalla on ohut öljykalvo. Kalvossa näkyy kiemurtelevia renkaita: sinistä, vihreää, keltaista ja purppuraa. Kalvo on keskeltä paksumpi kuin reunoilta. Värit on laskettu öljykalvolle veden päällä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-14-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
