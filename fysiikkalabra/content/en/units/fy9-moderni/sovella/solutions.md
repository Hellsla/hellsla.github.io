## fy9-moderni-s1

### a)
**Given:** atomic number of caesium $55$, of barium $56$, mass number $137$, gamma photon energy $E = 662\,\text{keV}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Find:** the equations of the decay and the de-excitation, and the wavelength $\lambda$ of the gamma photon
**Principle:** In beta minus decay a neutron of the nucleus turns into a proton, so the atomic number increases by one and the mass number is conserved. The nucleus emits an electron and an antineutrino. The excited nucleus de-excites by emitting a gamma photon, and neither the atomic number nor the mass number changes (chapter *The atomic nucleus and radioactive decay*). Like light, a gamma photon is a photon whose energy and wavelength are linked (chapter *The photoelectric effect and the photon*).
**Formula:** ${}^{137}_{55}\text{Cs} \to {}^{137}_{56}\text{Ba}^{\ast} + {}^{0}_{-1}\text{e} + \bar{\nu}$ and ${}^{137}_{56}\text{Ba}^{\ast} \to {}^{137}_{56}\text{Ba} + \gamma$; $E = \dfrac{hc}{\lambda}$, so $\lambda = \dfrac{hc}{E}$
**Conversions:** $662\,\text{keV} = 662 \cdot 1000 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 1.0605 \cdot 10^{-13}\,\text{J}$ and finally $1\,\text{pm} = 10^{-12}\,\text{m}$
**Substitution:** $\lambda = \dfrac{6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s}}{1.0605 \cdot 10^{-13}\,\text{J}} = 1.873 \cdot 10^{-12}\,\text{m} = 1.873\,\text{pm}$
**Answer:** The equations are above. The wavelength of the gamma photon is $\lambda \approx 1.87\,\text{pm}$, three significant figures like the energy $662\,\text{keV}$.
**Reasonableness:** In both equations the mass numbers ($137 = 137 + 0$) and the charge numbers ($55 = 56 - 1$) are conserved. The wavelength is about a hundred times smaller than the diameter of an atom, as it should be for gamma radiation: a photon of visible light is about $2\,\text{eV}$ with a wavelength of about $600\,\text{nm}$, and $662\,000\,\text{eV}$ is about $330\,000$ times as much.

### b)
**Given:** $A_0 = 2400\,\tfrac{\text{Bq}}{\text{kg}}$ in 1990, half-life $T_{1/2} = 30.1\,\text{a}$, elapsed time $t = 2026 - 1990 = 36\,\text{a}$
**Find:** the concentration $A$ in 2026
**Principle:** The mushrooms contain an enormous number of caesium nuclei, and each decays with the same probability. That is why the number of remaining nuclei and the activity halve every half-life (chapter *The decay law and half-life*). By assumption no caesium leaves in any other way and none is added.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** The times are in the same unit, so no conversions are needed.
**Substitution:** $\dfrac{t}{T_{1/2}} = \dfrac{36\,\text{a}}{30.1\,\text{a}} = 1.196$, so $A = 2400\,\tfrac{\text{Bq}}{\text{kg}} \cdot 0.5^{1.196} = 1047.6\,\tfrac{\text{Bq}}{\text{kg}}$
**Answer:** $A \approx 1050\,\tfrac{\text{Bq}}{\text{kg}} = 1.05 \cdot 10^{3}\,\tfrac{\text{Bq}}{\text{kg}}$, three significant figures like the half-life.
**Reasonableness:** A little over one half-life has passed, so the concentration must be a little under half of the original, $1200\,\tfrac{\text{Bq}}{\text{kg}}$. The result is just that.

### c)
**Given:** concentration $1047.6\,\tfrac{\text{Bq}}{\text{kg}}$ (part b), mass eaten $m = 5.0\,\text{kg}$, dose coefficient $1.3 \cdot 10^{-8}\,\tfrac{\text{Sv}}{\text{Bq}}$, average annual dose $H_\text{a} = 5.9\,\text{mSv}$
**Find:** the effective dose $H$ and its share of the average annual dose
**Principle:** The dose coefficient tells how large an effective dose one becquerel taken into the body causes before the caesium leaves the body. The number of becquerels eaten is the concentration times the mass (chapter *Radiation dose and radiation safety in Finland*).
**Formula:** $H = A_m \cdot m \cdot k_\text{dose}$, where $A_m$ is the concentration and $k_\text{dose}$ the dose coefficient, and share $= \dfrac{H}{H_\text{a}} = \dfrac{A_m \cdot m \cdot k_\text{dose}}{H_\text{a}}$
**Conversions:** Finally $1\,\text{Sv} = 1000\,\text{mSv}$.
**Substitution:** $1047.6\,\tfrac{\text{Bq}}{\text{kg}} \cdot 5.0\,\text{kg} = 5238\,\text{Bq}$ is eaten, so $H = 5238\,\text{Bq} \cdot 1.3 \cdot 10^{-8}\,\tfrac{\text{Sv}}{\text{Bq}} = 6.81 \cdot 10^{-5}\,\text{Sv} = 6.81 \cdot 10^{-5} \cdot 1000\,\text{mSv} = 0.0681\,\text{mSv}$. The share is $0.0681\,\text{mSv} : 5.9\,\text{mSv} = 0.0115 = 1.15\,\%$.
**Answer:** The mushroom picker gets a dose of about $0.068\,\text{mSv}$ from the mushrooms, two significant figures like the mass $5.0\,\text{kg}$ and the dose coefficient. It is about $1\,\%$ of the average annual dose of a person in Finland.
**Reasonableness:** The dose equals about seven dental X-ray images, each with a dose of about $0.01\,\text{mSv}$. It is small compared with the average share of radon, about $3\,\text{mSv}$, which fits the fact that mushrooms are only a small source of dose in Finland.

