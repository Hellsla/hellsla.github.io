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
**Principle:** In time $t$ the undisturbed wind would carry a cylinder of air through the swept area, with mass $m = \rho A v t$ and kinetic energy $\tfrac{1}{2}mv^2$. The power of the wind is this kinetic energy divided by the time. The efficiency is not needed, because we are asked for the power of the wind, not the electric power.
**Formula:** $P_\text{wind} = \dfrac{\tfrac{1}{2}mv^2}{t} = \dfrac{\tfrac{1}{2}\rho A v t\, v^2}{t}$, so $P_\text{wind} = \tfrac{1}{2}\rho A v^3$
**Conversions:** The quantities are in SI units, so the power comes out in watts; finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** $P_\text{wind} = \tfrac{1}{2} \cdot 1.25\,\tfrac{\text{kg}}{\text{m}^3} \cdot 1500\,\text{m}^2 \cdot \left(8.0\,\tfrac{\text{m}}{\text{s}}\right)^3 = 480\,000\,\text{W} = 480\,\text{kW}$
**Answer:** $480\,\text{kW}$ or $4.8 \cdot 10^{2}\,\text{kW}$, two significant figures like the wind speed $8.0\,\text{m/s}$.
**Reasonableness:** Every second $1.25 \cdot 1500 \cdot 8\,\text{kg} = 15\,000\,\text{kg}$ of air passes through the swept area in the undisturbed wind, and each kilogram has kinetic energy $\tfrac{1}{2}\cdot 8^2\,\text{J} = 32\,\text{J}$. The product is $480\,000\,\text{J}$ per second, the same result. Less than half of this would become electricity.

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
**Principle:** The undisturbed wind carries the kinetic energy $\tfrac{1}{2}\rho A v^3$ per second through the area swept by the rotor; this is the reference power of the turbine. The turbine converts the fraction $\eta$ of it into electricity, so the fraction follows from the formula for the power of a wind turbine.
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
**Principle:** The electric power is the fraction $\eta$ of the kinetic energy per second that the undisturbed wind carries through the swept area. When the wind is faster, more air flows through each second in proportion to $v$, and each kilogram has more kinetic energy in proportion to $v^2$. So the power is proportional to the cube $v^3$, when $\eta$, $\rho$ and $A$ stay the same.
**Formula:** $P = \tfrac{1}{2}\eta\rho A v^3$, so $x = \dfrac{P_2}{P_1} = \dfrac{\tfrac{1}{2}\eta\rho A v_2^3}{\tfrac{1}{2}\eta\rho A v_1^3} = \left(\dfrac{v_2}{v_1}\right)^3$
**Conversions:** Both speeds are in the same unit, so the unit cancels and no conversions are needed.
**Substitution:** $x = \left(\dfrac{9.0\,\text{m/s}}{6.0\,\text{m/s}}\right)^3 = 1.5^3 = 3.375$
**Answer:** about $3.4$ times as large, two significant figures like the wind speeds $6.0\,\text{m/s}$ and $9.0\,\text{m/s}$.
**Reasonableness:** $1.5$ times as much air flows through, and each kilogram has $1.5^2 = 2.25$ times as much kinetic energy: $1.5 \cdot 2.25 \approx 3.4$. The factor is larger than the ratio of the speeds, $1.5$, as follows from the third power.

## fy4-15-L3-02
**Given:** diameter of the old rotor $d_1 = 82\,\text{m}$, of the new one $d_2 = 162\,\text{m}$; the wind speed, the density of air and the efficiency are the same, and neither reaches its rated power
**Find:** how many times as large the electric power of the new turbine $P_2$ is as that of the old one $P_1$, the ratio $x$
**Principle:** At the same wind speed, the undisturbed wind carries a cylinder of air through the swept area of each rotor every second, and its mass is proportional to the area swept by the rotor, $A = \pi r^2$. Each kilogram of air has the same kinetic energy, so the power is proportional to the area and therefore to the square of the diameter.
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

