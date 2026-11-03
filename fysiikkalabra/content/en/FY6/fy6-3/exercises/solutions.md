## fy6-3-L1-01
**Given:** the voltage across the heating element $U = 230\,\text{V}$ and the current $I = 8.7\,\text{A}$
**Find:** the resistance $R$ of the heating element in ohms
**Principle:** Resistance is the ratio of the voltage across a component to the current through it. The given values refer to the same resistor at the same moment, while the kettle is on, so the ratio gives the resistance of the element at its operating temperature.
**Formula:** $R = \dfrac{U}{I}$
**Conversions:** Not needed: the voltage is in volts and the current in amperes, and $1\,\text{V/A} = 1\,\Omega$.
**Substitution:** $R = \dfrac{230\,\text{V}}{8.7\,\text{A}} = 26.44\,\Omega$
**Answer:** $26\,\Omega$, two significant figures like the current $8.7\,\text{A}$.
**Reasonableness:** Estimate: $230\,\text{V} : 10\,\text{A} = 23\,\Omega$; the current is a little under $10\,\text{A}$, so the resistance is a little over $23\,\Omega$. Check with Ohm's law: $26.44\,\Omega \cdot 8.7\,\text{A} = 230\,\text{V}$.

## fy6-3-L1-02
**Given:** the resistance of the resistor $R = 220\,\Omega$ and the current $I = 15\,\text{mA}$
**Find:** the voltage $U$ across the resistor in volts
**Principle:** The resistor obeys Ohm's law, so the voltage is the product of the resistance and the current. The same equation follows from the definition of resistance $R = U : I$ by multiplying both sides by the current.
**Formula:** $R = \dfrac{U}{I}$, so $U = R I$
**Conversions:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A} = 0.015\,\text{A}$
**Substitution:** $U = 220\,\Omega \cdot 0.015\,\text{A} = 3.3\,\text{V}$
**Answer:** $3.3\,\text{V}$, two significant figures like the current $15\,\text{mA}$.
**Reasonableness:** An ohm times an ampere is a volt, so the unit is correct. Estimate: $200\,\Omega \cdot 0.015\,\text{A} = 3\,\text{V}$, and the exact result is a little larger, as it should be. In electronics, voltages of a few volts like this are common.

## fy6-3-L1-03
**Given:** the resistance of the heating wires $R = 1.2\,\Omega$ and the voltage $U = 12\,\text{V}$
**Find:** the current $I$ through the wires in amperes
**Principle:** The current in a heating wire follows from the definition of resistance when the voltage and the resistance are known. The given resistance applies to the wires in use.
**Formula:** $R = \dfrac{U}{I}$, so $I = \dfrac{U}{R}$
**Conversions:** Not needed: the voltage is in volts and the resistance in ohms, and $1\,\text{V}/\Omega = 1\,\text{A}$.
**Substitution:** $I = \dfrac{12\,\text{V}}{1.2\,\Omega} = 10\,\text{A}$
**Answer:** $10\,\text{A}$, two significant figures like the voltage and the resistance.
**Reasonableness:** The resistance is small, so the current is large. Check: $1.2\,\Omega \cdot 10\,\text{A} = 12\,\text{V}$. The rear window heater is indeed one of the biggest electricity users in a car, and it has a fuse of its own.

## fy6-3-L1-04
**Given:** copper conductor, $l = 25\,\text{m}$, $A = 2.5\,\text{mm}^2$, $\rho = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$
**Find:** the resistance $R$ of the conductor in ohms
**Principle:** The conductor is uniform copper, so its resistance is directly proportional to its length and inversely proportional to its cross-sectional area. The constant of proportionality is the resistivity of copper.
**Formula:** $R = \rho \dfrac{l}{A}$
**Conversions:** $A = 2.5\,\text{mm}^2 = 2.5 \cdot (10^{-3}\,\text{m})^2 = 2.5 \cdot 10^{-6}\,\text{m}^2$
**Substitution:** $R = \dfrac{1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 25\,\text{m}}{2.5 \cdot 10^{-6}\,\text{m}^2} = 0.17\,\Omega$
**Answer:** $0.17\,\Omega$, two significant figures like the data.
**Reasonableness:** Units: $\Omega\cdot\text{m} \cdot \text{m} : \text{m}^2 = \Omega$. The resistance of an electric cable should indeed be small, under an ohm, so that the cable does not heat up. One metre of this conductor has a resistance of $0.0068\,\Omega$, and $25 \cdot 0.0068\,\Omega = 0.17\,\Omega$.

