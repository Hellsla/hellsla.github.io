## fy9-magnetismi-valo-s1

### a)
**Given:** turns $N = 60$, area $A = 0.060\,\text{m}^2$, magnetic flux density $B = 0.50\,\text{T}$, rotation frequency $f = 50\,\text{Hz}$
**Find:** the peak value $e_0$ and the rms value $U$ of the voltage
**Principle:** When a coil rotates steadily in a uniform field, the flux through it varies periodically, and by the law of induction a sinusoidal voltage is induced in the coil. The voltage is at its peak when the plane of the coil is parallel to the field, because the flux then changes fastest (chapters *Electromagnetic induction* and *The generator and alternating current*). The rms value is the direct voltage that would give the same average power in a resistor; for a sinusoidal voltage it is the peak value divided by $\sqrt{2}$.
**Formula:** $e_0 = NBA \cdot 2\pi f$ and $U = \dfrac{e_0}{\sqrt{2}}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $e_0 = 60 \cdot 0.50\,\text{T} \cdot 0.060\,\text{m}^2 \cdot 2\pi \cdot 50\,\tfrac{1}{\text{s}} = 565.5\,\text{V}$ and $U = \dfrac{565.5\,\text{V}}{\sqrt{2}} = 399.9\,\text{V}$
**Answer:** The peak value is $e_0 \approx 570\,\text{V}$ and the rms value $U \approx 400\,\text{V}$, two significant figures like the magnetic flux density $0.50\,\text{T}$ and the area $0.060\,\text{m}^2$.
**Reasonableness:** The units match: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. The rms value is smaller than the peak value, as it should be, and $400\,\text{V}$ is a common industrial voltage.

### b)
**Given:** rms voltage of the generator $U_1 = 400\,\text{V}$, line voltage $U_2 = 20.0\,\text{kV}$, power $P = 150\,\text{kW}$; the transformer is ideal
**Find:** the turns ratio $N_2 : N_1$ and the currents $I_1$ and $I_2$
**Principle:** In an ideal transformer the ratio of the voltages is the ratio of the numbers of turns, and power is conserved: $U_1 I_1 = U_2 I_2$ (chapter *The transformer and the transmission of electrical energy*). When the voltage increases, the current decreases in the same ratio. The voltages and currents are rms values, so $P = UI$.
**Formula:** $\dfrac{N_2}{N_1} = \dfrac{U_2}{U_1}$, $I_1 = \dfrac{P}{U_1}$ and $I_2 = \dfrac{P}{U_2}$
**Conversions:** $20.0\,\text{kV} = 20.0 \cdot 1000\,\text{V} = 20\,000\,\text{V}$ and $150\,\text{kW} = 150 \cdot 1000\,\text{W} = 150\,000\,\text{W}$
**Substitution:** $\dfrac{N_2}{N_1} = \dfrac{20\,000\,\text{V}}{400\,\text{V}} = 50$, $I_1 = \dfrac{150\,000\,\text{W}}{400\,\text{V}} = 375\,\text{A}$ and $I_2 = \dfrac{150\,000\,\text{W}}{20\,000\,\text{V}} = 7.50\,\text{A}$
**Answer:** The secondary coil has $50$ times as many turns as the primary coil. On the generator side the current is $I_1 \approx 375\,\text{A}$ and in the line $I_2 \approx 7.50\,\text{A}$, three significant figures like the voltage $20.0\,\text{kV}$ and the power $150\,\text{kW}$.
**Reasonableness:** The ratio of the currents $375 : 7.50 = 50$ is the same as the turns ratio, and $U_2 I_2 = 20\,000\,\text{V} \cdot 7.50\,\text{A} = 150\,\text{kW}$, the same as in the primary.

### c)
**Given:** line current $I_2 = 7.50\,\text{A}$ (part b), resistance $R = 6.0\,\Omega$, power $P = 150\,\text{kW}$; for comparison the voltage $400\,\text{V}$
**Find:** the fraction $\tfrac{P_\text{h}}{P}$ of the power that turns into heat, and what would happen at the voltage $400\,\text{V}$
**Principle:** In the resistance of the line electrical energy turns into internal energy at the rate $RI^2$. The transmission voltage $20\,\text{kV}$ is not across the resistance of the line, so the loss is calculated from the current, which is obtained from the transmitted power (chapter *The transformer and the transmission of electrical energy*).
**Formula:** $I = \dfrac{P}{U}$ and $P_\text{h} = RI^2$, fraction $\dfrac{P_\text{h}}{P}$
**Conversions:** Finally the fraction as a percentage: multiply by $100\,\%$.
**Substitution:** $P_\text{h} = 6.0\,\Omega \cdot (7.50\,\text{A})^2 = 337.5\,\text{W}$, so $\dfrac{P_\text{h}}{P} = \dfrac{337.5\,\text{W}}{150\,000\,\text{W}} = 0.00225 = 0.225\,\%$. At the voltage $400\,\text{V}$: $I = 375\,\text{A}$ and $RI^2 = 6.0\,\Omega \cdot (375\,\text{A})^2 = 843\,750\,\text{W} \approx 844\,\text{kW}$
**Answer:** About $0.23\,\%$ of the power turns into heat in the line, two significant figures like the resistance $6.0\,\Omega$. At the voltage $400\,\text{V}$ the expression $RI^2$ would give $844\,\text{kW}$, more than five times the transmitted power. This means that the transmission would not work at all: already the voltage drop of the line $RI = 6.0\,\Omega \cdot 375\,\text{A} = 2250\,\text{V}$ would be larger than the whole voltage.
**Reasonableness:** The loss is proportional to the square of the current, and the current is inversely proportional to the voltage, so a $50$ times higher voltage reduces the loss by a factor of $50^2 = 2500$: $844\,\text{kW} : 2500 \approx 340\,\text{W}$, the same result.

### d)
**Find:** whether the transformer works with a direct voltage
**Principle:** The secondary voltage of a transformer is produced by induction: the primary current produces a magnetic flux in the iron core, and only a change of the flux induces a voltage in the secondary coil (chapters *Electromagnetic induction* and *The transformer and the transmission of electrical energy*).
**Model answer:** The suggestion does not work. Direct current produces a constant flux in the iron core, and an unchanging flux induces no voltage in the secondary coil. Only at the moment the current is switched on does the flux change, and a short voltage spike appears in the secondary. That is why the direct voltage of the solar panels is first converted into an alternating voltage with an inverter, and only after that can the transformer step it up to the line voltage. In addition, with direct current the current in the primary coil is limited only by its small resistance, so the coil could overheat.

