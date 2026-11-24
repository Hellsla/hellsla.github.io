# Inside ITER: the machine and fusion gain

> **Why** is it so hard to get more energy out of a fusion plasma than you put into it?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a cut-away view of a huge doughnut-shaped machine in a dark hall. In the middle stands a tall stack of coils. On both sides, large D-shaped magnet coils surround a steel chamber with a double wall. Inside each half of the chamber a pink, glowing ring of plasma floats without touching the walls. A pale blue haze around the coils shows that they are extremely cold, while the plasma glows hot. A huge steel vessel with a domed lid encloses everything." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-inside-iter-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## The parts of the machine {Machine}

ITER is a **tokamak**. Its plasma, about $830\ \text{m}^3$ of deuterium and tritium at about $150$ million $^\circ\text{C}$, is held by magnetic fields inside a ring-shaped steel chamber.

- **Magnets.** $18$ D-shaped **toroidal field coils** make the field that runs around the ring (up to $11.8\ \text{T}$). Six ring-shaped **poloidal field coils** shape the plasma and hold it in place. The **central solenoid**, a $13\ \text{m}$ tall stack of six modules, works like the primary coil of a transformer: a changing current in it drives a current of up to $15\ \text{MA}$ in the plasma. All the magnets are **superconducting** and are cooled with helium to about $4\ \text{K}$.
- **Vacuum vessel.** A double-walled steel chamber, $19.4\ \text{m}$ wide, keeps the vacuum and is the first barrier that keeps tritium in.
- **Blanket.** $440$ modules line the inside of the vessel. They take the heat and the fast neutrons and shield the vessel and the magnets.
- **Divertor.** At the bottom, $54$ cassettes with tungsten targets catch the heat and the helium "ash" that flow out along the edge of the plasma. The heat flow there is up to about $10\text{–}20\ \text{MW}$ on each square metre, the highest in the machine.
- **Heating.** Beams of fast neutral atoms and two kinds of radio waves heat the plasma with a planned $50\ \text{MW}$.
- **Cryostat.** A vacuum chamber about $30\ \text{m}$ tall around everything insulates the cold magnets from the warm building.

```pysahdy
How does the central solenoid drive a current of up to $15\,\text{MA}$ in the plasma?
---
It works like the primary coil of a transformer: a changing current in the solenoid induces a current in the plasma, which acts as the secondary coil.
```

<figure class="unit-photo"><img src="units/fy14/pics/iter-magnet-coil.jpg" alt="Colour photograph of a very large ring-shaped magnet coil in a factory hall." width="1600" height="1067" loading="lazy"><figcaption>A poloidal field coil being built in the coil factory on the ITER site. These giant rings shape and position the plasma. <span class="photo-credit">Photo: Johannes Reimer, CC BY 4.0, via Wikimedia Commons</span></figcaption></figure>

<figure class="unit-photo"><img src="units/fy14/pics/iter-vacuum-vessel-hellsten.jpg" alt="Colour photograph looking up in the ITER assembly hall: a huge curved steel vacuum-vessel sector hangs in a grey tooling frame next to pink-wrapped D-shaped magnet coils, with yellow cranes overhead and workers on scaffolding." width="1200" height="1600" loading="lazy"><figcaption>A sector of the ITER vacuum vessel in its assembly tooling, 26 March 2024, next to D-shaped toroidal field coils wrapped in pink protective film. The workers on the scaffolding show the scale: one sector is about as tall as a four-storey building. <span class="photo-credit">Photo: Lauri Hellsten</span></figcaption></figure>

## Key idea

A fusion plasma loses energy all the time: hot particles escape across the magnetic field and the plasma radiates. To keep it hot, we heat it from outside. The **fusion gain** $Q$ compares the fusion power produced in the plasma with this heating power.

At $Q = 1$, called **scientific breakeven**, the plasma produces as much fusion power as it receives. No magnetic fusion experiment has reached it yet with real $\text{D–T}$ fuel: JET's record from 1997 was $16\ \text{MW}$ of fusion power from $24\ \text{MW}$ of heating, $Q \approx 0.67$. ITER's goal is $Q = 10$: $500\ \text{MW}$ of fusion power from $50\ \text{MW}$ of heating, in pulses of $400\text{–}600\ \text{s}$. In D–T fusion, $3.5\ \text{MeV}$ of the $17.6\ \text{MeV}$ goes to the helium nucleus, which is charged and stays in the plasma. At $Q = 10$ these helium nuclei heat the plasma about twice as much as the external heating does: a **burning plasma**.

## Formula: Fusion gain

