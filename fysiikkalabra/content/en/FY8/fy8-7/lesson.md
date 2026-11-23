# Lasers and quantum structures

> **Why** does the light of a laser pointer cross a dark classroom as a narrow beam and show on the wall as a small dot, while the light of a torch spreads into a large, dim patch?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: in a dim classroom, a laser pointer and a torch on a desk point at the same white screen. A thin red beam leaves the laser pointer and hits the screen as a small bright dot. The light of the torch spreads into a wide cone and lights a large, dim, yellowish area of the screen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Atom and photon: three events
In the chapter *Energy levels of the hydrogen atom and the Bohr model*, an atom absorbs a photon whose energy is the difference of two levels, or emits one when it drops to a lower level. An excited atom usually emits its photon by itself, at a random moment and in a random direction. This is **spontaneous emission**. The light of a lamp and of an LED is produced this way, so the photons of different atoms leave in different directions and out of step.

In 1917 Albert Einstein concluded that there is also a third event. When a photon whose energy is exactly the difference of the levels $E_2 - E_1$ hits an excited atom, it can make the atom drop to the lower level at once. This is **stimulated emission**. The incoming photon is not absorbed; a second photon is created beside it with the same energy, that is the same wavelength, the same direction of travel and the same phase. One photon becomes two identical ones, two become four, and so on. The laser is based on this amplification of light: the word comes from the English *light amplification by stimulated emission of radiation*.

<svg data-fig="processes" viewBox="0 0 600 380" role="img" aria-label="Three events side by side, schematic figure, not to scale. Each has two energy levels of an atom, the lower E1 and the upper E2, and the blue dot is an electron; the ring shows where it was before the event. On the left absorption: a photon whose energy hf is the difference of the levels enters the atom and lifts the electron to the level E2, and the photon disappears. In the middle spontaneous emission: the electron drops by itself from the level E2 to the level E1, and a photon leaves in a random direction, here obliquely upwards. On the right stimulated emission: an incoming photon makes the electron of an excited atom drop, and two identical photons leave the atom in the same direction and in step." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-processes.webp" x="0" y="0" width="600" height="390" preserveAspectRatio="none"/>
  <foreignObject x="7" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="7" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <foreignObject x="71.5" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{absorption}$</div></foreignObject>
  <foreignObject x="247.5" y="287.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{spontaneous}$</div></foreignObject>
  <foreignObject x="266" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emission}$</div></foreignObject>
  <foreignObject x="435.5" y="287.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{stimulated}$</div></foreignObject>
  <foreignObject x="448" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emission}$</div></foreignObject>
  <foreignObject x="77.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="353.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="431.5" y="111.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="535.5" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
</svg>

```pysahdy
A light pulse contains $1000$ photons of wavelength $650\,\text{nm}$. It passes through a medium with plenty of excited atoms, and every photon causes one stimulated emission. How many photons come out, and how much energy has the medium given to the light in total? Use $hc = 1240\,\text{eV}\,\text{nm}$.
---
For every incoming photon one new photon is produced, so $2000$ photons come out. There are $1000$ new photons, each with energy $hf = \tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{650\,\text{nm}} = 1.91\,\text{eV}$. The medium gives the light energy $1000 \cdot 1.91\,\text{eV} \approx 1.9\,\text{keV}$.
```

### Population inversion
A photon that makes an excited atom emit can be absorbed when it hits an atom in the ground state. Which happens more often depends on which level has more atoms. Normally almost all atoms are in the ground state, so a photon is much more likely to be absorbed than multiplied, and light becomes weaker in matter. Light is amplified only if the upper level has more atoms than the lower one, $N_2 > N_1$. This state is called **population inversion**. Heating does not produce it: even in warm matter the lower level always has more atoms than the upper one.

Inversion is made by **pumping**, that is by bringing energy to the atoms with light, an electric discharge or an electric current. In a simple model with two separate energy levels, inversion cannot be achieved by pumping with the same resonant light, because the photons of the pump light cause stimulated emission in atoms of the upper level just as likely as they excite atoms of the ground state: at most half of the atoms can be brought to the upper level. That is why many atomic and ion lasers use a structure of three or four energy levels. In semiconductor lasers, on the other hand, the amplification of light is based on the energy bands of the semiconductor and on an inversion produced by an electric current. In ruby, the green light of the pump lamp lifts atoms to a short-lived level $E_3$, from which they move quickly and without light to the level $E_2$. The level $E_2$ is long-lived: an atom stays in it for a few milliseconds on average, hundreds of thousands of times longer than in an ordinary excited state ($10^{-8}\,\text{s}$). So more atoms have time to collect on the level $E_2$ than are left in the ground state.

