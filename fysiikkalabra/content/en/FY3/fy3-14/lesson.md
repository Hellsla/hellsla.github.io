# Thermal balance during a change of state

> **Why** do ice cubes cool a drink so effectively, even though the ice itself is only at zero degrees? And why can some ice be left at the bottom of the glass, even though the drink was at room temperature?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a tall glass of a cold drink stands on a table, with ice cubes and a straw floating in it. Water droplets have condensed on the outside of the glass, and a box of ice cubes stands next to the glass." class="fig-hero" style="max-width:100%;font-size:24px">
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

## Key idea
When warm water and ice are put in an insulated container, heat is transferred from the water to the ice until the temperatures are equal and the container is in thermal equilibrium. Energy is conserved, so the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The energy taken in by the ice does not simply raise its temperature, however: the ice first warms to 0 °C and then melts. During melting the temperature stays constant, but every kilogram of ice takes in 334 kJ of energy, and the same energy would raise the temperature of a kilogram of water by almost 80 K.

<svg viewBox="0 0 600 344" role="img" aria-label="Before-and-after schematic: an insulated container first holds 0.30 kg of water at 20 °C and 0.10 kg of ice at 0 °C. Heat Q is transferred from the water to the ice. At equilibrium the thermometer reads 0 °C, there is 0.375 kg of water and only 0.025 kg of ice is left. The total area of the ice cubes is drawn to scale with the mass of the ice." style="max-width:100%;font-size:24px">
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
  <foreignObject x="53.0" y="4" width="200" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{initially}$</div></foreignObject>
  <foreignObject x="31.0" y="276" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{water } 0.30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="31.0" y="309" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{ice } 0.10\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
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
  <foreignObject x="375.0" y="4" width="200" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{at equilibrium}$</div></foreignObject>
  <foreignObject x="353.0" y="276" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{water } 0.375\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="353.0" y="309" width="244" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{ice } 0.025\,\text{kg},\ 0\,{}^\circ\text{C}$</div></foreignObject>
</svg>

This is why the final temperature cannot be found as the mean of the initial temperatures. There are three possible end states. If the heat from the water is enough to melt all the ice, the mixture warms to above 0 °C. If the heat is not enough, both ice and water are left in the container, and as long as both are present, the temperature is exactly 0 °C. If the ice is very cold and there is little water, the water can even freeze. The solution always starts with the same comparison: calculate how much heat the water can give out and how much the ice needs to melt completely.

## Formula: Thermal equilibrium and melting
An insulated container holds water of mass $m_\text{w}$ and temperature $T_\text{w} > 0\,{}^\circ\text{C}$, and ice of mass $m_\text{i}$ and temperature $T_\text{i} \le 0\,{}^\circ\text{C}$. We compare two quantities of heat: the one the water can give out as it cools to 0 °C, and the one the ice needs to warm to 0 °C and melt completely:
```latex
\begin{aligned}
Q_\text{w} &= c_\text{w} m_\text{w} T_\text{w} \\
Q_\text{i} &= c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i}
\end{aligned}
```
where $Q_\text{w}$ is the quantity of heat given out by the water (J), $c_\text{w}$ is the specific heat capacity of water and $c_\text{i}$ that of ice (J/(kg·K)), $T_\text{w}$ is the temperature of the water in degrees Celsius (the same number as the temperature change to 0 °C in kelvins), $Q_\text{i}$ is the quantity of heat the ice needs (J), $\Delta T_\text{i} = 0\,{}^\circ\text{C} - T_\text{i}$ is the rise in the temperature of the ice (K) and $s$ is the specific latent heat of fusion of ice (J/kg). The first term warms the ice to 0 °C and the second melts it.

