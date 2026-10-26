# Energiantuotanto ja voimalaitosten hyötysuhde

> **Miksi** voimalaitos tarvitsee polttoainetta noin kaksi ja puoli kertaa enemmän kuin se tuottaa sähköä, ja miten loput energiasta saadaan käyttöön?

## Ydinajatus
Voimalaitos ei tuota energiaa vaan muuttaa sitä. Polttoaineen kemiallinen energia, ydinenergia, virtaavan veden tai tuulen liike-energia ja auringon säteily muuttuvat sähköksi vaihe vaiheelta, ja tätä vaiheiden jonoa sanotaan energiaketjuksi. Energia säilyy jokaisessa vaiheessa, mutta osa siitä siirtyy lämpönä ympäristöön eikä ole enää sähkönä käytettävissä. Hyötysuhde kertoo, kuinka suuri osa vaiheeseen tulevasta tehosta tulee ulos hyödyllisessä muodossa.

Lauhdevoimalaitoksessa ketju on polttoaine, kattila, turbiini ja lauhdutin, generaattori ja muuntaja, sähköverkko. Kattilassa polttoaineen energia siirtyy höyryyn, ja osa poistuu savukaasujen mukana. Turbiinissa höyry laajenee ja pyörittää generaattoria, ja lauhduttimessa höyry tiivistyy takaisin vedeksi. Lauhduttimen kautta siirtyy mereen noin puolet polttoaineen energiasta. Kuva näyttää esimerkkilaitoksen, jonka kaistojen leveydet on piirretty mittakaavassa.

<svg viewBox="0 0 600 400" role="img" aria-label="Virtauskaavio (Sankey) lauhdevoimalaitoksen energiaketjusta. Polttoaineen teho 500 MW kulkee vasemmalta oikealle kaistana, joka kapenee vaihe vaiheelta. Kattilassa savukaasujen mukana menee 40 MW, turbiinissa ja lauhduttimessa lämpönä mereen 248 MW ja generaattorissa ja muuntajassa 12 MW. Sähköä saadaan 200 MW, eli 40 prosenttia polttoaineen tehosta. Kaistojen ja nuolten leveydet ovat mittakaavassa, 100 MW on 40 pikseliä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy315-loss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#ffc078"/></linearGradient><clipPath id="fy315-work"><rect x="349.4" y="0" width="400" height="400"/></clipPath></defs>
  <path d="M160,270 C168,270 168,254 176,254 V300 H160 Z" fill="url(#fy315-loss)" stroke="#e8590c" stroke-width="1.5"/><polygon points="148,300 188,300 168,324" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <path d="M250,254 C300,254 299.4,154.6 349.4,154.6 V330 H250 Z" fill="url(#fy315-loss)" stroke="#e8590c" stroke-width="1.5"/><polygon points="236,330 363.4,330 299.7,366" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <path d="M430,154.6 C432,154.6 431.7,150 434.7,150 V250 H430 Z" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/><polygon points="420,250 444.7,250 432.3,272" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <path d="M20,70 H510 V150 H434.7 C431.7,150 432,154.6 430,154.6 H349.4 C299.4,154.6 300,254 250,254 H176 C168,254 168,270 160,270 H20 Z" fill="#e8590c"/>
  <path d="M20,70 H510 V150 H434.7 C431.7,150 432,154.6 430,154.6 H349.4 C299.4,154.6 300,254 250,254 H176 C168,254 168,270 160,270 H20 Z" fill="#1f2933" clip-path="url(#fy315-work)"/>
  <polygon points="510,56 510,164 550,110" fill="#1f2933"/>
  <foreignObject x="10" y="12" width="320" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{polttoaine } 500\,\text{MW}$</div></foreignObject>
  <foreignObject x="330" y="12" width="262" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{sähkö } 200\,\text{MW}$</div></foreignObject>
  <foreignObject x="4" y="276" width="148" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{savukaasut}$</div></foreignObject>
  <foreignObject x="4" y="316" width="148" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$40\,\text{MW}$</div></foreignObject>
  <foreignObject x="372" y="290" width="224" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{lauhdutin}$</div></foreignObject>
  <foreignObject x="372" y="328" width="224" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="446" y="160" width="150" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{generaattori}$</div></foreignObject>
  <foreignObject x="446" y="196" width="150" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{ja muuntaja}$</div></foreignObject>
  <foreignObject x="446" y="232" width="150" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$12\,\text{MW}$</div></foreignObject>
  <path d="M20,386 H60 M20,378 V394 M60,378 V394" stroke="#1f2933" stroke-width="2.5" fill="none"/>
  <foreignObject x="70" y="368" width="200" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$=100\,\text{MW}$</div></foreignObject>
