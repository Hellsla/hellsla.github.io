## fy3-15-L1-01
**Given:** efficiency of the turbine $\eta_1 = 92.0\,\% = 0.920$, efficiency of the generator $\eta_2 = 98.0\,\% = 0.980$
**Find:** the efficiency $\eta$ of the whole plant as a percentage
**Principle:** The plant is a chain in which the output power of the turbine is the input power of the generator. Each step lets through only part of the energy coming into it, so the efficiency of the chain is the product of the efficiencies of the steps.
**Formula:** $P_1 = \eta_1 P_0$ and $P_2 = \eta_2 P_1$, so $\eta = \dfrac{P_2}{P_0} = \eta_1 \eta_2$
**Conversions:** The efficiencies are fractions of a whole: $92.0\,\% = 0.920$ and $98.0\,\% = 0.980$. At the end the result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta = 0.920 \cdot 0.980 = 0.9016 = 90.16\,\%$
**Answer:** $90.2\,\%$, three significant figures like the given efficiencies $92.0\,\%$ and $98.0\,\%$.
**Reasonableness:** The product is smaller than either efficiency, as it should be when the factors are less than 1. Estimate: $0.92 \cdot 0.98 \approx 0.92 - 0.02 \cdot 0.92 \approx 0.90$. A hydropower plant is not a heat engine, so its efficiency can be over 90%.

## fy3-15-L1-02
**Given:** power of the kinetic energy of the air flow $P_\text{wind} = 2.50\,\text{MW}$ and electric power $P_\text{elec} = 1.05\,\text{MW}$
**Find:** the efficiency $\eta$ of the turbine as a percentage
**Principle:** Efficiency is the share of the useful power in the power coming into the plant. Here the input power is the power of the kinetic energy of the air flowing through the rotor and the useful power is the power going to the electricity grid; the rest of the energy stays in the motion of the air or turns into heat.
**Formula:** $\eta = \dfrac{P_\text{elec}}{P_\text{wind}}$
**Conversions:** Both powers are in megawatts, so the units cancel. The result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta = \dfrac{1.05\,\text{MW}}{2.50\,\text{MW}} = 0.420 = 42.0\,\%$
**Answer:** $42.0\,\%$, three significant figures like the powers $2.50\,\text{MW}$ and $1.05\,\text{MW}$.
**Reasonableness:** Estimate: $1 / 2.5 = 0.4$, which matches the result. The efficiency of a modern wind turbine is at best about 40–45%. You cannot take all the energy from the wind, because the air has to keep moving after the rotor too; the rest is lost to friction and electrical losses.

## fy3-15-L1-03
**Given:** area $A = 20.0\,\text{m}^2$, radiation power per unit area $I = 1.00\,\tfrac{\text{kW}}{\text{m}^2}$, efficiency $\eta = 0.210$
**Find:** the electric power $P$ of the panel in kilowatts
**Principle:** The power of the radiation hitting the panel is the intensity times the area, and the efficiency tells what fraction of it turns into electricity. The rest turns into heat or is reflected, so the electric power is the $\eta$ fraction of the input power.
**Formula:** $P = \eta P_\text{in} = \eta I A$
**Conversions:** The units go along with the numbers: $\tfrac{\text{kW}}{\text{m}^2} \cdot \text{m}^2 = \text{kW}$, so the result comes directly in kilowatts and no conversions are needed.
**Substitution:** $P = 0.210 \cdot 1.00\,\tfrac{\text{kW}}{\text{m}^2} \cdot 20.0\,\text{m}^2 = 0.210 \cdot 20.0\,\text{kW} = 4.20\,\text{kW}$
**Answer:** $4.20\,\text{kW}$, three significant figures, because the area $20.0\,\text{m}^2$, the radiation power $1.00\,\tfrac{\text{kW}}{\text{m}^2}$ and the efficiency $0.210$ all have three figures.
**Reasonableness:** Radiation of $20.0\,\text{kW}$ hits the panel, and about a fifth of it ($0.210 \approx 0.2$) is $\approx 4\,\text{kW}$. The rest, $20.0\,\text{kW} - 4.20\,\text{kW} = 15.8\,\text{kW}$, heats the panel or is reflected away. On the roof of a detached house 4 kW is a usual peak power in clear weather.

