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

## fy6-3-L1-06
**Find:** what a characteristic curve that is a straight line through the origin tells about the component.
**Principle:** The characteristic curve shows how the voltage and the current depend on each other. If the curve is a straight line through the origin, the voltage is directly proportional to the current: when one doubles, the other doubles too. Then the ratio $R = U : I$ is the same at every point, and the slope of the line is the resistance.
**Model answer:** The component obeys Ohm's law, because the voltage is directly proportional to the current and the resistance $R = U : I$ is constant. The resistance does not increase with the voltage, because then the curve would be curved. The resistance is not zero either: passing through the origin only tells us that at zero voltage the current is also zero. The current and the voltage merely increasing at the same time does not prove proportionality; that is shown only by the ratio $U : I$ being constant.

## fy6-3-L1-07
**Find:** how the resistivity and the resistance differ for two wires of the same metal and the same thickness when one is twice as long.
**Principle:** The resistivity $\rho$ is a property of the material and depends on the material and the temperature, not on the dimensions of the wire. The resistance $R = \rho l : A$ also depends on the length $l$ and the cross-sectional area $A$. A wire twice as long is like two wires one after the other.
**Model answer:** The resistivity is the same, but the resistance of the longer wire is greater because of the length: it is double, because the cross-sectional area and the material are the same and the length is double. The resistivity of the longer wire is not greater, because it does not depend on the dimensions. The resistance is not the same either, because it depends on the length. A longer wire does not give the current more room either: the room for the current is described by the cross-sectional area, and it is the same for both wires.

## fy6-3-L1-08
**Given:** at first $U = 4.5\,\text{V}$ and $I_1 = 0.60\,\text{A}$; the new wire is of the same copper, equally thick and twice as long; the voltage and the temperature stay the same
**Find:** the current $I_2$ through the longer wire
**Principle:** The wire is of the same material and equally thick, so $R = \rho l : A$ is directly proportional to the length. The resistance of a wire twice as long is double. The voltage stays the same, so by the definition of resistance the current is inversely proportional to the resistance.
**Formula:** $R = \dfrac{U}{I}$, so $R_1 = \dfrac{U}{I_1}$, $R_2 = 2 R_1$ and $I_2 = \dfrac{U}{R_2}$
**Conversions:** Not needed: the voltage is in volts, the current in amperes and the resistance in ohms.
**Substitution:** $R_1 = \dfrac{4.5\,\text{V}}{0.60\,\text{A}} = 7.5\,\Omega$, $R_2 = 2 \cdot 7.5\,\Omega = 15\,\Omega$ and $I_2 = \dfrac{4.5\,\text{V}}{15\,\Omega} = 0.30\,\text{A}$
**Answer:** $0.30\,\text{A}$, two significant figures like the voltage and the current.
**Reasonableness:** The resistance doubles and the voltage stays the same, so the current is halved: $0.60\,\text{A} : 2 = 0.30\,\text{A}$. Check: $15\,\Omega \cdot 0.30\,\text{A} = 4.5\,\text{V}$. General rule: $R \propto l$, so at the same voltage $I \propto 1 : l$.

