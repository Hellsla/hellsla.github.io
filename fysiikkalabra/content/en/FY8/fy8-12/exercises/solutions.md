## fy8-12-L1-01
**Given:** half-value thickness of lead $d_{1/2} = 10.4\,\text{mm}$ for the mean gamma energy $1.25\,\text{MeV}$, thickness of the lead plate $d = 25.0\,\text{mm}$, narrow beam
**Asked:** the fraction of gamma radiation passing through, $\tfrac{I}{I_0}$, as a percentage
**Principle:** Every gamma photon has the same probability of interacting in every thin layer of lead, so every layer of one half-value thickness halves the intensity. In a narrow beam scattered photons do not return to the beam, so the attenuation law holds.
**Formula:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, from which $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Conversions:** Not needed: both thicknesses are in millimetres, so their ratio is a pure number. Finally the fraction is converted into a percentage: $1 = 100\,\%$.
**Substitution:** $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{25.0\,\text{mm} / 10.4\,\text{mm}} = \left(\tfrac{1}{2}\right)^{2.4038} = 0.18896 = 18.896\,\%$
**Answer:** $18.9\,\%$, three significant figures like the thicknesses $25.0\,\text{mm}$ and $10.4\,\text{mm}$.
**Reasonableness:** The plate contains a little over two half-value thicknesses. After two, $25\,\%$ would get through and after three $12.5\,\%$; the result lies between these and closer to $25\,\%$, as it should.

## fy8-12-L1-02
**Given:** kinetic energy of the alpha particle $E = 5.49\,\text{MeV}$, average energy of one ion pair in air $W = 34\,\text{eV}$
**Asked:** the number of ion pairs $n_\text{i}$ in the unit $10^{5}$
**Principle:** An alpha particle gives up all its kinetic energy to the air by ionising molecules one at a time until it stops. Each ion pair takes on average the energy $W$, so the number of ion pairs is the energy divided by the energy of one ion pair.
**Formula:** $E = n_\text{i} W$, from which $n_\text{i} = \dfrac{E}{W}$
**Conversions:** $5.49\,\text{MeV} = 5.49 \cdot 10^{6}\,\text{eV}$, so that the energies are in the same unit.
**Substitution:** $n_\text{i} = \dfrac{5.49 \cdot 10^{6}\,\text{eV}}{34\,\text{eV}} = 1.6147 \cdot 10^{5}$
**Answer:** $1.6 \cdot 10^{5}$ ion pairs, two significant figures like the energy $W = 34\,\text{eV}$.
**Reasonableness:** With the estimate $5 \cdot 10^{6} : 30 \approx 1.7 \cdot 10^{5}$ the order of magnitude agrees. So one particle ionises over a hundred thousand molecules, and that is why even a single alpha particle is a significant event for a GM tube or a human cell.

## fy8-12-L1-03
**Given:** total thickness of the plates $d = 18\,\text{mm}$, ratio of the net pulse counts $\tfrac{I}{I_0} = \tfrac{1}{8}$
**Asked:** the half-value thickness $d_{1/2}$ in millimetres
**Principle:** The net pulse count is proportional to the intensity of the gamma radiation hitting the GM tube, and the background radiation has already been subtracted from it. Every half-value thickness halves the intensity, and $\tfrac{1}{8} = \left(\tfrac{1}{2}\right)^{3}$, so the plates contain three half-value thicknesses.
**Formula:** $\left(\tfrac{1}{2}\right)^{d/d_{1/2}} = \left(\tfrac{1}{2}\right)^{3}$, so $\tfrac{d}{d_{1/2}} = 3$ and $d_{1/2} = \dfrac{d}{3}$
**Conversions:** Not needed: the thickness is in millimetres, and the half-value thickness is obtained in the same unit.
**Substitution:** $d_{1/2} = \dfrac{18\,\text{mm}}{3} = 6.0\,\text{mm}$
**Answer:** $6.0\,\text{mm}$, two significant figures like the thickness $18\,\text{mm}$.
**Reasonableness:** Check: $6.0\,\text{mm}$ halves the pulse count, $12\,\text{mm}$ reduces it to a quarter and $18\,\text{mm}$ to an eighth, as in the task. The value is of the order of the value for lead, $5.5\,\text{mm}$, so the material may be some heavy metal.

## fy8-12-L1-04
**Given:** half-value thickness of water $d_{1/2} = 8.1\,\text{cm}$, thickness of the water layer $d = 30\,\text{cm}$, narrow beam
**Asked:** the fraction of gamma radiation passing through, $\tfrac{I}{I_0}$, as a percentage
**Principle:** Gamma radiation is attenuated exponentially in water, because every photon has the same probability of interacting in every thin layer of water. Every $8.1\,\text{cm}$ layer halves the intensity.
**Formula:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, from which $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Conversions:** Not needed: both thicknesses are in centimetres. Finally the fraction is converted into a percentage: $1 = 100\,\%$.
**Substitution:** $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{30\,\text{cm} / 8.1\,\text{cm}} = \left(\tfrac{1}{2}\right)^{3.7037} = 0.076749 = 7.6749\,\%$
**Answer:** $7.7\,\%$, two significant figures like the half-value thickness $8.1\,\text{cm}$ and the thickness $30\,\text{cm}$.
**Reasonableness:** The water layer contains just under four half-value thicknesses. After three, $12.5\,\%$ would get through and after four $6.25\,\%$; the result lies between these, close to the latter. In a real pool there are metres of water, so the radiation is attenuated much more.