<svg data-fig="inversion" viewBox="0 0 600 360" role="img" aria-label="The energy levels of a three-level laser medium, such as ruby, schematic figure, not to scale. At the bottom is the ground state E1, at the top the short-lived level E3 and between them the long-lived level E2. Green arrow: pumping lifts atoms from the level E1 to the level E3. Grey dashed arrow: the atoms move from the level E3 quickly and without light to the level E2. Red arrow: the laser transition from the level E2 to the level E1, wavelength 694 nm. The blue dots are atoms: on the level E2 there are seven and on the level E1 four, so the upper level has more atoms than the lower. This is called population inversion." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-inversion.webp" x="2.5" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="77" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_3$</div></foreignObject>
  <foreignObject x="77" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="77" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <foreignObject x="330" y="90.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{fast, no light}$</div></foreignObject>
  <foreignObject x="330" y="190.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{laser}\ 694\,\text{nm}$</div></foreignObject>
  <foreignObject x="330" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{pumping}$</div></foreignObject>
  <foreignObject x="181" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_2 > N_1$</div></foreignObject>
</svg>

### Mirrors make light into a beam
The laser medium is between two mirrors. One mirror reflects all the light, the other for example $99\,\%$, and lets the rest through. A photon travelling along the axis between the mirrors passes through the medium hundreds of times and creates stimulated copies of itself on the way. Photons leaving sideways exit the medium and do not have time to multiply. So only light along the axis is amplified, and a beam comes out through the partly transmitting mirror. A laser starts to work only when the pumping is so strong that the amplification makes up for the light lost through the mirror and elsewhere. This limit of the pumping is called the **threshold**.

Laser light is nearly monochromatic because the photons are produced in the same transition. It is directional because only light along the axis is amplified, and the beam spreads only a little. It is also coherent: the waves are in step, because each stimulated photon copies the phase of the incoming photon. The light of a torch contains many wavelengths, and it leaves in different directions and out of step. A laser diode also has an amplifying medium and mirrors: an electric current produces the inversion in a semiconductor, and the cleaved ends of the crystal act as mirrors. Its energy levels, however, are energy bands and not the levels of a single atom.

<svg data-fig="cavity" viewBox="0 0 600 300" role="img" aria-label="The structure of a laser, schematic figure, not to scale. In the middle is a horizontal rod of active medium. At its left end is a mirror that reflects all the light, and at its right end a mirror that reflects 99 percent and lets 1 percent through. Under the rod is a pump lamp whose light lifts atoms to the excited state. Inside the rod red photons travel along the axis back and forth between the mirrors and multiply. Two photons leave obliquely sideways and exit the rod. A narrow red laser beam comes out through the right mirror." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-cavity.webp" x="30.7" y="23.6" width="566" height="293.6" preserveAspectRatio="none"/>
  <foreignObject x="41.5" y="49.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mirror}\ 100\,\%$</div></foreignObject>
  <foreignObject x="415.5" y="49.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mirror}\ 99\,\%$</div></foreignObject>
  <foreignObject x="221" y="73.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{active medium}$</div></foreignObject>
  <foreignObject x="530" y="171.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\text{beam}$</div></foreignObject>
  <foreignObject x="252.5" y="255.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{pumping}$</div></foreignObject>
</svg>

### Quantum structures: size determines the energy levels
The **energy gap** of a semiconductor is the smallest energy that its electron can get from light or give up as light, and it determines the colour of an LED (chapter *Light from an LED and measuring the Planck constant*). In a large crystal the energy gap depends only on the material. In the chapter *The wave-mechanical model of the atom and orbitals*, the states of an electron were compared with the standing waves of a string: the allowed vibrations of a shorter string are higher and farther apart. The same happens when electrons are confined in a structure only a few nanometres in size. The allowed energies move apart, and the energy gap grows as the structure gets smaller. Such semiconductor structures are called **quantum structures**. A thin layer is a quantum well, and a nanocrystal confined in every direction is a **quantum dot**.

