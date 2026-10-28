# Work done by a gas and the heat engine

> **Why** does a thermal power plant get less than half of the energy of its fuel as electricity, and where does the rest of the energy go?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a condensing power plant on a lake shore. Power lines carry electricity away, a large cloud of steam rises from the cooling tower, and the condenser water is discharged into the lake warm, which shows as an orange zone in the water. Most of the energy of the fuel leaves as heat into the air and the water." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy311h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy311h-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy311h-tower" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy311h-chimney" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy311h-sky)"/>
  <path d="M0,380 L15,338 L30,380 L40.5,353.5 L51,380 L62.5,350 L73.5,380 L86,348 L98,380 L107,357.5 L116,380 L129,346 L141.5,380 L152,352.5 L163,380 L175,347.5 L187.5,380 L198.5,350.5 L210,380 L221,352 L231.5,380 L245.5,341.5 L259.5,380 L270,353 L280.5,380 L295,340.5 L309,380 L323.5,340 L338,380 L353.5,336.5 L369,380 L380,351 L391,380 L402,352 L412.5,380 L422,357 L431.5,380 L441.5,355 L451.5,380 L465,342.5 L479,380 L488,358 L497,380 L505.5,360 L514,380 L527,344 L540.5,380 L554,342.5 L568,380 L579.5,349 L591.5,380 L604.5,345.5 L617,380 L628.5,350 L640,380 L653,346 L665.5,380 L674.5,357.5 L684,380 L699,337.5 L714,380 L726,349 L737.5,380 L749,351.5 L760,380 L773.5,342 L787.5,380 L798.5,351 L809.5,380 L825,337 L840.5,380 L853,345 L866,380 L879.5,342.5 L893.5,380 L904,351.5 L915,380 L927,349 L938.5,380 L953,340 L967.5,380 L977,356.5 L986.5,380 L1000.5,342 L1014,380 L1028.5,341 L1042.5,380 L1054,349 L1065.5,380 L1080.5,338.5 L1095.5,380 L1110,339 L1125,380 L1139,340.5 L1153.5,380 L1168.5,337.5 L1184,380 L1196,348 L1207.5,380 V420 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <rect x="0" y="420" width="1200" height="180" fill="url(#fy311h-lake)"/>
  <path d="M0,400 H900 Q860,420 820,440 H0 Z" fill="#c9c2b2" stroke-linejoin="round"/>
  <path d="M120,420 Q160,300 140,190 H300 Q280,300 320,420 Z" fill="url(#fy311h-tower)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M130,190 Q128,156 168,160 Q184,124 224,136 Q260,116 280,154 Q316,158 312,190 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M183,136 Q180.5,92 232.5,97 Q253,50 305,66 Q352,40 378,89 Q425,94.5 419.5,136 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M304,98 Q301,50.5 357,56 Q379.5,5.5 435.5,22.5 Q486,-5.5 514,47.5 Q564.5,53 559,98 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M481,82 Q479,44.5 523,49 Q540.5,9.5 584.5,22.5 Q624,0.5 646,42.5 Q685.5,47 681,82 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <rect x="360" y="250" width="140" height="170" fill="#e3dccb" stroke="#1f2933" stroke-width="3"/>
  <rect x="500" y="310" width="220" height="110" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="520" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="564" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="608" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="652" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="696" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="400" y="120" width="36" height="130" fill="url(#fy311h-chimney)" stroke="#1f2933" stroke-width="3"/>
  <rect x="380" y="290" width="30" height="40" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="440" y="290" width="30" height="40" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="690" y="420" width="30" height="24" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="760" cy="480" rx="150" ry="40" fill="#ffc078" fill-opacity="0.55"/>
  <ellipse cx="740" cy="468" rx="80" ry="22" fill="#e8590c" fill-opacity="0.45"/>
  <path d="M850,420 L880,230 L910,420 M840,270 H920 M850,300 H910" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M1030,420 L1060,230 L1090,420 M1020,270 H1100 M1030,300 H1090" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M720,320 Q800,290 840,270 M840,270 Q960,300 1020,270 M1100,270 Q1150,290 1200,285" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M720,330 Q800,320 850,300 M850,300 Q960,330 1030,300 M1090,300 Q1150,320 1200,315" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
</svg>

## Key idea
When a gas expands and pushes a piston, it does work. The gas pushes the piston with a force $F = pA$, where $A$ is the area of the piston. If the piston moves a distance $s$ and the pressure stays the same, the work done by the gas is force times distance, $pAs$. The product $As$ is the change in the volume of the gas $\Delta V$, so the work done by the gas is $W_\text{g} = p\,\Delta V$. In the ($V$, $p$) graph it is the area between the graph and the $V$ axis, just like the work in an ($s$, $F$) graph. When the gas is compressed, the surroundings do work on the gas, and $W_\text{g}$ is negative. A gas that does work gives up energy, so in this lesson the first law is written in the form $\Delta U = Q - W_\text{g}$.

<svg data-fig="piston-work" viewBox="0 0 600 330" role="img" aria-label="Principle drawing of the work done by a gas on a piston. The cross-sectional area of the cylinder is A. The pressure p of the gas pushes the piston with a force F = pA, and the piston moves a distance Δs to the right. The volume of the gas grows by the shaded part, ΔV = AΔs. The work is W_g = FΔs = pAΔs = pΔV. The picture is not to scale." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy311-dv" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" fill="#ffc078"/><line x1="0" y1="0" x2="0" y2="12" stroke="#e8590c" stroke-width="2"/></pattern></defs>
  <rect x="110" y="70" width="140" height="120" fill="#ffc078" fill-opacity="0.3"/>
  <rect x="250" y="70" width="170" height="120" fill="url(#fy311-dv)"/>
  <line x1="250" y1="70" x2="250" y2="190" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <rect x="104" y="64" width="6" height="132" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="104" y="64" width="458" height="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="104" y="190" width="458" height="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="413" y="71" width="14" height="118" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="429" y1="130" x2="515" y2="130" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M536,130 L514,140 L514,120 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="449" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F = pA$</div></foreignObject>
  <foreignObject x="143" y="115.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas},\ p$</div></foreignObject>
  <foreignObject x="318.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V$</span></div></foreignObject>
  <line x1="76" y1="130" x2="76" y2="82" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M76,71 L81.5,83 L70.5,83 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="76" y1="130" x2="76" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M76,189 L70.5,177 L81.5,177 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="46" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$A$</span></div></foreignObject>
  <line x1="250" y1="198" x2="250" y2="234" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="198" x2="420" y2="234" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="311" y1="226" x2="262" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M251,226 L263,220.5 L263,231.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="359" y1="226" x2="408" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M419,226 L407,231.5 L407,220.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="318.5" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="183.5" y="275.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W_\text{k} = F\,\Delta s = pA\,\Delta s = p\,\Delta V$</div></foreignObject>
</svg>

### A heat engine repeats its motion
A heat engine turns heat into work continuously, so it has to repeat its motion. The piston has to be brought back down. If it is pressed down at the same pressure, the return takes all the work done by the gas. The return takes less work if the gas is first cooled to a lower pressure, but then the gas gives up heat to a colder environment. In a steam power plant, water boils in the boiler, the hot steam expands in the turbine and turns the generator, and the steam coming out of the turbine condenses back into water in the condenser, which is cooled by seawater. The working substance goes round the same path again and again, so at the end of a cycle its internal energy is the same as at the start. Energy is conserved: the heat $Q_1$ from the hot source equals the work $W$ done by the engine plus the heat $Q_2$ given up to the colder environment.

Experience shows that a heat engine cannot turn all the heat it receives into work; part of it must always be given up to a colder environment. This is the content of the second law of thermodynamics. The larger the temperature difference between the hot source and the cold environment compared with the temperature of the hot source, the larger the share of the heat the engine can turn into work. Cyclic processes are not calculated in this course; the simulation only shows why the heat $Q_2$ cannot be avoided.

<svg data-fig="heat-engine" viewBox="0 0 600 340" role="img" aria-label="The energy flows of a heat engine as arrows whose width shows the energy flow, that is, the power: from the hot source, whose temperature is T_1, the heat Q_1 enters the engine. The engine does work W, which is 40 per cent of Q_1, and gives up the rest, the heat Q_2, to the cold environment, whose temperature is T_2. The widths of the arrows are to scale: Q_1 is 60, W is 24 and Q_2 is 36 units, so the Q_1 arrow is as wide as the W and Q_2 arrows together." style="max-width:100%;font-size:24px">
  <rect x="150" y="12" width="300" height="52" rx="10" fill="#f2a69c" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="221" y="23.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot source}\quad T_1$</div></foreignObject>
  <rect x="150" y="276" width="300" height="52" rx="10" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5"/>
  <foreignObject x="183.5" y="287.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold environment}\quad T_2$</div></foreignObject>
  <rect x="225" y="118" width="150" height="98" rx="12" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="258.5" y="152.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{engine}$</div></foreignObject>
  <path d="M270,64 L270,94 L258,94 L300,118 L342,94 L330,94 L330,64 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M282,216 L282,250 L270,250 L300,274 L330,250 L318,250 L318,216 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M375,179 L534,179 L534,190 L560,167 L534,144 L534,155 L375,155 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="354" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="342" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="460" y="119.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="16" y="137.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{arrow width}$</div></foreignObject>
  <foreignObject x="16" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{shows power}$</div></foreignObject>
</svg>

### Efficiency
Efficiency tells how large a share of the energy supplied to a machine is put to use, so its value depends on what is counted as useful. In the efficiency of a power plant's electricity production, only the electricity is useful. A Finnish condensing power plant that produces only electricity gets about $40\,\%$ of the energy of its fuel as electricity, and a nuclear power plant about $35\,\%$. Most of the rest is transferred to the sea through the condenser, and in a plant that burns fuel part also leaves into the air with the flue gases. The efficiency of a car engine is about $30\,\%$, and the rest of the energy leaves with the exhaust gases and the radiator.

In combined production of electricity and heat, the heat $Q_2$ of the condenser is recovered: it heats the water of the district heating network, which carries it to the houses of the city. So the heat engine still gives up heat to something colder, but this heat is put to use. In the overall efficiency, the electricity and the district heating together count as useful, and it is 85–$90\,\%$. The efficiency of electricity production therefore does not rise; it is usually lower than when only electricity is produced. This answers the opening question: less than half becomes electricity, but the rest does not disappear; it is transferred as heat to the environment or to the district heating network.

### Refrigerator and heat pump
A refrigerator and a heat pump work the opposite way to a heat engine: they use electrical energy to transfer heat from a cold place to a warm one. A refrigerator transfers heat from inside the cabinet to the room, and an air-source heat pump from the outdoor air to the inside. The heat given out indoors is the sum of the heat taken from outside and the electricity used, so a pump can heat a house with, for example, three times as much heating power as the electric power it uses. The ratio of the heating power to the electric power is called the coefficient of performance. The coefficient of performance is not an efficiency: it can be greater than 1, because part of the heat that comes indoors is transferred from the outdoor air and does not come from the electricity. The pump does not create energy; it transfers it.

<svg data-fig="heat-pump" viewBox="0 0 600 270" role="img" aria-label="The energy flows of a heat pump as arrows whose width shows the power: the electrical energy E_el and the heat Q_outdoors taken from the outdoor air enter the pump, and the pump gives out indoors the heat Q_indoors, which is their sum. The widths of the arrows are to scale: E_el is 20, Q_outdoors is 40 and Q_indoors is 60 units, so the arrow going indoors is as wide as the two incoming arrows together and three times as wide as the electricity arrow." style="max-width:100%;font-size:24px">
  <rect x="230" y="76" width="130" height="126" rx="12" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="266" y="124.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pump}$</div></foreignObject>
  <path d="M16,120 L208,120 L208,124 L230,110 L208,96 L208,100 L16,100 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M16,178 L208,178 L208,182 L230,158 L208,134 L208,138 L16,138 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M360,169 L532,169 L532,174 L560,139 L532,104 L532,109 L360,109 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="16" y="59.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{electricity}\ E_\text{s}$</div></foreignObject>
  <foreignObject x="16" y="191.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heat from outdoor air}$</div></foreignObject>
  <foreignObject x="16" y="223.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_\text{outdoors}$</div></foreignObject>
  <foreignObject x="387.5" y="77.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat indoors}$</div></foreignObject>
  <foreignObject x="406" y="177.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q_\text{indoors}$</div></foreignObject>
  <foreignObject x="393" y="237.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{width shows power}$</div></foreignObject>
</svg>

## Formula: Work done by a gas and efficiency
When the pressure of a gas stays constant, the work done by the gas is
```latex
W_\text{g} = p\,\Delta V
```
where $W_\text{g}$ is the work done by the gas (J), $p$ the pressure of the gas (Pa) and $\Delta V$ the change in the volume of the gas (m³). The work is positive when the gas expands and negative when the gas is compressed. The change in the internal energy of the gas is
```latex
\Delta U = Q - W_\text{g}
```
where $Q$ is the quantity of heat transferred to the gas (J). This is the first law $\Delta U = Q + W$ presented in the chapter *Internal energy, heat and conservation of energy*, where $W$ is the work done on the gas by the surroundings: $W = -W_\text{g}$.

During one cycle of a heat engine, the work done and the efficiency are
```latex
W = Q_1 - Q_2
```
```latex
\eta = \frac{W}{Q_1}
```
where $Q_1$ is the heat transferred to the engine from the hot source (J), $Q_2$ the heat given up to the colder environment (J), $W$ the work done by the engine during the cycle (J) and $\eta$ the efficiency, which is often given as a percentage. Efficiency can be calculated in the same way from powers, for example the electric power divided by the fuel power.

<svg data-fig="pv-work" viewBox="0 0 600 330" role="img" aria-label="(V, p) graph of a gas expanding at constant pressure: the pressure p stays constant while the volume grows from V_1 to V_2, so the graph is a horizontal line segment, and an arrow shows the direction of the expansion. The shaded rectangle between the segment and the V axis, whose width is the change in volume ΔV and whose height is p, is the work done by the gas W_g = p ΔV. Schematic diagram." style="max-width:100%;font-size:24px">
  <line x1="203" y1="270" x2="203" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="270" x2="363" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="470" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="271" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="203" y1="270" x2="203" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_1$</div></foreignObject>
  <line x1="363" y1="270" x2="363" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_2$</div></foreignObject>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="98" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{m}^3)$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{Pa})$</div></foreignObject>
  <polygon points="203,270 363,270 363,112.5 203,112.5" fill="#e8590c" fill-opacity="0.35"/>
  <polyline points="203,112.5 363,112.5" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="203" y1="112.5" x2="203" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="363" y1="112.5" x2="363" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="269" y1="112.5" x2="278" y2="112.5" stroke="#1f2933" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M297,112.5 L277,121.5 L277,103.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="216.5" y="72" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas expands}$</div></foreignObject>
  <foreignObject x="235.5" y="156" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W_\text{k} = p\,\Delta V$</div></foreignObject>
  <line x1="257" y1="228" x2="218" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M206,228 L219,222 L219,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="309" y1="228" x2="348" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360,228 L347,234 L347,222 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="266.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta V$</div></foreignObject>