## fy4-15-L1-06
**Find:** what explains why the power of the plant with the double head is twice as large when the flow rate and the efficiency are the same
**Principle:** Water falling through the turbine loses potential energy $mgh$, which is directly proportional to the head $h$. Since the mass $\rho Q$ passing through the turbine per second is the same, the power brought by the water $\rho Q g h$ is proportional to the head, and with the same efficiency so is the electric power.
**Model answer:** Every kilogram of water flowing through the turbine loses twice as much potential energy as it falls. The mass per second and the efficiency stay the same, so the power doubles when the head doubles. The other explanations do not hold: according to the task the flow rate is the same, the mass of the water does not grow as it falls, and the efficiency does not change.

## fy4-15-L1-07
**Given:** flow rate $Q = 35.0\,\text{m}^3\text{/s}$, head $h = 8.50\,\text{m}$; density of water $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** the power brought by the water $P_\text{o}$ in $\text{MW}$
**Principle:** The water mass $\rho Q$ falls through the turbines every second, and every kilogram loses potential energy $gh$. The efficiency is not taken into account, so the power asked for is the rate at which the potential energy decreases.
**Formula:** $P_\text{o} = \rho Q g h$
**Conversions:** The quantities are in SI units, so the power comes out in watts; finally $1\,\text{MW} = 10^{6}\,\text{W}$.
**Substitution:** $P_\text{o} = 1000\,\tfrac{\text{kg}}{\text{m}^3} \cdot 35.0\,\tfrac{\text{m}^3}{\text{s}} \cdot 9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 8.50\,\text{m} = 2\,918\,475\,\text{W} \approx 2.92\,\text{MW}$
**Answer:** $2.92\,\text{MW}$, three significant figures like the flow rate $35.0\,\text{m}^3\text{/s}$ and the head $8.50\,\text{m}$.
**Reasonableness:** $35\,000\,\text{kg}$ of water falls every second, and a kilogram loses about $10 \cdot 8.5\,\text{J} = 85\,\text{J}$ in an $8.5\,\text{m}$ drop. The product is about $3.0\,\text{MW}$, so the result is of the right magnitude. With an efficiency, the electric power would be less than $2.92\,\text{MW}$.

## fy4-15-L1-08
**Given:** mass of air $m = 2.50 \cdot 10^{3}\,\text{kg}$, speed $v = 12.0\,\text{m/s}$
**Find:** the kinetic energy $E_\text{k}$ in $\text{kJ}$
**Principle:** The kinetic energy of a moving body depends on its mass and on the square of its speed. The mass of air is calculated as one body whose parts all move at the speed $v$.
**Formula:** $E_\text{k} = \tfrac{1}{2}mv^2$
**Conversions:** The quantities are in SI units, so the energy comes out in joules; finally $1\,\text{kJ} = 1000\,\text{J}$.
**Substitution:** $E_\text{k} = \tfrac{1}{2} \cdot 2.50 \cdot 10^{3}\,\text{kg} \cdot \left(12.0\,\tfrac{\text{m}}{\text{s}}\right)^2 = 180\,000\,\text{J} = 180\,\text{kJ}$
**Answer:** $180\,\text{kJ}$, three significant figures like the mass and the speed.
**Reasonableness:** A kilogram of air at $12\,\text{m/s}$ has kinetic energy $\tfrac{1}{2} \cdot 12^2\,\text{J} = 72\,\text{J}$, and $2500$ kilograms have $2500 \cdot 72\,\text{J} = 180\,\text{kJ}$. The result agrees.

## fy4-15-L2-05
**Given:** table: power $P$ and time $t$ per year at five wind speeds (example data); at other times the power is zero
**Find:** the annual energy $E$ in $\text{GWh}$
**Principle:** Power tells the rate at which energy is converted, so the energy is power times time. At each speed the power is constant, so the energy of each row is $P t$. The annual energy is the sum of the energies of the rows.
**Formula:** $E = \sum P t$
**Conversions:** When the power is in kilowatts and the time in hours, the energy comes out in kilowatt-hours. Finally $1\,\text{GWh} = 10^{6}\,\text{kWh}$.
**Substitution:** The energies of the rows are $100\,\text{kW} \cdot 1500\,\text{h} = 150\,000\,\text{kWh}$, $340 \cdot 2200 = 748\,000\,\text{kWh}$, $850 \cdot 1800 = 1\,530\,000\,\text{kWh}$, $1650 \cdot 1000 = 1\,650\,000\,\text{kWh}$ and $2000 \cdot 700 = 1\,400\,000\,\text{kWh}$. The sum is $5\,478\,000\,\text{kWh}$, so $E = 5.478\,\text{GWh}$.
**Answer:** $5.5\,\text{GWh}$, two significant figures, because the powers in the table are given to two or three significant figures.
**Reasonableness:** If the turbine produced its rated power $2000\,\text{kW}$ for the whole year ($8760\,\text{h}$), the energy would be $17.5\,\text{GWh}$. The result $5.5\,\text{GWh}$ is about $31\,\%$ of that, which fits the fact that the mean power of a wind turbine is clearly lower than its rated power.

