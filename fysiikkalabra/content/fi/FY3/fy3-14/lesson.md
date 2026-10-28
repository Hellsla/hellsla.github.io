# Lämpötasapaino olomuodon muuttuessa

> **Miksi** jääpalat viilentävät juomaa niin tehokkaasti, vaikka jää itse on vain nollan asteen lämpöistä? Entä miksi lasin pohjalle voi jäädä jäätä, vaikka juoma oli huoneenlämpöistä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pöydällä on korkea lasi kylmää juomaa, jossa kelluu jääpaloja ja pilli. Lasin ulkopinnalle on tiivistynyt vesipisaroita, ja lasin vieressä on jääpalarasia." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy314h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f6f1e6"/></linearGradient><linearGradient id="fy314h-drink" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d0e6fb"/><stop offset="1" stop-color="#a9d1f0"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="380" fill="url(#fy314h-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="#c9c2b2"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110 Z" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M506,190 L521,458 Q523,470 536,470 H664 Q677,470 679,458 L694,190 Z" fill="url(#fy314h-drink)" stroke-linejoin="round"/>
  <path d="M640,60 L600,440" fill="none" stroke="#1971c2" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="540" y="170" width="52" height="46" rx="8" transform="rotate(-12 566 193)" fill="#a5d8ff" fill-opacity="0.9" stroke="#4f8fbf" stroke-width="2.5"/>
  <rect x="600" y="184" width="52" height="46" rx="8" transform="rotate(10 626 207)" fill="#a5d8ff" fill-opacity="0.9" stroke="#4f8fbf" stroke-width="2.5"/>
  <rect x="560" y="240" width="52" height="46" rx="8" transform="rotate(24 586 263)" fill="#a5d8ff" fill-opacity="0.9" stroke="#4f8fbf" stroke-width="2.5"/>
  <rect x="628" y="250" width="52" height="46" rx="8" transform="rotate(-8 654 273)" fill="#a5d8ff" fill-opacity="0.9" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M506,190 Q560,182 600,190 T694,190" fill="none" stroke="#ffffff" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.8"/>
  <path d="M500,110 L520,460 Q522,474 536,474 H664 Q678,474 680,460 L700,110" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <ellipse cx="522" cy="290.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="539.5" cy="443.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="531.5" cy="258.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="654.5" cy="265.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="547" cy="214" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="545" cy="226.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="631.5" cy="350.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="676" cy="419.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="630" cy="343" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="683.5" cy="228.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="665.5" cy="357" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="605" cy="266" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="674" cy="328.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="604.5" cy="240" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="568.5" cy="261.5" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <ellipse cx="632.5" cy="366" rx="4" ry="6" fill="#ffffff" stroke="#4f8fbf" stroke-width="1.5"/>
  <rect x="800" y="430" width="260" height="40" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <rect x="816" y="420" width="42" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="872" y="420" width="42" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="928" y="420" width="42" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="984" y="420" width="42" height="30" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <path d="M430,200 c-14,30 14,60 0,90 s14,60 0,90" fill="none" stroke="#d0e6fb" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M760,200 c-14,30 14,60 0,90 s14,60 0,90" fill="none" stroke="#d0e6fb" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
</svg>

## Ydinajatus
Kun eristettyyn astiaan laitetaan lämmintä vettä ja jäätä, lämpöä siirtyy vedestä jäähän, kunnes lämpötilat ovat samat ja astiassa on lämpötasapaino. Energia säilyy, joten veden luovuttama lämpömäärä on yhtä suuri kuin jään vastaanottama. Jään vastaanottama energia ei kuitenkaan vain nosta lämpötilaa: jää lämpenee ensin $0\,{}^\circ\text{C}$:seen ja sulaa sitten. Sulamisen aikana lämpötila pysyy vakiona, mutta jokainen kilogramma jäätä ottaa energiaa $334\,\text{kJ}$, ja sama energia nostaisi kilogramman vettä lähes $80\,\text{K}$.

