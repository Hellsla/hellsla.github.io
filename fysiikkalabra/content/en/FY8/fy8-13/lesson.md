# Radiation dose and radiation safety in Finland

> **Why** do nuclear power plants give a Finn only a negligible part of their radiation dose, and where does the rest come from?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a winter landscape in Finland. A red detached house is drawn in cross-section: there is snow on the roof, smoke rises from the chimney and the house has a cellar below it. Underground is a layer of sandy soil and deeper down grey granite bedrock. An aeroplane flies in the sky, and far away behind the forest the reactor building of a nuclear power plant can be seen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### Dose measures the energy left in tissue
Ionising radiation damages cells because it gives up its energy by knocking electrons out of atoms and molecules (chapter *Ionising radiation and the body*). The starting point for assessing the harm of radiation is therefore how much energy is left in the tissue. The **absorbed dose** $D$ is the radiation energy absorbed by tissue or another material divided by its mass. Its unit is the gray: $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$. Dividing by mass is necessary because the same energy concentrated in a small amount of tissue damages every cell more than the same energy spread over a large amount.

The energies are small on the scale of heat. A dose of $1\,\text{Gy}$ would warm water by only about $0.0002\,\text{K}$, yet receiving the same dose over the whole body at once already causes radiation sickness. The harm is therefore not caused by warming, but by the energy arriving in large packets that break individual molecules, such as DNA.

```pysahdy
Two pieces of tissue absorb the same radiation energy, but one has twice the mass. Which one has the greater absorbed dose?
---
The lighter one, twice as great. The dose is energy divided by mass, so every kilogram of the lighter piece receives twice the energy.
```

### The same energy, different harm: weighted doses
An alpha particle leaves a dense track of ionisation over a short distance, whereas a gamma photon ionises sparsely over a long distance. The same absorbed dose from alpha radiation therefore damages the DNA of cells more than from gamma radiation. Tissues also differ: red bone marrow and the lungs are more sensitive to radiation-induced cancer than the skin. In radiation protection these differences are taken into account with weighting factors, and the unit of a weighted dose is the sievert, $\text{Sv}$. The **effective dose** of the whole body is used to estimate the long-term cancer risk caused by small doses for an average person, not anyone's individual risk, and with it very different exposures, such as radon, an X-ray examination and a flight, can be compared.

<figure class="unit-photo"><img src="pics/fy8/radiacode-dosimeter.webp" alt="A black pocket-sized radiation meter on a green surface; the display shows a reading with the unit CPS."><figcaption>A pocket radiation meter whose display shows a count rate of $4.45$ counts per second. Background radiation gives the meter counts all the time, even when there is no radioactive source nearby.</figcaption></figure>

### Where a Finn's radiation dose comes from
According to the Radiation and Nuclear Safety Authority (STUK), a Finn receives an effective dose of about $5.9\,\text{mSv}$ per year on average. Most of it comes from nature: about $5.1\,\text{mSv}$, or about $85\,\%$. The combined share of nuclear power plants, the Chernobyl fallout and nuclear weapons tests is less than $0.1\,\text{mSv}$. The table and the bar chart below it show the same numbers.

| Source | Dose per year |
| --- | --- |
| indoor radon | about $4\,\text{mSv}$ |
| other natural radiation | about $1.1\,\text{mSv}$ |
| health care | about $0.8\,\text{mSv}$ |
| nuclear power, fallout and others | $< 0.1\,\text{mSv}$ |
| total | about $5.9\,\text{mSv}$ |

Source: STUK-A263 (2020), an estimate of the situation in 2018, rounded; the share of health care is $0.76\,\text{mSv}$ in the report. The share of health care comes from X-ray and isotope examinations. Other natural radiation consists of the gamma radiation of soil and building materials, radiation from space and the body's own radioactive substances, such as potassium-40. This is an average: an individual's dose depends above all on the radon concentration of their home and can be many times higher.

