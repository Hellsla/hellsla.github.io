## fy3-15-L1-01
**Given:** efficiency of the turbine $\eta_1 = 92.0\,\% = 0.920$, efficiency of the generator $\eta_2 = 98.0\,\% = 0.980$
**Find:** the efficiency $\eta$ of the whole plant as a percentage
**Principle:** The plant is a chain in which the output power of the turbine is the input power of the generator. Each step lets through only part of the energy coming into it, so the efficiency of the chain is the product of the efficiencies of the steps.
**Formula:** $P_1 = \eta_1 P_0$ and $P_2 = \eta_2 P_1$, so $\eta = \dfrac{P_2}{P_0} = \eta_1 \eta_2$
**Conversions:** The efficiencies are fractions of a whole: $92.0\,\% = 0.920$ and $98.0\,\% = 0.980$. At the end the result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta = 0.920 \cdot 0.980 = 0.9016 = 90.16\,\%$
**Answer:** $90.2\,\%$, three significant figures like the given efficiencies $92.0\,\%$ and $98.0\,\%$.
**Reasonableness:** The product is smaller than either efficiency, as it should be when the factors are less than 1. Estimate: $0.92 \cdot 0.98 \approx 0.92 - 0.02 \cdot 0.92 \approx 0.90$. A hydropower plant is not a heat engine, so its efficiency can be over $90\,\%$.

## fy3-15-L1-02
**Given:** power of the kinetic energy of the air flow $P_\text{wind} = 2.50\,\text{MW}$ and electric power $P_\text{elec} = 1.05\,\text{MW}$
**Find:** the efficiency $\eta$ of the turbine as a percentage
**Principle:** Efficiency is the share of the useful power in the power coming into the plant. Here the input power is the power of the kinetic energy of the air flowing through the rotor and the useful power is the power going to the electricity grid; the rest of the energy stays in the motion of the air or turns into heat.
**Formula:** $\eta = \dfrac{P_\text{elec}}{P_\text{wind}}$
**Conversions:** Both powers are in megawatts, so the units cancel. The result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta = \dfrac{1.05\,\text{MW}}{2.50\,\text{MW}} = 0.420 = 42.0\,\%$
**Answer:** $42.0\,\%$, three significant figures like the powers $2.50\,\text{MW}$ and $1.05\,\text{MW}$.
**Reasonableness:** Estimate: $1 / 2.5 = 0.4$, which matches the result. The efficiency of a modern wind turbine is at best about 40–$45\,\%$. You cannot take all the energy from the wind, because the air has to keep moving after the rotor too. Part of the energy taken by the rotor turns into internal energy in friction and electrical losses, and this is transferred to the surroundings as heat.

## fy3-15-L1-03
**Given:** area $A = 20.0\,\text{m}^2$, radiation power per unit area $I = 1.00\,\tfrac{\text{kW}}{\text{m}^2}$, efficiency $\eta = 0.210$
**Find:** the electric power $P$ of the panel in kilowatts
**Principle:** The power of the radiation hitting the panel is the intensity times the area, and the efficiency tells what fraction of it turns into electricity. The rest turns into heat or is reflected, so the electric power is the $\eta$ fraction of the input power.
**Formula:** $P = \eta P_\text{in} = \eta I A$
**Conversions:** The units go along with the numbers: $\tfrac{\text{kW}}{\text{m}^2} \cdot \text{m}^2 = \text{kW}$, so the result comes directly in kilowatts and no conversions are needed.
**Substitution:** $P = 0.210 \cdot 1.00\,\tfrac{\text{kW}}{\text{m}^2} \cdot 20.0\,\text{m}^2 = 0.210 \cdot 20.0\,\text{kW} = 4.20\,\text{kW}$
**Answer:** $4.20\,\text{kW}$, three significant figures, because the area $20.0\,\text{m}^2$, the radiation power $1.00\,\tfrac{\text{kW}}{\text{m}^2}$ and the efficiency $0.210$ all have three figures.
**Reasonableness:** Radiation of $20.0\,\text{kW}$ hits the panel, and about a fifth of it ($0.210 \approx 0.2$) is $\approx 4\,\text{kW}$. The rest, $20.0\,\text{kW} - 4.20\,\text{kW} = 15.8\,\text{kW}$, heats the panel or is reflected away. On the roof of a detached house $4\,\text{kW}$ is a usual peak power in clear weather.