<svg viewBox="0 0 600 392" role="img" aria-label="Energy balance bars drawn to scale, in kilojoules: 0.30 kg of water at 20 °C gives out 25.1 kJ when it cools to 0 °C. 0.10 kg of ice at −10 °C needs 2.1 kJ to warm to 0 °C and 33.4 kJ to melt, 35.5 kJ in total. The heat from the water is not enough: the pale part of the bar shows the ice that does not have time to melt." style="max-width:100%;font-size:24px">
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
  <foreignObject x="290" y="2" width="306" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{water } 0.30\,\text{kg},\ 20\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="290" y="38" width="306" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$\text{ice } 0.10\,\text{kg},\ {-10}\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="150" y="181.2" width="100" height="150.8" rx="3" fill="url(#fy314-heat2)" stroke="#1f2933" stroke-width="2"/>
  <rect x="350" y="319.4" width="100" height="12.6" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <rect x="350" y="181.2" width="100" height="138.2" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="350" y="119.0" width="100" height="62.2" fill="#a5d8ff" fill-opacity="0.35" stroke="#4f8fbf" stroke-width="2" stroke-dasharray="7 5"/>
  <line x1="250" y1="181.2" x2="460" y2="181.2" stroke="#1f2933" stroke-width="2" stroke-dasharray="7 5"/>
  <path d="M460,119.0 H466 V181.2 H460" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="472" y="133.07999999999998" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{ice left over}$</div></foreignObject>
  <foreignObject x="356" y="153.07999999999998" width="90" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$s\,m_\text{i}$</div></foreignObject>
  <foreignObject x="472" y="292.7" width="120" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{warming}$</div></foreignObject>
  <line x1="450" y1="325.7" x2="468" y2="309.7" stroke="#6b7480" stroke-width="1.5"/>
  <foreignObject x="130" y="143.16" width="140" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$25.1\,\text{kJ}$</div></foreignObject>
  <foreignObject x="330" y="81.0" width="140" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$35.5\,\text{kJ}$</div></foreignObject>
  <foreignObject x="110" y="338" width="180" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{water gives out}$</div></foreignObject>
  <foreignObject x="310" y="338" width="180" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{ice needs}$</div></foreignObject>
</svg>

| Quantity | Value |
| --- | --- |
| of water $c_\text{w}$ | 4190 J/(kg·K) |
| of ice $c_\text{i}$ | 2100 J/(kg·K) |
| of ice $s$ | 334 kJ/kg |

If $Q_\text{w} \ge Q_\text{i}$, all the ice melts. The heat given out by the water is then used to warm and melt the ice, and the rest warms the whole amount of water $m_\text{w} + m_\text{i}$ to the temperature $T$. The energy balance is
```latex
\begin{aligned}
&c_\text{w} m_\text{w} (T_\text{w} - T) \\
&\quad = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\
&\qquad + c_\text{w} m_\text{i} T
\end{aligned}
```
where the left-hand side is the quantity of heat given out by the water, and on the right are the warming of the ice, the melting of the ice and the warming of the meltwater. Solved:
```latex
T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})}
```
If $Q_\text{w} < Q_\text{i}$ but the water is enough to warm the ice to 0 °C, not all the ice has time to melt. The container then holds ice and water at the same time, so $T = 0\,{}^\circ\text{C}$. The mass of melted ice $m_\text{melt}$ is found from the heat that is left after warming the ice:
```latex
m_\text{melt} = \frac{Q_\text{w} - c_\text{i} m_\text{i} \Delta T_\text{i}}{s}
```
The mass of ice that is left is $m_\text{i} - m_\text{melt}$. The graph shows how the final temperature depends on the initial temperature of the water when there is 0.30 kg of water and 0.10 kg of ice at 0 °C: until the heat from the water is enough to melt the ice, the temperature stays at 0 °C, and after that it rises. The black dot is the glass of the first figure, where the water is at 20 °C.

