
## fy6-13-L1-01
**Given:** voltage $U = 12\,\text{V}$, charge $Q = 4.8\,\mu\text{C}$
**Find:** the capacitance $C$ in microfarads
**Principle:** The charge of a capacitor is directly proportional to its voltage, and their ratio is the capacitance. When charging has ended, the voltage of the capacitor is the voltage of the source.
**Formula:** $C = \dfrac{Q}{U}$
**Conversions:** $Q = 4.8\,\mu\text{C} = 4.8 \cdot 10^{-6}\,\text{C}$
**Substitution:** $C = \dfrac{4.8 \cdot 10^{-6}\,\text{C}}{12\,\text{V}} = 0.40 \cdot 10^{-6}\,\text{F} = 0.40\,\mu\text{F}$
**Answer:** $0.40\,\mu\text{F}$, two significant figures like the charge and the voltage.
**Reasonableness:** A capacitor of $0.40\,\mu\text{F}$ takes $0.40\,\mu\text{C}$ for every volt, and $12 \cdot 0.40\,\mu\text{C} = 4.8\,\mu\text{C}$. A tenth of a microfarad is an ordinary capacitance for a small capacitor.

## fy6-13-L1-02
**Given:** capacitance $C = 470\,\mu\text{F}$, voltage $U = 9.0\,\text{V}$
**Find:** the charge $Q$ in millicoulombs
**Principle:** After charging, the voltage of the capacitor is the voltage of the battery, and the charge is the capacitance times the voltage, because the capacitance is the ratio of the charge to the voltage.
**Formula:** $C = \dfrac{Q}{U}$, from which $Q = CU$
**Conversions:** $C = 470\,\mu\text{F} = 470 \cdot 10^{-6}\,\text{F}$
**Substitution:** $Q = 470 \cdot 10^{-6}\,\text{F} \cdot 9.0\,\text{V} = 4.23 \cdot 10^{-3}\,\text{C} = 4.23\,\text{mC}$
**Answer:** $4.2\,\text{mC}$, two significant figures like the voltage $9.0\,\text{V}$.
**Reasonableness:** The estimate $500\,\mu\text{F} \cdot 10\,\text{V} = 5000\,\mu\text{C} = 5\,\text{mC}$ is slightly greater, because both numbers were rounded up. The unit works out: $\text{F} \cdot \text{V} = \tfrac{\text{C}}{\text{V}} \cdot \text{V} = \text{C}$.

## fy6-13-L1-03
**Given:** capacitance $C = 2200\,\mu\text{F}$, voltage $U = 16\,\text{V}$
**Find:** the stored energy $W$ in joules
**Principle:** The energy of a charged capacitor is in the electric field between the plates. When the capacitance and the voltage are known, the energy is obtained from the form $\tfrac{1}{2} C U^2$, which follows from the area of the triangle under the $(Q, U)$ graph.
**Formula:** $W = \tfrac{1}{2} C U^2$
**Conversions:** $C = 2200\,\mu\text{F} = 2200 \cdot 10^{-6}\,\text{F}$
**Substitution:** $W = \tfrac{1}{2} \cdot 2200 \cdot 10^{-6}\,\text{F} \cdot (16\,\text{V})^2 = 0.2816\,\text{J}$
**Answer:** $0.28\,\text{J}$, two significant figures like the voltage $16\,\text{V}$.
**Reasonableness:** The charge is $Q = CU \approx 0.035\,\text{C}$, and $\tfrac{1}{2} \cdot 0.035\,\text{C} \cdot 16\,\text{V} \approx 0.28\,\text{J}$, the same result. An energy of less than a joule is small, which suits a low-voltage capacitor.

## fy6-13-L1-04
**Given:** area of the plate $A = 0.025\,\text{m}^2$, distance of the plates $d = 1.0\,\text{mm}$, dielectric air, from the table $\varepsilon_\text{r} = 1.0$, electric constant $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$
**Find:** the capacitance $C$ in picofarads
**Principle:** The capacitor is a parallel-plate capacitor, whose capacitance depends only on the area of the plates, their distance and the dielectric. The relative permittivity of air is almost one.
**Formula:** $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, from which for air $C = \dfrac{\varepsilon_0 A}{d}$
**Conversions:** $d = 1.0\,\text{mm} = 1.0 \cdot 10^{-3}\,\text{m}$
**Substitution:** $C = \dfrac{8.854 \cdot 10^{-12}\,\text{F/m} \cdot 0.025\,\text{m}^2}{1.0 \cdot 10^{-3}\,\text{m}} = 221 \cdot 10^{-12}\,\text{F} = 221\,\text{pF}$
**Answer:** $2.2 \cdot 10^{2}\,\text{pF} = 220\,\text{pF}$ (the calculated value $221\,\text{pF}$ rounded to two significant figures like the area and the distance).
**Reasonableness:** The ratio $A : d = 0.025\,\text{m}^2 : 0.0010\,\text{m} = 25\,\text{m}$, and $25\,\text{m} \cdot 8.854\,\text{pF/m} \approx 220\,\text{pF}$. The capacitance of a parallel-plate capacitor with air is typically hundreds of picofarads.

