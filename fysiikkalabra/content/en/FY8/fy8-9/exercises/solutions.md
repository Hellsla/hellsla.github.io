## fy8-9-L1-01
**Given:** initial activity $A_0 = 740\,\text{MBq}$, half-life $T_{1/2} = 6.01\,\text{h}$, time $t = 18.0\,\text{h}$
**Asked:** the activity $A$ of the preparation at the time $t$ in megabecquerels
**Principle:** The activity is proportional to the number of undecayed nuclei, $A = \lambda N$, so it decreases according to the decay law: every half-life halves it. The preparation contains an enormous number of nuclei, so the law holds exactly.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** None are needed: the time and the half-life are both in hours, so their ratio is a pure number, and the activity is obtained in the same unit as $A_0$.
**Substitution:** $A = 740\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{18.0\,\text{h} / 6.01\,\text{h}} = 740\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{2.9950} = 740\,\text{MBq} \cdot 0.12543 = 92.82\,\text{MBq}$
**Answer:** $92.8\,\text{MBq}$, three significant figures like the half-life $6.01\,\text{h}$ and the time $18.0\,\text{h}$.
**Reasonableness:** Almost exactly three half-lives passed, so the activity should be about an eighth of the initial value: $740\,\text{MBq} : 8 = 92.5\,\text{MBq}$. The result is slightly greater, because a little is still missing from three half-lives.

## fy8-9-L1-02
**Given:** half-life $T_{1/2} = 3.82\,\text{d}$, time $t = 10.0\,\text{d}$, no new radon is formed in the vessel
**Asked:** the fraction $\tfrac{N}{N_0}$ of undecayed radon nuclei as a percentage
**Principle:** The radon nuclei decay independently of each other, and there are very many of them in the air sample, so their number follows the decay law. Because no new radon is formed, the number only decreases.
**Formula:** $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, from which $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** None are needed: the time and the half-life are both in days. Finally the fraction is converted to a percentage: $1 = 100\,\%$.
**Substitution:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{10.0\,\text{d} / 3.82\,\text{d}} = \left(\tfrac{1}{2}\right)^{2.6178} = 0.16292 = 16.292\,\%$
**Answer:** $16.3\,\%$, three significant figures like the half-life $3.82\,\text{d}$ and the time $10.0\,\text{d}$.
**Reasonableness:** A little more than two and a half half-lives passed. After two, $25\,\%$ would be left and after three $12.5\,\%$; the result is between these.

## fy8-9-L1-03
**Given:** the half-life of caesium-137 $T_{1/2} = 30.1\,\text{a}$
**Asked:** the decay constant $\lambda$ in the unit $\tfrac{1}{\text{a}}$
**Principle:** At the half-life half of the nuclei are undecayed, so in the form $N = N_0 e^{-\lambda t}$ of the decay law $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$. This gives the relation between the decay constant and the half-life.
**Formula:** $\lambda T_{1/2} = \ln 2$, from which $\lambda = \dfrac{\ln 2}{T_{1/2}}$
**Conversions:** None are needed: when the half-life is in years, the decay constant is obtained directly in the unit $\tfrac{1}{\text{a}}$.
**Substitution:** $\lambda = \dfrac{0.69315}{30.1\,\text{a}} = 0.023028\,\tfrac{1}{\text{a}}$
**Answer:** $0.0230\,\tfrac{1}{\text{a}}$, three significant figures like the half-life $30.1\,\text{a}$.
**Reasonableness:** The decay constant tells that about $2.3\,\%$ of the nuclei decay in a year. Then half decay in a time of roughly $0.69 : 0.023\,\tfrac{1}{\text{a}} \approx 30\,\text{a}$, which agrees with the half-life.

## fy8-9-L1-04
**Given:** the number of undecayed nuclei $N = 3.20 \cdot 10^{12}$, the decay constant $\lambda = 4.17 \cdot 10^{-9}\,\tfrac{1}{\text{s}}$
**Asked:** the activity $A$ of the source in kilobecquerels
**Principle:** Every nucleus decays in a second with the probability $\lambda$, so of $N$ nuclei on average $\lambda N$ decay per second. This is the activity.
**Formula:** $A = \lambda N$
**Conversions:** $1\,\text{Bq} = 1\,\tfrac{1}{\text{s}}$ and $1\,\text{kBq} = 1000\,\text{Bq}$.
**Substitution:** $A = 4.17 \cdot 10^{-9}\,\tfrac{1}{\text{s}} \cdot 3.20 \cdot 10^{12} = 13\,344\,\tfrac{1}{\text{s}} = 13\,344\,\text{Bq} = 13.344\,\text{kBq}$
**Answer:** $13.3\,\text{kBq}$, three significant figures like the number of nuclei and the decay constant.
**Reasonableness:** By estimate $4 \cdot 10^{-9} \cdot 3 \cdot 10^{12} = 1.2 \cdot 10^{4}$, that is, about $12\,\text{kBq}$. There are many nuclei, but cobalt-60 decays slowly, so only a small fraction of the nuclei decays per second.

