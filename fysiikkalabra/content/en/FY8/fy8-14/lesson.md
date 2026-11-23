# Radiation in medicine and technology

> **Why** is a patient injected with radioactive sugar in a PET scan, and how does the scanner work out where inside the body the radiation came from?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: a hospital PET-CT scanning room. In the middle is a large white scanner with a round opening. A patient lies under a blanket on a scanning table that slides into the opening. On the left wall is a window to the control room, where a screen shows a dark cross-sectional image with one bright orange spot." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Key idea

### X-rays are produced when fast electrons hit an anode

**X-radiation** is high-energy photon radiation. It is produced when fast electrons slow down in matter (bremsstrahlung), or when they knock an electron out of the innermost shell of an atom and an electron from an outer shell drops into its place (characteristic X-radiation). In an X-ray tube, electrons released from a glowing cathode are accelerated by a voltage $U$ towards an anode made of tungsten. Each electron gains a kinetic energy $eU$, so at a voltage of $80\,\text{kV}$ the energy of a photon is at most $80\,\text{keV}$. Most of the electrons' energy, about $99\,\%$, turns into internal energy in the anode, and only a small part is radiated as X-ray photons. The bremsstrahlung spectrum is continuous, and the sharp characteristic peaks of the anode atoms stand on top of it; for tungsten they are at about $59\,\text{keV}$. X-ray and gamma photons are the same electromagnetic radiation: the name tells whether the photon was produced in the slowing down of electrons or in a transition in the inner shell of an atom, or in a transition in a nucleus. Both ionise and are attenuated in matter in the same way (chapter *Ionising radiation and the body*).

<svg data-fig="rontgen" viewBox="0 0 600 380" role="img" aria-label="Schematic, not to scale: X-ray imaging. At the top is a glass X-ray tube: on the left a glowing cathode, from which electrons are accelerated to the right towards the anode. X-ray photons leave the anode downwards as a fan of wavy lines. In their path is a cross-section of a forearm: soft tissue with two bones inside it. Photons that hit the bones are stopped, and the others continue through the tissue to the detector below. A lighter shadow appears on the detector where the bones are, because less radiation reaches it there." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-rontgen.webp" x="20.7" y="0" width="585.4" height="376.8" preserveAspectRatio="none"/>
  <foreignObject x="293.5" y="57.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="90" y="40.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{X-ray tube}$</div></foreignObject>
  <foreignObject x="117" y="151.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{soft tissue}$</div></foreignObject>
  <foreignObject x="542" y="191.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{bone}$</div></foreignObject>
  <foreignObject x="130" y="300.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{detector}$</div></foreignObject>
  <foreignObject x="296" y="337.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{shadow of the bones}$</div></foreignObject>
</svg>

### X-ray images and computed tomography

An X-ray image is a shadow image. The radiation passes through the patient to a detector, and every layer of tissue attenuates some of it. Bone attenuates X-rays much more than soft tissue, because it is denser and contains calcium, whose atomic number $20$ is much larger than those of the hydrogen, carbon and oxygen of soft tissue. At the energies of X-ray imaging the probability of photoelectric absorption grows strongly with the atomic number (chapter *Ionising radiation and the body*), so the difference also depends on the energy of the radiation: for radiation of about $60\,\text{keV}$, the half-value thickness of soft tissue is about $3.4\,\text{cm}$ and that of bone only about $1.1\,\text{cm}$. Less radiation therefore reaches the detector behind a bone, and the bone appears light in the image. The air in the lungs lets the radiation through almost unattenuated, so the lungs appear dark. The **contrast** of the image, that is, the difference in brightness, thus arises because different tissues attenuate radiation differently.

In computed tomography (CT), an X-ray tube and detectors rotate around the patient. The scanner measures the attenuation from thousands of directions, and a computer calculates from them how much each small volume element attenuates. The result is a cross-sectional image in which organs lying behind one another are also visible. However, the dose from a CT scan is tens of times larger than the dose from a chest X-ray.