## fy6-13-L1-05
**Given:** the graph of the voltage as a function of the charge, voltage $U = 12\,\text{V}$
**Find:** the stored energy $W$ in microjoules
**Principle:** In charging the voltage grows in the same proportion as the charge. The energy is the area of the triangle between the graph and the charge axis, that is, half of the product of the charge and the voltage.
**Reading the graph:** The grid line of the voltage $12\,\text{V}$ meets the line at the grid line of the charge $60\,\mu\text{C}$. The base of the triangle is thus $60\,\mu\text{C}$ and its height $12\,\text{V}$.
**Formula:** $W = \tfrac{1}{2} Q U$
**Conversions:** Not needed: $\mu\text{C} \cdot \text{V} = \mu\text{J}$, because $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Substitution:** $W = \tfrac{1}{2} \cdot 60\,\mu\text{C} \cdot 12\,\text{V} = 360\,\mu\text{J}$
**Answer:** $360\,\mu\text{J}$, two significant figures, because the values are read from grid lines spaced $10\,\mu\text{C}$ and $2\,\text{V}$ apart.
**Reasonableness:** The capacitance is $60\,\mu\text{C} : 12\,\text{V} = 5.0\,\mu\text{F}$, and $\tfrac{1}{2} \cdot 5.0\,\mu\text{F} \cdot (12\,\text{V})^2 = 360\,\mu\text{J}$, the same result. Half of the rectangle $60\,\mu\text{C} \cdot 12\,\text{V} = 720\,\mu\text{J}$ is the triangle, as it should be.

## fy6-13-L2-01
**Given:** thickness of the paper layer $d = 0.020\,\text{mm}$, dielectric strength $E_\text{max} = 16\,\text{MV/m}$
**Find:** the greatest voltage $U_\text{max}$ in volts
**Principle:** Between the plates there is a uniform field $E = \tfrac{U}{d}$. A breakdown happens when the field exceeds the dielectric strength of the dielectric, so the greatest allowed voltage is obtained when the field is exactly the dielectric strength.
**Formula:** $E_\text{max} = \dfrac{U_\text{max}}{d}$, from which $U_\text{max} = E_\text{max} d$
**Conversions:** $E_\text{max} = 16\,\text{MV/m} = 16 \cdot 10^{6}\,\text{V/m}$ and $d = 0.020\,\text{mm} = 0.020 \cdot 10^{-3}\,\text{m}$
**Substitution:** $U_\text{max} = 16 \cdot 10^{6}\,\tfrac{\text{V}}{\text{m}} \cdot 0.020 \cdot 10^{-3}\,\text{m} = 320\,\text{V}$
**Answer:** $320\,\text{V}$, that is, $3.2 \cdot 10^{2}\,\text{V}$, two significant figures like the thickness and the dielectric strength.
**Reasonableness:** One millimetre of paper would withstand $16\,\text{kV}$, and $0.020\,\text{mm}$ is a fiftieth of that: $16\,000\,\text{V} : 50 = 320\,\text{V}$. A thin dielectric gives a large capacitance but withstands only a small voltage.