</svg>

A heat pump gives out indoors a quantity of heat that is the sum of the heat taken from the outdoor air and the electrical energy used by the pump:
```latex
Q_\text{indoors} = Q_\text{outdoors} + E_\text{el}
```
The coefficient of performance tells how many times as much heat the pump gives out indoors as the electrical energy it uses:
```latex
\varepsilon = \frac{Q_\text{indoors}}{E_\text{el}}
```
where $Q_\text{indoors}$ is the heat given out indoors (J), $Q_\text{outdoors}$ the heat taken from the outdoor air (J), $E_\text{el}$ the electrical energy used by the pump (J) and $\varepsilon$ the coefficient of performance. The coefficient of performance can be calculated in the same way from powers.

## Worked example
Wood chip energy is fed into the boiler of a biopower plant at a power of $500\,\text{MW}$. When the plant produces only electricity, the electric power is $190\,\text{MW}$. In winter the same plant works as a combined heat and power plant: it produces $150\,\text{MW}$ of electricity and $290\,\text{MW}$ of district heating. What is the efficiency in each case, and how much power is transferred to the environment as waste heat?

<!-- vaihe -->

**Given and find.** Fuel power $P_1 = 500\,\text{MW}$. When only electricity is produced, the electric power is $P_\text{e} = 190\,\text{MW}$; in combined production $P_\text{e} = 150\,\text{MW}$ and the district heating power is $P_\text{dh} = 290\,\text{MW}$. The efficiencies $\eta$ and the power of the waste heat $P_2$ are asked for in both cases.