<svg viewBox="0 0 600 344" role="img" aria-label="Kaavakuva ennen ja jälkeen: eristetyssä astiassa on aluksi 0,30 kg vettä lämpötilassa 20 °C ja 0,10 kg jäätä lämpötilassa 0 °C. Lämpöä Q siirtyy vedestä jäähän. Tasapainossa lämpömittari näyttää 0 °C, vettä on 0,375 kg ja jäätä on jäljellä enää 0,025 kg. Jääpalojen yhteenlaskettu pinta-ala on mittakaavassa jään massaan nähden." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy314-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy314-heat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M78,96 V250 Q78,262 90,262 H216 Q228,262 228,250 V96 Z" fill="#eef5f9"/>
  <path d="M80,138 Q98.25,131 116.5,138 T153.0,138 T189.5,138 T226,138 V250 Q226,260 214,260 H92 Q80,260 80,250 Z" fill="url(#fy314-water)"/>
  <path d="M83,138 Q98.25,132 116.5,138 T153.0,138 T189.5,138 T223,138" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>
  <rect x="84.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M90.0,132.6 V126.0 H96.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="120.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M126.0,132.6 V126.0 H132.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="156.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M162.0,132.6 V126.0 H168.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="192.0" y="120.0" width="30" height="30" rx="4.0" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M198.0,132.6 V126.0 H204.6" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <path d="M147.0,232 V196 H138.0 L153.0,172 L168.0,196 H159.0 V232 Z" fill="url(#fy314-heat)"/>
  <rect x="173.0" y="192" width="40" height="36" rx="6" fill="#ffffff" fill-opacity="0.88"/>
  <foreignObject x="173.0" y="190" width="40" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$Q$</div></foreignObject>
  <path d="M78,96 V250 Q78,262 90,262 H216 Q228,262 228,250 V96" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="41" y="96" width="14" height="170" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <g stroke="#6b7480" stroke-width="1.5"><line x1="35" y1="232" x2="41" y2="232"/><line x1="35" y1="192" x2="41" y2="192"/><line x1="35" y1="152" x2="41" y2="152"/><line x1="35" y1="112" x2="41" y2="112"/></g>
  <rect x="45" y="152" width="6" height="106" fill="#c92a2a"/>
  <circle cx="48" cy="258" r="12" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="-2" y="218" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="-2" y="178" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="-2" y="138" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="-2" y="98" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="8" y="56" width="80" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="53.0" y="4" width="200" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{alussa}$</div></foreignObject>
  <foreignObject x="31.0" y="276" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{vesi } 0{,}30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="31.0" y="309" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{jää } 0{,}10\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
  <path d="M252,166 H306 V152 L334,174 L306,196 V182 H252 Z" fill="#1f2933"/>
  <path d="M400,96 V250 Q400,262 412,262 H538 Q550,262 550,250 V96 Z" fill="#eef5f9"/>
  <path d="M402,138 Q420.25,131 438.5,138 T475.0,138 T511.5,138 T548,138 V250 Q548,260 536,260 H414 Q402,260 402,250 Z" fill="url(#fy314-water)"/>
  <path d="M405,138 Q420.25,132 438.5,138 T475.0,138 T511.5,138 T545,138" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.8"/>
  <rect x="413.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M416.5,135.3 V132.0 H419.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="449.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M452.5,135.3 V132.0 H455.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="485.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M488.5,135.3 V132.0 H491.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <rect x="521.5" y="129.0" width="15" height="15" rx="3.8" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2.5"/>
  <path d="M524.5,135.3 V132.0 H527.8" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
  <path d="M400,96 V250 Q400,262 412,262 H538 Q550,262 550,250 V96" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="363" y="96" width="14" height="170" rx="7" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <g stroke="#6b7480" stroke-width="1.5"><line x1="357" y1="232" x2="363" y2="232"/><line x1="357" y1="192" x2="363" y2="192"/><line x1="357" y1="152" x2="363" y2="152"/><line x1="357" y1="112" x2="363" y2="112"/></g>
  <rect x="367" y="232" width="6" height="26" fill="#1971c2"/>
  <circle cx="370" cy="258" r="12" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="320" y="218" width="34" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="330" y="56" width="80" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="375.0" y="4" width="200" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{tasapainossa}$</div></foreignObject>
  <foreignObject x="353.0" y="276" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{vesi } 0{,}375\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="353.0" y="309" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{jää } 0{,}025\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
</svg>