## fy6-13-L2-02
**Given:** area of the plate $A = 100\,\text{cm}^2$, thickness of the dielectric layer $d = 0.10\,\text{mm}$, capacitance $C = 3.3\,\text{nF}$, electric constant $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$
**Find:** the relative permittivity $\varepsilon_\text{r}$ of the dielectric
**Principle:** The capacitor is a parallel-plate capacitor, and the dielectric fills the space between the plates, so its capacitance is $\varepsilon_\text{r}$ times that in vacuum. When the capacitance and the dimensions are known, the relative permittivity can be solved.
**Formula:** $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, from which $\varepsilon_\text{r} = \dfrac{C d}{\varepsilon_0 A}$
**Conversions:** $A = 100\,\text{cm}^2 = 100 \cdot (0.01\,\text{m})^2 = 10^{-2}\,\text{m}^2$, $d = 0.10\,\text{mm} = 0.10 \cdot 10^{-3}\,\text{m} = 10^{-4}\,\text{m}$ and $C = 3.3\,\text{nF} = 3.3 \cdot 10^{-9}\,\text{F}$
**Substitution:** $\varepsilon_\text{r} = \dfrac{3.3 \cdot 10^{-9}\,\text{F} \cdot 10^{-4}\,\text{m}}{8.854 \cdot 10^{-12}\,\text{F/m} \cdot 10^{-2}\,\text{m}^2} \approx 3.73$
**Answer:** $3.7$, two significant figures like the capacitance and the thickness. The relative permittivity is a ratio that has no unit.
**Reasonableness:** With air the capacitance would be $\varepsilon_0 A : d \approx 0.89\,\text{nF}$, and $3.3\,\text{nF}$ is about $3.7$ times that. According to the table the relative permittivity of paper is $3.7$, so the dielectric can be paper.

## fy6-13-L2-03
**Given:** energy $W = 200\,\text{J}$, voltage $U = 2.0\,\text{kV}$
**Find:** the capacitance $C$ in microfarads
**Principle:** The energy of a capacitor depends on the capacitance and the voltage, $W = \tfrac{1}{2} C U^2$. When the energy and the voltage are known, the capacitance is solved from this equation.
**Formula:** $W = \tfrac{1}{2} C U^2$, from which $C = \dfrac{2W}{U^2}$
**Conversions:** $U = 2.0\,\text{kV} = 2.0 \cdot 1000\,\text{V} = 2000\,\text{V}$
**Substitution:** $C = \dfrac{2 \cdot 200\,\text{J}}{(2000\,\text{V})^2} = \dfrac{400\,\text{J}}{4.0 \cdot 10^{6}\,\text{V}^2} = 1.0 \cdot 10^{-4}\,\text{F} = 100\,\mu\text{F}$
**Answer:** $1.0 \cdot 10^{2}\,\mu\text{F}$, that is, $100\,\mu\text{F}$, two significant figures like the voltage $2.0\,\text{kV}$.
**Reasonableness:** Check: $\tfrac{1}{2} \cdot 100 \cdot 10^{-6}\,\text{F} \cdot (2000\,\text{V})^2 = 200\,\text{J}$. Unit: $\tfrac{\text{J}}{\text{V}^2} = \tfrac{\text{C} \cdot \text{V}}{\text{V}^2} = \tfrac{\text{C}}{\text{V}} = \text{F}$.

## fy6-13-L2-04
**Given:** capacitance $C = 10\,\text{F}$, voltage $U = 2.7\,\text{V}$, power of the lamp $P = 0.50\,\text{W}$
**Find:** the time the lamp stays lit $t$ in seconds
**Principle:** The whole energy $\tfrac{1}{2} C U^2$ of the capacitor is assumed to be available to the lamp. Power is energy per unit of time, and the power is assumed constant, so the time is the energy divided by the power.
**Formula:** $W = \tfrac{1}{2} C U^2$ and $P = \dfrac{W}{t}$, from which $t = \dfrac{C U^2}{2P}$
**Conversions:** Not needed: all the quantities are in base units, and $\tfrac{\text{J}}{\text{W}} = \text{s}$.
**Substitution:** $t = \dfrac{10\,\text{F} \cdot (2.7\,\text{V})^2}{2 \cdot 0.50\,\text{W}} = \dfrac{72.9\,\text{J}}{1.0\,\text{W}} = 72.9\,\text{s}$
**Answer:** $73\,\text{s}$, two significant figures like the capacitance and the power.
**Reasonableness:** The energy is $\tfrac{1}{2} \cdot 10\,\text{F} \cdot 7.29\,\text{V}^2 \approx 36\,\text{J}$, and $0.50\,\text{W}$ uses it up in about $70$ seconds. The energy of a supercapacitor lasts only about a minute, whereas a small battery would last for hours, which matches experience.