## fy8-12-L1-05
**Given:** ionisation energy of a water molecule $E = 12.6\,\text{eV}$, Planck constant $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, speed of light $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Asked:** the longest ionising wavelength $\lambda$ in nanometres
**Principle:** A single photon can ionise a molecule only if its energy is at least the ionisation energy. The energy of a photon is $E = hf = \tfrac{hc}{\lambda}$, so the longer the wavelength, the smaller the energy. The longest ionising wavelength corresponds to a photon whose energy is exactly the ionisation energy.
**Formula:** $E = \dfrac{hc}{\lambda}$, from which $\lambda = \dfrac{hc}{E}$
**Conversions:** $12.6\,\text{eV} = 12.6 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 2.0185 \cdot 10^{-18}\,\text{J}$, and finally $1\,\text{m} = 10^{9}\,\text{nm}$.
**Substitution:** $\lambda = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot \dfrac{2.998 \cdot 10^{8}\,\text{m/s}}{2.0185 \cdot 10^{-18}\,\text{J}} = 9.8412 \cdot 10^{-8}\,\text{m} = 98.412\,\text{nm}$
**Answer:** $98.4\,\text{nm}$, three significant figures like the ionisation energy $12.6\,\text{eV}$.
**Reasonableness:** The wavelength is much shorter than the $380$–$720\,\text{nm}$ of visible light, so visible light does not ionise water, as it should. Check: $1240\,\text{eV}\,\text{nm} : 12.6\,\text{eV} \approx 98\,\text{nm}$.

## fy8-12-L2-01
**Given:** pulse count near the source $N = 1260$, pulse count of the background radiation $N_\text{t} = 72$, both in the time $t = 3.00\,\text{min}$
**Asked:** the pulse rate $R$ caused by the radiation of the source in the unit $\tfrac{1}{\text{s}}$
**Principle:** A GM counter counts all ionising events, so the reading measured near the source also includes background radiation. The contribution of the source, the net pulse count, is obtained by subtracting the pulses of the background, and the pulse rate is the pulse count divided by the measuring time.
**Formula:** $R = \dfrac{N - N_\text{t}}{t}$
**Conversions:** $t = 3.00\,\text{min} = 3.00 \cdot 60\,\text{s} = 180\,\text{s}$
**Substitution:** $R = \dfrac{1260 - 72}{180\,\text{s}} = \dfrac{1188}{180\,\text{s}} = 6.600\,\tfrac{1}{\text{s}}$
**Answer:** $6.60\,\tfrac{1}{\text{s}}$, three significant figures like the measuring time $3.00\,\text{min}$.
**Reasonableness:** The total pulse rate is ${1260 : 180}\,\text{s} = 7.0\,\tfrac{1}{\text{s}}$ and the background ${72 : 180}\,\text{s} = 0.40\,\tfrac{1}{\text{s}}$; the difference is $6.6\,\tfrac{1}{\text{s}}$. The share of the background is small but not insignificant.

## fy8-12-L2-02
**Given:** thickness of lead $d_\text{Pb} = 10\,\text{mm}$ and half-value thickness $d_{1/2,\text{Pb}} = 5.5\,\text{mm}$, thickness of concrete $d_\text{b} = 20\,\text{cm}$ and half-value thickness $d_{1/2,\text{b}} = 3.9\,\text{cm}$, narrow beam
**Asked:** the fraction of radiation passing through both barriers, $\tfrac{I_2}{I_0}$, as a percentage
**Principle:** Lead lets through the fraction $\left(\tfrac{1}{2}\right)^{d_\text{Pb}/d_{1/2,\text{Pb}}}$. The weakened radiation arrives at the concrete, and the concrete lets through its own fraction of it, so the fractions are multiplied. The exponents tell the number of half-value thicknesses of each barrier.
**Formula:** $I_1 = I_0 \left(\tfrac{1}{2}\right)^{d_\text{Pb}/d_{1/2,\text{Pb}}}$ and $I_2 = I_1 \left(\tfrac{1}{2}\right)^{d_\text{b}/d_{1/2,\text{b}}}$, so $\dfrac{I_2}{I_0} = \left(\tfrac{1}{2}\right)^{d_\text{Pb}/d_{1/2,\text{Pb}} + d_\text{b}/d_{1/2,\text{b}}}$
**Conversions:** $d_\text{b} = 20\,\text{cm} = 200\,\text{mm}$ and $d_{1/2,\text{b}} = 3.9\,\text{cm} = 39\,\text{mm}$; the ratio of each barrier is calculated in the same units. Finally $1 = 100\,\%$.
**Substitution:** $\dfrac{I_2}{I_0} = \left(\tfrac{1}{2}\right)^{10\,\text{mm} / 5.5\,\text{mm} + 200\,\text{mm} / 39\,\text{mm}} = \left(\tfrac{1}{2}\right)^{1.8182 + 5.1282} = \left(\tfrac{1}{2}\right)^{6.9464} = 0.0081083 = 0.81083\,\%$
**Answer:** $0.81\,\%$, two significant figures like the half-value thicknesses $5.5\,\text{mm}$ and $3.9\,\text{cm}$.
**Reasonableness:** The barriers contain almost seven half-value thicknesses in total, and $\left(\tfrac{1}{2}\right)^{7} = \tfrac{1}{128} \approx 0.78\,\%$. The result is slightly greater, because there are a little under seven half-value thicknesses.

