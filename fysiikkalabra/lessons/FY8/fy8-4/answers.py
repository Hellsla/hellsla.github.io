"""Every answer in exercises.json for fy8-4, computed from the task data (python -I answers.py).
Photon: E = hf = hc/λ, p = h/λ = E/c; photon flow N/t = P/E; Compton scattering: energy conservation hc/λ = hc/λ' + E_k.
A task that asks in a unit with a power of ten (10⁻²⁷ kg·m/s) has the mantissa as its answer.
Prints {exercise id: number} as JSON on the last line; the lint and the gate compare it with exercises.json."""
import json

h, c, e = 6.626e-34, 2.998e8, 1.602e-19            # J s, m/s, C (1 eV = 1,602e-19 J)
a = {}
# Level 1: one formula, values given
a["fy8-4-L1-01"] = h / 532e-9 / 1e-27              # green laser photon: p = h/λ = 1,2455e-27 kg m/s -> 1,25 (10⁻²⁷ kg·m/s)
a["fy8-4-L1-02"] = h / 0.0711e-9 / 1e-24           # X-ray photon 0,0711 nm: p = 9,319e-24 kg m/s -> 9,32 (10⁻²⁴ kg·m/s)
a["fy8-4-L1-03"] = h / 3.60e-27 / 1e-9             # λ = h/p = 6,626e-34 / 3,60e-27 m = 1,8406e-7 m -> 184 nm
a["fy8-4-L1-04"] = 2.00e-27 * c / 1e-19            # E = p c = 2,00e-27 · 2,998e8 J = 5,996e-19 J -> 6,00 (10⁻¹⁹ J)
a["fy8-4-L1-05"] = 1.0e-3 / 3.14e-19 / 1e15        # N/t = P/E = 1,0e-3 W / 3,14e-19 J = 3,18e15 1/s -> 3,2 (10¹⁵ 1/s)
# Level 2: two steps, one conversion or one rearrangement
lam, lam2 = 0.0711e-9, 0.0735e-9                   # Compton: X-ray 0,0711 nm scattered to 0,0735 nm
a["fy8-4-L2-01"] = (h * c / lam - h * c / lam2) / e   # electron's kinetic energy = photon's energy loss: 9,13e-17 J = 570 eV
a["fy8-4-L2-02"] = 662e3 * e / c / 1e-22           # gamma photon 662 keV: E = 662e3 · 1,602e-19 J = 1,0605e-13 J, p = E/c = 3,537e-22 -> 3,54
a["fy8-4-L2-03"] = 2 * h / 1550e-9 / 1e-28         # 1550 nm photon reflected straight back: Δp = 2h/λ = 8,550e-28 kg m/s -> 8,55 (10⁻²⁸ kg·m/s)
a["fy8-4-L2-04"] = 2.40e4 * h * c / 550e-9 / 1e-15 # detector counts 2,40e4 photons/s at 550 nm: P = (N/t) hc/λ = 8,669e-15 W -> 8,67 (10⁻¹⁵ W)
# Level 3: reasoning or an unfamiliar context
m_Na, lam_Na, v0 = 3.82e-26, 589e-9, 3.00e2        # laser cooling: a sodium atom absorbs photons coming against it
dv = h / lam_Na / m_Na                              # each absorbed photon changes the speed by h/(λ m) = 2,945e-2 m/s
a["fy8-4-L3-01"] = v0 / dv / 1e4                    # photons needed: N = v0/Δv = 1,0187e4 -> 1,02 (10⁴)
E_in = h * c / 0.0500e-9                            # Compton: X-ray 0,0500 nm, electron gets 1,00 keV
E_out = E_in - 1.00e3 * e                           # scattered photon's energy 3,9727e-15 J − 1,602e-16 J = 3,8125e-15 J
a["fy8-4-L3-02"] = h * c / E_out / 1e-9             # λ' = hc/E' = 0,05210 nm -> 0,0521 nm
E32 = 13.6 * (1 / 2**2 - 1 / 3**2) * e              # hydrogen n = 3 -> 2 photon: 1,889 eV = 3,0262e-19 J
a["fy8-4-L3-03"] = E32 / c / 1.67e-27               # recoil: m v = p = E/c -> v = 1,0094e-27 / 1,67e-27 m/s = 0,6044 m/s -> 0,604 m/s
print(json.dumps({k: float(f"{v:.6g}") for k, v in a.items()}))