## fy8-9-L1-05
**Given:** initial activity $A_0 = 800\,\text{kBq}$, activity $A = 200\,\text{kBq}$ after the time $t = 48.0\,\text{h}$
**Asked:** the half-life $T_{1/2}$ in hours
**Principle:** The activity halves during every half-life, because it is proportional to the number of undecayed nuclei. We count how many half-lives fit in the time $t$: $800\,\text{kBq} \to 400\,\text{kBq} \to 200\,\text{kBq}$ is two halvings.
**Formula:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}} = \tfrac{1}{4} = \left(\tfrac{1}{2}\right)^{2}$, so $\tfrac{t}{T_{1/2}} = 2$ and $T_{1/2} = \dfrac{t}{2}$
**Conversions:** None are needed: the time is in hours, and the answer is asked in hours.
**Substitution:** $T_{1/2} = \dfrac{48.0\,\text{h}}{2} = 24.0\,\text{h}$
**Answer:** $24.0\,\text{h}$, three significant figures like the time $48.0\,\text{h}$.
**Reasonableness:** Check with the decay law: $800\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{48.0\,\text{h} / 24.0\,\text{h}} = 800\,\text{kBq} \cdot \tfrac{1}{4} = 200\,\text{kBq}$, as in the task.

## fy8-9-L2-01
**Given:** the half-life of iodine-131 $T_{1/2} = 8.02\,\text{d}$
**Asked:** the decay constant $\lambda$ in the unit $10^{-6}\,\tfrac{1}{\text{s}}$
**Principle:** At the half-life $e^{-\lambda T_{1/2}} = \tfrac{1}{2}$, because half of the nuclei have decayed. The decay constant is wanted in seconds, so the half-life is first converted to seconds.
**Formula:** $\lambda T_{1/2} = \ln 2$, from which $\lambda = \dfrac{\ln 2}{T_{1/2}}$
**Conversions:** $1\,\text{d} = 24 \cdot 3600\,\text{s} = 86\,400\,\text{s}$, so $T_{1/2} = 8.02 \cdot 86\,400\,\text{s} = 692\,928\,\text{s}$.
**Substitution:** $\lambda = \dfrac{0.69315}{692\,928\,\text{s}} = 1.00032 \cdot 10^{-6}\,\tfrac{1}{\text{s}}$
**Answer:** $1.00 \cdot 10^{-6}\,\tfrac{1}{\text{s}}$, three significant figures like the half-life $8.02\,\text{d}$.
**Reasonableness:** About a millionth of the nuclei decays per second, so in a day about $86\,400 \cdot 10^{-6} \approx 0.09$, that is, $9\,\%$ of the remaining nuclei decay. Because $0.91^{8} \approx 0.47$, after eight days about a half is left, which fits the half-life $8.02\,\text{d}$.

## fy8-9-L2-02
**Given:** activity $A = 37\,\text{kBq}$, the half-life of americium-241 $T_{1/2} = 433\,\text{a}$, $1\,\text{a} = 365.25\,\text{d}$
**Asked:** the number of nuclei $N$ in the unit $10^{14}$
**Principle:** The activity is the product of the decay constant and the number of nuclei, $A = \lambda N$, and the decay constant is obtained from the half-life. Because the activity is decays per second, the decay constant must be in the unit $\tfrac{1}{\text{s}}$.
**Formula:** $A = \lambda N$ and $\lambda = \dfrac{\ln 2}{T_{1/2}}$, so $N = \dfrac{A}{\lambda} = \dfrac{A\,T_{1/2}}{\ln 2}$
**Conversions:** $A = 37\,\text{kBq} = 37 \cdot 10^{3}\,\tfrac{1}{\text{s}}$ and $T_{1/2} = 433 \cdot 365.25 \cdot 86\,400\,\text{s} = 1.36644 \cdot 10^{10}\,\text{s}$.
**Substitution:** $N = \dfrac{37 \cdot 10^{3}\,\tfrac{1}{\text{s}} \cdot 1.36644 \cdot 10^{10}\,\text{s}}{0.69315} = 7.294 \cdot 10^{14}$
**Answer:** $7.3 \cdot 10^{14}$ nuclei, two significant figures like the activity $37\,\text{kBq}$.
**Reasonableness:** The decay constant is $\lambda = 5.07 \cdot 10^{-11}\,\tfrac{1}{\text{s}}$, and $5.07 \cdot 10^{-11}\,\tfrac{1}{\text{s}} \cdot 7.29 \cdot 10^{14} \approx 3.7 \cdot 10^{4}\,\tfrac{1}{\text{s}}$, which is the given activity. There are many nuclei, because long-lived americium decays slowly; as a mass this is only about $0.3\,\mu\text{g}$.

