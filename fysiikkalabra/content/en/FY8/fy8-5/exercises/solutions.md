## fy8-5-L1-01
**Given:** principal quantum number of the shell $n = 5$
**Asked:** the greatest number of electrons $N_\text{max}$ that fit in the shell
**Principle:** The shell $n$ has $n^2$ orbitals, because its subshells s, p, d, … have $1$, $3$, $5$, … orbitals. Each orbital can hold at most two electrons with opposite spins (Pauli exclusion principle), so the greatest number is twice the number of orbitals.
**Formula:** $N_\text{max} = 2n^2$
**Conversions:** None are needed, because a count is asked.
**Substitution:** $N_\text{max} = 2 \cdot 5^2 = 2 \cdot 25 = 50$
**Answer:** $50$ electrons; the result is an exact integer, because it is calculated from counts.
**Reasonableness:** The result continues the series $2, 8, 18, 32$ of the table: the differences $6$, $10$ and $14$ of successive shells grow by four, so the next difference is $18$ and $32 + 18 = 50$. So more electrons fit in the shell $n = 5$ than in the shell $n = 4$, as they should.

## fy8-5-L1-02
**Given:** measurements $N = 8000$, hits inside the nodal sphere $k = 421$
**Asked:** the probability $P$ of detecting the $2\text{s}$ electron inside the nodal sphere, as a percentage
**Principle:** According to the probability interpretation, only probabilities can be calculated from the wave, and from measurements made in many atoms in the same state the probability is estimated as the share of the hits that land in the region. The more measurements there are, the more accurate the estimate.
**Formula:** the estimate of the probability is $P = \dfrac{k}{N}$
**Conversions:** The share is converted to a percentage by multiplying by one hundred: $1 = 100\,\%$.
**Substitution:** $P = \dfrac{421}{8000} = 0.052\,625 = 5.2625\,\%$
**Answer:** $5.26\,\%$, three significant figures like the number of hits $421$.
**Reasonableness:** About every twentieth measurement lands inside the nodal sphere, since $8000 : 20 = 400$, which is close to the number $421$. The share is small, because the radius of the nodal sphere is only about $0.11\,\text{nm}$ and most of the probability of the $2\text{s}$ electron is outside it.

## fy8-5-L1-03
**Given:** measurements $N = 3000$, boundary of the orbital $90\,\%$
**Asked:** the expected number $k_\text{out}$ of measurements that land outside the boundary
**Principle:** The boundary is drawn so that the electron is detected inside it with probability $0.90$, so the probability of landing outside is $1 - 0.90 = 0.10$. In many measurements the share of those landing outside is approximately this probability, $P \approx \tfrac{k}{N}$.
**Formula:** $k_\text{out} = (1 - p)\,N$
**Conversions:** $p = 90\,\% = 0.90$
**Substitution:** $k_\text{out} = (1 - 0.90) \cdot 3000 = 0.10 \cdot 3000 = 300$
**Answer:** about $300$ measurements; the number is an expected value, and the real number varies from one series to another.
**Reasonableness:** Every tenth measurement lands outside the boundary, and a tenth of $3000$ is $300$. If the boundary were a wall, there would be no hits outside, but the boundary of an orbital is only an agreed probability boundary.

## fy8-5-L1-04
**Given:** electron in the $3\text{p}$ state, so $n = 3$; energy levels of the hydrogen atom $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$
**Asked:** the smallest energy $E_\text{i}$ needed for release, in electronvolts
**Principle:** The electron is free of the atom when its energy is at least $0$. In the hydrogen atom the energy of a state depends only on the principal quantum number, so the energy of the $3\text{p}$ state is the energy of the shell $n = 3$, and the energy needed is the difference $0 - E_3$.
**Formula:** $E_\text{i} = 0 - E_3 = \dfrac{13.6\,\text{eV}}{3^2}$
**Conversions:** None are needed, because the energy levels and the asked energy are in electronvolts.
**Substitution:** $E_\text{i} = \dfrac{13.6\,\text{eV}}{9} = 1.5111\,\text{eV}$
**Answer:** $1.51\,\text{eV}$, three significant figures like the energy $13.6\,\text{eV}$.
**Reasonableness:** On the shell $n = 3$ the electron is farther from the nucleus and more weakly bound than in the ground state, so release takes only a ninth of the ground-state energy $13.6\,\text{eV}$. The energy is positive, because it is brought into the atom.

