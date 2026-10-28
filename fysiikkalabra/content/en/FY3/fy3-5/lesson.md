# Internal energy, heat and conservation of energy

> **Why** does a bicycle pump get hot when you pump up a tyre, even though nothing is heating the pump?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: hands push the handle of a foot pump down, and a hose leads air into a bicycle tyre. The lower part of the pump has warmed up, shown by an orange glow and wavy lines." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy35h-barrel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="520" width="1200" height="80" fill="#c9c2b2"/>
  <line x1="0" y1="520" x2="1200" y2="520" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="930" cy="330" r="210" fill="none" stroke="#1f2933" stroke-width="34"/>
  <circle cx="930" cy="330" r="186" fill="none" stroke="#8a96a3" stroke-width="4"/>
  <line x1="930" y1="330" x2="1114" y2="330" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1100" y2="400.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1060" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1000.5" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="930" y2="514" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="859.5" y2="500" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="800" y2="460" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="760" y2="400.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="746" y2="330" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="760" y2="259.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="800" y2="200" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="859.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="930" y2="146" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1000.5" y2="160" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1060" y2="200" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <line x1="930" y1="330" x2="1100" y2="259.5" stroke="#8a96a3" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="930" cy="330" r="22" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="764" y="270" width="24" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="500" width="200" height="22" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="220" width="60" height="284" rx="8" fill="url(#fy35h-barrel)" stroke="#1f2933" stroke-width="3"/>
  <rect x="370" y="400" width="60" height="104" rx="8" fill="#e8590c" fill-opacity="0.55"/>
  <rect x="370" y="220" width="60" height="284" fill="none" rx="8" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="392" y="140" width="16" height="84" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="300" y="124" width="200" height="28" rx="14" fill="#1f2933"/>
  <path d="M430,470 C520,470 560,400 640,380 S740,300 776,280" fill="none" stroke="#1f2933" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M340,470 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M460,470 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M330,90 L290,-10" fill="none" stroke="#1971c2" stroke-width="58" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="330" cy="128" rx="38" ry="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M470,90 L510,-10" fill="none" stroke="#1971c2" stroke-width="58" stroke-linejoin="round" stroke-linecap="round"/>
  <ellipse cx="470" cy="128" rx="38" ry="30" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M553,70 L553,154 L543,154 L560,180 L577,154 L567,154 L567,70 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

## Key idea
In chapter *Work and energy*, work was described as a way of transferring energy, and Joule's experiment showed that mechanical work can heat water: the work done by the weight increased the internal energy of the water, even though the water was not heated. Water does not contain "heat". The internal energy $U$ of a system is the sum of the kinetic energy of its particles and the energy of the interactions between the particles. According to the micro model, temperature tells you the average kinetic energy of the particles, so when the temperature of a gas or a liquid rises, its internal energy increases. Internal energy also depends on the amount of substance: a big lake contains much more internal energy than a cup of hot tea, even though the lake is colder.

You can change the internal energy of a system in two ways. The first is work: when the piston of a pump compresses air, the surroundings do work on the gas, and the internal energy of the gas increases, because the moving piston hits the particles like a bat hits a ball and they bounce off faster. In the simulation you can see this at the particle level. This is why the pump gets hot. The second is heat: when two objects at different temperatures touch, energy transfers by itself from the hotter one to the colder one until the temperatures are the same. Energy transferred in this way is called heat, and the amount of energy transferred is the quantity of heat $Q$. So heat is a transfer of energy, not a property of matter: an object has a temperature and internal energy, but it does not have heat.