### Yleisiä virheitä
- In part a the peak value is given as the rms value, or the division goes the wrong way, $e_0 \cdot \sqrt{2} \approx 800\,\text{V}$.
- In part a the factor $2\pi$ is forgotten, which gives $e_0 = 90\,\text{V}$.
- In part b the currents are swapped: on the side of the higher voltage the current is smaller.
- In part c the loss is calculated from the expression $\tfrac{U^2}{R} = \tfrac{(20\,000\,\text{V})^2}{6.0\,\Omega} \approx 67\,\text{MW}$; the transmission voltage is not across the resistance of the line.

### Hyväksytään myös
- In part c the comparison as a ratio: $\tfrac{P_\text{h,400}}{P_\text{h,20k}} = \left(\tfrac{20\,000}{400}\right)^2 = 2500$, when it is stated that transmission at $400\,\text{V}$ is impossible.

## fy9-magnetismi-valo-s2

### a)
**Given:** refractive index of the core $n_1 = 1.470$, refractive index of the cladding $n_2 = 1.455$
**Find:** the smallest angle of incidence $\alpha_\text{r}$ at which the light stays in the core, and the largest angle between the ray and the axis of the fibre
**Principle:** The light stays in the core if it is totally internally reflected at the boundary between core and cladding. Total internal reflection is possible because the light goes from a medium with a larger refractive index towards a medium with a smaller refractive index, and it happens when the angle of incidence is larger than the critical angle (chapter *Total internal reflection and optical fibre*). The angle of incidence is measured from the normal of the boundary, and the normal is perpendicular to the axis of the fibre, so the angle between the ray and the axis is $90^\circ - \alpha$.
**Formula:** $n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ$, so $\sin\alpha_\text{r} = \dfrac{n_2}{n_1}$, and relative to the axis $\beta_\text{max} = 90^\circ - \alpha_\text{r}$
**Conversions:** Refractive indices have no unit, so no conversions are needed.
**Substitution:** $\sin\alpha_\text{r} = \dfrac{1.455}{1.470} = 0.9898$, so $\alpha_\text{r} = 81.81^\circ$ and $\beta_\text{max} = 90^\circ - 81.81^\circ = 8.19^\circ$
**Answer:** The angle of incidence must be at least $81.8^\circ$, that is, the ray may be at most at an angle of $8.2^\circ$ to the axis of the fibre. The difference of the refractive indices, $0.015$, is known only to two figures: a change of only $0.001$ in it shifts the critical angle by about $0.3^\circ$. The honest precision is therefore about $82^\circ$ and $8^\circ$; the tenth is given only for comparison.
**Reasonableness:** The refractive indices are almost equal, so the critical angle is close to $90^\circ$: only rays almost parallel to the axis stay in the core. Between glass and air the critical angle would be about $43^\circ$.

### b)
**Given:** length of the fibre $s = 14.0\,\text{km}$, refractive index of the core $n_1 = 1.470$, $c = 3.00 \cdot 10^8\,\text{m/s}$, $\sin\alpha_\text{r} = 0.9898$ (part a)
**Find:** the travel time $t$ of a pulse along the axis and the extra time $\Delta t$ of the steepest ray
**Principle:** In a medium light travels at the speed $v = \tfrac{c}{n}$ (chapter *Reflection and refraction of light*). A ray along the axis travels the length of the fibre. The steepest ray that stays in the core travels at the angle $90^\circ - \alpha_\text{r}$ to the axis, so the distance it covers is the length of the fibre divided by the cosine of this angle, that is $\tfrac{s}{\sin\alpha_\text{r}}$ (chapter *Total internal reflection and optical fibre*). Both rays travel in the core at the same speed.
**Formula:** $t = \dfrac{n_1 s}{c}$, for the steepest ray $t' = \dfrac{t}{\sin\alpha_\text{r}}$ and $\Delta t = t' - t$
**Conversions:** $14.0\,\text{km} = 14.0 \cdot 1000\,\text{m} = 14\,000\,\text{m}$ and finally $1\,\text{s} = 10^6\,\mu\text{s}$
**Substitution:** $t = \dfrac{1.470 \cdot 14\,000\,\text{m}}{3.00 \cdot 10^8\,\text{m/s}} = 6.860 \cdot 10^{-5}\,\text{s} = 68.60\,\mu\text{s}$, $t' = \dfrac{68.60\,\mu\text{s}}{0.9898} = 69.31\,\mu\text{s}$ and $\Delta t = 69.31\,\mu\text{s} - 68.60\,\mu\text{s} = 0.71\,\mu\text{s}$
**Answer:** A pulse along the axis covers the distance in the time $t \approx 68.6\,\mu\text{s}$, three significant figures like the length $14.0\,\text{km}$. The steepest pulse arrives about $0.7\,\mu\text{s}$ later; the difference is known only to one or two figures.
**Reasonableness:** Light travels in the fibre at the speed $\tfrac{3.00 \cdot 10^8\,\text{m/s}}{1.470} \approx 2.04 \cdot 10^8\,\text{m/s}$, about two thirds of the speed of light in a vacuum. The difference of about $1\,\%$ corresponds to the ratio of the distances $\tfrac{1}{0.9898} \approx 1.010$. If pulses were sent more often than about once a microsecond, they could get mixed up.