### d)
**Given:** concentration $A = 1047.6\,\text{Bq}$ in one kilogram (part b), $T_{1/2} = 30.1\,\text{a}$, $1\,\text{a} = 3.156 \cdot 10^{7}\,\text{s}$, mass of an atom $m_\text{a} = 137\,\text{u}$, $1\,\text{u} = 1.66 \cdot 10^{-27}\,\text{kg}$
**Find:** the number $N$ of caesium-137 nuclei and their mass $m$
**Principle:** The activity is the product of the decay constant and the number of remaining nuclei, and the decay constant is obtained from the half-life (chapter *The decay law and half-life*). A becquerel is one decay per second, so the half-life is converted into seconds.
**Formula:** $A = \lambda N$ and $\lambda = \dfrac{\ln 2}{T_{1/2}}$, so $N = \dfrac{A\,T_{1/2}}{\ln 2}$; $m = N\,m_\text{a}$
**Conversions:** $30.1\,\text{a} = 30.1 \cdot 3.156 \cdot 10^{7}\,\text{s} = 9.500 \cdot 10^{8}\,\text{s}$, $m_\text{a} = 137\,\text{u} = 137 \cdot 1.66 \cdot 10^{-27}\,\text{kg} = 2.274 \cdot 10^{-25}\,\text{kg}$ and finally $1\,\text{kg} = 10^{12}\,\text{ng}$
**Substitution:** $N = \dfrac{1047.6\,\tfrac{1}{\text{s}} \cdot 9.500 \cdot 10^{8}\,\text{s}}{0.6931} = 1.436 \cdot 10^{12}$ and $m = 1.436 \cdot 10^{12} \cdot 2.274 \cdot 10^{-25}\,\text{kg} = 3.27 \cdot 10^{-13}\,\text{kg} = 0.327\,\text{ng}$
**Answer:** One kilogram of mushrooms contains about $1.44 \cdot 10^{12}$ caesium-137 nuclei, whose mass is about $0.327\,\text{ng}$, three significant figures like the half-life.
**Reasonableness:** There are trillions of nuclei, but the mass is under a nanogram, because a single atom is very light. The decay constant $\lambda = 7.30 \cdot 10^{-10}\,\tfrac{1}{\text{s}}$ is small, so a thousand decays per second need an enormous set of nuclei.

### Yleisiä virheitä
- In part a, in beta minus decay the atomic number is decreased or the mass number changed, or the antineutrino is forgotten.
- In part a, the energy is substituted in kiloelectronvolts into a formula with $h$ in joules.
- In part b, the activity is halved only once, because the time is “about one half-life”, or it is decreased linearly.
- In part c, multiplying by the mass is forgotten, or sieverts are converted into millisieverts the wrong way.
- In part d, the half-life is substituted in years, which gives $3.2 \cdot 10^{7}$ times too few nuclei (the number of seconds in a year).

## fy9-moderni-s2

### a)
**Given:** $E_n = -\tfrac{E_0}{n^2}$, $E_0 = 13.6\,\text{eV}$, transition from level $3$ to level $2$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Find:** the wavelength $\lambda$ of the line
**Principle:** When an electron moves from an upper level to a lower one, the atom emits a photon whose energy is the difference of the levels, because energy is conserved (chapter *Energy levels of the hydrogen atom and the Bohr model*). The wavelength is obtained from the photon energy (chapter *The photoelectric effect and the photon*).
**Formula:** $E_\text{f} = E_3 - E_2 = E_0\left(\tfrac{1}{2^2} - \tfrac{1}{3^2}\right)$ and $E_\text{f} = \dfrac{hc}{\lambda}$, so $\lambda = \dfrac{hc}{E_0\left(\tfrac{1}{2^2} - \tfrac{1}{3^2}\right)}$
**Conversions:** $1.8889\,\text{eV} = 1.8889 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.0260 \cdot 10^{-19}\,\text{J}$ and finally $1\,\text{nm} = 10^{-9}\,\text{m}$
**Substitution:** $E_3 - E_2 = 13.6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{9}\right) = 13.6\,\text{eV} \cdot \tfrac{5}{36} = 1.8889\,\text{eV}$, so $\lambda = \dfrac{6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s}}{3.0260 \cdot 10^{-19}\,\text{J}} = 6.565 \cdot 10^{-7}\,\text{m} = 656.5\,\text{nm}$
**Answer:** $\lambda \approx 656\,\text{nm}$, three significant figures like $13.6\,\text{eV}$.
**Reasonableness:** The result differs from the laboratory value $656.3\,\text{nm}$ by only $0.03\,\%$, and a photon of $1.9\,\text{eV}$ is red light, as the name of the line says.

### b)
**Given:** laboratory value $\lambda_0 = 656.3\,\text{nm}$, observed $\lambda = 671.8\,\text{nm}$, $c = 2.998 \cdot 10^{5}\,\text{km/s}$, $H_0 = 70\,\tfrac{\text{km/s}}{\text{Mpc}}$
**Find:** the recession speed $v$ and the distance $d$
**Principle:** Space expands, and distant galaxies recede from us. That is why the wavelength of their light has been stretched, and the redshift $z$ tells by how much. When $z$ is small, the recession speed is $v = cz$. By Hubble's law the speed is directly proportional to the distance (chapter *The evolution of the universe*).
**Formula:** $z = \dfrac{\lambda - \lambda_0}{\lambda_0}$, $v = cz$ and $v = H_0 d$, so $d = \dfrac{v}{H_0}$
**Conversions:** The wavelengths are in the same unit, and the speeds are in $\tfrac{\text{km}}{\text{s}}$, so no conversions are needed.
**Substitution:** $z = \dfrac{671.8\,\text{nm} - 656.3\,\text{nm}}{656.3\,\text{nm}} = \dfrac{15.5\,\text{nm}}{656.3\,\text{nm}} = 0.02362$, $v = 2.998 \cdot 10^{5}\,\text{km/s} \cdot 0.02362 = 7080\,\text{km/s}$ and $d = \dfrac{7080\,\text{km/s}}{70\,\tfrac{\text{km/s}}{\text{Mpc}}} = 101.1\,\text{Mpc}$
**Answer:** The galaxy recedes at the speed $v \approx 7080\,\text{km/s}$, three significant figures like the difference of the wavelengths $15.5\,\text{nm}$. It is at a distance of about $1.0 \cdot 10^{2}\,\text{Mpc}$, two significant figures like the Hubble constant.
**Reasonableness:** The speed is about $2\,\%$ of the speed of light, so $v = cz$ holds. $100\,\text{Mpc}$ is about $330$ million light years, which is beyond the nearby groups of galaxies but still a distance easily observed with a telescope.