<svg data-fig="two-ways" viewBox="0 0 600 316" role="img" aria-label="Two ways to change internal energy (schematic, not to scale). On the left, a piston is pushed into the cylinder and does work W on the air, and the air particles move faster. On the right, a hot and a cold object touch, and a quantity of heat Q is transferred from the hot one to the cold one." style="max-width:100%;font-size:24px">
  <foreignObject x="131" y="13.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{work}$</div></foreignObject>
  <foreignObject x="421" y="13.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat}$</div></foreignObject>
  <rect x="128" y="112" width="152" height="124" fill="#f2a69c"/>
  <path d="M70,112 H280 V236 H70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="112" y="113.5" width="16" height="121" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M22,181 L86,181 L86,189 L108,174 L86,159 L86,167 L22,167 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="50" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <line x1="160" y1="142" x2="174.5" y2="136.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M182,134 L175,141 L172,133.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="216" y1="140" x2="232.5" y2="145.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M240,148 L230,149 L232.5,141.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="254" y1="188" x2="239" y2="196" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M232,200 L238,192 L242,199 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="176" y1="196" x2="190" y2="183.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M196,178 L192,187 L186.5,181 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="150" y1="176" x2="164.5" y2="169.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M172,166 L165.5,173.5 L162,166 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="222" y1="214" x2="206" y2="211.5" stroke="#c92a2a" stroke-width="2" stroke-linecap="butt"/>
  <path d="M198,210 L207.5,207.5 L206,215.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="160" cy="142" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="216" cy="140" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="254" cy="188" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="176" cy="196" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="150" cy="176" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="222" cy="214" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="108.5" y="261.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{air heats up}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="322" y="112" width="120" height="124" fill="#f2a69c" stroke="#1f2933" stroke-width="3"/>
  <rect x="442" y="112" width="120" height="124" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="359.5" y="159.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hot}$</div></foreignObject>
  <foreignObject x="473" y="159.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{cold}$</div></foreignObject>
  <path d="M352,100 L504,100 L504,109 L532,92 L504,75 L504,84 L352,84 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="432" y="43.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="357" y="261.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{from hot to cold}$</div></foreignObject>
</svg>

Energy is conserved. When energy is transferred into a system as heat or work, its internal energy increases by exactly the amount of energy transferred, and when energy is transferred out, the internal energy decreases by the same amount. This is the first law of thermodynamics: the law of conservation of energy written for heat and work. An isolated system is a closed system into which, and out of which, no energy is transferred either as heat or as work. Its total energy stays constant, even if energy changes form inside it.

## Formula: First law of thermodynamics
The change in internal energy is the sum of the quantity of heat transferred into the system and the work done on the system:
```latex
\Delta U = Q + W
```
where $\Delta U$ is the change in internal energy (J), $Q$ is the quantity of heat transferred into the system (J) and $W$ is the work done on the system by the surroundings (J). The signs tell you the direction: $Q$ is positive when heat is transferred into the system and negative when it is transferred out; $W$ is positive when the surroundings do work on the system (for example, compress a gas) and negative when the system does work on the surroundings (the gas expands and pushes the piston). All the terms are in joules, the same unit as work in chapter *Work and energy*, and the work done by a piston on a gas is calculated in the same way as there, as the product of force and distance.

<svg data-fig="energy-balance" viewBox="0 0 600 300" role="img" aria-label="Energy diagram: a quantity of heat Q and work W enter the system, and the internal energy of the system changes by their sum. Energy transferred out is negative." style="max-width:100%;font-size:24px">
  <rect x="206" y="62" width="188" height="160" rx="14" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="258.5" y="103.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{system}$</div></foreignObject>
  <foreignObject x="258.5" y="151.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta U = Q + W$</div></foreignObject>
  <path d="M24,108 L172,108 L172,117 L200,100 L172,83 L172,92 L24,92 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="75" y="51.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{heat}\ Q$</div></foreignObject>
  <path d="M24,194 L172,194 L172,203 L200,186 L172,169 L172,178 L24,178 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="75" y="209.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{work}\ W$</div></foreignObject>
  <path d="M400,150 L548,150 L548,159 L576,142 L548,125 L548,134 L400,134 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="430.5" y="87.5" width="115" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q < 0\ \text{or}\ W < 0$</div></foreignObject>
  <foreignObject x="465.5" y="163.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{out}$</div></foreignObject>
  <foreignObject x="158.5" y="247.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{in positive, out negative}$</div></foreignObject>
</svg>