So the colour of a semiconductor quantum dot can be chosen by its size, even though the material is the same. A quantum dot made of cadmium selenide with a diameter of $2\,\text{nm}$ emits cyan light, and a dot with a diameter of $6\,\text{nm}$ emits red light. The energy gap of a large cadmium selenide crystal is $1.74\,\text{eV}$, which corresponds to dark red light at the edge of the visible range, about $713\,\text{nm}$. Making the dot smaller thus moves the light towards shorter wavelengths. In this chapter this qualitative connection is enough. Calculating the energy levels exactly from the size of the dot requires quantum mechanical modelling, and tasks in which the connection between size and wavelength is modelled by calculation are enrichment material. The Nobel Prize in Chemistry 2023 was awarded for the discovery and production of quantum dots.

<svg data-fig="qdots" viewBox="0 0 600 370" role="img" aria-label="Five quantum dots one under another, their diameters to scale with each other, each drawn in the colour of the light it emits. Diameter 2.0 nm: wavelength 480 nm, photon energy 2.58 eV, cyan. 3.0 nm: 530 nm, 2.34 eV, green. 4.0 nm: 570 nm, 2.18 eV, yellow-green. 5.0 nm: 600 nm, 2.07 eV, orange. 6.0 nm: 620 nm, 2.00 eV, red. The smaller the dot, the shorter the wavelength and the greater the photon energy." style="max-width:100%;font-size:24px">
  <circle cx="78" cy="46" r="11" fill="#1098ad" stroke="#1f2933" stroke-width="2"/>
  <circle cx="75" cy="43" r="2.2" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 2.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1098ad">$\lambda = 480\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="31.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.58\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="114" r="16.5" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="73" cy="109" r="3.3" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 3.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\lambda = 530\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="99.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.34\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="182" r="22" fill="#a8a21f" stroke="#1f2933" stroke-width="2"/>
  <circle cx="71.5" cy="175.5" r="4.4" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 4.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda = 570\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.18\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="250" r="27.5" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <circle cx="70" cy="242" r="5.5" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 5.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\lambda = 600\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="235.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.07\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="318" r="33" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="68.5" cy="308.5" r="6.6" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 6.0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\lambda = 620\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2.00\,\text{eV}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/helium-neon-laser.webp" alt="A black box-shaped device labelled He-Ne LASER sits in a mount on a table; red light shines from its end, with a holder in front of it."><figcaption>A helium–neon laser in an optics set-up. An electric discharge pumps the gas in the tube, and the mirrors at the ends of the tube amplify the light into a narrow red beam with a wavelength of $633\,\text{nm}$.</figcaption></figure>

```pysahdy
A quantum dot made of cadmium selenide emits blue light of wavelength $450\,\text{nm}$. Use $hc = 1240\,\text{eV}\,\text{nm}$. Calculate the photon energy and decide whether the dot has a larger or smaller diameter than the $2.0\,\text{nm}$ dot. By how much does the dot's energy gap exceed the $1.74\,\text{eV}$ gap of a large crystal?
---
The photon energy is $\tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{450\,\text{nm}} \approx 2.76\,\text{eV}$, and the energy gap is approximately this large. It is larger than the gap of the $2.0\,\text{nm}$ dot ($480\,\text{nm}$ corresponds to $2.58\,\text{eV}$), so the dot is smaller than $2.0\,\text{nm}$. The excess is $2.76\,\text{eV} - 1.74\,\text{eV} \approx 1.0\,\text{eV}$.
```

### Applications of quantum structures
In a quantum dot display, blue backlight hits quantum dots, which absorb it and emit pure green or red light in the same way as in the fluorescence of the chapter *Spectra reveal the energy levels of atoms*. Most laser diodes are quantum well lasers, in which the thickness of the well selects the wavelength. Quantum dot layers are being studied for solar cells, and by the size of the dots they can be tuned to absorb the wanted part of the spectrum of the Sun.