```pysahdy
In CT, $800$ projections are taken, each giving a dose of $0.010\,\text{mSv}$. The dose of a chest X-ray is $0.1\,\text{mSv}$. How many times larger is the total CT dose than the X-ray dose?
---
The doses add up: $800 \cdot 0.010\,\text{mSv} = 8\,\text{mSv}$. The ratio is $\tfrac{8\,\text{mSv}}{0.1\,\text{mSv}} = 80$, so the CT dose is about $80$ times larger. One direction gives only a tenth of an X-ray dose, but there are many directions, so the difference is tens of times and not a thousandfold.
```

| Examination | Effective dose |
| --- | --- |
| dental X-ray | $< 0.01\,\text{mSv}$ |
| chest X-ray (front and side view) | about $0.1\,\text{mSv}$ |
| head CT | about $2\,\text{mSv}$ |
| body CT | about $5$–$10\,\text{mSv}$ |
| bone scan (radionuclide imaging) | about $3\,\text{mSv}$ |
| PET scan | about $6\,\text{mSv}$ |

Source: typical orders of magnitude from the publications of STUK (the Radiation and Nuclear Safety Authority) on radiation exposure in health care ([STUK: Röntgentutkimuksen säteilyannokset vaihtelevat](https://www.julkari.fi/server/api/core/bitstreams/89234513-99f8-4ee2-a720-20bd04eb2cfb/content), in Finnish) and ICRP Publication 128 (2015); the dose of an individual examination depends on the equipment, the imaging protocol and the patient. For comparison, a person in Finland receives on average about $5.1\,\text{mSv}$ a year from natural radiation (chapter *Radiation dose and radiation safety in Finland*).

<figure class="unit-photo"><img src="pics/fy8/pet-ct-scanner.webp" alt="A hospital scanning room: a pale green ring-shaped device with a patient table covered by a white sheet pointing towards its opening."><figcaption>A PET-CT scanner in Bron, France. Inside the ring are the detector ring for PET imaging and the X-ray tube and detectors for computed tomography. The patient slides through the ring on the table.</figcaption></figure>


### Radionuclide imaging: a tracer shows how an organ works

A **tracer** is a radioactive nuclide attached to a compound that the body handles like its own substances, so it accumulates in the organ being examined. A detector outside the body detects the radiation of the tracer. The image therefore shows not only structure, like an X-ray image, but where the body is active: in a bone scan, for example, the tracer accumulates where bone is renewing itself rapidly, such as in fractures and metastases.

The most common nuclide in tracers is technetium-$99\text{m}$. It emits almost only gamma radiation of $140\,\text{keV}$, which escapes from the body and ionises sparsely along its way. Its half-life is $6.01\,\text{h}$ (chapter *The decay law and half-life*), so after a day only about $6\,\%$ of the activity is left, and part of the substance also leaves the body in the urine. A gamma camera images the radiation from the patient, and in a SPECT scanner it rotates around the patient, which gives a three-dimensional image.

### PET: two photons in opposite directions

The tracer in PET (positron emission tomography) is usually fluorine-18 in a compound resembling sugar (FDG). Cancer cells use a lot of sugar, so more of the tracer accumulates in them than elsewhere. The tracer is not completely specific to cancer cells, however: it also accumulates, for example, in inflamed tissue and in the brain, so a bright spot in a PET image does not prove cancer on its own. Fluorine-18 decays by $\beta^+$ decay, and its half-life is $110\,\text{min}$. The positron produced in the decay travels about a millimetre in the tissue and meets an electron. They annihilate: the mass of both turns into two photons, each with an energy of $511\,\text{keV}$, which leave in nearly opposite directions, because the total momentum of the particles is small.

<svg data-fig="pet" viewBox="0 0 600 380" role="img" aria-label="Schematic, not to scale: PET imaging. On the left is a cross-section of the patient in the middle of a detector ring. Inside the body a fluorine-18 nucleus emits a positron, which travels a short distance and meets an electron. Two photons leave the meeting point in opposite directions and hit two detectors of the ring, which are coloured orange. A dashed line segment is drawn between the detectors, and the annihilation must have happened on it. On the right is an enlargement: a positron and an electron meet, and two photons of 511 kiloelectronvolts are produced, leaving at an angle of 180 degrees to each other." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-pet.webp" x="0" y="0" width="600" height="390" preserveAspectRatio="none"/>
  <foreignObject x="107" y="347.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{detector ring}$</div></foreignObject>
  <foreignObject x="416" y="25.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$e^+ + e^- \rightarrow \gamma + \gamma$</div></foreignObject>
  <foreignObject x="393.5" y="73.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$e^+$</div></foreignObject>
  <foreignObject x="525.5" y="73.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="376.5" y="179.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$511\,\text{keV}$</div></foreignObject>
  <foreignObject x="480.5" y="237.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$511\,\text{keV}$</div></foreignObject>
  <foreignObject x="401" y="237.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$180^\circ$</div></foreignObject>
  <foreignObject x="420" y="303.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{source on line}$</div></foreignObject>
</svg>

A ring of detectors surrounds the patient. When two opposite detectors detect a photon within a few nanoseconds of each other, that is, in **coincidence**, the scanner concludes that the photons were produced in the same annihilation somewhere on the line segment between those detectors. If the difference in the photons' arrival times is not measured, a single line segment does not tell where on the segment the source is. Modern PET scanners also measure this time difference (time-of-flight PET) with an accuracy of about $0.3\,\text{ns}$. Light travels about $30\,\text{cm}$ in a nanosecond, so the time difference narrows the source to a stretch of a few centimetres on the segment. Because the positron travels before the annihilation, the segment tells the place of the annihilation and not exactly the place of the decay. The actual image is formed only from many segments: when millions of segments have accumulated, they intersect most densely where there is the most tracer, and a computer calculates the image from them. Because of its short half-life, fluorine-18 is made in a particle accelerator, a cyclotron, close to the imaging site, for example at the Turku PET Centre.

```pysahdy
The two opposite detectors of a PET scanner register the annihilation photons with a time difference of $0.40\,\text{ns}$. Light travels $30\,\text{cm}$ in a nanosecond. How far from the midpoint of the line is the source, and on which side?
---
The photon detected later travels an extra distance $2x$: $2x = c\,\Delta t = 30\,\tfrac{\text{cm}}{\text{ns}} \cdot 0.40\,\text{ns} = 12\,\text{cm}$, so $x = 6.0\,\text{cm}$. The source is $6.0\,\text{cm}$ from the midpoint, on the side of the detector that registered a photon first.
```

### Radiotherapy: a large dose to the tumour, a small dose to healthy tissue

**Radiotherapy** is the treatment of cancer with ionising radiation: a large dose damages the DNA of cancer cells so much that the cells die. Most commonly the radiation comes from outside the body from a linear accelerator, which accelerates electrons to millions of electronvolts and slows them down to produce X-rays. The radiation always passes through healthy tissue as well. The tumour is therefore irradiated from several directions: the beams intersect at the tumour, so the tumour receives the dose of all the beams, while healthy tissue along the beams receives only part of it. The treatment is planned with the help of a CT image.

<svg data-fig="sadehoito" viewBox="0 0 600 360" role="img" aria-label="Schematic, not to scale: radiotherapy from five directions. In the middle of a cross-section of the patient is a tumour. Five radiation beams come from outside the body from different directions, and each passes through the tumour and through the body. The beams intersect only at the tumour, so the tumour receives the dose of five beams, 5 times 0.40 gray, that is, 2.0 gray. Healthy tissue along a beam receives the dose of only one beam, about 0.40 gray." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-sadehoito.webp" x="1.2" y="0" width="597" height="369.4" preserveAspectRatio="none"/>
  <foreignObject x="440" y="109.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tumour}$</div></foreignObject>
  <foreignObject x="440" y="141.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$2.0\,\text{Gy}$</div></foreignObject>
  <foreignObject x="440" y="229.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{normal tissue}$</div></foreignObject>
  <foreignObject x="440" y="261.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$0.40\,\text{Gy}$</div></foreignObject>
  <foreignObject x="452" y="25.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{beam}$</div></foreignObject>
</svg>

The model in the figure is simplified. In real treatment the dose is distributed in three dimensions, the dose of a beam changes with depth and scattered radiation also reaches outside the beams, so healthy tissue always receives some radiation. The treatment plan is optimised so that the tumour receives a sufficient dose and the dose to healthy tissue, especially to sensitive organs, stays as small as possible.

The treatment is usually divided into many parts: typically the tumour receives $2\,\text{Gy}$ at a time on weekdays, for example $60\,\text{Gy}$ in total over about six weeks. Healthy cells repair their damage between treatments better than cancer cells do. The radiation source can also be placed inside or next to the tumour, or the patient can swallow a drug that accumulates like a tracer, such as the iodine-131 used in the treatment of thyroid cancer.

### Radiation in industry and research

Medical supplies such as syringes and surgical gloves are **sterilised** in their sealed packages with gamma radiation from cobalt-60 or with an electron beam. The usual dose of $25\,\text{kGy}$ kills microbes even though it would heat water by only about $6\,\text{K}$: the effect is based on ionisation, not on heating, and the product does not become radioactive. In a paper machine's **thickness gauge**, beta radiation passes through the paper web to a detector. The thicker the paper, the less radiation gets through, and the gauge reading continuously controls the adjustment of the machine. In a similar way, gamma radiation is used to measure steel plates, and welds are imaged with a gamma source.

A household **smoke detector** contains about $37\,\text{kBq}$ of americium-241, whose alpha radiation ionises the air in a small chamber, so that a weak electric current flows through the chamber. Smoke particles bind ions, the current decreases and the alarm sounds. The half-life of americium-241 is $432\,\text{a}$, so in ten years its activity decreases by only about $2\,\%$. **Radiocarbon dating** is based on the fact that carbon-14 is constantly produced in the atmosphere and a living organism keeps its share of carbon-14 the same. After death, carbon-14 decays with a half-life of $5700\,\text{a}$, so the age can be calculated from the remaining share up to about $50\,000$ years.

<svg data-fig="mittari" viewBox="0 0 600 340" role="img" aria-label="Schematic, not to scale: the thickness gauge of a paper machine. A horizontal paper web runs from left to right between two pairs of rollers. Below the web is a beta radiation source, from which electrons travel upwards as blue dots through the paper. Some are stopped in the paper, and some reach the detector above the web. A wire from the detector carries the reading to a controller, which adjusts the pressure of the rollers: the thicker the paper, the less radiation gets through." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-14-mittari.webp" x="1.2" y="0" width="597" height="348.3" preserveAspectRatio="none"/>
  <foreignObject x="142" y="83.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{detector}$</div></foreignObject>
  <foreignObject x="113" y="243.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{source}\ (\beta^-)$</div></foreignObject>
  <foreignObject x="362" y="199.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paper web}$</div></foreignObject>
  <foreignObject x="428.5" y="5.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{control}$</div></foreignObject>
  <foreignObject x="121.5" y="301.5" width="357" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{thicker paper: less gets through}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/linear-accelerator.webp" alt="A pale blue treatment room: a large white radiotherapy machine with its treatment head above the couch."><figcaption>A radiotherapy linear accelerator. It accelerates electrons and uses them to produce high-energy X-rays. The treatment head rotates around the patient, so the radiation reaches the tumour from many directions while healthy tissue receives a smaller dose.</figcaption></figure>

### Safety of patients and staff

The Radiation Act (859/2018) sets three principles for the use of radiation. **Justification:** the benefit from an examination or treatment must be greater than the harm from the radiation, so an X-ray examination is done only when its result affects the patient's care. **Optimisation:** the dose is kept as low as is practically possible while the image still answers the question (ALARA, *as low as reasonably achievable*). For example, children are imaged with lower settings than adults. **Dose limits:** the effective dose of a person working with radiation may be at most $20\,\text{mSv}$ a year. Dose limits do not apply to the patient's dose; the patient is protected by justification and optimisation.

Staff protect themselves with time, distance and shielding (chapter *Radiation dose and radiation safety in Finland*). A radiographer starts the scan from behind a protective wall, and a lead apron is worn in the imaging room. A tracer is handled with a syringe shielded with lead or tungsten. The $511\,\text{keV}$ photons of PET pass through lead much more easily than the $140\,\text{keV}$ photons of technetium-$99\text{m}$: the half-value thickness of lead is about $3.9\,\text{mm}$ for them and $0.26\,\text{mm}$ for the technetium photons. Radiation workers wear a dosimeter, and using radiation requires a safety licence from the Radiation and Nuclear Safety Authority (STUK).

## Formula: Attenuation in layers and annihilation

### Radiation through several layers

Each layer of tissue attenuates radiation according to its half-value thickness (chapter *Ionising radiation and the body*). When a beam passes first through soft tissue and then through bone, the share of the radiation that got through the soft tissue is passed through the bone in the same proportion. The shares are therefore multiplied:

```latex
I = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{tissue}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{bone}}
```

where $I_0$ is the intensity of the radiation entering the beam, $I$ is the intensity of the radiation that got through the layers, and $n$ is the thickness of a layer in half-value thicknesses: $n_\text{tissue} = d_\text{tissue} : d_{1/2}^\text{tissue}$ and $n_\text{bone} = d_\text{bone} : d_{1/2}^\text{bone}$. Here $d_\text{tissue}$ and $d_\text{bone}$ are the thicknesses of the soft tissue and the bone, and $d_{1/2}^\text{tissue}$ and $d_{1/2}^\text{bone}$ are their half-value thicknesses. Because $\left(\tfrac{1}{2}\right)^{n_\text{tissue}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{bone}} = \left(\tfrac{1}{2}\right)^{n_\text{tissue} + n_\text{bone}}$, the numbers of half-value thicknesses can also be added together. The order of the layers does not matter, and a third layer adds a third similar factor. The contrast of an X-ray image is obtained by comparing two beams, one of which passes through soft tissue alone and the other also through bone. The half-value thickness depends on the energy of the photons. The radiation from a real X-ray tube contains photons of many energies, so here we use an average energy of about $60\,\text{keV}$.

<svg data-fig="kontrasti" viewBox="0 0 600 380" role="img" aria-label="Graph to scale: the share of X-radiation that gets through, I per I zero, as a function of the thickness d of the layer, with the thickness from zero to 8 centimetres and the photon energy about 60 kiloelectronvolts. In soft tissue the share halves after every 3.4 centimetres, in bone already after 1.1 centimetres: at 1.1 centimetres half gets through bone and at 2.2 centimetres a quarter, while half gets through soft tissue at 3.4 centimetres. The curve for bone therefore falls much more steeply." style="max-width:100%;font-size:24px">
  <line x1="146" y1="312" x2="146" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="312" x2="192.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="239" y1="312" x2="239" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="312" x2="285" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331" y1="312" x2="331" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="377.5" y1="312" x2="377.5" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424" y1="312" x2="424" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="312" x2="470" y2="58" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="253" x2="470" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="194.5" x2="470" y2="194.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="135.5" x2="470" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="77" x2="470" y2="77" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="312" x2="484" y2="312" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,312 L483,318 L483,306 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="313" x2="100" y2="44" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,32 L106,45 L94,45 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="146" y1="312" x2="146" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="136" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="192.5" y1="312" x2="192.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="182.5" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="239" y1="312" x2="239" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="229" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="285" y1="312" x2="285" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="275" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="331" y1="312" x2="331" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="321" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="377.5" y1="312" x2="377.5" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367.5" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="424" y1="312" x2="424" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="414" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="470" y1="312" x2="470" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="93" y1="253" x2="100" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="238.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.25$</div></foreignObject>
  <line x1="93" y1="194.5" x2="100" y2="194.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="180" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.50$</div></foreignObject>
  <line x1="93" y1="135.5" x2="100" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="121" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0.75$</div></foreignObject>
  <line x1="93" y1="77" x2="100" y2="77" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="62.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="70" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="297.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d\ (\text{cm})$</div></foreignObject>
  <foreignObject x="90" y="1.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I : I_0$</div></foreignObject>
  <polyline points="100,77 103,80 106,83 109,86 112.5,89.5 115.5,92.5 118.5,95 121.5,98 124.5,101 128,104 131,106.5 134,109.5 137,112 140,115 143,117.5 146,120 149.5,123 152.5,125.5 155.5,128 158.5,130.5 161.5,133 165,135 168,137.5 171,140 174,142.5 177,144.5 180,147 183,149 186.5,151.5 189.5,153.5 192.5,155.5 195.5,157.5 198.5,160 202,162 205,164 208,166 211,168 214,170 217,171.5 220,173.5 223.5,175.5 226.5,177.5 229.5,179 232.5,181 235.5,182.5 239,184.5 242,186 245,188 248,189.5 251,191 254,193 257,194.5 260.5,196 263.5,197.5 266.5,199 269.5,200.5 272.5,202 276,203.5 279,205 282,206.5 285,208 288,209.5 291,210.5 294,212 297.5,213.5 300.5,215 303.5,216 306.5,217.5 309.5,218.5 313,220 316,221 319,222.5 322,223.5 325,225 328,226 331,227 334.5,228.5 337.5,229.5 340.5,230.5 343.5,231.5 346.5,232.5 350,234 353,235 356,236 359,237 362,238 365,239 368,240 371.5,241 374.5,242 377.5,243 380.5,243.5 383.5,244.5 387,245.5 390,246.5 393,247.5 396,248 399,249 402,250 405,251 408.5,251.5 411.5,252.5 414.5,253 417.5,254 420.5,255 424,255.5 427,256.5 430,257 433,258 436,258.5 439,259.5 442,260 445.5,260.5 448.5,261.5 451.5,262 454.5,262.5 457.5,263.5 461,264 464,264.5 467,265.5 470,266" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="100,77 103,86.5 106,96 109,104.5 112.5,113 115.5,121.5 118.5,129 121.5,136.5 124.5,144 128,151 131,157.5 134,164 137,170 140,176 143,181.5 146,187 149.5,192 152.5,197 155.5,201.5 158.5,206 161.5,210.5 165,214.5 168,218.5 171,222.5 174,226 177,229.5 180,233 183,236.5 186.5,239.5 189.5,242.5 192.5,245.5 195.5,248 198.5,250.5 202,253 205,255.5 208,258 211,260 214,262.5 217,264.5 220,266.5 223.5,268 226.5,270 229.5,271.5 232.5,273.5 235.5,275 239,276.5 242,278 245,279.5 248,280.5 251,282 254,283 257,284.5 260.5,285.5 263.5,286.5 266.5,287.5 269.5,288.5 272.5,289.5 276,290.5 279,291.5 282,292.5 285,293 288,294 291,294.5 294,295.5 297.5,296 300.5,296.5 303.5,297.5 306.5,298 309.5,298.5 313,299 316,299.5 319,300 322,300.5 325,301 328,301.5 331,302 334.5,302.5 337.5,302.5 340.5,303 343.5,303.5 346.5,304 350,304 353,304.5 356,305 359,305 362,305.5 365,305.5 368,306 371.5,306 374.5,306.5 377.5,306.5 380.5,307 383.5,307 387,307.5 390,307.5 393,307.5 396,308 399,308 402,308 405,308.5 408.5,308.5 411.5,308.5 414.5,309 417.5,309 420.5,309 424,309 427,309.5 430,309.5 433,309.5 436,309.5 439,309.5 442,310 445.5,310 448.5,310 451.5,310 454.5,310 457.5,310 461,310.5 464,310.5 467,310.5 470,310.5" fill="none" stroke="#a97a35" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="257" y1="194.5" x2="257" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="257" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="257" cy="194.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <line x1="151" y1="194.5" x2="151" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="194.5" x2="151" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="151" cy="194.5" r="6.5" fill="#a97a35" stroke="#ffffff" stroke-width="2"/>
  <line x1="202" y1="253" x2="202" y2="312" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="253" x2="202" y2="253" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="202" cy="253" r="6.5" fill="#a97a35" stroke="#ffffff" stroke-width="2"/>
  <circle cx="100" cy="77" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="341" y="189.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{soft tissue}$</span></div></foreignObject>
  <foreignObject x="109" y="213" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{bone}$</span></div></foreignObject>
  <foreignObject x="266.5" y="81" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$</span></div></foreignObject>
  <foreignObject x="276.5" y="151.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 3.4\,\text{cm}$</span></div></foreignObject>
  <foreignObject x="299" y="262" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$d_{1/2} = 1.1\,\text{cm}$</span></div></foreignObject>
</svg>

```pysahdy
An X-ray beam passes through two half-value thicknesses of soft tissue and then one half-value thickness of bone. What fraction of the radiation gets through?
---
The numbers of half-value thicknesses add up: $\left(\tfrac{1}{2}\right)^{2+1} = \tfrac{1}{8}$, so $12.5\,\%$ gets through.
```

### Energy of an annihilation photon

When a positron and an electron annihilate almost at rest, their combined mass $2m_e$ turns entirely into the energy of photons (chapter *Mass defect and nuclear binding energy*). The initial momentum is almost zero, so two photons are produced, they leave in nearly opposite directions and they have approximately the same energy:

```latex
E_\gamma = m_e c^2
```

where $E_\gamma$ is the energy of one photon ($\text{J}$), $m_e = 9.109 \cdot 10^{-31}\,\text{kg}$ is the mass of the electron and the positron, and $c = 2.998 \cdot 10^{8}\,\text{m/s}$ is the speed of light. Substituting gives $$
\begin{aligned}
&E_\gamma \\
&= 9.109 \cdot 10^{-31}\,\text{kg} \\
&\cdot (2.998 \cdot 10^{8}\,\text{m/s})^2 \\
&= 8.187 \cdot 10^{-14}\,\text{J}
\end{aligned}
$$. Substituting $1\,\text{J} = \tfrac{1}{1.602 \cdot 10^{-19}}\,\text{eV}$ gives $$
\begin{aligned}
E_\gamma &= 8.187 \cdot 10^{-14} \\
&\cdot \tfrac{1}{1.602 \cdot 10^{-19}}\,\text{eV} \\
&= 5.11 \cdot 10^{5}\,\text{eV} \\
&= 511\,\text{keV}
\end{aligned}
$$. This energy is about $150\,000$ times that of a photon of visible light, and it is the same in every annihilation, so a PET scanner can reject photons whose energy differs clearly from it, because they have scattered on the way.

## Worked example

In an X-ray image of a forearm, beam A passes through $8.0\,\text{cm}$ of soft tissue. Beam B passes through $5.0\,\text{cm}$ of soft tissue and $3.0\,\text{cm}$ of bone. For radiation of an average energy of about $60\,\text{keV}$, the half-value thickness of soft tissue is $3.4\,\text{cm}$ and that of bone is $1.1\,\text{cm}$. How many times greater is the intensity that reaches the detector at beam A than at beam B?

<!-- vaihe -->

**Given and asked.** Beam A: soft tissue $d_\text{A} = 8.0\,\text{cm}$. Beam B: soft tissue $d_\text{tissue} = 5.0\,\text{cm}$ and bone $d_\text{bone} = 3.0\,\text{cm}$. Half-value thicknesses $d_{1/2}^\text{tissue} = 3.4\,\text{cm}$ and $d_{1/2}^\text{bone} = 1.1\,\text{cm}$.

We are asked for the ratio of the intensities ${I_\text{A} : I_\text{B}}$.

<!-- vaihe -->

**Principle.** The same intensity $I_0$ enters both beams. Each layer lets through a share $\left(\tfrac{1}{2}\right)^{n}$ of the radiation entering it, where $n$ is the thickness of the layer in half-value thicknesses. The shares for beam B are multiplied, that is, its numbers of half-value thicknesses are added together. In the ratio, $I_0$ cancels.

<!-- vaihe -->

**Formula solved.** For beam A, $n_\text{A} = d_\text{A} : d_{1/2}^\text{tissue}$, and for beam B, $n_\text{B} = d_\text{tissue} : d_{1/2}^\text{tissue} + d_\text{bone} : d_{1/2}^\text{bone}$. When $I_\text{A} = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{A}}$ and $I_\text{B} = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{B}}$, the ratio is