## fy6-13-L3-01
**Given:** capacitance $C_1 = 120\,\text{pF}$, voltage $U_1 = 500\,\text{V}$, the source is disconnected, the distance of the plates doubles
**Find:** the change in energy $\Delta W$ in microjoules
**Principle:** The charge of a disconnected capacitor cannot change, because the charge has no path from one plate to the other. The capacitance of a parallel-plate capacitor is inversely proportional to the distance of the plates, so it halves, and the voltage $U = \tfrac{Q}{C}$ doubles. The increase in energy is the work done in pulling the plates apart.
**Formula:** $Q = C_1 U_1$, $C_2 = \tfrac{1}{2} C_1$, $U_2 = \dfrac{Q}{C_2}$ and $\Delta W = \tfrac{1}{2} Q U_2 - \tfrac{1}{2} Q U_1$, from which $\Delta W = \tfrac{1}{2} Q (U_2 - U_1)$
**Conversions:** $C_1 = 120\,\text{pF} = 120 \cdot 10^{-12}\,\text{F}$
**Substitution:** $Q = 120 \cdot 10^{-12}\,\text{F} \cdot 500\,\text{V} = 60 \cdot 10^{-9}\,\text{C}$, $U_2 = \dfrac{60 \cdot 10^{-9}\,\text{C}}{60 \cdot 10^{-12}\,\text{F}} = 1000\,\text{V}$ and $\Delta W = \tfrac{1}{2} \cdot 60 \cdot 10^{-9}\,\text{C} \cdot 500\,\text{V} = 15 \cdot 10^{-6}\,\text{J}$
**Answer:** $15\,\mu\text{J}$, two significant figures like the capacitance $120\,\text{pF}$.
**Reasonableness:** The energy grows from $15\,\mu\text{J}$ to $30\,\mu\text{J}$, that is, it doubles, because the charge stays the same and the voltage doubles. The energy does not appear from nothing: the plates attract each other, and separating them requires the work $15\,\mu\text{J}$.

## fy6-13-L3-02
**Given:** capacitance with air $C_1 = 220\,\text{pF}$, voltage $U = 1.5\,\text{kV}$, $\varepsilon_\text{r} = 5.6$ for glass, the source stays connected
**Find:** the additional charge $\Delta Q$ that moves from the source to the capacitor in microcoulombs
**Principle:** The source keeps the voltage the same all the time. The dielectric makes the capacitance $\varepsilon_\text{r}$ times as large, so at the same voltage the plates have $\varepsilon_\text{r}$ times the charge, and the source brings the difference.
**Formula:** $Q_1 = C_1 U$ and $Q_2 = \varepsilon_\text{r} C_1 U$, from which $\Delta Q = Q_2 - Q_1 = (\varepsilon_\text{r} - 1) C_1 U$
**Conversions:** $C_1 = 220\,\text{pF} = 220 \cdot 10^{-12}\,\text{F}$ and $U = 1.5\,\text{kV} = 1.5 \cdot 1000\,\text{V} = 1500\,\text{V}$
**Substitution:** $\Delta Q = (5.6 - 1) \cdot 220 \cdot 10^{-12}\,\text{F} \cdot 1500\,\text{V} = 1.518 \cdot 10^{-6}\,\text{C}$
**Answer:** $1.5\,\mu\text{C}$, two significant figures like the voltage $1.5\,\text{kV}$ and the relative permittivity $5.6$.
**Reasonableness:** At the start the charge is $220\,\text{pF} \cdot 1500\,\text{V} = 0.33\,\mu\text{C}$, and with glass $5.6$ times as much, that is, $1.85\,\mu\text{C}$. The increase $1.5\,\mu\text{C}$ is the difference. If the source had been disconnected, the charge would not have changed at all.

## fy6-13-L3-03
**Given:** capacitance $C = 1.0\,\text{nF}$, voltage $U = 6.0\,\text{kV}$, for polystyrene $\varepsilon_\text{r} = 2.6$ and $E_\text{max} = 24\,\text{MV/m}$, the field at most $\tfrac{1}{2} E_\text{max}$, $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$
**Find:** the area of the plate $A$ in square centimetres
**Principle:** The field between the plates is $E = \tfrac{U}{d}$. The field may be at most half of the dielectric strength, so the dielectric must be at least thick enough that the field does not exceed this limit. When the thickness is known, the area that gives the desired capacitance is solved from the formula of a parallel-plate capacitor.
**Formula:** $\tfrac{1}{2} E_\text{max} = \dfrac{U}{d}$, from which $d = \dfrac{2U}{E_\text{max}}$, and $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, from which $A = \dfrac{C d}{\varepsilon_0 \varepsilon_\text{r}}$
**Conversions:** $U = 6.0\,\text{kV} = 6000\,\text{V}$, $E_\text{max} = 24 \cdot 10^{6}\,\text{V/m}$, $C = 1.0 \cdot 10^{-9}\,\text{F}$ and finally $1\,\text{m}^2 = 100\,\text{cm} \cdot 100\,\text{cm} = 10\,000\,\text{cm}^2$
**Substitution:** $d = \dfrac{2 \cdot 6000\,\text{V}}{24 \cdot 10^{6}\,\text{V/m}} = 5.0 \cdot 10^{-4}\,\text{m}$ and $A = \dfrac{1.0 \cdot 10^{-9}\,\text{F} \cdot 5.0 \cdot 10^{-4}\,\text{m}}{8.854 \cdot 10^{-12}\,\text{F/m} \cdot 2.6} \approx 0.0217\,\text{m}^2 = 217\,\text{cm}^2$
**Answer:** $220\,\text{cm}^2$, that is, $2.2 \cdot 10^{2}\,\text{cm}^2$, two significant figures like the capacitance and the voltage.
**Reasonableness:** The dielectric is $0.50\,\text{mm}$ thick, and the field in it is $6000\,\text{V} : 0.50\,\text{mm} = 12\,\text{MV/m}$, half of the dielectric strength. The side of a square would be about $15\,\text{cm}$. A thinner dielectric would make the plates smaller, but the capacitor would no longer withstand the voltage safely.