## fy8-12-L2-03
**Given:** pulse count without a barrier $N_0 = 480$, behind lead $N = 105$, background radiation $N_\text{t} = 5$, all in periods of $10\,\text{s}$; thickness of lead $d = 12\,\text{mm}$
**Asked:** the half-value thickness $d_{1/2}$ of lead in millimetres
**Principle:** Lead attenuates only the radiation of the source, not the background, so the net pulse counts $N_0 - N_\text{t}$ and $N - N_\text{t}$ are substituted into the attenuation law. They are proportional to the intensities. The half-value thickness is in the exponent, so it is solved with a logarithm.
**Formula:** $N - N_\text{t} = (N_0 - N_\text{t}) \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$; logarithm of both sides: $\ln \tfrac{N_0 - N_\text{t}}{N - N_\text{t}} = \tfrac{d}{d_{1/2}} \ln 2$, from which $d_{1/2} = \dfrac{d \ln 2}{\ln \tfrac{N_0 - N_\text{t}}{N - N_\text{t}}}$
**Conversions:** Not needed: the pulse counts are from periods of equal length, so their ratio is a pure number, and the thickness is in millimetres.
**Substitution:** $d_{1/2} = \dfrac{12\,\text{mm} \cdot \ln 2}{\ln \tfrac{480 - 5}{105 - 5}} = \dfrac{12\,\text{mm} \cdot 0.69315}{\ln 4.75} = \dfrac{8.3178\,\text{mm}}{1.5581} = 5.3383\,\text{mm}$
**Answer:** $5.3\,\text{mm}$, two significant figures like the thickness $12\,\text{mm}$; the random variation of the pulse counts makes a more precise result uncertain.
**Reasonableness:** The net pulse count decreased to about a fifth, and $\left(\tfrac{1}{2}\right)^{2} = \tfrac{1}{4}$, $\left(\tfrac{1}{2}\right)^{3} = \tfrac{1}{8}$, so the lead contains a good two half-value thicknesses: $12\,\text{mm} : 2.25 \approx 5.3\,\text{mm}$. The result is close to the value for caesium-137, $5.5\,\text{mm}$.

## fy8-12-L2-04
**Given:** thickness of lead $d_\text{Pb} = 10\,\text{mm}$, half-value thicknesses $5.5\,\text{mm}$ for lead and $39\,\text{mm}$ for concrete
**Asked:** the thickness $d_\text{b}$ of the concrete wall in millimetres
**Principle:** Two barriers attenuate equally much when they let through the same fraction. The fraction that gets through is $\left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, so the fractions are the same when both barriers contain the same number of half-value thicknesses.
**Formula:** $\dfrac{d_\text{b}}{d_{1/2,\text{b}}} = \dfrac{d_\text{Pb}}{d_{1/2,\text{Pb}}}$, from which $d_\text{b} = \dfrac{d_\text{Pb}}{d_{1/2,\text{Pb}}} \cdot d_{1/2,\text{b}}$
**Conversions:** Not needed: all thicknesses are in millimetres.
**Substitution:** $d_\text{b} = \dfrac{10\,\text{mm}}{5.5\,\text{mm}} \cdot 39\,\text{mm} = 1.8182 \cdot 39\,\text{mm} = 70.909\,\text{mm}$
**Answer:** $71\,\text{mm}$, two significant figures like the half-value thicknesses.
**Reasonableness:** The half-value thickness of concrete is about seven times that of lead, so a layer of concrete about seven times thicker is needed: $7 \cdot 10\,\text{mm} = 70\,\text{mm}$. So lead is a more effective shield at the same thickness, but a thicker layer of concrete is needed, and it is often the more practical building material.