<svg viewBox="0 0 600 394" role="img" aria-label="Graph of the formula: final temperature T of 0.30 kg of water and 0.10 kg of ice at 0 °C as a function of the initial temperature of the water Tv. When Tv is at most 26.6 °C, some ice is left over and T is 0 °C. After that all the ice melts and T rises in a straight line, to 40 °C when the water starts at 80 °C. The axes are drawn to scale." style="max-width:100%;font-size:24px">
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
  <foreignObject x="340" y="358" width="250" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$T_\text{w}\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="100.0,310.0 252.8,310.0 560.0,69.6" fill="none" stroke="#c92a2a" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="252.8" y1="310.0" x2="252.8" y2="70" stroke="#6b7480" stroke-width="2" stroke-dasharray="6 5"/>
  <circle cx="252.8" cy="310.0" r="6.5" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="215.0" cy="310.0" r="6.5" fill="#1f2933"/>
  <foreignObject x="246.78440731901352" y="62" width="150" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$26.6\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="108" y="76" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{ice left over}$</div></foreignObject>
  <foreignObject x="108" y="110" width="128" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$T = 0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="350" y="256.0" width="220" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$\text{all ice melts}$</div></foreignObject>
  <foreignObject x="135.0" y="260.0" width="110" height="34"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{initial glass}$</div></foreignObject>
</svg>

If $Q_\text{w}$ is not enough even to warm the ice to 0 °C, the cold ice freezes some of the water. As long as some water is left, ice and water are present together and the temperature is 0 °C. Only if all the water freezes does the mass of ice cool to below 0 °C; its temperature is found from the same energy balance in the Level 3 exercise.

## Worked example
A calorimeter contains 0.250 kg of water at a temperature of 24.0 °C. 0.050 kg of ice at −8.0 °C is dropped into the water. Does all the ice melt, and what is the temperature of the contents of the calorimeter at thermal equilibrium? The heat capacity of the calorimeter itself and heat losses to the surroundings are ignored.

<!-- vaihe -->

**Given and find.** Water: $m_\text{w} = 0.250\,\text{kg}$, $T_\text{w} = 24.0\,{}^\circ\text{C}$. Ice: $m_\text{i} = 0.050\,\text{kg}$, $T_\text{i} = -8.0\,{}^\circ\text{C}$. From the table, $c_\text{w} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, $c_\text{i} = 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ and $s = 334\,\tfrac{\text{kJ}}{\text{kg}}$. We are asked whether all the ice melts, and for the final temperature $T$.

<!-- vaihe -->

**Principle.** Energy is conserved, because the calorimeter takes in no heat and no heat escapes to the surroundings: the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The ice first warms to 0 °C, then melts at a constant temperature, and finally the meltwater warms to the final temperature. So we must first check whether the heat given out by the water is enough to warm and melt all the ice. If it is, the ice melts completely and the temperature rises above 0 °C.

<!-- vaihe -->

**Rearranged formula.** When the water cools to 0 °C it gives out a quantity of heat $Q_\text{w}$, and to melt, the ice needs a quantity of heat $Q_\text{i}$. When $Q_\text{w} > Q_\text{i}$, the surplus warms all the water ($m_\text{w} + m_\text{i}$) to the temperature $T$:
```latex
\begin{aligned}
&Q_\text{w} = c_\text{w} m_\text{w} T_\text{w} \\
&Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\[6pt]
&T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The masses are already in kilograms. A temperature change is the same in kelvins and in degrees Celsius: the water cools by $24.0\,{}^\circ\text{C} - 0\,{}^\circ\text{C} = 24.0\,\text{K}$ and the ice warms by $\Delta T_\text{i} = 0\,{}^\circ\text{C} - (-8.0\,{}^\circ\text{C}) = 8.0\,\text{K}$. The latent heat of fusion is $334\,\tfrac{\text{kJ}}{\text{kg}} = 334\,000\,\tfrac{\text{J}}{\text{kg}}$.

<!-- vaihe -->

**Substitution.** We calculate the quantities of heat separately and then the temperature:
```latex
\begin{aligned}
&Q_\text{w} = c_\text{w} m_\text{w} T_\text{w} \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.250\,\text{kg} \cdot 24.0\,\text{K} \\
&= 25\,140\,\text{J} \\[6pt]
&Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i} \\
&= 2100\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.050\,\text{kg} \cdot 8.0\,\text{K} \\
&\quad + 334\,000\,\tfrac{\text{J}}{\text{kg}} \cdot 0.050\,\text{kg} \\
&= 840\,\text{J} + 16\,700\,\text{J} \\
&= 17\,540\,\text{J} \\[6pt]
&T = \frac{Q_\text{w} - Q_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})} \\
&= \frac{25\,140\,\text{J} - 17\,540\,\text{J}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0.300\,\text{kg}} \\
&= \frac{7600\,\text{J}}{1257\,\tfrac{\text{J}}{\text{K}}} \\
&= 6.05\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Result.** Because $Q_\text{w} = 25\,140\,\text{J} > Q_\text{i} = 17\,540\,\text{J}$, all the ice melts. The final state is 0.300 kg of water at a temperature of $6.0\,{}^\circ\text{C}$. The answer is given to two significant figures, because the mass of the ice, $0.050\,\text{kg}$, is known only to two figures and it determines the precision of the quantity of heat $Q_\text{i} = 17\,540\,\text{J}$ (hundreds of joules); the difference $Q_\text{w} - Q_\text{i} = 7600\,\text{J}$ is therefore a two-figure number.