## fy8-9-L2-03
**Given:** initial activity $A_0 = 2.00\,\text{GBq}$, duration of the journey $t = 2\,\text{h}\ 30\,\text{min}$, the half-life of fluorine-18 $T_{1/2} = 110\,\text{min}$
**Asked:** the activity $A$ on arrival in megabecquerels
**Principle:** The activity follows the decay law, because it is proportional to the number of undecayed nuclei. The time and the half-life must be expressed in the same unit so that the exponent is a pure number.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** $t = 2\,\text{h}\ 30\,\text{min} = 2 \cdot 60\,\text{min} + 30\,\text{min} = 150\,\text{min}$ and $A_0 = 2.00\,\text{GBq} = 2000\,\text{MBq}$.
**Substitution:** $A = 2000\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{150\,\text{min} / 110\,\text{min}} = 2000\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{1.3636} = 2000\,\text{MBq} \cdot 0.38860 = 777.20\,\text{MBq}$
**Answer:** $777\,\text{MBq}$, three significant figures like the initial activity $2.00\,\text{GBq}$ and the half-life $110\,\text{min}$.
**Reasonableness:** The journey took a little more than one half-life, so the activity should be slightly less than a half of the initial value, that is, less than $1000\,\text{MBq}$. After two half-lives it would be $500\,\text{MBq}$; the result is between these.

## fy8-9-L2-04
**Given:** initial mass $m_0 = 5.00\,\text{mg}$, half-life $T_{1/2} = 5.27\,\text{a}$, time $t = 15.0\,\text{a}$
**Asked:** the mass $m$ of the remaining cobalt-60 in milligrams
**Principle:** Every cobalt-60 nucleus has the same mass, so the mass of the undecayed cobalt is proportional to the number of undecayed nuclei and follows the same decay law as $N$.
**Formula:** $N = N_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ and $m \propto N$, so $m = m_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** None are needed: the time and the half-life are in years, and the mass is obtained in milligrams.
**Substitution:** $m = 5.00\,\text{mg} \cdot \left(\tfrac{1}{2}\right)^{15.0\,\text{a} / 5.27\,\text{a}} = 5.00\,\text{mg} \cdot \left(\tfrac{1}{2}\right)^{2.8463} = 5.00\,\text{mg} \cdot 0.13905 = 0.69526\,\text{mg}$
**Answer:** $0.695\,\text{mg}$, three significant figures like the initial mass $5.00\,\text{mg}$ and the half-life $5.27\,\text{a}$.
**Reasonableness:** A little less than three half-lives passed, so the mass should be slightly more than an eighth of the original: $5.00\,\text{mg} : 8 = 0.625\,\text{mg}$. Nickel-60 takes the place of the decayed nuclei, so the total mass of the source hardly changes.

## fy8-9-L3-01
**Given:** the activity of the sample is $38.0\,\%$ of the activity of living wood per gram of carbon, the half-life of carbon-14 $T_{1/2} = 5700\,\text{a}$
**Asked:** the time $t$ passed since the death of the tree in years
**Principle:** In living wood the fraction of carbon-14 stays constant, so at the moment of death the activity per gram was the same as in living wood. After that the activity has decreased according to the decay law. When the fraction $\tfrac{A}{A_0}$ is known, the elapsed time is solved from the exponent with a logarithm.
**Formula:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \ln 2$ and $t = T_{1/2} \cdot \dfrac{\ln (A_0 / A)}{\ln 2}$
**Conversions:** None are needed: $\tfrac{A_0}{A} = \tfrac{100\,\%}{38.0\,\%}$ is a pure number, and the time is obtained in the same unit as the half-life, that is, in years.
**Substitution:** $t = 5700\,\text{a} \cdot \dfrac{\ln 2.6316}{0.69315} = 5700\,\text{a} \cdot \dfrac{0.96758}{0.69315} = 5700\,\text{a} \cdot 1.3959 = 7957\,\text{a}$
**Answer:** $7960\,\text{a}$, that is, about $7.96 \cdot 10^{3}\,\text{a}$, three significant figures like the fraction $38.0\,\%$.
**Reasonableness:** After one half-life the activity would be $50\,\%$ and after two $25\,\%$. The value $38\,\%$ is between these, so the age must be $5700$–$11\,400$ years. The result $1.40$ half-lives fits this.