### c)
**Given:** attenuation coefficient $a = 0.22\,\text{dB/km}$, length $L = 14.0\,\text{km}$, four splices at $0.10\,\text{dB}$ each, transmitted power $P_0 = 2.0\,\text{mW}$
**Find:** the received power $P$
**Principle:** The glass of the fibre attenuates the light by the same ratio every kilometre, and the attenuation is given in decibels. The attenuations of successive sections and splices in decibels are added together (chapter *Applied chapter: wireless charging, the induction hob and the fibre link*).
**Formula:** $A = aL + 4 \cdot 0.10\,\text{dB}$ and $A = 10\,\text{dB} \cdot \lg \dfrac{P_0}{P}$, so $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$
**Conversions:** The length is already in kilometres and the power in milliwatts, so no conversions are needed.
**Substitution:** $A = 0.22\,\tfrac{\text{dB}}{\text{km}} \cdot 14.0\,\text{km} + 0.40\,\text{dB} = 3.08\,\text{dB} + 0.40\,\text{dB} = 3.48\,\text{dB}$, so $P = 2.0\,\text{mW} \cdot 10^{-0.348} = 2.0\,\text{mW} \cdot 0.4487 = 0.897\,\text{mW}$
**Answer:** About $0.90\,\text{mW}$ reaches the receiver, two significant figures like the transmitted power $2.0\,\text{mW}$ and the attenuation coefficient $0.22\,\text{dB/km}$.
**Reasonableness:** $3\,\text{dB}$ corresponds to roughly halving the power, so $3.5\,\text{dB}$ leaves a little under half, $45\,\%$. The result is plausible, because in a telecommunications fibre light travels tens of kilometres without amplification.

### d)
**Find:** why a gently curving fibre guides the light but a sharp bend lets it out
**Principle:** The light stays in the core when the angle of incidence at the boundary between core and cladding is larger than the critical angle, in this fibre at least $81.8^\circ$ (chapter *Total internal reflection and optical fibre*).
**Model answer:** In a gentle curve the direction of the boundary changes only a little along the path of the ray, so the ray still hits the boundary almost parallel to it, and the angle of incidence stays larger than the critical angle. The light is totally internally reflected and follows the fibre. In a sharp bend the boundary on the outer side of the curve turns in front of the ray, so the ray hits it more steeply: the angle of incidence falls below $81.8^\circ$, the light refracts into the cladding and leaks out. Because the critical angle is close to $90^\circ$, even a fairly small change in the angle of incidence is enough. That is why a minimum allowed bending radius is given for a fibre cable.

### Yleisiä virheitä
- In part a the refractive indices are swapped, $\sin\alpha_\text{r} = \tfrac{n_1}{n_2} > 1$, or the angle relative to the axis is given as the angle of incidence.
- In part b the speed of light in a vacuum is used, which gives $t \approx 46.7\,\mu\text{s}$.
- In part c the attenuation in decibels is divided by ten and the power is multiplied by that number, or the attenuation of the splices is forgotten, which gives $P \approx 0.98\,\text{mW}$.

## fy9-magnetismi-valo-s3

### a)
**Find:** a graph of the magnetic flux density as a function of distance, and whether it is inversely proportional to the distance
**Graph:** $r\ (\text{cm})$ is on the horizontal axis and $B\ (\mu\text{T})$ on the vertical axis, and the axes start from zero. The six points are plotted from the table. The points are not joined into a broken line; a smooth curve can be drawn through them.

<svg data-fig="fy9-magnetismi-valo-s3-B" viewBox="0 0 600 440" role="img" aria-label="Graph: the magnetic flux density B in microteslas as a function of the distance r in centimetres. Six black points at the distances 2–12 cm, values from 132 microteslas to 31 microteslas. A dashed curve through the points falls steeply and then levels off. When the distance doubles from 2 centimetres to 4 centimetres, the field decreases only from 132 to 72, not to half." style="max-width:100%;font-size:30px">
  <line x1="121.5" y1="380" x2="121.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="147.5" y1="380" x2="147.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="173" y1="380" x2="173" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="199" y1="380" x2="199" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224.5" y1="380" x2="224.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="380" x2="250" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="301.5" y1="380" x2="301.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="327" y1="380" x2="327" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="353" y1="380" x2="353" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="378.5" y1="380" x2="378.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="404.5" y1="380" x2="404.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="359.5" x2="430" y2="359.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="339.5" x2="430" y2="339.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="319" x2="430" y2="319" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="299" x2="430" y2="299" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="278.5" x2="430" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="258.5" x2="430" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="430" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218" x2="430" y2="218" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="430" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="177.5" x2="430" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="157" x2="430" y2="157" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137" x2="430" y2="137" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="116.5" x2="430" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="430" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="121.5" y1="380" x2="121.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="147.5" y1="380" x2="147.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="135.5" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="173" y1="380" x2="173" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="199" y1="380" x2="199" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="224.5" y1="380" x2="224.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="250" y1="380" x2="250" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="238" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$6$</div></foreignObject>
  <line x1="276" y1="380" x2="276" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="301.5" y1="380" x2="301.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289.5" y="386" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$8$</div></foreignObject>
  <line x1="327" y1="380" x2="327" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="353" y1="380" x2="353" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$10$</div></foreignObject>
  <line x1="378.5" y1="380" x2="378.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404.5" y1="380" x2="404.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$12$</div></foreignObject>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="359.5" x2="96" y2="359.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="339.5" x2="96" y2="339.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="319" x2="96" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="299" x2="96" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="278.5" x2="96" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="260.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="89" y1="258.5" x2="96" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218" x2="96" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="177.5" x2="96" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="159.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="89" y1="157" x2="96" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137" x2="96" y2="137" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="116.5" x2="96" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="58" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$150$</div></foreignObject>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="91" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="16" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="142,86 144.5,99.5 147,112 149.5,123 152,133 154,142.5 156.5,151 159,158.5 161.5,166 164,173 166,179 168.5,185 171,190.5 173.5,196 176,201 178,205.5 180.5,210 183,214 185.5,217.5 188,221.5 190,225 192.5,228 195,231.5 197.5,234.5 200,237.5 202,240 204.5,242.5 207,245 209.5,247.5 212,250 214,252 216.5,254 219,256 221.5,258 224,260 226,262 228.5,263.5 231,265.5 233.5,267 236,268.5 238,270 240.5,271.5 243,273 245.5,274.5 248,275.5 250,277 252.5,278 255,279.5 257.5,280.5 259.5,282 262,283 264.5,284 267,285 269.5,286 271.5,287 274,288 276.5,289 279,290 281.5,290.5 283.5,291.5 286,292.5 288.5,293.5 291,294 293.5,295 295.5,295.5 298,296.5 300.5,297 303,298 305.5,298.5 307.5,299 310,300 312.5,300.5 315,301 317.5,302 319.5,302.5 322,303 324.5,303.5 327,304 329.5,304.5 331.5,305.5 334,306 336.5,306.5 339,307 341.5,307.5 343.5,308 346,308.5 348.5,309 351,309.5 353.5,309.5 355.5,310 358,310.5 360.5,311 363,311.5 365.5,312 367.5,312.5 370,312.5 372.5,313 375,313.5 377,314 379.5,314.5 382,314.5 384.5,315 387,315.5 389,315.5 391.5,316 394,316.5 396.5,317 399,317 401,317.5 403.5,318 406,318 408.5,318.5 411,318.5 413,319 415.5,319.5 418,319.5 420.5,320 423,320 425,320.5 427.5,320.5 430,321" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="147.5" cy="112.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="173" cy="197.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="199" cy="234" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="250" cy="278.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="301.5" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="404.5" cy="317" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="263" y="169.5" width="148" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#6b7480">$\text{levels off}$</div></foreignObject>