### c)
**Given:** laboratory value of the cyan line $\lambda_0 = 486.1\,\text{nm}$, redshift $z = 0.02362$ (part b)
**Find:** the observed wavelength $\lambda$
**Principle:** The expansion of space stretches all wavelengths in the same ratio, so the redshift is the same for every line of the spectrum (chapter *The evolution of the universe*).
**Formula:** $z = \dfrac{\lambda - \lambda_0}{\lambda_0}$, so $\lambda = \lambda_0(1 + z)$
**Conversions:** The wavelength stays in nanometres, so no conversions are needed.
**Substitution:** $\lambda = 486.1\,\text{nm} \cdot (1 + 0.02362) = 497.58\,\text{nm}$
**Answer:** $\lambda \approx 497.6\,\text{nm}$, four significant figures like the laboratory value, because the shift $z$ is known to three figures and it changes only the last digits.
**Reasonableness:** The shift $11.5\,\text{nm}$ is smaller than the $15.5\,\text{nm}$ of the red line, because in the same ratio a shorter wavelength stretches by fewer nanometres. The calculated laboratory value $13.6\,\text{eV}\left(\tfrac{1}{4} - \tfrac{1}{16}\right)$ gives $486.3\,\text{nm}$, so the levels and the cyan line agree.

### d)
**Find:** why the hydrogen lines appear dark in the spectrum of the galaxy
**Principle:** A hot, dense body emits a continuous spectrum. A thin gas absorbs only photons whose energy is exactly the difference of two energy levels (chapters *Spectra reveal the energy levels of atoms* and *Energy levels of the hydrogen atom and the Bohr model*).
**Model answer:** The light of the galaxy is the light of its stars. The hot, dense surface of a star emits a continuous spectrum containing all wavelengths. The light passes through the outermost, thinner and cooler gas layers of the star, and these contain hydrogen. A hydrogen atom absorbs a photon only if the photon energy is exactly the difference of two energy levels, for example $E_3 - E_2 = 1.89\,\text{eV}$ for the red line. The atom is excited and soon de-excites by emitting a similar photon, but in a random direction. That is why less light comes in our direction at these wavelengths than at the neighbouring ones, and the lines appear dark as absorption lines. Bright lines would be seen if we looked at a thin hot gas without a continuous spectrum behind it, as in a gas discharge tube.

### Yleisiä virheitä
- In part a, the energy of one level is calculated, for example $|E_3| = 1.51\,\text{eV}$, instead of the difference of the levels.
- In part a, electronvolts are substituted into the formula together with $h$ in joules, which gives a wavelength of about $10^{-25}\,\text{m}$, about $10^{19}$ times too small.
- In part b, the redshift is calculated by dividing by the observed wavelength, or the division is forgotten, which gives $z = 15.5$.
- In part b, the speed is substituted in metres per second into Hubble's law, where $H_0$ is in $\tfrac{\text{km/s}}{\text{Mpc}}$.
- In part c, the same $15.5\,\text{nm}$ as for the red line is added to the cyan line, although what is the same is the relative change.
- In part d, the lines are said to be dark because the galaxy is far away or because the redshift darkens them.

### Hyväksytään myös
- In part c, the ratio $\lambda = 486.1\,\text{nm} \cdot \dfrac{671.8}{656.3} = 497.6\,\text{nm}$, because $1 + z$ is the ratio of the observed value to the laboratory value.

## fy9-moderni-s3

### a)
**Find:** the stopping voltage $U$ as a function of the frequency $f$ of the light as a graph
**Graph:** The frequency is calculated from the wavelength, $f = \tfrac{c}{\lambda}$: for example $\tfrac{2.998 \cdot 10^{8}\,\text{m/s}}{365 \cdot 10^{-9}\,\text{m}} = 8.214 \cdot 10^{14}\,\text{Hz}$. The frequencies are $8.214$, $7.402$, $6.876$, $6.379$ and $5.937$ times $10^{14}\,\text{Hz}$ for the wavelengths $365$–$505\,\text{nm}$. On the horizontal axis is $f\ (10^{14}\,\text{Hz})$ and on the vertical axis $U\ (\text{V})$. No point is plotted for the wavelength $590\,\text{nm}$, because no photocurrent arises at all, so there is no stopping voltage. The points are not joined into a broken line.

<svg data-fig="fy9-moderni-s3-p" viewBox="0 0 600 400" role="img" aria-label="Graph: the stopping voltage U in volts as a function of the frequency f of the light, the unit of the frequency axis 10 to the power 14 hertz. The horizontal axis starts at 5.0 and ends at 8.5, the vertical axis from zero to 1.4 volts. Five black points at frequencies 5.94–8.21 and voltages 0.21–1.15 volts rise steadily and lie roughly on the same straight line." style="max-width:100%;font-size:28px">
  <line x1="143.5" y1="340" x2="143.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="187" y1="340" x2="187" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230.5" y1="340" x2="230.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274.5" y1="340" x2="274.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318" y1="340" x2="318" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361.5" y1="340" x2="361.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="340" x2="405" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="301" x2="405" y2="301" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="261.5" x2="405" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="222.5" x2="405" y2="222.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="183.5" x2="405" y2="183.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="144.5" x2="405" y2="144.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="105" x2="405" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="66" x2="405" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="340" x2="419" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M431,340 L418,346 L418,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="341" x2="100" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,40 L106,53 L94,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143.5" y1="340" x2="143.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="187" y1="340" x2="187" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$6.0$</div></foreignObject>
  <line x1="230.5" y1="340" x2="230.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274.5" y1="340" x2="274.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="248.5" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$7.0$</div></foreignObject>
  <line x1="318" y1="340" x2="318" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="361.5" y1="340" x2="361.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="335.5" y="347" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$8.0$</div></foreignObject>
  <line x1="405" y1="340" x2="405" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="301" x2="100" y2="301" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="261.5" x2="100" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="244.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0.4$</div></foreignObject>
  <line x1="93" y1="222.5" x2="100" y2="222.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="183.5" x2="100" y2="183.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="166.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0.8$</div></foreignObject>
  <line x1="93" y1="144.5" x2="100" y2="144.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="105" x2="100" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="36" y="88" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1.2$</div></foreignObject>
  <line x1="93" y1="66" x2="100" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="437" y="323" width="158" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="90" y="7" width="71" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$U\ (\text{V})$</div></foreignObject>
  <circle cx="380" cy="115" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="309.5" cy="183.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="263.5" cy="220.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="220" cy="265.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="181.5" cy="299" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