## fy6-13-L1-06
**Find:** what happens to the capacitance when the voltage doubles.
**Principle:** The capacitance is the ratio of the charge to the voltage, $C = \tfrac{Q}{U}$. It is determined by the area of the plates, their distance and the dielectric, not by the voltage to which the capacitor is charged. When the voltage grows, the charge grows in the same proportion.
**Model answer:** The capacitance stays the same, because it is determined by the construction of the capacitor. At the voltage $5.0\,\text{V}$ the charge is $Q_1 = 5.0\,\text{V} \cdot C$, and at the voltage $10\,\text{V}$ it is $Q_2 = 10\,\text{V} \cdot C$, so the charge doubles but the ratio $\tfrac{Q}{U}$ does not change. The capacitance does not double, decrease or become four times as large. The energy, on the other hand, becomes four times as large, because $W = \tfrac{1}{2} C U^2$ depends on the square of the voltage.

## fy6-13-L1-07
**Find:** what happens to the voltage when a dielectric is pushed into a disconnected capacitor.
**Principle:** The charge of a disconnected capacitor cannot change, because the charge has no path from one plate to the other. The dielectric makes the capacitance $\varepsilon_\text{r}$ times as large, and the voltage is obtained from the formula $U = \tfrac{Q}{C}$.
**Model answer:** The voltage decreases. The charge $Q$ stays the same, because the source has been disconnected, and the capacitance $C$ increases because of the dielectric. Since $U = \tfrac{Q}{C}$, the voltage decreases in the same proportion as the capacitance increases: it becomes $\tfrac{1}{\varepsilon_\text{r}}$ times as large. The dielectric does not conduct charge from one plate to the other, and the voltage does not stay the same, because the source no longer keeps it constant. The energy $W = \tfrac{1}{2} Q U$ decreases too.

## fy6-13-L1-08
**Given:** capacitance $C = 1000\,\mu\text{F}$, voltages $U_1 = 6.0\,\text{V}$ and $U_2 = 18\,\text{V}$
**Find:** the increase in energy $\Delta W$ in millijoules
**Principle:** The energy of a capacitor is $\tfrac{1}{2} C U^2$ and depends on the square of the voltage. The capacitance does not change, so the increase in energy is the difference between the final and the initial energy.
**Formula:** $W = \tfrac{1}{2} C U^2$ and $\Delta W = W_2 - W_1 = \tfrac{1}{2} C (U_2^2 - U_1^2)$
**Conversions:** $C = 1000\,\mu\text{F} = 1000 \cdot 10^{-6}\,\text{F} = 1.0 \cdot 10^{-3}\,\text{F}$
**Substitution:** $W_1 = \tfrac{1}{2} \cdot 1.0 \cdot 10^{-3}\,\text{F} \cdot (6.0\,\text{V})^2 = 0.018\,\text{J}$, $W_2 = \tfrac{1}{2} \cdot 1.0 \cdot 10^{-3}\,\text{F} \cdot (18\,\text{V})^2 = 0.162\,\text{J}$ and $\Delta W = 0.162\,\text{J} - 0.018\,\text{J} = 0.144\,\text{J} = 144\,\text{mJ}$
**Answer:** $144\,\text{mJ}$, three significant figures, because the capacitance $1000\,\mu\text{F}$ and the voltage $18\,\text{V}$ determine the result accurately enough.
**Reasonableness:** The voltage triples, so the energy grows to $3^2 = 9$ times as large: $W_2 : W_1 = 162\,\text{mJ} : 18\,\text{mJ} = 9$. The increase is $9W_1 - W_1 = 8W_1 = 8 \cdot 18\,\text{mJ} = 144\,\text{mJ}$.

