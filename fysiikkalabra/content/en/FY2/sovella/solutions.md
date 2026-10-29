## fy2-s1

### a)
**Given:** rated power of a wind turbine $P_\text{n} = 5.0\,\text{MW}$, capacity factor $k = 0.32$, length of a year $t = 8760\,\text{h}$ and the city's annual consumption $E = 380\,\text{GWh}$
**Find:** the number of wind turbines needed $N$
**Principle:** A wind turbine does not run at rated power all year, because the wind varies. The capacity factor gives the average power over a year: $P_\text{avg} = k \cdot P_\text{n}$. The power varies, but the energy of a year is the average power times the time. Once the annual energy of one turbine is known, the number of turbines is the consumption divided by it. The number is a whole number, and it must be at least the calculated value.
**Formula:** $E_1 = k \cdot P_\text{n} \cdot t$ and $N = \dfrac{E}{E_1}$
**Conversions:** When the power is in megawatts and the time in hours, the energy is in megawatt-hours: $1\,\text{GWh} = 1000\,\text{MWh}$.
**Substitution:** $E_1 = 0.32 \cdot 5.0\,\text{MW} \cdot 8760\,\text{h} = 14\,016\,\text{MWh} = 14.0\,\text{GWh}$ and $N = \dfrac{380\,\text{GWh}}{14.0\,\text{GWh}} = 27.1$
**Answer:** $28$ wind turbines are needed. The calculated value $27.1$ is rounded up, because $27$ turbines would produce only $27 \cdot 14.0\,\text{GWh} = 378\,\text{GWh}$, which is too little. The number is a whole number, so the rule of significant figures does not limit it.
**Reasonableness:** The city's average power is $\dfrac{380\,000\,\text{MWh}}{8760\,\text{h}} \approx 43\,\text{MW}$. The combined rated power of the turbines is $28 \cdot 5.0\,\text{MW} = 140\,\text{MW}$, about three times as much, which fits the capacity factor $0.32 \approx \tfrac{1}{3}$.

### b)
**Given:** annual consumption $E = 380\,\text{GWh}$ and life-cycle emission factors: coal $e = 820\,\text{g/kWh}$, natural gas $490\,\text{g/kWh}$ and onshore wind power $11\,\text{g/kWh}$
**Find:** the annual emission $m$ for each method and the decrease in the emission as a percentage compared with coal
**Principle:** The emission factor tells how many grams of carbon dioxide equivalent are produced per kilowatt-hour when the whole life cycle is included. When all the kilowatt-hours are produced in the same way, the emission is directly proportional to the energy. The percentage decrease is the difference of the emissions relative to the emission of coal. The energy is the same in all the alternatives, so it cancels, and the ratio can be calculated directly from the emission factors.
**Formula:** $m = e \cdot E$ and the decrease $\dfrac{m_\text{coal} - m}{m_\text{coal}} = 1 - \dfrac{e}{e_\text{coal}}$
**Conversions:** $E = 380\,\text{GWh} = 380 \cdot 10^{6}\,\text{kWh}$, because the factor is in the unit $\text{g/kWh}$. Finally $1\,\text{t} = 10^{6}\,\text{g}$.
**Substitution:** Coal: $m = 820\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 3.116 \cdot 10^{11}\,\text{g} = 3.116 \cdot 10^{5}\,\text{t}$. Natural gas: $m = 490\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 1.862 \cdot 10^{11}\,\text{g} = 1.862 \cdot 10^{5}\,\text{t}$. Wind power: $m = 11\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 4.18 \cdot 10^{9}\,\text{g} = 4.18 \cdot 10^{3}\,\text{t}$. Decrease: natural gas $1 - \dfrac{490\,\text{g/kWh}}{820\,\text{g/kWh}} = 0.40$ and wind power $1 - \dfrac{11\,\text{g/kWh}}{820\,\text{g/kWh}} = 0.99$
**Answer:** With coal $m \approx 3.1 \cdot 10^{5}\,\text{t}$, with natural gas $1.9 \cdot 10^{5}\,\text{t}$ and with wind power $4.2 \cdot 10^{3}\,\text{t}$ per year, to two significant figures like the emission factors. Natural gas reduces the emission by about $40\,\%$, wind power by about $99\,\%$.
**Reasonableness:** Coal produces just under a kilogram per kilowatt-hour, and there are hundreds of millions of kilowatt-hours, so hundreds of thousands of tonnes is the right order of magnitude. The percentages agree with those calculated from the tonnes: with natural gas $\dfrac{1.862 \cdot 10^{5}\,\text{t}}{3.116 \cdot 10^{5}\,\text{t}} \approx 0.60$ of the coal emission is left, so the decrease is $40\,\%$. Even the emission of wind power is not zero, because the manufacture and construction of the turbines cause emissions.

