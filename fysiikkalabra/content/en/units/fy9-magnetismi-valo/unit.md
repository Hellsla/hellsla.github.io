# Magnetism, induction and light

> **Why** does the electricity for the cottages on an island travel in a submarine cable at a voltage of $20\,\text{kV}$, although the cottages use a voltage of $230\,\text{V}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: an archipelago landscape in cross-section at dusk. On the left, on the mainland shore, a power-line pylon and a grey substation. A dark submarine cable leaves the substation, descends along the rocky shore to the seabed, runs under the water along the sandy bottom and rises on the right onto an island. On the island there is a second small substation and a red cottage with light shining from its window. Behind the cottage a birch and a spruce, on the horizon distant islands." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

The phenomena of the module are connected with two fields. A **magnetic field** $\overline{B}$ does not act on a charge at rest; on a moving charge and on a current-carrying wire it exerts a force when the motion or the current is not parallel to the field, and the force is perpendicular to both the motion and the field. A **changing magnetic flux** produces a voltage: the generator, the transformer, the induction hob and the eddy-current brake are based on this. When the electric and magnetic fields change and produce each other, an **electromagnetic wave** forms, and its visible part is light.

<svg data-fig="kartta" viewBox="0 0 380 866" role="img" aria-label="Recognition chart: how do I tell which law to use? Make a picture and mark the directions first, then see which sign in the task fits. A particle moves in a field: the magnetic force is charge times speed times the perpendicular magnetic flux density. A current-carrying wire in a field: the force is current times wire length times the perpendicular flux density. A particle moves in a circle: the magnetic force is the centripetal force, and the radius is mass times speed divided by charge times flux density. The magnetic flux changes: the induced voltage in a coil is minus the number of turns times the change of flux divided by the time. Transformer: the ratio of the numbers of turns equals the ratio of the voltages. A generator rotates: the peak voltage is the number of turns times the area times the flux density times two pi times the frequency. Light passes from one medium to another: use Snell&#x27;s law of refraction. Light cannot get out of a medium: the sine of the critical angle is the ratio of the refractive indices. Light hits a grating: the grating equation, the slit spacing times the sine of the angle equals the order times the wavelength." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{how do I tell the law?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{picture and directions first, then the sign}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a particle moves in a field}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{force}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{M} = QvB_\perp$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a current-carrying wire in a field}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{force}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{M} = I\ell B_\perp$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a particle moves in a circle}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{centripetal force}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$r = mv/(QB)$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{the magnetic flux changes}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{induction}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$e = -N\Delta\Phi/\Delta t$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{transformer}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{turns and voltage}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$N_1/N_2 = U_1/U_2$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{a generator rotates}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{peak voltage}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$u_0 = NAB\,2\pi f$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{light enters another medium}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{refraction}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{Snell's law}$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{light cannot get out of a medium}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{total reflection}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\sin\alpha_\text{r} = n_2/n_1$</div></foreignObject>
  <line x1="14" y1="822" x2="30" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{light hits a grating}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{interference}$</div></foreignObject>
  <rect x="238" y="830" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="832" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$d\sin\alpha = n\lambda$</div></foreignObject>
</svg>

In exam problems it pays to ask first what changes. If the flux does not change, no voltage is produced. When light passes from one medium into another, the frequency stays the same, but the speed and the wavelength change. The colours of light and bright and dark spots are explained either by refraction or by interference, and in a problem you have to recognise which one it is.

This gives the answer to the opening question. A power of $40\,\text{kW}$ is transmitted along the cable from the mainland, and the resistance of the cable is $0.50\,\Omega$. At the voltage $230\,\text{V}$ the current in the cable would be $I = \tfrac{P}{U} \approx 174\,\text{A}$, and about $15\,\text{kW}$, or $38\,\%$ of the power, would be converted into internal energy in the resistance of the cable (the power loss is derived under *Induction and alternating current*). At the voltage $20\,\text{kV}$ the current is only $2.0\,\text{A}$, and the loss is $2.0\,\text{W}$. Transformers step the voltage up on the mainland and down on the island.

<svg data-fig="siirto" viewBox="0 0 600 360" role="img" aria-label="Diagram to scale: the same power of 40 kilowatts is transmitted through a cable whose resistance is 0.50 ohms. Upper bar: at a voltage of 230 volts the current is 174 amperes, and the reddish-brown part of the bar, the power of 15 kilowatts that is converted into internal energy of the cable, is 38 per cent of the whole bar. Lower bar: at a voltage of 20 kilovolts the current is 2.0 amperes, and only 2.0 watts is converted into internal energy, 0.005 per cent, which is thinner than a line in the bar." style="max-width:100%;font-size:24px">
  <foreignObject x="194.5" y="7.5" width="211" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P = 40\,\text{kW},\ R = 0.50\,\Omega$</div></foreignObject>
  <foreignObject x="24" y="59.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 230\,\text{V}$</div></foreignObject>
  <foreignObject x="481" y="59.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I \approx 174\,\text{A}$</div></foreignObject>
  <rect x="24" y="100" width="552" height="46" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="367.5" y="100" width="208.5" height="46" fill="#8f3b1b"/>
  <rect x="24" y="100" width="552" height="46" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="108.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{delivered } 25\,\text{kW}$</div></foreignObject>
  <foreignObject x="494" y="108.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$15\,\text{kW}$</div></foreignObject>
  <foreignObject x="468" y="155.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8f3b1b">$\text{loss } 38\,\%$</div></foreignObject>
  <foreignObject x="24" y="199.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 20\,\text{kV}$</div></foreignObject>
  <foreignObject x="481" y="199.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I = 2.0\,\text{A}$</div></foreignObject>
  <rect x="24" y="240" width="552" height="46" rx="4" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="574" y="240" width="2" height="46" fill="#8f3b1b"/>
  <rect x="24" y="240" width="552" height="46" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="36" y="248.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{delivered almost } 40\,\text{kW}$</div></foreignObject>
  <foreignObject x="356" y="295.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#8f3b1b">$\text{loss } 2.0\,\text{W} = 0.005\,\%$</div></foreignObject>
</svg>

## Formula: Magnetism, induction and light

### Magnetic field and forces

```kaavat
magnetic force on a charged particle :: F_\text{M} = QvB_\perp
magnetic force on a straight conductor :: F_\text{M} = I\ell B_\perp
magnetic flux density of a straight current-carrying wire :: B = \frac{\mu_0}{2\pi r}\,I
magnetic flux density of a long solenoid :: B = N\,\frac{\mu_0}{\ell}\,I
```

where $F_\text{M}$ is the magnetic force ($\text{N}$), $Q$ the charge ($\text{C}$), $v$ the speed ($\text{m/s}$), $B$ the magnetic flux density ($\text{T}$), $B_\perp = B\sin\alpha$ its component perpendicular to the velocity or the wire, when $\alpha$ is the angle between the velocity or the wire and the field, $r$ the distance from the wire ($\text{m}$), $I$ the current ($\text{A}$), $\ell$ the length of the wire or the coil ($\text{m}$), $N$ the number of turns and $\mu_0 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$. The magnetic force does not change the speed. The formula for the wire holds for a long straight wire, and the formula for the coil at the middle of a long coil.

When a charged particle of mass $m$ ($\text{kg}$) and charge $Q$ moves with the speed $v$ perpendicular to a uniform magnetic field, the magnetic force is always perpendicular to the velocity. The particle then moves in uniform circular motion on a path of radius $r$ ($\text{m}$).

<svg data-fig="ympyra" viewBox="0 0 600 420" role="img" aria-label="Diagram: a positive particle in a uniform magnetic field pointing into the paper (green crosses). The path of the particle is a dashed circle, which it goes round anticlockwise. At four points of the path a blue velocity arrow is along the path and a red arrow of the magnetic force points to the centre of the circle, perpendicular to the velocity. The radius r is marked from the centre to the path." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-ympyra.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="302" y="169.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="241" y="342" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="381" y="202" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="241" y="62" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="101" y="202" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="334" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="264" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{M}$</div></foreignObject>
  <foreignObject x="416" y="387.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{into the page}$</div></foreignObject>
</svg>

```johda
A charged particle (mass $m$, charge $Q$) moves with the speed $v$ perpendicular to a uniform magnetic field $B$. Derive the radius $r$ of its circular path.
---
The magnetic force is perpendicular to the velocity, so it does not change the speed, only the direction of motion: the particle is in uniform circular motion. The magnetic force is the only force acting, so by Newton's second law it gives the particle the centripetal acceleration $a_\text{n} = \tfrac{v^2}{r}$:

$$F_\text{M} = ma_\text{n} = m\frac{v^2}{r}$$

The velocity is perpendicular to the field, so $B_\perp = B$, and the magnetic force on a charged particle is $F_\text{M} = QvB$. Substitute:

$$QvB = m\frac{v^2}{r}$$

Divide both sides by $v$ and solve for the radius:

$$r = \frac{mv}{QB}$$

Here $Q$ is the magnitude of the charge. The result holds when the speed is small compared with the speed of light and gravity is negligible compared with the magnetic force.
```

### Induction and alternating current

```kaavat
voltage induced in a coil :: e = -N\frac{\Delta\Phi}{\Delta t}
peak value of the sinusoidal voltage induced in a generator coil :: u_0 = NAB\cdot 2\pi f
rms value of a sinusoidal alternating voltage :: U_\text{eff} = \frac{u_0}{\sqrt{2}}
transformer :: \frac{N_1}{N_2} = \frac{U_1}{U_2} \approx \frac{I_2}{I_1}
```

where $e$ is the induced voltage ($\text{V}$), $\Phi = BA$ the magnetic flux ($\text{Wb}$) when the field is perpendicular to the surface $A$, $u_0$ the peak value of the generator voltage, $f$ the rotation frequency ($\text{Hz}$), $U_\text{eff}$ and $u_0$ the rms value and the peak value, the indices $1$ and $2$ the primary and secondary side of the transformer. The minus sign is Lenz's law: the induced current opposes the change of flux. The voltage of a rod moving in a field is $e = vBl$. The transformer equation applies to an alternating voltage; the ratio of the currents is an equality only in an ideal, lossless transformer.

A transmission line carries the power $P$ ($\text{W}$) at the transmission voltage $U$ ($\text{V}$), and the resistance of the line is $R$ ($\Omega$). Part of the power is converted into internal energy of the line, which is transferred to the surroundings as heat, and this power loss $P_\text{h}$ ($\text{W}$) depends on the current in the line.

```johda
A transmission line carries the power $P$ at the voltage $U$, and the resistance of the line is $R$. Derive the power loss $P_\text{h}$ of the line first in terms of the current $I$ and then in terms of the power $P$ and the voltage $U$.
---
The current in the line follows from the transmitted power. The power consumed in a conductor is $P = UI$, so

$$I = \frac{P}{U}$$

The transmission voltage $U$ is not across the line. The voltage between the ends of the line is the voltage drop across a conductor, $RI$, and the power converted into internal energy in the line is this voltage times the current:

$$P_\text{h} = RI \cdot I = RI^2$$

Substitute the current:

$$P_\text{h} = R\left(\frac{P}{U}\right)^2 = \frac{RP^2}{U^2}$$

The loss is inversely proportional to the square of the transmission voltage. When a transformer raises the transmission voltage $10$-fold, the current falls to a tenth and the loss to a hundredth.
```

### Light

```kaavat
wave equation :: c = f\lambda
Wien's displacement law :: \lambda_\text{max} = \frac{b}{T}
law of refraction (Snell's law) :: \frac{\sin\alpha_1}{\sin\alpha_2} = \frac{v_1}{v_2} = \frac{n_2}{n_1}
grating equation :: d\sin\alpha = n\lambda
I = I_0\cos^2\theta
```

where $c = 3.00 \cdot 10^8\,\text{m/s}$, $f$ is the frequency, $\lambda$ the wavelength, $T$ the absolute temperature ($\text{K}$), $b = 2.898 \cdot 10^{-3}\,\text{m} \cdot \text{K}$, $n = \tfrac{c}{v}$ the refractive index and $v$ the speed of light in the material, $\alpha_1$ and $\alpha_2$ the angles of incidence and refraction from the normal, $d$ the grating constant, in the grating equation $\alpha$ the direction of a maximum and $n = 0, 1, 2, \ldots$ its order, and $I_0$ the intensity of the polarised light before the analyser. In Malus's law $\theta$ is the angle between the direction of polarisation and the transmission axis of the analyser. In a thin film the path difference is $2nd$ when the light arrives almost perpendicularly. When only one of the reflections inverts the wave, $2nd = \left(k + \tfrac12\right)\lambda$ gives constructive interference; when both invert it, $2nd = k\lambda$.

When light passes from a medium of higher refractive index into one of lower refractive index ($n_1 > n_2$), the angle of refraction is larger than the angle of incidence. The angle of incidence at which the angle of refraction is $90^\circ$ is the critical angle $\alpha_\text{r}$, and at larger angles of incidence the light is totally internally reflected.

<svg data-fig="rajakulma" viewBox="0 0 600 330" role="img" aria-label="Schematic, no numbers. Below is a medium with the larger refractive index n 1, above a medium with the smaller refractive index n 2. A lamp at the bottom sends two light rays to the boundary. At each point where a ray meets the boundary the normal is drawn as a dashed line. The left ray meets the boundary at the critical angle alpha r: the refracted ray runs along the boundary, so the angle of refraction alpha 2 is 90 degrees, and a weak part is reflected back. The right ray meets the boundary at an angle larger than the critical angle: no light refracts into the upper medium, and the whole ray is reflected back, which is total internal reflection." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-magnetismi-valo-rajakulma.webp" x="1.2" y="1.2" width="597" height="335.8" preserveAspectRatio="none"/>
  <foreignObject x="226" y="195.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_\text{r}$</div></foreignObject>
  <foreignObject x="309.5" y="81.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_2 = 90^\circ$</div></foreignObject>
  <foreignObject x="389.5" y="19.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1 > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="24" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_2$</div></foreignObject>
  <foreignObject x="24" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1$</div></foreignObject>
  <foreignObject x="275" y="275.5" width="295" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{total internal reflection}$</div></foreignObject>
</svg>

```johda
Light travels in a medium of refractive index $n_1$ towards the boundary with a medium of refractive index $n_2 < n_1$. Derive the critical angle $\alpha_\text{r}$ of total internal reflection.
---
The law of refraction (Snell's law) relates the angle of incidence $\alpha_1$ and the angle of refraction $\alpha_2$:

$$\frac{\sin\alpha_1}{\sin\alpha_2} = \frac{n_2}{n_1}$$

At the critical angle the refracted ray runs along the boundary, so $\alpha_1 = \alpha_\text{r}$ and $\alpha_2 = 90^\circ$. Since $\sin 90^\circ = 1$,

$$\sin\alpha_\text{r} = \frac{n_2}{n_1}$$

At a larger angle of incidence the law of refraction would give $\sin\alpha_2 > 1$, which is impossible. The light then does not refract into the other medium but is reflected back completely.
```

## Common mistakes {Virheet}

- **Force in the direction of the field.** The magnetic force is perpendicular to the velocity and the field, and on a negative charge it points in the opposite direction.
- **Large field, large voltage.** The induced voltage depends on the rate of change of the flux, not on the size of the flux.
- **Lenz opposes the field.** The induced current opposes the change of flux: a ring attracts a receding magnet.
- **Loss from the formula $\tfrac{U^2}{R}$.** The transmission voltage is not across the line. First calculate the current $I = \tfrac{P}{U}$, then the power loss from the resistance of the line and the current.
- **Peak value and rms value mixed up.** The $230\,\text{V}$ of a socket is the rms value.
- **Angle from the surface.** The angles of incidence and refraction are measured from the normal.
- **Small angle in a grating.** First calculate the angle from the tangent $\tan\theta = \tfrac{x}{L}$, and only then the sine.
- **Wien in degrees Celsius.** The temperature is in kelvins.

## Review if needed {Kertaa}

- Field and forces: [*Magnets, the magnetic dipole and the magnetic field*](fy7-1.html), [*Charged particle in electric and magnetic fields*](fy7-2.html), [*Magnetic field of a wire and a coil*](fy7-3.html) and [*Force on a current-carrying wire: the electric motor and the loudspeaker*](fy7-4.html).
- Induction: [*Electromagnetic induction*](fy7-5.html), [*Lenz's law and eddy currents*](fy7-6.html), [*The generator and alternating current*](fy7-7.html) and [*The transformer and the transmission of electrical energy*](fy7-8.html).
- Radiation and the path of light: [*Electromagnetic radiation and the black-body spectrum*](fy7-9.html), [*Reflection and refraction of light*](fy7-10.html), [*Dispersion: the prism and the rainbow*](fy7-11.html) and [*Total internal reflection and optical fibre*](fy7-12.html).
- Light as a wave: [*Interference and diffraction of light*](fy7-13.html), [*Thin-film interference*](fy7-14.html) and [*Polarisation of light*](fy7-15.html).
- Applications: [*Applied chapter: wireless charging, the induction hob and the fibre link*](fy7-16.html).