Siksi lopputilan lämpötilaa ei saa alkulämpötilojen keskiarvona. Lopputilanteita on neljä. Jos vesi voi jäähtyessään luovuttaa tarpeeksi lämpöä kaiken jään sulattamiseen, kaikki jää sulaa ja seoksen lämpötila on vähintään $0\,{}^\circ\text{C}$: tasan $0\,{}^\circ\text{C}$, jos lämpö riittää juuri ja juuri, ja muuten yli $0\,{}^\circ\text{C}$. Jos lämpö ei riitä, astiaan jää sekä jäätä että vettä, ja niin kauan kuin kumpaakin on, lämpötila on tasan $0\,{}^\circ\text{C}$. Jos jää on hyvin kylmää ja vettä on vähän, osa vedestä tai kaikki vesi jäätyy; vasta kun kaikki vesi on jäätynyt, lämpötila on alle $0\,{}^\circ\text{C}$. Ratkaisu alkaa aina samasta vertailusta: lasketaan, paljonko lämpöä vesi voi luovuttaa ja paljonko jää tarvitsee sulaakseen kokonaan.

## Kaava: Lämpötasapaino ja sulaminen
Eristetyssä astiassa on vettä, jonka massa on $m_\text{v}$ ja lämpötila $T_\text{v} > 0\,{}^\circ\text{C}$, sekä jäätä, jonka massa on $m_\text{j}$ ja lämpötila $T_\text{j} \le 0\,{}^\circ\text{C}$. Vertaillaan kahta lämpömäärää: sitä, jonka vesi voi luovuttaa jäähtyessään $0\,{}^\circ\text{C}$:seen, ja sitä, jonka jää tarvitsee lämmetäkseen $0\,{}^\circ\text{C}$:seen ja sulaakseen kokonaan:
```latex
\begin{aligned}
Q_\text{v} &= c_\text{v} m_\text{v} T_\text{v} \\
Q_\text{j} &= c_\text{j} m_\text{j} \Delta T_\text{j} + s m_\text{j}
\end{aligned}
```
missä $Q_\text{v}$ on veden luovuttama lämpömäärä (J), $c_\text{v}$ veden ja $c_\text{j}$ jään ominaislämpökapasiteetti (J/(kg·K)), $T_\text{v}$ veden lämpötila celsiusasteina (sama luku kuin lämpötilan muutos $0\,{}^\circ\text{C}$:seen kelvineinä), $Q_\text{j}$ jään tarvitsema lämpömäärä (J), $\Delta T_\text{j} = 0\,{}^\circ\text{C} - T_\text{j}$ jään lämpötilan nousu (K) ja $s$ jään ominaissulamislämpö (J/kg). Termeistä ensimmäinen lämmittää jään $0\,{}^\circ\text{C}$:seen ja toinen sulattaa sen.

<svg viewBox="0 0 600 392" role="img" aria-label="Energiataseen palkit mittakaavassa, kilojouleina: 0,30 kg vettä lämpötilassa 20 °C luovuttaa jäähtyessään 0 °C:seen 25.1 kJ. 0,10 kg jäätä lämpötilassa −10 °C tarvitsee lämpenemiseen 0 °C:seen 2.1 kJ ja sulamiseen 33.4 kJ eli yhteensä 35.5 kJ. Veden lämpö ei riitä: palkin vaalea osa kuvaa jäätä, joka ei ehdi sulaa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy314-heat2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <line x1="100" y1="272.0" x2="590" y2="272.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="212.0" x2="590" y2="212.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="152.0" x2="590" y2="152.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="92.0" x2="590" y2="92.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="332" x2="590" y2="332" stroke="#1f2933" stroke-width="2.5"/><line x1="100" y1="68.0" x2="100" y2="332" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="318.0" width="56" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="36" y="258.0" width="56" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="36" y="198.0" width="56" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="36" y="138.0" width="56" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="36" y="78.0" width="56" height="28"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="20" y="6" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$Q\ (\text{kJ})$</div></foreignObject>
  <foreignObject x="290" y="2" width="306" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{vesi } 0{,}30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="290" y="38" width="306" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{jää } 0{,}10\,\text{kg},\ {-10}\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="150" y="181.2" width="100" height="150.8" rx="3" fill="url(#fy314-heat2)" stroke="#1f2933" stroke-width="2"/>
  <rect x="350" y="319.4" width="100" height="12.6" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <rect x="350" y="181.2" width="100" height="138.2" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="350" y="119.0" width="100" height="62.2" fill="#a5d8ff" fill-opacity="0.35" stroke="#4f8fbf" stroke-width="2" stroke-dasharray="7 5"/>
  <line x1="250" y1="181.2" x2="460" y2="181.2" stroke="#1f2933" stroke-width="2" stroke-dasharray="7 5"/>
  <path d="M460,119.0 H466 V181.2 H460" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="472" y="133.07999999999998" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{jäätä jää}$</div></foreignObject>
  <foreignObject x="356" y="153.07999999999998" width="90" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$s\,m_\text{j}$</div></foreignObject>
  <foreignObject x="472" y="292.7" width="120" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{lämmitys}$</div></foreignObject>
  <line x1="450" y1="325.7" x2="468" y2="309.7" stroke="#6b7480" stroke-width="1.5"/>
  <foreignObject x="130" y="143.16" width="140" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$25{,}1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="330" y="81.0" width="140" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$35{,}5\,\text{kJ}$</div></foreignObject>
  <foreignObject x="110" y="338" width="180" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{vesi luovuttaa}$</div></foreignObject>
  <foreignObject x="310" y="338" width="180" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{jää tarvitsee}$</div></foreignObject>