```latex
Q = \frac{P_\text{fusion}}{P_\text{heating}}
```

Here $P_\text{fusion}$ is the fusion power produced in the plasma and $P_\text{heating}$ is the heating power that reaches the plasma from outside. Both are in watts, so $Q$ has no unit.

<svg data-fig="power" viewBox="0 0 560 500" role="img" aria-label="Bar chart to scale, power in megawatts. First bar: 50 MW of heating power delivered into the plasma. Second bar: 500 MW of fusion power made in the plasma, divided into about 400 MW carried by neutrons, which leave the plasma and heat the blanket, and about 100 MW carried by helium nuclei, which stay in the plasma and heat it. Third bar: the electricity that the whole ITER plant draws from the grid, at least 110 MW, drawn solid, and up to 620 MW in peaks of 30 seconds, drawn as a pale range with a dashed outline." style="max-width:100%;font-size:26px">
  <line x1="64" y1="400" x2="545" y2="400" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="64" y1="298.5" x2="545" y2="298.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="283" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200$</div></foreignObject>
  <line x1="64" y1="197" x2="545" y2="197" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="181.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$400$</div></foreignObject>
  <line x1="64" y1="95.5" x2="545" y2="95.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="7" y="80" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$600$</div></foreignObject>
  <foreignObject x="34" y="384.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0$</div></foreignObject>
  <foreignObject x="8" y="10.5" width="80" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$P\ (\text{MW})$</div></foreignObject>
  <rect x="80" y="374.5" width="90" height="25.5" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="107.5" y="337" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$50$</div></foreignObject>
  <rect x="215" y="146" width="130" height="50.5" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="215" y="196.5" width="130" height="203.5" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="242" y="156" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#ffffff">$\alpha\text{: }100$</div></foreignObject>
  <foreignObject x="242" y="283" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#ffffff">$\text{n: }400$</div></foreignObject>
  <foreignObject x="255.5" y="108.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$500$</div></foreignObject>
  <rect x="395" y="85" width="130" height="259" fill="#b2f2bb" fill-opacity="0.45"/>
  <path d="M395,344 L395,85 L525,85 L525,344" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round" stroke-dasharray="6 5"/>
  <rect x="395" y="344" width="130" height="56" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="435.5" y="356.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$110$</div></foreignObject>
  <foreignObject x="435.5" y="47.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$620$</div></foreignObject>
  <foreignObject x="422" y="199" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{peaks}$</div></foreignObject>
  <foreignObject x="73.5" y="410.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{heating}$</div></foreignObject>
  <foreignObject x="53.5" y="444.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{into plasma}$</div></foreignObject>
  <foreignObject x="235.5" y="410.5" width="89" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{fusion}$</div></foreignObject>
  <foreignObject x="222" y="444.5" width="116" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{in plasma}$</div></foreignObject>
  <foreignObject x="429" y="410.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{grid}$</div></foreignObject>
  <foreignObject x="368" y="444.5" width="184" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{electricity in}$</div></foreignObject>
</svg>

**Gain is not electricity.** $Q$ describes the plasma only. ITER has no turbines and will not produce any electricity. During a pulse the whole plant (heating systems, cooling water, cryogenics, magnets) draws far more electricity than the $50\ \text{MW}$ that reaches the plasma. According to ITER, it needs $110\ \text{MW}$ at the least and up to $620\ \text{MW}$ in peaks of $30\ \text{s}$; the cooling water and the cryogenic systems take about $80\ \%$ of it. A power plant would turn the heat into electricity with steam turbines, typically about one third of it. Even then, $500\ \text{MW}$ of heat would give only about $170\ \text{MW}$ of electricity: far less than ITER's peak demand of $620\ \text{MW}$.

**Scientific gain is not commercial viability.** A power plant must also produce more electricity than the whole plant uses, run for months instead of minutes, breed its own tritium, survive years of neutron damage and sell its electricity at a price people will pay. ITER is built to test the physics and the technology for that, not to show that fusion electricity is cheap.

## Fuel, blankets and radiation {Fuel}

**Tritium fuel cycle.** Only a small fraction of the fuel, about one per cent according to ITER, fuses on its way through the plasma. Cryopumps pump the exhaust out of the vessel, and the tritium plant separates the hydrogen isotopes and sends deuterium and tritium back to the fuelling system. Tritium is radioactive (half-life $12.3$ years, a weak beta emitter), so detritiation systems take it out of air and water.

```pysahdy
Only about one per cent of the fuel fuses on its way through the plasma. What happens to the rest?
---
Cryopumps remove it from the vessel, the tritium plant separates the hydrogen isotopes, and deuterium and tritium are sent back to the fuelling system.
```