## fy6-13-L2-05
**Given:** the points $(U;\ Q)$ of the table: $(2.0\,\text{V};\ 94\,\mu\text{C})$, $(4.0\,\text{V};\ 189\,\mu\text{C})$, $(6.0\,\text{V};\ 281\,\mu\text{C})$, $(8.0\,\text{V};\ 380\,\mu\text{C})$, $(10.0\,\text{V};\ 471\,\mu\text{C})$ and $(12.0\,\text{V};\ 567\,\mu\text{C})$
**Find:** the energy $W$ at the voltage $12\,\text{V}$ in millijoules
**Principle:** Since $Q = CU$, the points lie on a straight line through the origin whose slope is the capacitance $C$. When the capacitance is known, the energy is obtained from the formula $W = \tfrac{1}{2} C U^2$. The same energy is the area $\tfrac{1}{2} Q U$ of the triangle between the line of the $(U, Q)$ graph and the $Q$ axis.
**Reading the graph:** The points lie on a rising straight line with points on both sides of it, and the line passes through the origin. The slope is read from two points of the fitted line that are far apart, the origin and the point $(12\,\text{V};\ 566\,\mu\text{C})$: $\tfrac{566\,\mu\text{C}}{12\,\text{V}} \approx 47.2\,\tfrac{\mu\text{C}}{\text{V}}$, so the capacitance is about $47.2\,\mu\text{F}$.
**Formula:** $C = \dfrac{Q}{U}$ (the slope of the line) and $W = \tfrac{1}{2} C U^2$
**Conversions:** $C = 47.2\,\tfrac{\mu\text{C}}{\text{V}} = 47.2\,\mu\text{F} = 47.2 \cdot 10^{-6}\,\text{F}$
**Substitution:** $W = \tfrac{1}{2} \cdot 47.2 \cdot 10^{-6}\,\text{F} \cdot (12\,\text{V})^2 = 3.40 \cdot 10^{-3}\,\text{J} = 3.40\,\text{mJ}$
**Answer:** $3.4\,\text{mJ}$, two significant figures like the voltage and the slope. Fitting by eye varies, so about $3.3\text{–}3.5\,\text{mJ}$ is a good answer.
**Reasonableness:** The area of the triangle is $\tfrac{1}{2} \cdot 567\,\mu\text{C} \cdot 12\,\text{V} = 3402\,\mu\text{J} \approx 3.4\,\text{mJ}$, the same result. The capacitance $47\,\mu\text{F}$ is an ordinary value for an electrolytic capacitor.

## fy6-13-L2-06
**Find:** the time interval during which the charging current is the greatest.
**Principle:** The current is the rate at which charge moves. Since $Q = CU$ and the capacitance is constant, the charge changes at the same rate as the voltage, so the current is directly proportional to the rate at which the voltage grows, that is, to the steepness of the graph. The current thus depends not on the size of the voltage but on how fast the voltage grows.
**Model answer:** The charging current is the greatest during the interval $0\text{–}1\,\text{s}$, because the voltage then grows the fastest, $3.5\,\text{V}$ per second, and charge moves to the plates the fastest. At the start the voltage of the capacitor is zero, so the whole voltage of the source drives the current. As charge accumulates in the capacitor, its voltage opposes the source, the growth of the voltage slows down and the current decreases towards zero. The current is not the greatest when the voltage or the charge is the greatest, but when they change the fastest.
**Reading the graph:** The growth of the voltage in one second is $3.5\,\text{V}$ during $0\text{–}1\,\text{s}$, $2.0\,\text{V}$ during $1\text{–}2\,\text{s}$, $1.4\,\text{V}$ during $2\text{–}3\,\text{s}$, $0.8\,\text{V}$ during $3\text{–}4\,\text{s}$, $0.5\,\text{V}$ during $4\text{–}5\,\text{s}$ and $0.3\,\text{V}$ during $5\text{–}6\,\text{s}$. The graph is steepest at the start and becomes gentler all the time.

