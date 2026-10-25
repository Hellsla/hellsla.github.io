# Lämpölaajeneminen

> **Miksi** pitkän sillan päässä on kampamainen teräsliitos, jonka yli auton renkaat kolahtavat?

## Ydinajatus
Lähes kaikki aineet laajenevat lämmetessään ja kutistuvat jäähtyessään. Ilmiötä sanotaan lämpölaajenemiseksi. Mikromalli selittää sen. Kiinteässä aineessa hiukkaset värähtelevät tasapainoasemiensa ympärillä. Kun lämpötila nousee, värähtely voimistuu. Hiukkasten on helpompi loitota toisistaan kuin puristua lähemmäs toisiaan, joten voimakkaammin värähtelevien hiukkasten keskimääräinen etäisyys kasvaa. Hiukkaset itse eivät suurene, vaan niiden väliset etäisyydet kasvavat, ja koko kappale laajenee.

Muutos on pieni mutta voimakas. Teräksinen sauva pitenee vain noin sadastuhannesosan pituudestaan jokaista kelviniä kohti, mutta jos sauvan päät on kiinnitetty, laajeneva teräs työntää niitä valtavalla voimalla. Siksi pitkissä rakenteissa on liikuntasaumoja. Sillan teräskansi on talvipakkasella lyhyempi kuin kesähelteellä, ja kampamainen liitos sillan päässä antaa kannen liikkua vapaasti. Samasta syystä sähkölinjat roikkuvat helteellä alempana kuin pakkasella.

Kappale laajenee kaikkiin suuntiin samassa suhteessa, kuin valokuvaa suurennettaessa. Myös reikä levyssä suurenee, kun levy lämpenee. Tätä käytetään kutistusliitoksessa: kuumennettu teräsrengas pujotetaan akselille, ja jäähtyessään se puristuu tiukasti kiinni. Eri aineet laajenevat eri tavalla. Kaksoismetalliliuska, jossa kaksi eri metallia on liitetty toisiinsa, taipuu lämmetessään, koska toinen metalli pitenee enemmän. Sellainen liuska avaa ja sulkee virtapiirin vanhanmallisissa termostaateissa.

Nesteet laajenevat yleensä selvästi enemmän kuin kiinteät aineet, ja kaasut vielä paljon enemmän. Nestelämpömittari perustuu nesteen laajenemiseen: kun lämpötila nousee, nestepatsas kohoaa ohuessa putkessa. Kaasun tilavuus riippuu lisäksi paineesta, ja kaasuja tarkastellaan kaasulakien avulla. Vesi on poikkeus: 0 °C:n ja 4 °C:n välillä se kutistuu lämmetessään, joten sen tiheys on suurin noin 4 °C:ssa. Siksi järvi jäätyy pinnalta alkaen, ja pohjalla on talvellakin noin 4-asteista vettä, jossa kalat selviävät.

## Kaava
Kun kappaleen lämpötila muuttuu ΔT, sen pituus muuttuu
```latex
\Delta L = \alpha L_0 \Delta T
```
missä ΔL on pituuden muutos (m), α pituuden lämpötilakerroin (1/K), L₀ alkuperäinen pituus (m) ja ΔT lämpötilan muutos (K). Uusi pituus on L = L₀ + ΔL. Jäähtyessä ΔT on negatiivinen, joten myös ΔL on negatiivinen eli kappale lyhenee.

Nesteiden ja kaasujen tilavuuden muutos lasketaan samalla tavalla:
```latex
\Delta V = \gamma V_0 \Delta T
```
missä ΔV on tilavuuden muutos (m³), γ tilavuuden lämpötilakerroin (1/K) ja V₀ alkuperäinen tilavuus (m³). Kiinteällä aineella γ ≈ 3α, koska kappale laajenee kaikkiin kolmeen suuntaan. Kaavat ovat hyviä malleja, kun lämpötilan muutos on kohtuullinen, esimerkiksi muutamia kymmeniä kelvinejä.