## fy3-15-L1-04
**Given:** read from the bars of the figure: $P_0 = 400\,\text{MW}$, $P_1 = 350\,\text{MW}$, $P_2 = 150\,\text{MW}$ and $P_3 = 140\,\text{MW}$
**Find:** the step in which the power decreases the most, and the power transferred to the surroundings as heat in that step
**Principle:** The power plant runs steadily and energy is conserved, so when the power decreases in a step, the difference is transferred to the surroundings as heat. The power coming out of a step is smaller than the power going in, and the difference is the waste heat produced in it.
**Reading the graph:** The tops of the bars $P_0$, $P_1$ and $P_2$ are on the gridlines, and they give the powers $400$, $350$ and $150\,\text{MW}$. The electric power $P_3$ is a little below the line $150\,\text{MW}$, about $140\,\text{MW}$; it is not needed for the answer. The decrease of power step by step is $P_0 - P_1 = 50\,\text{MW}$ in the boiler, $P_1 - P_2 = 200\,\text{MW}$ in the steam cycle and $P_2 - P_3 = 10\,\text{MW}$ in the generator and transformer. The biggest drop is between the bars $P_1$ and $P_2$, that is in the steam cycle.
**Formula:** $P_\text{h} = P_\text{in} - P_\text{out}$, here $P_\text{h} = P_1 - P_2$
**Conversions:** Not needed: all powers are in megawatts.
**Substitution:** $P_\text{h} = 350\,\text{MW} - 150\,\text{MW} = 200\,\text{MW}$
**Answer:** The power decreases the most in the steam cycle, where $200\,\text{MW}$ is transferred to the surroundings as heat. The values are read from the gridlines as whole megawatts, so the result to three significant figures is $200\,\text{MW}$.
**Reasonableness:** The losses of the steps add up to $50 + 200 + 10 = 260\,\text{MW} = P_0 - P_3 = 400\,\text{MW} - 140\,\text{MW}$, so the balance works out. The efficiency of the steam cycle is $150 / 350 \approx 0.43$, which suits a steam cycle, and its loss is over $75\,\%$ of the waste heat of the whole plant.

## fy3-15-L1-05
**Given:** fuel power $P_0 = 250\,\text{MW}$, electric power $P_\text{s} = 75.0\,\text{MW}$ and district heating power $P_\text{k} = 150\,\text{MW}$
**Find:** the overall efficiency $\eta_\text{tot}$ as a percentage
**Principle:** In a combined heat and power plant both electricity and district heating are useful, so both are counted in the useful power. Only the rest is wasted, and the overall efficiency is the share of the useful power in the fuel power.
**Formula:** $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Conversions:** All powers are in megawatts and the units cancel. The result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta_\text{tot} = \dfrac{75.0\,\text{MW} + 150\,\text{MW}}{250\,\text{MW}} = \dfrac{225\,\text{MW}}{250\,\text{MW}} = 0.900 = 90.0\,\%$
**Answer:** $90.0\,\%$, three significant figures, because all powers are given to the nearest megawatt and the sum $75.0 + 150 = 225\,\text{MW}$ keeps the same precision; so the quotient $225/250$ has three figures.
**Reasonableness:** The result is in the usual range of 85–$90\,\%$ for combined production. The power of waste heat is $250\,\text{MW} - 225\,\text{MW} = 25\,\text{MW}$, and $225 + 25 = 250$, so the balance works out. The share of electricity is only $\dfrac{75.0\,\text{MW}}{250\,\text{MW}} = 30\,\%$, so the electrical efficiency is lower than in a condensing power plant.

## fy3-15-L1-06
**Find:** why the overall efficiency of a combined heat and power plant is higher than that of a condensing power plant when the fuel is the same
**Principle:** Efficiency tells what share of the energy of the fuel is put to use. The energy released from the fuel is the same in both, so the difference comes from what is counted as useful: in a condensing power plant only electricity, in combined production electricity and district heating, $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$.
**Model answer:** In combined production the heat of the condenser is led into the district heating network instead of the sea, so a larger share of the energy of the fuel is put to use. No more energy is released from the fuel, because the heat of combustion is the same. The turbine does not convert a larger share of the heat into electricity either: usually less electricity is obtained than in a condensing power plant. The district heating network does not produce extra energy, since the electricity and heat together do not exceed the fuel power. Waste heat is still produced, but less of it.

