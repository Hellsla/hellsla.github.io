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

## fy8-9-L1-06
**Asked:** which statement about the undecayed nuclei of the sample is correct, when $8.0\,\text{h}$ is two half-lives ($T_{1/2} = 4.0\,\text{h}$).
**Principle:** In every half-life half of the nuclei remaining at that time decay, not half of the original ones. Decay neither stops nor speeds up, because a nucleus has no memory and its decay probability stays the same.
**Model answer:** The correct statement is the one according to which one quarter of the nuclei remain, because each half-life removes half of those remaining at that time. After the first $4.0\,\text{h}$ a fraction $\tfrac{1}{2}$ of the original nuclei remains, and after the second $\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}$.

The statement that all have decayed is an error, because the second half-life removes only half of what was left. The statement that decay stops is wrong, because the remaining nuclei still decay with the same probability. The statement about the effect of age is wrong, because the decay probability of a nucleus does not depend on its age.

## fy8-9-L1-07
**Given:** half-life $T_{1/2} = 28.8\,\text{a}$, time $t = 144\,\text{a}$
**Asked:** the fraction $\tfrac{N}{N_0}$ of undecayed nuclei as a percentage
**Principle:** Every half-life halves the number of undecayed nuclei, so the fraction is $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$.
**Formula:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** None are needed: the time and the half-life are both in years, so their ratio is a pure number. Finally the fraction is converted to a percentage by multiplying by $100$.
**Substitution:** $\dfrac{N}{N_0} = \left(\tfrac{1}{2}\right)^{144\,\text{a} : 28.8\,\text{a}} = \left(\tfrac{1}{2}\right)^{5.00} = \tfrac{1}{32} = 0.03125 = 3.125\,\%$
**Answer:** $3.13\,\%$, three significant figures like the given values.
**Reasonableness:** After five half-lives the fraction has been halved five times: $100\,\% \to 50\,\% \to 25\,\% \to 12.5\,\% \to 6.25\,\% \to 3.125\,\%$. The sample is not empty, but only a small fraction of it is left.

## fy8-9-L1-08
**Given:** half-life $T_{1/2} = 5.27\,\text{a}$, activity $A = 0.100\,A_0$
**Asked:** the time $t$ in years
**Principle:** The activity follows the decay law, $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$. The wanted time is in the exponent, so it is solved using a logarithm.
**Formula:** $\dfrac{A}{A_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \ln 2$ and $t = T_{1/2} \cdot \dfrac{\ln (A_0 / A)}{\ln 2}$
**Conversions:** None are needed: $\tfrac{A_0}{A} = \tfrac{1}{0.100} = 10.0$ is a pure number, and the time is obtained in the same unit as the half-life, that is, in years.
**Substitution:** $t = 5.27\,\text{a} \cdot \dfrac{\ln 10.0}{0.69315} = 5.27\,\text{a} \cdot \dfrac{2.3026}{0.69315} = 5.27\,\text{a} \cdot 3.3219 = 17.51\,\text{a}$
**Answer:** $17.5\,\text{a}$, three significant figures like the half-life $5.27\,\text{a}$.
**Reasonableness:** After three half-lives the activity is $\tfrac{1}{8} = 12.5\,\%$ and after four $\tfrac{1}{16} = 6.25\,\%$. The time at which the activity is $10\,\%$ lies between these: $3.32$ half-lives, that is, $3.32 \cdot 5.27\,\text{a} \approx 17.5\,\text{a}$.

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

## fy8-9-L2-05
**Given:** pulse counts in $10\,\text{s}$ intervals in the table, background $8$ pulses per $10\,\text{s}$ interval
**Asked:** the half-life $T_{1/2}$ in seconds
**Principle:** The counter counts the pulses of both the sample and the background. Only the contribution of the sample decreases according to the decay law, so the background is subtracted first. The measurement points vary at random, so the half-life is read through two points that are far apart.
**Formula:** $\dfrac{R}{R_0} = \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $T_{1/2} = \dfrac{t \ln 2}{\ln (R_0 / R)}$, where $R_0$ and $R$ are the net pulse counts
**Conversions:** a) The net pulse counts are $291 - 8 = 283$, $250 - 8 = 242$, $204 - 8 = 196$, $178 - 8 = 170$, $143 - 8 = 135$, $126 - 8 = 118$, $103 - 8 = 95$, $90 - 8 = 82$, $72 - 8 = 64$, $66 - 8 = 58$ and $51 - 8 = 43$ ($t = 0, 40, \ldots, 400\,\text{s}$). The unit of time is the second, like in the answer, so no other conversions are needed.
**Substitution:** b) At the start $R_0 = 283$ and at $t = 320\,\text{s}$ $R = 64$. The ratio is $\tfrac{283}{64} = 4.42$, that is, slightly over two half-lives ($2^2 = 4$), and $64$ is about $23\,\%$ of $283$. Thus $T_{1/2} = \dfrac{320\,\text{s} \cdot 0.69315}{\ln 4.42} = \dfrac{221.8\,\text{s}}{1.4865} = 149.2\,\text{s}$
**Answer:** $149\,\text{s}$, that is, about $150\,\text{s}$. The accuracy of an estimate from two points is about $\pm 8\,\%$, because the scatter of the net count $64$ is about $\sqrt{64} = 8$.
**Reasonableness:** Half of the initial value is $\tfrac{283}{2} = 141.5$. In the table the net pulse count is $170$ at $120\,\text{s}$ and $135$ at $160\,\text{s}$, so the halving happens at about $150\,\text{s}$. This fits the result. The points are not exactly on the curve, because the pulse counts vary at random.