<svg data-fig="lahteet" viewBox="0 0 600 360" role="img" aria-label="Horizontal bar chart to scale: the average effective dose of a Finn per year by source, STUK&#x27;s estimate of the situation in 2018, about 5.9 millisieverts in total. Indoor radon about 4, other natural radiation, that is soil, buildings, space and the body&#x27;s own substances, about 1.1 in total, and health care about 0.8 millisieverts per year. The bar of radon is clearly the longest, more than three times as long as the next one." style="max-width:100%;font-size:24px">
  <line x1="325.5" y1="34" x2="325.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325.5" y1="286" x2="325.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="315.5" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="389" y1="34" x2="389" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="389" y1="286" x2="389" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="379" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="452.5" y1="34" x2="452.5" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="452.5" y1="286" x2="452.5" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="442.5" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="516" y1="34" x2="516" y2="286" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="516" y1="286" x2="516" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="506" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="232" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <rect x="262" y="56" width="254" height="36" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="105" y="59.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{indoor radon}$</div></foreignObject>
  <foreignObject x="526" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4.0$</div></foreignObject>
  <rect x="262" y="132" width="70" height="36" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="92" y="135.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{other natural}$</div></foreignObject>
  <foreignObject x="342" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1.1$</div></foreignObject>
  <rect x="262" y="208" width="51" height="36" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="117" y="211.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{health care}$</div></foreignObject>
  <foreignObject x="323" y="211.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0.8$</div></foreignObject>
  <line x1="262" y1="287" x2="562" y2="287" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M574,287 L561,293 L561,281 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="262" y1="287" x2="262" y2="32" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="219" y="325.5" width="162" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$H_\text{E}\ (\text{mSv/year})$</div></foreignObject>
</svg>

**Background radiation** is the radiation that constantly comes from natural sources in the environment: radioactive substances in the soil and bedrock, radiation from space and radon in the air. Outdoors in Finland the dose rate of external background radiation is usually $0.05$–$0.30\,\mu\text{Sv/h}$, and STUK's monitoring network measures it continuously around the country. In an aeroplane the dose rate is many times higher, about $3\,\mu\text{Sv/h}$ on a typical long-haul flight, because the higher you are, the less the atmosphere shields you from radiation from space.

### Radon: an invisible gas from the bedrock
**Radon** is a radioactive noble gas. Its most common isotope, radon-222, is formed from radium in the decay series of uranium-238 in the soil and bedrock, and its half-life is $3.82\,\text{d}$ (chapter *The decay law and half-life*). The granitic bedrock of Finland contains a lot of uranium, and the gravel of eskers lets soil air through easily. In winter warm indoor air rises and leaks out of the upper parts of a house, which creates an underpressure in the lower part of the house. It sucks radon-containing soil air in through cracks and gaps in the foundations.

Most of the radon itself is breathed out again, but its short-lived decay products, isotopes of polonium, lead and bismuth, are solids. They attach to dust particles in the air and remain on the surfaces of the airways. There polonium-218 and polonium-214 emit alpha radiation directly into the cells of the lungs. After smoking, radon is the most important cause of lung cancer: according to STUK, it causes about 300 lung cancers per year in Finland.

The radon concentration is given in becquerels per cubic metre: $1\,\tfrac{\text{Bq}}{\text{m}^3}$ means one decay per second in a cubic metre of air. According to STUK's nationwide sample surveys, the average concentration in Finnish homes is about $94\,\tfrac{\text{Bq}}{\text{m}^3}$. The reference level for dwellings is $300\,\tfrac{\text{Bq}}{\text{m}^3}$ and for new buildings $200\,\tfrac{\text{Bq}}{\text{m}^3}$ (decree of the Ministry of Social Affairs and Health 1044/2018). The concentration is measured with a radon detector can, which is left in the dwelling for two months during the heating season. The concentration can be reduced by improving ventilation, sealing gaps in the foundations and sucking radon-containing air from under the house with a radon suction pipe or a radon well.