```latex
\begin{aligned}
\frac{I_\text{A}}{I_\text{B}} &= \frac{I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{A}}}{I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{B}}} \\
&= 2^{\,n_\text{B} - n_\text{A}}
\end{aligned}
```

<!-- vaihe -->

**Unit conversions.** None are needed: all thicknesses are in centimetres, so the units of the numbers $n$ cancel.

<!-- vaihe -->

**Substitution.** First we calculate the numbers of half-value thicknesses:

```latex
\begin{aligned}
n_\text{A} &= d_\text{A} : d_{1/2}^\text{tissue} \\
&= 8.0\,\text{cm} : 3.4\,\text{cm} = 2.353
\end{aligned}
```

```latex
\begin{aligned}
n_\text{B} &= d_\text{tissue} : d_{1/2}^\text{tissue} + d_\text{bone} : d_{1/2}^\text{bone} \\
&= 5.0\,\text{cm} : 3.4\,\text{cm} \\
&\quad + 3.0\,\text{cm} : 1.1\,\text{cm} \\
&= 1.471 + 2.727 = 4.198
\end{aligned}
```

The ratio is

```latex
\begin{aligned}
\frac{I_\text{A}}{I_\text{B}} &= 2^{\,n_\text{B} - n_\text{A}} \\
&= 2^{\,4.198 - 2.353} \\
&= 2^{\,1.845} = 3.59
\end{aligned}
```

