## fy8-14-L1-01
**Given:** thickness of soft tissue $d = 6.8\,\text{cm}$, half-value thickness $d_{1/2} = 3.4\,\text{cm}$
**Asked:** the share of the radiation that gets through ${I : I_0}$ as a percentage
**Principle:** Each layer of one half-value thickness lets through half of the X-radiation entering it, because every photon has the same probability of interacting in each layer.
**Formula:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, so $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$
**Conversions:** Not needed: the thickness and the half-value thickness are both in centimetres. At the end the share is converted to a percentage by multiplying by $100\,\%$.
**Substitution:** $\dfrac{I}{I_0} = \left(\tfrac{1}{2}\right)^{6.8\,\text{cm} / 3.4\,\text{cm}} = \left(\tfrac{1}{2}\right)^{2} = 0.25 = 25\,\%$
**Answer:** $25\,\%$, two significant figures like the thicknesses $6.8\,\text{cm}$ and $3.4\,\text{cm}$.
**Reasonableness:** The layer is exactly two half-value thicknesses: the first halves the radiation to $50\,\%$ and the second to $25\,\%$. The radiation weakens but does not disappear, as is typical of photon radiation.

## fy8-14-L1-02
**Given:** initial activity $A_0 = 600\,\text{MBq}$, half-life $T_{1/2} = 6.01\,\text{h}$, time $t = 24.0\,\text{h}$
**Asked:** the activity $A$ at time $t$ in megabecquerels
**Principle:** Activity is proportional to the number of undecayed nuclei, so it decreases according to the decay law: every half-life halves it. The problem assumes that nothing leaves the body, so only decay reduces the activity.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** Not needed: the time and the half-life are both in hours.
**Substitution:** $A = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{24.0\,\text{h} / 6.01\,\text{h}} = 600\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{3.9933} = 600\,\text{MBq} \cdot 0.062789 = 37.67\,\text{MBq}$
**Answer:** $38\,\text{MBq}$, two significant figures, because the activity $600\,\text{MBq}$ is given with two or three significant figures.
**Reasonableness:** In a day almost exactly four half-lives pass, and $600\,\text{MBq} : 16 = 37.5\,\text{MBq}$. In reality the activity is even smaller, because part of the tracer leaves in the urine.

## fy8-14-L1-03
**Given:** injected activity $A = 300\,\text{MBq}$, dose per megabecquerel $0.019\,\tfrac{\text{mSv}}{\text{MBq}}$
**Asked:** the patient's effective dose $H_\text{E}$ in millisieverts
**Principle:** Every injected megabecquerel decays in the body in the same way and gives the same dose, so the effective dose is directly proportional to the injected activity.
**Formula:** $H_\text{E} = 0.019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot A$
**Conversions:** Not needed: the activity is in megabecquerels, and the unit of the coefficient is millisieverts per megabecquerel.
**Substitution:** $H_\text{E} = 0.019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot 300\,\text{MBq} = 5.7\,\text{mSv}$
**Answer:** $5.7\,\text{mSv}$, two significant figures like the coefficient $0.019\,\tfrac{\text{mSv}}{\text{MBq}}$.
**Reasonableness:** Estimate: $0.02 \cdot 300 = 6$. The dose is of the same order of magnitude as the average annual dose from natural radiation in Finland, $5.1\,\text{mSv}$, which agrees with the value of about $6\,\text{mSv}$ in the chapter's dose table.

## fy8-14-L1-04
**Given:** mass of the tumour $m = 50\,\text{g}$, absorbed dose $D = 2.0\,\text{Gy}$
**Asked:** the energy $E$ absorbed by the tumour in joules
**Principle:** The absorbed dose is the energy absorbed by tissue per unit mass (chapter *Radiation dose and radiation safety in Finland*), so the energy is the dose times the mass.
**Formula:** $D = \dfrac{E}{m}$, so $E = D m$
**Conversions:** $1\,\text{Gy} = 1\,\tfrac{\text{J}}{\text{kg}}$ and $m = 50\,\text{g} = 50 \cdot 0.001\,\text{kg} = 0.050\,\text{kg}$
**Substitution:** $E = 2.0\,\tfrac{\text{J}}{\text{kg}} \cdot 0.050\,\text{kg} = 0.10\,\text{J}$
**Answer:** $0.10\,\text{J}$, two significant figures like the dose $2.0\,\text{Gy}$ and the mass $50\,\text{g}$.
**Reasonableness:** The energy is very small: it would warm the tumour by only about $0.0005\,\text{K}$. The effect is based on the energy arriving as ionisations that break DNA, not on warming.