## fy8-5-L1-05
**Given:** shell $n = 5$; energy levels of the hydrogen atom $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$
**Asked:** the energy $E_5$ of the electron in electronvolts
**Principle:** In the hydrogen atom the energy of the state of the electron depends only on the principal quantum number, and the energy levels are given by the formula. The energy is negative, because a bound electron needs energy to be released.
**Formula:** $E_5 = -\dfrac{13.6\,\text{eV}}{5^2}$
**Conversions:** None are needed, because the energy is asked in electronvolts.
**Substitution:** $E_5 = -\dfrac{13.6\,\text{eV}}{25} = -0.544\,\text{eV}$
**Answer:** $-0.544\,\text{eV}$, three significant figures like the energy $13.6\,\text{eV}$.
**Reasonableness:** The energy is close to zero, because the electron of the shell $n = 5$ is weakly bound. It is greater than $E_4 = -0.85\,\text{eV}$, as it should be, because the energy increases as the number of the shell increases.

## fy8-5-L2-01
**Given:** initial state $3\text{p}$, so $n = 3$; final state $1\text{s}$, so $n = 1$; $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Asked:** the wavelength $\lambda$ of the photon in nanometres
**Principle:** Energy is conserved: the energy of the atom decreases by the difference between the energies of the states, and the same energy leaves as a photon, whose energy is $hf = \tfrac{hc}{\lambda}$. In the hydrogen atom the energy of a state depends only on the principal quantum number.
**Formula:** $\dfrac{hc}{\lambda} = E_3 - E_1$, so $\lambda = \dfrac{hc}{E_3 - E_1}$
**Conversions:** The energy difference in electronvolts is $E_3 - E_1 = -\tfrac{13.6\,\text{eV}}{9} + 13.6\,\text{eV} = 12.089\,\text{eV}$. Substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $E_3 - E_1 = 12.089 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 1.9366 \cdot 10^{-18}\,\text{J}$. Finally $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Substitution:** First $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}$ and then $\lambda = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{1.9366 \cdot 10^{-18}\,\text{J}} = 1.0257 \cdot 10^{-7}\,\text{m} = 102.57\,\text{nm}$
**Answer:** $103\,\text{nm}$, three significant figures like the energy $13.6\,\text{eV}$.
**Reasonableness:** The energy of the photon is about $12\,\text{eV}$, more than the energy $10.2\,\text{eV}$ of the transition $2\text{p} \to 1\text{s}$, so the wavelength must be shorter than the $122\,\text{nm}$ of that transition. The radiation is ultraviolet, like all the lines of hydrogen that end in the ground state.

## fy8-5-L2-02
**Given:** argon has $18$ electrons; filling order $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$; at most two electrons per orbital
**Asked:** the number of electrons $N_\text{outer}$ in the outermost shell
**Principle:** In the ground state the electrons fill the orbitals starting from the lowest energy. At most $2n^2$ electrons fit in the shell $n$, so first the shells $n = 1$ and $n = 2$ fill, and the remaining electrons are in the shell $n = 3$, which is the outermost shell of argon.
**Formula:** $N_\text{outer} = N - 2 \cdot 1^2 - 2 \cdot 2^2$
**Conversions:** None are needed, because a count is asked.
**Substitution:** $N_\text{outer} = 18 - 2 - 8 = 8$
**Answer:** $8$ electrons; the result is an exact integer.
**Reasonableness:** On the shell $n = 3$ the electrons are in the $3\text{s}$ and $3\text{p}$ subshells: $2 + 6 = 8$, so both subshells are full. The configuration $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^6$ contains $18$ electrons. Full outermost s and p subshells fit the fact that argon is a noble gas that hardly forms bonds.