## fy3-15-L1-04
**Given:** fuel power $P_0 = 800\,\text{MW}$ and electric power $P_\text{s} = 320\,\text{MW}$
**Find:** the power $P_\text{h}$ transferred from the power plant to the surroundings as heat, in megawatts
**Principle:** Energy is conserved and the plant runs steadily, so the power going in equals the power going out. Only electricity and heat go out, so the part of the fuel power that does not turn into electricity is transferred to the surroundings as heat.
**Formula:** $P_0 = P_\text{s} + P_\text{h}$, so $P_\text{h} = P_0 - P_\text{s}$
**Conversions:** Both powers are already in megawatts, so no conversions are needed.
**Substitution:** $P_\text{h} = 800\,\text{MW} - 320\,\text{MW} = 480\,\text{MW}$
**Answer:** $480\,\text{MW}$, three significant figures, because both powers, $800\,\text{MW}$ and $320\,\text{MW}$, are given to the nearest megawatt and the difference keeps the same precision.
**Reasonableness:** The efficiency is $\dfrac{320\,\text{MW}}{800\,\text{MW}} = 0.40$, which is usual for a condensing power plant. The balance works out: $320\,\text{MW} + 480\,\text{MW} = 800\,\text{MW}$. In addition to the 40% that turns into electricity, the other 60% is transferred to the surroundings as heat, most of it through the condenser to the sea.

## fy3-15-L1-05
**Given:** fuel power $P_0 = 250\,\text{MW}$, electric power $P_\text{s} = 75.0\,\text{MW}$ and district heating power $P_\text{k} = 150\,\text{MW}$
**Find:** the overall efficiency $\eta_\text{tot}$ as a percentage
**Principle:** In a combined heat and power plant both electricity and district heating are useful, so both are counted in the useful power. Only the rest is wasted, and the overall efficiency is the share of the useful power in the fuel power.
**Formula:** $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Conversions:** All powers are in megawatts and the units cancel. The result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta_\text{tot} = \dfrac{75.0\,\text{MW} + 150\,\text{MW}}{250\,\text{MW}} = \dfrac{225\,\text{MW}}{250\,\text{MW}} = 0.900 = 90.0\,\%$
**Answer:** $90.0\,\%$, three significant figures, because all powers are given to the nearest megawatt and the sum $75.0 + 150 = 225\,\text{MW}$ keeps the same precision; so the quotient $225/250$ has three figures.
**Reasonableness:** The result is in the usual range of 85–90% for combined production. The power of waste heat is $250\,\text{MW} - 225\,\text{MW} = 25\,\text{MW}$, and $225 + 25 = 250$, so the balance works out. The share of electricity is only $\dfrac{75.0\,\text{MW}}{250\,\text{MW}} = 30\,\%$, so the electrical efficiency is lower than in a condensing power plant.

## fy3-15-L2-01
**Given:** fuel power $P_0 = 300\,\text{MW}$, efficiency of the boiler $\eta_1 = 0.880$, of the steam cycle $\eta_2 = 0.420$ and of the generator $\eta_3 = 0.980$
**Find:** the electric power $P_3$ of the plant in megawatts
**Principle:** The steps are in series, and the output power of each is the input power of the next. Each step keeps only the $\eta$ fraction of its power, so the electric power is the fuel power multiplied by all three efficiencies.
**Formula:** $P_1 = \eta_1 P_0$, $P_2 = \eta_2 P_1$ and $P_3 = \eta_3 P_2$, so $P_3 = \eta_1 \eta_2 \eta_3 P_0$
**Conversions:** The efficiencies are dimensionless and the power is already in megawatts, so no conversions are needed.
**Substitution:** $P_3 = 0.880 \cdot 0.420 \cdot 0.980 \cdot 300\,\text{MW} = 0.362208 \cdot 300\,\text{MW} = 108.6624\,\text{MW}$
**Answer:** $109\,\text{MW}$, three significant figures, because the efficiencies $0.880$, $0.420$ and $0.980$ have three figures and the fuel power $300\,\text{MW}$ is given to the nearest megawatt.
**Reasonableness:** Estimate: $0.9 \cdot 0.4 \cdot 1.0 \cdot 300\,\text{MW} \approx 110\,\text{MW}$. The efficiency of the whole chain is $0.362$ or 36%, less than the weakest step ($0.420$) would give alone. The losses of the boiler and the steam cycle together take $1 - 0.880 \cdot 0.420 = 0.630$, that is almost two thirds (about 63%) of the energy of the fuel.