<!-- vaihe -->

**Reasonableness.** The result lies between the initial temperatures −8.0 °C and 24.0 °C, but below 8.0 °C, the midpoint of the two, even though there is five times as much water: the melting of the ice pulls the result down. If the latent heat were forgotten, the result would be about 19 °C, so melting takes two thirds of the heat given out by the water (16.7 kJ of 25.1 kJ). The energy balance checks out: the water gives out a total of $4190 \cdot 0.250 \cdot (24.0 - 6.05) \approx 18.8\,\text{kJ}$ and the ice takes in $840 + 16\,700 + 4190 \cdot 0.050 \cdot 6.05 \approx 18.8\,\text{kJ}$. Try the same values in the simulation.

## Common misconception
Many people calculate the final temperature as if the ice were just cold water, which forgets the latent heat of fusion. When 0.30 kg of water (20 °C) and 0.10 kg of ice (0 °C) are mixed, this method would give
```latex
\begin{aligned}
T &= \frac{c_\text{w} m_\text{w} T_\text{w} + c_\text{w} m_\text{i} T_\text{i}}{c_\text{w} (m_\text{w} + m_\text{i})} \\
&= \frac{0.30\,\text{kg} \cdot 20\,{}^\circ\text{C}}{0.40\,\text{kg}} \\
&= 15\,{}^\circ\text{C}
\end{aligned}
```
In reality, melting all the ice would need 33.4 kJ, but the water can give out only 25.1 kJ as it cools. So the final state is 0 °C, and 24.7 g of ice is left over. Another mistake is to put the temperature below 0 °C when the container still holds ice and water: as long as both are present, the temperature is 0 °C. If your calculation gives a temperature below 0 °C with a formula that assumes all the ice melts, the assumption is wrong: some ice is left, and the temperature is 0 °C. The exception is very cold ice that freezes all the water: then the container holds only ice, and its temperature is below 0 °C.

## Summary
- In an insulated container, the quantity of heat given out by the water is equal to the quantity of heat taken in by the ice. The ice first warms to 0 °C and then melts; during melting the temperature does not change.
- First compare the quantities of heat $Q_\text{w} = c_\text{w} m_\text{w} T_\text{w}$ and $Q_\text{i} = c_\text{i} m_\text{i} \Delta T_\text{i} + s m_\text{i}$. If $Q_\text{w} \ge Q_\text{i}$, all the ice melts and $T = \tfrac{Q_\text{w} - Q_\text{i}}{c_\text{w}(m_\text{w} + m_\text{i})}$.
- If $Q_\text{w} < Q_\text{i}$, some ice is left and the temperature is 0 °C. The mass of melted ice is $m_\text{melt} = \tfrac{Q_\text{w} - c_\text{i} m_\text{i} \Delta T_\text{i}}{s}$. Exception: if the ice is so cold that all the water freezes, the temperature is below 0 °C.
- The specific latent heat of fusion of water is 334 kJ/kg: melting one kilogram of ice needs the same energy as warming a kilogram of water by almost 80 K.
- The final temperature is not the mean of the initial temperatures, and ice and water together in the same container are always at 0 °C.
