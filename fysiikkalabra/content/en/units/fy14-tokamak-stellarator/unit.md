# Tokamak or stellarator?

> **Why** do the two leading designs for a magnetic fusion reactor look so different, although both hold the plasma in a ring?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: two ring-shaped fusion machines side by side in a dark hall, seen from above at an angle. Left: a smooth pink plasma ring surrounded by evenly spaced, flat orange coils, with a copper column in the middle. Right: a pink plasma ring that waves up and down and in and out as it goes round, surrounded by orange coils that are tilted and bent to follow it. No words." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-tokamak-stellarator-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Twisting the field lines {Twist}

Coils around a ring make a **toroidal** magnetic field, which runs the long way round the ring. On its own it cannot hold a plasma. The coils are closer together on the inside of the ring, so the field is stronger there, and the field lines are curved. As you saw in the chapter *Charged particles and magnetic confinement*, this makes ions and electrons drift apart, an electric field builds up, and the whole plasma drifts outward.

The cure is a **poloidal** field, which runs the short way round the plasma's cross-section. Together the two make **helical** field lines that wind around the ring like the stripes on a candy cane. A particle on such a line visits the inside and the outside, the top and the bottom, so the separated charges can flow back along the lines and the outward drift does not build up.

```pysahdy
Why does adding a poloidal field stop the outward drift of the plasma?
---
The field lines become helical, so a particle visits both the inside and the outside of the ring. The separated charges can then flow back along the lines and no electric field builds up to push the plasma outward.
```

## Formula: The toroidal field

Ampère's law gives the field of $N$ turns carrying a current $I$, at a distance $R$ from the central axis of the ring:
```latex
B = \frac{\mu_0 N I}{2 \pi R}
```
Here $\mu_0 = 4\pi \cdot 10^{-7}\ \text{T} \cdot \text{m/A}$. The field falls as $1/R$: it is stronger on the inner side of the plasma than on the outer side.

<svg data-fig="toroidal" viewBox="0 0 600 420" role="img" aria-label="Top view of a tokamak drawn to scale with ITER&#x27;s dimensions. Eighteen toroidal field coils, orange, stand around the ring like the spokes of a wheel; they are close together near the centre and far apart on the outside. The plasma, pink, is a ring between 4.2 m and 8.2 m from the central axis. Green field lines go round the ring. Labels give the field: 7.8 T at the inner edge of the plasma, 5.3 T at its centre line, R = 6.2 m, and 4.0 T at the outer edge." style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-tokamak-stellarator-toroidal.webp" x="0" y="0" width="600" height="426.2" preserveAspectRatio="none"/>
  <foreignObject x="404" y="54" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$R = 4.2\ \text{m}$</div></foreignObject>
  <foreignObject x="404" y="90" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px;color:#2b8a3e">$B = 7.8\ \text{T}$</div></foreignObject>
  <foreignObject x="404" y="180" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$R = 6.2\ \text{m}$</div></foreignObject>
  <foreignObject x="404" y="216" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px;color:#2b8a3e">$B = 5.3\ \text{T}$</div></foreignObject>
  <foreignObject x="404" y="306" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px">$R = 8.2\ \text{m}$</div></foreignObject>
  <foreignObject x="404" y="342" width="96" height="32" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:27px;color:#2b8a3e">$B = 4.0\ \text{T}$</div></foreignObject>
</svg>

## The tokamak: a current in the plasma {Tokamak}

The **tokamak** was proposed by Igor Tamm and Andrei Sakharov in the Soviet Union in the early 1950s. A large **plasma current** $I_\text{p}$ flows round the ring *in the plasma itself*, and its magnetic field is the poloidal field. In ITER it will be $15\ \text{MA}$.

The current is driven like the current in a transformer: the **central solenoid** in the middle of the ring is the primary coil, and the plasma is a one-turn secondary coil. A *changing* current in the solenoid induces the plasma current, which also heats the plasma. The coils are flat and fairly simple, and tokamaks have reached the best plasma conditions so far. The risk is a **disruption**: the plasma suddenly loses its confinement, and its large current dies within milliseconds, putting large forces and heat loads on the vessel.

## The stellarator: twisted coils {Stellarator}

The **stellarator** was invented by Lyman Spitzer at Princeton in 1951. Its **coils**, bent into complicated three-dimensional shapes, make the whole twist. No large plasma current is needed, so there are no disruptions of the tokamak kind.

Early stellarators confined plasma worse than tokamaks. Modern ones are **optimised**: computers search for coil shapes that hold the plasma well. Wendelstein 7-X in Greifswald, Germany, has 50 non-planar and 20 planar superconducting coils. It made its first plasma in December 2015 and held a plasma for about eight minutes in February 2023. The price is the coils: they are very hard to design, build and place accurately.

<figure class="unit-photo"><img src="units/fy14/pics/wendelstein-7x-2.jpg" alt="Colour photograph of a large twisted superconducting magnet coil on display." width="1490" height="1600" loading="lazy"><figcaption>One of the 50 twisted (non-planar) superconducting coils of Wendelstein 7-X. Their shape creates the magnetic cage without a plasma current. <span class="photo-credit">Photo: Siarhei Besarab, CC BY-SA 4.0, via Wikimedia Commons</span></figcaption></figure>

