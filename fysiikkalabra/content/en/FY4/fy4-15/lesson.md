# Hydro and wind power as energy converters

> **Why** does the same water of the Vuoksi river give three times as much power at Imatra as at Tainionkoski? And why does the power of a wind turbine grow so much more than the wind speed?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a river valley on a summer day. In the middle, a hydropower plant has been built across the river: behind the dam the upper water is high, and below the plant the water leaving it foams white at a lower level. In the background, four wind turbines turn on a ridge, and lines in the sky show the wind. A power line with pylons leads away from the plant." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### A power plant converts energy
Hydro and wind power plants do not produce energy out of nothing. They convert the mechanical energy of water or air into electricity. Water behind a dam has potential energy $E_\text{p} = mgh$ relative to the water below. When the water flows down a pipe, the potential energy turns into kinetic energy, as in the chapter *Conservation of mechanical energy and the work–energy principle*. The fast stream of water pushes on the blades of the turbine and makes it rotate (in many turbines the pressure of the water also does work, but the energy chain is the same), and the shaft of the turbine turns a generator, which converts the energy of rotation into electricity. After the turbine, the water flows slowly on to the tailwater. The difference in height between the upper and the lower water surface is called the **head** $h$.

<svg data-fig="vesivoimala" viewBox="0 0 600 360" role="img" aria-label="Schematic cross-section of a hydropower plant, not to scale. On the left, behind the dam, is the upper reservoir with its surface high up. Water flows down a pipe through the dam to a turbine, which turns a generator through a shaft. After the turbine the water is discharged to the right into the tailwater. The difference in height between the upper and lower water surfaces is the head h. The potential energy of the water turns into kinetic energy in the pipe, into energy of rotation in the turbine and into electricity in the generator, shown by the orange arrow." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-vesivoimala.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="496" y="192.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{a}$</div></foreignObject>
  <foreignObject x="542" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="14.5" y="45.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{upper reservoir}$</div></foreignObject>
  <foreignObject x="64.5" y="145.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E_\text{p} = mgh$</span></div></foreignObject>
  <foreignObject x="217.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="340" y="145.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{generator}$</div></foreignObject>
  <foreignObject x="252.5" y="315.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{turbine}$</span></div></foreignObject>
  <foreignObject x="460" y="307.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{tailwater}$</span></div></foreignObject>
</svg>

### Power tells how much energy per second
A power plant is described by its power: how much energy it converts in one second. When one cubic metre of water, that is $1000\,\text{kg}$, falls the $24\,\text{m}$ head of Imatra, it releases potential energy $mgh \approx 235\,\text{kJ}$. If hundreds of cubic metres flow through the turbines every second, the power is hundreds of megawatts. So power grows for two reasons: when more water falls each second, and when it falls from higher up. The water of the Vuoksi flows first through the Tainionkoski power plant and then through the Imatra power plant, so the flow rate is the same at both. The head at Imatra is about three times as large, and so is its power.

```pysahdy
Two power plants get the same flow of water, but one has twice the drop height. Which one has the greater power, and by how much?
---
The plant with twice the drop height has twice the power, because the potential energy $mgh$ of every cubic metre falling each second is twice as large.
```

