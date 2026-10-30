## fy4-15-L1-01
**Given:** head $h = 15.0\,\text{m}$, flow rate $Q = 120\,\text{m}^3\text{/s}$, efficiency $\eta = 0.900$; density of water $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** the electric power $P$ in $\text{MW}$
**Principle:** The water falling through the turbines loses potential energy $mgh$, and the mass $\rho Q$ falls every second. The plant converts the fraction $\eta$ of this power into electricity, so we use the formula for the power of a hydropower plant.
**Formula:** $P = \eta\rho Q g h$
**Conversions:** The quantities are in SI units, so the power comes out in watts; finally $1\,\text{MW} = 10^{6}\,\text{W}$.
**Substitution:** $P = 0.900 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 120\,\tfrac{\text{m}^3}{\text{s}} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 15.0\,\text{m} = 15\,892\,200\,\text{W} \approx 15.9\,\text{MW}$
**Answer:** $15.9\,\text{MW}$, three significant figures like the head $15.0\,\text{m}$, the flow rate $120\,\text{m}^3\text{/s}$ and the efficiency $0.900$.
**Reasonableness:** A cubic metre of water gives about $1000\,\text{kg} \cdot 10\,\text{m/s}^2 \cdot 15\,\text{m} = 150\,\text{kJ}$ in a $15\,\text{m}$ drop, so $120$ cubic metres per second give about $18\,\text{MW}$, and $90\,\%$ of that is about $16\,\text{MW}$. The power is smaller than the $192\,\text{MW}$ of Imatra, because both the flow rate and the head are smaller.

## fy4-15-L1-02
**Given:** mass of water $m = 1000\,\text{kg}$, height difference $h = 24.0\,\text{m}$; $g = 9.81\,\text{m/s}^2$
**Find:** the decrease in potential energy $E_\text{p}$ in $\text{kJ}$
**Principle:** Gravitational potential energy is proportional to the height above the chosen zero level. When the zero level is the surface of the tailwater, the potential energy of the water in the upper reservoir is $mgh$, and that is exactly how much it decreases when it falls to the tailwater.
**Formula:** $E_\text{p} = mgh$
**Conversions:** The quantities are in SI units, so the energy comes out in joules; finally $1\,\text{kJ} = 1000\,\text{J}$.
**Substitution:** $E_\text{p} = 1000\,\text{kg} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 24.0\,\text{m} = 235\,440\,\text{J} \approx 235\,\text{kJ}$
**Answer:** $235\,\text{kJ}$, three significant figures like the height difference $24.0\,\text{m}$.
**Reasonableness:** The estimate $1000\,\text{kg} \cdot 10\,\text{m/s}^2 \cdot 24\,\text{m} = 240\,\text{kJ}$ is close to the result. If hundreds of cubic metres fall every second, the power is hundreds of times $235\,\text{kW}$, that is tens or hundreds of megawatts, as in large hydropower plants.

## fy4-15-L1-03
**Given:** power of the water flowing into the turbine $P_\text{o} = 50.0\,\text{MW}$, electric power $P_\text{s} = 46.0\,\text{MW}$
**Find:** the efficiency $\eta$ as a percentage
**Principle:** Efficiency is the ratio of the useful power obtained to the power taken into the device. Here the useful power is the electric power and the power taken in is the power the water brings to the plant.
**Formula:** $\eta = \dfrac{P_\text{s}}{P_\text{o}}$
**Conversions:** Both powers are in megawatts, so the unit cancels. A decimal number is changed to a percentage by multiplying by one hundred.
**Substitution:** $\eta = \dfrac{46.0\,\text{MW}}{50.0\,\text{MW}} = 0.920 = 92.0\,\%$
**Answer:** $92.0\,\%$, three significant figures like the powers $46.0\,\text{MW}$ and $50.0\,\text{MW}$.
**Reasonableness:** The efficiency is below $100\,\%$, as it should be, and the efficiency of a large hydropower plant is typically about $90\,\%$. The losses are $4.0\,\text{MW}$, that is $8\,\%$ of the power taken in.