</svg>

**Model answer:** The field decreases ever more slowly as the distance increases, but it is not inversely proportional to the distance. If it were, doubling the distance would halve the field, but from $2.0\,\text{cm}$ to $4.0\,\text{cm}$ the field decreases only from $132\,\mu\text{T}$ to $72\,\mu\text{T}$, and from $4.0\,\text{cm}$ to $8.0\,\text{cm}$ from $72\,\mu\text{T}$ to $41\,\mu\text{T}$. The product $Br$ also grows: $264$, $270$, $288$, $300$, $328$ and $372\,\mu\text{T} \cdot \text{cm}$. In an inversely proportional relationship it would be constant. So the curve does not approach zero but some positive value: the field seems to contain a part that does not depend on the distance.

### b)
**Find:** a presentation of the data in which a straight line fits the points, the justification and the fitted line
**Graph:** The field of a long straight wire is $B = \tfrac{\mu_0 I}{2\pi r} = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r}$, so $B$ is directly proportional to the reciprocal of the distance. If there is also a constant field $b$, $B = k \cdot \tfrac{1}{r} + b$, which is still a straight line in the $(\tfrac{1}{r}, B)$ coordinates. Calculate the reciprocals: $50.0$, $33.3$, $25.0$, $16.7$, $12.5$ and $8.33\,\tfrac{1}{\text{m}}$. $\tfrac{1}{r}\ (\tfrac{1}{\text{m}})$ is on the horizontal axis and $B\ (\mu\text{T})$ on the vertical axis. The line is fitted between the points and not forced through the origin, so that a possible constant field shows.

<svg data-fig="fy9-magnetismi-valo-s3-lin" viewBox="0 0 600 440" role="img" aria-label="Graph: the magnetic flux density B in microteslas as a function of the reciprocal of the distance 1 over r in the unit 1 per metre. Six black points between 8 and 50 per metre, values from 31 to 132 microteslas. A rising straight line is fitted to the points and extended as a dashed line to the vertical axis, which it crosses at about 11 microteslas, clearly above the origin. Two points are circled on the line, (5.0; 23) and (50; 132), from which the slope of about 2.42 microteslas times metre is read." style="max-width:100%;font-size:30px">
  <line x1="126.5" y1="380" x2="126.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156.5" y1="380" x2="156.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="187" y1="380" x2="187" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217.5" y1="380" x2="217.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="380" x2="248" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278" y1="380" x2="278" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308.5" y1="380" x2="308.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339" y1="380" x2="339" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="369.5" y1="380" x2="369.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="399.5" y1="380" x2="399.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="380" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="359.5" x2="430" y2="359.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="339.5" x2="430" y2="339.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="319" x2="430" y2="319" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="299" x2="430" y2="299" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="278.5" x2="430" y2="278.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="258.5" x2="430" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="238" x2="430" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218" x2="430" y2="218" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="430" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="177.5" x2="430" y2="177.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="157" x2="430" y2="157" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137" x2="430" y2="137" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="116.5" x2="430" y2="116.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="96.5" x2="430" y2="96.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="380" x2="444" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,380 L443,386 L443,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="381" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="126.5" y1="380" x2="126.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="156.5" y1="380" x2="156.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="137" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$10$</div></foreignObject>
  <line x1="187" y1="380" x2="187" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="217.5" y1="380" x2="217.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="198" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$20$</div></foreignObject>
  <line x1="248" y1="380" x2="248" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="278" y1="380" x2="278" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$30$</div></foreignObject>
  <line x1="308.5" y1="380" x2="308.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="339" y1="380" x2="339" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="319.5" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$40$</div></foreignObject>
  <line x1="369.5" y1="380" x2="369.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="399.5" y1="380" x2="399.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="380" y="386" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="430" y1="380" x2="430" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="359.5" x2="96" y2="359.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="339.5" x2="96" y2="339.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="319" x2="96" y2="319" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="299" x2="96" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="278.5" x2="96" y2="278.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="260.5" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$50$</div></foreignObject>
  <line x1="89" y1="258.5" x2="96" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="238" x2="96" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218" x2="96" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="177.5" x2="96" y2="177.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="159.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$100$</div></foreignObject>
  <line x1="89" y1="157" x2="96" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="137" x2="96" y2="137" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="116.5" x2="96" y2="116.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="96.5" x2="96" y2="96.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="29" y="58" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$150$</div></foreignObject>
  <foreignObject x="62" y="382" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="462" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$\tfrac{1}{r}\ (\tfrac{1}{\text{m}})$</div></foreignObject>
  <foreignObject x="86" y="16" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="146.5,318 399.5,113.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,358.5 146.5,318" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="399.5" cy="112.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="298.5" cy="197.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="248" cy="234" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="197" cy="278.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="172" cy="297" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="146.5" cy="317" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="126.5" cy="333.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="126.5" y1="333.5" x2="126.5" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="333.5" x2="126.5" y2="333.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="399.5" cy="112.5" r="11" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="399.5" y1="112.5" x2="399.5" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="112.5" x2="399.5" y2="112.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="96" cy="358.5" r="6" fill="#2b8a3e"/>
  <line x1="101" y1="353.5" x2="114" y2="254.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="105" y="216" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b \approx 11\,\mu\text{T}$</span></div></foreignObject>
  <foreignObject x="108" y="78.5" width="148" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$k \approx 2.42\,\mu\text{T}\cdot\text{m}$</div></foreignObject>