| Aine | α (10⁻⁶ 1/K) |
| --- | --- |
| teräs | 12 |
| alumiini | 23 |
| kupari | 17 |
| tavallinen lasi | 9 |
| borosilikaattilasi | 3,3 |

| Aine (20 °C) | γ (10⁻³ 1/K) |
| --- | --- |
| vesi | 0,21 |
| etanoli | 1,1 |
| bensiini | 0,95 |
| ilma (vakiopaineessa) | 3,4 |

<svg viewBox="0 0 600 300" role="img" aria-label="Sama sauva kylmänä ja lämpimänä: lämmin sauva on pidempi, ja pituuden muutos ΔL on merkitty sauvan päähän. Laajeneminen on piirretty liioiteltuna." style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <text x="60" y="52" fill="currentColor">kylmä, lämpötila T₀</text>
  <rect x="60" y="64" width="400" height="40" fill="currentColor" fill-opacity="0.25" stroke="currentColor" stroke-width="2"/>
  <text x="260" y="91" text-anchor="middle" fill="currentColor">L₀</text>
  <text x="60" y="152" fill="currentColor">lämmin, lämpötila T₀ + ΔT</text>
  <rect x="60" y="164" width="470" height="40" fill="currentColor" fill-opacity="0.45" stroke="currentColor" stroke-width="2"/>
  <text x="260" y="191" text-anchor="middle" fill="currentColor">L₀ + ΔL</text>
  <line x1="460" y1="56" x2="460" y2="236" stroke="currentColor" stroke-width="2" stroke-dasharray="6 5"/>
  <line x1="466" y1="228" x2="524" y2="228" stroke="currentColor" stroke-width="2"/>
  <polygon points="460,228 470,222 470,234" fill="currentColor"/>
  <polygon points="530,228 520,222 520,234" fill="currentColor"/>
  <text x="495" y="258" text-anchor="middle" fill="currentColor">ΔL</text>
  <text x="590" y="290" text-anchor="end" fill="currentColor">laajeneminen liioiteltu</text>
</svg>

## Esimerkki
Teräksisen sillan kansi on 120 m pitkä. Paikkakunnalla lämpötila vaihtelee vuoden aikana −30 °C:n pakkasesta +30 °C:n helteeseen, ja teräksen pituuden lämpötilakerroin on 12 · 10⁻⁶ 1/K. Kuinka paljon kannen pituus muuttuu, eli kuinka paljon liikuntasauman on vähintään annettava periksi?

Lämpötilan muutos on $\Delta T = 30\,°\text{C} - (-30\,°\text{C}) = 60\,\text{K}$. Pituuden muutos on
```latex
\Delta L = 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}} \cdot 120\,\text{m} \cdot 60\,\text{K} = 0{,}0864\,\text{m} \approx 86\,\text{mm}
```
Kansi pitenee kesään mennessä lähes yhdeksän senttimetriä. Se on vain 0,07 % kannen pituudesta, mutta ilman liikuntasaumaa laajeneva teräs työntäisi sillan päitä niin suurella voimalla, että rakenteet vaurioituisivat. Siksi sillan päässä on kampamainen liitos, jonka hampaat liukuvat toistensa lomassa.

## Yleinen virhekäsitys
Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee, kun levy laajenee ”reiän sisään päin”. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään: vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja siksi jää kelluu ja järvet jäätyvät pinnalta.

## Tiivistelmä
- Lämmetessä hiukkasten värähtely voimistuu ja niiden keskimääräinen etäisyys kasvaa, joten aine laajenee.
- Pituuden muutos on $\Delta L = \alpha L_0 \Delta T$ ja tilavuuden muutos $\Delta V = \gamma V_0 \Delta T$. Kiinteällä aineella γ ≈ 3α.
- Nesteet laajenevat enemmän kuin kiinteät aineet ja kaasut paljon enemmän kuin nesteet.
- Kappale laajenee kaikkiin suuntiin samassa suhteessa, joten myös reiät suurenevat.
- Vesi on poikkeus: sen tiheys on suurin noin 4 °C:ssa.
