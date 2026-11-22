VERDICT: PASS
CONTENT-HASH: d5f34c806d597277

## Blocking

## Polish
- $\sqrt{2000}/2000 \approx 2.2\,\%$; "about $2\,\%$" is acceptable, "about $2.2\,\%$" would match the first figure's precision ($7.1\,\%$ shown as $7\,\%$). Not blocking.

## Vanhan sisällön löydökset
None.

## Checked
batch delta review: Pysähdy box at line 977 only. The previous round's Blocking finding (the $\sqrt{N}$ rule used but not given) is fixed: the answer now states that the random variation is roughly the square root of the expected count. Recomputed: $0.040 \cdot 5000 = 200$, $0.040 \cdot 50\,000 = 2000$, $\sqrt{200} = 14.1$ ($7.1\,\%$), $\sqrt{2000} = 44.7$ ($2.2\,\%$). The conclusion (the relative scatter falls as $1/\sqrt{N}$, so the larger run's share is closer to $4\,\%$) is right and fits the lesson's probability interpretation. "Roughly" is a fair level C simplification of Poisson/binomial scatter ($\sqrt{Np(1-p)} \approx \sqrt{Np}$ for $p = 0.04$).