## fy6-13-L2-07
**Given:** capacitance $C = 220\,\mu\text{F}$, voltage of the source $U = 24\,\text{V}$, the student’s result $QU = 127\,\text{mJ}$
**Find:** a) the error in the student’s reasoning, b) the stored energy $W$ in millijoules
**Principle:** The source moves the charge $Q$ from one plate to the other across its whole voltage $U$, and so gives the energy $QU$. In charging, the voltage of the capacitor grows from zero to $U$, so the charge moves on average across the voltage $\tfrac{U}{2}$, and only half of the energy given by the source is stored in the capacitor.
**Formula:** $W = \tfrac{1}{2} C U^2$
**Conversions:** $C = 220\,\mu\text{F} = 220 \cdot 10^{-6}\,\text{F}$
**Substitution:** $W = \tfrac{1}{2} \cdot 220 \cdot 10^{-6}\,\text{F} \cdot (24\,\text{V})^2 = 0.0634\,\text{J} = 63.4\,\text{mJ}$
**Answer:** $63\,\text{mJ}$, two significant figures like the capacitance and the voltage.
**Model answer on the error:** The student’s $QU = 127\,\text{mJ}$ is the energy given by the source, but only half of it is stored in the capacitor. During charging the voltage of the capacitor is at first zero and grows only gradually to $24\,\text{V}$, so the charge does not move across the full voltage all the time. The other half, about $63\,\text{mJ}$, becomes internal energy of the wires and resistors and passes to the surroundings as heat.
**Reasonableness:** The stored energy is $\tfrac{1}{2} \cdot 5.28\,\text{mC} \cdot 24\,\text{V} = 63.4\,\text{mJ}$, the same result, and it is exactly half of the student’s figure $127\,\text{mJ}$.

## fy6-13-L3-04
**Given:** charging current $I = 15\,\text{mA}$, the points $(t;\ U)$ of the table: $(0\,\text{s};\ 0\,\text{V})$, $(2\,\text{s};\ 203\,\text{V})$, $(4\,\text{s};\ 396\,\text{V})$, $(6\,\text{s};\ 607\,\text{V})$, $(8\,\text{s};\ 805\,\text{V})$, $(10\,\text{s};\ 992\,\text{V})$ and $(12\,\text{s};\ 1201\,\text{V})$, voltage of the shock $1.8\,\text{kV}$, discharge time $5.0\,\text{ms}$
**Find:** the average power of the shock $P$ in kilowatts, and in addition the charging time and the justification for not touching the capacitor
**Principle:** With a constant current the charge is $Q = It$, and for a capacitor $Q = CU$, so $U = \tfrac{I}{C} t$: the voltage grows directly with time, and the slope of the line is $\tfrac{I}{C}$. When the capacitance is known, the energy released in the shock is the energy of the capacitor $\tfrac{1}{2} C U^2$, and the average power is obtained by dividing it by the discharge time.
**Reading the graph:** The points lie on a straight line through the origin, and the voltage grows by about $100\,\text{V}$ per second. The slope is read from two points of the fitted line that are far apart, the origin and the point $(12\,\text{s};\ 1200\,\text{V})$: $\tfrac{1200\,\text{V}}{12\,\text{s}} = 100\,\tfrac{\text{V}}{\text{s}}$.
**Formula:** $\dfrac{I}{C} = k$, from which $C = \dfrac{I}{k}$, and $W = \tfrac{1}{2} C U^2$ and $P = \dfrac{W}{t}$
**Conversions:** $I = 15\,\text{mA} = 15 \cdot 10^{-3}\,\text{A}$, $U = 1.8\,\text{kV} = 1800\,\text{V}$ and $t = 5.0\,\text{ms} = 5.0 \cdot 10^{-3}\,\text{s}$
**Substitution:** $C = \dfrac{15 \cdot 10^{-3}\,\text{A}}{100\,\text{V/s}} = 1.5 \cdot 10^{-4}\,\text{F} = 150\,\mu\text{F}$, $W = \tfrac{1}{2} \cdot 1.5 \cdot 10^{-4}\,\text{F} \cdot (1800\,\text{V})^2 = 243\,\text{J}$ and $P = \dfrac{243\,\text{J}}{5.0 \cdot 10^{-3}\,\text{s}} = 4.86 \cdot 10^{4}\,\text{W}$
**Answer:** $48.6\,\text{kW}$, that is, about $49\,\text{kW}$, two significant figures like the discharge time.
**Model answer on the charging time and safety:** Charging takes $t = \tfrac{U}{k} = \tfrac{1800\,\text{V}}{100\,\text{V/s}} = 18\,\text{s}$. The capacitor of the device must not be touched even when it is unplugged, because a charged capacitor keeps its charge and energy until it gets a path for the current: here the energy is $243\,\text{J}$ and the voltage $1.8\,\text{kV}$. Touching the terminals would let a current pass through the body, and the discharge would be a dangerous shock.
**Reasonableness:** The charge is $Q = It = 15\,\text{mA} \cdot 18\,\text{s} = 0.27\,\text{C}$, and $\tfrac{1}{2} \cdot 0.27\,\text{C} \cdot 1800\,\text{V} = 243\,\text{J}$, the same result. The average power of charging is only $243\,\text{J} : 18\,\text{s} = 13.5\,\text{W}$, whereas in the shock the same energy is released in $5.0\,\text{ms}$, so the power is thousands of times as great.