## fy8-14-L1-05
**Given:** initial activity $A_0 = 37\,\text{kBq}$, half-life of americium-241 $T_{1/2} = 432\,\text{a}$, time $t = 100\,\text{a}$
**Asked:** the activity $A$ in kilobecquerels
**Principle:** Activity is proportional to the number of undecayed nuclei and therefore decreases according to the decay law. The source in a smoke detector is sealed, so no substance leaves except by decaying.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$
**Conversions:** Not needed: the time and the half-life are both in years.
**Substitution:** $A = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{100\,\text{a} / 432\,\text{a}} = 37\,\text{kBq} \cdot \left(\tfrac{1}{2}\right)^{0.23148} = 37\,\text{kBq} \cdot 0.85176 = 31.52\,\text{kBq}$
**Answer:** $32\,\text{kBq}$, two significant figures like the activity $37\,\text{kBq}$.
**Reasonableness:** One hundred years is less than a quarter of the half-life, so the activity does not have time to halve but decreases to clearly more than $50\,\%$: it decreased by about $15\,\%$. This is why the source of a smoke detector works for the whole lifetime of the device.

## fy8-14-L2-01
**Given:** carbon activity of a living tree $A_0 = 0.23\,\text{Bq}$ per gram, activity of the find $A = 0.029\,\text{Bq}$ per gram, half-life of carbon-14 $T_{1/2} = 5700\,\text{a}$
**Asked:** the age $t$ of the charcoal in years
**Principle:** A living tree keeps the share of carbon-14 in its carbon the same as in the atmosphere. When the tree dies, no new carbon-14 arrives, and the activity per gram decreases according to the decay law. To solve for the age, the time in the exponent is solved with a logarithm.
**Formula:** $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $\dfrac{A_0}{A} = 2^{t/T_{1/2}}$. We take the natural logarithm of both sides and use the rule $\ln 2^{x} = x \ln 2$: $\ln \dfrac{A_0}{A} = \dfrac{t}{T_{1/2}} \cdot \ln 2$, so $t = T_{1/2} \cdot \dfrac{\ln (A_0 : A)}{\ln 2}$
**Conversions:** Not needed: the activities are in the same unit, so their ratio is a pure number, and the age is obtained in years like the half-life.
**Substitution:** $t = 5700\,\text{a} \cdot \dfrac{\ln (0.23 : 0.029)}{\ln 2} = 5700\,\text{a} \cdot \dfrac{\ln 7.931}{0.69315} = 5700\,\text{a} \cdot \dfrac{2.0708}{0.69315} = 5700\,\text{a} \cdot 2.9875 = 17\,029\,\text{a}$
**Answer:** $1.7 \cdot 10^{4}\,\text{a}$, that is, about $17\,000$ years, two significant figures like the activities $0.23\,\text{Bq}$ and $0.029\,\text{Bq}$.
**Reasonableness:** The activity has decreased to about an eighth, and $\left(\tfrac{1}{2}\right)^3 = \tfrac{1}{8}$, so almost three half-lives have passed: $3 \cdot 5700\,\text{a} = 17\,100\,\text{a}$. The age is below the limit of radiocarbon dating, about $50\,000$ years.

## fy8-14-L2-02
**Given:** count rate without the strip $I_0 = 1200\,\tfrac{1}{\text{s}}$, with the strip $I = 900\,\tfrac{1}{\text{s}}$ (background subtracted), half-value thickness of steel $d_{1/2} = 0.73\,\text{mm}$
**Asked:** the thickness $d$ of the strip in millimetres
**Principle:** The intensity of photon radiation is attenuated in steel according to the half-value thickness, and the net count rate of the detector is proportional to the intensity of the radiation reaching it. The ratio of the count rates is therefore the same as the ratio of the intensities.
**Formula:** $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, so $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$. We take the natural logarithm of both sides and use the rule $\ln 2^{x} = x \ln 2$: $\ln \dfrac{I_0}{I} = \dfrac{d}{d_{1/2}} \cdot \ln 2$, so $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Conversions:** Not needed: the count rates are in the same unit, and the thickness is obtained in millimetres like the half-value thickness.
**Substitution:** $d = 0.73\,\text{mm} \cdot \dfrac{\ln (1200 : 900)}{\ln 2} = 0.73\,\text{mm} \cdot \dfrac{0.28768}{0.69315} = 0.73\,\text{mm} \cdot 0.41504 = 0.3030\,\text{mm}$
**Answer:** $0.30\,\text{mm}$, two significant figures like the half-value thickness $0.73\,\text{mm}$.
**Reasonableness:** The strip lets through $900 : 1200 = 75\,\%$, which is more than half, so the strip must be thinner than one half-value thickness, $0.73\,\text{mm}$. If the strip gets thicker, the count rate decreases, and the gauge controls the roll to make it thinner.