## fy3-15-L1-07
**Given:** thermal power of the reactor $P_0 = 1500\,\text{MW}$ and electric power $P_\text{s} = 510\,\text{MW}$
**Find:** the efficiency $\eta$ of the electricity production as a percentage
**Principle:** Efficiency is the share of the useful power in the power supplied to the plant. The useful power here is only electricity, and the rest of the heat of the reactor is transferred to the surroundings as waste heat.
**Formula:** $\eta = \dfrac{P_\text{s}}{P_0}$
**Conversions:** Both powers are in megawatts, so the units cancel. The result is multiplied by one hundred to get a percentage.
**Substitution:** $\eta = \dfrac{510\,\text{MW}}{1500\,\text{MW}} = 0.340 = 34.0\,\%$
**Answer:** $34.0\,\%$, three significant figures like the electric power $510\,\text{MW}$.
**Reasonableness:** Estimate: $1500 : 3 = 500$, and $510\,\text{MW}$ is slightly more, so the efficiency is slightly over a third. The waste heat is $1500\,\text{MW} - 510\,\text{MW} = 990\,\text{MW}$, about two thirds. The electrical efficiency of a thermal power plant is typically 30–$40\,\%$, and the result is in that range.

## fy3-15-L1-08
**Given:** fuel power $P_0 = 500\,\text{MW}$ and running time $t = 1\,\text{day} = 24\,\text{h}$
**Find:** the energy of the fuel $E$ in gigawatt-hours
**Principle:** Power is energy per unit of time. When the power is constant, the energy is the power times the time.
**Formula:** $P = \dfrac{E}{t}$, so $E = P_0\,t$
**Conversions:** $1\,\text{day} = 24\,\text{h}$. The power is converted into gigawatts: $500\,\text{MW} = 0.500\,\text{GW}$. Then the result comes directly in gigawatt-hours.
**Substitution:** $E = 0.500\,\text{GW} \cdot 24\,\text{h} = 12.0\,\text{GWh}$
**Answer:** $12.0\,\text{GWh}$, three significant figures. The power $500\,\text{MW}$ is given with three figures, and a day is exactly $24\,\text{h}$.
**Reasonableness:** Estimate: $500\,\text{MW} \cdot 24\,\text{h} \approx 500 \cdot 24\,\text{MWh} = 12\,000\,\text{MWh}$, which is $12\,\text{GWh}$. One hour would give $0.5\,\text{GWh}$, and a day has 24 hours, so the number is of the right order of magnitude. The same energy is $12.0 \cdot 3.6 \cdot 10^{12}\,\text{J} \approx 4.3 \cdot 10^{13}\,\text{J}$.

## fy3-15-L2-01
**Given:** fuel power $P_0 = 300\,\text{MW}$, efficiency of the boiler $\eta_1 = 0.880$, of the steam cycle $\eta_2 = 0.420$ and of the generator $\eta_3 = 0.980$
**Find:** the electric power $P_3$ of the plant in megawatts
**Principle:** The steps are in series, and the output power of each is the input power of the next. Each step keeps only the $\eta$ fraction of its power, so the electric power is the fuel power multiplied by all three efficiencies.
**Formula:** $P_1 = \eta_1 P_0$, $P_2 = \eta_2 P_1$ and $P_3 = \eta_3 P_2$, so $P_3 = \eta_1 \eta_2 \eta_3 P_0$
**Conversions:** The efficiencies are dimensionless and the power is already in megawatts, so no conversions are needed.
**Substitution:** $P_3 = 0.880 \cdot 0.420 \cdot 0.980 \cdot 300\,\text{MW} = 0.362208 \cdot 300\,\text{MW} = 108.6624\,\text{MW}$
**Answer:** $109\,\text{MW}$, three significant figures, because the efficiencies $0.880$, $0.420$ and $0.980$ have three figures and the fuel power $300\,\text{MW}$ is given to the nearest megawatt.
**Reasonableness:** Estimate: $0.9 \cdot 0.4 \cdot 1.0 \cdot 300\,\text{MW} \approx 110\,\text{MW}$. The efficiency of the whole chain is $0.362$ or $36\,\%$, less than the weakest step ($0.420$) would give alone. The losses of the boiler and the steam cycle together take $1 - 0.880 \cdot 0.420 = 0.630$, that is almost two thirds (about $63\,\%$) of the energy of the fuel.

