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

## fy8-5-L1-06
**Find:** what the essential difference is between an orbital of the wave-mechanical model of the atom and an orbit of the Bohr model.
**Principle:** In the wave model the state of the electron is described by a standing wave spread around the nucleus, and the wave tells how probably the electron is detected at each place. An orbital is drawn as a region inside which the electron is detected with a chosen probability, usually $90\,\%$.
**Model answer:** An orbital is not a path but a region inside which the electron is detected with a chosen probability, and no route can be drawn for the electron. In the Bohr model the electron has a precise orbit, but in the wave model a measurement always gives a single point and the orbital describes only the distribution of many measurements. The claim that an orbital is an imprecise path is wrong, because there is no path at all. A spherical surface is not acceptable, because the measurement results scatter over different distances. The cloud does not mean either that the electron is spread out into parts: in each measurement a whole electron is detected at one place.

## fy8-5-L1-07
**Find:** what the point cloud of $5000$ measurements describes.
**Principle:** According to the probability interpretation, the wave does not tell the position of a particle but how probably the particle is detected at each place. A single measurement gives one random result, and the distribution becomes visible only from many measurements.
**Model answer:** The cloud describes the distribution of the measurement results: there are the most points where the electron is most probably detected, so the cloud is densest near the nucleus. Each point is a separate measurement result independent of the others, so the points are not the route of the electron. The blurring explanation is not acceptable, because each measurement finds the electron precisely at one place, and the cloud arises only as the results accumulate. The electron does not break into pieces either, but in each measurement a whole electron is detected.

## fy8-5-L1-08
**Given:** subshell $4\text{f}$; the f subshell has seven orbitals; at most two electrons in an orbital
**Find:** the greatest number of electrons $N_\text{max}$ in the subshell $4\text{f}$
**Principle:** The number of orbitals of a subshell depends on the shape of the wave, and the f subshell has seven. An electron has spin, which has only two values, so at most two electrons with opposite spins fit in each orbital (Pauli exclusion principle). The greatest number is twice the number of orbitals.
**Formula:** $N_\text{max} = 2 \cdot N_\text{orbitals}$
**Conversions:** None are needed, because a count is asked.
**Substitution:** $N_\text{max} = 2 \cdot 7 = 14$
**Answer:** $14$ electrons; the result is an exact integer, because it is calculated from counts.
**Reasonableness:** By the same rule, $2 \cdot 1 = 2$ electrons fit in an s subshell, $2 \cdot 3 = 6$ in a p subshell and $2 \cdot 5 = 10$ in a d subshell. In the subshells s, p, d and f of the shell $n = 4$ there is room for $2 + 6 + 10 + 14 = 32$ electrons in total, and this equals $2n^2 = 2 \cdot 4^2 = 32$.

## fy8-5-L2-05
**Given:** measurements $N = 400$; class width $0.05\,\text{nm}$; counts $k$ of the classes: $118$, $171$, $79$, $23$, $7$ and $2$; radius of the $90\,\%$ boundary $0.14\,\text{nm}$
**Find:** a) the most common class, b) the share $P$ of the measurements that land at a distance of less than $0.10\,\text{nm}$, as a percentage, c) whether the data fits the $90\,\%$ boundary
**Principle:** The probability is estimated as the share of the measurements that land in the region out of all the measurements, $P \approx \tfrac{k}{N}$. The first two classes belong to less than $0.10\,\text{nm}$. The $90\,\%$ boundary is the distance inside which $90\,\%$ of the measurements land.
**Reading the graph:** The counts of the classes are read from the table: in the classes $0.00$–$0.05\,\text{nm}$ and $0.05$–$0.10\,\text{nm}$ there are $118$ and $171$ measurements. The class $0.05$–$0.10\,\text{nm}$ is the most common, because it has the greatest count, $171$.
**Formula:** $P = \dfrac{k}{N}$, where $k$ is the sum of the measurements that land in the region
**Conversions:** The share is converted to a percentage by multiplying by one hundred: $1 = 100\,\%$.
**Substitution:** The sum of the measurements of the first two classes is $k = 118 + 171 = 289$, so $P = \dfrac{289}{400} = 0.7225 = 72.25\,\%$. In part c) the sum of the first three classes is calculated similarly, $289 + 79 = 368$, and the share is $\dfrac{368}{400} = 0.920 = 92.0\,\%$.
**Answer:** In the answer box: $72.3\,\%$.

a) The most common class is $0.05$–$0.10\,\text{nm}$.

b) $72.3\,\%$, three significant figures like the counts.

