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
**Substitution:** $N E_1 = 28 \cdot 14.016\,\text{GWh} = 392.4\,\text{GWh}$. $P_\text{w} = \dfrac{0.32 \cdot 392.4\,\text{GWh}}{2160\,\text{h}} = \dfrac{125\,600\,\text{MWh}}{2160\,\text{h}} = 58.1\,\text{MW}$ and $P_\text{c} = \dfrac{0.31 \cdot 380\,\text{GWh}}{2160\,\text{h}} = \dfrac{117\,800\,\text{MWh}}{2160\,\text{h}} = 54.5\,\text{MW}$. During a calm spell the power is $P_\text{wind} < 0.05 \cdot 28 \cdot 5.0\,\text{MW} = 7\,\text{MW}$, so the power needed from elsewhere is $P_\text{elsewhere} > 80\,\text{MW} - 7\,\text{MW} = 73\,\text{MW}$.
**Answer:** The average power of the wind turbines in winter is $P_\text{w} \approx 58\,\text{MW}$, to two significant figures like the percentages in the table. It is slightly larger than the city's average demand in winter, $55\,\text{MW}$, so the winter energy is enough on average. On a calm, frosty evening, however, the combined output of the wind turbines can fall below $7\,\text{MW}$. If the city's power demand is then $80\,\text{MW}$, more than $73\,\text{MW}$ of electric power is needed from elsewhere.
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

*The strongest counterargument* is that the biomass plant stands idle for much of the year, so building it is expensive per unit of energy produced, and the carbon dioxide from burning biomass is bound back only over decades, so the real emission can be larger than the assumed $230\,\text{g/kWh}$. My answer is that the plant is needed precisely because of its controllability: without it, more than $50\,\text{MW}$ would be needed from the grid on the peak evening, when the consumption of the whole country is at its highest. The share of biomass in the energy is only about $11\,\%$.

*Assumptions.* I assumed that the capacity factors are the same every year. Windiness and rainfall vary, so in a bad year the biomass plant runs more and the emission grows. I also assumed that consumption stays at $380\,\text{GWh}$. If heating and transport are electrified, consumption grows and more wind turbines are needed. The price and the reinforcement of the electricity grid were left uncalculated, although they may decide the matter.

### Hyväksytään myös
Any production method or combination receives full points when the recommendation covers the annual energy and either covers the winter peak or estimates the missing power and how it is handled, the emission has been calculated correctly, the limitations have been discussed, and a counterargument and assumptions have been presented. For example:
- *A small nuclear plant.* It produces $0.90 \cdot 60\,\text{MW} \cdot 8760\,\text{h} \approx 473\,\text{GWh}$ per year, which is more than the city needs, and the emission for the whole consumption would be only $12\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 4.6 \cdot 10^{3}\,\text{t}$. The reasoning must discuss that the plant is not yet available and that construction takes more than ten years (what the city does in the meantime), that $20\,\text{MW}$ is missing from the peak, and that spent fuel must be disposed of permanently.
- *Wind power with a natural gas plant as reserve power.* When the gas plant runs only during calm spells, the emission stays small. The reasoning estimates what share of the energy is produced with gas and calculates its emission.
- *Two biomass plants.* They cover the peak of $80\,\text{MW}$ and the annual energy at a capacity factor of $\dfrac{380\,000\,\text{MWh}}{80\,\text{MW} \cdot 8760\,\text{h}} \approx 0.54$. The emission $230\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 8.7 \cdot 10^{4}\,\text{t}$ is about $72\,\%$ lower than with coal. The reasoning discusses the availability of wood chips, transport and the slow binding of carbon, and that the factor $230\,\text{g/kWh}$ is an accounting assumption from which the real factor of forest wood chips can differ.
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

## fy2-s2

The sources and the question are the student's own, so the answers differ. Below is the structure of a model answer and one example. The question of the example is the greenhouse gas emission of wind power per unit of electricity produced. Source 1 is real: Annex III of Working Group III of the Fifth Assessment Report of the IPCC (AR5, 2014), whose median of life-cycle emissions is also used in task fy2-s1. Source 2 is an invented example of a common type of publication, an energy company's web page, and it does not exist.

### a)
**Find:** the question, the references of the two sources and the author, publisher and purpose of each
**Principle:** From the reference the reader can find the publication themselves. The author and the publisher tell who is responsible for the figure, and the purpose tells why the publication was made. The purpose does not make the figure wrong, but it can affect which figures the publication chooses and how it presents them. Therefore a source is not rejected because of its publisher; instead its purpose is taken into account in the interpretation.
**Model answer:** *Structure.* The question in one sentence. For each source the reference, the author or publisher, the type of publication and its purpose, and one or two sentences on how the purpose may show in the figures.

*Example.* My question is how large the greenhouse gas emission of wind power is per unit of electricity produced.

References:

- Source 1: Schlömer, S. et al. (2014). Annex III: Technology-specific cost and performance parameters. In *Climate Change 2014: Mitigation of Climate Change. Contribution of Working Group III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge University Press. Accessed (date of reading).
- Source 2 (invented example): Esimerkkienergia Oy. Tuulivoima – puhdasta sähköä [Wind power – clean electricity]. Web page, updated (year). (web address). Accessed (date of reading).

Source 1 is an annex of an assessment report of the Intergovernmental Panel on Climate Change, the IPCC, which collects the emissions of production methods from many studies. Its authors are researchers, and its purpose is to collect research findings as a basis for decision-making. The report gives a range and a median and does not recommend any production method.

Source 2 is the web page of an energy company on which the company presents its wind farms. Its purpose is to inform customers about the company's production and to market it. Therefore the page tells about the advantages of wind power and does not necessarily tell how the figure has been calculated.