</svg>

Suurin häviö ei johdu kitkasta tai huonosta tekniikasta. Se on höyrykierron hukkalämpö, jota lämpövoimakone ei voi välttää: osa lämmöstä on luovutettava kylmempään ympäristöön, kuten luvussa Kaasun tekemä työ ja lämpövoimakone nähtiin. Vesivoimala, tuulivoimala ja aurinkopaneeli eivät ole lämpövoimakoneita, joten niillä tätä pakollista häviötä ei ole: vesivoimalan hyötysuhde on noin 90 %, tuulivoimalan 40–45 % ja aurinkopaneelin noin 20 %. Näiden lukujen nimittäjä on kuitenkin virtaavan veden, tuulen tai säteilyn teho eikä ostettu polttoaine, joten ne eivät ole suoraan verrattavissa polttolaitoksen hyötysuhteeseen.

Sähkön ja lämmön yhteistuotannossa lauhduttimen lämpö johdetaan kaukolämpöverkkoon. Jotta vesi lämpenee riittävästi, höyry lauhdutetaan korkeammassa lämpötilassa, ja turbiinista saadaan vähemmän sähköä. Kuvaaja näyttää esimerkkilaitoksen, jonka polttoaineteho on 400 MW: kun kaukolämpöteho kasvaa, sähköteho pienenee vähän, mutta hukkalämpö pienenee paljon enemmän. Kuvaajassa pystysuora matka kerrosten välillä on teho, ja kolmen kerroksen yhteenlaskettu korkeus on aina 400 MW.