c) $72.3\,\%$ of the measurements land at a distance of less than $0.10\,\text{nm}$ and $92.0\,\%$ at a distance of less than $0.15\,\text{nm}$, so $90\,\%$ is reached between these. Interpolating linearly, the boundary is about $0.10\,\text{nm} + \tfrac{90.0 - 72.3}{92.0 - 72.3} \cdot 0.05\,\text{nm} = 0.145\,\text{nm}$, which is close to $0.14\,\text{nm}$. So the data is consistent with the boundary. There are hits outside the boundary too: at a distance of more than $0.15\,\text{nm}$ there are $23 + 7 + 2 = 32$ measurements, that is, $8.0\,\%$.
**Reasonableness:** The most common class $0.05$–$0.10\,\text{nm}$ contains the Bohr radius $0.053\,\text{nm}$, and the class nearest the nucleus is the second most common. The counts decrease quickly outwards, and in total $118 + 171 + 79 + 23 + 7 + 2 = 400$, as it should be.

## fy8-5-L2-06
**Given:** length of the string $L = 0.80\,\text{m}$; speed of the wave $v = 64\,\text{m/s}$; ends of the string fixed
**Find:** a) the wavelength $\lambda$ in each state, b) the frequency $f$ in each state, c) an explanation of the connection between nodes and frequency
**Principle:** The ends of the string stay in place, so the ends are nodes and a whole number of antinodes fits on the string. When there are $m$ antinodes, the length of each antinode is half a wavelength, so $L = m \cdot \tfrac{\lambda}{2}$. For a wave, $v = f\lambda$.
**Reading the graph:** In the figure the uppermost state has one antinode and no node between the ends, the middle one has two antinodes and one node, and the lowest has three antinodes and two nodes. So there is always one more antinode than there are nodes: $m = 1, 2, 3$. The wavelengths of the figure cannot be read, so they are calculated from the length of the string.
**Formula:** $\lambda = \dfrac{2L}{m}$ and $f = \dfrac{v}{\lambda}$
**Conversions:** None are needed, because the length is in metres and the speed in $\text{m/s}$.
**Substitution:** a) In the state $m = 1$ the wavelength is $\lambda = \dfrac{2 \cdot 0.80\,\text{m}}{1} = 1.60\,\text{m}$, in the state $m = 2$ it is $\lambda = \dfrac{2 \cdot 0.80\,\text{m}}{2} = 0.80\,\text{m}$ and in the state $m = 3$ it is $\lambda = \dfrac{2 \cdot 0.80\,\text{m}}{3} = 0.533\,\text{m}$. b) In the state $m = 1$ the frequency is $f_1 = \dfrac{64\,\text{m/s}}{1.60\,\text{m}} = 40\,\text{Hz}$, in the state $m = 2$ it is $f_2 = \dfrac{64\,\text{m/s}}{0.80\,\text{m}} = 80\,\text{Hz}$ and in the state $m = 3$ (two nodes) it is $f_3 = \dfrac{64\,\text{m/s}}{0.5333\,\text{m}} = 120\,\text{Hz}$.
**Answer:** the frequency of the state with two nodes is $120\,\text{Hz}$, two significant figures like the speed $64\,\text{m/s}$.

a) The wavelengths are $1.60\,\text{m}$, $0.80\,\text{m}$ and $0.533\,\text{m}$.

b) The frequencies are $40\,\text{Hz}$, $80\,\text{Hz}$ and $120\,\text{Hz}$.

c) As the number of nodes increases, more antinodes fit on the string, so the wavelength gets shorter and the frequency grows: the wavelengths $1.60\,\text{m}$, $0.80\,\text{m}$ and $0.533\,\text{m}$ give the frequencies $40\,\text{Hz}$, $80\,\text{Hz}$ and $120\,\text{Hz}$. The state of the electron in an atom is also described by a standing wave, so only certain wave shapes are possible and the energy is quantised. In the hydrogen atom, the more nodes, the greater the energy, just as on a string the more nodes, the higher the frequency.
**Reasonableness:** In the state $m = 2$ the wavelength $0.80\,\text{m}$ equals the length of the string, and its frequency $\dfrac{64\,\text{m/s}}{0.80\,\text{m}} = 80\,\text{Hz}$ lies between $40\,\text{Hz}$ and $120\,\text{Hz}$. The frequencies $40\,\text{Hz}$, $80\,\text{Hz}$ and $120\,\text{Hz}$ are successive multiples of the fundamental frequency $40\,\text{Hz}$, as the number of antinodes requires.

## fy8-5-L2-07
**Find:** what is wrong in the student’s reasoning.
**Principle:** The boundary of an orbital is an agreed probability boundary, not a wall. On average $90\,\%$ of the measurements land inside the $90\,\%$ boundary, so $1 - 0.90 = 0.10$, that is, every tenth measurement, lands outside. In many measurements the share is approximately this probability, $P \approx \tfrac{k}{N}$.
**Model answer:** The boundary is an agreed probability boundary: about nine tenths of the measurements land inside it, and the rest land outside. $0.10 \cdot 2000 = 200$ hits are expected outside, and the observed number $205$ fits this: $\tfrac{205}{2000} = 10.25\,\%$. So the simulation works correctly, and the hits outside the boundary belong to the probability distribution of the wave model. They are not caused by the electron rushing about quickly or by measurement error, because each measurement gives one point, and even a more accurate measurement would find the electron outside the boundary one time in ten.