## fy8-12-L3-01
**Given:** energy of the alpha particle $E_\alpha = 5.49\,\text{MeV}$ and distance $s_\alpha = 4.1\,\text{cm}$; energy of the beta particle $E_\beta = 1.0\,\text{MeV}$ and distance $s_\beta = 3.6\,\text{m}$; energy of an ion pair $W = 34\,\text{eV}$
**Asked:** how many times more ion pairs per centimetre the alpha particle produces than the beta particle, that is the ratio $\tfrac{n_\alpha / s_\alpha}{n_\beta / s_\beta}$
**Principle:** Both particles give up all their energy by ionising, so the number of ion pairs is $n_\text{i} = \tfrac{E}{W}$. When ion pairs are produced evenly, their number per centimetre is the total number divided by the length of the track. This ionisation density tells how concentrated the damage to matter by the particle is.
**Formula:** $\dfrac{n_\alpha}{s_\alpha} = \dfrac{E_\alpha}{W s_\alpha}$ and $\dfrac{n_\beta}{s_\beta} = \dfrac{E_\beta}{W s_\beta}$, so the ratio is $\dfrac{E_\alpha s_\beta}{E_\beta s_\alpha}$; $W$ cancels out.
**Conversions:** $s_\beta = 3.6\,\text{m} = 360\,\text{cm}$, so that the tracks are in the same unit. Both energies are in megaelectronvolts.
**Substitution:** $\dfrac{E_\alpha s_\beta}{E_\beta s_\alpha} = \dfrac{5.49\,\text{MeV} \cdot 360\,\text{cm}}{1.0\,\text{MeV} \cdot 4.1\,\text{cm}} = \dfrac{1976.4}{4.1} = 482.05$
**Answer:** about $4.8 \cdot 10^{2}$ times, two significant figures like the distance $4.1\,\text{cm}$ and the energy $1.0\,\text{MeV}$.
**Reasonableness:** Per centimetre the alpha particle produces about $5.49 \cdot 10^{6} : 34 : 4.1 \approx 3.9 \cdot 10^{4}$ and the beta particle about $1.0 \cdot 10^{6} : 34 : 360 \approx 82$ ion pairs; the ratio is about $480$. This is why an alpha particle stops within such a short distance and damages cells in a concentrated way.

## fy8-12-L3-02
**Given:** pulse rate without a shield $R_0 = 2400\,\tfrac{1}{\text{min}}$, behind $d_1 = 11.0\,\text{mm}$ of lead $R_1 = 630\,\tfrac{1}{\text{min}}$, background radiation $R_\text{t} = 30\,\tfrac{1}{\text{min}}$
**Asked:** the thickness $d$ of the lead shield at which the pulse rate caused by the source is $30\,\tfrac{1}{\text{min}}$
**Principle:** Lead attenuates only the radiation of the source, so the background is subtracted first: the net pulse rates are $2370$ and $600$ pulses per minute. They follow the attenuation law, so the measurements first give the half-value thickness and with it the required thickness. Both are solved with a logarithm.
**Formula:** $R_1 - R_\text{t} = (R_0 - R_\text{t}) \left(\tfrac{1}{2}\right)^{d_1/d_{1/2}}$, from which $d_{1/2} = \dfrac{d_1 \ln 2}{\ln \tfrac{R_0 - R_\text{t}}{R_1 - R_\text{t}}}$; similarly $d = \dfrac{d_{1/2} \ln \tfrac{R_0 - R_\text{t}}{R_\text{t}}}{\ln 2}$
**Conversions:** Not needed: all pulse rates are in pulses per minute and the thicknesses in millimetres.
**Substitution:** $d_{1/2} = \dfrac{11.0\,\text{mm} \cdot 0.69315}{\ln \tfrac{2370}{600}} = \dfrac{7.6246\,\text{mm}}{1.3737} = 5.5505\,\text{mm}$ and $d = \dfrac{5.5505\,\text{mm} \cdot \ln \tfrac{2370}{30}}{0.69315} = \dfrac{5.5505\,\text{mm} \cdot 4.3694}{0.69315} = 34.989\,\text{mm}$
**Answer:** about $35\,\text{mm}$ of lead, two significant figures, because the reading of the background radiation, $30\,\tfrac{1}{\text{min}}$, has two figures.
**Reasonableness:** The net pulse rate has to be reduced from $2370$ to $30$, that is to about $\tfrac{1}{79}$, and $2^{6} = 64$, $2^{7} = 128$, so a good six half-value thicknesses are needed: $6.3 \cdot 5.55\,\text{mm} \approx 35\,\text{mm}$. The half-value thickness is close to the value for caesium-137, $5.5\,\text{mm}$.