</svg>

| Suure | Arvo |
| --- | --- |
| veden $c_\text{v}$ | $4190\,\text{J/(kg}\cdot\text{K)}$ |
| jään $c_\text{j}$ | $2100\,\text{J/(kg}\cdot\text{K)}$ |
| jään $s$ | $334\,\text{kJ/kg}$ |

Jos $Q_\text{v} \ge Q_\text{j}$, kaikki jää sulaa. Silloin veden luovuttama lämpö kuluu jään lämmittämiseen ja sulattamiseen, ja loput lämmittää koko vesimäärän $m_\text{v} + m_\text{j}$ lämpötilaan $T$. Energiatase on
```latex
\begin{aligned}
&c_\text{v} m_\text{v} (T_\text{v} - T) \\
&\quad = c_\text{j} m_\text{j} \Delta T_\text{j} + s m_\text{j} \\
&\qquad + c_\text{v} m_\text{j} T
\end{aligned}
```
missä vasen puoli on veden luovuttama lämpömäärä ja oikealla ovat jään lämpeneminen, jään sulaminen ja sulamisveden lämpeneminen. Ratkaistuna
```latex
T = \frac{Q_\text{v} - Q_\text{j}}{c_\text{v} (m_\text{v} + m_\text{j})}
```
Rajatapauksessa $Q_\text{v} = Q_\text{j}$ kaava antaa $T = 0\,{}^\circ\text{C}$: kaikki jää on juuri sulanut, mutta sulamisvesi ei lämpene.

Jos $Q_\text{v} < Q_\text{j}$, mutta vesi riittää lämmittämään jään $0\,{}^\circ\text{C}$:seen, kaikki jää ei ehdi sulaa. Astiassa on silloin jäätä ja vettä yhtä aikaa, joten $T = 0\,{}^\circ\text{C}$. Sulaneen jään massa $m_\text{s}$ saadaan siitä lämmöstä, joka jää jäljelle jään lämmittämisen jälkeen:
```latex
m_\text{s} = \frac{Q_\text{v} - c_\text{j} m_\text{j} \Delta T_\text{j}}{s}
```
Jäljelle jäävän jään massa on $m_\text{j} - m_\text{s}$. Kuvaaja näyttää, miten lopputilan lämpötila riippuu veden alkulämpötilasta, kun vettä on $0{,}30\,\text{kg}$ ja 0-asteista jäätä $0{,}10\,\text{kg}$: kunnes veden luovuttama lämpö riittää sulattamaan jään, lämpötila pysyy $0\,{}^\circ\text{C}$:ssa, ja sen jälkeen se nousee. Musta piste on ensimmäisen kuvan lasi, jossa vesi on 20-asteista.