<svg viewBox="0 0 600 380" role="img" aria-label="Pinottu pinta-alakuvaaja yhteistuotantolaitoksesta, jonka polttoaineteho on 400 MW. Vaaka-akselilla on kaukolämpöteho 0–250 MW, pystyakselilla teho. Kun kaukolämpöteho kasvaa nollasta 232 MW:iin, sähköteho pienenee 160 MW:sta 120 MW:iin, kaukolämpö kasvaa ja hukkalämpö pienenee 240 MW:sta 48 MW:iin. Kolmen kerroksen yhteenlaskettu korkeus on aina 400 MW. Kuvaaja on mittakaavassa, ja sähkön ja lämmön riippuvuus on likimain suora." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy315-waste" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="10" stroke="#c9c2b2" stroke-width="3"/></pattern></defs>
  <line x1="100" y1="230" x2="560" y2="230" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="170" x2="560" y2="170" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="110" x2="560" y2="110" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="50" x2="560" y2="50" stroke="#e3dccb" stroke-width="2"/>
  <polygon points="100,194 526.9,218 526.9,290 100,290" fill="#1f2933" fill-opacity="0.18"/>
  <polygon points="100,194 526.9,218 526.9,78.8 100,194" fill="#ffc078"/>
  <polygon points="100,194 526.9,78.8 526.9,50 100,50" fill="url(#fy315-waste)"/>
  <line x1="100" y1="194" x2="526.9" y2="218" stroke="#1f2933" stroke-width="4"/>
  <line x1="100" y1="194" x2="526.9" y2="78.8" stroke="#e8590c" stroke-width="4"/>
  <line x1="100" y1="50" x2="560" y2="50" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="8 6"/>
  <line x1="526.9" y1="290" x2="526.9" y2="50" stroke="#6b7480" stroke-width="2" stroke-dasharray="5 5"/>
  <circle cx="100" cy="194" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="526.9" cy="218" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="526.9" cy="78.8" r="6" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="100" y1="290" x2="578" y2="290" stroke="#1f2933" stroke-width="3"/><polygon points="590,290 576,283 576,297" fill="#1f2933"/>
  <line x1="100" y1="290" x2="100" y2="44" stroke="#1f2933" stroke-width="3"/><polygon points="100,32 93,46 107,46" fill="#1f2933"/>
  <line x1="100" y1="290" x2="100" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="70" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0$</div></foreignObject>
  <line x1="284" y1="290" x2="284" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="254" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$100$</div></foreignObject>
  <line x1="468" y1="290" x2="468" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="438" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$200$</div></foreignObject>
  <line x1="92" y1="290" x2="100" y2="290" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="92" y1="230" x2="100" y2="230" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="212" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$100$</div></foreignObject>
  <line x1="92" y1="170" x2="100" y2="170" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="152" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$200$</div></foreignObject>
  <line x1="92" y1="110" x2="100" y2="110" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="92" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$300$</div></foreignObject>
  <line x1="92" y1="50" x2="100" y2="50" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="32" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$400$</div></foreignObject>
  <foreignObject x="380" y="332" width="214" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$P_\text{k}\ (\text{MW})$</div></foreignObject>
  <foreignObject x="104" y="2" width="200" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$P\ (\text{MW})$</div></foreignObject>
  <foreignObject x="250" y="214" width="200" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{sähkö } P_\text{s}$</div></foreignObject>
  <foreignObject x="238" y="148" width="230" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{kaukolämpö } P_\text{k}$</div></foreignObject>
  <foreignObject x="180" y="64" width="220" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{hukkalämpö}$</div></foreignObject>
  <foreignObject x="312" y="8" width="280" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$P_0 = 400\,\text{MW}$</div></foreignObject>
</svg>

Kokonaishyötysuhde nousee yhteistuotannossa jopa 85–90 %:iin, mutta sähkö ja lämpö eivät ole yhtä arvokkaita. Sähköä voi käyttää mihin tahansa, ja sitä voi siirtää satojen kilometrien päähän. Kaukolämpö kelpaa vain lämmitykseen, ja sen verkko ulottuu vain kaupunkiin. Siksi yhteistuotantolaitoksen sähkön ja lämmön suhde valitaan lämmön tarpeen mukaan: kesällä lämpöä tarvitaan vähän ja laitos tuottaa lähes pelkkää sähköä, talvella pakkasella lämpöä tarvitaan paljon.

## Kaava: Voimalaitoksen hyötysuhde
Yhden vaiheen tai koko laitoksen hyötysuhde on hyödyksi saadun tehon suhde sisään tuotuun tehoon, ja hukkalämmön teho on se osa, joka ei tule hyödyksi:
```latex
\eta = \frac{P_\text{hyöty}}{P_0}
```
```latex
P_\text{h} = P_0 - P_\text{hyöty}
```
missä $\eta$ on hyötysuhde (usein prosentteina), $P_\text{hyöty}$ hyödyksi saatu teho (W), $P_0$ sisään tuotu teho, esimerkiksi polttoaineteho (W), ja $P_\text{h}$ hukkalämmön teho (W). Voimalaitoksessa vaiheet ovat peräkkäin. Kunkin vaiheen ulostuleva teho on sen hyötysuhteen ja sisään tulevan tehon tulo:
```latex
\begin{aligned}
P_1 &= \eta_1 P_0 \\
P_2 &= \eta_2 P_1 \\
P_3 &= \eta_3 P_2
\end{aligned}
```
Sijoittamalla ylempi yhtälö alempaan saadaan koko ketjun hyötysuhde:
```latex
\eta = \frac{P_3}{P_0} = \eta_1\,\eta_2\,\eta_3
```
missä $\eta_1$, $\eta_2$ ja $\eta_3$ ovat vaiheiden hyötysuhteet (kattila, höyrykierto, generaattori ja muuntaja) ja $P_3$ on sähköteho. Hyötysuhteet kerrotaan keskenään, ei lasketa yhteen. Koska jokainen tekijä on pienempi kuin 1, ketjun hyötysuhde on pienempi kuin heikoimman vaiheen. Kuvassa pylväät $P_1$, $P_2$ ja $P_3$ saadaan edellisestä pylväästä kertomalla se vaiheen hyötysuhteella $\eta_1$, $\eta_2$ tai $\eta_3$.

