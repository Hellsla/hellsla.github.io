"""Numbers of the lesson text and inquiry.json for fy6-10, computed from their data (python -I lesson-answers.py); the
exercises' answers are in answers.py. Charge Q = n e (e = 1,602 · 10^-19 C); Coulomb's law F = k |q1 q2| / r^2 with
k = 8,988 · 10^9 N m^2 / C^2 between point charges; current I = Q / t. The simulation: two small spheres treated as
point charges q1 and q2 (nC) at the distance r (cm) between their centres; F in mN.
Prints {id: number} as JSON."""
import json

K, E = 8.988e9, 1.602e-19
G, ME, MP = 6.674e-11, 9.109e-31, 1.673e-27
nC, cm = 1e-9, 1e-2


def F(q1, q2, r):
    """Coulomb force in N; q1, q2 in C, r in m."""
    return K * abs(q1 * q2) / r ** 2


def F_sim(q1, q2, r):
    """The simulation's force in mN; q1, q2 in nC, r in cm."""
    return F(q1 * nC, q2 * nC, r * cm) * 1000


a = {}
# --- Ydinajatus ---
a["pallo-n"] = 50 * nC / E                                    # a balloon at -50 nC carries 3,1 · 10^11 extra electrons
a["coulombi-n"] = 1 / E                                       # 1 C = 6,24 · 10^18 elementary charges
# --- Kaava: the graph F(r) for q1 = q2 = 20 nC ---
for r in (3, 6, 9, 12):
    a[f"kuvaaja-{r}"] = F_sim(20, 20, r)                      # 4,0 mN; 1,0 mN; 0,44 mN; 0,25 mN
a["vety-suhde"] = K * E ** 2 / (G * ME * MP)                  # electric : gravitational force in hydrogen, 2,3 · 10^39
# --- Esimerkki: q1 = +12 nC, q2 = -8,0 nC, r = 6,0 cm ---
a["esim-F"] = F(12 * nC, 8.0 * nC, 6.0 * cm) * 1000           # 0,2397 mN
a["esim-tulo"] = 12e-9 * 8.0e-9                               # 9,6 · 10^-17 C^2
a["esim-r2"] = 0.060 ** 2                                     # 0,0036 m^2
a["esim-F-puolet"] = F(12 * nC, 8.0 * nC, 3.0 * cm) * 1000    # half the distance: four times, 0,959 mN
a["esim-paino-mg"] = a["esim-F"] / 1000 / 9.81 * 1e6          # the weight of 24 mg equals the force
# --- the simulation on load: q1 = q2 = +20 nC, r = 6,0 cm ---
a["sim-F"] = F_sim(20, 20, 6)                                 # 0,999 mN
# --- koe 1: q1 = q2 = +20 nC, r varies ---
for r in (3, 4, 6, 8, 12):
    a[f"koe1-r{r}"] = F_sim(20, 20, r)                        # 3,996; 2,248; 0,999; 0,562; 0,250 mN
a["koe1-suhde"] = a["koe1-r3"] / a["koe1-r12"]                # 16: a quarter of the distance, 16 times the force
a["koe1-suhde-36"] = a["koe1-r3"] / a["koe1-r6"]              # 4: the prediction's doubling
# --- koe 2: q1 = +20 nC, r = 6,0 cm, q2 varies; both spheres feel the same force ---
for q in (10, 20, 40, -20):
    a[f"koe2-q{q}"] = F_sim(20, q, 6)                         # 0,4995; 0,999; 1,998; 0,999 mN
# --- virhe (Etsi virhe): q1 = q2 = 5,0 nC, r = 2,0 cm ---
a["virhe-oikein"] = F(5.0 * nC, 5.0 * nC, 0.020)              # 5,6 · 10^-4 N
a["virhe-cm"] = F(5.0 * nC, 5.0 * nC, 2.0)                    # with r = 2,0 "m": 5,6 · 10^-8 N
a["virhe-ilman-nelio"] = K * (5.0 * nC) ** 2 / 2.0            # r in cm and not squared, as the student wrote: 1,1 · 10^-7 N
# --- siirto: 1,0 · 10^11 electrons moved onto each of two spheres, r = 5,0 cm ---
q_s = 1.0e11 * E                                              # 1,602 · 10^-8 C = 16 nC
a["siirto-q-nC"] = q_s / nC
a["siirto"] = F(q_s, q_s, 0.050) * 1000                       # 0,923 mN
a["siirto-cm"] = F(q_s, q_s, 5.0) * 1000                      # r left in cm: 9,2 · 10^-5 mN
a["siirto-ei-nelio"] = K * q_s ** 2 / 0.050 * 1000            # r not squared: 0,046 mN
a["siirto-q-kerran"] = K * q_s / 0.050 ** 2 * 1000            # q not squared (k q / r^2): 5,8 · 10^7 mN
# --- kertaus: 0,50 C in 2,0 s ---
a["kertaus"] = 0.50 / 2.0                                     # 0,25 A
# --- tarkistus-2: figure check-graph, two equal charges q = 30 nC; the student reads F = 9,0 mN at r = 3,0 cm ---
for r in (3, 4, 5, 6, 9):
    a[f"check-graph-{r}"] = F_sim(30, 30, r)                  # 8,99; 5,06; 3,24; 2,25; 1,0 mN (the figure's data)
a["tarkistus-2"] = 0.030 * (9.0e-3 / K) ** 0.5 / nC           # q = r sqrt(F / k) = 30,0 nC
a["tarkistus-2-nelio"] = 0.030 ** 2 * 9.0e-3 / K / nC ** 2    # q^2 in nC^2 = 900 (forgot the root)
a["tarkistus-2-cm"] = 3.0 * (9.0e-3 / K) ** 0.5 / nC          # r left in cm: 3000 nC
# --- exit ticket ---
a["exit-n"] = 3.2e-19 / E                                     # 2 missing electrons
a["exit-suhde"] = (2 * 2) / 2 ** 2                            # both charges doubled and the distance doubled: 1

print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