## fy8-12-L3-03
**Given:** frequency $f = 2.45\,\text{GHz}$, ionisation energy of a water molecule $E_\text{i} = 12.6\,\text{eV}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$
**Asked:** the ratio $\tfrac{E_\text{i}}{E}$, where $E$ is the energy of one photon, in the unit $10^{6}$, and why the radiation is not ionising
**Principle:** Electromagnetic radiation interacts with matter as photons, and a single photon can ionise a molecule only if its own energy $E = hf$ is at least the ionisation energy. The number of photons, that is the power of the radiation, does not help, because individual photons do not combine their energies into one ionisation.
**Formula:** $E = hf$, so $\dfrac{E_\text{i}}{E} = \dfrac{E_\text{i}}{hf}$
**Conversions:** $f = 2.45\,\text{GHz} = 2.45 \cdot 10^{9}\,\text{Hz}$; the energy of the photon is converted into electronvolts: $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$.
**Substitution:** $E = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.45 \cdot 10^{9}\,\tfrac{1}{\text{s}} = 1.6234 \cdot 10^{-24}\,\text{J} = \dfrac{1.6234 \cdot 10^{-24}\,\text{J}}{1.602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}}} = 1.0134 \cdot 10^{-5}\,\text{eV}$ and $\dfrac{E_\text{i}}{E} = \dfrac{12.6\,\text{eV}}{1.0134 \cdot 10^{-5}\,\text{eV}} = 1.2434 \cdot 10^{6}$
**Answer:** $1.24 \cdot 10^{6}$ times, three significant figures like the frequency and the ionisation energy. The energy of one microwave photon is over a million times too small to ionise a water molecule, so even powerful microwave radiation does not ionise: it only heats matter, when the energy of the photons is transferred to the motion of the molecules.
**Reasonableness:** The energy of a visible-light photon is about $2\,\text{eV}$ and its frequency about $5 \cdot 10^{14}\,\text{Hz}$; the frequency of microwaves is about $2 \cdot 10^{5}$ times smaller, so the energy of the photon is about $2\,\text{eV} : (2 \cdot 10^{5}) = 10^{-5}\,\text{eV}$, as calculated.

## fy8-12-L1-06
**Asked:** which of the shields stops alpha radiation but lets some of the beta radiation through
**Principle:** Alpha and beta particles give up their energy by ionising matter, and that is why they have a range. An alpha particle is heavy and doubly charged, so it ionises densely and stops over a very short distance. A beta particle ionises less densely, so its range is much longer.
**Model answer:** A sheet of paper is the right shield, because an alpha particle gives up its energy in a thin layer of paper owing to its dense ionisation, whereas a beta particle ionises less densely and some of it gets through the paper. An aluminium plate, a lead plate and a concrete wall are thicker, so they stop beta particles as well as alpha particles. The speed or the small mass of a particle does not prevent it from losing energy by ionising, and stopping is based on ionisation and not on electric repulsion.

## fy8-12-L1-07
**Given:** measuring time $t = 45\,\text{s}$, pulse count $N = 1215$, pulse rate of the background radiation $R_\text{t} = 90\,\tfrac{1}{\text{min}}$
**Asked:** the pulse rate $R$ caused by the radiation of the source in the unit $\tfrac{1}{\text{min}}$
**Principle:** A GM counter counts all ionising events, so the measured pulse rate also includes the background radiation. The share of the source is obtained by subtracting the pulse rate of the background from the total pulse rate.
**Formula:** $R = \dfrac{N}{t} - R_\text{t}$
**Conversions:** $t = 45\,\text{s} = \dfrac{45}{60}\,\text{min} = 0.75\,\text{min}$, so that the pulse rates are in the same unit.
**Substitution:** $R = \dfrac{1215}{0.75\,\text{min}} - 90\,\tfrac{1}{\text{min}} = 1620\,\tfrac{1}{\text{min}} - 90\,\tfrac{1}{\text{min}} = 1530\,\tfrac{1}{\text{min}}$
**Answer:** $1530\,\text{min}^{-1}$, three significant figures like the pulse count $1215$ and the background $90$.
**Reasonableness:** The total pulse rate $1620\,\tfrac{1}{\text{min}}$ is about $27\,\tfrac{1}{\text{s}}$, and the background $90\,\tfrac{1}{\text{min}}$ is only about $1.5\,\tfrac{1}{\text{s}}$. So the background is a small part of the total, and the share of the source, $1530$, is slightly below the total $1620$.

## fy8-12-L1-08
**Asked:** why an alpha emitter is fairly harmless outside the skin but dangerous inside the body
**Principle:** An alpha particle ionises densely and gives up all its energy over a very short distance. Ionisation damages cells, so the damage occurs where the energy is given up.
**Model answer:** Outside the skin, alpha particles stop in the air and in the surface layer of the skin before they reach living cells. When an alpha emitter has been swallowed or breathed in, it is right next to tissue. The alpha particle then gives up all its energy over the distance of a few cells by ionising, and the damage is concentrated in a small area. So the difference is explained by the range of the particle, not by its energy increasing or turning into another kind of radiation: an alpha particle does not accelerate in tissue and does not turn into gamma radiation.

## fy8-12-L1-09
**Asked:** the order of shields A–E according to how large a fraction of the gamma radiation they let through, from largest to smallest.
**Principle:** Every layer of one half-value thickness halves the gamma radiation, so the fraction that gets through is $\tfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$. The fraction depends only on how many half-value thicknesses $\tfrac{d}{d_{1/2}}$ there are in the shield: the more there are, the smaller the fraction that gets through. Neither the thickness alone nor the material alone decides.
**Model answer:** Let us calculate the number of half-value thicknesses $\tfrac{d}{d_{1/2}}$ for each shield.