## fy4-15-L2-06
**Given:** flow rates from April to September $85$, $120$, $45$, $30$, $28$ and $40\,\text{m}^3\text{/s}$ (example data), head $h = 9.0\,\text{m}$, efficiency $\eta = 0.85$, length of a month $30\,\text{days}$; $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** a) the electric energy $E$ in $\text{GWh}$; b) the ratio of the powers in May and August and an explanation of the variation
**Principle:** The power of a hydropower plant at the flow rate of a month is $P = \eta\rho Q g h$. Since $\eta$, $\rho$ and $h$ are constants, the power is proportional to the flow rate. Energy is power times time, and every month has the same length, so the energy is obtained by summing the powers of the months and multiplying by the length of one month.
**Formula:** $P = \eta\rho Q g h$ and $E = Pt$, so $E = \eta\rho g h\,\left(\sum Q\right) t$
**Conversions:** The length of a month is $t = 30 \cdot 24\,\text{h} = 720\,\text{h}$. The power is calculated in watts and converted to megawatts, $1\,\text{MW} = 10^{6}\,\text{W}$, so the energy comes out in megawatt-hours; finally $1\,\text{GWh} = 1000\,\text{MWh}$.
**Substitution:** The sum of the flow rates is $85 + 120 + 45 + 30 + 28 + 40 = 348\,\text{m}^3\text{/s}$. The sum of the monthly powers is
$$\begin{aligned}\textstyle\sum P &= 0.85 \cdot 1000 \cdot 9.81 \cdot 9.0 \cdot 348\,\text{W} \\ &= 26.12\,\text{MW}\end{aligned}$$
and the energy
$$\begin{aligned}E &= 26.12\,\text{MW} \cdot 720\,\text{h} \\ &= 18\,804\,\text{MWh} \\ &= 18.8\,\text{GWh}\end{aligned}$$
**Answer:** $19\,\text{GWh}$, two significant figures like the head $9.0\,\text{m}$ and the efficiency $0.85$.
**Model answer for part b:** The power is proportional to the flow rate, so the ratio of the powers in May and August is the same as the ratio of the flow rates, $120 : 28 = 4.3$. In May the power is about $9.0\,\text{MW}$ and in August about $2.1\,\text{MW}$. In the table the flow rate is greatest in spring and smallest in late summer, so the production varies with how much water flows in the river. The head and the efficiency stay constant, so they do not explain the variation.
**Reasonableness:** The mean flow rate is $348 : 6 = 58\,\text{m}^3\text{/s}$, and at that flow rate the power would be $0.85 \cdot 1000 \cdot 58 \cdot 9.81 \cdot 9.0\,\text{W} \approx 4.35\,\text{MW}$. Over six months ($4320\,\text{h}$) the energy would be $4.35\,\text{MW} \cdot 4320\,\text{h} \approx 18.8\,\text{GWh}$, the same result.

