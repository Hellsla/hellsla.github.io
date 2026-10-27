VERDICT: FAIL
CONTENT-HASH: be18593c28fd79f4

## Blocking
- lessons/FY1/fy1-1/figures.py:70,81 (lesson.md:48,83, figure `scale-axis`): the figure says its axis is to scale and that it plots each size's order of magnitude, but it puts the Milky Way at 10^20. Its size of about 9,5·10^20 m (the sim's value, 10^5 ly) is of order 10^21 under the lesson's own rule (a > about 3), and check-3's model answer uses 10^21 m. Fix: put it at exponent 21 (marker x ≈ 476.8) and change "Linnunrata 20" to "21" in the aria-label.

## Polish
- inquiry.json:202: exp-2 mistake value `-4e+26` has the wrong sign. The mean of the two sizes in metres is +4,4·10^26 m, so this feedback never fires. Fix: use `4.4e+26`.
- solutions.md:88 (L2-04): "tiedoissa on kolme, mutta tulos pyöristetään kahteen" gives no reason, and the house rule says three figures. Fix: give 1,31 miljoonaa (three significant figures).
- inquiry.json `menetelmat`: "Maan rata 1,5·10^11 m" is the orbit's radius (1 AU), not the orbit's size. Fix: say "Maan radan säde (1 AU)".
- sim.js `helio`/`oort`: unlike the planetary orbits, these have no radius marker, but their labels show the radius while the picture's width is the diameter. Fix: add the same orange radius line as `orbitPicture`.

## Checked
- All 12 exercise answers, siirto (12 732 km and its three mistakes), check-2 (8,33 min) and the worked example (6,5·10^4, Δn = 5) were recomputed independently and match answers.py and the solutions.
- Sim object sizes (40) against reference values: Planck length, proton (charge diameter), He and Pb nuclei, He and H atoms, DNA, virus, red blood cell, hair, 1 € coin, ball, blue whale, 828 m tower, Everest, Kármán line, Moon, Earth, Jupiter, Sun, 1 AU, Saturn and Neptune orbits, heliopause about 120 AU, Oort cloud about 10^5 AU, Proxima, Orion Nebula about 24 ly, LMC, Milky Way, Andromeda, Local Group, Virgo, Laniakea, observable universe. All are right to well within an order of magnitude.
- To scale: every picture is drawn with S = ext/W·560 at one shared W. The layout spacing (slot, sc) moves pictures but never resizes them. Screenshots at L = 1 (human about 95 px, ball about 12 px, whale cropped) and L = −9 (H atom about 62 px, He atom about 35 px) agree. Orbits are drawn as diameters, and the radius marker matches the radius label.
- Exaggerations are disclosed in `model`: the atom's nucleus, the stars in the Proxima picture, and the Planck grid as a symbol.
- `kohdeExp = round(log10 m)` matches the "a ≈ 3" rule. The initial states give the right nearest object: L = −9 → H atom (−10), L = 1 → human (0), L = −34 → Planck (−35), L = 27,5 → universe (27). The answers 10 and −4 follow.
- `calc` text: 0,3–1700 px matches fadeIn/fadeOut. The scale bar is 10^floor(L) m.
- The light-time figure (1,28 s, 8,3 min, 4,2 a) and the light-year (9,46·10^15 m) are correct.
- Every prediction's correct option and the numbers in its feedback, the Etsi virhe item (factor 109), check-1 (10^17) and the exit ticket are correct.
- Scope: powers of ten, orders of magnitude and s = ct as a linear model are within FY1.
- Hash unchanged at the start and the end.