The basic unit of a quantum computer is the **qubit**: a quantum system that has two states and can also be in a combination of them, a superposition. Qubits are made, for example, of electrons confined in the quantum dots of a semiconductor and of superconducting circuits. Such a circuit behaves like an artificial atom with its own quantised energy levels. In Finland, superconducting quantum computers are being built by VTT and IQM. The states of a qubit are sensitive, so the circuits are cooled close to absolute zero and shielded from disturbances of the environment.

<figure class="unit-photo"><img src="pics/fy8/rgb-laser-pointer.webp" alt="Three horizontal laser beams in the dark: red at the top, green in the middle and blue at the bottom; the beams come from devices on the right."><figcaption>Red, green and blue laser beams. Particles in the air scatter some of the light towards the camera, so the beams are visible. A photon of blue light carries the most energy and one of red light the least.</figcaption></figure>

## Formula: Laser photons
All the photons of a laser are produced in the same transition, so the energy and wavelength of each photon are
```latex
\begin{aligned}
hf &= E_2 - E_1 \\
\lambda &= \frac{hc}{E_2 - E_1}
\end{aligned}
```
where $E_2$ is the energy of the upper and $E_1$ of the lower laser level, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is the Planck constant, $f$ the frequency of the light, $c = 2.998 \cdot 10^{8}\,\text{m/s}$ the speed of light and $\lambda$ the wavelength.

Because the photons are identical, the power of a laser is the number of photons leaving per second multiplied by the energy of one photon:
```latex
P = \frac{N}{t} \cdot hf
```
where $P$ is the power of the laser and $N$ the number of photons leaving in the time $t$. The number of photons per second is thus $\tfrac{N}{t} = \tfrac{P}{hf}$. Energies are often calculated in electronvolts and converted to joules by substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.

With the same power, a laser of a longer wavelength emits more photons, because one photon carries less energy. In the graph, a red laser pointer of $1.0\,\text{mW}$ emits about $3.3 \cdot 10^{15}$ photons per second and a violet one of equal power about $2.0 \cdot 10^{15}$.

<svg data-fig="rate-graph" viewBox="0 0 600 340" role="img" aria-label="Graph to scale: the number of photons per second emitted by a laser of power 1.0 milliwatt as a function of the wavelength. On the horizontal axis the wavelength from zero to 700 nanometres, on the vertical axis the number of photons per second in units of 10 to the power 15 photons per second, from zero to 3.5. The graph is a straight line through the origin. Three laser pointers are marked on it: violet 405 nm, 2.04; green 532 nm, 2.68; and red 650 nm, 3.27. With the same power, a laser of a longer wavelength emits more photons, because one photon carries less energy." style="max-width:100%;font-size:24px">
  <line x1="151.5" y1="290" x2="151.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207.5" y1="290" x2="207.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="290" x2="263" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="290" x2="319" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374.5" y1="290" x2="374.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430.5" y1="290" x2="430.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="486" y1="290" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="259" x2="486" y2="259" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228.5" x2="486" y2="228.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="486" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="166.5" x2="486" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="135.5" x2="486" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="105" x2="486" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="74" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="500" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M512,290 L499,296 L499,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,48 L102,61 L90,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="151.5" y1="290" x2="151.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="129" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="207.5" y1="290" x2="207.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="185" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="263" y1="290" x2="263" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="319" y1="290" x2="319" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="296.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="374.5" y1="290" x2="374.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="430.5" y1="290" x2="430.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="486" y1="290" x2="486" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="89" y1="259" x2="96" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="244.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.5$</div></foreignObject>
  <line x1="89" y1="228.5" x2="96" y2="228.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="214" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="183" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1.5$</div></foreignObject>
  <line x1="89" y1="166.5" x2="96" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="152" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="135.5" x2="96" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="121" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2.5$</div></foreignObject>
  <line x1="89" y1="105" x2="96" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="74" x2="96" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3.5$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="518" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="86" y="17.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N/t\ (10^{15}\,\text{1/s})$</div></foreignObject>
  <polyline points="96,290 486,72.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="321.5" cy="164" r="7" fill="#7048e8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="392.5" cy="124.5" r="7" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="458" cy="88" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="224.5" y="123.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$405\,\text{nm}$</div></foreignObject>
  <foreignObject x="295.5" y="84" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$532\,\text{nm}$</div></foreignObject>
  <foreignObject x="361" y="47.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$650\,\text{nm}$</div></foreignObject>
  <foreignObject x="362" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 1.0\,\text{mW}$</div></foreignObject>