**Breeding.** Tritium is very rare; today it comes mainly from heavy-water fission reactors. A power plant must make its own from lithium: $^{6}_{3}\text{Li} + \text{n} \to {}^{4}_{2}\text{He} + {}^{3}_{1}\text{H} + 4.8\ \text{MeV}$. In ITER, a few **test blanket modules** will try out ways to do this.

**Radiation protection.** The fast neutrons make the vessel and the blanket radioactive (**activation**), so parts inside the vessel are changed by remote-handling robots. A thick concrete **bioshield** surrounds the machine. The fuel leaves no long-lived high-level waste, and the reaction stops by itself if anything fails, but tritium, activated parts, the strong magnets and the heat are real hazards. ITER obtained the licence of a French nuclear installation in 2012.

## Worked example

ITER's goal is a pulse with $P_\text{heating} = 50\ \text{MW}$ and $P_\text{fusion} = 500\ \text{MW}$. Calculate the fusion gain $Q$ and the power carried by the helium nuclei. Do the helium nuclei heat the plasma more than the external heating does?

<!-- vaihe -->

**Given:** heating power ${P_\text{heating} = 50\ \text{MW}}$, fusion power ${P_\text{fusion} = 500\ \text{MW}}$. In one $\text{D–T}$ reaction, ${E_\text{total} = 17.6\ \text{MeV}}$ is released and the helium nucleus carries ${E_\alpha = 3.5\ \text{MeV}}$. **Find:** $Q$ and the helium power $P_\alpha$.

<!-- vaihe -->

**Principle:** $Q$ is the ratio of the two powers. Every reaction gives the same share of its energy to the helium nucleus, so the helium nuclei carry the same share of the fusion power.

<!-- vaihe -->

**Formula:**
```latex
\begin{aligned}
Q &= \frac{P_\text{fusion}}{P_\text{heating}} \\
P_\alpha &= \frac{E_\alpha}{E_\text{total}} \cdot P_\text{fusion}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions:** None are needed. Both powers are in megawatts and both energies in megaelectronvolts, so the units cancel in each ratio.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
Q &= \frac{500\ \text{MW}}{50\ \text{MW}} = 10 \\[6pt]
P_\alpha &= \frac{3.5\ \text{MeV}}{17.6\ \text{MeV}} \cdot 500\ \text{MW} \\
&= 0.1989 \cdot 500\ \text{MW} \\
&= 99.4\ \text{MW}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $Q = 10$ and $P_\alpha \approx 99\ \text{MW}$, two significant figures as in $3.5\ \text{MeV}$. The helium nuclei heat the plasma with about $99\ \text{MW}$, about twice the external $50\ \text{MW}$: about two thirds of the heating comes from fusion itself.

<!-- vaihe -->

**Reasonableness:** The helium nucleus is about four times heavier than the neutron, so by conservation of momentum it gets about one fifth of the energy: one fifth of $500\ \text{MW}$ is $100\ \text{MW}$. The other, about $400\ \text{MW}$, leaves with the neutrons and heats the blanket. $Q = 10$ is far above JET's $0.67$, which is why ITER is so much larger.

## Common misconception

"$Q = 10$ means that ITER gives ten times more electricity than it uses." $Q$ compares two powers *in the plasma*: the fusion power and the heating that reaches the plasma. ITER produces no electricity at all, and the whole plant draws far more from the grid than the $50\ \text{MW}$ that reaches the plasma.

A second mistake is "the plasma is $150$ million degrees, so the machine must be extremely hot everywhere". The plasma is hundreds of thousands of times less dense than air, and the magnetic field holds it away from the walls. A few metres away, the magnets are at about $4\ \text{K}$.

## Summary

- ITER's superconducting magnets (toroidal field coils, poloidal field coils, central solenoid) hold and shape the plasma; the vacuum vessel, the blanket and the divertor surround it; beams and waves heat it.
- Fusion gain: $Q = P_\text{fusion} / P_\text{heating}$. $Q = 1$ is scientific breakeven; JET reached $0.67$ in 1997; ITER aims at $Q = 10$, $500\ \text{MW}$ from $50\ \text{MW}$.
- At $Q = 10$ the helium nuclei carry about $100\ \text{MW}$ and heat the plasma more than the external heating: a burning plasma.
- $Q$ is a plasma gain, not electricity. ITER produces no electricity, and a power plant needs much more than a high $Q$.
- Tritium is recycled in a closed loop and must later be bred from lithium; neutrons activate the structure, so ITER is a licensed nuclear installation.