<svg viewBox="0 0 600 480" role="img" aria-label="Pylväskuvaaja siitä, miten teho pienenee energiaketjussa. Polttoaineteho P0 on 500 MW, kattilan jälkeen P1 on 460 MW, höyrykierron jälkeen P2 on 212 MW ja generaattorin ja muuntajan jälkeen P3 on 200 MW. Jokainen pylväs on edellistä matalampi, ja pylvään päällä oleva vaalea katkoviivalla rajattu osa on edellisessä vaiheessa hukkaan mennyt teho, ja jokaiseen on merkitty häviö: kattilassa 40 MW, höyrykierrossa 248 MW ja generaattorissa ja muuntajassa 12 MW. Vaiheiden hyötysuhteet ovat 0,92, 0,46 ja 0,945, ja niiden tulo on 0,40. Pylväät ovat mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy315-bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <line x1="30" y1="380" x2="590" y2="380" stroke="#1f2933" stroke-width="3"/>
  <rect x="50" y="130" width="100" height="250" fill="url(#fy315-bar)"/>
  <rect x="190" y="130" width="100" height="20" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="190" y="150" width="100" height="230" fill="url(#fy315-bar)"/>
  <rect x="330" y="150" width="100" height="124.2" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="330" y="274.2" width="100" height="105.8" fill="#1f2933"/>
  <rect x="470" y="274.2" width="100" height="5.8" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="470" y="280" width="100" height="100" fill="#1f2933"/>
  <foreignObject x="170" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_1 = 0{,}92$</div></foreignObject>
  <foreignObject x="310" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_2 = 0{,}46$</div></foreignObject>
  <foreignObject x="450" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_3 = 0{,}945$</div></foreignObject>
  <foreignObject x="40" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_0$</div></foreignObject>
  <foreignObject x="40" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$500\,\text{MW}$</div></foreignObject>
  <foreignObject x="180" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_1$</div></foreignObject>
  <foreignObject x="180" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$460\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_2$</div></foreignObject>
  <foreignObject x="320" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$212\,\text{MW}$</div></foreignObject>
  <foreignObject x="460" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_3$</div></foreignObject>
  <foreignObject x="460" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$200\,\text{MW}$</div></foreignObject>
  <foreignObject x="180" y="54" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="180" y="92" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$40\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="172" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="320" y="210" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="460" y="196" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="460" y="234" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$12\,\text{MW}$</div></foreignObject>
</svg>

Yhteistuotantolaitoksessa hyödyksi saadaan sekä sähkö että kaukolämpö, joten kokonaishyötysuhde on
```latex
\eta_\text{kok} = \frac{P_\text{s} + P_\text{k}}{P_0}
```
missä $P_\text{s}$ on sähköteho (W) ja $P_\text{k}$ kaukolämpöteho (W). Lauhduttimen lämpö lämmittää jäähdytysvettä. Jos vettä virtaa massa $m$ ajassa $t$ ja sen lämpötila nousee $\Delta T$, lämpömäärän $Q = cm\,\Delta T$ avulla lauhduttimen lämpöteho on
```latex
P_\text{L} = c\,q_m\,\Delta T
```
missä $P_\text{L}$ on lauhduttimesta veteen siirtyvä lämpöteho (W), $c$ on veden ominaislämpökapasiteetti (4190 J/(kg·K)), $q_m = m/t$ vesivirta (kg/s) ja $\Delta T$ veden lämpötilan nousu (K). Lauhduttimen lämpöteho on hukkalämmön suurin osa mutta ei koko hukkalämpö $P_\text{h}$: osa hukkalämmöstä lähtee savukaasujen mukana ja generaattorin ja muuntajan häviöinä.