<svg viewBox="0 0 600 394" role="img" aria-label="Kaavan kuvaaja: 0,30 kg veden ja 0,10 kg 0-asteisen jään lopputilan lämpötila T veden alkulämpötilan Tv funktiona. Kun Tv on alle 26,6 °C, jäätä jää jäljelle ja T on 0 °C; rajalla kaikki jää juuri sulaa ja T on yhä 0 °C. Tämän jälkeen kaikki jää sulaa ja T nousee suoraviivaisesti, 40 °C:seen veden alkulämpötilassa 80 °C. Akselit on piirretty mittakaavassa." style="max-width:100%;font-size:24px">
  <rect x="100" y="70" width="152.8" height="240" fill="#d0e6fb" fill-opacity="0.55"/>
  <line x1="100" y1="250.0" x2="560" y2="250.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="190.0" x2="560" y2="190.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="130.0" x2="560" y2="130.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="70.0" x2="560" y2="70.0" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="215.0" y1="70" x2="215.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="330.0" y1="70" x2="330.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="445.0" y1="70" x2="445.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="560.0" y1="70" x2="560.0" y2="310" stroke="#e3dccb" stroke-width="1.5"/>
  <line x1="100" y1="310" x2="570" y2="310" stroke="#1f2933" stroke-width="2.5"/><line x1="100" y1="310" x2="100" y2="60" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="72.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="187.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="302.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="417.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$60$</div></foreignObject>
  <foreignObject x="532.0" y="322" width="56" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center;color:#6b7480">$80$</div></foreignObject>
  <foreignObject x="36" y="295.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="36" y="235.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$10$</div></foreignObject>
  <foreignObject x="36" y="175.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$20$</div></foreignObject>
  <foreignObject x="36" y="115.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="36" y="55.0" width="52" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="6" y="6" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$T\ (^\circ\text{C})$</div></foreignObject>
  <foreignObject x="340" y="358" width="250" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$T_\text{v}\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="100.0,310.0 252.8,310.0 560.0,69.6" fill="none" stroke="#c92a2a" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="252.8" y1="310.0" x2="252.8" y2="70" stroke="#6b7480" stroke-width="2" stroke-dasharray="6 5"/>
  <circle cx="252.8" cy="310.0" r="6.5" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="215.0" cy="310.0" r="6.5" fill="#1f2933"/>
  <foreignObject x="246.78440731901352" y="62" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$26{,}6\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="108" y="76" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{jäätä jää}$</div></foreignObject>
  <foreignObject x="108" y="110" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$T = 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="350" y="256.0" width="220" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{kaikki jää sulaa}$</div></foreignObject>
  <foreignObject x="135.0" y="260.0" width="110" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{alun lasi}$</div></foreignObject>
</svg>

Jos $Q_\text{v}$ ei riitä edes jään lämmittämiseen $0\,{}^\circ\text{C}$:seen, kylmä jää jäädyttää osan vedestä. Niin kauan kuin vettä jää, jäätä ja vettä on yhtä aikaa ja lämpötila on $0\,{}^\circ\text{C}$. Vasta jos kaikki vesi jäätyy, jäämassa jäähtyy alle $0\,{}^\circ\text{C}$:n; sen lämpötila ratkaistaan samasta energiataseesta tason 3 tehtävässä.

## Esimerkki
Kalorimetrissä on $0{,}250\,\text{kg}$ vettä, jonka lämpötila on $24{,}0\,{}^\circ\text{C}$. Veteen pudotetaan $0{,}050\,\text{kg}$ jäätä, jonka lämpötila on $-8{,}0\,{}^\circ\text{C}$. Sulaako kaikki jää, ja mikä on kalorimetrin sisällön lämpötila lämpötasapainossa? Kalorimetrin oma lämpökapasiteetti ja lämpöhäviöt ympäristöön jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** Vesi: $m_\text{v} = 0{,}250\,\text{kg}$, $T_\text{v} = 24{,}0\,{}^\circ\text{C}$. Jää: $m_\text{j} = 0{,}050\,\text{kg}$, $T_\text{j} = -8{,}0\,{}^\circ\text{C}$. Taulukosta $c_\text{v} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, $c_\text{j} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ ja $s = 334\,\tfrac{\text{kJ}}{\text{kg}}$. Kysytään, sulaako kaikki jää, ja lopputilan lämpötilaa $T$.

<!-- vaihe -->