</svg>

**Model answer:** The points rise steadily as the frequency increases and lie roughly on the same straight line. A larger frequency gives a larger stopping voltage, that is the electrons leave with a larger kinetic energy.

### b)
**Find:** a justification that a straight line fits the points, the fitted line and its extension to the axes
**Graph:** One photon gives all its energy $hf$ to one electron. Part of the energy is used for the work function $W$, and the fastest electron is left with the kinetic energy $E_\text{k,max} = hf - W$ (chapter *The photoelectric effect and the photon*). When the anode is more negative than the cathode, the electric field brakes the electron, and its kinetic energy turns into electric potential energy. The current stops when even the fastest electron stops just before the anode: $eU = E_\text{k,max}$ (chapter *Potential energy and potential in an electric field*). Combining these gives $eU = hf - W$, that is $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$, so $U$ is a linear function of the frequency with slope $\tfrac{h}{e}$ and constant term $-\tfrac{W}{e}$. The line is fitted between the points and extended as a dashed line to the vertical axis, because the constant term is needed to determine the work function (chapter *Graphing and fitting a straight line*).

<svg data-fig="fy9-moderni-s3-fit" viewBox="0 0 600 470" role="img" aria-label="Graph: the stopping voltage U in volts as a function of the frequency f of the light, the frequency axis from zero to 9 times 10 to the power 14 hertz and the voltage axis from minus 2.5 to plus 1.5 volts. A rising straight line has been fitted to five points and extended as a dashed line to the vertical axis. The line crosses the vertical axis at about minus 2.24 volts and the horizontal axis at about 5.43 times 10 to the power 14 hertz. The points used for reading are circled on the line: zero and minus 2.24 volts, and 8.0 times 10 to the power 14 hertz and 1.06 volts." style="max-width:100%;font-size:28px">
  <line x1="130.5" y1="410" x2="130.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164.5" y1="410" x2="164.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="199" y1="410" x2="199" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="233.5" y1="410" x2="233.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="267.5" y1="410" x2="267.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="302" y1="410" x2="302" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336.5" y1="410" x2="336.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370.5" y1="410" x2="370.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="410" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="367.5" x2="405" y2="367.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="325" x2="405" y2="325" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="282.5" x2="405" y2="282.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="240" x2="405" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="155" x2="405" y2="155" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="405" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="70" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="410" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="197.5" x2="419" y2="197.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M431,197.5 L418,203.5 L418,191.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="198.5" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="130.5" y1="197.5" x2="130.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="164.5" y1="197.5" x2="164.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="199" y1="197.5" x2="199" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="233.5" y1="197.5" x2="233.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="267.5" y1="197.5" x2="267.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="302" y1="197.5" x2="302" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="336.5" y1="197.5" x2="336.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370.5" y1="197.5" x2="370.5" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="405" y1="197.5" x2="405" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="410" x2="96" y2="410" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="367.5" x2="96" y2="367.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="350.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$-2$</div></foreignObject>
  <line x1="89" y1="325" x2="96" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="282.5" x2="96" y2="282.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="265.5" width="37" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$-1$</div></foreignObject>
  <line x1="89" y1="240" x2="96" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="61" y="180.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$0$</div></foreignObject>
  <line x1="89" y1="155" x2="96" y2="155" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="61" y="95.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:28px">$1$</div></foreignObject>
  <line x1="89" y1="70" x2="96" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="437" y="180.5" width="158" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="86" y="11" width="71" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$U\ (\text{V})$</div></foreignObject>
  <foreignObject x="153" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$2$</div></foreignObject>
  <foreignObject x="222" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$4$</div></foreignObject>
  <foreignObject x="290.5" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$6$</div></foreignObject>
  <foreignObject x="359" y="204.5" width="23" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$8$</div></foreignObject>
  <polyline points="291,188.5 388.5,89.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,388 291,188.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="378" cy="100" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="350" cy="129.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332" cy="145.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="315" cy="165" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="300" cy="179.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="96" cy="388" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="370.5" cy="107.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="370.5" y1="107.5" x2="370.5" y2="410" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="107.5" x2="370.5" y2="107.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="282.5" cy="197.5" r="6" fill="#2b8a3e"/>
  <foreignObject x="252.5" y="253" width="226" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$f_0 \approx 5.43 \cdot 10^{14}\,\text{Hz}$</span></div></foreignObject>
  <foreignObject x="108" y="371" width="154" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-\tfrac{W}{e} \approx -2.24\,\text{V}$</span></div></foreignObject>
  <foreignObject x="247" y="299.5" width="52" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:28px">$k = \tfrac{h}{e}$</div></foreignObject>
</svg>

**Model answer:** According to the model $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$, the points should lie on a straight line, and indeed they lie on the same line to within about $0.01\,\text{V}$. The fitted line crosses the vertical axis at about $-2.24\,\text{V}$ and the horizontal axis at about $5.43 \cdot 10^{14}\,\text{Hz}$. The extension of the line to negative voltages is only a mathematical aid: at frequencies below the threshold frequency no electrons leave at all.