<figure class="unit-photo"><img src="pics/fy8/dosimeter-japan.webp" alt="A device on a metal stand outdoors, with red numerical displays and Japanese text at the top and a red and a green indicator light; a stone statue and trees in the background."><figcaption>An outdoor radiation monitor in Japan. The large display shows passers-by the ambient dose rate, so that anyone can judge how long it is sensible to stay in the area.</figcaption></figure>

```pysahdy
Radon-222 has a half-life of $3.82\,\text{d}$ and a breath stays in the lungs for about $5\,\text{s}$. Estimate the order of magnitude of the fraction of radon atoms that decay during one breath, and say what this tells about the source of the lung dose.
---
$3.82\,\text{d} \approx 3.3 \cdot 10^{5}\,\text{s}$, so the fraction is of the order of $\tfrac{5\,\text{s}}{3.3 \cdot 10^{5}\,\text{s}} \approx 10^{-5}$. Almost all radon is breathed out undecayed, so the lung dose comes mainly from the solid decay products that stay in the airways.
```

### Protection: time, distance and shielding
There are three ways to protect yourself from an external radiation source. **Time:** the dose grows in direct proportion to the time spent near the source, so near a radiation source only what is necessary is done, and quickly. **Distance:** from a point source radiation spreads in all directions over an ever larger area, so the dose rate decreases rapidly as the distance grows. **Shielding:** material between the source and the person absorbs radiation. Alpha radiation is stopped by paper or the dead surface layer of the skin, beta radiation by a plastic or aluminium plate a few millimetres thick. Gamma radiation is attenuated best by dense materials, such as lead and concrete, but no layer stops it completely.

Protection from internal radiation sources, such as the decay products of radon or radioactive substances in food, works differently: the substances are prevented from entering the body. Radon is removed from indoor air, and, for example, mushrooms that accumulate a lot of caesium-137 are not eaten in large amounts.

The use of radiation is limited by dose limits. The effective dose of a person doing radiation work may be at most $20\,\text{mSv}$ per year, and the dose of the public from the use of radiation at most $1\,\text{mSv}$ per year (Radiation Act 859/2018). The limit for the public does not apply to natural radiation or to a patient's own medical examinations, whose benefit is assessed separately.

## Formula: Absorbed and effective dose

### Absorbed dose
When the mass of the tissue is $m$ and it absorbs energy $E$ from radiation, the absorbed dose is
```latex
D = \frac{E}{m}
```
where $D$ is the absorbed dose ($\text{Gy}$), $E$ the absorbed energy ($\text{J}$) and $m$ the mass of the tissue ($\text{kg}$). The absorbed dose is a physical quantity: it does not tell what kind of radiation it was.

### Equivalent dose and the radiation weighting factor
The equivalent dose of an organ or tissue $\text{T}$ takes the type of radiation into account:
```kaavat
equivalent dose :: H_\text{T} = w_\text{R} D_\text{T}
```
where $H_\text{T}$ is the equivalent dose of the tissue ($\text{Sv}$), $w_\text{R}$ the radiation weighting factor (a pure number) and $D_\text{T}$ the absorbed dose of the tissue ($\text{Gy}$). The weighting factor is a rounded value agreed on in radiation protection. It describes how much more harmful a type of radiation is than gamma radiation at the same absorbed dose, but it is not an exact measured ratio of the damage in every cell. The factor for neutrons depends on their energy.

| Type of radiation | $w_\text{R}$ |
| --- | --- |
| gamma and X-ray radiation | $1$ |
| beta radiation (electrons) | $1$ |
| alpha radiation | $20$ |
| neutrons | $2.5$–$20$ |