## fy3-15-L2-02
**Given:** efficiency of the whole chain $\eta = 0.380$, of the boiler $\eta_1 = 0.900$ and of the generator $\eta_3 = 0.980$
**Find:** the efficiency $\eta_2$ of the steam cycle as a percentage
**Principle:** The chain is the product of three steps in series, so the efficiency of the whole chain is the product of the efficiencies of the steps. When two steps and the whole are known, the missing step is found by division.
**Formula:** $\eta = \eta_1 \eta_2 \eta_3$, so $\eta_2 = \dfrac{\eta}{\eta_1 \eta_3}$
**Conversions:** The efficiencies are dimensionless numbers, so no unit conversions are needed. At the end the result is multiplied by a hundred to give a percentage.
**Substitution:** $\eta_2 = \dfrac{0.380}{0.900 \cdot 0.980} = \dfrac{0.380}{0.882} = 0.43084 = 43.08\,\%$
**Answer:** $43.1\,\%$, three significant figures, because all three efficiencies, $0.380$, $0.900$ and $0.980$, have three figures.
**Reasonableness:** Check: $0.900 \cdot 0.4308 \cdot 0.980 = 0.380$. The efficiency of the steam cycle is greater than that of the whole chain, $0.380$, as it should be, because the other steps only reduce it. It is a little greater than the usual efficiency of a whole condensing power plant (about $40\,\%$, typically $38$–$42\,\%$), because the losses of the boiler and the generator are not included in it, and it is the weakest link of the chain.

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

## fy3-15-L2-05
**Given:** from the table, in 2023 the energy of the fuel $E_0 = 2450\,\text{GWh}$, electricity $E_\text{s} = 735\,\text{GWh}$ and district heating $E_\text{k} = 1470\,\text{GWh}$; the values for 2021 and 2022 are in the table
**Find:** the overall efficiency $\eta_\text{tot}$ of 2023 as a percentage
**Principle:** In a combined heat and power plant both electricity and district heating are put to use, so both are counted in the overall efficiency. The ratio is the same for energies as for powers, because the plant runs for the same time.
**Formula:** $\eta_\text{s} = \dfrac{E_\text{s}}{E_0}$ and $\eta_\text{tot} = \dfrac{E_\text{s} + E_\text{k}}{E_0}$
**Conversions:** All energies are in gigawatt-hours, so the units cancel and no conversions are needed. The results are multiplied by one hundred to get percentages.
**Substitution:** In 2023 the sum of electricity and district heating is $735\,\text{GWh} + 1470\,\text{GWh} = 2205\,\text{GWh}$, so $\eta_\text{tot} = \dfrac{2205\,\text{GWh}}{2450\,\text{GWh}} = 0.900 = 90.0\,\%$. The electrical efficiencies are $\eta_\text{s} = \tfrac{840}{2400} = 35.0\,\%$ (2021), $\tfrac{800}{2500} = 32.0\,\%$ (2022) and $\tfrac{735}{2450} = 30.0\,\%$ (2023). The overall efficiencies are $\tfrac{2030}{2400} = 84.6\,\%$ (2021) and $\tfrac{2210}{2500} = 88.4\,\%$ (2022).
**Answer:** $90.0\,\%$, three significant figures like the energies in the table.
**Reasonableness:** The overall efficiency is at most $100\,\%$ and greater than the electrical efficiency, as it should be. In 2023 the waste heat is $2450\,\text{GWh} - 2205\,\text{GWh} = 245\,\text{GWh}$, about a tenth. In a cold year more district heating is needed, so a larger share of the heat of the condenser is put to use and less electricity is obtained: the electrical efficiency decreased from $35.0\,\%$ to $30.0\,\%$, but the overall efficiency increased from $84.6\,\%$ to $90.0\,\%$. Electricity and heat are still not equally valuable, even though they are added together.