### b)
**Find:** the time of publication of the sources, the period of the data, and the figures with their quantities and units in the same unit
**Principle:** The time of publication and the period of the data are different things: a new publication can use old data. Production methods and their equipment change, so figures from different years can differ for that reason alone. Figures can be compared only when they are the same quantity and in the same unit. The units of an emission factor are converted into each other by converting both the mass prefix and the energy prefix.
**Model answer:** *Structure.* For each source the year of publication and the years of the data, the figure with its quantity and unit and, if needed, the conversion to the same unit.

*Example.* Source 1 was published in 2014, and it collects studies published before that. Source 2 was updated last year, but it does not say which year the figure is from. Source 1 gives the median of the life-cycle greenhouse gas emissions of onshore wind power as $11\,\tfrac{\text{g}}{\text{kWh}}$ in carbon dioxide equivalent. The quantity is thus the combined effect of all greenhouse gases converted into an amount of carbon dioxide. Source 2 says that wind power produces electricity without carbon dioxide emissions, so its figure is $0\,\tfrac{\text{g}}{\text{kWh}}$, and it concerns carbon dioxide only. If one source gave the emission in the unit $\tfrac{\text{t}}{\text{GWh}}$, the conversion would be $11\,\tfrac{\text{g}}{\text{kWh}} = \tfrac{11 \cdot 10^{-6}\,\text{t}}{10^{-6}\,\text{GWh}} = 11\,\tfrac{\text{t}}{\text{GWh}}$, so the number stays the same.

### c)
**Find:** the system boundary, assumptions and uncertainty of each source
**Principle:** The system boundary tells what the figure includes. Electricity is only part of all energy, because energy is also used for heating, transport and industry. Operational emissions are produced when the power plant produces energy. Life-cycle emissions also include the construction of the plant, the supply of fuel, maintenance and decommissioning. Therefore a production method that has no operational emissions can still cause life-cycle emissions. Assumptions such as the plant type, the region and the capacity factor change the figure, and the uncertainty shows as a range.
**Model answer:** *Structure.* For each source: electricity or total energy, operational or life-cycle emission (or the corresponding boundary for another question), the most important assumptions and the uncertainty. If the source does not tell something, this is stated.

*Example.* Both sources concern electricity. Source 1 calculates life-cycle emissions, so the manufacture, construction and decommissioning of the plants are included. Source 2 means operational emissions: a rotating wind turbine burns nothing. Source 1 assumes the capacity factors and plant lifetimes obtained from its studies, and the result depends on them: a longer lifetime spreads the construction emissions over a larger amount of energy. Besides the median, source 1 gives the range of the studies, $7\text{–}56\,\tfrac{\text{g}}{\text{kWh}}$ for onshore wind power, so its uncertainty is visible. Source 2 does not give the uncertainty, but the operational emission is zero by definition.

### d)
**Find:** the comparability of the sources and a justified conclusion
**Principle:** Figures are comparable when they are the same quantity in the same unit, from the same period or at least from a period in which the matter has not had time to change, and with the same system boundary and the same key assumptions. If one of these differs, the difference can explain the difference between the figures. The conclusion distinguishes what the sources say from what can be inferred from them.
**Model answer:** *Structure.* Comparability item by item, an explanation of the difference between the figures and a conclusion that answers the question or justifies why the sources are not enough for it.

*Example.* The figures are in the same unit, and both concern electricity. The quantity is almost the same: source 1 counts all greenhouse gases in carbon dioxide equivalent and source 2 only carbon dioxide. The figures are still not directly comparable, because the system boundary is different: source 1 gives the life-cycle emission and source 2 the operational emission. The difference between $11\,\tfrac{\text{g}}{\text{kWh}}$ and $0\,\tfrac{\text{g}}{\text{kWh}}$ is explained by this, and neither source is wrong. My conclusion is that wind power has no operational carbon dioxide emissions and that its life-cycle greenhouse gas emission is about $11\,\tfrac{\text{g}}{\text{kWh}}$ in carbon dioxide equivalent according to source 1. When comparing production methods I use life-cycle emissions, because in them all production methods are calculated with the same boundary. The claim that wind power is emission-free holds only for the time of operation.

Another equally good conclusion would be, for example, this: the sources are not comparable, because source 2 states neither its boundary nor its year, and an answer requires a source that gives the life-cycle emission with the same boundary as source 1.

### Hyväksytään myös
- Any energy production question that is answered with a number, and any two publications with different publishers. The points come from the assessment, not from the choice of sources.
- A justified conclusion that the figures are not comparable, for example because one concerns electricity and the other all energy, or because the data are from different decades. In that case part d tells what kind of source would be needed for a comparison.
- A conclusion that the sources are comparable and support each other, when it has been justified item by item.
- Different conclusions from the same sources, when they have been justified with the information in the sources and do not claim more than the sources support.

### Yleisiä virheitä
- The source is a search engine results page, an AI answer or the front page of a website on which the figure cannot be found. The reference lacks the publisher, the year or the date of reading.
- The sources have the same publisher, for example two pages of the same company, or a news item that only repeats the figure of the other source.
- A source is rejected on the basis of its publisher alone, for example because it is a company page, even though its figure may be correct within its own boundary.
- The time of publication and the period of the data are confused.
- Figures are compared in different units, or in the conversion only the mass prefix or only the energy prefix is converted.
- Electricity and total energy, or operational and life-cycle emissions, are compared with each other without noticing the difference in the boundary.
- The conclusion chooses one of the sources as correct without justification, or it claims more on the basis of the sources than they say.