## fy6-3-L2-05
**Given:** the measurement points $(U, I)$ in the table, $U = 1.0\,\text{V}$–$8.0\,\text{V}$ and $I = 6.6\,\text{mA}$–$53.6\,\text{mA}$; the error limit of the multimeter about $\pm 0.5\,\text{mA}$
**Find:** the resistance $R$ of the resistor from the slope of the fitted line and its uncertainty $\Delta R$
**Principle:** The characteristic curve of a resistor is a straight line through the origin, and its slope is the resistance. The measurement points scatter around the line because of measurement uncertainty, so the line is drawn through the middle of the set of points so that there are points on both sides of it. The line does not have to pass through any single point.
**Reading the graph:** The current $I$ is on the horizontal axis and the voltage $U$ on the vertical axis. The fitted line runs from the origin through the middle of the points. The line is drawn on paper or with a graphing program; your own drawing is checked by comparing its reading with this one. A point far from the others is read from the line: when $I = 50.0\,\text{mA}$, the line is at $U = 7.5\,\text{V}$. The farther the reading point is from the origin, the smaller the share of the reading error in the slope.
**Formula:** $R = \dfrac{\Delta U}{\Delta I}$, that is, the slope of the line; the uncertainty $\Delta R \approx \dfrac{R_{\text{max}} - R_{\text{min}}}{2}$, where $R_{\text{max}}$ and $R_{\text{min}}$ are the largest and smallest $U : I$ of the individual points
**Conversions:** $50.0\,\text{mA} = 50.0 \cdot 10^{-3}\,\text{A} = 0.0500\,\text{A}$
**Substitution:** $R = \dfrac{7.5\,\text{V} - 0\,\text{V}}{0.0500\,\text{A} - 0\,\text{A}} = 150\,\Omega$. The values $U : I$ of the points are $152$, $148$, $152$, $149$, $151$, $149$, $151$ and $149\,\Omega$ (smallest $148.1\,\Omega$ and largest $151.5\,\Omega$), so the estimate from the scatter of the points is $\Delta R \approx \dfrac{151.5\,\Omega - 148.1\,\Omega}{2} = 1.7\,\Omega$
**Answer:** $R = 150\,\Omega$, three significant figures, because the uncertainty is only about $2\,\Omega$; the uncertainty is about $\Delta R \approx 2\,\Omega$, that is, $R = (150 \pm 2)\,\Omega$.
**Reasonableness:** All the resistances of the points are between $148\,\Omega$ and $152\,\Omega$, that is, at most about $1.5\,\%$ from the fitted value, so the line describes the measurements well. The scatter matches the error limit of the multimeter: the deviations of the points from the line are at most about $0.4\,\text{mA}$, which is within the error limit $0.5\,\text{mA}$. The voltage across the resistor is $8.0\,\text{V}$ when the current is $53.3\,\text{mA}$: $150\,\Omega \cdot 0.0533\,\text{A} = 8.0\,\text{V}$.

## fy6-3-L2-06
**Given:** the measurement points $(U, I)$ of a filament lamp in the table, $U = 1.0\,\text{V}$–$5.0\,\text{V}$
**Find:** the resistance $R = U : I$ at each voltage, whether the lamp obeys Ohm's law, and the ratio of the resistances at the voltages $5.0\,\text{V}$ and $1.0\,\text{V}$
**Principle:** If the lamp obeyed Ohm's law, the ratio $U : I$ would be the same at all voltages. We calculate the ratio for each point and compare the values. The ratio of the resistances $R_{5.0} : R_{1.0}$ shows how much the resistance changes.
**Formula:** $R = \dfrac{U}{I}$ and the ratio $\dfrac{R_{5.0}}{R_{1.0}}$
**Conversions:** Not needed: the voltage is in volts and the current in amperes.
**Substitution:** $R = 1.0\,\text{V} : 0.098\,\text{A} = 10.2\,\Omega$, $2.0\,\text{V} : 0.146\,\text{A} = 13.7\,\Omega$, $3.0\,\text{V} : 0.187\,\text{A} = 16.0\,\Omega$, $4.0\,\text{V} : 0.221\,\text{A} = 18.1\,\Omega$ and $5.0\,\text{V} : 0.248\,\text{A} = 20.2\,\Omega$. The ratio is $\dfrac{20.2\,\Omega}{10.2\,\Omega} = 1.98$
**Answer:** $2.0$ times, two significant figures like the voltages. The lamp does not obey Ohm's law, because the resistance increases from $10\,\Omega$ to about $20\,\Omega$.
**Reasonableness:** The voltage becomes five times as large ($5.0\,\text{V} : 1.0\,\text{V} = 5.0$), but the current only about $2.5$ times as large ($0.248\,\text{A} : 0.098\,\text{A} = 2.5$). By Ohm's law the current would also become five times as large, so the resistance must become about $5.0 : 2.5 = 2.0$ times as large, as calculated. Explanation: a larger current heats the tungsten wire, and the resistance of a hot metal wire is greater. The temperature of the lamp changes during the measurement, so the condition of Ohm's law of a constant temperature is not met.