## fy8-14-L2-03
**Given:** dose of a CT examination $H = 8.0\,\text{mSv}$, dose from natural radiation $5.1\,\text{mSv}$ a year, $365$ days in a year
**Asked:** the time $t$ in days in which natural radiation gives the same dose
**Principle:** The dose from natural radiation accumulates on average evenly through the year, so the dose is directly proportional to time: the dose is the dose rate times the time.
**Formula:** $H = \dot{H} t$, so $t = \dfrac{H}{\dot{H}}$
**Conversions:** The dose rate is converted to per day by substituting $1\,\text{a} = 365\,\text{d}$: $\dot{H} = \tfrac{5.1\,\text{mSv}}{1\,\text{a}} = \tfrac{5.1\,\text{mSv}}{365\,\text{d}}$
**Substitution:** $t = \dfrac{8.0\,\text{mSv}}{5.1\,\text{mSv} : 365\,\text{d}} = \dfrac{8.0}{5.1} \cdot 365\,\text{d} = 1.5686 \cdot 365\,\text{d} = 572.5\,\text{d}$
**Answer:** about $570\,\text{d}$, two significant figures like the doses $8.0\,\text{mSv}$ and $5.1\,\text{mSv}$.
**Reasonableness:** The dose of the CT examination is slightly larger than the annual dose from natural radiation, so the time must be a little over a year: $572\,\text{d}$ is about a year and a half. The dose is significant, and this is why a CT examination must be justified.

## fy8-14-L2-04
**Given:** dose rate $\dot{H}_1 = 30\,\mu\text{Sv/h}$ at a distance $r_1 = 1.0\,\text{m}$, the nurse's distance $r_2 = 0.50\,\text{m}$, time $t = 5.0\,\text{min}$
**Asked:** the nurse's dose $H$ in microsieverts
**Principle:** The patient is treated as a point source, so the dose rate is inversely proportional to the square of the distance (chapter *Radiation dose and radiation safety in Finland*). The dose rate stays constant during this time, so the dose is the dose rate times the time.
**Formula:** $\dot{H}_2 = \dot{H}_1 \left(\tfrac{r_1}{r_2}\right)^2$ and $H = \dot{H}_2 t$, so $H = \dot{H}_1 \left(\dfrac{r_1}{r_2}\right)^2 t$
**Conversions:** $t = 5.0\,\text{min} = 5.0 \cdot \tfrac{1}{60}\,\text{h} = 0.08333\,\text{h}$
**Substitution:** $H = 30\,\mu\text{Sv/h} \cdot \left(\dfrac{1.0\,\text{m}}{0.50\,\text{m}}\right)^2 \cdot 0.08333\,\text{h} = 30\,\mu\text{Sv/h} \cdot 4 \cdot 0.08333\,\text{h} = 120\,\mu\text{Sv/h} \cdot 0.08333\,\text{h} = 10\,\mu\text{Sv}$
**Answer:** $10\,\mu\text{Sv}$, two significant figures like the dose rate $30\,\mu\text{Sv/h}$ and the time $5.0\,\text{min}$.
**Reasonableness:** Halving the distance quadruples the dose rate to $120\,\mu\text{Sv/h}$, and five minutes is a twelfth of an hour: $120 : 12 = 10$. At a distance of a metre the nurse would receive only $2.5\,\mu\text{Sv}$ in the same time, so distance is an effective protection.