<svg viewBox="0 0 600 310" role="img" aria-label="Lauhduttimen kaaviokuva. Merivesi virtaa putkessa vasemmalta oikealle lauhduttimen läpi, ja sen lämpötila nousee arvosta T1 arvoon T2. Putken väri vaihtuu sinisestä punaiseen. Lauhduttimen yläosassa oleva höyry luovuttaa lämpöä veteen teholla P_L, jota kuvaa oranssi nuoli, ja höyry tiivistyy alaosaan vedeksi. Vesivirta q_m on molemmissa päissä sama. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy315-pipe" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="400" y2="0"><stop offset="0" stop-color="#1971c2"/><stop offset="0.25" stop-color="#1971c2"/><stop offset="0.75" stop-color="#c92a2a"/><stop offset="1" stop-color="#c92a2a"/></linearGradient><linearGradient id="fy315-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <rect x="190" y="70" width="220" height="170" rx="14" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <path d="M193,205 H407 V228 a11,11 0 0 1 -11,11 H204 a11,11 0 0 1 -11,-11 Z" fill="#a9d1f0"/>
  <path d="M30,160 H570" stroke="#1f2933" stroke-width="30" stroke-linecap="butt" fill="none"/>
  <path d="M30,160 H570" stroke="url(#fy315-pipe)" stroke-width="22" stroke-linecap="butt" fill="none"/>
  <polygon points="100,148 100,172 122,160" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <polygon points="478,148 478,172 500,160" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M285,94 H315 V122 H335 L300,148 L265,122 H285 Z" fill="url(#fy315-heat)"/>
  <foreignObject x="196" y="72" width="80" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{höyry}$</div></foreignObject>
  <foreignObject x="328" y="88" width="76" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_\text{L}$</div></foreignObject>
  <foreignObject x="246" y="200" width="108" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{lauhde}$</div></foreignObject>
  <foreignObject x="6" y="100" width="184" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{merivesi sisään}$</div></foreignObject>
  <foreignObject x="30" y="184" width="110" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$T_1$</div></foreignObject>
  <foreignObject x="414" y="100" width="184" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\text{merivesi ulos}$</div></foreignObject>
  <foreignObject x="414" y="184" width="180" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$T_2 = T_1 + \Delta T$</div></foreignObject>
  <foreignObject x="140" y="256" width="320" height="50"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$q_m = \dfrac{m}{t}$</div></foreignObject>
</svg>

## Esimerkki
Lauhdevoimalaitoksen polttoaineteho on 600 MW. Kattilan hyötysuhde on 0,910, höyrykierron 0,440 ja generaattorin ja muuntajan 0,950. Mikä on laitoksen sähköteho, mikä on koko laitoksen hyötysuhde ja kuinka suuri teho siirtyy ympäristöön hukkalämpönä?

<!-- vaihe -->
**Tunnetut ja kysytty.** Polttoaineteho $P_0 = 600\,\text{MW}$ ja vaiheiden hyötysuhteet $\eta_1 = 0{,}910$, $\eta_2 = 0{,}440$ ja $\eta_3 = 0{,}950$. Kysytään sähkötehoa $P_3$, koko ketjun hyötysuhdetta $\eta$ ja hukkalämmön tehoa $P_\text{h}$.

<!-- vaihe -->
**Kaavat ratkaistuina.** Hyötysuhteet kerrotaan, ja hukkalämpö on se osa, joka ei muutu sähköksi:
```latex
\begin{aligned}
P_3 &= \eta_1\,\eta_2\,\eta_3\,P_0 \\
\eta &= \frac{P_3}{P_0} \\
P_\text{h} &= P_0 - P_3
\end{aligned}
```

<!-- vaihe -->
**Sijoitus.** Vaiheiden jälkeiset tehot ovat $P_1 = \eta_1 P_0 = 546\,\text{MW}$ ja $P_2 = \eta_2 P_1 \approx 240\,\text{MW}$. Sähköteho on
```latex
\begin{aligned}
P_3 &= \eta_1\,\eta_2\,\eta_3\,P_0 \\
&= 0{,}910 \cdot 0{,}440 \cdot 0{,}950 \cdot 600\,\text{MW} \\
&= 0{,}38038 \cdot 600\,\text{MW} \\
&\approx 228\,\text{MW}
\end{aligned}
```

<!-- vaihe -->
**Tulos.** Koko ketjun hyötysuhde on tulo $0{,}38038$, joten
```latex
\begin{aligned}
\eta &= \frac{P_3}{P_0} \\
&\approx 0{,}380 = 38{,}0\,\% \\
P_\text{h} &= P_0 - P_3 \\
&= 600\,\text{MW} - 228\,\text{MW} \\
&= 372\,\text{MW}
\end{aligned}
```

<!-- vaihe -->
**Järkevyys.** Hyötysuhde on pienempi kuin heikoimman vaiheen 0,440, kuten tulon pitääkin, ja sopii lauhdevoimalaitoksen tavalliseen 35–45 %:iin. Lauhduttimeen siirtyy teho $P_1 - P_2 \approx 546\,\text{MW} - 240\,\text{MW} = 306\,\text{MW}$, eli yli puolet polttoaineen energiasta.

Kattilan häviö on vain 54 MW ja generaattorin ja muuntajan 12 MW, joten parannukset kannattaa kohdistaa höyrykiertoon ja sen jälkeen lauhduttimen lämmön käyttöön.

## Yleinen virhekäsitys
Moni ajattelee, että hukkalämpö on energiaa, joka on kadonnut. Energia ei katoa: se siirtyy lämpönä mereen tai ilmaan, jossa sen lämpötila on niin matala, ettei sitä voi enää muuttaa sähköksi. Yhteistuotannossa sama lämpö johdetaan kaukolämpöverkkoon ja lämmittää koteja.

Toinen virhe on laskea vaiheiden hyötysuhteet yhteen tai ottaa niiden keskiarvo. Kun kolmen vaiheen hyötysuhteet ovat 0,92, 0,46 ja 0,945, ketjun hyötysuhde on niiden tulo 0,40, ei keskiarvo 0,78. Kolmas virhe on pitää yhteistuotannon 88 %:n kokonaishyötysuhdetta merkkinä siitä, että kaikki energia olisi yhtä arvokasta: sähköä voi käyttää kaikkeen, kaukolämpöä vain lämmitykseen.

## Tiivistelmä
- Voimalaitos muuttaa energiaa vaihe vaiheelta energiaketjussa, ja jokaisessa vaiheessa osa siirtyy lämpönä ympäristöön.
- Hyötysuhde on $\eta = P_\text{hyöty}/P_0$, ja hukkalämmön teho on $P_\text{h} = P_0 - P_\text{hyöty}$.
- Ketjun hyötysuhde on vaiheiden hyötysuhteiden tulo, $\eta = \eta_1\,\eta_2\,\eta_3$, ja se on pienempi kuin heikoimman vaiheen.
- Lauhdevoimalaitoksen suurin häviö on höyrykierron lauhduttimeen siirtyvä lämpö, jota lämpövoimakone ei voi välttää. Hyötysuhde on noin 40 %.
- Yhteistuotannossa lauhduttimen lämpö johdetaan kaukolämpöverkkoon, ja kokonaishyötysuhde on $\eta_\text{kok} = (P_\text{s} + P_\text{k})/P_0$, noin 85–90 %. Sähköä saadaan silloin vähemmän.
- Vesivoimala, tuulivoimala ja aurinkopaneeli eivät ole lämpövoimakoneita, mutta niiden hyötysuhteiden nimittäjä on virtaavan veden, tuulen tai säteilyn teho, ei ostettu polttoaine.
- Lauhduttimen jäähdytysvesi saa lämpötehon $P_\text{L} = c\,q_m\,\Delta T$, joka on hukkalämmön suurin osa.