<!-- vaihe -->

**Principle.** Efficiency is the useful power divided by the power supplied; it is calculated from powers just like from energies, because both are energy in the same time. Energy is conserved, so the fuel power is divided into the useful power and the waste heat. In electricity production alone only the electricity is useful; in combined production both the electricity and the district heating are.

<!-- vaihe -->

**Rearranged formula.** Solve for the quantities asked for, with symbols before numbers:
```latex
\begin{aligned}
\eta &= \frac{P_\text{useful}}{P_1} \\
P_2 &= P_1 - P_\text{useful}
\end{aligned}
```
For electricity alone $P_\text{useful} = P_\text{e}$, and for combined production $P_\text{useful} = P_\text{e} + P_\text{dh}$.

<!-- vaihe -->

**Unit conversions.** All powers are given in megawatts, so no conversions are needed: in the efficiency the unit cancels, and the waste heat comes out in megawatts. A decimal number is changed to a percentage by multiplying by one hundred.

<!-- vaihe -->

**Substitution.** For electricity alone and for combined production separately:
```latex
\begin{aligned}
\eta_1 &= \frac{P_\text{e}}{P_1} \\
&= \frac{190\,\text{MW}}{500\,\text{MW}} \\
&= 0.380 \\
P_{2,1} &= P_1 - P_\text{e} \\
&= 500\,\text{MW} - 190\,\text{MW} \\
&= 310\,\text{MW} \\[6pt]
\eta_2 &= \frac{P_\text{e} + P_\text{dh}}{P_1} \\
&= \frac{150\,\text{MW} + 290\,\text{MW}}{500\,\text{MW}} \\
&= 0.880 \\
P_{2,2} &= P_1 - (P_\text{e} + P_\text{dh}) \\
&= 500\,\text{MW} - 440\,\text{MW} \\
&= 60\,\text{MW}
\end{aligned}
```