## fy6-3-L1-05
**Given:** the voltage between the electrodes $U = 5.0\,\text{V}$ and the current $I = 2.0\,\text{mA}$
**Find:** the resistance $R$ of the soil in kilohms
**Principle:** Between the electrodes the soil is a component of the circuit, and its resistance is the ratio of the voltage to the current at the same moment.
**Formula:** $R = \dfrac{U}{I}$
**Conversions:** $I = 2.0\,\text{mA} = 2.0 \cdot 10^{-3}\,\text{A}$. Finally $1\,\text{k}\Omega = 1000\,\Omega$.
**Substitution:** $R = \dfrac{5.0\,\text{V}}{2.0 \cdot 10^{-3}\,\text{A}} = 2500\,\Omega = 2.5\,\text{k}\Omega$
**Answer:** $2.5\,\text{k}\Omega$, two significant figures like the voltage and the current.
**Reasonableness:** The current is only milliamperes, so the resistance is large, thousands of ohms. Moist soil conducts electricity better than dry soil, so as the soil dries the resistance increases and the current decreases: this is how the sensor works.

## fy6-3-L2-01
**Given:** at first $U_1 = 6.0\,\text{V}$ and $I_1 = 0.25\,\text{A}$; at the end $U_2 = 9.0\,\text{V}$; the temperature stays the same
**Find:** the current $I_2$ at the voltage $9.0\,\text{V}$
**Principle:** The temperature of the resistor stays the same, so it obeys Ohm's law and its resistance is the same at both voltages. The resistance is calculated from the first measurement and used for the second.
**Formula:** $R = \dfrac{U_1}{I_1}$ and $I_2 = \dfrac{U_2}{R}$
**Conversions:** Not needed: the voltages are in volts and the current in amperes.
**Substitution:** $R = \dfrac{6.0\,\text{V}}{0.25\,\text{A}} = 24\,\Omega$ and $I_2 = \dfrac{9.0\,\text{V}}{24\,\Omega} = 0.375\,\text{A}$
**Answer:** $0.38\,\text{A}$, two significant figures like the voltages and the current $0.25\,\text{A}$.
**Reasonableness:** The voltage becomes 1.5 times as large ($9.0\,\text{V} : 6.0\,\text{V} = 1.5$), so by Ohm's law the current also becomes 1.5 times as large: $1.5 \cdot 0.25\,\text{A} = 0.375\,\text{A}$. The result is the same.

## fy6-3-L2-02
**Given:** the characteristic curve of a filament lamp as an $(I, U)$ graph; the voltage $U = 1.0\,\text{V}$
**Find:** the resistance $R$ of the lamp at the voltage $1.0\,\text{V}$
**Principle:** Resistance is the ratio of voltage to current at the same point of the curve. The lamp does not obey Ohm's law, so the resistance must be read exactly at this voltage, not from the steepness of the curve nor from another point.
**Reading the graph:** On the vertical axis we find $U = 1.0\,\text{V}$ and go horizontally to the curve. The point on the curve is at $I = 0.15\,\text{A}$ on the horizontal axis, halfway between the grid lines $0.10\,\text{A}$ and $0.20\,\text{A}$.
**Formula:** $R = \dfrac{U}{I}$
**Conversions:** Not needed: the voltage is in volts and the current in amperes.
**Substitution:** $R = \dfrac{1.0\,\text{V}}{0.15\,\text{A}} = 6.67\,\Omega$
**Answer:** $6.7\,\Omega$, two significant figures, because the current is read from the graph to about $0.005\,\text{A}$.
**Reasonableness:** The resistance of the lamp increases as the wire gets hotter. At the voltage $3.0\,\text{V}$ the curve gives $0.25\,\text{A}$ and a resistance of $12\,\Omega$, so at a smaller voltage the value $6.7\,\Omega$ is sensibly smaller.