## fy6-3-L2-07
**Given:** the measurement points $(U, I)$: $(0.0\,\text{V}; 0.00\,\text{A})$, $(1.0\,\text{V}; 0.20\,\text{A})$, $(2.0\,\text{V}; 0.41\,\text{A})$, $(3.0\,\text{V}; 0.61\,\text{A})$ and $(4.0\,\text{V}; 0.81\,\text{A})$
**Find:** what is wrong in the student's reasoning, and the mean $R_{\text{avg}}$ of the resistances at the non-zero voltages
**Principle:** The resistance $R = U : I$ is defined only when the current is not zero. At the point $U = 0.0\,\text{V}$ and $I = 0.00\,\text{A}$ the ratio is $0 : 0$, which is not a number. That a resistor does not pass a current without a voltage does not mean that the resistance is zero. The resistance is estimated from the points where the current can be measured. If the ratio $U : I$ is the same at them, the resistor obeys Ohm's law and the resistance does not increase with the voltage.
**Formula:** $R = \dfrac{U}{I}$ for each point and $R_{\text{avg}} = \dfrac{R_1 + \ldots + R_4}{4}$
**Conversions:** Not needed: the voltage is in volts and the current in amperes.
**Substitution:** $R_1 = 1.0\,\text{V} : 0.20\,\text{A} = 5.00\,\Omega$, $R_2 = 2.0\,\text{V} : 0.41\,\text{A} = 4.88\,\Omega$, $R_3 = 3.0\,\text{V} : 0.61\,\text{A} = 4.92\,\Omega$ and $R_4 = 4.0\,\text{V} : 0.81\,\text{A} = 4.94\,\Omega$. The sum is $19.74\,\Omega$, so $R_{\text{avg}} = 19.74\,\Omega : 4 = 4.93\,\Omega$
**Answer:** $R_{\text{avg}} = 4.9\,\Omega$, two significant figures like the currents. The student's reasoning is wrong: at the zero point the resistance cannot be calculated (the ratio $0 : 0$ is not zero), and at the other points the resistance is practically the same, so it does not increase with the voltage.
**Reasonableness:** At the largest voltage $4.0\,\text{V}$ we get $4.94\,\Omega$, and all the values are between $4.88\,\Omega$ and $5.00\,\Omega$, so the mean $4.9\,\Omega$ is between them. Check: $4.9\,\Omega \cdot 0.81\,\text{A} = 4.0\,\text{V}$. The difference between the first point, $5.00\,\Omega$, and the other values is measurement uncertainty, not an increase. The slope of a line fitted through the origin gives the same result, $4.9\,\Omega$.