## fy3-15-L2-02
**Given:** efficiency of the whole chain $\eta = 0.380$, of the boiler $\eta_1 = 0.900$ and of the generator $\eta_3 = 0.980$
**Find:** the efficiency $\eta_2$ of the steam cycle as a percentage
**Principle:** The chain is the product of three steps in series, so the efficiency of the whole chain is the product of the efficiencies of the steps. When two steps and the whole are known, the missing step is found by division.
**Formula:** $\eta = \eta_1 \eta_2 \eta_3$, so $\eta_2 = \dfrac{\eta}{\eta_1 \eta_3}$
**Conversions:** The efficiencies are dimensionless numbers, so no unit conversions are needed. At the end the result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta_2 = \dfrac{0.380}{0.900 \cdot 0.980} = \dfrac{0.380}{0.882} = 0.43084 = 43.08\,\%$
**Answer:** $43.1\,\%$, three significant figures, because all three efficiencies, $0.380$, $0.900$ and $0.980$, have three figures.
**Reasonableness:** Check: $0.900 \cdot 0.4308 \cdot 0.980 = 0.380$. The efficiency of the steam cycle is greater than that of the whole chain, $0.380$, as it should be, because the other steps only reduce it. It is also close to the usual 40–45% of a condensing power plant, and it is the weakest link of the chain.