## fy3-15-L2-06
**Given:** from the table, the nuclear power plant $P_0 = 2400\,\text{MW}$ and $P_\text{s} = 840\,\text{MW}$, the coal power plant $1200\,\text{MW}$ and $432\,\text{MW}$, the bio power plant $350\,\text{MW}$ and $112\,\text{MW}$
**Find:** the largest waste heat power $P_\text{h}$ in megawatts
**Principle:** In a condensing power plant only electricity is put to use, and energy is conserved, so the fuel or reactor power is either electricity or waste heat: $P_0 = P_\text{s} + P_\text{h}$. Efficiency is a ratio, but the waste heat power also depends on the size of the plant.
**Formula:** $\eta = \dfrac{P_\text{s}}{P_0}$ and $P_\text{h} = P_0 - P_\text{s}$
**Conversions:** All powers are in megawatts, so no conversions are needed.
**Substitution:** Nuclear power plant: $\eta = \tfrac{840\,\text{MW}}{2400\,\text{MW}} = 0.350$ and $P_\text{h} = 2400\,\text{MW} - 840\,\text{MW} = 1560\,\text{MW}$. Coal power plant: $\eta = \tfrac{432}{1200} = 0.360$ and $P_\text{h} = 1200\,\text{MW} - 432\,\text{MW} = 768\,\text{MW}$. Bio power plant: $\eta = \tfrac{112}{350} = 0.320$ and $P_\text{h} = 350\,\text{MW} - 112\,\text{MW} = 238\,\text{MW}$.
**Answer:** $1560\,\text{MW}$ (nuclear power plant), three significant figures like the electric powers.
**Reasonableness:** For each plant $P_\text{s} + P_\text{h}$ equals $P_0$: for example $840 + 1560 = 2400$. The lowest efficiency belongs to the bio power plant ($32.0\,\%$), but it has the smallest waste heat power ($238\,\text{MW}$), because it is small. The largest waste heat power belongs to the nuclear power plant, even though its efficiency ($35.0\,\%$) is almost as high as that of the coal power plant ($36.0\,\%$). So efficiency and waste heat power do not come in the same order.

## fy3-15-L2-07
**Given:** $\eta_1 = 0.920$ (boiler), $\eta_2 = 0.410$ (steam cycle) and $\eta_3 = 0.970$ (generator); the student's result $230\,\%$
**Find:** the correct efficiency $\eta$ of the plant as a percentage and an explanation of the error
**Principle:** The steps are in a row, and each step lets through only its efficiency's share of the power coming into it. When $P_1 = \eta_1 P_0$, $P_2 = \eta_2 P_1$ and $P_3 = \eta_3 P_2$, the efficiency of the chain is $\eta = \dfrac{P_3}{P_0} = \eta_1\,\eta_2\,\eta_3$, that is the efficiencies are multiplied.
**Formula:** $\eta = \eta_1\,\eta_2\,\eta_3$
**Conversions:** The efficiencies are dimensionless numbers, so no conversions are needed. At the end the result is multiplied by one hundred to get a percentage.
**Substitution:** $\eta = 0.920 \cdot 0.410 \cdot 0.970 = 0.3659 = 36.6\,\%$
**Answer:** $36.6\,\%$, three significant figures like the given efficiencies.
**Reasonableness:** The student's error: a sum of efficiencies of $230\,\%$ would be over $100\,\%$, which is impossible, because a plant cannot produce more electricity than there is energy in the fuel. Each step reduces the power that is left, so the efficiencies are multiplied, not added. The product $0.366$ is smaller than the weakest step $0.410$, as it should be when all the factors are below 1. Estimate: $0.9 \cdot 0.4 \cdot 1.0 = 0.36$. The waste heat is $100\,\% - 36.6\,\% = 63.4\,\%$ of the fuel power.