## fy8-9-L2-06
**Given:** pulse counts of the table in $10\,\text{s}$ intervals, background $20$ pulses per $10\,\text{s}$ interval, the student’s result $70\,\text{s}$
**Asked:** a) the half-life $T_{1/2}$ in seconds, b) why the student’s result is too large
**Principle:** Only the net pulse count caused by the sample decreases according to the decay law. The background stays the same throughout the measurement, so it must be subtracted before looking for the halving.
**Formula:** $R = R_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so after two half-lives $R = \tfrac{R_0}{4}$, where $R_0$ and $R$ are the net pulse counts
**Conversions:** The net pulse counts are $200 - 20 = 180$, $148 - 20 = 128$, $108 - 20 = 88$, $84 - 20 = 64$, $65 - 20 = 45$, $50 - 20 = 30$ and $43 - 20 = 23$ ($t = 0, 30, \ldots, 180\,\text{s}$). No other conversions: the time is in seconds, like in the answer.
**Substitution:** a) At the start $R_0 = 180$, and a quarter of it is $\tfrac{180}{4} = 45$. It is reached at the moment $t = 120\,\text{s}$, so $2\,T_{1/2} = 120\,\text{s}$ and $T_{1/2} = \dfrac{120\,\text{s}}{2} = 60\,\text{s}$.
**Answer:** $60\,\text{s}$, two significant figures. Check: the net count has halved by the time $60\,\text{s}$, because at that point it is $88$ and half of the initial value is $90$.
**Reasonableness:** a) The result $60\,\text{s}$ fits the table: the net count $88$ is close to half of the initial value, $90$.

**Explanation of part b):** The student halved the measured total pulse count $200$. Of this, $20$ pulses are background, which does not decay, so the total count does not halve in the same time as the net count: when the net count is $90$, the total count is still $110$. The measured count reaches the value $100$ only later, at about $70\,\text{s}$, and the result is too large. The background slows the decrease of the total pulse count and moves the halving of the total count to a later time.