<!-- vaihe -->

**Result.** At beam A, an intensity about $3.6$ times greater reaches the detector, two significant figures like the thicknesses and the half-value thicknesses. The bone therefore appears clearly lighter in the image than soft tissue alone.

<!-- vaihe -->

**Reasonableness.** We calculate the same another way, through the shares that got through: $\left(\tfrac{1}{2}\right)^{2.353} = 0.1957$ and $\left(\tfrac{1}{2}\right)^{4.198} = 0.05449$, so $I_\text{A} : I_\text{B} = 0.1957 : 0.05449 = 3.59$, as above. The ratio is also reasonable in order of magnitude: beam B has about two more half-value thicknesses, and $2^2 = 4$.

## Common misconception

Many people think that a patient gives off radiation after an X-ray examination. X-radiation is produced only while a current flows in the tube, and it stops the moment the tube is switched off: nothing radioactive stays in the patient. In radionuclide imaging the situation is different. The tracer is in the patient's body and it emits radiation until it has decayed or left the body, usually within hours or a day. This is why a PET patient waits for the scan in a room of their own, and the nurses keep their distance from the patient.

Another mistake is to think that radiation protection means the smallest possible dose at any cost. With too small a dose the image remains noisy and does not show what was being looked for. The examination has to be repeated, and the patient receives two doses. Optimisation means the smallest dose with which the image answers the question.