<svg data-fig="work-sign" viewBox="0 0 600 316" role="img" aria-label="The sign of work (schematic, not to scale). On the left, the piston is pushed in and the gas is compressed: the surroundings do work on the gas, so W is positive. On the right, the gas pushes the piston out and expands: the gas does work on the surroundings, so W is negative." style="max-width:100%;font-size:24px">
  <foreignObject x="102.5" y="13.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{compression}$</div></foreignObject>
  <foreignObject x="395" y="13.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{expansion}$</div></foreignObject>
  <rect x="142" y="100" width="138" height="110" fill="#eef5f9"/>
  <path d="M70,100 H280 V210 H70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="126" y="101.5" width="16" height="107" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M22,162 L100,162 L100,170 L122,155 L100,140 L100,148 L22,148 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="168" cy="124" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="212" cy="130" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="252" cy="150" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="186" cy="160" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="232" cy="186" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="166" cy="192" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="206" cy="178" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="416" y="100" width="164" height="110" fill="#eef5f9"/>
  <path d="M330,100 H580 V210 H330" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="400" y="101.5" width="16" height="107" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M396,148 L358,148 L358,140 L336,155 L358,170 L358,162 L396,162 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="450" cy="122" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="520" cy="128" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="556" cy="158" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="478" cy="156" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="536" cy="190" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="448" cy="190" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="500" cy="178" r="6" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="300" y1="20" x2="300" y2="292" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="152.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="432.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="58.5" y="269.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{surroundings do work}$</div></foreignObject>
  <foreignObject x="382.5" y="269.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gas does work}$</div></foreignObject>
</svg>

## Worked example
A pump cylinder contains air. The piston is pushed down, so the surroundings do 150 J of work on the air. At the same time, a quantity of heat of 40 J is transferred from the warming air through the cylinder walls to the surroundings. By how much does the internal energy of the air change?

<!-- vaihe -->

**Given and find.** The air is the system. The surroundings do work on the system, so $W = +150\,\text{J}$. Heat is transferred out of the system, so $Q = -40\,\text{J}$. The quantity to find is the change in internal energy $\Delta U$.

<!-- vaihe -->

**Principle.** Energy is conserved: the internal energy of the system changes by exactly the amount of energy transferred into it as heat and work. This is the first law of thermodynamics, and it applies because the air is a clearly bounded system, and energy crosses its boundary only as work and heat.

<!-- vaihe -->

**Rearranged formula.** In the first law, the quantity to find $\Delta U$ is already alone on the left-hand side, so the equation does not need rearranging:

```latex
\begin{aligned}
&\Delta U = Q + W
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None needed: both $Q$ and $W$ are given in joules, and the result is wanted in joules. The signs, however, must be decided: energy into the system is positive and energy out of the system is negative.

<!-- vaihe -->

**Substitution.** Substitute the values with their signs:

```latex
\begin{aligned}
&\Delta U = Q + W \\
&= -40\,\text{J} + 150\,\text{J} \\
&= 110\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Result.** The internal energy of the air increases by $110\,\text{J}$. The result is given in whole joules, because both the work and the heat were given in whole joules.

<!-- vaihe -->

**Reasonableness.** The work brought 150 J into the air and only 40 J left as heat, so the internal energy must increase and the temperature of the air must rise. If the same 150 J of work were done so slowly that all the energy from the work had time to leave as heat, then $Q = -150\,\text{J}$ and $\Delta U = 0$, and the temperature would not change. Now less heat leaves, so the result lies between this limiting case and the work alone, $150\,\text{J}$.

## Common misconception
In everyday language we say that an object "has heat" or that heat is "stored". In physics, heat is the transfer of energy because of a temperature difference, and what is stored in an object is internal energy. Another mistake is to treat temperature and internal energy as the same thing: a hot spark has a temperature of thousands of degrees, but its internal energy is small, because it contains very little matter. A third mistake is to think that internal energy can be changed only by heating. The air in a pump gets hot without any heat source, because work is done on it.

## Summary
- The internal energy $U$ is the sum of the kinetic energy of the particles of a system and the energy of the interactions between the particles. It increases when the temperature rises, and it also depends on the amount of substance.
- Heat is the transfer of energy from hotter to colder because of a temperature difference; the energy transferred is the quantity of heat $Q$. An object does not "have heat".
- Heat and work change internal energy: $\Delta U = Q + W$. Energy transferred in is positive and energy transferred out is negative.
- Energy is conserved: this is the first law of thermodynamics. The total energy of an isolated system stays constant.