## fy8-14-L3-01
**Given:** $30$ treatment sessions, dose to the tumour per session $2.0\,\text{Gy}$, $5$ beams, each giving the same share to the tumour, the dose at the entry point is $1.3$ times the beam's dose to the tumour
**Asked:** the total dose $D$ to healthy tissue at the entry point of one beam, in grays
**Principle:** The doses of the beams add up only where the beams intersect, that is, in the tumour. Only one beam passes through the entry point, so it receives only the dose of this beam, which is $1.3$ times the dose the beam gives to the tumour. The doses of the sessions are added together.
**Formula:** the tumour dose of one beam is $\tfrac{2.0\,\text{Gy}}{5}$, so $D = 30 \cdot 1.3 \cdot \dfrac{D_\text{session}}{5}$, where $D_\text{session} = 2.0\,\text{Gy}$
**Conversions:** Not needed: all doses are in grays.
**Substitution:** $D = 30 \cdot 1.3 \cdot \dfrac{2.0\,\text{Gy}}{5} = 30 \cdot 1.3 \cdot 0.40\,\text{Gy} = 30 \cdot 0.52\,\text{Gy} = 15.6\,\text{Gy}$
**Answer:** about $16\,\text{Gy}$, two significant figures like the factor $1.3$ and the dose $2.0\,\text{Gy}$.
**Reasonableness:** The tumour receives $30 \cdot 2.0\,\text{Gy} = 60\,\text{Gy}$ in total, and healthy tissue at the entry point about a quarter of that. With one beam the entry point would receive $1.3 \cdot 60\,\text{Gy} = 78\,\text{Gy}$, more than the tumour, so several directions are necessary.

## fy8-14-L3-02
**Given:** half-value thickness of soft tissue $d_{1/2}^\text{tissue} = 1.8\,\text{cm}$, of a calcification $d_{1/2}^\text{bone} = 0.27\,\text{cm}$, thickness of the replaced layer $d = 1.0\,\text{cm}$
**Asked:** the ratio of the intensities ${I_\text{A} : I_\text{B}}$, when beam A passes through soft tissue alone and beam B through a calcification
**Principle:** The beams are equally long and otherwise pass through the same soft tissue, so the shares from the other layers are the same for both and cancel from the ratio. The difference comes only from the $1.0\,\text{cm}$ layer: for beam A it is soft tissue, for beam B calcification. The shares that get through the layers are multiplied.
**Formula:** $\dfrac{I_\text{A}}{I_\text{B}} = \dfrac{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{tissue}}}{\left(\tfrac{1}{2}\right)^{d/d_{1/2}^\text{bone}}} = 2^{d/d_{1/2}^\text{bone} - d/d_{1/2}^\text{tissue}}$
**Conversions:** Not needed: all thicknesses are in centimetres.
**Substitution:** $\dfrac{I_\text{A}}{I_\text{B}} = 2^{1.0\,\text{cm} / 0.27\,\text{cm} - 1.0\,\text{cm} / 1.8\,\text{cm}} = 2^{3.7037 - 0.5556} = 2^{3.1481} = 8.87$
**Answer:** about $8.9$, two significant figures like the half-value thicknesses $1.8\,\text{cm}$ and $0.27\,\text{cm}$.
**Reasonableness:** The calcification is about $3.7$ half-value thicknesses, whereas soft tissue would have been about $0.56$, so beam B is halved about three more times: $2^3 = 8$. At low energy the contrast is large, and this is why even small calcifications show up in mammography.

## fy8-14-L3-03
**Given:** half-value thickness of lead for photons of $511\,\text{keV}$ $d_{1/2} = 3.9\,\text{mm}$, share that gets through ${I : I_0} = 5.0\,\% = 0.050$
**Asked:** the thickness $d$ of the lead shield in millimetres
**Principle:** Each half-value thickness halves the intensity of photon radiation, so the attenuation follows the equation $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$. The thickness is in the exponent, so it is solved with a logarithm.
**Formula:** $\dfrac{I_0}{I} = 2^{d/d_{1/2}}$. We take the natural logarithm of both sides and use the rule $\ln 2^{x} = x \ln 2$: $\ln \dfrac{I_0}{I} = \dfrac{d}{d_{1/2}} \cdot \ln 2$, so $d = d_{1/2} \cdot \dfrac{\ln (I_0 : I)}{\ln 2}$
**Conversions:** $5.0\,\% = 0.050$, so ${I_0 : I} = {1 : 0.050} = 20$. The thickness is obtained in millimetres like the half-value thickness.
**Substitution:** $d = 3.9\,\text{mm} \cdot \dfrac{\ln 20}{\ln 2} = 3.9\,\text{mm} \cdot \dfrac{2.9957}{0.69315} = 3.9\,\text{mm} \cdot 4.3219 = 16.86\,\text{mm}$
**Answer:** about $17\,\text{mm}$, two significant figures like the half-value thickness $3.9\,\text{mm}$ and the share $5.0\,\%$.
**Reasonableness:** Four half-value thicknesses would let through $\tfrac{1}{16} \approx 6.3\,\%$ and five $\tfrac{1}{32} \approx 3.1\,\%$, so the thickness must be between $4 \cdot 3.9\,\text{mm} = 15.6\,\text{mm}$ and $5 \cdot 3.9\,\text{mm} = 19.5\,\text{mm}$. For the $140\,\text{keV}$ photons of technetium-$99\text{m}$, the same attenuation would need only about $1\,\text{mm}$ of lead, because their half-value thickness is about $0.26\,\text{mm}$.