### Efficiency
Not all the energy the water loses becomes electricity. The water rubs against the walls of the pipe, the turbine and the generator warm up, and the water leaving into the tailwater still has a little kinetic energy. The **efficiency** of a power plant is the ratio of the output work $W_\text{a}$ to the input work $W_\text{o}$, or equally of the output power $P_\text{a}$ to the input power $P_\text{o}$. In a power plant the output power is the electric power it delivers:
```kaavat
efficiency :: \eta = \frac{W_\text{a}}{W_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
where $\eta$ (eta) is the efficiency, given as a decimal number or as a percentage. Efficiency is at most $100\,\%$. In real devices it is usually below $100\,\%$, because part of the energy taken in does not end up in the intended useful form, here electricity. The efficiency of a large hydropower plant is about $90\,\%$.

```pysahdy
A power plant takes in a power of $100\,\text{MW}$ from the water and delivers an electric power of $90\,\text{MW}$. Where does the other $10\,\text{MW}$ go?
---
No energy disappears. Most of it becomes internal energy, which is transferred to the surroundings as heat, as the water rubs against the pipe and the machines warm up, and some stays as the kinetic energy of the water leaving into the lower pool.
```

### The kinetic energy of the wind
In a wind turbine the source of energy is the kinetic energy of moving air, $E_\text{k} = \tfrac{1}{2}mv^2$. The wind pushes on the rotor blades and makes the rotor turn, and the air slows down as it passes the rotor. The rotor cannot stop the air completely, because the air must be able to flow away behind the rotor. So even an ideal rotor can capture only about $59\,\%$ of the power that the undisturbed wind carries through the area swept by the rotor, and a real wind turbine captures less than half. Air is light: a cubic metre has a mass of only about $1.25\,\text{kg}$. This is why the rotor of a wind turbine has to be large, so that a lot of air flows through it every second.

```pysahdy
Air carries a lot of energy. Why is a wind turbine's rotor still made enormous?
---
Air is light, so its mass is small. A large rotor lets a lot of air pass through each second, and only then is enough kinetic energy captured.
```

<figure class="unit-photo"><img src="pics/fy4/middelgrunden-wind-farm.webp" alt="White wind turbines behind a breakwater against a blue sky. Open sea and a few boats are in the foreground."><figcaption>The Middelgrunden offshore wind farm off Copenhagen, Denmark, photographed from a boat.</figcaption></figure>

## Formula: Hydro and wind power

### Hydropower
The flow rate $Q$ tells how many cubic metres of water flow through the turbines each second. In time $t$ a volume $V = Qt$ flows through the turbines, and its mass is $m = \rho V = \rho Q t$. Its potential energy over the head $h$ is $mgh = \rho Q t g h$, so the power the water brings is $P_\text{o} = \rho Q g h$. By the definition of efficiency, the electric power is $\eta$ times this:
```latex
P = \eta \rho Q g h
```
where $P$ is the electric power of the plant ($\text{W}$), $\eta$ the efficiency, $\rho$ the density of water ($1000\,\text{kg/m}^3$), $Q$ the flow rate ($\text{m}^3\text{/s}$), $g$ the acceleration due to gravity ($9.81\,\text{m/s}^2$) and $h$ the head ($\text{m}$). The formula assumes that the kinetic energy of the water in the upper and lower water is small, so the energy that is converted is the change in potential energy.

### Wind power
Consider first the undisturbed wind, that is, the wind before the rotor has slowed it down. In time $t$ the undisturbed wind of speed $v$ would carry through the area swept by the rotor, $A = \pi r^2$, the air that fills a cylinder of length $vt$. The mass of this air is $m = \rho A v t$, and its kinetic energy is $\tfrac{1}{2}mv^2 = \tfrac{1}{2}\rho A v^3 t$. So the power flow of the undisturbed wind through the swept area is $P_\text{wind} = \tfrac{1}{2}\rho A v^3$.

In reality the rotor slows the air down already before the blades, so at the rotor the air flows more slowly than $v$, and its mass flow is not $\rho A v$. Therefore $P_\text{wind}$ is a reference power: it tells how much energy per second would pass through an area of the same size without the turbine. The efficiency $\eta$ of the turbine is defined as a fraction of this reference power, $\eta = P : P_\text{wind}$.

<svg data-fig="ilmalierio" viewBox="0 0 600 360" role="img" aria-label="Schematic, not to scale: the wind blows from the left towards the rotor of a wind turbine. In time t the undisturbed wind would carry air through the area swept by the rotor, and this air would fill a cylinder. The cross-sectional area of the cylinder is the area swept by the rotor, A = πr², and its length is s = vt, so the mass of the air would be m = ρAvt. The blue arrow is the wind speed v." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-ilmalierio.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="53.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="256" y="303.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = vt$</div></foreignObject>
  <foreignObject x="243.5" y="155.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = \rho A v t$</div></foreignObject>
  <foreignObject x="372" y="107.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="488" y="93.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A = \pi r^2$</div></foreignObject>
</svg>

So the electric power is:
```latex
P = \frac{1}{2}\eta \rho A v^3
```
where $P$ is the electric power ($\text{W}$), $\eta$ the efficiency of the turbine, that is, the electric power as a fraction of the reference power of the undisturbed wind, $\rho$ the density of air (about $1.25\,\text{kg/m}^3$), $A$ the area swept by the rotor ($\text{m}^2$) and $v$ the speed of the undisturbed wind ($\text{m/s}$).

### Why is the speed raised to the third power?
When the wind speed doubles, twice as much air passes through the swept area each second, and each kilogram of air has four times as much kinetic energy. So the reference power grows by a factor of $2 \cdot 4 = 2^3 = 8$. The electric power grows in the same ratio only in a model where the efficiency stays roughly constant. In the power curve of a real turbine, the power grows about $8.9$ times when the wind speed goes from $5\,\text{m/s}$ to $10\,\text{m/s}$, because the efficiency is slightly better at the higher speed.

A real turbine also has three ranges of wind speed that the cubic model does not describe. In a wind weaker than the cut-in speed, for this turbine about $3\text{–}4\,\text{m/s}$, the turbine produces no electricity. From a wind of about $13\,\text{m/s}$ on, the power stays at $1650\,\text{kW}$. This is the rated power of the turbine, which the generator cannot exceed, so the blades are turned to let part of the wind pass by. Then the formula with a constant efficiency no longer describes the turbine. In a storm wind stronger than the cut-out speed the turbine is stopped to protect its structure, and its power drops to zero.

<svg data-fig="tehokayra" viewBox="0 0 600 340" role="img" aria-label="Graph to scale, the power curve given by the manufacturer: the electric power P of a wind turbine in kilowatts as a function of the wind speed v, for a rotor diameter of 82 m. Points: 3 m/s 0 kW, 4 m/s 28 kW, 5 m/s 144 kW, 6 m/s 309 kW, 7 m/s 511 kW, 8 m/s 758 kW, 9 m/s 1017 kW, 10 m/s 1285 kW, 11 m/s 1504 kW, 12 m/s 1637 kW and 13–20 m/s 1650 kW. The dashed line is the model curve ½ηρAv³ for η = 0.45: it rises like the points but keeps rising when the points level off at 1650 kilowatts." style="max-width:100%;font-size:24px">
  <line x1="133.5" y1="296" x2="133.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="296" x2="171" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="208" y1="296" x2="208" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245.5" y1="296" x2="245.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="296" x2="283" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="296" x2="320.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358" y1="296" x2="358" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="296" x2="395" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="296" x2="432.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="296" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="268.5" x2="470" y2="268.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="241.5" x2="470" y2="241.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="214" x2="470" y2="214" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="186.5" x2="470" y2="186.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="159.5" x2="470" y2="159.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="132" x2="470" y2="132" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="104.5" x2="470" y2="104.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="77.5" x2="470" y2="77.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="296" x2="484" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,296 L483,302 L483,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,24 L102,37 L90,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="133.5" y1="296" x2="133.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="171" y1="296" x2="171" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="208" y1="296" x2="208" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="245.5" y1="296" x2="245.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="283" y1="296" x2="283" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="296" x2="320.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="304" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="358" y1="296" x2="358" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="395" y1="296" x2="395" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="378.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="432.5" y1="296" x2="432.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="296" x2="470" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="268.5" x2="96" y2="268.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="241.5" x2="96" y2="241.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="227" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="214" x2="96" y2="214" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="186.5" x2="96" y2="186.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="172" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="89" y1="159.5" x2="96" y2="159.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="132" x2="96" y2="132" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="117.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1200$</div></foreignObject>
  <line x1="89" y1="104.5" x2="96" y2="104.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="77.5" x2="96" y2="77.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="63" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1600$</div></foreignObject>
  <line x1="89" y1="50" x2="96" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <foreignObject x="110" y="15.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$P\ (\text{kW})$</span></div></foreignObject>
  <polyline points="96,296 97.5,296 99.5,296 101,296 102.5,296 104.5,296 106,296 107.5,296 109.5,296 111,296 112.5,296 114.5,296 116,296 117.5,295.5 119.5,295.5 121,295.5 122.5,295.5 124,295.5 126,295 127.5,295 129,295 131,294.5 132.5,294.5 134,294.5 136,294 137.5,294 139,293.5 141,293 142.5,293 144,292.5 146,292 147.5,292 149,291.5 151,291 152.5,290.5 154,290 156,289.5 157.5,289 159,288 161,287.5 162.5,287 164,286 166,285.5 167.5,284.5 169,284 171,283 172.5,282 174,281 175.5,280.5 177.5,279.5 179,278 180.5,277 182.5,276 184,275 185.5,273.5 187.5,272.5 189,271 190.5,269.5 192.5,268 194,267 195.5,265 197.5,263.5 199,262 200.5,260.5 202.5,258.5 204,257 205.5,255 207.5,253 209,251 210.5,249 212.5,247 214,245 215.5,243 217.5,240.5 219,238.5 220.5,236 222.5,233.5 224,231 225.5,228.5 227.5,226 229,223 230.5,220.5 232,217.5 234,214.5 235.5,211.5 237,208.5 239,205.5 240.5,202.5 242,199 244,195.5 245.5,192 247,188.5 249,185 250.5,181.5 252,178 254,174 255.5,170 257,166 259,162 260.5,158 262,153.5 264,149.5 265.5,145 267,140.5 269,136 270.5,131 272,126.5 274,121.5 275.5,116.5 277,111.5 279,106.5 280.5,101.5 282,96 283.5,90.5 285.5,85 287,79.5 288.5,74 290.5,68 292,62 293.5,56 295.5,50" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <foreignObject x="200.5" y="39.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\tfrac{1}{2}\eta\rho A v^3$</span></div></foreignObject>
  <circle cx="152" cy="296" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="171" cy="292" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189.5" cy="276.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="208" cy="254" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227" cy="226" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="245.5" cy="192.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="264.5" cy="157" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283" cy="120.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="301.5" cy="90.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="72.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="339" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="358" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="376.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="414" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="470" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="338" y="86" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{power curve}$</span></div></foreignObject>
</svg>

The points of the graph are the manufacturer's power curve of the Vestas V82 wind turbine (rotor diameter $82\,\text{m}$, rated power $1650\,\text{kW}$). A manufacturer's power curve is given for standard conditions, usually an air density of $1.225\,\text{kg/m}^3$ and ten-minute average winds at hub height. The dashed model curve is calculated with the density $1.25\,\text{kg/m}^3$, so the comparison is approximate. In too strong a wind the turbine is stopped, and its power drops to zero; the graph does not show this region. Source: Vestas Wind Systems, technical data of the V82 turbine; values from the NREL turbine archive (turbine-models, Vestas V82).

## Worked example
The rotor of a wind turbine has a diameter of $120\,\text{m}$. The wind speed is $9.0\,\text{m/s}$ and the density of air is $1.25\,\text{kg/m}^3$. The turbine converts into electricity $45\,\%$ of the power that the undisturbed wind carries through the area swept by the rotor. What is the electric power of the turbine?

<!-- vaihe -->

**Given and find.** The rotor diameter is $d = 120\,\text{m}$, the wind speed $v = 9.0\,\text{m/s}$, the density of air $\rho = 1.25\,\text{kg/m}^3$ and the efficiency $\eta = 45\,\%$. We are asked for the electric power $P$.

<!-- vaihe -->

**Principle.** The undisturbed wind carries the power $\tfrac{1}{2}\rho A v^3$ through the area swept by the rotor. The turbine converts the fraction $\eta$ of this reference power into electricity, so the electric power comes from the formula for the power of a wind turbine. The area $A$ is the circle swept by the rotor.

<!-- vaihe -->

**Formula solved.** The formula gives the asked power directly, once the area is calculated from the radius $r = \tfrac{d}{2}$:
```latex
\begin{aligned}
&P = \tfrac{1}{2}\eta\rho A v^3 \\
&A = \pi r^2
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The radius is $r = 120\,\text{m} : 2 = 60\,\text{m}$, and the efficiency as a decimal number is $\eta = 0.45$. The other quantities are in SI units, and $\tfrac{\text{kg}}{\text{m}^3}\cdot\text{m}^2\cdot\tfrac{\text{m}^3}{\text{s}^3} = \tfrac{\text{kg}\cdot\text{m}^2}{\text{s}^3} = \text{W}$.