## fy3-15-L3-01
**Given:** $P_0 = 600\,\text{MW}$. Electricity only: $P_\text{s,0} = 240\,\text{MW}$. Full combined production: $P_\text{s,full} = 180\,\text{MW}$ and $P_\text{k,full} = 348\,\text{MW}$. Now the district heating power is $P_\text{k} = 200\,\text{MW}$.
**Find:** the electric power $P_\text{s}$ in megawatts and the overall efficiency $\eta_\text{tot}$
**Principle:** According to the problem the electric power decreases linearly as the district heating power increases, so the two extreme modes define a straight line. District heating is taken in an intermediate mode, so the electric power is read from that line. The overall efficiency is the combined power of electricity and district heating divided by the fuel power.
**Formula:** $P_\text{s} = P_\text{s,0} - k P_\text{k}$, where $k = \dfrac{P_\text{s,0} - P_\text{s,full}}{P_\text{k,full}}$, and $\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{k}}{P_0}$
**Conversions:** All powers are in megawatts and $k$ is a dimensionless number, so no conversions are needed.
**Substitution:** $k = \dfrac{240\,\text{MW} - 180\,\text{MW}}{348\,\text{MW}} = 0.17241$ and $P_\text{s} = 240\,\text{MW} - 0.17241 \cdot 200\,\text{MW} = 205.517\,\text{MW}$. Then $\eta_\text{tot} = \dfrac{205.517\,\text{MW} + 200\,\text{MW}}{600\,\text{MW}} = 0.67586 = 67.6\,\%$.
**Answer:** $P_\text{s} = 206\,\text{MW}$ and $\eta_\text{tot} = 67.6\,\%$, three significant figures, that is megawatt precision, because all powers are given to the nearest megawatt: the difference $240 - 180 = 60\,\text{MW}$ has that precision, and the subtracted $0.172 \cdot 200 \approx 34\,\text{MW}$ is to the nearest unit.
**Reasonableness:** The results are between the extreme modes: the electric power between $180$ and $240\,\text{MW}$ and the efficiency between $40\,\%$ and $88\,\%$. Limiting case: when $P_\text{k} = 348\,\text{MW}$, the formula gives $240 - 60 = 180\,\text{MW}$. For every megawatt of district heating $\tfrac{60}{348} = 0.17\,\text{MW}$ of electricity is lost. The combined efficiency does not tell which is more worthwhile, because electricity can be used for anything, but district heat only for heating; profitability depends on need and prices.

## fy3-15-L3-02
**Given:** electrical energy $E = 36.0\,\text{GWh}$, efficiency $\eta = 0.380$ and heat of combustion of coal $H = 25.0\,\tfrac{\text{MJ}}{\text{kg}}$; given $1\,\text{GWh} = 3.60 \cdot 10^{12}\,\text{J}$
**Find:** the mass $m$ of coal burned in a year, in kilotonnes
**Principle:** Energy is conserved: the chemical energy $Q_1$ of the coal turns into electricity with efficiency $\eta$ and the rest into waste heat. The denominator of the efficiency is the bought fuel, and the energy of the fuel is the heat of combustion times the mass.
**Formula:** $E = \eta Q_1$ and $Q_1 = H m$, so $m = \dfrac{E}{\eta H}$
**Conversions:** $E = 36.0 \cdot 3.60 \cdot 10^{12}\,\text{J} = 1.296 \cdot 10^{14}\,\text{J}$ and $H = 25.0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}$. At the end $1\,\text{kt} = 10^6\,\text{kg}$.
**Substitution:** $m = \dfrac{1.296 \cdot 10^{14}\,\text{J}}{0.380 \cdot 25.0 \cdot 10^6\,\tfrac{\text{J}}{\text{kg}}} = 1.3642 \cdot 10^7\,\text{kg} = 13.642\,\text{kt}$
**Answer:** $13.6\,\text{kt}$, three significant figures, because the electrical energy $36.0\,\text{GWh}$, the efficiency $0.380$, the heat of combustion $25.0\,\tfrac{\text{MJ}}{\text{kg}}$ and the conversion factor $3.60 \cdot 10^{12}\,\text{J}/\text{GWh}$ all have three figures.
**Reasonableness:** Estimate: $\tfrac{1.3 \cdot 10^{14}\,\text{J}}{0.4 \cdot 2.5 \cdot 10^7\,\tfrac{\text{J}}{\text{kg}}} \approx 1.3 \cdot 10^7\,\text{kg}$. The amount corresponds to about 270 wagonloads of coal, when a wagon holds $50\,\text{t}$. The efficiencies cannot be compared directly: in a coal power plant the denominator is bought fuel, which gets used up: about $38\,\%$ of its energy turns into electricity and the rest into waste heat, and burning produces emissions, but the energy of the wind is not a store that gets used up. The efficiency of a wind farm only tells what fraction of the kinetic energy of the air flowing through the rotors is turned into electricity.