## fy8-9-L2-07
**Given:** the sum of the background pulse counts $80$ in ten $10\,\text{s}$ intervals, $340$ pulses in one $10\,\text{s}$ interval with the sample, number of intervals $n = 10$
**Asked:** the net pulse rate $R$ in pulses per second (and a) the mean of the background, c) the relative scatter)
**Principle:** The counter counts the pulses of both the background and the sample. The contribution of the sample itself is obtained by subtracting the average background from the total count. The pulse count is random, and its scatter is approximately $\sqrt{N}$.
**Formula:** The mean of the background $N_\text{bg} = \dfrac{\text{sum}}{n}$, the net pulse count $N_\text{net} = N - N_\text{bg}$ and the pulse rate $R = \dfrac{N_\text{net}}{\Delta t}$
**Conversions:** The length of an interval is $\Delta t = 10\,\text{s}$, so the pulse count is divided by ten to get pulses per second.
**Substitution:** a) The sum of the background pulse counts is $80$, so the mean is $N_\text{bg} = \dfrac{80}{10} = 8.0$ pulses in $10\,\text{s}$. b) $N_\text{net} = 340 - 8.0 = 332$ and $R = \dfrac{332}{10\,\text{s}} = 33.2\,\tfrac{1}{\text{s}}$. c) The scatter is $\sqrt{340} = 18.4$, so the relative scatter is $\dfrac{18.4}{340} = 0.0542 = 5.4\,\%$.
**Answer:** $33.2\,\tfrac{1}{\text{s}}$, three significant figures like the net pulse count $332$.
**Reasonableness:** The variation of the background of $5$–$11$ pulses means a deviation of at most about $\pm 3$ pulses from the mean $8.0$. That is under one percent of the pulse count $340$, whereas the scatter of the sample’s own pulse count is about $18$ pulses. The randomness of the sample measurement dominates the uncertainty, and the variation of the background does not change the net result significantly.

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

## fy8-9-L3-04
**Given:** $T_{1/2} = 6.0\,\text{h}$ of the shorter-lived nuclide, total activity in the table, $A = A_1 + A_2$
**Asked:** a) the half-life of the longer-lived nuclide in days, b) its initial activity and the share of the shorter-lived nuclide at the start, c) the check of $6.0\,\text{h}$
**Principle:** Each nuclide follows its own decay law, and the total activity is their sum. The activity of the shorter-lived one has dropped almost to zero in the last measurements: at $96\,\text{h}$ there have passed $\tfrac{96}{6.0} = 16$ half-lives, and $\left(\tfrac{1}{2}\right)^{16} \approx 1.5 \cdot 10^{-5}$. So the late points describe only the longer-lived nuclide.
**Formula:** $\dfrac{A_2(t_2)}{A_2(t_1)} = \left(\tfrac{1}{2}\right)^{(t_2 - t_1)/T_2}$, so $T_2 = \dfrac{(t_2 - t_1) \ln 2}{\ln \left(A_2(t_1) / A_2(t_2)\right)}$
**Conversions:** The points $t_1 = 96\,\text{h}$ and $t_2 = 168\,\text{h}$ are $\Delta t = 72\,\text{h}$ apart. The result is converted to days by dividing by $24\,\tfrac{\text{h}}{\text{d}}$.
**Substitution:** a) $A(96\,\text{h}) = 71.2\,\text{MBq}$ and $A(168\,\text{h}) = 32.8\,\text{MBq}$, so $T_2 = \dfrac{72\,\text{h} \cdot 0.69315}{\ln (71.2 : 32.8)} = \dfrac{49.907\,\text{h}}{0.7752} = 64.38\,\text{h} = \dfrac{64.38\,\text{h}}{24\,\text{h/d}} = 2.683\,\text{d}$. b) The activity at the moment $t = 0$ is $A_2(0) = 71.2\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{-96/64.38} = 71.2\,\text{MBq} \cdot 2^{1.491} = 71.2\,\text{MBq} \cdot 2.811 = 200\,\text{MBq}$. The total activity at the start is $1000\,\text{MBq}$, so the activity of the shorter-lived nuclide is $1000\,\text{MBq} - 200\,\text{MBq} = 800\,\text{MBq}$, that is, $80\,\%$ of the total activity. c) At $12\,\text{h}$ the activity of the longer-lived nuclide is $200\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{12/64.38} = 200\,\text{MBq} \cdot 0.879 = 175.8\,\text{MBq}$. The activity of the shorter-lived one is then $376\,\text{MBq} - 175.8\,\text{MBq} = 200.2\,\text{MBq}$. The initial activity $800\,\text{MBq}$ has halved twice ($12\,\text{h} = 2 \cdot 6.0\,\text{h}$): $\tfrac{800\,\text{MBq}}{4} = 200\,\text{MBq}$, which matches.
**Answer:** $2.68\,\text{d}$, three significant figures like the activities of the table.
**Reasonableness:** The result $2.68\,\text{d} = 64.4\,\text{h}$ is much longer than $6.0\,\text{h}$, as the task requires. With a third pair of points the result stays the same: $A(120\,\text{h}) = 55.9\,\text{MBq}$ and $A(168\,\text{h}) = 32.8\,\text{MBq}$ give $T_2 = \tfrac{48\,\text{h} \cdot 0.69315}{\ln 1.704} = 62.4\,\text{h} \approx 2.6\,\text{d}$, which is close to the result, considering the random variation of the measurement points.