### c)
**Given:** the fitted line of part b, $e = 1.602 \cdot 10^{-19}\,\text{C}$
**Find:** the Planck constant $h$ and its comparison with the value $6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$
**Principle:** According to the model $U = \tfrac{h}{e}\,f - \tfrac{W}{e}$, the slope of the line is $k = \tfrac{h}{e}$. The slope is read from two points of the fitted line far apart, not from the measurement points (chapter *Graphing and fitting a straight line*).
**Reading the graph:** The points $(0;\ -2.24\,\text{V})$ and $(8.0 \cdot 10^{14}\,\text{Hz};\ 1.06\,\text{V})$ are read from the line.
**Formula:** $k = \dfrac{\Delta U}{\Delta f}$ and $k = \dfrac{h}{e}$, so $h = ek$
**Conversions:** $1\,\text{C} \cdot 1\,\text{V} \cdot 1\,\text{s} = 1\,\text{J}\,\text{s}$, because $1\,\text{V} = 1\,\tfrac{\text{J}}{\text{C}}$ and $\tfrac{1}{\text{Hz}} = 1\,\text{s}$.
**Substitution:** $k = \dfrac{1.06\,\text{V} - (-2.24\,\text{V})}{8.0 \cdot 10^{14}\,\text{Hz} - 0} = \dfrac{3.30\,\text{V}}{8.0 \cdot 10^{14}\,\tfrac{1}{\text{s}}} = 4.125 \cdot 10^{-15}\,\text{V}\,\text{s}$, so $h = 1.602 \cdot 10^{-19}\,\text{C} \cdot 4.125 \cdot 10^{-15}\,\text{V}\,\text{s} = 6.608 \cdot 10^{-34}\,\text{J}\,\text{s}$
**Answer:** $h \approx 6.61 \cdot 10^{-34}\,\text{J}\,\text{s}$, three significant figures, because the voltages are read from the graph to about a hundredth of a volt. The result is $0.3\,\%$ smaller than the table value $6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$.
**Reasonableness:** The difference is much smaller than the reading uncertainty, about $1\,\%$, so the measurement supports the model. The slope does not depend on the material of the cathode, so any metal would give the same $h$.

### d)
**Given:** the line of part b, which crosses the vertical axis at $b = -2.24\,\text{V}$, slope $k = 4.125 \cdot 10^{-15}\,\text{V}\,\text{s}$ (part c), $\lambda = 590\,\text{nm}$
**Find:** the work function $W$ in electronvolts, the threshold frequency $f_0$ and an explanation of the result at the wavelength $590\,\text{nm}$
**Principle:** The constant term of the line is $-\tfrac{W}{e}$, so the work function in electronvolts is the absolute value of the constant term. At the threshold frequency the photon energy is just enough for the work function and $U = 0$, so it is where the line crosses the horizontal axis. The intensity of the light changes only the number of photons, not the energy of one photon (chapter *The photoelectric effect and the photon*).
**Reading the graph:** The line crosses the vertical axis at $-2.24\,\text{V}$ and the horizontal axis at about $5.43 \cdot 10^{14}\,\text{Hz}$.
**Formula:** $b = -\dfrac{W}{e}$, so $W = -e\,b$; $hf_0 = W$, so $f_0 = \dfrac{W}{h} = -\dfrac{b}{k}$, because $k = \dfrac{h}{e}$; $f = \dfrac{c}{\lambda}$ and $E = hf$
**Conversions:** $e \cdot 1\,\text{V} = 1\,\text{eV}$, so $W = 2.24\,\text{eV}$ directly. The wavelength $590\,\text{nm} = 590 \cdot 10^{-9}\,\text{m}$, and the energy is converted into electronvolts by dividing by $1.602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}}$.
**Substitution:** $W = -e \cdot (-2.24\,\text{V}) = 2.24\,\text{eV}$ and $f_0 = -\dfrac{-2.24\,\text{V}}{4.125 \cdot 10^{-15}\,\text{V}\,\text{s}} = 5.43 \cdot 10^{14}\,\text{Hz}$. At the wavelength $590\,\text{nm}$: $f = \dfrac{2.998 \cdot 10^{8}\,\text{m/s}}{590 \cdot 10^{-9}\,\text{m}} = 5.08 \cdot 10^{14}\,\text{Hz}$ and $E = \dfrac{6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 5.08 \cdot 10^{14}\,\tfrac{1}{\text{s}}}{1.602 \cdot 10^{-19}\,\tfrac{\text{J}}{\text{eV}}} = 2.10\,\text{eV}$
**Answer:** The work function of potassium is $W \approx 2.24\,\text{eV}$ and the threshold frequency $f_0 \approx 5.43 \cdot 10^{14}\,\text{Hz}$, three significant figures by the reading accuracy of the graph. The frequency $5.08 \cdot 10^{14}\,\text{Hz}$ of light of wavelength $590\,\text{nm}$ is below the threshold frequency, that is the energy $2.10\,\text{eV}$ of one photon is not enough to free an electron. Ten times as much light means ten times as many photons of the same kind. One photon gives its energy to one electron, so still no electrons leave, and no photocurrent arises.
**Reasonableness:** The threshold frequency corresponds to the wavelength $\tfrac{c}{f_0} \approx 552\,\text{nm}$, green light, so yellow $590\,\text{nm}$ light is on the wrong side of the limit and all the measured violet and blue wavelengths on the right side, as in the table. The work functions of the alkali metals are about $2\,\text{eV}$, so the result is credible.

### Yleisiä virheitä
- In part a, the wavelength is plotted on the horizontal axis, so the points are not on a straight line, or the points are joined into a broken line.
- In part a, a point $U = 0$ is plotted for the wavelength $590\,\text{nm}$, although no current arises at all.
- In part b, the line is forced through the origin, so the work function cannot be determined.
- In part c, the slope is read from two measurement points and not from the fitted line, or $10^{14}$ is forgotten, which gives $h \approx 6.6 \cdot 10^{-20}\,\text{J}\,\text{s}$.
- In part d, the work function is given as negative or in joules, although electronvolts are asked for.
- In part d, it is claimed that brighter light frees electrons because there is more energy.

### Hyväksytään myös
- In part c, a fit with a calculator or spreadsheet: $k = 4.13 \cdot 10^{-15}\,\text{V}\,\text{s}$, $h = 6.61 \cdot 10^{-34}\,\text{J}\,\text{s}$ and constant term $-2.24\,\text{V}$.
- In part d, the threshold frequency from the equation of the line $f_0 = \tfrac{W}{h}$ with the value of part c, or directly from where the line crosses the horizontal axis.

## fy9-moderni-s4