## fy4-15-L2-07
**Given:** diameter $d = 60\,\text{m}$, wind speed $v = 7.0\,\text{m/s}$, density of air $\rho = 1.25\,\text{kg/m}^3$, efficiency $\eta = 0.40$; the student's result $4.9\,\text{kW}$
**Find:** the student's error and the correct electric power $P$ in $\text{kW}$
**Principle:** The mass of air that the undisturbed wind carries through the swept area per second is proportional to the speed $v$, and the kinetic energy of each kilogram of air is proportional to the square of the speed $v^2$. The power of the wind is therefore proportional to the cube of the speed $v^3$. The student used the speed to the first power.
**Formula:** $P = \tfrac{1}{2}\eta\rho A v^3$ and $A = \pi r^2$
**Conversions:** The radius is $r = 60\,\text{m} : 2 = 30\,\text{m}$. The area is $A = \pi \cdot (30\,\text{m})^2 = 2827\,\text{m}^2$, as in the student's solution. Finally $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** The correct power is
$$\begin{aligned}P &= 0.5 \cdot 0.40 \cdot 1.25\,\tfrac{\text{kg}}{\text{m}^3} \\ &\quad \cdot 2827\,\text{m}^2 \cdot \left(7.0\,\tfrac{\text{m}}{\text{s}}\right)^3 \\ &= 242\,452\,\text{W}\end{aligned}$$
**Answer:** $240\,\text{kW}$ or $2.4 \cdot 10^{2}\,\text{kW}$, two significant figures like the wind speed $7.0\,\text{m/s}$ and the efficiency $0.40$.
**Model answer for the error:** In the student's formula the wind speed is to the first power, although it must be to the third power. The error can be noticed from the units: $\tfrac{\text{kg}}{\text{m}^3} \cdot \text{m}^2 \cdot \tfrac{\text{m}}{\text{s}}$ is $\tfrac{\text{kg}}{\text{s}}$, not a watt $\tfrac{\text{kg} \cdot \text{m}^2}{\text{s}^3}$: the result lacks the factor $v^2$, that is, the unit $\tfrac{\text{m}^2}{\text{s}^2}$. The correct power is $7.0^2 = 49$ times the student's result.
**Reasonableness:** The student's result $4948\,\text{W}$ multiplied by $49$ is $242\,452\,\text{W}$, the same as the correct result. The power of the wind is $240 : 0.40 = 600\,\text{kW}$, and $40\,\%$ of it is converted into electricity, as it should be.

## fy4-15-L3-04
**Given:** table: speeds $v = 4$–$9\,\text{m/s}$ and powers $P = 80$–$905\,\text{kW}$ (example data), diameter $d = 80\,\text{m}$, density of air $\rho = 1.25\,\text{kg/m}^3$, rated power $2.0\,\text{MW}$
**Find:** a) whether $P \propto v^3$; b) the efficiency $\eta$ as a percentage; c) the power of the model at a speed of $13\,\text{m/s}$ and its comparison with the rated power
**Principle:** If the power follows the model $P = k v^3$, the ratio $P/v^3 = k$ is constant. In the formula of a wind turbine, $P = \tfrac{1}{2}\eta\rho A v^3$, the constant is $k = \tfrac{1}{2}\eta\rho A$, so the efficiency is obtained from the constant $k$ when the area of the rotor is known.
**Formula:** $k = \dfrac{P}{v^3}$ and $k = \tfrac{1}{2}\eta\rho A$, so $\eta = \dfrac{2k}{\rho A}$ and $A = \pi r^2$
**Conversions:** The radius is $r = 80\,\text{m} : 2 = 40\,\text{m}$, and $A = \pi \cdot (40\,\text{m})^2 = 5027\,\text{m}^2$. The ratios are calculated in the unit $\text{kW}/(\text{m/s})^3$; the mean is converted to watts, $1\,\text{kW} = 1000\,\text{W}$.
**Substitution:** The ratios $P/v^3$ at the speeds $4$–$9\,\text{m/s}$ are $1.250$, $1.240$, $1.273$, $1.239$, $1.270$ and $1.241$ in the unit $\tfrac{\text{kW}}{(\text{m/s})^3}$.
The sum of the ratios is $7.513$, so the mean is $k_\text{mean} = 7.513 : 6 = 1.252\,\tfrac{\text{kW}}{(\text{m/s})^3} = 1252\,\tfrac{\text{W}}{(\text{m/s})^3}$. The efficiency is
$$\begin{aligned}\eta &= \frac{2 \cdot 1252}{1.25 \cdot 5027} \\ &= 0.3986\end{aligned}$$
**Answer:** $40\,\%$, two significant figures, because the powers in the table are given to two or three significant figures.
**Model answer for parts a and c:** The speed grows from $4\,\text{m/s}$ to $9\,\text{m/s}$, that is, $2.25$-fold, so $v^3$ grows more than $11$-fold, and the power grows by the same factor: $905 : 80 \approx 11.3$. The ratio $P/v^3$ stays between $1.24$ and $1.27$, that is, it varies only by about $\pm 2\,\%$ over the whole speed range. The random scatter of the points explains the small variation, and the ratio neither grows nor decreases with the speed, so the model $P = k v^3$ fits the data. Doubling supports the result: from $4\,\text{m/s}$ to $8\,\text{m/s}$ the power grows by a factor of $650 : 80 \approx 8.1$, and $2^3 = 8$. The prediction of the model at $13\,\text{m/s}$ is $1.252 \cdot 13^3\,\text{kW} \approx 2750\,\text{kW} = 2.8\,\text{MW}$, which is greater than the rated power $2.0\,\text{MW}$. The turbine cannot produce more than its rated power; the blades are turned to let part of the wind pass, so the model $P = k v^3$ holds only below the rated power.
**Reasonableness:** The power of the wind at $9\,\text{m/s}$ is $\tfrac{1}{2} \cdot 1.25 \cdot 5027 \cdot 9^3\,\text{W} \approx 2290\,\text{kW}$, and $905\,\text{kW}$ is $905 : 2290 \approx 0.40$ of it, the same as the efficiency obtained. The result is below the theoretical upper limit of $59\,\%$ and below half, as for a wind turbine.