$\tfrac{30\,\text{mm}}{12\,\text{mm}} = 2.50$ (shield A, iron)

$\tfrac{120\,\text{mm}}{39\,\text{mm}} \approx 3.08$ (shield B, concrete)

$\tfrac{22\,\text{mm}}{5.5\,\text{mm}} = 4.00$ (shield C, lead)

$\tfrac{400\,\text{mm}}{81\,\text{mm}} \approx 4.94$ (shield D, water)

$\tfrac{120\,\text{mm}}{34\,\text{mm}} \approx 3.53$ (shield E, aluminium)

The fractions that get through are, for example, for shield A $\left(\tfrac{1}{2}\right)^{2.50} \approx 0.18$ and for shield D $\left(\tfrac{1}{2}\right)^{4.94} \approx 0.033$. Similarly, for shield B one gets $12\,\%$, for shield E $8.7\,\%$ and for shield C $6.3\,\%$. According to the fraction that gets through, from largest to smallest, the order is A, B, E, C, D.

Lead is not the best shield here, although its half-value thickness is the smallest: a $400\,\text{mm}$ layer of water contains more half-value thicknesses than a $22\,\text{mm}$ lead plate. The thickness alone does not decide either: the concrete and aluminium shields are equally thick, but the half-value thickness of aluminium is smaller, so it lets through a smaller fraction. Reasonableness: the iron shield has only two and a half half-value thicknesses, and $18\,\%$ is between a quarter, $25\,\%$, and an eighth, $12.5\,\%$, as it should be.

## fy8-12-L2-05
**Given:** ten pulse counts in $10\,\text{s}$ periods: $52$, $45$, $49$, $57$, $44$, $48$, $51$, $42$, $50$ and $46$; the order of magnitude of the random variation is $\sqrt{N}$
**Asked:** the relative uncertainty of the total pulse count $N_\text{tot}$ as a percentage
**Principle:** The mean describes the typical pulse count in a period. The order of magnitude of the random variation of the number of pulses is $\sqrt{N}$, and the relative uncertainty is the share that the variation is of the pulse count. The more pulses are counted, the smaller the relative uncertainty.
**Formula:** $N_\text{mean} = \dfrac{N_\text{tot}}{10}$ and relative uncertainty $\dfrac{\sqrt{N_\text{tot}}}{N_\text{tot}}$
**Conversions:** Not needed: all periods are equally long. Finally the fraction is converted into a percentage: $1 = 100\,\%$.
**Substitution:** a) The sum is $N_\text{tot} = 484$, so $N_\text{mean} = \dfrac{484}{10} = 48.4$. b) $\sqrt{48.4} = 7.0$. Nine of the ten readings in the table are in the range $48.4 \pm 7.0$, that is $41.4$–$55.4$, and only $57$ is outside it; the difference between the largest and the smallest reading is $57 - 42 = 15$, which is about $2\sqrt{N}$. c) $\dfrac{\sqrt{484}}{484} = \dfrac{22}{484} = 0.04545 = 4.545\,\%$
**Answer:** $4.5\,\%$, two significant figures. The uncertainty of the total pulse count $484$ is about $\pm 22$ pulses. The uncertainty of a single period is relatively much greater: $\dfrac{7.0}{48.4} = 14\,\%$.
**Reasonableness:** There are ten times as many pulses as in one period, so the relative uncertainty decreases by the factor $\sqrt{10} = 3.16$: $14.4\,\% : 3.16 = 4.5\,\%$, as calculated. So a longer measurement gives a more accurate result.

## fy8-12-L2-06
**Given:** thicknesses of lead $d = 0$, $3$, $6$, $9$, $12$ and $15\,\text{mm}$ and pulses in $60\,\text{s}$ $1850$, $1290$, $890$, $640$, $440$ and $315$; pulse count of the background radiation $N_\text{t} = 50$
**Asked:** the half-value thickness $d_{1/2}$ of lead in millimetres (the mean of part c))
**Principle:** Lead attenuates only the radiation of the source, so the net pulse counts, that is the pulse counts from which the background has been subtracted, are substituted into the attenuation law. They are proportional to the intensity. Each measurement gives its own estimate of the half-value thickness, and the mean evens out the random variation of the pulses.
**Reading the graph:** The net pulse counts are $1800$, $1240$, $840$, $590$, $390$ and $265$. The points form a falling, curving line that does not cross the axis. Half of the original net pulse count is $900$. At the value $900$ the curve passes between the thicknesses $3\,\text{mm}$ ($1240$) and $6\,\text{mm}$ ($840$): linear interpolation gives $3\,\text{mm} + \dfrac{1240 - 900}{1240 - 840} \cdot 3\,\text{mm} = 5.6\,\text{mm}$. So the half-value thickness read from the graph is about $5.6\,\text{mm}$.
**Formula:** $N - N_\text{t} = (N_0 - N_\text{t}) \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, from which $d_{1/2} = \dfrac{d \cdot \ln 2}{\ln \tfrac{N_0 - N_\text{t}}{N - N_\text{t}}}$
**Conversions:** Not needed: the pulse counts are from periods of equal length and the thicknesses are in millimetres.
**Substitution:** At the thickness $3\,\text{mm}$: $d_{1/2} = \dfrac{3\,\text{mm} \cdot 0.69315}{\ln \tfrac{1800}{1240}} = \dfrac{2.0794\,\text{mm}}{0.37268} = 5.580\,\text{mm}$. Similarly at the thicknesses $6$, $9$, $12$ and $15\,\text{mm}$ one gets $5.457\,\text{mm}$, $5.593\,\text{mm}$, $5.439\,\text{mm}$ and $5.427\,\text{mm}$. The sum is $27.496\,\text{mm}$, so $d_{1/2} = \dfrac{27.496\,\text{mm}}{5} = 5.499\,\text{mm}$
**Answer:** $5.5\,\text{mm}$, two significant figures like the background and thickness values. The values vary between $5.4$ and $5.6\,\text{mm}$ because of the random variation of the pulses.
**Reasonableness:** The value is the same as the value of lead in the table, $5.5\,\text{mm}$, for the gamma radiation of caesium-137. Check: the thickness $15\,\text{mm}$ is about $2.7$ half-value thicknesses, and $1800 \cdot \left(\tfrac{1}{2}\right)^{2.7} = 277$ is close to the measured net $265$.

