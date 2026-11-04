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