<svg data-fig="painotus" viewBox="0 0 600 360" role="img" aria-label="Schematic figure, not to scale: two identical pieces of tissue. Gamma radiation enters the left one: a wavy line passes through the piece, and a few ionisation points lie sparsely along it. An alpha particle hits the right one: its short thick track stops inside the piece, and the ionisations along the track are dense. In both the absorbed dose is D = 1 milligray. The weighting factor of gamma radiation is 1, so the equivalent dose is 1 millisievert; the weighting factor of alpha radiation is 20, so the equivalent dose is 20 millisieverts." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-painotus.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="63.5" y="11.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{gamma radiation}$</div></foreignObject>
  <foreignObject x="107.5" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D = 1\,\text{mGy}$</div></foreignObject>
  <foreignObject x="126" y="247.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$w_\text{R} = 1$</div></foreignObject>
  <foreignObject x="101" y="315.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$H_\text{T} = 1\,\text{mSv}$</div></foreignObject>
  <foreignObject x="353.5" y="11.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alpha radiation}$</div></foreignObject>
  <foreignObject x="397.5" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D = 1\,\text{mGy}$</div></foreignObject>
  <foreignObject x="410" y="247.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$w_\text{R} = 20$</div></foreignObject>
  <foreignObject x="385" y="315.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$H_\text{T} = 20\,\text{mSv}$</div></foreignObject>
</svg>

### Effective dose and the tissue weighting factor
When only a part of the body is irradiated, the equivalent dose of each tissue is multiplied by the tissue weighting factor $w_\text{T}$, which describes its sensitivity, and the products are added up:
```latex
H_\text{E} = w_{\text{T}1} H_{\text{T}1} + w_{\text{T}2} H_{\text{T}2} + \ldots
```
where $H_\text{E}$ is the effective dose ($\text{Sv}$) and $w_{\text{T}1}, w_{\text{T}2}, \ldots$ are the weighting factors of the irradiated tissues. The international symbol of the effective dose is $E$; in this chapter the symbol $H_\text{E}$ is used so that it is not confused with the energy $E$.

The tissue weighting factors are:

- $0.12$ each: red bone marrow, colon, lungs, stomach and breasts, and the remaining tissues together
- $0.08$: gonads
- $0.04$ each: bladder, oesophagus, liver and thyroid
- $0.01$ each: bone surface, brain, salivary glands and skin

The weighting factors are from the 2007 recommendation of the International Commission on Radiological Protection (ICRP), and they are also the basis of Finnish radiation legislation. The tissue factors add up to $1$, so when the whole body receives the same equivalent dose, the effective dose is equal to it. The effective dose is a radiation protection quantity calculated for an agreed average person and meant for small doses. It is used to compare exposures and to monitor dose limits, but it is not an exact risk estimate for an individual person, and it is not used to plan radiotherapy. The immediate effects of large single doses, such as radiation sickness, are assessed with the absorbed dose in grays.

### Dose rate and time
A radiation meter usually shows the **dose rate** $\dot{H}$, that is, the dose per unit time, for example in the unit $\mu\text{Sv/h}$. When the dose rate stays constant, the dose accumulated in time $t$ is
```latex
H = \dot{H} t
```
where $H$ is the dose ($\text{Sv}$), $\dot{H}$ the dose rate ($\tfrac{\text{Sv}}{\text{h}}$) and $t$ the time spent ($\text{h}$). Halving the time spent halves the dose.

### The inverse-square law
Radiation leaving a point source in all directions is spread at distance $r$ over the surface of a sphere with area $4\pi r^2$. When the distance doubles, the same radiation is spread over four times the area, so a quarter of the previous amount hits the window of the meter. At distances $r_1$ and $r_2$ the dose rates are related by
```latex
\dot{H}_2 = \dot{H}_1 \left(\frac{r_1}{r_2}\right)^2
```
where $\dot{H}_1$ is the dose rate at distance $r_1$ and $\dot{H}_2$ at distance $r_2$. The law holds when the source is small compared with the distance and the air attenuates the radiation only a little, as for gamma radiation over a few metres.