## fy8-5-L2-03
**Given:** measurements $N = 2400$; $50\,\%$ boundary $0.071\,\text{nm}$ and $90\,\%$ boundary $0.14\,\text{nm}$
**Asked:** the expected number $k$ of measurements that land between the boundaries
**Principle:** The $50\,\%$ boundary lies entirely inside the $90\,\%$ boundary, so the probability $0.90 - 0.50 = 0.40$ remains in the shell between the boundaries. In many measurements the share of those landing in a region is approximately the probability of the region. The radii of the boundaries are not needed.
**Formula:** $k = (p_{90} - p_{50})\,N$
**Conversions:** $p_{90} = 90\,\% = 0.90$ and $p_{50} = 50\,\% = 0.50$
**Substitution:** $k = (0.90 - 0.50) \cdot 2400 = 0.40 \cdot 2400 = 960$
**Answer:** about $960$ measurements; the number is an expected value, and the real number varies from one series to another.
**Reasonableness:** Half, that is $1200$ measurements, land inside the $50\,\%$ boundary and $2160$ measurements inside the $90\,\%$ boundary; their difference is $960$. There are fewer hits between the boundaries than inside the inner boundary, although the shell has a greater volume, because the cloud thins out outwards.

## fy8-5-L2-04
**Given:** electron in the shell $n = 2$; $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Asked:** the greatest wavelength $\lambda_\text{max}$ at which a photon releases the electron, in nanometres
**Principle:** The energy of the photon must be at least the energy $0 - E_2$ needed for release. The energy of a photon, $\tfrac{hc}{\lambda}$, decreases as the wavelength increases, so the greatest suitable wavelength corresponds to exactly this energy.
**Formula:** $\dfrac{hc}{\lambda_\text{max}} = 0 - E_2$, so $\lambda_\text{max} = \dfrac{hc}{-E_2}$
**Conversions:** $-E_2 = \tfrac{13.6\,\text{eV}}{4} = 3.40\,\text{eV}$. Substituting $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$: $-E_2 = 3.40 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 5.4468 \cdot 10^{-19}\,\text{J}$. Finally $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Substitution:** First $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}$ and then $\lambda_\text{max} = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{5.4468 \cdot 10^{-19}\,\text{J}} = 3.6470 \cdot 10^{-7}\,\text{m} = 364.70\,\text{nm}$
**Answer:** $365\,\text{nm}$, three significant figures like the energy $13.6\,\text{eV}$.
**Reasonableness:** The energy $3.4\,\text{eV}$ is slightly above the energy of a photon of violet light, so the wavelength is just below the visible range, near ultraviolet. Visible light with a longer wavelength does not release an electron from the shell $n = 2$.

## fy8-5-L3-01
**Given:** wavelength of the photon $\lambda = 97.3\,\text{nm}$; atom in the ground state, $n = 1$; $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$, $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$
**Asked:** the number of orbitals in the shell $n$ to which the electron moves
**Principle:** An atom can absorb a photon only if the energy of the photon is exactly the difference between the energies of two states. The energy of the photon gives the energy of the upper state, $E_n = E_1 + \tfrac{hc}{\lambda}$, from that the number of the shell $n$, and the shell $n$ has $n^2$ orbitals.
**Formula:** $E_n = E_1 + \dfrac{hc}{\lambda}$, so $n = \sqrt{\dfrac{13.6\,\text{eV}}{-E_n}}$ and the number of orbitals is $n^2$
**Conversions:** $\lambda = 97.3\,\text{nm} = 97.3 \cdot 10^{-9}\,\text{m}$. With $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}$, the energy of the photon is $\tfrac{hc}{\lambda} = \tfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{97.3 \cdot 10^{-9}\,\text{m}} = 2.0416 \cdot 10^{-18}\,\text{J}$. It is converted to electronvolts by substituting $1\,\text{J} = \tfrac{1}{1.602 \cdot 10^{-19}}\,\text{eV}$: $\tfrac{2.0416 \cdot 10^{-18}}{1.602 \cdot 10^{-19}}\,\text{eV} = 12.744\,\text{eV}$.
**Substitution:** $E_n = -13.6\,\text{eV} + 12.744\,\text{eV} = -0.856\,\text{eV}$ and $n = \sqrt{\dfrac{13.6\,\text{eV}}{0.856\,\text{eV}}} = \sqrt{15.9} = 3.99 \approx 4$, so there are $4^2 = 16$ orbitals
**Answer:** $16$ orbitals (shell $n = 4$: $4\text{s}$, three $4\text{p}$, five $4\text{d}$ and seven $4\text{f}$); $n$ is an integer, so the rounding $3.99 \to 4$ is reliable.
**Reasonableness:** The energy of the shell $n = 4$, $-\tfrac{13.6\,\text{eV}}{16} = -0.85\,\text{eV}$, equals the calculated $-0.856\,\text{eV}$ to the precision of three figures of the wavelength. The energies of the shells $n = 3$ ($-1.51\,\text{eV}$) and $n = 5$ ($-0.54\,\text{eV}$) are clearly farther away, so no other shell fits.