## fy6-13-L3-05
**Given:** area of the plate $A = 100\,\text{cm}^2$, thickness of the dielectric layer $d = 0.050\,\text{mm}$, from the table for Teflon $\varepsilon_\text{r} = 2.1$ and $E_\text{max} = 60\,\text{MV/m}$ and for glass $\varepsilon_\text{r} = 5.6$ and $E_\text{max} = 14\,\text{MV/m}$, the field at most $\tfrac{1}{2} E_\text{max}$, $\varepsilon_0 = 8.854 \cdot 10^{-12}\,\text{F/m}$
**Find:** the ratio of the energies of the Teflon and the glass capacitor $\tfrac{W_\text{Teflon}}{W_\text{glass}}$ and a justification
**Principle:** The allowed field is $\tfrac{1}{2} E_\text{max}$, so the greatest voltage is $U = \tfrac{1}{2} E_\text{max} d$. The capacitance of a parallel-plate capacitor is obtained from the formula $C = \tfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, and the energy is $W = \tfrac{1}{2} C U^2$. The ratio of the energies shows which dielectric stores more energy in the same volume.
**Formula:** $U = \tfrac{1}{2} E_\text{max} d$, $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$ and $W = \tfrac{1}{2} C U^2$
**Conversions:** $A = 100\,\text{cm}^2 = 1.0 \cdot 10^{-2}\,\text{m}^2$, $d = 0.050\,\text{mm} = 5.0 \cdot 10^{-5}\,\text{m}$, $60\,\text{MV/m} = 60 \cdot 10^{6}\,\text{V/m}$ and $14\,\text{MV/m} = 14 \cdot 10^{6}\,\text{V/m}$
**Substitution:** Teflon: $U = \tfrac{1}{2} \cdot 60 \cdot 10^{6}\,\tfrac{\text{V}}{\text{m}} \cdot 5.0 \cdot 10^{-5}\,\text{m} = 1500\,\text{V}$, $\varepsilon_0 \varepsilon_\text{r} A = 1.86 \cdot 10^{-13}\,\text{F} \cdot \text{m}$, from which $C = \dfrac{1.86 \cdot 10^{-13}\,\text{F} \cdot \text{m}}{5.0 \cdot 10^{-5}\,\text{m}} = 3.72\,\text{nF}$ and $W = \tfrac{1}{2} \cdot 3.72 \cdot 10^{-9}\,\text{F} \cdot (1500\,\text{V})^2 = 4.18\,\text{mJ}$. For glass $U = 350\,\text{V}$, $C = 9.92\,\text{nF}$ and $W = \tfrac{1}{2} \cdot 9.92 \cdot 10^{-9}\,\text{F} \cdot (350\,\text{V})^2 = 0.607\,\text{mJ}$. The ratio is $\dfrac{4.18\,\text{mJ}}{0.607\,\text{mJ}} = 6.89$.
**Answer:** $6.9$, two significant figures like the values of the table. The ratio is a pure number with no unit.
**Model answer c):** Substituting $C$ and $U$ into the formula of the energy gives $W = \tfrac{1}{8} \varepsilon_0 \varepsilon_\text{r} E_\text{max}^2 A d$, so with the same dimensions the energy is proportional to the quantity $\varepsilon_\text{r} E_\text{max}^2$. The relative permittivity of glass is $\tfrac{5.6}{2.1} = 2.7$ times that of Teflon, but the dielectric strength of Teflon is $\tfrac{60}{14} = 4.3$ times that of glass, and it enters the formula as a square: $4.3^2 = 18.4$. The ratio is $\tfrac{18.4}{2.7} \approx 6.9$: Teflon withstands a much greater voltage and therefore stores more energy, even though the capacitance of glass is greater.
**Reasonableness:** For Teflon the voltage is $1500\,\text{V}$ and for glass $350\,\text{V}$, and the capacitances are $3.72\,\text{nF}$ and $9.92\,\text{nF}$. The ratio is obtained from these too: $\tfrac{3.72}{9.92} \cdot \left(\tfrac{1500}{350}\right)^2 = 0.375 \cdot 18.4 = 6.9$.
