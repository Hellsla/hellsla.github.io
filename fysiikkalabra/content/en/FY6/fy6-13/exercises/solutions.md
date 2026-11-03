
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
**Principle:** The field between the plates is $E = \tfrac{U}{d}$. The field may be at most half of the dielectric strength, so the dielectric must be at least thick enough for the field to be this limiting value. When the thickness is known, the area that gives the desired capacitance is solved from the formula of a parallel-plate capacitor.
**Formula:** $\tfrac{1}{2} E_\text{max} = \dfrac{U}{d}$, from which $d = \dfrac{2U}{E_\text{max}}$, and $C = \dfrac{\varepsilon_0 \varepsilon_\text{r} A}{d}$, from which $A = \dfrac{C d}{\varepsilon_0 \varepsilon_\text{r}}$
**Conversions:** $U = 6.0\,\text{kV} = 6000\,\text{V}$, $E_\text{max} = 24 \cdot 10^{6}\,\text{V/m}$, $C = 1.0 \cdot 10^{-9}\,\text{F}$ and finally $1\,\text{m}^2 = 100\,\text{cm} \cdot 100\,\text{cm} = 10\,000\,\text{cm}^2$
**Substitution:** $d = \dfrac{2 \cdot 6000\,\text{V}}{24 \cdot 10^{6}\,\text{V/m}} = 5.0 \cdot 10^{-4}\,\text{m}$ and $A = \dfrac{1.0 \cdot 10^{-9}\,\text{F} \cdot 5.0 \cdot 10^{-4}\,\text{m}}{8.854 \cdot 10^{-12}\,\text{F/m} \cdot 2.6} \approx 0.0217\,\text{m}^2 = 217\,\text{cm}^2$
**Answer:** $220\,\text{cm}^2$, that is, $2.2 \cdot 10^{2}\,\text{cm}^2$, two significant figures like the capacitance and the voltage.
**Reasonableness:** The dielectric is $0.50\,\text{mm}$ thick, and the field in it is $6000\,\text{V} : 0.50\,\text{mm} = 12\,\text{MV/m}$, half of the dielectric strength. The side of a square would be about $15\,\text{cm}$. A thinner dielectric would make the plates smaller, but the capacitor would no longer withstand the voltage safely.