## fy8-9-L3-02
**Given:** pulse rate at the start $820$ pulses per minute and $t = 10.0\,\text{min}$ later $230$ pulses per minute, background radiation $30$ pulses per minute
**Asked:** the half-life $T_{1/2}$ in minutes
**Principle:** The meter counts both the radiation of the sample and that of the surroundings. Only the part from the sample is proportional to its activity and decreases according to the decay law, so the background is subtracted first. The background is assumed to stay the same during the whole measurement.
**Formula:** $\dfrac{R_1}{R_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $\ln \dfrac{R_0}{R_1} = \dfrac{t}{T_{1/2}} \ln 2$ and $T_{1/2} = \dfrac{t \ln 2}{\ln (R_0 / R_1)}$, where $R_0$ and $R_1$ are the net pulse rates of the sample
**Conversions:** No unit conversions: the ratio of the pulse rates is a pure number, and the time is in minutes. The net pulse rates: $R_0 = 820 - 30 = 790$ and $R_1 = 230 - 30 = 200$ pulses per minute.
**Substitution:** $T_{1/2} = \dfrac{10.0\,\text{min} \cdot 0.69315}{\ln (790 : 200)} = \dfrac{6.9315\,\text{min}}{\ln 3.95} = \dfrac{6.9315\,\text{min}}{1.3737} = 5.0458\,\text{min}$
**Answer:** $5.05\,\text{min}$, three significant figures like the time $10.0\,\text{min}$.
**Reasonableness:** The net pulse rate decreased from $790$ to $200$, that is, to almost a quarter, so $10\,\text{min}$ is a little less than two half-lives and the half-life is a little more than $5\,\text{min}$. Without subtracting the background the ratio would be $820 : 230 = 3.57$, and the half-life would wrongly be about $5.5\,\text{min}$.

## fy8-9-L3-03
**Given:** the activities are at first equal, $A_\text{I,0} = A_\text{Cs,0} = A_0$, the half-life of iodine-131 $8.02\,\text{d}$, that of caesium-137 $30.1\,\text{a}$, time $t = 30.0\,\text{d}$, $1\,\text{a} = 365.25\,\text{d}$
**Asked:** the share of iodine-131 in the total activity as a percentage
**Principle:** Each isotope decays with its own half-life independently of the other, and the activity of each follows the decay law. The total activity is their sum. Because the initial activities are equal, $A_0$ cancels from the fraction.
**Formula:** $A_\text{I} = A_0 \left(\tfrac{1}{2}\right)^{t/T_\text{I}}$ and $A_\text{Cs} = A_0 \left(\tfrac{1}{2}\right)^{t/T_\text{Cs}}$, so the share is $p = \dfrac{A_\text{I}}{A_\text{I} + A_\text{Cs}} = \dfrac{\left(\tfrac{1}{2}\right)^{t/T_\text{I}}}{\left(\tfrac{1}{2}\right)^{t/T_\text{I}} + \left(\tfrac{1}{2}\right)^{t/T_\text{Cs}}}$
**Conversions:** $T_\text{Cs} = 30.1\,\text{a} = 30.1 \cdot 365.25\,\text{d} = 10\,994\,\text{d}$, so that all times are in days.
**Substitution:** $\left(\tfrac{1}{2}\right)^{30.0\,\text{d} / 8.02\,\text{d}} = \left(\tfrac{1}{2}\right)^{3.7406} = 0.074809$ and $\left(\tfrac{1}{2}\right)^{30.0\,\text{d} / 10\,994\,\text{d}} = \left(\tfrac{1}{2}\right)^{0.0027288} = 0.99811$, so $p = \dfrac{0.074809}{0.074809 + 0.99811} = \dfrac{0.074809}{1.07292} = 0.069725 = 6.9725\,\%$
**Answer:** $6.97\,\%$, three significant figures like the half-lives and the time $30.0\,\text{d}$.
**Reasonableness:** In a month almost four half-lives of iodine pass, so the activity of iodine has dropped below a tenth, while the activity of caesium is almost unchanged. The share of iodine must therefore be below $10\,\%$ but above zero, as the result is. That is why after an accident iodine is a big problem for the first weeks, caesium for decades.