</svg>

**Model answer:** The points lie well on a straight line, so the model of a long straight wire describes the data. However, the line does not pass through the origin but crosses the vertical axis at about $10$–$11\,\mu\text{T}$. This is interpreted in part d.

### c)
**Given:** the fitted line in the graph; points read from the line $(5.0\,\tfrac{1}{\text{m}};\ 23\,\mu\text{T})$ and $(50\,\tfrac{1}{\text{m}};\ 132\,\mu\text{T})$; current $I = 12.0\,\text{A}$
**Find:** the vacuum permeability $\mu_0$ and its comparison with the table value
**Principle:** According to the model $B = \tfrac{\mu_0 I}{2\pi} \cdot \tfrac{1}{r} + b$ the slope of the $(\tfrac{1}{r}, B)$ graph is $k = \tfrac{\mu_0 I}{2\pi}$ (chapter *Magnetic field of a wire and a coil*). The slope is read from two points of the fitted line far apart, not from the measured points (chapter *Graphing and fitting a straight line*). The constant field shifts the line but does not change its slope, so it does not affect the result.
**Reading the graph:** At $\tfrac{1}{r} = 5.0\,\tfrac{1}{\text{m}}$ and $\tfrac{1}{r} = 50\,\tfrac{1}{\text{m}}$ the values $B \approx 23\,\mu\text{T}$ and $B \approx 132\,\mu\text{T}$ are read from the line.
**Formula:** $k = \dfrac{\Delta B}{\Delta(1/r)}$ and $k = \dfrac{\mu_0 I}{2\pi}$, so $\mu_0 = \dfrac{2\pi k}{I}$
**Conversions:** $1\,\mu\text{T} = 10^{-6}\,\text{T}$, and $\text{T} = \tfrac{\text{Vs}}{\text{m}^2}$, so $\tfrac{\text{T} \cdot \text{m}}{\text{A}} = \tfrac{\text{Vs}}{\text{Am}}$.
**Substitution:** $k = \dfrac{132\,\mu\text{T} - 23\,\mu\text{T}}{50\,\tfrac{1}{\text{m}} - 5.0\,\tfrac{1}{\text{m}}} = \dfrac{109\,\mu\text{T}}{45\,\tfrac{1}{\text{m}}} = 2.422\,\mu\text{T} \cdot \text{m} = 2.422 \cdot 10^{-6}\,\text{T} \cdot \text{m}$, so $\mu_0 = \dfrac{2\pi \cdot 2.422 \cdot 10^{-6}\,\text{T} \cdot \text{m}}{12.0\,\text{A}} = 1.268 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$
**Answer:** $\mu_0 \approx 1.27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$, three significant figures like the current $12.0\,\text{A}$ and the values read from the graph.
**Reasonableness:** The table value is $4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} = 1.257 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$, so the difference is about $0.9\,\%$. The scatter of the readings, about $1\,\mu\text{T}$, is under $1\,\%$ at the largest $\tfrac{1}{r}$ values, so the difference is within the precision of the measurement.

### d)
**Given:** slope of the line $k \approx 2.42\,\mu\text{T} \cdot \text{m}$ and constant term $b \approx 10.9\,\mu\text{T}$ (from the points read in part c: $23\,\mu\text{T} - 2.422\,\mu\text{T} \cdot \text{m} \cdot 5.0\,\tfrac{1}{\text{m}}$), distance $r = 50\,\text{cm}$, length of the wire $2.0\,\text{m}$
**Find:** what the constant term tells about the measurement, and the sensor reading $50\,\text{cm}$ away
**Principle:** The wire's own field is inversely proportional to the distance, so the constant term is a field that depends neither on the current nor on the distance. The sensor stayed in the same orientation and was not zeroed, so its reading includes the component of the Earth's magnetic field in the direction of the sensor and the sensor's own zero offset (chapters *Magnets, the magnetic dipole and the magnetic field* and *Measuring and the reliability of a measurement*). The reading further away is obtained from the equation of the fitted line, but the long-wire model holds only when the distance is much smaller than the length of the wire.
**Reading the graph:** The line crosses the $B$ axis at about $11\,\mu\text{T}$; from the points read, $b = 23\,\mu\text{T} - 2.422\,\mu\text{T} \cdot \text{m} \cdot 5.0\,\tfrac{1}{\text{m}} = 10.9\,\mu\text{T}$.
**Formula:** $B = \dfrac{k}{r} + b$
**Conversions:** $50\,\text{cm} = 50 \cdot 0.01\,\text{m} = 0.50\,\text{m}$
**Substitution:** $B = \dfrac{2.422\,\mu\text{T} \cdot \text{m}}{0.50\,\text{m}} + 10.9\,\mu\text{T} = 4.84\,\mu\text{T} + 10.9\,\mu\text{T} = 15.7\,\mu\text{T}$
**Answer:** The constant term of about $11\,\mu\text{T}$ is a constant field independent of the current in the wire: the component of the Earth's magnetic field in the direction of the sensor and the zero offset of the sensor. This can be checked by measuring the reading with the current switched off, when the sensor should show about $11\,\mu\text{T}$. According to the model the sensor would show about $16\,\mu\text{T}$ at $50\,\text{cm}$, two significant figures, because the result depends on the constant term read from the graph. The result is only an estimate, because $50\,\text{cm}$ is outside the measured range ($2$–$12\,\text{cm}$) and the length of the wire, $2.0\,\text{m}$, is no longer much larger than the distance, so the wire's own field is somewhat smaller than $4.8\,\mu\text{T}$.
**Reasonableness:** In southern Finland the horizontal component of the Earth's field is about $14\,\mu\text{T}$, so a component of $11\,\mu\text{T}$ in the direction of the sensor is plausible. The constant term can also be obtained from two measurements: if $B = \tfrac{k}{r} + b$, then $b = 2B(4.0\,\text{cm}) - B(2.0\,\text{cm}) = 2 \cdot 72\,\mu\text{T} - 132\,\mu\text{T} = 12\,\mu\text{T}$, almost the same.