## fy4-15-L1-04
**Given:** area swept by the rotor $A = 1500\,\text{m}^2$, wind speed $v = 8.0\,\text{m/s}$, density of air $\rho = 1.25\,\text{kg/m}^3$
**Find:** the power of the wind $P_\text{wind}$ in $\text{kW}$
**Principle:** In time $t$ a cylinder of air flows through the rotor, with mass $m = \rho A v t$ and kinetic energy $\tfrac{1}{2}mv^2$. The power of the wind is this kinetic energy divided by the time. The efficiency is not needed, because we are asked for the power of the wind, not the electric power.
**Formula:** $P_\text{wind} = \dfrac{\tfrac{1}{2}mv^2}{t} = \dfrac{\tfrac{1}{2}\rho A v t\, v^2}{t}$, so $P_\text{wind} = \tfrac{1}{2}\rho A v^3$
**Conversions:** The quantities are in SI units, so the power comes out in watts; finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P_\text{wind} = \tfrac{1}{2} \cdot 1.25\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1500\,\text{m}^2 \cdot \left(8.0\,\tfrac{\text{m}}{\text{s}}\right)^3 = 480\,000\,\text{W} = 480\,\text{kW}$
**Answer:** $480\,\text{kW}$ or $4.8 \cdot 10^{2}\,\text{kW}$, two significant figures like the wind speed $8.0\,\text{m/s}$.
**Reasonableness:** Every second $1.25 \cdot 1500 \cdot 8\,\text{kg} = 15\,000\,\text{kg}$ of air flows through the rotor, and each kilogram has kinetic energy $\tfrac{1}{2}\cdot 8^2\,\text{J} = 32\,\text{J}$. The product is $480\,000\,\text{J}$ per second, the same result. Less than half of this would become electricity.

## fy4-15-L1-05
**Given:** electric power $P = 3.00\,\text{MW}$, time $t = 6.00\,\text{h}$
**Find:** the electric energy $E$ in $\text{MWh}$
**Principle:** Power tells how much energy is converted per unit of time. When the power stays constant, the energy is power times time.
**Formula:** $P = \dfrac{E}{t}$, so $E = Pt$
**Conversions:** When the power is in megawatts and the time in hours, the energy comes out directly in megawatt-hours, so no conversions are needed.
**Substitution:** $E = 3.00\,\text{MW} \cdot 6.00\,\text{h} = 18.0\,\text{MWh}$
**Answer:** $18.0\,\text{MWh}$, three significant figures like the power $3.00\,\text{MW}$ and the time $6.00\,\text{h}$.
**Reasonableness:** In joules the energy is $3.00 \cdot 10^{6}\,\text{W} \cdot 6.00 \cdot 3600\,\text{s} \approx 6.5 \cdot 10^{10}\,\text{J}$. A detached house with electric heating uses about $20\,\text{MWh}$ a year, so this is almost one house's consumption for a whole year.

## fy4-15-L2-01
**Given:** electric power $P = 10.0\,\text{MW}$, head $h = 12.0\,\text{m}$, efficiency $\eta = 0.880$; density of water $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** the flow rate $Q$ in $\text{m}^3\text{/s}$
**Principle:** Falling water loses potential energy, and the plant converts the fraction $\eta$ of it into electricity. We solve the flow rate that gives the desired power from the formula for the power of a hydropower plant.
**Formula:** $P = \eta\rho Q g h$, so $Q = \dfrac{P}{\eta\rho g h}$
**Conversions:** $P = 10.0\,\text{MW} = 10.0 \cdot 10^{6}\,\text{W}$
**Substitution:** The quantities are in SI units, and $\tfrac{\text{W}}{\text{kg/m}^3 \cdot \text{m/s}^2 \cdot \text{m}} = \tfrac{\text{m}^3}{\text{s}}$, so $Q = \dfrac{10.0 \cdot 10^{6}}{0.880 \cdot 1000 \cdot 9.81 \cdot 12.0}\,\tfrac{\text{m}^3}{\text{s}} = 96.53\,\tfrac{\text{m}^3}{\text{s}}$
**Answer:** $96.5\,\text{m}^3\text{/s}$, three significant figures like the power $10.0\,\text{MW}$, the head $12.0\,\text{m}$ and the efficiency $0.880$.
**Reasonableness:** A cubic metre of water gives about $120\,\text{kJ}$ in a $12\,\text{m}$ drop and about $105\,\text{kJ}$ of electricity. So a power of $10\,\text{MW}$ needs about $10\,000 : 105 \approx 95$ cubic metres per second.

