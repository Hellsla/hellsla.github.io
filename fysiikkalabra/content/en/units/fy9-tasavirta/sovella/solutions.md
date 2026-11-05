## fy9-tasavirta-s1

### a)
**Given:** $10$ strips, voltage between the busbars $U = 13.5\,\text{V}$, current of the heater $I = 12.0\,\text{A}$
**Find:** the power $P$ of the heater and the resistance $R_1$ of one strip
**Principle:** Each strip runs from one busbar to the other, so the strips are in parallel: the voltage across all of them is the same $13.5\,\text{V}$, and identical strips share the current equally (chapter *Resistors in series and in parallel*). The power of the heater is the product of the voltage and the current (chapter *Electric power and the heating of a resistor*), and the resistance of a strip is the ratio of its voltage to its current (chapter *Resistance and Ohm's law*).
**Formula:** $P = UI$, $I_1 = \dfrac{I}{10}$ and $R_1 = \dfrac{U}{I_1}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $P = 13.5\,\text{V} \cdot 12.0\,\text{A} = 162\,\text{W}$, $I_1 = \dfrac{12.0\,\text{A}}{10} = 1.20\,\text{A}$ and $R_1 = \dfrac{13.5\,\text{V}}{1.20\,\text{A}} = 11.25\,\Omega$
**Answer:** The power of the heater is $P \approx 162\,\text{W}$ and the resistance of one strip $R_1 \approx 11.3\,\Omega$, three significant figures like the voltage and the current.
**Reasonableness:** The resistance of the whole heater is $\tfrac{11.25\,\Omega}{10} = 1.125\,\Omega$, and $\tfrac{13.5\,\text{V}}{1.125\,\Omega} = 12.0\,\text{A}$, as measured. A power of a few hundred watts is enough to melt thin frost off the glass in a few minutes.

### b)
**Given:** resistance of a strip $R_1 = 11.25\,\Omega$ (part a), length $l = 1.10\,\text{m}$, width $b = 3.0\,\text{mm}$, resistivity $\rho = 3.0 \cdot 10^{-7}\,\Omega\cdot\text{m}$
**Find:** the thickness $h$ of a strip
**Principle:** A strip is a conductor of uniform thickness, whose resistance is proportional to its length and inversely proportional to its cross-sectional area (chapter *Resistance and Ohm's law*). The cross-section of a strip is a rectangle whose area is the width times the thickness.
**Formula:** $R_1 = \rho\,\dfrac{l}{A}$, so $A = \dfrac{\rho l}{R_1}$, and $A = bh$, so $h = \dfrac{A}{b} = \dfrac{\rho l}{R_1 b}$
**Conversions:** $3.0\,\text{mm} = 3.0 \cdot 10^{-3}\,\text{m}$ and finally $1\,\text{m} = 10^{6}\,\mu\text{m}$
**Substitution:** $A = \dfrac{3.0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 1.10\,\text{m}}{11.25\,\Omega} = 2.933 \cdot 10^{-8}\,\text{m}^2$ and $h = \dfrac{2.933 \cdot 10^{-8}\,\text{m}^2}{3.0 \cdot 10^{-3}\,\text{m}} = 9.78 \cdot 10^{-6}\,\text{m} = 9.78\,\mu\text{m}$
**Answer:** The thickness of a strip is $h \approx 9.8\,\mu\text{m}$, that is, about a hundredth of a millimetre, two significant figures like the resistivity and the width.
**Reasonableness:** A conducting strip printed on the surface of the glass is a very thin film, so a thickness of micrometres is credible. If the strip were a millimetre thick, its resistance would be a hundred times smaller, and the current would be too large.

### c)
**Find:** how the current and the power change when one strip breaks, and whether the glass warms up as well as before where the strips are intact
**Principle:** The voltage across parallel branches is the same, so a broken branch does not change the voltage or the current of the other branches (chapter *Resistors in series and in parallel*). The current entering the busbars is the sum of the currents of the branches (chapter *Kirchhoff's laws and potential in a circuit*).
**Model answer:** No current passes through the broken strip any more, but the voltage across the nine intact strips is still $13.5\,\text{V}$. The current of each intact strip is still $1.20\,\text{A}$ and its power $13.5\,\text{V} \cdot 1.20\,\text{A} = 16.2\,\text{W}$, so they heat the glass as before. The current of the heater decreases to $9 \cdot 1.20\,\text{A} = 10.8\,\text{A}$, and the power to $13.5\,\text{V} \cdot 10.8\,\text{A} \approx 146\,\text{W}$, so both decrease by a tenth. A narrow band remains where the broken strip is, and there the frost melts only with the heat of the neighbouring strips. If the strips were in series, one break would switch off the whole heater.

### d)
**Given:** resistance of a strip $R_1 = 11.25\,\Omega$ (part a), $10$ strips in parallel, emf of the battery $E = 12.6\,\text{V}$ and internal resistance $R_\text{s} = 0.020\,\Omega$, power of the heater with the engine running $162\,\text{W}$ (part a)
**Find:** the power $P$ of the heater on the battery alone
**Principle:** Ten identical parallel strips are equivalent to one resistor whose resistance is a tenth of the resistance of a strip (chapter *Resistors in series and in parallel*). The internal resistance of the battery is in series with the heater, so the current is set by their combined resistance (chapter *Electromotive force and internal resistance*). The power of the heater is obtained from its current with Joule's law (chapter *Electric power and the heating of a resistor*).
**Formula:** $R = \dfrac{R_1}{10}$, $I = \dfrac{E}{R + R_\text{s}}$ and $P = RI^2$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $R = \dfrac{11.25\,\Omega}{10} = 1.125\,\Omega$, $I = \dfrac{12.6\,\text{V}}{1.125\,\Omega + 0.020\,\Omega} = 11.00\,\text{A}$ and $P = 1.125\,\Omega \cdot (11.00\,\text{A})^2 = 136.2\,\text{W}$
**Answer:** The power of the heater is $P \approx 136\,\text{W}$, three significant figures like the emf $12.6\,\text{V}$.
**Reasonableness:** The terminal voltage is $12.6\,\text{V} - 0.020\,\Omega \cdot 11.0\,\text{A} = 12.38\,\text{V}$, and $\tfrac{(12.38\,\text{V})^2}{1.125\,\Omega} \approx 136\,\text{W}$, the same result. The power is about $84\,\%$ of that with the engine running, because the power is proportional to the square of the voltage and $\left(\tfrac{12.38}{13.5}\right)^2 \approx 0.84$. With the engine running the alternator keeps the voltage higher.

### Yleisiä virheitä
- In part a the resistance of the whole heater $\tfrac{13.5\,\text{V}}{12.0\,\text{A}} = 1.125\,\Omega$ is taken as the resistance of a strip, or the strips are assumed to be in series, so that the resistance is divided by ten in the wrong direction.
- In part b millimetres are not converted into metres, or the cross-sectional area is taken as $\pi r^2$, although the strip is flat.
- In part c it is assumed that the current of the other strips increases, because the total current is “shared” between nine.
- In part d the internal resistance is forgotten, or the power is calculated with the emf, $\tfrac{(12.6\,\text{V})^2}{1.125\,\Omega} = 141\,\text{W}$.

### Hyväksytään myös
- In part d the power from the terminal voltage $P = \tfrac{U^2}{R}$, once $U = E - R_\text{s} I$ has been calculated.

## fy9-tasavirta-s2

### a)
**Given:** rated voltage $U = 36\,\text{V}$, capacity $Q = 10.4\,\text{Ah}$
**Find:** the energy $W$ stored in the battery in watt-hours and in megajoules
**Principle:** The capacity tells the charge that can pass through the battery, and each unit of charge gives up energy according to the voltage. That is why the energy of the battery is the rated voltage times the capacity (chapter *Batteries and the charging circuit*).
**Formula:** $W = UQ$
**Conversions:** $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh}$ and $1\,\text{Wh} = 1\,\text{W} \cdot 3600\,\text{s} = 3600\,\text{J}$
**Substitution:** $W = 36\,\text{V} \cdot 10.4\,\text{Ah} = 374.4\,\text{Wh} = 374.4 \cdot 3600\,\text{J} = 1.348 \cdot 10^{6}\,\text{J}$
**Answer:** $W \approx 374\,\text{Wh} \approx 1.35\,\text{MJ}$, three significant figures like the capacity $10.4\,\text{Ah}$.
**Reasonableness:** A phone battery holds about $15\,\text{Wh}$ and a laptop battery about $50\,\text{Wh}$, so the scooter battery is the size of a few laptop batteries, which suits a vehicle.

### b)
**Given:** capacity $Q = 10.4\,\text{Ah}$, average current $I = 7.5\,\text{A}$, speed $v = 20\,\text{km/h}$
**Find:** the riding distance $s$ on a full battery
**Principle:** With a constant current the charge passing through the battery is the current times the time, so the capacity and the current give the riding time (chapter *Batteries and the charging circuit*). At a steady speed the distance is the speed times the time. It is assumed that the whole capacity can be used and that the current stays at its average.
**Formula:** $Q = It$, so $t = \dfrac{Q}{I}$, and $s = vt$
**Conversions:** Ampere-hours divided by amperes give the time directly in hours.
**Substitution:** $t = \dfrac{10.4\,\text{Ah}}{7.5\,\text{A}} = 1.387\,\text{h}$ and $s = 20\,\tfrac{\text{km}}{\text{h}} \cdot 1.387\,\text{h} = 27.7\,\text{km}$
**Answer:** The battery lasts for about $s \approx 28\,\text{km}$, two significant figures like the current $7.5\,\text{A}$ and the speed $20\,\text{km/h}$.
**Reasonableness:** The riding time is about $1\,\text{h}\ 23\,\text{min}$, and the average power $36\,\text{V} \cdot 7.5\,\text{A} = 270\,\text{W}$, which is usual for the motor of a scooter. The real distance is often shorter: hills, headwind and cold weather increase the current, and it is not advisable to run the battery completely flat.

### c)
**Given:** voltage of the charger $U_\text{ch} = 42.0\,\text{V}$, emf of the empty battery $E = 34.5\,\text{V}$ and internal resistance $R_\text{s} = 0.40\,\Omega$, resistance of the charger and the leads $R = 2.6\,\Omega$
**Find:** the charging current $I$ and the terminal voltage $U$ of the battery at the start of charging
**Principle:** The loop of the charging circuit is gone round in the direction of the current (chapter *Kirchhoff's laws and potential in a circuit*). The potential rises by $U_\text{ch}$ in the charger and falls by $RI$ and $R_\text{s} I$ across the resistances. In addition it falls by the emf of the battery, because during charging the current passes through the battery from the positive terminal to the negative terminal (chapter *Batteries and the charging circuit*). That is why the charging current is driven by the difference between the voltage of the charger and the emf of the battery.
**Formula:** $U_\text{ch} - RI - R_\text{s} I - E = 0$, so $I = \dfrac{U_\text{ch} - E}{R + R_\text{s}}$; terminal voltage during charging $U = E + R_\text{s} I$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $I = \dfrac{42.0\,\text{V} - 34.5\,\text{V}}{2.6\,\Omega + 0.40\,\Omega} = \dfrac{7.5\,\text{V}}{3.0\,\Omega} = 2.50\,\text{A}$ and $U = 34.5\,\text{V} + 0.40\,\Omega \cdot 2.50\,\text{A} = 35.5\,\text{V}$
**Answer:** The charging current is $I \approx 2.5\,\text{A}$, two significant figures like the voltage difference $7.5\,\text{V}$, and the terminal voltage $U \approx 35.5\,\text{V}$.
**Reasonableness:** During charging the terminal voltage is larger than the emf, as it should be. Across the charger and the leads there is $2.6\,\Omega \cdot 2.5\,\text{A} = 6.5\,\text{V}$, and $35.5\,\text{V} + 6.5\,\text{V} = 42.0\,\text{V}$. As the battery charges, its emf increases, so the current decreases and charging slows down towards the end.

### d)
**Given:** voltage of the charger $U_\text{ch} = 42.0\,\text{V}$, charge passing through the battery $Q = 10.4\,\text{Ah}$, energy stored in the battery $W_\text{bat} = 374.4\,\text{Wh}$ (part a), price $15\,\text{c/kWh}$
**Find:** the efficiency $\eta$ of charging and the cost $K$ of one charge
**Principle:** The power of the charger is $U_\text{ch} I$ (chapter *Electric power and the heating of a resistor*), so a constant-voltage charger supplies the energy $U_\text{ch} Q$ when the charge $Q$ passes through the battery. Only the share of the emf is stored in the battery as chemical energy, and the rest is transformed into internal energy of the resistances (chapter *Batteries and the charging circuit*). In the model the emf of the battery during charging is on average equal to the rated voltage $36\,\text{V}$. The cost is calculated from the energy supplied by the charger (chapter *Electrical energy at home*).
**Formula:** $W_\text{ch} = U_\text{ch} Q$, $\eta = \dfrac{W_\text{bat}}{W_\text{ch}}$ and $K = aW_\text{ch}$
**Conversions:** $437\,\text{Wh} = 0.437\,\text{kWh}$ and $15\,\text{c/kWh} = 0.15\,\text{€/kWh}$
**Substitution:** $W_\text{ch} = 42.0\,\text{V} \cdot 10.4\,\text{Ah} = 436.8\,\text{Wh}$, $\eta = \dfrac{374.4\,\text{Wh}}{436.8\,\text{Wh}} = 0.857$ and $K = 0.15\,\tfrac{\text{€}}{\text{kWh}} \cdot 0.4368\,\text{kWh} = 0.066\,\text{€}$
**Answer:** The efficiency is $\eta \approx 86\,\%$, and one full charge costs about $7\,\text{c}$. The precision is two significant figures, because the rated voltage of the battery $36\,\text{V}$ is given to only two figures.
**Reasonableness:** The efficiency is below $100\,\%$, because $436.8\,\text{Wh} - 374.4\,\text{Wh} \approx 62\,\text{Wh}$ is transformed into internal energy of the resistances of the charger, the leads and the battery; that is why the charger and the battery warm up during charging. About seven cents for a ride of about $28\,\text{km}$ is very cheap.

### Yleisiä virheitä
- In part a milliampere-hours or ampere-hours are taken as energy, or watt-hours are not converted into joules by substitution.
- In part b the time is calculated from the energy and the current, so the units do not match.
- In part c the charging current is calculated from the voltage of the charger alone, $\tfrac{42.0\,\text{V}}{3.0\,\Omega} = 14\,\text{A}$, or the terminal voltage is given as $E - R_\text{s} I$, which applies to discharging.
- In part d an efficiency above $100\,\%$ is obtained by comparing the wrong way round, or the cost is calculated from the energy stored in the battery instead of the energy of the charger.

### Hyväksytään myös
- In part d the efficiency directly as the ratio of the voltages $\eta = \tfrac{36\,\text{V}}{42.0\,\text{V}}$, when it has been justified that the same charge passes through the charger and the battery.

## fy9-tasavirta-s3

### a)
**Find:** the terminal voltage as a function of the current as a graph, a fitted model and the justification of the model
**Graph:** $I\ (\text{A})$ is on the horizontal axis and $U\ (\text{V})$ on the vertical axis. The voltages are between $3.89$ and $4.56\,\text{V}$, so the vertical axis is broken so that the small changes show; the break is marked on the axis. The horizontal axis starts at zero, so that the line can be extended to the vertical axis. The points are not joined into a broken line; instead one straight line is fitted between them.

<svg data-fig="fy9-tasavirta-s3-ui" viewBox="0 0 600 440" role="img" aria-label="Graph: the terminal voltage U of a battery holder in volts as a function of the current I in amperes. The vertical axis starts at 3.6 volts, and the break is marked on the axis. Six black points at currents of 0.10–1.00 A, voltages from 4.56 volts to 3.89 volts. A falling straight line is fitted to the points and extended as a dashed line to the vertical axis, which it crosses at about 4.63 V, and up to a current of 1.20 A. Two points on the line are circled, (0 A; 4.63 V) and (1.20 A; 3.75 V), from which the slope is read." style="max-width:100%;font-size:30px">
  <line x1="137.5" y1="380" x2="137.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="165.5" y1="380" x2="165.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="193" y1="380" x2="193" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="221" y1="380" x2="221" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248.5" y1="380" x2="248.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="380" x2="304" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="380" x2="331.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="380" x2="359" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="387" y1="380" x2="387" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="380" x2="414.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="442.5" y1="380" x2="442.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="380" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="353.5" x2="470" y2="353.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="326.5" x2="470" y2="326.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="300" x2="470" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="273.5" x2="470" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="246.5" x2="470" y2="246.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="220" x2="470" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="193.5" x2="470" y2="193.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="166.5" x2="470" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="140" x2="470" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="113.5" x2="470" y2="113.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="86.5" x2="470" y2="86.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="380" x2="484" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,380 L483,386 L483,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="381" x2="110" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,34 L116,47 L104,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="137.5" y1="380" x2="137.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="165.5" y1="380" x2="165.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193" y1="380" x2="193" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="221" y1="380" x2="221" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="193.5" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0.4$</div></foreignObject>
  <line x1="248.5" y1="380" x2="248.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="276" y1="380" x2="276" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="304" y1="380" x2="304" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="331.5" y1="380" x2="331.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="304" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$0.8$</div></foreignObject>
  <line x1="359" y1="380" x2="359" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="387" y1="380" x2="387" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="414.5" y1="380" x2="414.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="442.5" y1="380" x2="442.5" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="415" y="386" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1.2$</div></foreignObject>
  <line x1="470" y1="380" x2="470" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="353.5" x2="110" y2="353.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="326.5" x2="110" y2="326.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="308.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$3.8$</div></foreignObject>
  <line x1="103" y1="300" x2="110" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="273.5" x2="110" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="255.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4.0$</div></foreignObject>
  <line x1="103" y1="246.5" x2="110" y2="246.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="220" x2="110" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="202" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4.2$</div></foreignObject>
  <line x1="103" y1="193.5" x2="110" y2="193.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="166.5" x2="110" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="148.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4.4$</div></foreignObject>
  <line x1="103" y1="140" x2="110" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="113.5" x2="110" y2="113.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="95.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4.6$</div></foreignObject>
  <line x1="103" y1="86.5" x2="110" y2="86.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="103" y1="60" x2="110" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="42" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4.8$</div></foreignObject>
  <foreignObject x="502" y="362" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="100" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$U\ (\text{V})$</div></foreignObject>
  <path d="M101,366 L119,358 M101,356 L119,348" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="76" y="384" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <polyline points="137.5,126 387,300.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="110,106.5 137.5,126" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="387,300.5 442.5,339.5" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="137.5" cy="124" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="179" cy="158.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="221" cy="182.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="276" cy="225.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="331.5" cy="257.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="387" cy="302.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="110" cy="105.5" r="11" fill="none" stroke="#1971c2" stroke-width="2.5"/>
  <circle cx="442.5" cy="340" r="11" fill="none" stroke="#1971c2" stroke-width="2.5"/>
  <line x1="442.5" y1="340" x2="442.5" y2="380" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="340" x2="442.5" y2="340" stroke="#1971c2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="126.5" y="63.5" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E \approx 4.63\,\text{V}$</span></div></foreignObject>
  <foreignObject x="158" y="322" width="247" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$(1.20\,\text{A};\ 3.75\,\text{V})$</span></div></foreignObject>
</svg>

**Model answer:** The group of batteries is described by a model in which a source with the emf $E$ is in series with the internal resistance $R_\text{s}$. When the current $I$ is drawn from the group, the terminal voltage is smaller by the voltage drop across the internal resistance, $U = E - R_\text{s} I$. The voltage drop is proportional to the current when $E$ and $R_\text{s}$ are constant, so the graph of the model is a falling straight line. The points lie well on a straight line, and their deviations from the line are about $0.01\,\text{V}$, of the order of the precision of the readings. So the model fits the data.

### b)
**Given:** the fitted line in the graph; the points read from the line $(0\,\text{A};\ 4.63\,\text{V})$ and $(1.20\,\text{A};\ 3.75\,\text{V})$; the typical values of a new AA battery $1.5$–$1.6\,\text{V}$ and $0.1$–$0.3\,\Omega$
**Find:** the emf $E$ and the internal resistance $R_\text{s}$ of the group of batteries and a comparison with the values of one battery
**Principle:** According to the model $U = E - R_\text{s} I$ the line crosses the vertical axis at $U = E$, because without a current there is no voltage drop across the internal resistance, and the slope of the line is $-R_\text{s}$ (chapter *Electromotive force and internal resistance*). The slope is read from two points of the fitted line far apart, not from the measured points (chapter *Graphing and fitting a straight line*). The emfs and the internal resistances of batteries connected in series add up.
**Reading the graph:** The line crosses the vertical axis at $4.63\,\text{V}$. At $I = 1.20\,\text{A}$ the value of the line is $3.75\,\text{V}$.
**Formula:** $E = U(0)$ and $R_\text{s} = -\dfrac{\Delta U}{\Delta I}$; per battery $\dfrac{E}{3}$ and $\dfrac{R_\text{s}}{3}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $E = 4.63\,\text{V}$ and $R_\text{s} = -\dfrac{3.75\,\text{V} - 4.63\,\text{V}}{1.20\,\text{A} - 0\,\text{A}} = \dfrac{0.88\,\text{V}}{1.20\,\text{A}} = 0.733\,\Omega$; per battery $\dfrac{4.63\,\text{V}}{3} = 1.54\,\text{V}$ and $\dfrac{0.733\,\Omega}{3} = 0.244\,\Omega$
**Answer:** The emf is $E \approx 4.63\,\text{V}$ and the internal resistance $R_\text{s} \approx 0.73\,\Omega$. The internal resistance is given to two significant figures, because the change in voltage $0.88\,\text{V}$ is read from the graph to about a hundredth.
**Reasonableness:** Per battery, $1.54\,\text{V}$ and $0.24\,\Omega$ are typical values of a new AA battery. The $4.56\,\text{V}$ measured at the smallest current is a little below the emf, as it should be.

### c)
**Given:** $E \approx 4.63\,\text{V}$ and $R_\text{s} \approx 0.733\,\Omega$ (part b), largest measured current $1.00\,\text{A}$
**Find:** the short-circuit current $I_\text{k}$, why it was not measured and how reliable the result is
**Principle:** In a short circuit the resistance of the external circuit is zero, so the current is limited only by the internal resistance (chapter *Electromotive force and internal resistance*). In the graph the short-circuit current is the intersection of the line with the horizontal axis, where the terminal voltage is zero.
**Formula:** $I_\text{k} = \dfrac{E}{R_\text{s}}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $I_\text{k} = \dfrac{4.63\,\text{V}}{0.733\,\Omega} = 6.31\,\text{A}$

<svg data-fig="fy9-tasavirta-s3-ik" viewBox="0 0 600 400" role="img" aria-label="Graph: the terminal voltage U in volts as a function of the current I in amperes, axes from zero. The measured points are on the left at currents of 0–1 A. The fitted line continues as a dashed line outside the measuring range and crosses the horizontal axis at the short-circuit current, at about 6.3 amperes, more than six times the largest measured current." style="max-width:100%;font-size:30px">
  <line x1="145.5" y1="340" x2="145.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201.5" y1="340" x2="201.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="257" y1="340" x2="257" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="340" x2="313" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368.5" y1="340" x2="368.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="424.5" y1="340" x2="424.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="340" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="284" x2="480" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="228" x2="480" y2="228" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="172" x2="480" y2="172" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="116" x2="480" y2="116" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="480" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="340" x2="494" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,340 L493,346 L493,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="341" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145.5" y1="340" x2="145.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="133.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="201.5" y1="340" x2="201.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="189.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="257" y1="340" x2="257" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="313" y1="340" x2="313" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="301" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="368.5" y1="340" x2="368.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="356.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$5$</div></foreignObject>
  <line x1="424.5" y1="340" x2="424.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412.5" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$6$</div></foreignObject>
  <line x1="480" y1="340" x2="480" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="468" y="346" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$7$</div></foreignObject>
  <line x1="83" y1="284" x2="90" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="266" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$1$</div></foreignObject>
  <line x1="83" y1="228" x2="90" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="210" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$2$</div></foreignObject>
  <line x1="83" y1="172" x2="90" y2="172" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="154" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$3$</div></foreignObject>
  <line x1="83" y1="116" x2="90" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="98" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$4$</div></foreignObject>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="42" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$5$</div></foreignObject>
  <foreignObject x="56" y="342" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:30px">$0$</div></foreignObject>
  <foreignObject x="512" y="322" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="80" y="0" width="75" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px">$U\ (\text{V})$</div></foreignObject>
  <polygon points="90,340 145.5,340 145.5,60 90,60" fill="#d0e6fb" fill-opacity="0.5"/>
  <polyline points="90,81 145.5,121.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="145.5,121.5 444,340" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <circle cx="95.5" cy="84.5" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="104" cy="92" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="112.5" cy="97" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="123.5" cy="106" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="134.5" cy="112.5" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="145.5" cy="122" r="5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="444" cy="340" r="7" fill="#c92a2a"/>
  <foreignObject x="380" y="255" width="133" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I_\text{k} \approx 6.3\,\text{A}$</span></div></foreignObject>
  <foreignObject x="154" y="260.5" width="226" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{measuring range}$</span></div></foreignObject>
</svg>

**Answer:** The short-circuit current would be about $I_\text{k} \approx 6.3\,\text{A}$, two significant figures like the internal resistance. It was not measured, because in a short circuit the batteries would heat up quickly and could be damaged. The result is only an estimate: it is an extrapolation to more than six times the current, outside the measuring range, and it assumes that the internal resistance stays the same at large currents too.
**Reasonableness:** The line extended in the graph crosses the axis at the same place, about $6.3\,\text{A}$. The short-circuit current of a new AA battery is a few amperes, so the result is credible. In reality the chemistry of the batteries cannot keep up with a large current, and the voltage falls more than the model predicts, so the real current would probably be smaller.

### d)
**Given:** resistance of the bulb $R = 3.6\,\Omega$, $E \approx 4.63\,\text{V}$ and $R_\text{s} \approx 0.733\,\Omega$ (part b)
**Find:** the power $P$ transferred to the bulb and its fraction of the source power $EI$
**Principle:** The bulb and the internal resistance are in series in the same loop, so the current is set by the sum of their resistances (chapter *Electromotive force and internal resistance*). The power of the bulb is obtained from its resistance and current with Joule's law, and the source produces electrical energy at the power $EI$ (chapter *Electric power and the heating of a resistor*).
**Formula:** $I = \dfrac{E}{R + R_\text{s}}$, $P = RI^2$ and the fraction $\dfrac{P}{EI}$
**Conversions:** The quantities are in base units, so no conversions are needed.
**Substitution:** $I = \dfrac{4.63\,\text{V}}{3.6\,\Omega + 0.733\,\Omega} = 1.069\,\text{A}$, $P = 3.6\,\Omega \cdot (1.069\,\text{A})^2 = 4.11\,\text{W}$, $EI = 4.63\,\text{V} \cdot 1.069\,\text{A} = 4.95\,\text{W}$ and $\dfrac{4.11\,\text{W}}{4.95\,\text{W}} = 0.831$
**Answer:** The power transferred to the bulb is $P \approx 4.1\,\text{W}$, which is about $83\,\%$ of the source power. The precision is two significant figures like the resistance of the bulb $3.6\,\Omega$.
**Reasonableness:** The internal resistance takes $0.733\,\Omega \cdot (1.069\,\text{A})^2 \approx 0.84\,\text{W}$, and $4.11\,\text{W} + 0.84\,\text{W} = 4.95\,\text{W}$, as conservation of energy requires. The fraction is also $\tfrac{R}{R + R_\text{s}} = \tfrac{3.6}{4.33} \approx 0.83$. The current $1.07\,\text{A}$ is slightly above the measuring range, so the model probably holds well for it.

### Yleisiä virheitä
- In part a the points are joined into a broken line, or the vertical axis is broken without marking the break.
- In part b the terminal voltage at the smallest current, $4.56\,\text{V}$, is given as the emf, or the slope is calculated from two measured points instead of the line.
- In part b the internal resistance is calculated as the ratio $\tfrac{U}{I}$ of one measurement, which is the resistance of the load resistor.
- In part c the short-circuit current is calculated from the terminal voltage, or the result is considered as reliable as the measured values.
- In part d the internal resistance is forgotten, so that $I = \tfrac{4.63\,\text{V}}{3.6\,\Omega} = 1.29\,\text{A}$ and $P = 5.95\,\text{W}$.

### Hyväksytään myös
- In part b the equation of the fitted line with a calculator: $U = 4.625\,\text{V} - 0.727\,\Omega \cdot I$, so $E \approx 4.63\,\text{V}$ and $R_\text{s} \approx 0.73\,\Omega$.
- In part d the power from the terminal voltage: $U = E - R_\text{s} I = 3.85\,\text{V}$ and $P = UI \approx 4.1\,\text{W}$.

## fy9-tasavirta-s4

### a)
**Find:** whether claim 1 is true and how much power is transformed into internal energy in the $15\,\text{m}$ extension cord
**Principle:** Current is not used up: the same charge passes along the cord to the device and returns along the other conductor (chapter *Electric circuit, current and voltage*). The conductors have the resistance $R = \rho\,\tfrac{l}{A}$ (chapter *Resistance and Ohm's law*), and in a resistance electrical energy is transformed into internal energy at the power $P = RI^2$ (chapter *Electric power and the heating of a resistor*).
**Model answer:** The claim is wrong. No current is used up in the cord: the current going to the device and the current returning from it are equal. The cord heats up because in its resistance electrical energy is transformed into internal energy at the power $P = RI^2$. The current passes through two conductors, so the distance is $2 \cdot 15\,\text{m} = 30\,\text{m}$, and $R = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \tfrac{30\,\text{m}}{0.75 \cdot 10^{-6}\,\text{m}^2} = 0.68\,\Omega$. With a current of $10\,\text{A}$ the power is $0.68\,\Omega \cdot (10\,\text{A})^2 = 68\,\text{W}$, like a small heater inside the cord. The resistance is proportional to the length and inversely proportional to the cross-sectional area, so a thin cord heats up equally much per unit length whether it is short or long. The power grows as the square of the current, so the decisive factor is a large current: a thin cord is dangerous with a large current even when it is short, and especially when it is wound on a reel, so that the heat cannot escape. A thicker cord of $1.5\,\text{mm}^2$ would halve the power to $34\,\text{W}$.

### b)
**Find:** whether claim 2 is true when a $2000\,\text{W}$ kettle and an $850\,\text{W}$ toaster are on the same $10\,\text{A}$ circuit
**Principle:** The sockets of a home are connected in parallel, so the mains voltage is across every device (chapter *Resistors in series and in parallel*). The current of a heating device is $I = \tfrac{P}{U}$ (chapter *Electrical energy at home*). The wiring of the circuit carries the sum of the currents of the branches (chapter *Kirchhoff's laws and potential in a circuit*).
**Model answer:** The claim is wrong. The sockets are in parallel, so the voltage across every device is $230\,\text{V}$, and a device takes its own current $I = \tfrac{P}{U}$ regardless of the other devices. The kettle takes $\tfrac{2000\,\text{W}}{230\,\text{V}} = 8.7\,\text{A}$ and the toaster $\tfrac{850\,\text{W}}{230\,\text{V}} = 3.7\,\text{A}$ whether or not the other one is on. By the current law the wiring of the circuit carries their sum $12.4\,\text{A}$, which exceeds the $10\,\text{A}$ of the fuse. The fuse cuts off the current, because too large a current would heat the wiring of the circuit (power $RI^2$). So a new device does not reduce the current of the others but increases the total current of the circuit, and that is exactly why a circuit must not be overloaded.

### c)
**Find:** whether claim 3 is true, and how large the voltage between the bird's feet is
**Principle:** The current through the body is driven by the potential difference, that is, the voltage, between the two points where the body is in contact (chapter *Kirchhoff's laws and potential in a circuit*). In a conductor the potential falls by $RI$ in the direction of the current, and the resistance of a short piece of conductor is $R = \rho\,\tfrac{l}{A}$ (chapter *Resistance and Ohm's law*).
**Model answer:** The claim is true. The piece of line between the bird's feet is $4.0\,\text{cm}$ long, so its resistance is $2.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot \tfrac{0.040\,\text{m}}{400 \cdot 10^{-6}\,\text{m}^2} = 2.7 \cdot 10^{-6}\,\Omega$, and the voltage between the feet is $2.7 \cdot 10^{-6}\,\Omega \cdot 600\,\text{A} \approx 1.6\,\text{mV}$. Such a small voltage drives hardly any current through the bird's body, although the whole bird is, together with the line, at a high potential relative to the earth. The pylon is at the potential of the earth. If the bird touches it at the same time, almost the whole voltage between the line and the earth, tens or hundreds of kilovolts, is across its body, and a dangerous current passes through the body. So what is dangerous is not a high potential but a large potential difference between two points of the body.

### Yleisiä virheitä
- In part a the length of the cord is taken as $15\,\text{m}$, although the current passes through two conductors, or square millimetres are not converted into square metres.
- In part a the power is calculated with the mains voltage, $\tfrac{(230\,\text{V})^2}{0.68\,\Omega}$, although only $RI \approx 6.8\,\text{V}$ is across the cord.
- In part b the devices are assumed to be in series, in which case a new device would reduce the current.
- In part c the argument is that the bird's feet insulate it, or that the voltage of the line is small.

## fy9-tasavirta-s5

### a)
**Given:** measurement 1: $U = 0.51\,\text{V}$ on the $20\,\text{V}$ range (resolution $0.01\,\text{V}$, $\pm(0.5\,\% + 2\ \text{digits})$) and $I = 5.3\,\text{mA}$ on the $200\,\text{mA}$ range (resolution $0.1\,\text{mA}$, $\pm(1.0\,\% + 2\ \text{digits})$)
**Find:** the resistance $R$ of measurement 1 and its error limit $\Delta R$
**Principle:** The resistance is the ratio of the voltage to the current (chapter *Resistance and Ohm's law*). The error limit of each meter is a percentage of the reading plus the number of digits times the resolution (chapter *Measurements in an electric circuit*). The largest possible value of the resistance is obtained from the largest voltage and the smallest current, and the smallest the other way round (chapter *Measuring and the reliability of a measurement*).
**Formula:** $R = \dfrac{U}{I}$, $\Delta x = p \cdot x + n \cdot r$, $R_\text{min} = \dfrac{U - \Delta U}{I + \Delta I}$ and $R_\text{max} = \dfrac{U + \Delta U}{I - \Delta I}$
**Conversions:** $5.3\,\text{mA} = 5.3 \cdot 0.001\,\text{A} = 0.0053\,\text{A}$ and $0.1\,\text{mA} = 0.0001\,\text{A}$
**Substitution:** $\Delta U = 0.005 \cdot 0.51\,\text{V} + 2 \cdot 0.01\,\text{V} = 0.0226\,\text{V}$, $\Delta I = 0.010 \cdot 5.3\,\text{mA} + 2 \cdot 0.1\,\text{mA} = 0.253\,\text{mA}$, $R = \dfrac{0.51\,\text{V}}{0.0053\,\text{A}} = 96.2\,\Omega$, $R_\text{min} = \dfrac{0.4874\,\text{V}}{0.005553\,\text{A}} = 87.8\,\Omega$ and $R_\text{max} = \dfrac{0.5326\,\text{V}}{0.005047\,\text{A}} = 105.5\,\Omega$
**Answer:** The resistance of measurement 1 is $R = (96 \pm 9)\,\Omega$, so according to the error limits of the meters the true value is probably between about $88$ and $106\,\Omega$. The error limit is given to one significant figure and the result to the same precision.
**Reasonableness:** The relative error limits are $\tfrac{0.0226}{0.51} \approx 4.4\,\%$ and $\tfrac{0.253}{5.3} \approx 4.8\,\%$, and the relative error limit of a quotient is their sum, about $9.2\,\%$, that is, $9\,\Omega$, the same result. For small readings the digits part $2 \cdot r$ is large, so the error limit is large.

### b)
**Find:** whether the group's conclusion is justified
**Principle:** A difference between two results is real only if it is larger than the error limits of the results (chapter *Measuring and the reliability of a measurement*). In the error limit of a meter the digits part matters more the smaller the reading is compared with the range (chapter *Measurements in an electric circuit*). The resistance of a metal and of a carbon film changes mainly with temperature (chapter *Resistance and Ohm's law*).
**Model answer:** The conclusion is not justified. Calculated in the same way, the resistance of measurement 2 is $(100 \pm 4)\,\Omega$ and that of measurement 3 $(102 \pm 3)\,\Omega$, and the result of measurement 1 is $(96 \pm 9)\,\Omega$. All three intervals include the value $100\,\Omega$, so the resistances do not differ from each other within the measurement precision. The largest deviation is in measurement 1, in which the readings $0.51\,\text{V}$ and $5.3\,\text{mA}$ are small compared with the ranges, so the digits part dominates the error limit. Heating could change the resistance, but the power of the resistor is at most only $3.02\,\text{V} \cdot 29.6\,\text{mA} \approx 0.09\,\text{W}$, so the resistor hardly heats up. So the data fit a constant resistance of about $100\,\Omega$, and it cannot be concluded from three imprecise points that the resistance depends on the voltage.

### c)
**Find:** how the measurement is improved so that the validity of Ohm's law can be established reliably
**Principle:** A dependence is established most reliably from a graph in which a straight line has been fitted to many points (chapter *Graphing and fitting a straight line*). The error limit of a meter is smallest when the smallest range on which the reading fits is used (chapter *Measurements in an electric circuit*). Ohm's law concerns a constant temperature, so the temperature must be kept constant (chapter *Resistance and Ohm's law*).
**Model answer:** At least eight points are measured over a wide voltage range, for example $0.5$–$10\,\text{V}$, and an $(I, U)$ graph is drawn. If the resistor obeys Ohm's law, the points lie on a straight line through the origin whose slope is $R$; a deviation from the line shows better in a graph than in three ratios. Each reading is taken on the smallest range on which it fits: for example $0.510\,\text{V}$ on the $2\,\text{V}$ range gives the error limit $0.005 \cdot 0.510\,\text{V} + 2 \cdot 0.001\,\text{V} \approx 0.005\,\text{V}$, that is, about $0.9\,\%$. The temperature is kept constant: the power of the resistor is kept small, the readings are taken quickly, and the voltage is both increased and decreased, so that any effect of heating would show as differences. The ammeter is kept in series and the voltmeter in parallel with the resistor, and the effect of the meters is assessed: the resistance of the voltmeter is of the order of megohms, that is, much larger than $100\,\Omega$, so a negligibly small current passes through it. The result is given with its error limits.

### Yleisiä virheitä
- In part a the error limit is calculated from the percentage alone, so that the digits part $n \cdot r$ is forgotten and the error limit is too small.
- In part a milliamperes are not converted into amperes, so that the resistance is wrong by a factor of a thousand.
- In part b the conclusion is accepted because the numbers increase, without comparing the difference with the error limits.
- In part c the only suggestion is to repeat the measurements in the same way, which does not reduce the error limit of the meter.

### Hyväksytään myös
- In part a the error limit as the sum of the relative error limits $\tfrac{\Delta R}{R} = \tfrac{\Delta U}{U} + \tfrac{\Delta I}{I} \approx 9\,\%$.

## fy9-tasavirta-s6

### a)
**Given:** volume of the water $300\,\text{l}$, so the mass $m = 300\,\text{kg}$; temperatures $15\,{}^\circ\text{C}$ and $70\,{}^\circ\text{C}$; power $P = 3.0\,\text{kW}$; $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Find:** the heating time $t$
**Principle:** In the resistor electrical energy is transformed into internal energy (chapter *Electric power and the heating of a resistor*), and from the resistor it is transferred as heat to the water. The efficiency of a resistive heater is practically $100\,\%$, and when the heat losses are ignored, all the electrical energy heats the water (chapter *Heating and cooling of matter*). The power is constant, so the energy is the power times the time.
**Formula:** $Pt = cm\Delta T$, so $t = \dfrac{cm\Delta T}{P}$
**Conversions:** $3.0\,\text{kW} = 3.0 \cdot 1000\,\text{W} = 3000\,\text{W}$; the change in temperature $70\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 55\,{}^\circ\text{C} = 55\,\text{K}$; finally $1\,\text{h} = 3600\,\text{s}$
**Substitution:** $Q = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 300\,\text{kg} \cdot 55\,\text{K} = 6.914 \cdot 10^{7}\,\text{J}$ and $t = \dfrac{6.914 \cdot 10^{7}\,\text{J}}{3000\,\text{W}} = 23\,045\,\text{s} = 6.40\,\text{h}$
**Answer:** The heating takes about $t \approx 6.4\,\text{h}$, two significant figures like the power $3.0\,\text{kW}$.
**Reasonableness:** The energy received by the water is $\tfrac{6.914 \cdot 10^{7}\,\text{J}}{3.6 \cdot 10^{6}\,\text{J/kWh}} = 19.2\,\text{kWh}$, and $3.0\,\text{kW} \cdot 6.4\,\text{h} = 19.2\,\text{kWh}$. The heating fits into the night hours, and it costs about $19.2\,\text{kWh} \cdot 0.14\,\tfrac{\text{€}}{\text{kWh}} \approx 2.7\,\text{€}$. Heat losses lengthen the time slightly.

### b)
**Given:** heat loss $E = 1.6\,\text{kWh}$ per day, price $a = 14\,\text{c/kWh}$
**Find:** the average power $P$ of the losses and the annual cost $K$
**Principle:** The average power is the energy divided by the time (chapter *Electric power and the heating of a resistor*). The thermostat of the heater replaces the losses with electricity, so the lost energy costs the same as electricity (chapter *Electrical energy at home*).
**Formula:** $P = \dfrac{E}{t}$ and $K = a \cdot 365E$
**Conversions:** $1.6\,\text{kWh} = 1600\,\text{Wh}$, $1\,\text{d} = 24\,\text{h}$ and $14\,\text{c/kWh} = 0.14\,\text{€/kWh}$
**Substitution:** $P = \dfrac{1600\,\text{Wh}}{24\,\text{h}} = 66.7\,\text{W}$, in a year $365 \cdot 1.6\,\text{kWh} = 584\,\text{kWh}$ and $K = 0.14\,\tfrac{\text{€}}{\text{kWh}} \cdot 584\,\text{kWh} = 81.8\,\text{€}$
**Answer:** The average power of the losses is $P \approx 67\,\text{W}$, and the losses cost about $82\,\text{€}$ a year. The precision is two significant figures like the loss $1.6\,\text{kWh}$ and the price $14\,\text{c/kWh}$.
**Reasonableness:** The loss power is only $2\,\%$ of the power of the resistor, but it continues round the clock, so in a year it adds up to as much energy as a month of hot water. In winter the lost heat warms the house, so it is not entirely wasted.

### c)
**Given:** power $P = 3.0\,\text{kW}$ at the voltage $U = 230\,\text{V}$, new voltage $U' = 220\,\text{V}$, resistance assumed to be the same
**Find:** the power $P'$ of the resistor at a voltage of $220\,\text{V}$
**Principle:** The power marked on a device is the power at the rated voltage, and it gives the resistance of the resistor. When the resistance stays the same, the power of the resistor is proportional to the square of the voltage (chapter *Electric power and the heating of a resistor*).
**Formula:** $R = \dfrac{U^2}{P}$ and $P' = \dfrac{U'^2}{R} = P\left(\dfrac{U'}{U}\right)^2$
**Conversions:** $3.0\,\text{kW} = 3000\,\text{W}$ and finally $1\,\text{kW} = 1000\,\text{W}$
**Substitution:** $R = \dfrac{(230\,\text{V})^2}{3000\,\text{W}} = 17.63\,\Omega$ and $P' = \dfrac{(220\,\text{V})^2}{17.63\,\Omega} = 2745\,\text{W} = 2.74\,\text{kW}$
**Answer:** The power is about $P' \approx 2.7\,\text{kW}$, two significant figures like the power $3.0\,\text{kW}$.
**Reasonableness:** The voltage decreases by $4.3\,\%$, and the power by about twice as much, $8.5\,\%$, as the square dependence gives. The heating would take about $\tfrac{19.2\,\text{kWh}}{2.74\,\text{kW}} \approx 7.0\,\text{h}$, but the same amount of energy is used.

### d)
**Given:** duration of the shower $10\,\text{min}$, water flow $8.0\,\text{l/min}$, temperature of the shower water $40\,{}^\circ\text{C}$, temperature of the cold water $15\,{}^\circ\text{C}$, $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Find:** the electrical energy $E$ needed for the hot water of the shower
**Principle:** The shower water has been heated from $15\,{}^\circ\text{C}$ to $40\,{}^\circ\text{C}$, so the energy it has received is $cm\Delta T$ (chapter *Heating and cooling of matter*). The same energy has come from the resistor of the heater as electrical energy, because the efficiency of the resistor is practically $100\,\%$; it does not matter whether water at $70\,{}^\circ\text{C}$ is mixed with cold water, because the end result is the same amount of water at $40\,{}^\circ\text{C}$.
**Formula:** $E = cm\Delta T$
**Conversions:** $m = 10 \cdot 8.0\,\text{kg} = 80\,\text{kg}$, $\Delta T = 40\,{}^\circ\text{C} - 15\,{}^\circ\text{C} = 25\,\text{K}$ and finally $1\,\text{kWh} = 3.6 \cdot 10^{6}\,\text{J}$
**Substitution:** $E = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 80\,\text{kg} \cdot 25\,\text{K} = 8.38 \cdot 10^{6}\,\text{J} = \dfrac{8.38 \cdot 10^{6}\,\text{J}}{3.6 \cdot 10^{6}\,\text{J/kWh}} = 2.33\,\text{kWh}$
**Answer:** The shower corresponds to about $E \approx 2.3\,\text{kWh}$ of electrical energy, two significant figures like the water flow $8.0\,\text{l/min}$.
**Reasonableness:** The shower costs about $2.33\,\text{kWh} \cdot 0.14\,\tfrac{\text{€}}{\text{kWh}} \approx 33\,\text{c}$. A full heater ($19.2\,\text{kWh}$) is enough for about $\tfrac{19.2}{2.33} \approx 8$ such showers; the same result is reached by noticing that about $36\,\text{l}$ of water at $70\,{}^\circ\text{C}$ is needed for the shower water.

### Yleisiä virheitä
- In part a the power is left in kilowatts and the energy in joules, so that the time is wrong by a factor of a thousand, or the change in temperature is taken as $70\,{}^\circ\text{C}$.
- In part b the loss power is calculated by dividing $1.6\,\text{kWh}$ by the number of seconds in a day, leaving the units mixed.
- In part c the power is assumed to be directly proportional to the voltage, which gives $2.87\,\text{kW}$.
- In part d the change in temperature is taken as $70\,{}^\circ\text{C} - 40\,{}^\circ\text{C}$, or litres are not converted into kilograms.

### Hyväksytään myös
- In part a the energy in kilowatt-hours: $19.2\,\text{kWh} : 3.0\,\text{kW} = 6.4\,\text{h}$.