## fy6-3-L2-03
**Given:** copper conductor, $l = 50\,\text{m}$, $\rho = 1.7 \cdot 10^{-8}\,\Omega\cdot\text{m}$; resistance at most $R = 0.50\,\Omega$
**Find:** the smallest cross-sectional area $A$ in square millimetres
**Principle:** The resistance of a uniform conductor is inversely proportional to its cross-sectional area, so the largest allowed resistance gives the smallest allowed cross-sectional area.
**Formula:** $R = \rho \dfrac{l}{A}$, so $A = \dfrac{\rho l}{R}$
**Conversions:** The result comes out in square metres, and $1\,\text{m}^2 = (10^3\,\text{mm})^2 = 10^6\,\text{mm}^2$.
**Substitution:** $A = \dfrac{1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 50\,\text{m}}{0.50\,\Omega} = 1.7 \cdot 10^{-6}\,\text{m}^2 = 1.7 \cdot 10^{-6} \cdot 10^6\,\text{mm}^2 = 1.7\,\text{mm}^2$
**Answer:** $1.7\,\text{mm}^2$, two significant figures like the data.
**Reasonableness:** Units: $\Omega\cdot\text{m} \cdot \text{m} : \Omega = \text{m}^2$. Check: $1.7 \cdot 10^{-8}\,\Omega\cdot\text{m} \cdot 50\,\text{m} : (1.7 \cdot 10^{-6}\,\text{m}^2) = 0.50\,\Omega$. Conductors in homes are typically $1.5$–$2.5\,\text{mm}^2$, so the result is of the usual size.

## fy6-3-L2-04
**Given:** constantan wire, diameter $d = 0.40\,\text{mm}$, length $l = 2.0\,\text{m}$, $\rho = 5.0 \cdot 10^{-7}\,\Omega\cdot\text{m}$
**Find:** the resistance $R$ of the wire in ohms
**Principle:** The wire is uniform, so $R = \rho l : A$. The cross-section is a circle, so the cross-sectional area is calculated from the radius, which is half the diameter.
**Formula:** $A = \pi r^2 = \pi \left(\dfrac{d}{2}\right)^2$ and $R = \dfrac{\rho l}{A}$
**Conversions:** $d = 0.40\,\text{mm} = 0.40 \cdot 10^{-3}\,\text{m}$, so $r = 0.20 \cdot 10^{-3}\,\text{m}$.
**Substitution:** $A = \pi \cdot (0.20 \cdot 10^{-3}\,\text{m})^2 = 1.257 \cdot 10^{-7}\,\text{m}^2$ and $R = \dfrac{5.0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 2.0\,\text{m}}{1.257 \cdot 10^{-7}\,\text{m}^2} = 7.96\,\Omega$
**Answer:** $8.0\,\Omega$, two significant figures like the diameter, the length and the resistivity.
**Reasonableness:** The cross-sectional area is about $0.13\,\text{mm}^2$, a little more than that of the thinnest wire in the simulation ($0.10\,\text{mm}^2$). In the simulation $1.00\,\text{m}$ of wire with a cross-sectional area of $0.10\,\text{mm}^2$ has $5.0\,\Omega$, so $2.0\,\text{m}$ of slightly thicker wire has a little under $10\,\Omega$.

## fy6-3-L3-01
**Given:** original resistance $R_1 = 0.80\,\Omega$; the length doubles, $l_2 = 2 l_1$; the volume is conserved
**Find:** the resistance $R_2$ of the stretched wire
**Principle:** The wire is of the same material and uniform, so $R = \rho l : A$. The volume $V = A l$ stays the same, so when the length doubles, the cross-sectional area is halved. Both changes increase the resistance: the length doubles it, and the half-size cross-sectional area doubles it again. So the resistance changes more than the length.
**Formula:** $R_1 = \rho \dfrac{l_1}{A_1}$ and $R_2 = \rho \dfrac{l_2}{A_2}$, where $l_2 = 2 l_1$ and $A_2 = \dfrac{A_1}{2}$, so $R_2 = \rho \dfrac{2 l_1}{A_1 / 2} = 4 R_1$
**Conversions:** Not needed: the resistances are in ohms, and the comparison is made with ratios.
**Substitution:** $R_2 = 4 \cdot 0.80\,\Omega = 3.2\,\Omega$
**Answer:** $3.2\,\Omega$, two significant figures like the original resistance.
**Reasonableness:** The volume is conserved: $2 l_1 \cdot \tfrac{1}{2} A_1 = l_1 A_1$. If the cross-sectional area stayed the same, the result would be only $1.6\,\Omega$; the thinning brings the second doubling. The resistivity does not change, because the material is the same.