## fy6-3-L3-04
**Given:** the currents of the components A, B and C at the voltages $0.5\,\text{V}$–$3.0\,\text{V}$ in the table (in milliamperes); the components are a resistor, a filament lamp and a diode
**Find:** the identification of the components from the change of the resistance, and the resistance $R$ of the diode at the operating point $U = 1.5\,\text{V}$ in ohms
**Principle:** The resistance at each point is $R = U : I$. For a resistor it stays the same when the temperature is constant, that is, the characteristic curve is a straight line. The resistance of a filament lamp increases with the voltage, because a larger current heats the wire and the resistance of a hot metal is greater. A diode does not obey Ohm's law: at a small voltage hardly any current flows through it and the resistance is large, but once the current starts to grow, the resistance of the diode decreases as the voltage increases. The identification is made by comparing the resistances as a function of the voltage, and at an operating point the resistance is the $U : I$ of the point, not the steepness of the curve.
**Formula:** $R = \dfrac{U}{I}$
**Conversions:** Currents from milliamperes to amperes: $1\,\text{mA} = 10^{-3}\,\text{A}$, for example $20.0\,\text{mA} = 0.0200\,\text{A}$.
**Substitution:** Component A: $R = 0.5\,\text{V} : 6.6\,\text{mA} = 76\,\Omega$, $1.0\,\text{V} : 13.5\,\text{mA} = 74\,\Omega$, $1.5\,\text{V} : 20.0\,\text{mA} = 75\,\Omega$, $2.0\,\text{V} : 26.6\,\text{mA} = 75\,\Omega$ and $3.0\,\text{V} : 40.2\,\text{mA} = 75\,\Omega$. Component B: $16\,\Omega$, $22\,\Omega$, $26\,\Omega$, $30\,\Omega$ and $37\,\Omega$. Component C: $1.0\,\text{V} : 0.1\,\text{mA} = 10\,\text{k}\Omega$, $1.5\,\text{V} : 2.5\,\text{mA} = 600\,\Omega$, $2.0\,\text{V} : 21\,\text{mA} = 95\,\Omega$ and $3.0\,\text{V} : 98\,\text{mA} = 31\,\Omega$ (at the voltage $0.5\,\text{V}$ the current is zero, so the resistance is not calculated). The resistance of the diode at the operating point is $R = \dfrac{1.5\,\text{V}}{2.5 \cdot 10^{-3}\,\text{A}} = 600\,\Omega$, and the resistance of the filament lamp at the same point is $\dfrac{1.5\,\text{V}}{57 \cdot 10^{-3}\,\text{A}} = 26\,\Omega$
**Answer:** $6.0 \cdot 10^{2}\,\Omega$, two significant figures like the current $2.5\,\text{mA}$. Component A is the resistor (constant resistance, about $75\,\Omega$), B the filament lamp (the resistance increases from $16\,\Omega$ to $37\,\Omega$) and C the diode (the resistance decreases from $10\,\text{k}\Omega$ to $31\,\Omega$). At the point $U = 1.5\,\text{V}$ the resistance of the diode is about $23$ times the resistance of the filament lamp.
**Reasonableness:** Check: $600\,\Omega \cdot 2.5 \cdot 10^{-3}\,\text{A} = 1.5\,\text{V}$. The ratio is $600\,\Omega : 26\,\Omega = 23$. The current of the resistor is directly proportional to the voltage: the voltage triples from $1.0\,\text{V}$ to $3.0\,\text{V}$, and the current grows from $13.5\,\text{mA}$ to $40.2\,\text{mA}$, that is, $2.98$ times. For the filament lamp the voltage grows by the same amount but the current only $81 : 46 = 1.8$ times, so the resistance increases.