## fy4-15-L2-02
**Given:** rotor diameter $d = 82\,\text{m}$, wind speed $v = 8.0\,\text{m/s}$, electric power $P = 758\,\text{kW}$, density of air $\rho = 1.25\,\text{kg/m}^3$
**Find:** the fraction converted into electricity, that is the efficiency $\eta$, as a percentage
**Principle:** The power of the wind flowing through the rotor is the kinetic energy of the air per second, $\tfrac{1}{2}\rho A v^3$. The turbine converts the fraction $\eta$ of it into electricity, so the fraction follows from the formula for the power of a wind turbine.
**Formula:** $P = \tfrac{1}{2}\eta\rho A v^3$ and $A = \pi r^2$, so $\eta = \dfrac{2P}{\rho A v^3}$
**Conversions:** The radius is $r = 82\,\text{m} : 2 = 41\,\text{m}$ and $P = 758\,\text{kW} = 758\,000\,\text{W}$.
**Substitution:** $A = \pi \cdot (41\,\text{m})^2 = 5281.0\,\text{m}^2$ and $\eta = \dfrac{2 \cdot 758\,000\,\text{W}}{1.25\,\tfrac{\text{kg}}{\text{m}^3} \cdot 5281.0\,\text{m}^2 \cdot \left(8.0\,\tfrac{\text{m}}{\text{s}}\right)^3} = 0.4485$
**Answer:** about $45\,\%$, two significant figures like the diameter $82\,\text{m}$ and the wind speed $8.0\,\text{m/s}$.
**Reasonableness:** The fraction is below the theoretical upper limit of $59\,\%$, and the fraction of a real wind turbine is less than half, as it should be. The power of the wind is about $1.7\,\text{MW}$, and the electric power $0.76\,\text{MW}$ is a little less than half of it.

## fy4-15-L2-03
**Given:** flow rate $Q = 850\,\textsf{l}\text{/s}$, head $h = 6.5\,\text{m}$, efficiency $\eta = 0.75$; density of water $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** the electric power $P$ in $\text{kW}$
**Principle:** The water falling through the turbine loses potential energy, and the mass $\rho Q$ falls every second. The plant converts the fraction $\eta$ of this power into electricity, so we use the formula for the power of a hydropower plant.
**Formula:** $P = \eta\rho Q g h$
**Conversions:** $850\,\textsf{l} = 850 \cdot 0.001\,\text{m}^3 = 0.850\,\text{m}^3$, so $Q = 0.850\,\text{m}^3\text{/s}$; finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P = 0.75 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 0.850\,\tfrac{\text{m}^3}{\text{s}} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 6.5\,\text{m} = 40\,650\,\text{W} \approx 41\,\text{kW}$
**Answer:** $41\,\text{kW}$, two significant figures like the head $6.5\,\text{m}$ and the efficiency $0.75$.
**Reasonableness:** Every second $850\,\text{kg}$ of water falls, which gives about $850 \cdot 10 \cdot 6.5\,\text{J} \approx 55\,\text{kJ}$ in a $6.5\,\text{m}$ drop, and three quarters of that is about $41\,\text{kJ}$ per second. If the litres were not converted, the result would be a thousand times too large, $41\,\text{MW}$, which is far too much for a stream.

## fy4-15-L2-04
**Given:** head $h = 9.50\,\text{m}$, flow rate $Q = 3.20\,\text{m}^3\text{/s}$, efficiency $\eta = 0.800$, time $t = 24.0\,\text{h}$; density of water $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** the electric energy $E$ in $\text{MWh}$
**Principle:** First we calculate the electric power from the formula for the power of a hydropower plant, because the fraction $\eta$ of the potential energy of the falling water becomes electricity. The power stays constant when the flow rate stays constant, so the energy is power times time.
**Formula:** $P = \eta\rho Q g h$ and $E = Pt$, so $E = \eta\rho Q g h t$
**Conversions:** The power is calculated in watts and converted to megawatts, $1\,\text{MW} = 10^{6}\,\text{W}$; the time is kept in hours, so the energy comes out in megawatt-hours.
**Substitution:** $P = 0.800 \cdot 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 3.20\,\tfrac{\text{m}^3}{\text{s}} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 9.50\,\text{m} = 238\,579\,\text{W}$ and $E = 0.238\,579\,\text{MW} \cdot 24.0\,\text{h} = 5.7259\,\text{MWh}$
**Answer:** $5.73\,\text{MWh}$, three significant figures like the initial data.
**Reasonableness:** The power is about $0.24\,\text{MW}$, and a day has $24$ hours: $0.24 \cdot 24 \approx 5.8\,\text{MWh}$. That is about a third of the yearly consumption of a detached house with electric heating, which fits a small power plant.