**Periaate.** Energia säilyy, koska kalorimetri ei ota lämpöä eikä lämpöä karkaa ympäristöön: veden luovuttama lämpömäärä on yhtä suuri kuin jään vastaanottama. Jää lämpenee ensin $0\,{}^\circ\text{C}$:seen, sulaa sitten vakiolämpötilassa ja sulamisvesi lämpenee lopuksi lopputilan lämpötilaan. Siksi on ensin tarkistettava, riittääkö veden luovuttama lämpö kaiken jään lämmittämiseen ja sulattamiseen. Jos riittää, jää sulaa kokonaan, eikä lopputilan lämpötila ole alle $0\,{}^\circ\text{C}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Vesi luovuttaa jäähtyessään $0\,{}^\circ\text{C}$:seen lämpömäärän $Q_\text{v}$, ja jää tarvitsee sulaakseen lämpömäärän $Q_\text{j}$. Kun $Q_\text{v} > Q_\text{j}$, ylijäämä lämmittää kaiken veden ($m_\text{v} + m_\text{j}$) lämpötilaan $T$:
```latex
\begin{aligned}
&Q_\text{v} = c_\text{v} m_\text{v} T_\text{v} \\
&Q_\text{j} = c_\text{j} m_\text{j} \Delta T_\text{j} + s m_\text{j} \\[6pt]
&T = \frac{Q_\text{v} - Q_\text{j}}{c_\text{v} (m_\text{v} + m_\text{j})}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massat ovat jo kilogrammoina. Lämpötilan muutos on sama kelvineinä ja celsiusasteina: vesi jäähtyy $24{,}0\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 24{,}0\,\text{K}$ ja jää lämpenee $\Delta T_\text{j} = 0\,{}^\circ\text{C} - (-8{,}0\,{}^\circ\text{C}) = 8{,}0\,\text{K}$. Sulamislämpö $334\,\tfrac{\text{kJ}}{\text{kg}} = 334\,000\,\tfrac{\text{J}}{\text{kg}}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan lämpömäärät erikseen ja sitten lämpötila:
```latex
\begin{aligned}
&Q_\text{v} = c_\text{v} m_\text{v} T_\text{v} \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}250\,\text{kg} \cdot 24{,}0\,\text{K} \\
&= 25\,140\,\text{J} \\[6pt]
&Q_\text{j} = c_\text{j} m_\text{j} \Delta T_\text{j} + s m_\text{j} \\
&= 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}050\,\text{kg} \cdot 8{,}0\,\text{K} \\
&\quad + 334\,000\,\tfrac{\text{J}}{\text{kg}} \cdot 0{,}050\,\text{kg} \\
&= 840\,\text{J} + 16\,700\,\text{J} \\
&= 17\,540\,\text{J} \\[6pt]
&T = \frac{Q_\text{v} - Q_\text{j}}{c_\text{v} (m_\text{v} + m_\text{j})} \\
&= \frac{25\,140\,\text{J} - 17\,540\,\text{J}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}300\,\text{kg}} \\
&= \frac{7600\,\text{J}}{1257\,\tfrac{\text{J}}{\text{K}}} \\
&= 6{,}05\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Koska $Q_\text{v} = 25\,140\,\text{J} > Q_\text{j} = 17\,540\,\text{J}$, kaikki jää sulaa. Lopputilassa on $0{,}300\,\text{kg}$ vettä lämpötilassa $6{,}0\,{}^\circ\text{C}$. Vastaus annetaan kahdella merkitsevällä numerolla, koska jään massa $0{,}050\,\text{kg}$ tunnetaan vain kahden numeron tarkkuudella ja se määrää lämpömäärän $Q_\text{j} = 17\,540\,\text{J}$ tarkkuuden (sadat joulet); erotus $Q_\text{v} - Q_\text{j} = 7600\,\text{J}$ on siis kahden numeron luku.

<!-- vaihe -->

**Järkevyys.** Tulos on alkulämpötilojen $-8{,}0\,{}^\circ\text{C}$ ja $24{,}0\,{}^\circ\text{C}$ välissä, mutta niiden puolivälin $8{,}0\,{}^\circ\text{C}$ alapuolella, vaikka vettä on viisinkertainen määrä: jään sulaminen painaa tulosta alas. Jos sulamislämpö unohdettaisiin, tulokseksi tulisi noin $19\,{}^\circ\text{C}$, joten sulaminen vie kaksi kolmasosaa veden luovuttamasta lämmöstä ($16{,}7\,\text{kJ}$ lämmöstä $25{,}1\,\text{kJ}$). Energiatase täsmää: vesi luovuttaa yhteensä $4190 \cdot 0{,}250 \cdot (24{,}0 - 6{,}05) \approx 18{,}8\,\text{kJ}$ ja jää vastaanottaa $840 + 16\,700 + 4190 \cdot 0{,}050 \cdot 6{,}05 \approx 18{,}8\,\text{kJ}$. Kokeile samoja arvoja simulaatiossa.