## fy8-12-L2-07
**Asked:** with which measurement beta and gamma radiation can be told apart most reliably
**Principle:** A beta particle has a range because it gives up its energy by ionising, and a few millimetres of aluminium stops it. Gamma radiation is attenuated layer by layer, and for example the half-value thickness of aluminium is tens of millimetres. A GM tube counts events but does not distinguish types of radiation.
**Model answer:** The types are told apart by comparing the net pulse count without a barrier and behind a thin aluminium plate. If the net pulse count drops almost to zero, the source is a beta source, because the plate stops beta particles. If the pulse count decreases only a little, the source is a gamma source, because a thin aluminium plate lets most of the gamma photons through. A sheet of paper does not distinguish the types, because it does not stop beta particles. A lead plate does not distinguish them, because it attenuates both, and the pulses of a GM tube are always the same size, so the type cannot be deduced from the height of the pulse.

## fy8-12-L3-04
**Given:** source caesium-137 ($662\,\text{keV}$), thicknesses $d = 0$, $6$, $12$, $18$, $24$ and $30\,\text{mm}$ and pulses in $60\,\text{s}$ $2640$, $1895$, $1330$, $950$, $685$ and $495$; background $N_\text{t} = 40$; half-value thicknesses of the table: lead $5.5\,\text{mm}$, iron $12\,\text{mm}$, aluminium $34\,\text{mm}$, concrete $39\,\text{mm}$, water $81\,\text{mm}$
**Asked:** the mean half-value thickness $d_{1/2}$ in millimetres, the material of the plates, the thickness that drops the net pulse count to one per cent, and why the thickest measurement is the most uncertain
**Principle:** A plate attenuates only the radiation of the source, not the background, so the background is subtracted first and the net pulse counts follow the attenuation law. The net pulse count of gamma radiation is halved by every layer of one half-value thickness and does not stop at a certain thickness. The range of beta particles is short, so their pulse count would drop almost to zero in a layer of a few millimetres. Each measurement gives its own estimate of the half-value thickness, and the material is identified by comparing the mean with the table.
**Reading the graph:** The net pulse counts are $2600$, $1855$, $1290$, $910$, $645$ and $455$. The net pulse count is halved at intervals of $12\,\text{mm}$: $2600 \to 1290$ at the thickness $12\,\text{mm}$ and $1290 \to 645$ at the thickness $24\,\text{mm}$. A steady halving is the attenuation of gamma radiation, and the curve is still clearly above zero at the thickness $30\,\text{mm}$, so it is not a matter of a range. So the radiation is gamma and not beta (part a).
**Formula:** $N - N_\text{t} = (N_0 - N_\text{t}) \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, from which $d_{1/2} = \dfrac{d \cdot \ln 2}{\ln \tfrac{N_0 - N_\text{t}}{N - N_\text{t}}}$; the thickness for a certain fraction $p$ is $d = d_{1/2} \cdot \dfrac{\ln (1 : p)}{\ln 2}$
**Conversions:** Not needed: the pulse counts are from periods of equal length and the thicknesses are in millimetres. The per cent is converted into a ratio: $1.0\,\% = 0.010$.
**Substitution:** At the thickness $6\,\text{mm}$: $d_{1/2} = \dfrac{6\,\text{mm} \cdot 0.69315}{\ln \tfrac{2600}{1855}} = \dfrac{4.1589\,\text{mm}}{0.33763} = 12.32\,\text{mm}$. Similarly at the thicknesses $12$, $18$, $24$ and $30\,\text{mm}$ one gets $11.87\,\text{mm}$, $11.88\,\text{mm}$, $11.93\,\text{mm}$ and $11.93\,\text{mm}$. The sum is $59.93\,\text{mm}$, so $d_{1/2} = \dfrac{59.93\,\text{mm}}{5} = 11.99\,\text{mm}$. In part c) $d = 11.99\,\text{mm} \cdot \dfrac{\ln 100}{\ln 2} = 11.99\,\text{mm} \cdot 6.644 = 79.6\,\text{mm}$.
**Answer:** $12.0\,\text{mm}$, three significant figures. The value is close to the half-value thickness of iron, $12\,\text{mm}$, and not to the values of the other materials in the table ($5.5\,\text{mm}$, $34\,\text{mm}$, $39\,\text{mm}$ or $81\,\text{mm}$), so the plates are iron. About $80\,\text{mm}$ of iron is needed to drop the net pulse count to one per cent.
**Reasonableness:** Check: at the thickness $24\,\text{mm}$ there are two half-value thicknesses, so the net pulse count should be $\tfrac{2600}{4} = 650$, and the measured $645$ is close. Dropping to one per cent requires $6.6$ half-value thicknesses, because $\left(\tfrac{1}{2}\right)^{6} = 1.6\,\%$ and $\left(\tfrac{1}{2}\right)^{7} = 0.78\,\%$; the thickness $79.6\,\text{mm}$ is between these. Justification of part d): with the thickest plate there are few pulses, so the random variation $\sqrt{495} = 22$ pulses is large relative to the net $455$, $\dfrac{22}{455} = 4.9\,\%$, whereas without a plate it is $\dfrac{\sqrt{2640}}{2600} = 2.0\,\%$. A longer measuring time increases the number of pulses, and the relative uncertainty decreases by the factor $\tfrac{1}{\sqrt{N}}$.