<!-- vaihe -->

**Substitution.** First we calculate the area and then the power:
```latex
\begin{aligned}
A &= \pi r^2 \\
&= \pi\cdot(60\,\text{m})^2 \\
&= 11\,309.7\,\text{m}^2 \\
P &= \tfrac{1}{2}\eta\rho A v^3 \\
&= 0.5\cdot 0.45\cdot 1.25\,\tfrac{\text{kg}}{\text{m}^3} \\
&\quad\cdot 11\,309.7\,\text{m}^2\cdot\left(9.0\,\tfrac{\text{m}}{\text{s}}\right)^3 \\
&= 2\,318\,849\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Answer.** The electric power is about $2.3\,\text{MW}$, to two significant figures like the wind speed $9.0\,\text{m/s}$ and the efficiency $0.45$.

<!-- vaihe -->

**Reasonableness.** The turbine of the power curve, with a rotor diameter of $82\,\text{m}$, gives a power of $1017\,\text{kW}$ at a wind speed of $9\,\text{m/s}$. The area of this rotor is $(120 : 82)^2 \approx 2.14$ times as large, so the power should be about $2.14 \cdot 1.02\,\text{MW} \approx 2.2\,\text{MW}$. The result $2.3\,\text{MW}$ is of the same order of magnitude. The reference power of the undisturbed wind is $5.2\,\text{MW}$, and less than half of it becomes electricity, as it should.

## Common misconception
People often think that a power plant produces energy. A power plant converts energy: the electricity of a hydropower plant comes from the potential energy of water and the electricity of a wind turbine from the kinetic energy of the wind, and some of the energy always turns into something other than electricity. A second mistake is to assume that double the wind gives double the power. The power grows with the third power of the speed, until the turbine reaches its rated power. A third mistake is to mix up power and energy: power is given in watts, and energy is obtained by multiplying power by time. A power plant with a power of $3\,\text{MW}$ produces $3\,\text{MWh}$ of energy in an hour.

## Summary
- Hydro and wind power plants convert mechanical energy into electricity: a hydropower plant the potential energy of water, a wind turbine the kinetic energy of air.
- The efficiency $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ is at most $100\,\%$; for a large hydropower plant it is about $90\,\%$ and for a wind turbine below $50\,\%$.
- The power of a hydropower plant is $P = \eta\rho Q g h$: it is proportional to the flow rate and the head.
- The power of a wind turbine is $P = \tfrac{1}{2}\eta\rho A v^3$: when the efficiency stays roughly constant, double the wind speed gives about eight times the power, until the turbine reaches its rated power. In a very strong wind the turbine is stopped.
- Energy is power times time, $E = Pt$.