<svg data-fig="etaisyys" viewBox="0 0 600 384" role="img" aria-label="Schematic figure of the inverse-square law. On the left is a point source of radiation, from which four boundary rays spread to the right. At distance r the rays pass through one square; at distance 2 r the same radiation has to be spread over 2 times 2, that is four, squares of the same size, and at distance 3 r over 3 times 3, that is nine, squares. So one square receives a quarter of the radiation at distance 2 r and a ninth at distance 3 r, and the relative dose rate at these distances is 1, a quarter and a ninth." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-13-etaisyys.webp" x="1.2" y="2.5" width="597" height="388.1" preserveAspectRatio="none"/>
  <foreignObject x="162" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="162" y="329.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$1$</div></foreignObject>
  <foreignObject x="285.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2r$</div></foreignObject>
  <foreignObject x="292" y="315" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dfrac{1}{4}$</div></foreignObject>
  <foreignObject x="415.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3r$</div></foreignObject>
  <foreignObject x="422" y="315" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dfrac{1}{9}$</div></foreignObject>
  <foreignObject x="65.5" y="317.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\dot{H}$</div></foreignObject>
  <foreignObject x="28" y="349.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{relative}$</div></foreignObject>
  <foreignObject x="32" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="4.5" y="199.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{source}$</div></foreignObject>
</svg>

```pysahdy
The dose rate of a point-like gamma source is $8\,\mu\text{Sv/h}$ at a distance of $1\,\text{m}$. What is it at $4\,\text{m}$?
---
The distance becomes four times as large, so the dose rate is $\left(\tfrac{1}{4}\right)^2 = \tfrac{1}{16}$ of the original: $8\,\mu\text{Sv/h} \cdot \tfrac{1}{16} = 0.5\,\mu\text{Sv/h}$.
```

### Half-value thickness
The photons of gamma radiation do not stop in a shield at a certain depth; instead, each photon is absorbed or scattered at random. Every layer of the same thickness therefore attenuates the same fraction of the radiation arriving at it, in the same way as every half-life halves the number of nuclei. The **half-value thickness** $d_{1/2}$ is the thickness of material that halves the dose rate (chapter *Ionising radiation and the body*). When the thickness of the shield is $d$, the dose rate is
```latex
\dot{H} = \dot{H}_0 \left(\frac{1}{2}\right)^{d/d_{1/2}}
```
where $\dot{H}_0$ is the dose rate without a shield and $\dot{H}$ behind the shield. The half-value thickness depends on the material and on the energy of the gamma radiation: for the gamma radiation of caesium-137 it is about $5.5\,\text{mm}$ in lead and about $4\,\text{cm}$ in concrete. In the model of this chapter the half-value thickness of lead is rounded to $6.0\,\text{mm}$. The formula is a simplified model: in a real shield some of the scattered photons still get through, so a shield is dimensioned with a safety margin.