## fy8-14-L1-06
**Asked:** why a tracer that emits positrons is suited to locating the source from outside the body.
**Principle:** A positron is a charged particle, so it stops in the tissue within a few millimetres and annihilates with an electron. At that moment its momentum is almost zero, so the annihilation produces two photons that leave in opposite directions and have the same energy $E_\gamma = m_e c^2 = 511\,\text{keV}$.
**Model answer:** The positron annihilates with an electron into two photons in opposite directions, and the line segment joining them passes through the source. The detector registers the photons at the same time, and the source lies on this segment. The intersection of many segments reveals the position of the tracer. The detector does not register the positron itself, because it stops in the tissue; it is electrically charged and does not travel straight out. The energy of the photons is always $511\,\text{keV}$, so it does not tell the depth but only that an annihilation has taken place.

## fy8-14-L1-07
**Asked:** whether reducing the dose is sensible from the point of view of radiation protection when the image is noisy.
**Principle:** The principles of the use of radiation are justification, optimisation and dose limits. Optimisation does not mean the smallest possible dose at any cost but the smallest dose with which the image answers the question.
**Model answer:** The proposal is not sensible. When the dose is too small, the image stays noisy, and the small change in the lung that was being looked for cannot be seen in it. The examination has to be repeated, and the patient receives two doses instead of one. So the dose is not reduced further; instead the imaging settings are chosen so that the image is just clear enough.

## fy8-14-L1-08
**Given:** accelerating voltage $U = 80\,\text{kV}$, elementary charge $e = 1.602 \cdot 10^{-19}\,\text{C}$
**Asked:** the greatest possible energy $E_\text{max}$ of an X-ray photon in joules
**Principle:** The voltage $U$ gives the electron a kinetic energy $eU$. The greatest energy a photon can receive arises when the electron gives the photon all of its kinetic energy as it decelerates in the anode.
**Formula:** $E_\text{max} = eU$
**Conversions:** $U = 80\,\text{kV} = 80 \cdot 1000\,\text{V} = 80\,000\,\text{V}$, and $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Substitution:** $E_\text{max} = 1.602 \cdot 10^{-19}\,\text{C} \cdot 80\,000\,\text{V} = 1.2816 \cdot 10^{-14}\,\text{J}$
**Answer:** $1.3 \cdot 10^{-14}\,\text{J}$, two significant figures like the voltage $80\,\text{kV}$.
**Reasonableness:** The energy of the electron is $80\,\text{keV}$, and $80\,000 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 1.28 \cdot 10^{-14}\,\text{J}$. In imaging the energies of the photons are tens of kiloelectronvolts, so the result is of the right order of magnitude. Most photons receive less energy than this, because a decelerating electron often gives up only part of its energy.

## fy8-14-L2-05
**Given:** from the table a dental X-ray $0.010\,\text{mSv}$ three times, a chest X-ray $0.10\,\text{mSv}$ twice and a head CT $2.0\,\text{mSv}$ once; annual dose from natural radiation $H_\text{nature} = 5.1\,\text{mSv}$ (STUK-A263, 2020)
**Asked:** the share $p$ of the annual dose from natural radiation that the total dose makes up, as a percentage
**Principle:** Effective doses can be compared directly and added together, so the total dose is the dose of each examination times the number of examinations, summed. The comparison is made with a single division.
**Formula:** $H = n_1 H_1 + n_2 H_2 + n_3 H_3$ and $p = \dfrac{H}{H_\text{nature}} \cdot 100\,\%$
**Conversions:** Not needed: all doses are in millisieverts. The share is converted to a percentage by multiplying by $100\,\%$.
**Substitution:** $H = 3 \cdot 0.010\,\text{mSv} + 2 \cdot 0.10\,\text{mSv} + 1 \cdot 2.0\,\text{mSv} = 0.030\,\text{mSv} + 0.20\,\text{mSv} + 2.0\,\text{mSv} = 2.23\,\text{mSv}$
$p = \dfrac{2.23\,\text{mSv}}{5.1\,\text{mSv}} \cdot 100\,\% = 43.73\,\%$
**Answer:** $44\,\%$, two significant figures like the dose from natural radiation $5.1\,\text{mSv}$.
**Reasonableness:** The dose of the head CT, $2.0\,\text{mSv}$, is almost the whole sum, and $2.0 : 5.1 \approx 0.39$. The small images add only $0.23\,\text{mSv}$, so the whole is $(2.0 + 0.23) : 5.1 \approx 0.44$, or about $44\,\%$. The dose is less than half of the annual dose, and most of it comes from a single CT examination.