## fy8-12-L3-05
**Given:** thickness of the lead wall $d = 8.0\,\text{mm}$ and half-value thickness $d_{1/2} = 5.5\,\text{mm}$, geometric efficiency $\eta = 1.5\,\% = 0.015$, pulses of five $60\,\text{s}$ periods with the source $1010$, $987$, $1032$, $1001$ and $1020$ and without the source $24$, $29$, $22$, $27$ and $28$
**Asked:** the activity $A$ of the source in kilobecquerels
**Principle:** The background is subtracted first, and the net pulse rate tells how many photons per second hit the tube. Of the photons from the source only the fraction $\eta$ leaves in the direction of the tube, and the lead wall attenuates the photons according to the attenuation law. Activity is the number of decays per second, and by assumption each decay emits one photon, so the photons per second of the source are obtained by dividing the pulse rate by the fraction that reaches the tube.
**Formula:** $R = \dfrac{N_\text{s,mean} - N_\text{t,mean}}{t}$, the fraction passing through the wall $T = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$ and $R = A \cdot T \cdot \eta$, from which $A = \dfrac{R}{T \cdot \eta}$
**Conversions:** $t = 60\,\text{s}$ and $1.5\,\% = 0.015$. Finally $1\,\text{kBq} = 1000\,\text{Bq}$ and $1\,\text{Bq} = 1\,\tfrac{1}{\text{s}}$.
**Substitution:** a) With the source there are $5050$ pulses in total and without the source $130$, so the means are $\dfrac{5050}{5} = 1010$ and $\dfrac{130}{5} = 26$, and $R = \dfrac{1010 - 26}{60\,\text{s}} = \dfrac{984}{60\,\text{s}} = 16.4\,\tfrac{1}{\text{s}}$. b) $T = \left(\tfrac{1}{2}\right)^{8.0\,\text{mm} / 5.5\,\text{mm}} = \left(\tfrac{1}{2}\right)^{1.4545} = 0.3649$. c) $A = \dfrac{16.4\,\tfrac{1}{\text{s}}}{0.3649 \cdot 0.015} = \dfrac{16.4\,\tfrac{1}{\text{s}}}{0.005473} = 2997\,\text{Bq} = 3.0\,\text{kBq}$
**Answer:** $3.0\,\text{kBq}$, two significant figures like the thickness $8.0\,\text{mm}$ and the efficiency $1.5\,\%$. The net pulse rate is $16.4\,\tfrac{1}{\text{s}}$ (a), and about $36\,\%$ of the photons pass through the wall (b). In part d) the true activity is greater, because the tube does not count every photon and not every decay is accompanied by one photon.
**Reasonableness:** The wall contains $1.45$ half-value thicknesses, so the fraction passing through is between $\tfrac{1}{2}$ and $\tfrac{1}{4}$, like $0.36$. Calculating back: $3000\,\text{Bq} \cdot 0.365 \cdot 0.015 = 16.4\,\tfrac{1}{\text{s}}$, as measured. Justification of part d): a GM tube detects only a small fraction of gamma photons, so counting all the photons hitting the tube as pulses underestimates the decays; in addition, only about $85\,\%$ of the decays of caesium-137 emit a gamma photon. Both assumptions make the estimate too small.