<svg data-fig="suoja" viewBox="0 0 600 380" role="img" aria-label="Graph to scale: dose rate in microsieverts per hour as a function of the thickness of a lead plate, thickness from zero to 30 millimetres. Without lead the dose rate is 40, and every 6 millimetre layer halves it: 20 at 6 millimetres, 10 at 12 millimetres, 5 at 18 millimetres. The curve falls ever more gently and never reaches zero. The half-value thickness is marked with a horizontal bracket at the first layer." style="max-width:100%;font-size:24px">
  <line x1="177" y1="312" x2="177" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="312" x2="253.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330.5" y1="312" x2="330.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="407" y1="312" x2="407" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="484" y1="312" x2="484" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="254.5" x2="484" y2="254.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="196.5" x2="484" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="139" x2="484" y2="139" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="81" x2="484" y2="81" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="498" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M510,312 L497,318 L497,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="177" y1="312" x2="177" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="253.5" y1="312" x2="253.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="330.5" y1="312" x2="330.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="314" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$18$</div></foreignObject>
  <line x1="407" y1="312" x2="407" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="390.5" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="484" y1="312" x2="484" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="321.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="93" y1="254.5" x2="100" y2="254.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="240" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="93" y1="196.5" x2="100" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="182" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="93" y1="139" x2="100" y2="139" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="124.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="93" y1="81" x2="100" y2="81" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="66.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="516" y="297.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{mm})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dot{H}\ (\mu\text{Sv/h})$</div></foreignObject>
  <polyline points="100,81 103,87.5 106.5,94 109.5,100.5 113,106.5 116,112 119,118 122.5,123.5 125.5,128.5 129,134 132,139 135,144 138.5,148.5 141.5,153.5 145,158 148,162.5 151,166.5 154.5,170.5 157.5,174.5 161,178.5 164,182.5 167,186 170.5,189.5 173.5,193 177,196.5 180,200 183,203 186.5,206 189.5,209 193,212 196,215 199,217.5 202.5,220.5 205.5,223 209,225.5 212,228 215,230.5 218.5,232.5 221.5,235 225,237 228,239.5 231,241.5 234.5,243.5 237.5,245.5 241,247 244,249 247,251 250.5,252.5 253.5,254.5 257,256 260,257.5 263,259 266.5,260.5 269.5,262 273,263.5 276,265 279,266 282.5,267.5 285.5,269 289,270 292,271 295,272.5 298.5,273.5 301.5,274.5 305,275.5 308,276.5 311,277.5 314.5,278.5 317.5,279.5 321,280.5 324,281.5 327,282.5 330.5,283 333.5,284 337,285 340,285.5 343,286.5 346.5,287 349.5,287.5 353,288.5 356,289 359,289.5 362.5,290.5 365.5,291 369,291.5 372,292 375,292.5 378.5,293.5 381.5,294 385,294.5 388,295 391,295.5 394.5,296 397.5,296.5 401,296.5 404,297 407,297.5 410.5,298 413.5,298.5 417,299 420,299 423,299.5 426.5,300 429.5,300 433,300.5 436,301 439,301 442.5,301.5 445.5,302 449,302 452,302.5 455,302.5 458.5,303 461.5,303 465,303.5 468,303.5 471,304 474.5,304 477.5,304.5 481,304.5 484,305" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="177" y1="196.5" x2="177" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="196.5" x2="177" y2="196.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="177" cy="196.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="253.5" y1="254.5" x2="253.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="254.5" x2="253.5" y2="254.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="253.5" cy="254.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="330.5" y1="283" x2="330.5" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="283" x2="330.5" y2="283" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="330.5" cy="283" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="81" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="100" y1="61" x2="177" y2="61" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="100" y1="61" x2="100" y2="69" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="177" y1="61" x2="177" y2="69" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="189" y="46.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 6.0\,\text{mm}$</span></div></foreignObject>
  <foreignObject x="279" y="159" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\dot{H} = \dot{H}_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$</span></div></foreignObject>
</svg>

## Worked example
Alpha radiation from the decay products of radon in the indoor air of a dwelling reaches the lungs. Assume simply that the radiation is spread evenly over the whole lungs, whose mass is $1.2\,\text{kg}$, and that over a year the lungs absorb energy $2.0\,\text{mJ}$ from alpha radiation. How large an effective dose does this cause? The tissue weighting factor of the lungs is $0.12$.

<!-- vaihe -->

**Given and asked.** Absorbed energy $E = 2.0\,\text{mJ}$, mass of the lungs $m = 1.2\,\text{kg}$, weighting factor of alpha radiation $w_\text{R} = 20$ and weighting factor of the lungs $w_\text{T} = 0.12$. The effective dose $H_\text{E}$ is asked.

<!-- vaihe -->

**Principle.** The absorbed dose is energy per unit mass. At the same dose alpha radiation damages cells many times more than gamma radiation, so the equivalent dose of the lungs is obtained with the factor $w_\text{R}$. Only the lungs are irradiated, so the effective dose is the equivalent dose of the lungs multiplied by their weighting factor $w_\text{T}$.