## fy3-15-L2-03
**Given:** electric power $P_\text{s} = 150\,\text{MW}$, efficiency $\eta = 0.360$, heat of combustion $H = 9.00\,\tfrac{\text{MJ}}{\text{kg}}$, time $t = 1\,\text{h}$
**Find:** the mass $m$ of wood chips burned in an hour, in tonnes
**Principle:** Energy is conserved: the chemical energy of the fuel is either electricity or waste heat. The efficiency connects the electric power to the fuel power, and the fuel power is the heat of combustion times the mass flow, because the heat of combustion tells the energy per unit mass.
**Formula:** $P_0 = \dfrac{P_\text{s}}{\eta}$ and $P_0 = \dfrac{H m}{t}$, so $m = \dfrac{P_\text{s}\, t}{\eta H}$
**Conversions:** $150\,\text{MW} = 150 \cdot 10^6\,\text{W}$, $9.00\,\tfrac{\text{MJ}}{\text{kg}} = 9.00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}$ and $1\,\text{h} = 3600\,\text{s}$. At the end $1\,\text{t} = 1000\,\text{kg}$.
**Substitution:** $m = \dfrac{150 \cdot 10^6\,\text{W} \cdot 3600\,\text{s}}{0.360 \cdot 9.00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 1.66667 \cdot 10^5\,\text{kg} = 166.67\,\text{t}$
**Answer:** $167\,\text{t}$, three significant figures, because the efficiency $0.360$ and the heat of combustion $9.00\,\tfrac{\text{MJ}}{\text{kg}}$ have three figures and the electric power $150\,\text{MW}$ is given to the nearest megawatt; the hour is exact ($3600\,\text{s}$) and does not limit the precision.
**Reasonableness:** The fuel power is $\dfrac{150\,\text{MW}}{0.360} = 417\,\text{MW}$, and the mass flow $\dfrac{417 \cdot 10^6\,\text{W}}{9.00 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 46\,\tfrac{\text{kg}}{\text{s}}$. In a day that is $46 \cdot 86\,400\,\text{kg} \approx 4000\,\text{t}$, which requires continuous lorry or train transport and suits a large bio power plant.

## fy3-15-L2-04
**Given:** heat power transferred to the condenser $P_\text{L} = 270\,\text{MW}$, rise in the temperature of the water $\Delta T = 9.00\,\text{K}$ and the given specific heat capacity $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$
**Find:** the water flow $q_m = m/t$ through the condenser in tonnes per second
**Principle:** The heat released by the condenser is transferred entirely to the cooling water when there are no other losses. The water only warms up and does not vaporise, so $Q = c m \Delta T$ applies to the quantity of heat; dividing by time gives the power.
**Formula:** $P_\text{L} = \dfrac{Q}{t} = c\, q_m \Delta T$, so $q_m = \dfrac{P_\text{L}}{c\, \Delta T}$
**Conversions:** $270\,\text{MW} = 270 \cdot 10^6\,\text{W}$ and $1\,\text{W} = 1\,\tfrac{\text{J}}{\text{s}}$. The change in temperature $9.00\,\text{K}$ is the same in kelvins and in degrees Celsius. At the end $1\,\text{t} = 1000\,\text{kg}$.
**Substitution:** $q_m = \dfrac{270 \cdot 10^6\,\text{W}}{4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 9.00\,\text{K}} = 7159.9\,\tfrac{\text{kg}}{\text{s}} = 7.1599\,\tfrac{\text{t}}{\text{s}}$
**Answer:** $7.16\,\tfrac{\text{t}}{\text{s}}$, three significant figures, because the change in temperature $9.00\,\text{K}$ and the specific heat capacity $4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ have three figures and the power $270\,\text{MW}$ is given to the nearest megawatt.
**Reasonableness:** Check: $4190 \cdot 7160 \cdot 9.00\,\text{W} = 2.70 \cdot 10^8\,\text{W}$. The water flow corresponds to about $7\,\tfrac{\text{m}^3}{\text{s}}$, which is the discharge of a small river. A condensing power plant needs a large amount of cooling water on the shore, and that is why they are built on the coast or by a river.

## fy3-15-L3-01
**Given:** $P_0 = 600\,\text{MW}$. Electricity only: $P_\text{s,0} = 240\,\text{MW}$. Full combined production: $P_\text{s,full} = 180\,\text{MW}$ and $P_\text{k,full} = 348\,\text{MW}$. Now the district heating power is $P_\text{k} = 200\,\text{MW}$.
**Find:** the electric power $P_\text{s}$ in megawatts and the overall efficiency $\eta_\text{tot}$
**Principle:** According to the problem the electric power decreases linearly as the district heating power increases, so the two extreme modes define a straight line. District heating is taken in an intermediate mode, so the electric power is read from that line. The overall efficiency is the combined power of electricity and district heating divided by the fuel power.
**Formula:** $P_\text{s} = P_\text{s,0} - k P_\text{k}$, where $k = \dfrac{P_\text{s,0} - P_\text{s,full}}{P_\text{k,full}}$, and $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Conversions:** All powers are in megawatts and $k$ is a dimensionless number, so no conversions are needed.
**Substitution:** $k = \dfrac{240\,\text{MW} - 180\,\text{MW}}{348\,\text{MW}} = 0.17241$ and $P_\text{s} = 240\,\text{MW} - 0.17241 \cdot 200\,\text{MW} = 205.517\,\text{MW}$. Then $\eta_\text{tot} = \dfrac{205.517\,\text{MW} + 200\,\text{MW}}{600\,\text{MW}} = 0.67586 = 67.6\,\%$.
**Answer:** $P_\text{s} = 206\,\text{MW}$ and $\eta_\text{tot} = 67.6\,\%$, three significant figures, that is megawatt precision, because all powers are given to the nearest megawatt: the difference $240 - 180 = 60\,\text{MW}$ has that precision, and the subtracted $0.172 \cdot 200 \approx 34\,\text{MW}$ is to the nearest unit.
**Reasonableness:** The results are between the extreme modes: the electric power between $180$ and $240\,\text{MW}$ and the efficiency between $40\,\%$ and $88\,\%$. Limiting case: when $P_\text{k} = 348\,\text{MW}$, the formula gives $240 - 60 = 180\,\text{MW}$. For every megawatt of district heating $\tfrac{60}{348} = 0.17\,\text{MW}$ of electricity is lost. The combined efficiency does not tell which is more worthwhile, because electricity is good for anything but district heating only for heating; profitability depends on need and prices.

## fy3-15-L3-02
**Given:** electrical energy $E = 36.0\,\text{GWh}$, efficiency $\eta = 0.380$ and heat of combustion of coal $H = 25.0\,\tfrac{\text{MJ}}{\text{kg}}$; given $1\,\text{GWh} = 3.60 \cdot 10^{12}\,\text{J}$
**Find:** the mass $m$ of coal burned in a year, in kilotonnes
**Principle:** Energy is conserved: the chemical energy $Q_1$ of the coal turns into electricity with efficiency $\eta$ and the rest into waste heat. The denominator of the efficiency is the bought fuel, and the energy of the fuel is the heat of combustion times the mass.
**Formula:** $E = \eta Q_1$ and $Q_1 = H m$, so $m = \dfrac{E}{\eta H}$
**Conversions:** $E = 36.0 \cdot 3.60 \cdot 10^{12}\,\text{J} = 1.296 \cdot 10^{14}\,\text{J}$ and $H = 25.0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}$. At the end $1\,\text{kt} = 10^6\,\text{kg}$.
**Substitution:** $m = \dfrac{1.296 \cdot 10^{14}\,\text{J}}{0.380 \cdot 25.0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 1.3642 \cdot 10^7\,\text{kg} = 13.642\,\text{kt}$
**Answer:** $13.6\,\text{kt}$, three significant figures, because the electrical energy $36.0\,\text{GWh}$, the efficiency $0.380$, the heat of combustion $25.0\,\tfrac{\text{MJ}}{\text{kg}}$ and the conversion factor $3.60 \cdot 10^{12}\,\text{J}/\text{GWh}$ all have three figures.
**Reasonableness:** Estimate: $\tfrac{1.3 \cdot 10^{14}\,\text{J}}{0.4 \cdot 2.5 \cdot 10^7\,\tfrac{\text{J}}{\text{kg}}} \approx 1.3 \cdot 10^7\,\text{kg}$. The amount corresponds to about 270 wagonloads of coal, when a wagon holds 50 t. The efficiencies cannot be compared directly: in a coal power plant the denominator is bought fuel, which turns into waste heat and emissions, but the energy of the wind is not a store that gets used up. The efficiency of a wind farm only tells what fraction of the kinetic energy of the air flowing through the rotors is turned into electricity.

## fy3-15-L3-03
**Given:** heating need $Q = 100\,\text{kWh}$, coefficient of performance $\varepsilon = 3.00$, efficiency of the power plant $\eta_\text{plant} = 0.400$ and share left after transmission $\eta_\text{transm} = 0.950$
**Find:** the energy of the fuel $E_\text{fuel}$ at the power plant in kilowatt-hours
**Principle:** A heat pump moves heat from outside to inside and uses electricity for it, so the coefficient of performance tells the ratio of heat to electricity. The electricity is produced from fuel in a chain where each step lets through only part of the energy, so the fuel is found by dividing the electricity by the efficiency of the chain.
**Formula:** $\varepsilon = \dfrac{Q}{E_\text{s}}$, so $E_\text{s} = \dfrac{Q}{\varepsilon}$, and $E_\text{fuel} = \dfrac{E_\text{s}}{\eta_\text{transm}\, \eta_\text{plant}}$, thus $E_\text{fuel} = \dfrac{Q}{\eta_\text{transm}\, \eta_\text{plant}\, \varepsilon}$
**Conversions:** All energies are in kilowatt-hours and the factors are dimensionless, so no conversions are needed.
**Substitution:** $E_\text{fuel} = \dfrac{100\,\text{kWh}}{0.950 \cdot 0.400 \cdot 3.00} = \dfrac{100\,\text{kWh}}{1.14} = 87.719\,\text{kWh}$
**Answer:** $87.7\,\text{kWh}$, three significant figures, because the factors $0.950$, $0.400$ and $3.00$ have three figures and the heating need $100\,\text{kWh}$ is given to the nearest kilowatt-hour.
**Reasonableness:** Direct electric heating would need $\dfrac{100\,\text{kWh}}{0.380} = 263\,\text{kWh}$ of fuel and an oil boiler $\dfrac{100\,\text{kWh}}{0.900} = 111\,\text{kWh}$. The heat pump saves the most fuel, because it moves heat from the outside air into the house instead of turning electricity into heat. Direct electric heating is the worst, because over 60% of the energy of the fuel has already been wasted in producing the electricity.