## fy8-14-L2-06
**Given:** from the table the activity $A = 500$; $355$; $252$; $123$ and $64\,\text{MBq}$ at times $t = 0.0$; $2.0$; $4.0$; $8.0$ and $12.0\,\text{h}$; half-life of the decay $T_{1/2} = 6.01\,\text{h}$
**Asked:** a) the time in which the activity in the patient halves; b) the share $p$ of the activity given by decay alone that the measured activity makes up at $12.0\,\text{h}$, as a percentage
**Principle:** The activity in the patient decreases for two reasons: the nucleus decays, and the body removes the tracer, for example in the urine. The activity given by decay alone follows the law $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$.
**Formula:** a) the halving time is read from the table; b) $A_\text{decay} = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ and $p = \dfrac{A_\text{measured}}{A_\text{decay}} \cdot 100\,\%$
**Conversions:** Not needed: the time and the half-life are both in hours, and the activities are in megabecquerels.
**Substitution:**
a) The activity $500\,\text{MBq}$ halves to about $250\,\text{MBq}$ in $4.0\,\text{h}$ (in the table $252\,\text{MBq}$), and from there to about $125\,\text{MBq}$ in the next $4.0\,\text{h}$ (in the table $123\,\text{MBq}$ at $8.0\,\text{h}$). So the halving time is about $4.0\,\text{h}$.
b) $A_\text{decay} = 500\,\text{MBq} \cdot \left(\tfrac{1}{2}\right)^{12.0\,\text{h} / 6.01\,\text{h}} = 500\,\text{MBq} \cdot 0.2506 = 125.3\,\text{MBq}$, so $p = \dfrac{64\,\text{MBq}}{125.3\,\text{MBq}} \cdot 100\,\% = 51.1\,\%$
**Answer:** b) $51\,\%$, two significant figures like the measured activity $64\,\text{MBq}$. In part a) the halving time is about $4.0\,\text{h}$, which is shorter than the half-life of the decay, because in addition to decay the tracer is removed from the body.
**Reasonableness:** Twelve hours is two half-lives for decay, so by decay alone the activity would be about $500 : 4 = 125\,\text{MBq}$, and the measured $64\,\text{MBq}$ is about half of that. Three halving times of $4.0\,\text{h}$ would give $500 : 8 = 62.5\,\text{MBq}$, which agrees with the measured value.

## fy8-14-L2-07
**Given:** share allowed through ${I : I_0} = 1.0\,\% = 0.010$, half-value thickness of lead for $511\,\text{keV}$ photons $d_{1/2} = 3.9\,\text{mm}$ and for $140\,\text{keV}$ photons $0.26\,\text{mm}$
**Asked:** the student's error and the correct thickness $d$ of the lead shield in millimetres
**Principle:** The half-value thickness depends on the energy of the photons. The shield has to stop the $511\,\text{keV}$ photons, so the calculation must use their half-value thickness, $3.9\,\text{mm}$. The student used the value $0.26\,\text{mm}$ for $140\,\text{keV}$ photons, so the shield would be too thin. Otherwise the student's number $n = 6.64$ is correct.
**Formula:** $\left(\tfrac{1}{2}\right)^{n} = \dfrac{I}{I_0}$, so $n = \dfrac{\ln (I_0 : I)}{\ln 2}$ and $d = n \, d_{1/2}$
**Conversions:** $1.0\,\% = 0.010$, so ${I_0 : I} = {1 : 0.010} = 100$. The thickness comes out in millimetres like the half-value thickness.
**Substitution:** $n = \dfrac{\ln 100}{\ln 2} = \dfrac{4.6052}{0.69315} = 6.644$ and $d = 6.644 \cdot 3.9\,\text{mm} = 25.91\,\text{mm}$
**Answer:** the correct thickness is $26\,\text{mm}$, two significant figures like the half-value thickness $3.9\,\text{mm}$. The student's result $1.7\,\text{mm}$ is wrong, because it is based on the value for the energy $140\,\text{keV}$.
**Reasonableness:** Seven half-value thicknesses would let through $\left(\tfrac{1}{2}\right)^{7} = \tfrac{1}{128} \approx 0.78\,\%$ and six $\tfrac{1}{64} \approx 1.6\,\%$, so the thickness must lie between $6 \cdot 3.9\,\text{mm} = 23.4\,\text{mm}$ and $7 \cdot 3.9\,\text{mm} = 27.3\,\text{mm}$. For $511\,\text{keV}$ photons the student's $1.7\,\text{mm}$ is only $1.7 : 3.9 \approx 0.44$ half-value thicknesses, so about $74\,\%$ would get through, not $1.0\,\%$.