## fy6-3-L3-05
**Given:** varnished iron wire in a water bath, $U = 1.00\,\text{V}$ in all the measurements; $T$ and $I$: $20\,{}^\circ\text{C}$ and $0.500\,\text{A}$, $40\,{}^\circ\text{C}$ and $0.442\,\text{A}$, $60\,{}^\circ\text{C}$ and $0.398\,\text{A}$, $80\,{}^\circ\text{C}$ and $0.362\,\text{A}$
**Find:** the variables of the experiment and the measuring arrangement, the increase of the resistance of the wire as a percentage from $20\,{}^\circ\text{C}$ to $80\,{}^\circ\text{C}$, and two sources of error
**Principle:** At each temperature the resistance is obtained as the ratio $R = U : I$. When the voltage is kept the same, a decrease of the current shows an increase of the resistance. In the experiment only one factor, the temperature, is changed and the other factors are kept constant, so that the result can be connected to the temperature. The percentage increase is $\dfrac{R_{80} - R_{20}}{R_{20}} \cdot 100\,\%$.
**Formula:** $R = \dfrac{U}{I}$ and the increase $\dfrac{R_{80} - R_{20}}{R_{20}} \cdot 100\,\%$
**Conversions:** Not needed: the voltage is in volts and the current in amperes, and the change of the temperature does not need to be converted.
**Substitution:** Variables: the independent variable is the temperature $T$ of the water, that is, of the wire, the dependent variable is the resistance $R$ of the wire (measured from the current and the voltage), and the controlled factors are the material, length and thickness of the wire and the voltage $1.00\,\text{V}$. Measuring arrangement: the ammeter is connected in series with the wire and the voltmeter in parallel with the wire, so that the meters measure the current and the voltage of the wire; the wire is varnished so that the water does not conduct current past it, and the thermometer is next to the wire. The resistances are $R_{20} = 1.00\,\text{V} : 0.500\,\text{A} = 2.000\,\Omega$, $R_{40} = 2.262\,\Omega$, $R_{60} = 2.513\,\Omega$ and $R_{80} = 1.00\,\text{V} : 0.362\,\text{A} = 2.762\,\Omega$, so the increase is $\dfrac{2.762\,\Omega - 2.000\,\Omega}{2.000\,\Omega} \cdot 100\,\% = 38.1\,\%$. Sources of error: (1) the wire also heats up from the current itself, so its temperature may be higher than that of the water; the current is switched on only for the moment of measurement and the voltage is kept small. (2) The wire has not had time to settle to the temperature of the water, or the thermometer is not at the wire; at each temperature we wait until the reading of the thermometer no longer changes, and stir the water.
**Answer:** The resistance has increased by about $38\,\%$ (calculated $38.1\,\%$), two significant figures, because the increase is the difference of two almost equal resistances relative to the value $R_{20}$. The result supports the conclusion that the resistance of a metal wire increases as the temperature rises.
**Reasonableness:** The current decreases as the temperature rises ($0.500\,\text{A} \to 0.362\,\text{A}$) and the voltage is constant, so the resistance must increase: $0.500\,\text{A} : 0.362\,\text{A} = 1.38$. The resistance increases by about the same amount over each $20\,{}^\circ\text{C}$ interval ($0.262\,\Omega$, $0.251\,\Omega$ and $0.249\,\Omega$), that is, the increase is almost steady. The measurement is of one wire, so the result describes the wire of this example data and is not an exact property of iron wire.

## fy6-3-L1-09
**Find:** which of the four $(I, U)$ graphs is the characteristic curve of a $2.0\,\text{k}\Omega$ resistor obeying Ohm's law.
**Principle:** The resistance of a resistor obeying Ohm's law is constant, so $U = RI$: the characteristic curve is a straight line through the origin whose slope is the resistance $R$. Resistance is the ratio of the voltage to the current $U : I$, not $I : U$, and it must be the same at every point of the curve.
**Model answer:** The correct one is graph C. Let us calculate the voltage of the resistor at a current of $4.0\,\text{mA}$.

$U = RI$

$U = 2.0 \cdot 10^{3}\,\Omega \cdot 4.0 \cdot 10^{-3}\,\text{A}$

$U = 8.0\,\text{V}$

The line of graph C passes through the origin and the point $(4.0\,\text{mA};\ 8.0\,\text{V})$, and also at the point $(2.0\,\text{mA};\ 4.0\,\text{V})$ the ratio is $U : I = 2.0\,\text{k}\Omega$. The curve of graph A passes through the same point $(4.0\,\text{mA};\ 8.0\,\text{V})$, but at the point $(2.0\,\text{mA};\ 2.0\,\text{V})$ the ratio is only $1.0\,\text{k}\Omega$: the resistance increases with the voltage, so the component does not obey Ohm's law. In graph B the voltage at a current of $4.0\,\text{mA}$ is $2.0\,\text{V}$, so the resistance would be $0.50\,\text{k}\Omega$: there the slope has been taken to be $I : U$. In graph D the voltage is constant $2.0\,\text{V}$, so the ratio $U : I$ changes all the time: there the numerical value of the resistance has been drawn as the voltage.

**Reading the graph:** The voltage is read from each graph at two currents, for example $2.0\,\text{mA}$ and $4.0\,\text{mA}$, and the ratio $U : I$ is calculated. Only in graph C is the ratio $2.0\,\text{k}\Omega$ at both points.