### a)
**Find:** whether claim 1 is true and how radon causes a radiation dose
**Principle:** An alpha particle is heavy and doubly charged, so it ionises densely and loses its energy over a short distance: a few centimetres in air and less than a tenth of a millimetre in tissue. External alpha radiation is stopped by the dead surface layer of the skin, but inside the body an alpha particle hits living cells directly. That is why its radiation weighting factor is $20$ (chapter *Ionising radiation and the body*). Radon is a gas, and its short-lived decay products are solids that stick to dust particles in the air (chapter *Radiation dose and radiation safety in Finland*).
**Model answer:** The first part of the claim is true: the alpha radiation of radon does not pass through paper or skin, so radon in the air of the room does not irradiate the skin dangerously from outside. The conclusion is still false. Radon and its decay products, isotopes of polonium, lead and bismuth, are breathed into the lungs, and the decay products stick to the surface of the bronchi. There their alpha particles hit the cells of the lungs directly. An alpha particle gives up all its energy, several megaelectronvolts, over a distance of a few cells and can break both strands of DNA. That is why the equivalent dose of the same absorbed dose is $20$ times that of photon radiation. Radon is the largest single source of radiation dose in Finland and, after smoking, the most common cause of lung cancer. The $450\,\tfrac{\text{Bq}}{\text{m}^3}$ of the flat exceeds the reference level $300\,\tfrac{\text{Bq}}{\text{m}^3}$ by a factor of $1.5$, so remedial measures are worthwhile.

### b)
**Find:** whether claim 2 is true, what fraction of the radon nuclei is undecayed after a month, and whether the radon disappears
**Principle:** A large set of radon nuclei decays according to the decay law, and the fraction left is $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ (chapter *The decay law and half-life*). The law applies only to the nuclei that are in the room at the start. New radon nuclei form all the time from radium in the uranium decay series of the soil, and they flow in through cracks in the foundations (chapter *Radiation dose and radiation safety in Finland*).
**Model answer:** A month, $30\,\text{d}$, is $\tfrac{30\,\text{d}}{3.8\,\text{d}} = 7.89$ half-lives, so of the radon nuclei that were in the room at the start $\left(\tfrac{1}{2}\right)^{7.89} = 0.0042$ is left, that is about $0.4\,\%$. The calculation is correct, but the claim is still false. The parent of radon, radium-226, whose half-life is about $1600$ years, and the start of the decay series, uranium-238, are in the soil and bedrock, so radon forms again all the time. When warm indoor air rises and leaves, a lower pressure arises in the lower part of the house, which draws radon-rich air from the soil in through the cracks in the foundations. With the windows shut, as much radon decays as comes in, and the concentration settles at a high level. In a tightly closed flat the concentration usually increases, because the air is exchanged less. The concentration is reduced by improving the ventilation, sealing the cracks in the foundations and installing a radon extraction fan, which draws the air from under the house outside.

### c)
**Find:** whether claim 3 is true
**Principle:** Radioactivity is a property of unstable nuclei: the nucleus decays and emits radiation. X-rays are photon radiation that is produced in an X-ray tube only while there is a voltage across the tube (chapter *Radiation in medicine and technology*). The energy of an X-ray photon, about $60\,\text{keV}$, is enough to ionise atoms but too small to change nuclei (chapter *Ionising radiation and the body*).
**Model answer:** The claim is false. At the dental X-ray the neighbour was briefly exposed to external X-rays. Each photon either passed through the tissue to the image plate or was absorbed and ionised an atom during the imaging. No photons stay in the body, and their energy, about $60\,\text{keV}$, is not enough to make atomic nuclei unstable, since the binding energies of the particles of the nucleus are of the order of megaelectronvolts. When the unit switches off, there is no radiation any more, and as far as radiation goes the neighbour is exactly the same as before. A person can be a radiation source for a short time only if radioactive material is put into the body, such as the tracer of a nuclear medicine examination or in radioiodine treatment of the thyroid. Then the hospital gives instructions. So the children do not need to avoid the neighbour. In addition, the dose of a dental X-ray image, about $0.01\,\text{mSv}$, is small compared with the dose from the radon of the flat.

### Yleisiä virheitä
- In part a, alpha radiation is said to be harmless or dangerous without distinguishing external radiation from inhaled decay products.
- In part b, it is calculated that the amount halves once in a month, or that everything decays in $2 \cdot 3.8\,\text{d}$.
- In part b, it is concluded that the radon disappears because the calculation gives less than $1\,\%$, without noticing that more radon forms all the time.
- In part c, radiation and radioactive material are mixed up, or it is claimed that X-rays “stay in the body”.

## fy9-moderni-s5

### a)
**Given:** counts in $10\,\text{s}$ periods at the times $0$–$300\,\text{s}$ ($11$ readings), $398$ at the start and $104$ at the end, background $5$ counts in $10\,\text{s}$
**Find:** the half-life $T_{1/2}$ taking the background radiation into account
**Principle:** The GM tube counts the pulses of both the sample and the background radiation, so the share of the sample is obtained by subtracting the background from each reading. The count of the sample is proportional to the activity, and the activity of a large set of nuclei decreases according to the decay law, because each nucleus decays with the same probability (chapter *The decay law and half-life*). All $11$ points are used by fitting a line, because a single reading varies randomly.
**Reading the graph:** After subtracting the background, $\ln N$ is calculated for all $11$ readings ($N$ counts in $10\,\text{s}$, for example $\ln 393 = 5.974$ and $\ln 99 = 4.595$), and the points $(t,\ \ln N)$ are plotted as points. Exponential decrease is a straight line in $\ln N$, so one line is fitted to the points over the whole range $0$–$300\,\text{s}$. The slope $k$ is read from two points of the fitted line far apart, for example $(0;\ 5.993)$ and $(300\,\text{s};\ 4.635)$, not from individual measurement points.
**Formula:** $N = N_0 e^{-\lambda t}$, so $\ln N = \ln N_0 - \lambda t$. The slope of the line is $k = -\lambda$, and $T_{1/2} = \dfrac{\ln 2}{\lambda}$, so $T_{1/2} = \dfrac{\ln 2}{-k}$, where $k = \dfrac{\Delta(\ln N)}{\Delta t}$
**Conversions:** All the counts are in the same unit, counts in $10\,\text{s}$, and $\ln N$ is a pure number, so no conversions are needed.
**Substitution:** The slope of the fitted line is $k = \dfrac{4.635 - 5.993}{300\,\text{s} - 0\,\text{s}} = -4.528 \cdot 10^{-3}\,\tfrac{1}{\text{s}}$, so $T_{1/2} = \dfrac{0.6931}{4.528 \cdot 10^{-3}\,\tfrac{1}{\text{s}}} = 153.1\,\text{s}$
**Answer:** $T_{1/2} \approx 153\,\text{s}$, three significant figures, but the random variation of the counts makes the last digit uncertain. Without subtracting the background the fit would give $157\,\text{s}$; the fit uses all the points.
**Reasonableness:** The two-endpoint calculation $T_{1/2} = \dfrac{t \ln 2}{\ln (N_0 : N)} = \dfrac{300\,\text{s} \cdot 0.6931}{\ln (393 : 99)} = 151\,\text{s}$ differs from the fit by only $1.5\,\%$. The count has fallen from $393$ to about $99$ in $300\,\text{s}$, roughly a quarter, and two half-lives would give $\tfrac{393}{4} \approx 98$, so $T_{1/2} \approx \tfrac{300\,\text{s}}{2} = 150\,\text{s}$ is of the right order.