</svg>

```pysahdy
The power of a laser is kept the same, but the photon energy doubles. What happens to the number of photons emitted per second?
---
Since $\tfrac{N}{t} = \tfrac{P}{hf}$, the number of photons per second is halved.
```

## Worked example
The energy difference of the levels of the laser transition of a helium–neon laser is $1.96\,\text{eV}$, and the power of the laser is $1.0\,\text{mW}$. How many photons does the laser emit per second?

<!-- vaihe -->

**Given and asked.** The energy difference of the levels is $E_2 - E_1 = 1.96\,\text{eV}$ and the power is $P = 1.0\,\text{mW}$. We are asked for the number of photons leaving per second, $\tfrac{N}{t}$.

<!-- vaihe -->

**Principle.** All the photons of a laser are produced in the same transition, so the energy of each is $hf = E_2 - E_1$. The power is the number of photons per second multiplied by the energy of one photon.

<!-- vaihe -->

**Formula solved.** We substitute the difference of the levels for the energy of the photon and solve the number of photons per second:
```latex
\begin{aligned}
&P = \frac{N}{t} \cdot (E_2 - E_1) \\
&\frac{N}{t} = \frac{P}{E_2 - E_1}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** The power is $P = 1.0\,\text{mW} = 1.0 \cdot 10^{-3}\,\text{W}$, and the energy difference is converted to joules by substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $E_2 - E_1 = 1.96 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.1399 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&\frac{N}{t} = \frac{P}{E_2 - E_1} \\
&= \frac{1.0 \cdot 10^{-3}\,\text{W}}{3.1399 \cdot 10^{-19}\,\text{J}} \\
&= 3.1848 \cdot 10^{15}\,\tfrac{1}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Result.** The laser emits about $3.2 \cdot 10^{15}$ photons per second. The result is given with two significant figures, because the power $1.0\,\text{mW}$ is given with two.

<!-- vaihe -->

**Reasonableness.** The unit is correct, because $\tfrac{\text{W}}{\text{J}} = \tfrac{\text{J/s}}{\text{J}} = \tfrac{1}{\text{s}}$. The energy difference corresponds to the wavelength $\lambda = \tfrac{hc}{E_2 - E_1} \approx 633\,\text{nm}$, the familiar red light of a helium–neon laser. According to the graph, a laser of $1.0\,\text{mW}$ emits about $3.3 \cdot 10^{15}$ photons per second at the wavelength $650\,\text{nm}$, so a slightly smaller number at a slightly shorter wavelength is credible.

## Common misconception
Many think that laser light is dangerous because its photons would be especially energetic. But the energy of a photon depends only on the wavelength: the photon energy $1.91\,\text{eV}$ of a red laser pointer is the same as that of any light of $650\,\text{nm}$, and the photons of violet light of $405\,\text{nm}$ are more energetic, whether they come from a laser or from a lamp. The danger of a laser is that the whole power travels in a narrow beam, which the lens of the eye focuses on the retina into a very small spot. That is why only low-power lasers are used at school, and nobody looks into the beam or its mirror reflection or points it at people.

Another mistake is to think that in stimulated emission the atom absorbs a photon and emits two. The incoming photon is not absorbed but continues on its way. The energy of the new photon comes from the excited atom, which drops from the level $E_2$ to the level $E_1$, so energy is conserved.

## Tunnelling {Tunneloituminen}
According to classical physics, a ball whose energy is not enough to get over a hill rolls back. In quantum physics, the probability of detecting an electron does not end at the edge of a barrier but decreases quickly inside the barrier. If the barrier is very thin, the probability behind the barrier remains small but not zero: the electron can be found behind the barrier even though its energy is smaller than the energy needed to cross the barrier. This is called **tunnelling**. The probability decreases extremely steeply as the barrier gets thicker and higher, so tunnelling is significant only for barriers of the order of nanometres.

<svg data-fig="tunnel" viewBox="0 0 600 320" role="img" aria-label="Schematic figure of tunnelling, not to scale. An electron arrives from the left; its energy E, the horizontal dashed line, is smaller than the height of the grey barrier in the middle. The blue area shows the probability of detecting the electron: on the left of the barrier it is large, inside the barrier it decreases quickly, and on the right of the barrier it is small but not zero. So the electron can be found behind the barrier even though its energy is not enough to get over the barrier." style="max-width:100%;font-size:24px">
  <rect x="270" y="90" width="60" height="170" rx="2" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="24" y1="260" x2="576" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="24" y1="180" x2="576" y2="180" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M30,260 L30,198 L30,198 L34,196 L38,194 L42,192.5 L46,192 L50,192 L54,193 L58,194.5 L62,197 L66,199 L70,201 L74,202.5 L78,203.5 L82,204 L86,203.5 L90,202 L94,200.5 L98,198.5 L102,196 L106,194 L110,193 L114,192 L118,192 L122,193 L126,194.5 L130,196.5 L134,198.5 L138,200.5 L142,202.5 L146,203.5 L150,204 L154,203.5 L158,202.5 L162,200.5 L166,198.5 L170,196.5 L174,194.5 L178,193 L182,192 L186,192 L190,193 L194,194 L198,196 L202,198.5 L206,200.5 L210,202 L214,203.5 L218,204 L222,203.5 L226,202.5 L230,201 L234,199 L238,197 L242,194.5 L246,193 L250,192 L254,192 L258,192.5 L262,194 L266,196 L270,198 L270,198 L271.5,200.5 L273,203.5 L274.5,206 L276,208 L277.5,210.5 L279,212.5 L280.5,215 L282,216.5 L283.5,218.5 L285,220.5 L286.5,222 L288,224 L289.5,225.5 L291,227 L292.5,228.5 L294,230 L295.5,231 L297,232.5 L298.5,233.5 L300,235 L301.5,236 L303,237 L304.5,238 L306,239 L307.5,240 L309,241 L310.5,241.5 L312,242.5 L313.5,243 L315,244 L316.5,244.5 L318,245.5 L319.5,246 L321,246.5 L322.5,247 L324,247.5 L325.5,248.5 L327,249 L328.5,249.5 L330,250 L570,250 L570,260 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="252.5" y="51.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{barrier}$</div></foreignObject>
  <foreignObject x="36" y="143.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$E$</div></foreignObject>
  <foreignObject x="46" y="275.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{incoming electron}$</div></foreignObject>
  <foreignObject x="352" y="275.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{behind the barrier}$</div></foreignObject>
  <line x1="380" y1="210" x2="439" y2="210" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M450,210 L438,215.5 L438,204.5 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

In a scanning tunnelling microscope, a sharp metal tip is brought about a nanometre from a surface. The current of electrons tunnelling between the tip and the surface changes strongly with the distance, so the tip can be used to image single atoms. A bit is written into a memory cell of flash memory by moving electrons through a thin insulating layer by tunnelling. In superconducting qubits the current passes through a thin insulating layer by tunnelling; the Nobel Prize in Physics 2025 was awarded for the discovery of quantum tunnelling and the quantisation of energy in such circuits. Alpha decay, discussed in the chapter *The atomic nucleus and radioactive decay*, is also tunnelling.

## Summary
- An excited atom can emit a photon by itself (spontaneous emission) or under the influence of an incoming photon (stimulated emission). Stimulated emission produces a photon with the energy, direction and phase of the incoming photon.
- Light is amplified only when the upper laser level has more atoms than the lower one, $N_2 > N_1$ (population inversion). In atomic and ion lasers it is obtained by pumping a medium that has three or four levels and a long-lived upper laser level. In a semiconductor laser the inversion is produced in the energy bands by an electric current.
- Between the mirrors, light along the axis passes through the medium many times and is amplified; the laser works when the pumping exceeds the threshold. Laser light is nearly monochromatic, directional and coherent.
- The energy of the photons of a laser is $hf = E_2 - E_1$, and the power is $P = \tfrac{N}{t} \cdot hf$.
- In semiconductor quantum structures the electrons are confined in a space of nanometre size, and the energy gap grows as the structure gets smaller: a smaller quantum dot emits a shorter wavelength. Applications are quantum dot displays, quantum well lasers, research on solar cells and the qubits of quantum computers.