## fy4-15-L3-01
**Given:** wind speed before $v_1 = 6.0\,\text{m/s}$ and after $v_2 = 9.0\,\text{m/s}$; the rotor and the efficiency are the same, and the turbine does not reach its rated power
**Find:** how many times as large the electric power $P_2$ is as $P_1$, the ratio $x$
**Principle:** The electric power is the fraction $\eta$ of the kinetic energy per second of the air flowing through the rotor. When the wind is faster, more air flows through each second in proportion to $v$, and each kilogram has more kinetic energy in proportion to $v^2$. So the power is proportional to the cube $v^3$, when $\eta$, $\rho$ and $A$ stay the same.
**Formula:** $P = \tfrac{1}{2}\eta\rho A v^3$, so $x = \dfrac{P_2}{P_1} = \dfrac{\tfrac{1}{2}\eta\rho A v_2^3}{\tfrac{1}{2}\eta\rho A v_1^3} = \left(\dfrac{v_2}{v_1}\right)^3$
**Conversions:** Both speeds are in the same unit, so the unit cancels and no conversions are needed.
**Substitution:** $x = \left(\dfrac{9.0\,\text{m/s}}{6.0\,\text{m/s}}\right)^3 = 1.5^3 = 3.375$
**Answer:** about $3.4$ times as large, two significant figures like the wind speeds $6.0\,\text{m/s}$ and $9.0\,\text{m/s}$.
**Reasonableness:** $1.5$ times as much air flows through, and each kilogram has $1.5^2 = 2.25$ times as much kinetic energy: $1.5 \cdot 2.25 \approx 3.4$. The factor is larger than the ratio of the speeds, $1.5$, as follows from the third power.

## fy4-15-L3-02
**Given:** diameter of the old rotor $d_1 = 82\,\text{m}$, of the new one $d_2 = 162\,\text{m}$; the wind speed, the density of air and the efficiency are the same, and neither reaches its rated power
**Find:** how many times as large the electric power of the new turbine $P_2$ is as that of the old one $P_1$, the ratio $x$
**Principle:** At the same wind speed, a cylinder of air flows through each rotor every second, and its mass is proportional to the area swept by the rotor, $A = \pi r^2$. Each kilogram of air has the same kinetic energy, so the power is proportional to the area and therefore to the square of the diameter.
**Formula:** $P = \tfrac{1}{2}\eta\rho A v^3$ and $A = \pi\left(\tfrac{d}{2}\right)^2$, so $x = \dfrac{P_2}{P_1} = \dfrac{A_2}{A_1} = \left(\dfrac{d_2}{d_1}\right)^2$
**Conversions:** The diameters are in the same unit, so the unit cancels and no conversions are needed.
**Substitution:** $x = \left(\dfrac{162\,\text{m}}{82\,\text{m}}\right)^2 = 1.9756^2 = 3.903$
**Answer:** about $3.9$ times as large, two significant figures like the diameter $82\,\text{m}$.
**Reasonableness:** The diameter is about double, so the area is about $2^2 = 4$ times as large, and the result is a little below four. This is why new turbines have ever longer blades: the area grows with the square of the diameter.

## fy4-15-L3-03
**Given:** wind speed $v = 10.0\,\text{m/s}$, mass $m = 1\,\text{kg}$ for both the air and the water; $g = 9.81\,\text{m/s}^2$
**Find:** the height of the fall $h$ in $\text{m}$
**Principle:** The kinetic energy of a kilogram of air is $\tfrac{1}{2}mv^2$, and the potential energy of a kilogram of water decreases by $mgh$ in a fall. We set these equal. The mass cancels, so the result does not depend on how many kilograms are compared.
**Formula:** $mgh = \tfrac{1}{2}mv^2$, so $h = \dfrac{v^2}{2 \cdot g}$
**Conversions:** The quantities are in SI units, so no conversions are needed.
**Substitution:** $h = \dfrac{\left(10.0\,\tfrac{\text{m}}{\text{s}}\right)^2}{2 \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2}} = 5.097\,\text{m}$
**Answer:** $5.10\,\text{m}$, three significant figures like the wind speed $10.0\,\text{m/s}$.
**Reasonableness:** A kilogram of wind has kinetic energy of only $50\,\text{J}$, while in the $24\,\text{m}$ drop at Imatra a kilogram of water gives about $235\,\text{J}$. So wind has little energy per kilogram, and air is also light, which is why the rotor of a wind turbine has to be large. Unit: $\tfrac{\text{m}^2/\text{s}^2}{\text{m}/\text{s}^2} = \text{m}$.