### b)
**Find:** an assessment of the group's conclusion
**Principle:** A nucleus has no memory and no age: each barium-137m nucleus decays with the same probability per second, however long it has existed (chapter *The decay law and half-life*). The count of a GM tube varies randomly by about $\sqrt{N}$ (chapter *Measuring and the reliability of a measurement*).
**Model answer:** The group's explanation is wrong. Standing for a minute reduces the activity of the sample but does not change the half-life, because the remaining nuclei decay with exactly the same probability as before. The difference comes from the method. The group read the half-life between one pair of points, and a single reading varies randomly: the uncertainty of the reading of $212$ counts is about $\sqrt{212} \approx 15$ counts, that is $7\,\%$. The reading at $150\,\text{s}$ happens to be large, which shifts the reading later. Ignoring the background was also a mistake. At the start the background is only $1\,\%$ of the reading, but at the end already $5\,\%$, and a background left unsubtracted apparently slows down the decrease and lengthens the half-life. In addition, the background was measured only once for $10\,\text{s}$, so its value $5 \pm 2$ is very imprecise. The conclusion “$166\,\text{s}$” is therefore not reliable. All the points after subtracting the background give about $153\,\text{s}$, which matches the book value.

### c)
**Find:** how the measurement and the processing of the results can be improved
**Principle:** The random error decreases when more pulses are counted or the measurement is repeated, and a systematic error is removed by correcting its cause. All the measurement points are used by fitting a model (chapters *Your own experimental investigation: planning, carrying out and reporting* and *Graphing and fitting a straight line*).
**Model answer:** The background is measured for a long time before and after the measurement, for example $10\,\text{min}$, so that about $300$ counts accumulate and the uncertainty of the background is about $6\,\%$ and not $45\,\%$. The background is converted into the same unit, counts in $10\,\text{s}$, and subtracted from each reading. The counting time can be lengthened, for example to $20\,\text{s}$, and measurements made more often, so that the relative uncertainty of a single reading decreases. All the points are used: $\ln(N - N_\text{bg})$ is plotted against time, and the slope of the line is $-\tfrac{\ln 2}{T_{1/2}}$, or the model $N = A\,e^{-Ct} + B$, in which the constant $B$ is the background, is fitted with a calculator. The measurement is repeated with a new sample and the results compared, so that the spread can be seen. The distance of the sample from the GM tube is kept the same throughout. The result is given with its uncertainty, for example $T_{1/2} = (152 \pm 4)\,\text{s}$.

### Yleisiä virheitä
- In part a, the background is not subtracted, or it is subtracted only from the first reading.
- In part a, the half-life is read directly by linear interpolation, as if the decrease were steady.
- In part b, the group's explanation about “older nuclei” is accepted, or only calculation errors are assessed without mentioning random variation.
- In part c, only “a more accurate meter” is suggested without saying what changes in the measurement and why.

### Hyväksytään myös
- in part a the two-endpoint calculation after subtracting the background: $T_{1/2} = \dfrac{t \ln 2}{\ln (N_0 : N)} \approx 151\,\text{s}$.
- In part a, some other pair of points far apart after subtracting the background, as long as the result is between $147$ and $159\,\text{s}$.

## fy9-moderni-s6

### a)
**Given:** electric power $P_\text{e} = 1600\,\text{MW}$, thermal power $P_\text{th} = 4300\,\text{MW}$, energy per fission $E_\text{f} = 200\,\text{MeV}$
**Find:** the efficiency $\eta$ and the number of fissions per second $n$
**Principle:** The efficiency is the ratio of the useful power to the power used (chapter *Energy production and the efficiency of power plants*). The thermal power of the reactor is the energy of one fission times the number of fissions per second (chapter *Fission, fusion and nuclear power*).
**Formula:** $\eta = \dfrac{P_\text{e}}{P_\text{th}}$ and $P_\text{th} = nE_\text{f}$, so $n = \dfrac{P_\text{th}}{E_\text{f}}$
**Conversions:** $200\,\text{MeV} = 200 \cdot 10^{6} \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.204 \cdot 10^{-11}\,\text{J}$ and $4300\,\text{MW} = 4300 \cdot 10^{6}\,\text{W}$
**Substitution:** $\eta = \dfrac{1600\,\text{MW}}{4300\,\text{MW}} = 0.3721 = 37.21\,\%$ and $n = \dfrac{4300 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}}}{3.204 \cdot 10^{-11}\,\text{J}} = 1.342 \cdot 10^{20}\,\tfrac{1}{\text{s}}$
**Answer:** The efficiency is $\eta \approx 37.2\,\%$, and about $1.34 \cdot 10^{20}$ fissions happen in the reactor per second, three significant figures like the powers.
**Reasonableness:** The efficiency of a thermal power plant with a steam turbine is typically $30$–$40\,\%$. There are enormous numbers of fissions, because one fission releases only about $3 \cdot 10^{-11}\,\text{J}$.