## fy6-3-L3-02
**Given:** nichrome wire, $A = 0.20\,\text{mm}^2$, $U = 2.00\,\text{V}$; measurements of $l$ and $I$: $0.40\,\text{m}$ and $0.91\,\text{A}$, $0.80\,\text{m}$ and $0.46\,\text{A}$, $1.20\,\text{m}$ and $0.30\,\text{A}$, $1.60\,\text{m}$ and $0.23\,\text{A}$
**Find:** the resistivity $\rho$ of nichrome in $\mu\Omega\cdot\text{m}$
**Principle:** The resistance for each length is $R = U : I$. The resistance of a uniform wire is $R = \rho l : A$, so $R$ is directly proportional to the length and the ratio $R : l$ is the constant $\rho : A$. In real data sets the points are usually not exactly on the same line because of measurement uncertainty, so all the measurements are used.
**Formula:** $R = \dfrac{U}{I}$ and $R = \rho \dfrac{l}{A}$, so $\rho = \dfrac{R}{l} \cdot A$
**Conversions:** $A = 0.20\,\text{mm}^2 = 0.20 \cdot 10^{-6}\,\text{m}^2$. Finally $10^{-6}\,\Omega\cdot\text{m} = 1\,\mu\Omega\cdot\text{m}$.
**Substitution:** The resistances are $2.00\,\text{V} : 0.91\,\text{A} = 2.20\,\Omega$, $4.35\,\Omega$, $6.67\,\Omega$ and $8.70\,\Omega$, and the ratios $R : l$ are $5.49$, $5.43$, $5.56$ and $5.43\,\Omega/\text{m}$. The slope of the line fitted through the origin is $5.47\,\Omega/\text{m}$, so $\rho = 5.47\,\tfrac{\Omega}{\text{m}} \cdot 0.20 \cdot 10^{-6}\,\text{m}^2 = 1.09 \cdot 10^{-6}\,\Omega\cdot\text{m}$
**Answer:** $1.1\,\mu\Omega\cdot\text{m}$, two significant figures like the cross-sectional area and the currents $0.30\,\text{A}$ and $0.23\,\text{A}$.
**Reasonableness:** The result is the same as the table value for nichrome, $1.1 \cdot 10^{-6}\,\Omega\cdot\text{m}$. The resistance becomes four times as large when the length becomes four times as large ($2.20\,\Omega$ and $8.70\,\Omega$), so the proportionality holds.

## fy6-3-L3-03
**Given:** the resistance of the cold lamp $R_\text{cold} = 1.0\,\Omega$; in use $U = 3.0\,\text{V}$ and $I = 0.25\,\text{A}$
**Find:** the current $I_\text{cold}$ at the moment of switching on at the voltage $3.0\,\text{V}$
**Principle:** At the moment of switching on, the wire is still at room temperature, so its resistance is the value for the cold lamp. The wire heats up only after current has flowed through it for a moment. The current follows from the definition of resistance.
**Formula:** $R_\text{cold} = \dfrac{U}{I_\text{cold}}$, so $I_\text{cold} = \dfrac{U}{R_\text{cold}}$
**Conversions:** Not needed: the voltage is in volts and the resistance in ohms.
**Substitution:** $I_\text{cold} = \dfrac{3.0\,\text{V}}{1.0\,\Omega} = 3.0\,\text{A}$
**Answer:** $3.0\,\text{A}$, two significant figures like the voltage and the resistance.
**Reasonableness:** The resistance of the lit lamp is $3.0\,\text{V} : 0.25\,\text{A} = 12\,\Omega$, which is 12 times the cold value, so the switch-on current is 12 times the operating current $0.25\,\text{A}$. This large current heats the thin wire very quickly, and the thinnest part of the wire heats up most, because there the resistance per unit length is greatest. That is why the wire most often breaks right when the lamp is switched on.