### c)
**Given:** $N = 28$ wind turbines, the annual energy of one $E_1 = 14.0\,\text{GWh}$, the share of winter in the annual energy of wind power $32\,\%$ and in the city's annual consumption $31\,\%$, consumption $E = 380\,\text{GWh}$, length of winter $90\,\text{d}$, peak power $80\,\text{MW}$ and the power during a calm spell below $5\,\%$ of the rated power
**Find:** the average power $P_\text{w}$ of the wind turbines in December–February and whether it meets the city's needs
**Principle:** The table gives what share of the annual energy is produced and consumed in winter. The average power in winter is the energy of winter divided by the hours of winter. The average power only tells whether the energy is enough on average: consumption and wind vary even during the winter, so the need must also be compared with the peak power and with the power during a calm spell.
**Formula:** $P_\text{w} = \dfrac{0.32 \cdot N E_1}{t}$ and the city's average power in winter $P_\text{c} = \dfrac{0.31 \cdot E}{t}$
**Conversions:** $t = 90 \cdot 24\,\text{h} = 2160\,\text{h}$ and $1\,\text{GWh} = 1000\,\text{MWh}$
**Substitution:** $N E_1 = 28 \cdot 14.016\,\text{GWh} = 392.4\,\text{GWh}$. $P_\text{w} = \dfrac{0.32 \cdot 392.4\,\text{GWh}}{2160\,\text{h}} = \dfrac{125\,600\,\text{MWh}}{2160\,\text{h}} = 58.1\,\text{MW}$ and $P_\text{c} = \dfrac{0.31 \cdot 380\,\text{GWh}}{2160\,\text{h}} = \dfrac{117\,800\,\text{MWh}}{2160\,\text{h}} = 54.5\,\text{MW}$. During a calm spell the power is below $0.05 \cdot 28 \cdot 5.0\,\text{MW} = 7\,\text{MW}$.
**Answer:** The average power of the wind turbines in winter is $P_\text{w} \approx 58\,\text{MW}$, to two significant figures like the percentages in the table. It is slightly larger than the city's average demand in winter, $55\,\text{MW}$, so the winter energy is enough on average. On a calm, frosty evening, however, the wind turbines give only about $7\,\text{MW}$ when the demand is $80\,\text{MW}$. Then about $73\,\text{MW}$ must come from elsewhere.
**Reasonableness:** Winter is a quarter of the year and accounts for about a third of both production and consumption, so the average powers in winter are larger than the average powers over the year ($45\,\text{MW}$ and $43\,\text{MW}$), as they should be. Both average powers are smaller than the peak power of $80\,\text{MW}$, as an average must be.

### d)
**Find:** how much the solar parks help on the peak evening, and which production methods could produce power on a calm, frosty evening, with their limitations
**Principle:** The annual energy does not tell whether power is available exactly when it is needed. On a peak evening the power at that moment is what matters. It can be produced by plants whose power can be adjusted or which run steadily regardless of the weather. Controllability and weather dependence are properties that have limits, not absolute categories.
**Model answer:** The annual energy of one solar park is $0.11 \cdot 10\,\text{MW} \cdot 8760\,\text{h} \approx 9.6\,\text{GWh}$, so $40$ parks produce about $385\,\text{GWh}$ per year. In winter, according to the table, only $4\,\%$ of that comes, about $15\,\text{GWh}$, which corresponds to an average power of $\dfrac{15\,400\,\text{MWh}}{2160\,\text{h}} \approx 7\,\text{MW}$. An evening in January is dark, so the power at the peak is zero. Solar electricity is mostly produced in summer, when consumption is at its lowest.

On a calm, frosty evening power could be produced by
- *a natural gas plant* ($50\,\text{MW}$): the power can be raised quickly, but gas is an imported fuel and its emission factor is the highest of the new alternatives
- *a biomass plant* ($40\,\text{MW}$): controllable, but slower to start, and the fuel has to be transported and stored
- *a share of hydropower* ($20\,\text{MW}$): the power can be adjusted quickly, but the energy of a year depends on rainfall, so the water cannot be used without limit
- *a small nuclear plant* ($60\,\text{MW}$): runs steadily regardless of the weather and is therefore running also on the peak evening, but the power cannot be raised above the rated power, and the plant is not yet available
- *electricity bought from the grid*: available when production elsewhere has spare capacity, but the consumption of the whole of Finland is at its highest on the same frosty evenings.

### e)
**Find:** a justified recommendation for the city's electricity production with calculations, a counterargument and assumptions
**Principle:** A good recommendation covers two different requirements: the annual energy (the calculations of parts a and b) and the winter peak power (parts c and d). The emission is calculated separately for each production method with the formula $m = e \cdot E$ and added together. The choice is a value judgement in which, besides emissions, controllability, fuel, land use, waste and schedule also weigh. That is why there is no single right production method, and the answer is assessed on the basis of the reasoning. Below is one possible recommendation.
**Model answer:** I recommend a combination: $18$ wind turbines, the city's share of the hydropower plant and one biomass plant that runs mainly when the wind is not enough.

*Energy.* The wind turbines produce $18 \cdot 14.0\,\text{GWh} \approx 252\,\text{GWh}$ and the hydropower share $0.50 \cdot 20\,\text{MW} \cdot 8760\,\text{h} \approx 88\,\text{GWh}$ per year. The remaining $380\,\text{GWh} - 252\,\text{GWh} - 88\,\text{GWh} \approx 40\,\text{GWh}$ is produced by the biomass plant, whose capacity factor is then only about $\dfrac{40\,100\,\text{MWh}}{40\,\text{MW} \cdot 8760\,\text{h}} \approx 0.11$.