## Summary

- X-radiation is produced when fast electrons slow down in the anode or knock electrons out of the inner shells of its atoms; a voltage $U$ gives a photon an energy of at most $eU$.
- The contrast of an X-ray and CT image arises because bone attenuates radiation more than soft tissue; the shares that get through the layers are multiplied: $I = I_0 \cdot \left(\tfrac{1}{2}\right)^{n_\text{tissue}} \cdot \left(\tfrac{1}{2}\right)^{n_\text{bone}}$, where $n = d : d_{1/2}$.
- A tracer accumulates in the organ being examined; technetium-$99\text{m}$ emits gamma radiation of $140\,\text{keV}$, and its half-life is $6.01\,\text{h}$.
- PET: a positron and an electron annihilate into two photons going in nearly opposite directions, each with an energy of $E_\gamma = m_e c^2 = 511\,\text{keV}$; a coincidence gives a line segment, and the intersections of many segments reveal the location of the tracer.
- In radiotherapy the tumour is irradiated from several directions and with the treatment divided into parts, so that the tumour receives a large dose and healthy tissue a small one.
- Radiation is also used in sterilisation, thickness gauges, smoke detectors and radiocarbon dating.
- The principles for the use of radiation are justification, optimisation and dose limits; staff protect themselves with time, distance and shielding.