## Pulsed or steady? {Operation}

A transformer works only while the current in its primary coil keeps *changing*, and that cannot go on for ever. So **inductive** current drive alone gives **pulses**: ITER's solenoid can drive $15\ \text{MA}$ for about $300$ to $500\ \text{s}$.

```pysahdy
Why does inductive current drive alone give only pulses?
---
A transformer induces a current only while the current in its primary coil, the central solenoid, keeps changing. The solenoid current cannot change for ever, so the pulse ends.
```

But a tokamak current can also be driven **without induction**:

- **neutral beams**: fast neutral atoms enter the plasma, become fast ions and carry current round the ring;
- **radio-frequency waves**, such as lower hybrid waves, push electrons along the field;
- the **bootstrap current**: the plasma's own pressure gradient drives part of the current.

On 12 February 2025 the French tokamak WEST held a plasma for $1337\ \text{s}$, about 22 minutes, with its current driven by lower hybrid waves. A stellarator needs no driven current, so it can run steadily by design.

<figure class="unit-photo"><img src="units/fy14/pics/west.jpg" alt="Colour photograph of the ring-shaped inside of the WEST tokamak, lined with metal tiles." width="1600" height="1199" loading="lazy"><figcaption>The vacuum chamber of WEST at CEA Cadarache, France, in 2018. WEST tests the tungsten wall components that ITER will use. <span class="photo-credit">Photo: Christophe Roux / IRFM, CC BY 4.0, via Wikimedia Commons</span></figcaption></figure>

## Key idea

Both designs hold the plasma in **twisted field lines**. The tokamak twists them with a **plasma current**: simpler coils and the best results so far, but disruptions, and steady operation needs non-inductive current drive. The stellarator twists them with **three-dimensional coils**: steady operation without disruptions, but coils that are very hard to make.

## Worked example

ITER has 18 toroidal field coils. Each has 134 turns, and the current in them is $68\ \text{kA}$. Calculate the toroidal field at the centre line of the plasma, $R = 6.2\ \text{m}$ from the central axis.

<!-- vaihe -->

**Given:** $N = 18 \cdot 134 = 2412$ turns, $I = 68\ \text{kA}$, $R = 6.2\ \text{m}$, $\mu_0 = 4\pi \cdot 10^{-7}\ \text{T} \cdot \text{m/A}$. Asked: the field $B$.

<!-- vaihe -->

**Principle:** The toroidal field coils together act like one ring-shaped coil of $N$ turns. Ampère's law around a circle of radius $R$ inside the coils gives the field there. The field of the other coils and of the plasma current is much weaker in this direction, so we ignore it.

<!-- vaihe -->

**Formula:**
```latex
B = \frac{\mu_0 N I}{2 \pi R}
```

<!-- vaihe -->

**Unit conversions:** $I = 68\ \text{kA} = 68 \cdot 10^{3}\ \text{A} = 6.8 \cdot 10^{4}\ \text{A}$.

<!-- vaihe -->

**Substitution:**
```latex
\begin{aligned}
B &= \frac{4\pi \cdot 10^{-7}\ \text{T} \cdot \text{m/A}}{2\pi \cdot 6.2\ \text{m}} \\
&\quad \cdot 2412 \cdot 6.8 \cdot 10^{4}\ \text{A} \\
&= 5.29\ \text{T}
\end{aligned}
```

<!-- vaihe -->

**Answer:** $B \approx 5.3\ \text{T}$, two significant figures as in the radius and the current.

<!-- vaihe -->

**Reasonableness:** ITER gives its toroidal field as $5.3\ \text{T}$, about $100\ 000$ times the Earth's magnetic field. The peak field in the coils themselves, $11.8\ \text{T}$, is higher, because the inner legs of the coils are close to the axis, where $R$ is small.

## Common misconception

"Every tokamak can only run in short pulses, because its current comes from a transformer." Inductive drive alone is limited in time, but neutral beams, radio-frequency waves and the bootstrap current can drive the current without induction. WEST held a plasma for over 22 minutes in this way. A second mistake: "A stellarator has no magnetic field inside the plasma made by currents." It has no *large plasma current*, but its twisted coils carry very large currents.

## Summary

- A purely toroidal field cannot hold a plasma: in the curved field that is stronger on the inside, ions and electrons drift apart and the plasma drifts outward. The field lines must be **twisted** (toroidal + poloidal = helical).
- The toroidal field is $B = \mu_0 N I / (2\pi R)$, so it falls as $1/R$ across the plasma.
- **Tokamak:** the poloidal field comes from a large plasma current, driven inductively by the central solenoid (pulses) or non-inductively by beams, waves and the bootstrap current (long pulses, perhaps steady). Risk: disruptions.
- **Stellarator:** the twist comes from three-dimensional coils. Steady by design and without disruptions, but the coils are difficult. In 2025 Wendelstein 7-X set a record triple product for long plasmas.