<!-- vaihe -->

**Result.** With electricity production alone the efficiency is $\eta_1 = 0.380 = 38.0\,\%$ and $310\,\text{MW}$ of waste heat is transferred to the environment, most of it through the condenser to the sea. In combined production the overall efficiency is $\eta_2 = 0.880 = 88.0\,\%$ and there is only $60\,\text{MW}$ of waste heat. The powers are given in whole megawatts, so the differences $310\,\text{MW}$ and $60\,\text{MW}$ are known to the nearest megawatt. The efficiencies are quotients, so they have as many figures as the least precise power: $190\,\text{MW}$, $150\,\text{MW}$, $290\,\text{MW}$ and $500\,\text{MW}$ all have three figures, so the efficiencies are given with three figures.

<!-- vaihe -->

**Reasonableness.** Energy is conserved: $190\,\text{MW} + 310\,\text{MW} = 500\,\text{MW}$ and $150\,\text{MW} + 290\,\text{MW} + 60\,\text{MW} = 500\,\text{MW}$. The efficiency of electricity production stays clearly below $100\,\%$, because a heat engine must give up part of the heat to something colder. Even the overall efficiency is not $100\,\%$, because part of the heat leaves with the flue gases and other losses. Less electricity is obtained in combined production because the steam is condensed at a higher temperature so that its heat is suitable for district heating. The energy of the fuel is still put to much better use.