<!-- vaihe -->

**Formula solved.** The equations $D = \tfrac{E}{m}$, $H_\text{T} = w_\text{R} D$ and $H_\text{E} = w_\text{T} H_\text{T}$ are combined:
```latex
H_\text{E} = w_\text{T} w_\text{R} \frac{E}{m}
```

<!-- vaihe -->

**Unit conversions.** $E = 2.0\,\text{mJ} = 2.0 \cdot 0.001\,\text{J} = 0.0020\,\text{J}$. In addition, $1\,\tfrac{\text{J}}{\text{kg}} = 1\,\text{Gy}$, and for a weighted dose the same unit is $1\,\text{Sv}$.

<!-- vaihe -->

**Substitution.**
```latex
\begin{aligned}
&H_\text{E} = w_\text{T} w_\text{R} \frac{E}{m} \\
&= 0.12 \cdot 20 \cdot \frac{0.0020\,\text{J}}{1.2\,\text{kg}} \\
&= 2.4 \cdot 0.0016667\,\text{Sv} \\
&= 0.0040\,\text{Sv}
\end{aligned}
```

<!-- vaihe -->

**Result.** The effective dose is about $0.0040\,\text{Sv} = 4.0\,\text{mSv}$ per year, with two significant figures like the energy $2.0\,\text{mJ}$ and the mass $1.2\,\text{kg}$.

<!-- vaihe -->

**Reasonableness.** The absorbed dose is only about $1.7\,\text{mGy}$, but the factor $20$ of alpha radiation raises the equivalent dose of the lungs to about $33\,\text{mSv}$, and the factor $0.12$ reduces it to the effective dose, which describes the radiation detriment to the whole body.

The even distribution is a rough model assumption: in reality the alpha particles are absorbed in a thin cell layer on the surface of the airways. The result is of the same order of magnitude as the average radon dose of a Finn, about $4\,\text{mSv}$ per year.

The example dealt with the weighting of the dose; in the next task the dose is reduced with time, distance and shielding.

## Common misconception
Many people think that natural radiation is harmless and only radiation produced by humans is dangerous. The body, however, does not distinguish whether an alpha particle comes from the radon in a cellar or from a laboratory source: the origin of the radiation does not in itself decide how dangerous it is. The effective dose is used to compare exposures and to estimate radiation detriment, but the same effective dose does not guarantee exactly the same individual risk. The largest dose of a Finn comes from natural radon, and therefore measuring and fixing radon is the most effective way to reduce one's own radiation dose.

Another common mistake is to think that doubling the distance halves the dose rate. The radiation from a point source spreads over an area that grows as the square of the distance, so doubling the distance reduces the dose rate to a quarter. Likewise, two half-value thicknesses do not stop gamma radiation completely, but let a quarter through.

## Summary
- The absorbed dose is the absorbed energy per unit mass, $D = \tfrac{E}{m}$, in the unit gray, $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$.
- The equivalent dose $H_\text{T} = w_\text{R} D_\text{T}$ takes the type of radiation into account (alpha $20$, gamma and beta $1$), and the effective dose

    $$H_\text{E} = w_{\text{T}1} H_{\text{T}1} + w_{\text{T}2} H_{\text{T}2} + \ldots$$

    the sensitivity of the tissues. Both are in the unit sievert, $\text{Sv}$.

- The average effective dose of a Finn is about $5.9\,\text{mSv}$ per year (STUK-A263, 2020), of which indoor radon is about $4\,\text{mSv}$, or about two thirds.
- The decay products of radon emit alpha radiation into the lungs; the reference level for dwellings is $300\,\tfrac{\text{Bq}}{\text{m}^3}$.
- Protection from external radiation is by time ($H = \dot{H} t$), distance ($\dot{H} \propto \tfrac{1}{r^2}$) and shielding: every half-value thickness halves the dose rate of gamma radiation.