### b)
**Given:** $n = 1.342 \cdot 10^{20}\,\tfrac{1}{\text{s}}$ (part a), $1\,\text{a} = 3.156 \cdot 10^{7}\,\text{s}$, mass of a uranium-235 atom $m_\text{U} = 235\,\text{u}$, $1\,\text{u} = 1.661 \cdot 10^{-27}\,\text{kg}$, $P_\text{th} = 4300\,\text{MW}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Find:** the mass $m$ of uranium-235 that undergoes fission in a year and the mass $\Delta m$ converted into energy
**Principle:** Each fission uses up one uranium-235 nucleus. The released energy corresponds to the mass defect: the mass of the reaction products is smaller than that of the reactants (chapters *Mass defect and nuclear binding energy* and *Fission, fusion and nuclear power*).
**Formula:** $m = n t\,m_\text{U}$ and $E = \Delta m\,c^2$, so $\Delta m = \dfrac{P_\text{th}t}{c^2}$
**Conversions:** $m_\text{U} = 235\,\text{u} = 235 \cdot 1.661 \cdot 10^{-27}\,\text{kg} = 3.903 \cdot 10^{-25}\,\text{kg}$
**Substitution:** $nt = 1.342 \cdot 10^{20}\,\tfrac{1}{\text{s}} \cdot 3.156 \cdot 10^{7}\,\text{s} = 4.236 \cdot 10^{27}$, so $m = 4.236 \cdot 10^{27} \cdot 3.903 \cdot 10^{-25}\,\text{kg} = 1653\,\text{kg}$. $\Delta m = \dfrac{4300 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}} \cdot 3.156 \cdot 10^{7}\,\text{s}}{(2.998 \cdot 10^{8}\,\text{m/s})^2} = \dfrac{1.357 \cdot 10^{17}\,\text{J}}{8.988 \cdot 10^{16}\,\tfrac{\text{m}^2}{\text{s}^2}} = 1.51\,\text{kg}$
**Answer:** About $1650\,\text{kg}$ of uranium-235 undergoes fission in a year, and about $1.51\,\text{kg}$ of mass is converted into energy, three significant figures like the powers.
**Reasonableness:** Only $1.51 : 1653 \approx 0.09\,\%$ of the mass of the uranium is converted into energy, which is the same as $200\,\text{MeV}$ divided by the rest energy of a uranium atom, $235 \cdot 931.5\,\text{MeV}$. The rest of the mass remains as fission products and neutrons, because the number of nucleons is conserved.

### c)
**Given:** $P_\text{th} = 4300\,\text{MW}$, $P_\text{e} = 1600\,\text{MW}$, specific heat capacity of seawater $c_\text{w} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, temperature rise $\Delta T = 11\,\text{K}$
**Find:** the mass flow rate of seawater $\tfrac{m}{t}$
**Principle:** Energy is conserved: the part of the reactor's thermal power that does not become electricity goes to the seawater in the condenser (chapter *Energy production and the efficiency of power plants*). The heat needed to warm the water is $Q = c_\text{w}m\Delta T$ (chapter *Internal energy, heat and conservation of energy*).
**Formula:** $P_\text{th} - P_\text{e} = \dfrac{Q}{t} = c_\text{w}\dfrac{m}{t}\Delta T$, so $\dfrac{m}{t} = \dfrac{P_\text{th} - P_\text{e}}{c_\text{w}\Delta T}$
**Conversions:** $4300\,\text{MW} - 1600\,\text{MW} = 2700\,\text{MW} = 2700 \cdot 10^{6}\,\text{W}$
**Substitution:** $\dfrac{m}{t} = \dfrac{2700 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 11\,\text{K}} = 58\,581\,\tfrac{\text{kg}}{\text{s}}$
**Answer:** About $5.9 \cdot 10^{4}\,\tfrac{\text{kg}}{\text{s}}$ of seawater must be pumped, two significant figures like the temperature rise $11\,\text{K}$.
**Reasonableness:** That is about $59\,\text{m}^3$ per second, the flow of a medium-sized river. The cooling water of a large nuclear power plant really is of this order, and in winter the heat shows as an open water area in front of the plant.

### d)
**Given:** electric power $P_\text{e} = 1600\,\text{MW}$, $t = 1\,\text{a} = 3.156 \cdot 10^{7}\,\text{s}$, heat of combustion of hard coal $H = 24\,\tfrac{\text{MJ}}{\text{kg}}$, efficiency of the coal power plant $\eta_\text{c} = 40\,\%$
**Find:** the mass $m_\text{c}$ of hard coal burned in a year
**Principle:** The coal power plant produces the same electrical energy, but only $40\,\%$ of the energy of the fuel becomes electricity (chapter *Energy production and the efficiency of power plants*). The energy of the fuel is the heat of combustion times the mass (chapter *Fuels and heat of combustion*).
**Formula:** $E_\text{e} = P_\text{e}t$, $\eta_\text{c}Hm_\text{c} = E_\text{e}$, so $m_\text{c} = \dfrac{P_\text{e}t}{\eta_\text{c}H}$
**Conversions:** $1600\,\text{MW} = 1600 \cdot 10^{6}\,\text{W}$, $24\,\tfrac{\text{MJ}}{\text{kg}} = 24 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}}$ and finally $1\,\text{t} = 1000\,\text{kg}$
**Substitution:** $E_\text{e} = 1600 \cdot 10^{6}\,\tfrac{\text{J}}{\text{s}} \cdot 3.156 \cdot 10^{7}\,\text{s} = 5.050 \cdot 10^{16}\,\text{J}$, so $m_\text{c} = \dfrac{5.050 \cdot 10^{16}\,\text{J}}{0.40 \cdot 24 \cdot 10^{6}\,\tfrac{\text{J}}{\text{kg}}} = 5.26 \cdot 10^{9}\,\text{kg} = 5.26 \cdot 10^{6}\,\text{t}$
**Answer:** The coal power plant would burn about $5.3 \cdot 10^{6}\,\text{t}$, that is five million tonnes of hard coal a year, two significant figures like the heat of combustion and the efficiency.
**Reasonableness:** The amount is about three million times the mass of the uranium-235 that undergoes fission, because one fission releases about $200\,\text{MeV}$, while burning one carbon atom releases only a few electronvolts. It is about $14\,000$ tonnes a day, hundreds of railway wagons.

### Yleisiä virheitä
- In part a, the efficiency is calculated the wrong way round, $\tfrac{4300}{1600}$, or the megaelectronvolts are not converted into joules.
- In part b, $\Delta m$ is taken as the mass, that is it is claimed that all the fuel turns into energy, or $\Delta m$ is calculated from the electrical energy instead of the thermal energy.
- In part c, the whole thermal power $4300\,\text{MW}$ or the electric power $1600\,\text{MW}$ is taken as the power going to the seawater.
- In part d, the efficiency is multiplied by instead of divided by, which gives $6.25$ times too little coal, or the kilograms are not converted into tonnes.