*Emission.* $m = 11\,\text{g/kWh} \cdot 252 \cdot 10^{6}\,\text{kWh} + 24\,\text{g/kWh} \cdot 88 \cdot 10^{6}\,\text{kWh} + 230\,\text{g/kWh} \cdot 40 \cdot 10^{6}\,\text{kWh} \approx 2.8 \cdot 10^{3}\,\text{t} + 2.1 \cdot 10^{3}\,\text{t} + 9.2 \cdot 10^{3}\,\text{t} \approx 1.4 \cdot 10^{4}\,\text{t}$ per year. That is about $95\,\%$ less than with coal ($3.1 \cdot 10^{5}\,\text{t}$) and clearly less than with natural gas alone ($1.9 \cdot 10^{5}\,\text{t}$). Wind power alone ($4.2 \cdot 10^{3}\,\text{t}$) would have lower emissions, but it does not cover the peak.

*Peak.* On a calm, frosty evening the biomass plant ($40\,\text{MW}$), hydropower ($20\,\text{MW}$) and the wind turbines (below $0.05 \cdot 90\,\text{MW} \approx 4.5\,\text{MW}$) give about $65\,\text{MW}$ in total. The remaining $15\,\text{MW}$ or so is bought from the grid, or part of the consumption, such as electric heating, is shifted a few hours later.

*Other arguments.* The combination does not depend on a single fuel or a single kind of weather: wind power has no fuel, and the power of hydropower and biomass can be adjusted. The wind turbines take up land and change the landscape. The biomass plant needs wood chips, but only about a sixth of what it would need at full capacity factor.

*The strongest counterargument* is that the biomass plant stands idle for much of the year, so building it is expensive per unit of energy produced, and the carbon dioxide from burning biomass is bound back only over decades. My answer is that the plant is needed precisely because of its controllability: without it, more than $50\,\text{MW}$ would be needed from the grid on the peak evening, when the consumption of the whole country is at its highest. The share of biomass in the energy is only about $11\,\%$.

*Assumptions.* I assumed that the capacity factors are the same every year. Windiness and rainfall vary, so in a bad year the biomass plant runs more and the emission grows. I also assumed that consumption stays at $380\,\text{GWh}$. If heating and transport are electrified, consumption grows and more wind turbines are needed. The price and the reinforcement of the electricity grid were left uncalculated, although they may decide the matter.

### Hyväksytään myös
Any production method or combination receives full points when the recommendation covers the annual energy and either covers the winter peak or estimates the missing power and how it is handled, the emission has been calculated correctly, the limitations have been discussed, and a counterargument and assumptions have been presented. For example:
- *A small nuclear plant.* It produces $0.90 \cdot 60\,\text{MW} \cdot 8760\,\text{h} \approx 473\,\text{GWh}$ per year, which is more than the city needs, and the emission for the whole consumption would be only $12\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 4.6 \cdot 10^{3}\,\text{t}$. The reasoning must discuss that the plant is not yet available and that construction takes more than ten years (what the city does in the meantime), that $20\,\text{MW}$ is missing from the peak, and that spent fuel must be disposed of permanently.
- *Wind power with a natural gas plant as reserve power.* When the gas plant runs only during calm spells, the emission stays small. The reasoning estimates what share of the energy is produced with gas and calculates its emission.
- *Two biomass plants.* They cover the peak of $80\,\text{MW}$ and the annual energy at a capacity factor of $\dfrac{380\,000\,\text{MWh}}{80\,\text{MW} \cdot 8760\,\text{h}} \approx 0.54$. The emission $230\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 8.7 \cdot 10^{4}\,\text{t}$ is about $72\,\%$ lower than with coal. The reasoning discusses the availability of wood chips, transport and the slow binding of carbon.
- *Wind power and buying electricity from the grid during peaks*, when the dependence on the grid on the coldest days is noted and assessed.

Points are given not for the production method chosen but for how the choice is justified.

### Yleisiä virheitä
- In part a the energy is calculated with the rated power without the capacity factor: $5.0\,\text{MW} \cdot 8760\,\text{h} = 43.8\,\text{GWh}$, so it seems that only $9$ turbines are needed.
- In part a $27.1$ is rounded down to $27$, so some electricity is left missing.
- In part b gigawatt-hours are not converted to kilowatt-hours, or grams are not converted to tonnes.
- In part c it is concluded from the average power that wind power is always enough in winter, even though the peak power and calm spells are decisive. Energy and power are confused.
- Wind power, solar power or nuclear power is called emission-free, even though their life-cycle emission factors are also $11\text{–}48\,\text{g/kWh}$.
- Nuclear power is considered completely non-adjustable or hydropower unlimited: the power of a nuclear plant can be reduced, and the energy of hydropower depends on rainfall.
- In part e only an opinion is given, without a calculation, or the winter peak is left undiscussed.