## fy3-15-L3-03
**Given:** heating need $Q = 100\,\text{kWh}$, coefficient of performance $\varepsilon = 3.00$, efficiency of the power plant $\eta_\text{plant} = 0.400$ and share left after transmission $\eta_\text{transm} = 0.950$
**Find:** the energy of the fuel $E_\text{fuel}$ at the power plant in kilowatt-hours
**Principle:** A heat pump moves heat from outside to inside and uses electricity for it, so the coefficient of performance tells the ratio of heat to electricity. The electricity is produced from fuel in a chain where each step lets through only part of the energy, so the fuel is found by dividing the electricity by the efficiency of the chain.
**Formula:** $\varepsilon = \dfrac{Q}{E_\text{s}}$, so $E_\text{s} = \dfrac{Q}{\varepsilon}$, and $E_\text{fuel} = \dfrac{E_\text{s}}{\eta_\text{transm}\, \eta_\text{plant}}$, thus $E_\text{fuel} = \dfrac{Q}{\eta_\text{transm}\, \eta_\text{plant}\, \varepsilon}$
**Conversions:** All energies are in kilowatt-hours and the factors are dimensionless, so no conversions are needed.
**Substitution:** $E_\text{fuel} = \dfrac{100\,\text{kWh}}{0.950 \cdot 0.400 \cdot 3.00} = \dfrac{100\,\text{kWh}}{1.14} = 87.719\,\text{kWh}$
**Answer:** $87.7\,\text{kWh}$, three significant figures, because the factors $0.950$, $0.400$ and $3.00$ have three figures and the heating need $100\,\text{kWh}$ is given to the nearest kilowatt-hour.
**Reasonableness:** Direct electric heating would need $\dfrac{100\,\text{kWh}}{0.380} = 263\,\text{kWh}$ of fuel and an oil boiler $\dfrac{100\,\text{kWh}}{0.900} = 111\,\text{kWh}$. The heat pump saves the most fuel, because in addition to the electricity used, heat transferred from the outside air comes into the house, so electricity is needed for only a third of the heat. Direct electric heating is the worst, because over $60\,\%$ of the energy of the fuel has already been wasted in producing the electricity.

## fy3-15-L3-04
**Given:** electricity need $P_\text{s} = 100\,\text{MW}$ and district heating need $P_\text{k} = 200\,\text{MW}$. A: efficiency of the condensing power plant $\eta_\text{s,A} = 0.400$ and of the heating boiler $\eta_\text{boiler} = 0.900$. B: electrical efficiency of the combined heat and power plant $\eta_\text{s,B} = 0.320$ and district heating power $0.560\,P_{0,\text{B}}$; the missing heat is produced in a similar heating boiler ($\eta_\text{boiler} = 0.900$)
**Find:** the difference of the fuel powers $P_{0,\text{A}} - P_{0,\text{B}}$ in megawatts
**Principle:** The fuel power is found by dividing the useful power by the efficiency. In option A electricity and heat are produced separately, so the fuel powers are added. In option B the plant is sized according to the electricity need, and the district heating it produces is subtracted from the heat need; the heat that is left is produced in a boiler.
**Formula:** A: $P_{0,\text{A}} = \dfrac{P_\text{s}}{\eta_\text{s,A}} + \dfrac{P_\text{k}}{\eta_\text{boiler}}$. B: $P_{0,\text{CHP}} = \dfrac{P_\text{s}}{\eta_\text{s,B}}$, $P_\text{k,CHP} = 0.560\,P_{0,\text{CHP}}$ and $P_{0,\text{B}} = P_{0,\text{CHP}} + \dfrac{P_\text{k} - P_\text{k,CHP}}{\eta_\text{boiler}}$. The difference is $P_{0,\text{A}} - P_{0,\text{B}}$.
**Conversions:** All powers are in megawatts and the efficiencies are dimensionless numbers, so no conversions are needed.
**Substitution:** A: $P_{0,\text{A}} = \dfrac{100\,\text{MW}}{0.400} + \dfrac{200\,\text{MW}}{0.900} = 250\,\text{MW} + 222.22\,\text{MW} = 472.22\,\text{MW}$. B: $P_{0,\text{CHP}} = \dfrac{100\,\text{MW}}{0.320} = 312.5\,\text{MW}$ and $P_\text{k,CHP} = 0.560 \cdot 312.5\,\text{MW} = 175.0\,\text{MW}$. The boiler has to produce $200\,\text{MW} - 175.0\,\text{MW} = 25.0\,\text{MW}$, so the fuel power of the boiler is $\dfrac{25.0\,\text{MW}}{0.900} = 27.78\,\text{MW}$ and $P_{0,\text{B}} = 312.5\,\text{MW} + 27.78\,\text{MW} = 340.28\,\text{MW}$. The difference is $472.22\,\text{MW} - 340.28\,\text{MW} = 131.94\,\text{MW}$.
**Answer:** $132\,\text{MW}$, three significant figures like the given efficiencies. Option B needs about $28\,\%$ less fuel.
**Reasonableness:** The overall efficiency of combined production is $0.320 + 0.560 = 0.880$, and $0.880 \cdot 312.5\,\text{MW} = 275\,\text{MW}$ is the sum of electricity and heat, $100\,\text{MW} + 175\,\text{MW}$. The overall efficiency of option A is only $\dfrac{300\,\text{MW}}{472.22\,\text{MW}} = 0.635$. The saving comes from the fact that in combined production the heat of the condenser, which in a condensing power plant would go to the sea, heats the city.