## fy4-15-L3-05
**Given:** surplus powers $40$, $52$, $62$, $58$, $48$ and $40\,\text{MW}$ over six hours, as the mean of each hour (example data); lifting height $h = 85.0\,\text{m}$, efficiency of the pumps $\eta = 0.800$, volume of the upper reservoir $1.20 \cdot 10^{6}\,\text{m}^3$, consumption $40.0\,\text{MW}$; $\rho = 1000\,\text{kg/m}^3$, $g = 9.81\,\text{m/s}^2$
**Find:** a) the volume $V$ of the pumped water in $\text{m}^3$; b) whether the water fits into the upper reservoir; c) how long the stored energy lasts for a consumption of $40.0\,\text{MW}$
**Principle:** The surplus electric energy is power times time. The pumps convert the fraction $\eta$ of it into the potential energy $mgh$ of the water, from which the mass of the lifted water is solved, and then the volume $V = m/\rho$.
**Formula:** $E = \sum P t$, $\eta E = mgh$, so $m = \dfrac{\eta E}{gh}$ and $V = \dfrac{m}{\rho}$
**Conversions:** The power of each hour is constant, so $E$ comes out in megawatt-hours. Finally $1\,\text{MWh} = 10^{6}\,\text{W} \cdot 3600\,\text{s} = 3.6 \cdot 10^{9}\,\text{J}$.
**Substitution:** The sum of the powers is $40 + 52 + 62 + 58 + 48 + 40 = 300\,\text{MW}$, and each power lasts one hour, so $E = 300\,\text{MWh} = 300 \cdot 3.6 \cdot 10^{9}\,\text{J} = 1.08 \cdot 10^{12}\,\text{J}$. The energy transferred to the water is $\eta E = 0.800 \cdot 1.08 \cdot 10^{12}\,\text{J} = 8.64 \cdot 10^{11}\,\text{J}$. The mass and the volume are
$$\begin{aligned}m &= \frac{8.64 \cdot 10^{11}\,\text{J}}{9.81\,\tfrac{\text{m}}{\text{s}^2} \cdot 85.0\,\text{m}} \\ &= 1.036 \cdot 10^{9}\,\text{kg} \\ V &= \frac{m}{\rho} = 1.036 \cdot 10^{6}\,\text{m}^3\end{aligned}$$
**Answer:** $1.04 \cdot 10^{6}\,\text{m}^3$, three significant figures like the height $85.0\,\text{m}$ and the efficiency $0.800$.
**Model answer for parts b and c:** The pumped water $1.04 \cdot 10^{6}\,\text{m}^3$ is less than the volume of the upper reservoir $1.20 \cdot 10^{6}\,\text{m}^3$, so the water fits into the reservoir and it fills to about $86\,\%$. The energy stored in the water is $0.800 \cdot 300\,\text{MWh} = 240\,\text{MWh}$. At a power of $40.0\,\text{MW}$ it would last $240\,\text{MWh} : 40.0\,\text{MW} = 6.00\,\text{h}$, if the losses of the turbine and the generator are ignored. In reality the losses shorten the time. A pumped-storage plant suits well alongside wind power, because wind power depends on the weather and its power can exceed consumption, while hydropower is easy to regulate. Surplus electricity can be stored as the potential energy of water and converted back into electricity when the wind calms down and consumption is greater than production.
**Reasonableness:** Let us check the potential energy: $1.036 \cdot 10^{9}\,\text{kg} \cdot 9.81\,\text{m/s}^2 \cdot 85.0\,\text{m} = 8.64 \cdot 10^{11}\,\text{J}$, which is $240\,\text{MWh}$. A cubic metre of water at a height of $85\,\text{m}$ stores about $1000 \cdot 9.81 \cdot 85\,\text{J} = 0.83\,\text{MJ}$, so $240\,\text{MWh} = 8.64 \cdot 10^{5}\,\text{MJ}$ requires about $10^{6}$ cubic metres, as obtained.