## fy8-14-L3-04
**Given:** from the table mass $m = 75\,\text{kg}$, activity required at the start of imaging $a = 2.0\,\tfrac{\text{MBq}}{\text{kg}}$, waiting time $t = 60\,\text{min}$, half-life of fluorine-$18$ $T_{1/2} = 110\,\text{min}$, dose coefficient $k = 0.019\,\tfrac{\text{mSv}}{\text{MBq}}$, dose of the CT part $H_\text{CT} = 6.0\,\text{mSv}$; annual dose from natural radiation $5.1\,\text{mSv}$
**Asked:** a) the patient's total effective dose $H$ in millisieverts; b) a comparison with natural radiation and when the examination is justified
**Principle:** The activity needed for imaging, $A_\text{scan} = a m$, must remain after the waiting time, and during the wait the activity decreases only by decay. So the injected activity $A_0$ is greater than $A_\text{scan}$, and the smallest suitable value comes from the decay law. The dose depends on the injected activity, and the doses of the PET part and the CT part are added together.
**Formula:** $A_\text{scan} = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$, so $A_0 = \dfrac{a m}{\left(\tfrac{1}{2}\right)^{t/T_{1/2}}}$, and $H = k A_0 + H_\text{CT}$
**Conversions:** Not needed: the waiting time and the half-life are both in minutes, and the dose coefficient is in millisieverts per megabecquerel.
**Substitution:** $A_\text{scan} = 2.0\,\tfrac{\text{MBq}}{\text{kg}} \cdot 75\,\text{kg} = 150\,\text{MBq}$ and $\left(\tfrac{1}{2}\right)^{60\,\text{min} / 110\,\text{min}} = \left(\tfrac{1}{2}\right)^{0.5455} = 0.6853$, so $A_0 = \dfrac{150\,\text{MBq}}{0.6853} = 218.9\,\text{MBq}$. Then $H = 0.019\,\tfrac{\text{mSv}}{\text{MBq}} \cdot 218.9\,\text{MBq} + 6.0\,\text{mSv} = 4.16\,\text{mSv} + 6.0\,\text{mSv} = 10.16\,\text{mSv}$
**Answer:** a) $10\,\text{mSv}$, two significant figures like the mass $75\,\text{kg}$ and the activity $2.0\,\tfrac{\text{MBq}}{\text{kg}}$. b) The total dose is about two annual doses from natural radiation ($10.16 : 5.1 = 2.0$), so clearly greater than the annual dose. The examination is justified when the physician judges that the result settles a question about the treatment and that a method with a smaller dose would not give the same information; the benefit to the patient is then greater than the small additional risk caused by the radiation. The dose is optimised by using the smallest activity with which the imaging succeeds.
**Reasonableness:** The waiting time $60\,\text{min}$ is a little over half of the half-life, so about a third of the activity has time to decay: $150 : 0.69 \approx 217\,\text{MBq}$. This agrees with the result $218.9\,\text{MBq}$. The dose of the PET part, $4.2\,\text{mSv}$, is of the same order of magnitude as the doses of other PET examinations, and the CT part adds even more to it.