## fy3-15-L3-05
**Given:** $P_0 = 2700\,\text{MW}$, $P_\text{s} = 900\,\text{MW}$, water flow $q_m = 38.0\,\text{t/s}$ and $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$; from the table the temperatures in and out in January $1.2\,{}^\circ\text{C}$ and $12.1\,{}^\circ\text{C}$, in April $3.5\,{}^\circ\text{C}$ and $14.2\,{}^\circ\text{C}$, in July $17.8\,{}^\circ\text{C}$ and $28.4\,{}^\circ\text{C}$ and in September $12.3\,{}^\circ\text{C}$ and $23.2\,{}^\circ\text{C}$
**Find:** the heat power $P_\text{L}$ transferred to the condenser in megawatts
**Principle:** The heat of the condenser warms the cooling water, and the quantity of heat is $Q = cm\,\Delta T$ as long as the water stays liquid. Power is the quantity of heat per unit of time, so $P_\text{L} = c\,q_m\,\Delta T$. The rise in temperature varies slightly from month to month, so the average is used.
**Reading the graph:** From the table the rise $\Delta T = T_\text{out} - T_\text{in}$ is calculated for each month: January $10.9\,\text{K}$, April $10.7\,\text{K}$, July $10.6\,\text{K}$ and September $10.9\,\text{K}$. A temperature difference is the same on the Celsius and Kelvin scales.
**Formula:** $\Delta T_\text{avg} = \dfrac{\Sigma\,\Delta T}{4}$ and $P_\text{L} = c\,q_m\,\Delta T_\text{avg}$
**Conversions:** $q_m = 38.0\,\text{t/s} = 38\,000\,\text{kg/s}$. The result is converted from watts to megawatts, $1\,\text{MW} = 10^6\,\text{W}$.
**Substitution:** The sum of the rises is $10.9 + 10.7 + 10.6 + 10.9 = 43.1\,\text{K}$, so $\Delta T_\text{avg} = 10.775\,\text{K}$. Then
$P_\text{L} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 38\,000\,\tfrac{\text{kg}}{\text{s}} \cdot 10.775\,\text{K} = 1.7156 \cdot 10^{9}\,\text{W} = 1716\,\text{MW}$
**Answer:** $1720\,\text{MW}$, three significant figures like the water flow and the rise in temperature.
**Reasonableness:** Estimate: $4000 \cdot 4 \cdot 10^4 \cdot 11\,\text{W} \approx 1.8 \cdot 10^9\,\text{W}$. The waste heat power is $P_\text{h} = 2700\,\text{MW} - 900\,\text{MW} = 1800\,\text{MW}$, and the condenser's share of it is $\tfrac{1716}{1800} = 95\,\%$; the rest, about $84\,\text{MW}$, goes into the air, for example as losses of the generator and the transformer. Less heat is transferred to the sea water than the waste heat, as it should be. After the condenser the water is only about $11\,\text{K}$ warmer than the surroundings, so it can no longer be used to produce electricity, but the energy has not disappeared: it warms the sea. In July the water leaves at a temperature of $28.4\,{}^\circ\text{C}$, so the sea is warmer in the discharge area than elsewhere, and conditions for aquatic life may worsen.