## Yleinen virhekäsitys
Moni laskee lopputilan lämpötilan niin kuin jää olisi vain kylmää vettä, jolloin sulamislämpö unohtuu. Kun sekoitetaan $0{,}30\,\text{kg}$ vettä ($20\,{}^\circ\text{C}$) ja $0{,}10\,\text{kg}$ jäätä ($0\,{}^\circ\text{C}$), tällä tavalla saataisiin
```latex
\begin{aligned}
T &= \frac{c_\text{v} m_\text{v} T_\text{v} + c_\text{v} m_\text{j} T_\text{j}}{c_\text{v} (m_\text{v} + m_\text{j})} \\
&= \frac{0{,}30\,\text{kg} \cdot 20\,{}^\circ\text{C}}{0{,}40\,\text{kg}} \\
&= 15\,{}^\circ\text{C}
\end{aligned}
```
Todellisuudessa kaiken jään sulattaminen vaatisi $33{,}4\,\text{kJ}$, mutta vesi voi luovuttaa jäähtyessään vain $25{,}1\,\text{kJ}$. Lopputila on siis $0\,{}^\circ\text{C}$, ja jäätä jää jäljelle $24{,}7\,\text{g}$. Toinen virhe on pitää lämpötilaa alle $0\,{}^\circ\text{C}$:n, kun astiassa on yhä jäätä ja vettä: niin kauan kuin molempia on, lämpötila on $0\,{}^\circ\text{C}$. Jos laskusi antaa alle $0\,{}^\circ\text{C}$:n lämpötilan kaavalla, joka olettaa kaiken jään sulavan, oletus on väärä: jäätä jää, ja lämpötila on $0\,{}^\circ\text{C}$. Poikkeus on hyvin kylmä jää, joka jäädyttää kaiken veden: silloin astiassa on pelkkää jäätä, ja sen lämpötila on alle $0\,{}^\circ\text{C}$.

## Tiivistelmä
- Eristetyssä astiassa veden luovuttama lämpömäärä on yhtä suuri kuin jään vastaanottama. Jää lämpenee ensin $0\,{}^\circ\text{C}$:seen ja sulaa sitten; sulamisen aikana lämpötila ei muutu.
- Vertaa ensin lämpömääriä $Q_\text{v} = c_\text{v} m_\text{v} T_\text{v}$ ja $Q_\text{j} = c_\text{j} m_\text{j} \Delta T_\text{j} + s m_\text{j}$. Jos $Q_\text{v} \ge Q_\text{j}$, kaikki jää sulaa ja $T = \tfrac{Q_\text{v} - Q_\text{j}}{c_\text{v}(m_\text{v} + m_\text{j})}$; rajatapauksessa $Q_\text{v} = Q_\text{j}$ lämpötila on tasan $0\,{}^\circ\text{C}$.
- Jos $Q_\text{v} < Q_\text{j}$, jäätä jää jäljelle ja lämpötila on $0\,{}^\circ\text{C}$. Sulaneen jään massa on $m_\text{s} = \tfrac{Q_\text{v} - c_\text{j} m_\text{j} \Delta T_\text{j}}{s}$. Poikkeus: jos jää on niin kylmää, että kaikki vesi jäätyy, lämpötila on alle $0\,{}^\circ\text{C}$.
- Veden ominaissulamislämpö on $334\,\text{kJ/kg}$: yhden kilogramman jään sulattaminen vaatii saman energian kuin kilogramman veden lämmittäminen lähes $80\,\text{K}$.
- Lopputilan lämpötila ei ole alkulämpötilojen keskiarvo, ja kun jää ja vesi ovat samassa astiassa tasapainossa normaalipaineessa, lämpötila on $0\,{}^\circ\text{C}$.