## fy8-5-L3-02
**Given:** filling order $1\text{s}$, $2\text{s}$, $2\text{p}$, $3\text{s}$, $3\text{p}$; at most two electrons per orbital; the $3\text{p}$ subshell is half full
**Asked:** the number of electrons $N$ in the atom
**Principle:** In the ground state the electrons fill the orbitals starting from the lowest energy, so electrons go to the $3\text{p}$ subshell only when $1\text{s}$, $2\text{s}$, $2\text{p}$ and $3\text{s}$ are full. An s subshell has one orbital and a p subshell three, so they hold $2$ and $6$ electrons. A half-full $3\text{p}$ subshell contains half of its maximum number.
**Formula:** $N = N_\text{1s} + N_\text{2s} + N_\text{2p} + N_\text{3s} + \dfrac{N_\text{3p,max}}{2}$
**Conversions:** None are needed, because a count is asked.
**Substitution:** $N = 2 + 2 + 6 + 2 + \dfrac{6}{2} = 2 + 2 + 6 + 2 + 3 = 15$
**Answer:** $15$ electrons (the element is phosphorus, configuration $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^2\,3\text{p}^3$); the result is an exact integer.
**Reasonableness:** The full shells $n = 1$ and $n = 2$ hold $2 + 8 = 10$ electrons, and the shell $n = 3$ has $2 + 3 = 5$ electrons, $15$ altogether. In the periodic table the atomic number $15$ is phosphorus, which is in the middle of the third period, as a half-full $3\text{p}$ subshell leads one to expect.

## fy8-5-L3-03
**Given:** measurements $N = 5000$; boundary of the orbital $90\,\%$; $5.3\,\%$ of the measurements land inside the nodal sphere, and this inner part belongs practically entirely to the region of the orbital
**Asked:** the expected number $k$ of measurements that land in the region of the orbital outside the nodal sphere
**Principle:** The probability $0.90$ of the region of the orbital divides into two parts: the inner part of the nodal sphere and the shell outside the nodal sphere. Since the inner part belongs entirely to the region, the probability of the outer part is the difference $0.90 - 0.053$. In many measurements the share of those landing in a region is approximately the probability of the region.
**Formula:** $k = (p - p_\text{in})\,N$
**Conversions:** $p = 90\,\% = 0.90$ and $p_\text{in} = 5.3\,\% = 0.053$
**Substitution:** $k = (0.90 - 0.053) \cdot 5000 = 0.847 \cdot 5000 = 4235$
**Answer:** about $4240$ measurements; the number is an expected value that a real series fulfils only approximately, and the share of the inner part, $5.3\,\%$, limits the precision to about two or three significant figures.
**Reasonableness:** Altogether about $0.90 \cdot 5000 = 4500$ measurements land in the region, and of these about $0.053 \cdot 5000 = 265$ inside the nodal sphere; the difference $4235$ is clearly the largest part. This fits the fact that the most common distance of the $2\text{s}$ electron is outside the nodal sphere.