### Yleisiä virheitä
- In part a the points are joined into a broken line, or inverse proportionality is concluded from a decreasing curve alone.
- In part b $B$ is plotted against the distance on a logarithmic scale without justification, or the line is forced through the origin, which makes the slope and $\mu_0$ too large.
- In part c microteslas are not converted to teslas or the distance to metres, which makes the result wrong by orders of magnitude.
- In part d the constant term is explained by random error; it raises all readings by the same amount.

### Hyväksytään myös
- In part c the slope $2.42\,\mu\text{T} \cdot \text{m}$ from fitting software and $\mu_0 \approx 1.27 \cdot 10^{-6}\,\tfrac{\text{Vs}}{\text{Am}}$.
- In part d the estimate $4.8\,\mu\text{T}$ of the wire's own field and the statement that the reading is about $16\,\mu\text{T}$ with the constant field.

## fy9-magnetismi-valo-s4

### a)
**Find:** how a rainbow forms and on which edge red is
**Principle:** The refractive index depends on the wavelength (dispersion): in water the refractive index of violet is the largest and that of red the smallest. In a rainbow light refracts into a drop, reflects from its back surface and refracts out (chapter *Dispersion: the prism and the rainbow*).
**Model answer:** Sunlight enters a drop, refracts at its front surface, reflects from the back surface of the drop and refracts out again. Because the refractive index of water is $1.331$ for red and $1.343$ for violet, the colours refract by different amounts and leave the drop in slightly different directions. The brightest light leaves at an angle of about $42^\circ$ for red and about $40.6^\circ$ for violet relative to the direction of the antisolar point. The viewer sees red from the drops that are at an angle of $42^\circ$, and violet from drops slightly further in. That is why red is on the outer edge of the arc and violet on the inner edge. For the rainbow the guest's claim is correct: the colours separate because different colours refract by different amounts in water.

### b)
**Find:** how the colours of a soap bubble arise and why the thinnest spot looks dark
**Principle:** The waves reflected from the two surfaces of a thin film interfere. At perpendicular incidence their path difference is $2nd$, and a wave is inverted when it reflects off a medium with a larger refractive index (chapter *Thin-film interference*).
**Model answer:** A bubble is a thin film of soapy water with air on both sides. Part of the light is reflected from the outer surface of the film and part from the inner surface, and these waves interfere. Their path difference $2nd$ depends on the thickness $d$ of the film: at some wavelengths the waves reinforce each other and at others they weaken each other. What remains of white light is a mixture of wavelengths that is seen as a colour, and when the thickness of the film varies, the colour changes in stripes. Only the reflection at the outer surface inverts the wave, because there the light reflects from air off soapy water. Just before bursting the top of the bubble is very thin, $2nd \approx 0$, so the reflected waves are almost in opposite phase and cancel each other at all wavelengths, and the spot looks dark. For the bubble the claim is wrong: the colours arise from interference, not from refraction, and the colour depends on the thickness of the film.

### c)
**Find:** how a CD produces colours, the first-order angles of red and violet, and an assessment of the claim
**Principle:** Closely spaced tracks repeating at regular intervals act as a reflection grating. The waves reflected from adjacent tracks reinforce each other in the directions for which $d\sin\theta = k\lambda$ (chapter *Interference and diffraction of light*).
**Model answer:** The surface of a CD has a spiral track whose adjacent turns are $1.6\,\mu\text{m}$ apart. Each track reflects light, and the waves reflected from different tracks reinforce each other only in the directions in which their path difference is a whole number of wavelengths. At perpendicular incidence the first order for red is $\sin\theta = \tfrac{650 \cdot 10^{-9}\,\text{m}}{1.6 \cdot 10^{-6}\,\text{m}} = 0.41$, that is $\theta \approx 24^\circ$, and for violet $\sin\theta = \tfrac{400 \cdot 10^{-9}\,\text{m}}{1.6 \cdot 10^{-6}\,\text{m}} = 0.25$, that is $\theta \approx 14.5^\circ$. So red deviates most, the opposite of a drop and a prism, which shows that the colours arise in a different way. As a whole the guest's claim is wrong. It holds only for the rainbow. The colours of the bubble arise from the interference of the reflections from the two surfaces of the film, and the colours of the CD from the interference of the reflections from many tracks, and no refraction is needed in them.

### Yleisiä virheitä
- In part a it is said that red refracts most because its wavelength is the longest; in water violet refracts most.
- In part b the colours are explained by the dye of the soap or by refraction, or the inversion on reflection is forgotten, so that the thinnest spot is claimed to be bright.
- In part c the angle is calculated without the inverse sine, or violet is said to deviate most in a grating.

## fy9-magnetismi-valo-s5

### a)
**Given:** the grating has $N = 600$ lines per millimetre, $L = 80.0\,\text{cm}$, $x_1 = 27.0\,\text{cm}$, $x_2 = 66.4\,\text{cm}$
**Find:** the wavelength $\lambda$ of the laser from each maximum
**Principle:** The maxima of a grating lie in the directions for which $d\sin\theta = k\lambda$, and the grating constant is the line spacing (chapter *Interference and diffraction of light*). The angle is obtained from the right triangle at the screen, $\tan\theta = \tfrac{x}{L}$. The sine and the tangent are almost equal only at small angles, so the angle is calculated first from the tangent and only then its sine.
**Formula:** $d = \dfrac{1\,\text{mm}}{N}$, $\theta_k = \tan^{-1}\dfrac{x_k}{L}$ and $\lambda = \dfrac{d\sin\theta_k}{k}$
**Conversions:** $d = \dfrac{1\,\text{mm}}{600} = \dfrac{1 \cdot 10^{-3}\,\text{m}}{600} = 1.667 \cdot 10^{-6}\,\text{m}$; in the ratio of the distances the units cancel, and finally $1\,\text{m} = 10^9\,\text{nm}$.
**Substitution:** $\tan\theta_1 = \dfrac{27.0\,\text{cm}}{80.0\,\text{cm}} = 0.3375$, so $\theta_1 = 18.65^\circ$ and $\lambda = 1.667 \cdot 10^{-6}\,\text{m} \cdot \sin 18.65^\circ = 1.667 \cdot 10^{-6}\,\text{m} \cdot 0.3198 = 533.0\,\text{nm}$. $\tan\theta_2 = \dfrac{66.4\,\text{cm}}{80.0\,\text{cm}} = 0.830$, so $\theta_2 = 39.69^\circ$ and $\lambda = \dfrac{1.667 \cdot 10^{-6}\,\text{m} \cdot 0.6386}{2} = 532.2\,\text{nm}$
**Answer:** From the first order $\lambda \approx 533\,\text{nm}$ and from the second $\lambda \approx 532\,\text{nm}$, three significant figures like the distances.
**Reasonableness:** Both orders give the same result, and it is the wavelength of green light, as the colour of the laser shows. The angle $\theta_2 \approx 40^\circ$ is so large that $\sin\theta_2 = 0.64$ and $\tan\theta_2 = 0.83$ differ clearly.