## Common misconception
Many people think that better technology could make a heat engine almost perfect, so that all the heat would turn into work. Reducing friction and other losses helps, but part of the heat must always be given up to a colder environment, so the efficiency of a heat engine stays clearly below $100\,\%$. The frictionless piston of the simulation shows the reason: for the piston to be brought down with less work than it took to raise it, the gas has to be cooled, and in the cooling heat is transferred to the cold water. The limit applies to a machine that turns heat into work, not to all devices: for example, in an electric heater practically all the electrical energy increases the internal energy of the resistor and is transferred as heat to the room.

Another mistake is to think of a heat pump as a perpetual motion machine, because it gives out more heat than it uses electricity. The extra heat comes from the outdoor air, and energy is not created out of nothing. A third mistake is to think that a pressurised gas does work just because its pressure is high. Work is done only when the volume changes and the piston moves.

## Summary
- A gas that expands at constant pressure does the work $W_\text{g} = p\,\Delta V$, which is the area under the ($V$, $p$) graph. The internal energy changes by $\Delta U = Q - W_\text{g}$.
- A piston machine can repeat its work only if the gas is cooled before the piston is returned; then heat is transferred to something colder.
- A heat engine takes heat $Q_1$ from a hot source, does work $W$ and gives up heat $Q_2$ to a colder environment: $W = Q_1 - Q_2$.
- Efficiency is $\eta = W/Q_1$. A heat engine cannot turn all the heat into work.
- The efficiency of electricity production of a condensing power plant is about $40\,\%$. In combined production of electricity and heat the heat of the condenser is used as district heating, so the overall efficiency, in which electricity and heat both count as useful, is 85–$90\,\%$.
- A refrigerator and a heat pump use work to transfer heat from cold to warm. They do not create energy. The coefficient of performance of a heat pump, $\varepsilon = Q_\text{indoors}/E_\text{el}$, is not an efficiency, and it can be greater than 1, because part of the heat comes from the outdoor air.