## fy8-5-L3-04
**Given:** wavelengths $\lambda$: $657.1\,\text{nm}$, $485.4\,\text{nm}$, $433.5\,\text{nm}$ and $410.6\,\text{nm}$; final shell $n = 2$; $E_n = -\tfrac{13.6\,\text{eV}}{n^2}$; $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$, $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$
**Find:** a) the energies $E_\text{f}$ of the photons, b) the numbers $n$ of the starting shells, c) the slope of the line of the graph, d) the wavelength of the line starting from the shell $n = 7$
**Principle:** The energy of the atom decreases by the difference of the energies of the states, and the same energy leaves as a photon: $E_\text{f} = \tfrac{hc}{\lambda} = E_n - E_2$. Substituting the energy-level formula gives $E_\text{f} = 13.6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)$. If the points are plotted according to this equation, they fall on a line whose slope is the constant of the energy-level formula.
**Reading the graph:** The values on the horizontal axis are $\tfrac{1}{4} - \tfrac{1}{n^2} = 0.139$, $0.188$, $0.210$ and $0.222$ for the shells $n = 3, 4, 5, 6$, and the values on the vertical axis are the energies of part a). The points fall approximately on a line that passes through the origin; the measured points vary slightly around the line. As a check, the slope calculated through the first and the last measured point, $(0.1389;\ 1.887\,\text{eV})$ and $(0.2222;\ 3.020\,\text{eV})$, is $\dfrac{3.020\,\text{eV} - 1.887\,\text{eV}}{0.2222 - 0.1389} = 13.6\,\text{eV}$, and the line fitted to all the points, whose slope is used as the answer, gives $13.62\,\text{eV}$ and the constant term $-0.003\,\text{eV}$.
**Formula:** $E_\text{f} = \dfrac{hc}{\lambda}$, $\ \dfrac{1}{n^2} = \dfrac{1}{4} - \dfrac{E_\text{f}}{13.6\,\text{eV}}$ and the slope $k = \dfrac{\Delta E_\text{f}}{\Delta\left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)}$
**Conversions:** The wavelength $657.1\,\text{nm} = 657.1 \cdot 10^{-9}\,\text{m}$ and similarly for the others. The product $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. Joules are converted to electronvolts by dividing by $1.602 \cdot 10^{-19}$.
**Substitution:** a) For the first line $E_\text{f} = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{657.1 \cdot 10^{-9}\,\text{m}} = 3.0231 \cdot 10^{-19}\,\text{J} = 1.887\,\text{eV}$. Similarly for the other lines: $2.555\,\text{eV}$, $2.860\,\text{eV}$ and $3.020\,\text{eV}$. b) For the first line $\dfrac{1}{n^2} = \dfrac{1}{4} - \dfrac{1.887\,\text{eV}}{13.6\,\text{eV}} = 0.2500 - 0.1388 = 0.1112$, so $n = \sqrt{\dfrac{1}{0.1112}} = 3.00$. Similarly for the other lines $n = 4.01$, $5.02$ and $5.98$. d) The energy of a photon starting from the shell $n = 7$ is $13.6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{49}\right) = 3.122\,\text{eV} = 5.002 \cdot 10^{-19}\,\text{J}$ and the wavelength is $\lambda = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{5.002 \cdot 10^{-19}\,\text{J}} = 3.971 \cdot 10^{-7}\,\text{m} = 397.1\,\text{nm}$.
**Answer:** a) $1.887\,\text{eV}$, $2.555\,\text{eV}$, $2.860\,\text{eV}$ and $3.020\,\text{eV}$; b) the starting shells are $n = 3, 4, 5$ and $6$, because $n$ is the number of the shell and therefore an integer, and the calculated values $3.00$, $4.01$, $5.02$ and $5.98$ differ from integers only by the measurement uncertainty; c) the slope is $13.6\,\text{eV}$, and it is the constant of the energy-level formula, that is, the absolute value of the ground-state energy of the hydrogen atom; d) about $397\,\text{nm}$.
**Reasonableness:** The slope $13.6\,\text{eV}$ equals the constant of the energy-level formula, and the line passes through the origin, as $E_\text{f} = 13.6\,\text{eV} \cdot \left(\tfrac{1}{4} - \tfrac{1}{n^2}\right)$ requires. The predicted wavelength $397\,\text{nm}$ is shorter than $410.6\,\text{nm}$ of the fourth line, and the lines get closer together towards the limit where $n \to \infty$: then $E_\text{f} = \tfrac{13.6\,\text{eV}}{4} = 3.40\,\text{eV}$ and $\lambda = 365\,\text{nm}$. The lines are separate, because the allowed states of the electron are standing waves and the energy is quantised.