## fy8-9-L3-05
**Given:** iodine-131 activity of the body in the table ($400\,\text{MBq} \to 65.5\,\text{MBq}$ in eight days), physical half-life $T_\text{phys} = 8.02\,\text{d}$, $\lambda_\text{eff} = \lambda_\text{phys} + \lambda_\text{bio}$
**Asked:** a) the effective half-life $T_\text{eff}$, b) the biological half-life $T_\text{bio}$ in days, c) the remaining fraction with physical decay alone and which process decreases the activity faster
**Principle:** The measured activity decreases according to the decay law with the effective half-life, because both decay and removal reduce the iodine in the body. The decay constants are added, and $\lambda = \tfrac{\ln 2}{T_{1/2}}$ gives the half-lives. The biological constant is obtained by subtracting the physical one from the total.
**Formula:** $T_\text{eff} = \dfrac{t \ln 2}{\ln (A_0 / A)}$ and $\lambda_\text{bio} = \lambda_\text{eff} - \lambda_\text{phys}$, that is, $\dfrac{1}{T_\text{bio}} = \dfrac{1}{T_\text{eff}} - \dfrac{1}{T_\text{phys}}$
**Conversions:** All times are in days, so no unit conversions are needed. The equation $\lambda = \tfrac{\ln 2}{T_{1/2}}$ divided by $\ln 2$ gives $\tfrac{1}{T_\text{bio}} = \tfrac{1}{T_\text{eff}} - \tfrac{1}{T_\text{phys}}$.
**Substitution:** a) $T_\text{eff} = \dfrac{8.0\,\text{d} \cdot 0.69315}{\ln (400 : 65.5)} = \dfrac{5.545\,\text{d}}{1.8092} = 3.065\,\text{d}$. b) $\dfrac{1}{T_\text{bio}} = \dfrac{1}{3.065\,\text{d}} - \dfrac{1}{8.02\,\text{d}} = 0.3263\,\tfrac{1}{\text{d}} - 0.1247\,\tfrac{1}{\text{d}} = 0.2016\,\tfrac{1}{\text{d}}$, so $T_\text{bio} = \dfrac{1}{0.2016\,\tfrac{1}{\text{d}}} = 4.96\,\text{d}$. c) With decay alone the remaining fraction would be $100\,\% \cdot \left(\tfrac{1}{2}\right)^{8.0/8.02} = 100\,\% \cdot 0.5008 = 50.1\,\%$. The measured fraction is $\tfrac{65.5}{400} = 16.4\,\%$. Both processes act on all nuclei, so the faster process is the one with the greater decay constant: $\lambda_\text{bio} = \tfrac{0.69315}{4.96\,\text{d}} = 0.140\,\tfrac{1}{\text{d}}$ and $\lambda_\text{phys} = \tfrac{0.69315}{8.02\,\text{d}} = 0.0864\,\tfrac{1}{\text{d}}$.
**Answer:** $T_\text{bio} = 4.96\,\text{d}$, three significant figures like the values of the table.
**Reasonableness:** The biological half-life is shorter than the physical one, so removal is the faster process and the effective time is shorter than either: $3.07\,\text{d} < 4.96\,\text{d} < 8.02\,\text{d}$. Check: $\lambda_\text{eff} = \tfrac{0.69315}{3.065\,\text{d}} = 0.2262\,\tfrac{1}{\text{d}}$ and $\lambda_\text{phys} + \lambda_\text{bio} = 0.0864\,\tfrac{1}{\text{d}} + 0.1398\,\tfrac{1}{\text{d}} = 0.2262\,\tfrac{1}{\text{d}}$. On the basis of part c), biological removal decreases the iodine-131 activity of the body faster than physical decay, because $\lambda_\text{bio} > \lambda_\text{phys}$. Together they leave only $16.4\,\%$ and not the $50.1\,\%$ of decay alone.