### b)
**Find:** whether the group's conclusions are justified
**Principle:** The small-angle assumption $\sin\theta \approx \tfrac{x}{L}$ holds only at small angles. The result is compared with the manufacturer's value using the uncertainty, and the number of maxima is limited by the condition $k\lambda < d$ (chapters *Interference and diffraction of light* and *Measuring and the reliability of a measurement*).
**Model answer:** Neither conclusion is justified. The mistake is in the method of calculation, not in the laser. The small-angle assumption gives from the first order $\tfrac{1.667\,\mu\text{m} \cdot 0.270\,\text{m}}{0.800\,\text{m}} \approx 562\,\text{nm}$, about $6\,\%$ too much, and from the second $692\,\text{nm}$, about $30\,\%$ too much, because the difference between the tangent and the sine grows as the angle grows. Calculated correctly, the result is $532$–$533\,\text{nm}$. If the distances are known to about $0.3\,\text{cm}$, the extreme values for the second order give about $530$–$535\,\text{nm}$, so the result agrees with the manufacturer's value $532\,\text{nm}$. In addition, the laser looked green, which already rules out red light. The third order exists, because $3\lambda = 1.60\,\mu\text{m} < d = 1.667\,\mu\text{m}$, but $\sin\theta_3 = 0.958$, $\theta_3 \approx 73^\circ$ and the maximum is $x_3 = 0.800\,\text{m} \cdot \tan 73.3^\circ \approx 2.7\,\text{m}$ from the central maximum. It is probably beyond the edge of the wall or so faint that it was not noticed. So the grating is not faulty.

### c)
**Find:** how the measurement can be improved
**Principle:** The relative uncertainty decreases when the measured distance is large compared with the uncertainty of reading it. Systematic errors, such as a crooked set-up, are removed by the measuring method, and the result is given with its uncertainty (chapters *Measuring and the reliability of a measurement* and *Your own experimental investigation: planning, carrying out and reporting*).
**Model answer:** Measure the distance between the maxima $+k$ and $-k$ on both sides of the central maximum and halve it. Measuring the gap between two light spots is more precise than estimating the centre of the central maximum, and if the distances to the two sides are equal, the beam hits the grating perpendicularly. Use the second order, whose $x$ is large, or increase the distance $L$, so that the reading uncertainty of about $0.3\,\text{cm}$ is a small part of the measured distance. Estimate $\Delta x$ and $\Delta L$, calculate the wavelength with their extreme values and give the result in the form $\lambda \pm \Delta\lambda$, for example $(532 \pm 3)\,\text{nm}$, so that it can be compared with the manufacturer's value. Repeat the measurement, preferably with readings by different people, and use the tangent in the calculation instead of the small-angle assumption. Safety: do not look into the laser beam, do not point it at anyone's eyes, and do not leave reflecting objects in the path of the beam.

### Yleisiä virheitä
- In part a $\sin\theta = \tfrac{x}{L}$ is used, or $\sin\theta = \tfrac{x}{\sqrt{x^2 + L^2}}$ while forgetting to divide by the order.
- In part a the grating constant is taken as $600\,\text{mm}$ or $\tfrac{1}{600}\,\text{m}$.
- In part b the conclusion is accepted because the calculated number “looks red”, or the uncertainty is not compared with the difference.
- In part c only repetitions are suggested; they do not remove the systematic error of the calculation method.

## fy9-magnetismi-valo-s6

### a)
**Given:** magnetic flux density $B = 1.20\,\text{T}$, mass of the proton $m = 1.673 \cdot 10^{-27}\,\text{kg}$ and charge $q = 1.602 \cdot 10^{-19}\,\text{C}$; velocity perpendicular to the field
**Find:** a proof that the period of revolution does not depend on the speed, and the frequency $f$ of the voltage
**Principle:** The magnetic force $qvB$ is perpendicular to the velocity, so inside an electrode the proton is in uniform circular motion, and the force is its centripetal force (chapters *Charged particle in electric and magnetic fields* and *Centripetal acceleration and the equation of motion in a circle*). In one revolution the proton travels the circumference of the circle, $2\pi r$ (chapter *Moving in a circle: period and speed*). The direction of the voltage must change every half revolution, when the proton crosses the gap, so the frequency of the voltage is the same as the frequency of revolution.
**Formula:** $qvB = \dfrac{mv^2}{r}$, so $r = \dfrac{mv}{qB}$, and $T = \dfrac{2\pi r}{v} = \dfrac{2\pi m}{qB}$; the speed cancels, and $f = \dfrac{1}{T} = \dfrac{qB}{2\pi m}$
**Conversions:** The quantities are in base units; finally $1\,\text{MHz} = 10^6\,\text{Hz}$.
**Substitution:** $T = \dfrac{2\pi \cdot 1.673 \cdot 10^{-27}\,\text{kg}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.20\,\text{T}} = 5.468 \cdot 10^{-8}\,\text{s}$, so $f = \dfrac{1}{5.468 \cdot 10^{-8}\,\text{s}} = 1.829 \cdot 10^{7}\,\text{Hz} = 18.29\,\text{MHz}$
**Answer:** The period of revolution $T = \tfrac{2\pi m}{qB}$ depends neither on the speed nor on the radius: a faster proton goes round a larger circle in the same time. The voltage must alternate at the frequency $f \approx 18.3\,\text{MHz}$, three significant figures like the magnetic flux density $1.20\,\text{T}$.
**Reasonableness:** Units: $\tfrac{\text{kg}}{\text{C} \cdot \text{T}} = \tfrac{\text{kg}}{\text{C} \cdot \tfrac{\text{N}}{\text{A} \cdot \text{m}}} = \tfrac{\text{kg} \cdot \text{m}}{\text{N} \cdot \text{s}} = \text{s}$. The frequency is in the radio-frequency range, as for the accelerating voltages of cyclotrons.