## fy8-14-L3-05
**Given:** from the table thicknesses $d = 0.0$; $5.0$; $10.0$; $15.0$ and $20.0\,\text{mm}$ and count rates $R = 1006$; $689$; $468$; $327$ and $221\,\tfrac{1}{\text{s}}$; for the unknown plate $R_x = 402\,\tfrac{1}{\text{s}}$
**Asked:** a) the ratios of the count rates; b) the half-value thickness $d_{1/2}$ of aluminium; c) the thickness $d_x$ of the unknown plate in millimetres
**Principle:** If the radiation is attenuated according to the half-value thickness, every additional layer of equal thickness reduces the count rate by the same factor. The count rate is proportional to the intensity of the radiation reaching the detector, so $R = R_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$, and the unknown thickness has to be solved with a logarithm.
**Reading the graph:** The count rates of all the plates are read from the table. In part a) the ratios are calculated: $689 : 1006 = 0.685$, $468 : 689 = 0.679$, $327 : 468 = 0.699$ and $221 : 327 = 0.676$. They are almost the same, about $0.68$, although the measurement has small random variation. So every $5.0\,\text{mm}$ of plate reduces the count rate to the same fraction, which fits exponential attenuation. In part b) the half-value thickness is calculated from the first and the last row of the table. As a check, a line fitted to all five points between $\ln R$ and $d$ gives $d_{1/2} = 9.18\,\text{mm}$ and $d_x = 12.1\,\text{mm}$, that is, the same answer.
**Formula:** $\dfrac{R_0}{R} = 2^{d/d_{1/2}}$, so $d = d_{1/2} \cdot \dfrac{\ln (R_0 : R)}{\ln 2}$. From the calibration $d_{1/2} = \dfrac{d_{20} \ln 2}{\ln (R_0 : R_{20})}$ and for the unknown plate $d_x = d_{1/2} \cdot \dfrac{\ln (R_0 : R_x)}{\ln 2}$.
**Conversions:** Not needed: the thicknesses are in millimetres, and the ratio of the count rates is a pure number.
**Substitution:** b) $d_{1/2} = \dfrac{20.0\,\text{mm} \cdot 0.69315}{\ln (1006 : 221)} = \dfrac{13.863\,\text{mm}}{1.5157} = 9.147\,\text{mm}$. c) $d_x = 9.147\,\text{mm} \cdot \dfrac{\ln (1006 : 402)}{0.69315} = 9.147\,\text{mm} \cdot \dfrac{0.9174}{0.69315} = 9.147\,\text{mm} \cdot 1.3236 = 12.11\,\text{mm}$
**Answer:** c) $12\,\text{mm}$, two significant figures, because the half-value thickness $d_{1/2}$ has been determined from a calibration in which the random variation of the measurements limits the precision to about two figures (ratios $0.68 \pm 0.01$). In part b) the half-value thickness of aluminium is $9.1\,\text{mm}$.
**Reasonableness:** The count rate $402\,\tfrac{1}{\text{s}}$ lies between the table values $468$ ($10.0\,\text{mm}$) and $327$ ($15.0\,\text{mm}$), so the thickness must lie between $10.0\,\text{mm}$ and $15.0\,\text{mm}$, and $12.1\,\text{mm}$ does. Check: $12.1\,\text{mm}$ is $12.1 : 9.147 = 1.32$ half-value thicknesses, and $1006 \cdot \left(\tfrac{1}{2}\right)^{1.32} = 403$, as the measured $402$. The result is valid only within the calibrated range, and the background radiation has to be subtracted, because it is not attenuated in the plate.

## fy8-14-L1-09
**Asked:** an expression for the initial activity $A_0$ when the activity $A$ is needed at the moment of injection and the transport takes a time $t$.
**Principle:** The activity decreases according to the law of decay, $A = A_0 \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$: every half-life halves the activity that remains. During the transport the number of half-lives is $\tfrac{t}{T_{1/2}}$, and the law is solved for the initial activity $A_0$.
**Model answer:** We divide both sides of the law of decay by the factor $\left(\tfrac{1}{2}\right)^{t/T_{1/2}}$:

$$A_0 = \frac{A}{\left(\tfrac{1}{2}\right)^{t/T_{1/2}}}$$

Because $\dfrac{1}{\left(\tfrac{1}{2}\right)^{n}} = 2^{n}$, we get

$$A_0 = A \cdot 2^{t/T_{1/2}}$$

So the correct expression is $A_0 = A \cdot 2^{t/T_{1/2}}$. Check: the half-life of fluorine-$18$ is about $110\,\text{min}$. For example, in a transport that lasts $330\,\text{min}$ the activity halves three times, and when it leaves, $2^{3} = 8$ times the activity $A$ is needed. The expression for a steady change would give only $\tfrac{2 \cdot 330}{110} = 6$ times $A$. The wrong expressions: $A \cdot \left(\tfrac{1}{2}\right)^{t/T_{1/2}}$ is smaller than $A$, so the law of decay has been used in the wrong direction. In the expression $A \cdot 2^{T_{1/2}/t}$ the exponent has been turned upside down, and it would decrease as the transport time increases. The expression $A \cdot \tfrac{2t}{T_{1/2}}$ assumes that the activity changes steadily, and at the time $t = 0$ it would give zero.