## fy4-15-L2-08
**Find:** the order of magnitude of the electric power $P$ of the wind turbine.
**Principle:** The undisturbed wind carries the power $\tfrac{1}{2}\rho A v^3$ through the area swept by the rotor, and the turbine converts the fraction $\eta$ of this reference power into electricity. The turbine does not reach its rated power, so the formula $P = \tfrac{1}{2}\eta\rho A v^3$ describes it. The speed must be converted to the unit $\text{m/s}$, because it is in the formula to the third power.
**Model answer:** The radius is $r = 100\,\text{m} : 2 = 50\,\text{m}$ and $\eta = 0.40$. The wind speed is converted to $\text{m/s}$, and then the area swept by the rotor and the electric power are calculated:

$$\begin{aligned}
&v = 36\,\text{km/h} \\
&\phantom{v} = \dfrac{36\,000\,\text{m}}{3600\,\text{s}} \\
&\phantom{v} = 10\,\text{m/s} \\
&A = \pi r^2 = \pi \cdot (50\,\text{m})^2 \\
&\phantom{A} \approx 7854\,\text{m}^2 \\
&P = \tfrac{1}{2}\eta\rho A v^3 \\
&\phantom{P} = 0.5 \cdot 0.40 \cdot 1.25\,\tfrac{\text{kg}}{\text{m}^3} \\
&\qquad \cdot 7854\,\text{m}^2 \cdot \left(10\,\tfrac{\text{m}}{\text{s}}\right)^3 \\
&\phantom{P} \approx 1.96 \cdot 10^{6}\,\text{W}
\end{aligned}$$

The electric power is of the order of magnitude $2\,\text{MW}$. The power can be written as $P = \eta \cdot \tfrac{1}{2}v^2 \cdot \rho A v$, where $\tfrac{1}{2}v^2$ is the kinetic energy of one kilogram of air and $\rho A v$ is the mass of air that the undisturbed wind carries through the swept area per second. Both grow with the speed. The option $0.2\,\text{MW}$ comes from calculating the power as proportional to the square $v^2$: only the kinetic energy per kilogram is included, and the growth of the mass flow is forgotten. The option $20\,\text{kW}$ comes from calculating the power as proportional to the speed $v$: only the mass flow is included, and the growth of the kinetic energy per kilogram is forgotten. If the speed is substituted as the number $36$ without converting it, the result is about $47$ times too large, about $90\,\text{MW}$.

The result is reasonable. The power of the wind is $P : \eta \approx 4.9\,\text{MW}$, and less than half of it becomes electricity. In the example of the chapter a $120\,\text{m}$ rotor produced about $2.3\,\text{MW}$ at a wind speed of $9.0\,\text{m/s}$, so the result is of the same order of magnitude.