### b)
**Given:** kinetic energy $E_\text{k} = 8.0\,\text{MeV}$, $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$, $m$, $q$ and $B$ as in part a
**Find:** the speed $v$ of the proton and the radius $r$ of its path when it comes out
**Principle:** In classical mechanics the kinetic energy is $\tfrac12 mv^2$. The radius of the path is obtained from the equation of the centripetal force as in part a (chapter *Charged particle in electric and magnetic fields*). The condition is met if the speed stays clearly smaller than the speed of light.
**Formula:** $v = \sqrt{\dfrac{2E_\text{k}}{m}}$ and $r = \dfrac{mv}{qB}$
**Conversions:** $8.0\,\text{MeV} = 8.0 \cdot 10^6 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 1.282 \cdot 10^{-12}\,\text{J}$
**Substitution:** $v = \sqrt{\dfrac{2 \cdot 1.282 \cdot 10^{-12}\,\text{J}}{1.673 \cdot 10^{-27}\,\text{kg}}} = 3.914 \cdot 10^{7}\,\text{m/s}$ and $r = \dfrac{1.673 \cdot 10^{-27}\,\text{kg} \cdot 3.914 \cdot 10^{7}\,\text{m/s}}{1.602 \cdot 10^{-19}\,\text{C} \cdot 1.20\,\text{T}} = 0.3406\,\text{m}$
**Answer:** The speed of the proton is $v \approx 3.9 \cdot 10^7\,\text{m/s}$ and the radius of its path $r \approx 0.34\,\text{m}$, two significant figures like the energy $8.0\,\text{MeV}$.
**Reasonableness:** $\tfrac{v}{c} = \tfrac{3.914 \cdot 10^7\,\text{m/s}}{3.00 \cdot 10^8\,\text{m/s}} \approx 0.13$, under a fifth, so by the condition of the problem the classical model is sufficient. An electrode diameter of about $70\,\text{cm}$ suits a hospital device.

### c)
**Given:** gap voltage $U = 50\,\text{kV}$ per crossing, two crossings per revolution, $E_\text{k} = 8.0\,\text{MeV}$, $T = 5.468 \cdot 10^{-8}\,\text{s}$ (part a)
**Find:** the number of revolutions $n$ and the duration $t$ of the acceleration
**Principle:** The magnetic force is perpendicular to the velocity, so it does no work and does not change the speed. Only the electric field of the gap does work: at each crossing the kinetic energy of the proton increases by $qU$ (chapter *Potential energy and potential in an electric field*). The proton crosses the gap twice per revolution, and the period of revolution stays the same throughout the acceleration (part a).
**Formula:** $n = \dfrac{E_\text{k}}{2qU}$ and $t = nT$
**Conversions:** The charge of the proton is the elementary charge, so $qU = 50\,\text{keV} = 0.050\,\text{MeV}$; finally $1\,\text{s} = 10^6\,\mu\text{s}$.
**Substitution:** $n = \dfrac{8.0\,\text{MeV}}{2 \cdot 0.050\,\text{MeV}} = 80$ and $t = 80 \cdot 5.468 \cdot 10^{-8}\,\text{s} = 4.37 \cdot 10^{-6}\,\text{s} = 4.37\,\mu\text{s}$
**Answer:** The proton makes about $80$ revolutions, and the acceleration lasts about $4.4\,\mu\text{s}$, two significant figures like the energy $8.0\,\text{MeV}$.
**Reasonableness:** Without the magnetic field the same energy would require a voltage of $8.0\,\text{MV}$; the cyclotron reaches it with a voltage of $50\,\text{kV}$ because the same gap is used $160$ times. The distance travelled is under $80 \cdot 2\pi \cdot 0.34\,\text{m} \approx 170\,\text{m}$, so the short time is plausible.

### d)
**Given:** $v = 3.914 \cdot 10^{7}\,\text{m/s}$ and $r = 0.3406\,\text{m}$ (part b)
**Find:** the acceleration $a$ and its direction when the proton comes out
**Principle:** Inside an electrode the proton is in uniform circular motion, so its acceleration is the centripetal acceleration, which points to the centre of the path (chapter *Centripetal acceleration and the equation of motion in a circle*). Newton's second law for the magnetic force gives the same.
**Formula:** $a_\text{n} = \dfrac{v^2}{r}$, and as a check $a = \dfrac{qvB}{m}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $a_\text{n} = \dfrac{(3.914 \cdot 10^{7}\,\text{m/s})^2}{0.3406\,\text{m}} = 4.498 \cdot 10^{15}\,\text{m/s}^2$
**Answer:** The acceleration is $a \approx 4.5 \cdot 10^{15}\,\text{m/s}^2$ and points to the centre of the path, two significant figures like the results of part b.
**Reasonableness:** $\tfrac{qvB}{m} = \tfrac{1.602 \cdot 10^{-19}\,\text{C} \cdot 3.914 \cdot 10^{7}\,\text{m/s} \cdot 1.20\,\text{T}}{1.673 \cdot 10^{-27}\,\text{kg}} \approx 4.5 \cdot 10^{15}\,\text{m/s}^2$, the same result. The acceleration is enormous because the mass of the proton is very small and the force about $7.5 \cdot 10^{-12}\,\text{N}$.

### Yleisiä virheitä
- In part a the period of revolution is calculated separately for some speed, and it is not stated that the speed cancels.
- In part b megaelectronvolts are not converted to joules, or the mass of the electron is used.
- In part c it is forgotten that the gap is crossed twice per revolution, which gives $160$ revolutions.
- In part d the acceleration is said to point in the direction of the velocity or to speed the proton up in the magnetic field.

### Hyväksytään myös
- In part a calculating the frequency directly from the expression $f = \tfrac{qB}{2\pi m}$.
- In part c the answer $n = 80$ without decimals, because the number of revolutions is a whole number.