## fy8-5-L3-05
**Given:** $Z = 11$; ionisation energies $E_\text{i}$ (NIST Atomic Spectra Database): Li $5.39\,\text{eV}$ ($n = 2$), Na $5.14\,\text{eV}$ ($n = 3$), K $4.34\,\text{eV}$ ($n = 4$); energy of the transition $3\text{s} \to 3\text{p}$ $\Delta E = 2.10\,\text{eV}$; $h = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$, $c = 2.998 \cdot 10^{8}\,\text{m/s}$, $1\,\text{eV} = 1.602 \cdot 10^{-19}\,\text{J}$
**Find:** a) the electron configuration of sodium, b) the decrease of the ionisation energy, c) the wavelength $\lambda$ of the exciting photon, d) the longest wavelength $\lambda_\text{max}$ of an ionising photon
**Principle:** In the ground state the electrons fill the orbitals starting from the lowest energy, at most two in each orbital. When a photon is absorbed, the energy of the atom changes by the energy of the photon, so the energy of the photon is the difference of the energies of the states, $\tfrac{hc}{\lambda} = \Delta E$. At least the ionisation energy is needed to release the electron, so the longest acceptable wavelength corresponds to the energy $E_\text{i}$.
**Formula:** $\lambda = \dfrac{hc}{\Delta E}$ and $\lambda_\text{max} = \dfrac{hc}{E_\text{i}}$
**Conversions:** $\Delta E = 2.10\,\text{eV} = 2.10 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 3.3642 \cdot 10^{-19}\,\text{J}$ and $E_\text{i} = 5.14\,\text{eV} = 5.14 \cdot 1.602 \cdot 10^{-19}\,\text{J} = 8.2343 \cdot 10^{-19}\,\text{J}$. Finally $1\,\text{nm} = 10^{-9}\,\text{m}$.
**Substitution:** First $hc = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2.998 \cdot 10^{8}\,\text{m/s} = 1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}$. In part c) $\lambda = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{3.3642 \cdot 10^{-19}\,\text{J}} = 5.905 \cdot 10^{-7}\,\text{m} = 590.5\,\text{nm}$ and in part d) $\lambda_\text{max} = \dfrac{1.9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{8.2343 \cdot 10^{-19}\,\text{J}} = 2.412 \cdot 10^{-7}\,\text{m} = 241.2\,\text{nm}$.
**Answer:** a) The atom has $11$ electrons, and the configuration is $1\text{s}^2\,2\text{s}^2\,2\text{p}^6\,3\text{s}^1$: the shells $n = 1$ and $n = 2$ fill up ($2 + 8 = 10$ electrons), and the eleventh electron is in the next lowest orbital, $3\text{s}$, so there is only one electron in the outermost shell. b) The valence electron is in the shell $n = 2$ in lithium, in the shell $n = 3$ in sodium and in the shell $n = 4$ in potassium. The higher the shell, the farther from the nucleus it is, and between it and the nucleus there are more and more full shells whose electrons repel it. The charge of the nucleus grows according to the numbers $3$, $11$ and $19$, but the ionisation energy still decreases from $5.39\,\text{eV}$ and $5.14\,\text{eV}$ to $4.34\,\text{eV}$, so the effect of the growth of the shell is greater than that of the charge of the nucleus. The formula $\tfrac{13.6\,\text{eV}}{n^2}$ of the hydrogen atom would give similarly decreasing values $3.40\,\text{eV}$, $1.51\,\text{eV}$ and $0.85\,\text{eV}$; for the alkali metals the values are greater, because the electrons of the inner shells do not completely screen the charge of the nucleus, so a greater charge than in hydrogen acts on the valence electron. c) The wavelength of the photon is $590\,\text{nm}$, three significant figures like the number $2.10\,\text{eV}$. d) A photon with a wavelength of at most $241\,\text{nm}$ is suitable for ionisation. The energy of the photon, $2.10\,\text{eV}$, is smaller than $E_\text{i} = 5.14\,\text{eV}$, so the photon of part c) is not enough to release the electron; it only moves the electron to the state $3\text{p}$.
**Reasonableness:** The wavelength $590\,\text{nm}$ is in the region of visible light, at yellow light, and a sodium lamp glows yellow. The energies are consistent: an ionising photon needs the energy $5.14\,\text{eV}$, which is $\tfrac{5.14}{2.10} = 2.45$ times the energy of the exciting photon, and the wavelength is correspondingly $\tfrac{590.5\,\text{nm}}{241.2\,\text{nm}} = 2.45$ times as long. The ionisation limit $241\,\text{nm}$ is ultraviolet, as it should be.
