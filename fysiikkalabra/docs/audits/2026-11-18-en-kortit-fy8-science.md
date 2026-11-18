# Science review: English concept cards FY8 (`kortit/en/fy8.json`)

Date 2026-11-18. Reviewer: science agent. Scope: the 147 cards in `kortit/en/fy8.json`, checked against the Finnish
originals in `kortit/fy8.json` (same ids; `luku` and `aihe` agree on every card; the five formulas with numbers differ
only by the decimal mark) and against the English lessons `content/en/FY8/<luku>/lesson.md` (their `kaavat` blocks and
bold terms). 23 cards have `luku: null`; for them I judged only the physics and the course level. I did not edit any card.

**Overall verdict: FIX.** 134 cards PASS. 13 cards need a fix: 1 error (annihilation), 3 missing conditions, 4 notation
mismatches with the lesson formulas, 1 ambiguous `kaava_puhe` and 4 terminology or consistency mismatches. Every
decimal point is in English style (1.60, 13.6, 1.66). Recomputed: 1 eV = 1.602·10⁻¹⁹ J, 1 u = 1.661·10⁻²⁷ kg,
E₁ = −13.6 eV, hc/e = 1240 V·nm (so λ_min = 0.0155 nm at 80 kV, which matches the fy8-14 limit E ≤ eU),
μ = ln 2 / d₁/₂. All the card formulas are dimensionally and numerically right.

Classes: **A** = error, **B** = true only under a condition the card does not state, **T** = terminology, notation or
reading mismatch with the lesson.

## FIX

| id | class | problem | suggested wording |
|---|---|---|---|
| fy8-annihilaatio | A | "they can change into radiation energy": particles do not turn into energy. They turn into photons, and the photons carry the energy. Lesson fy8-15 says "both disappear, and all their energy turns into, for example, photons". The Finnish card has the same flaw. | "When a particle and its antiparticle meet, both can disappear, and all their energy is carried away by, for example, photons." |
| fy8-ionisoiva-sateily | B | "Radiation with enough energy" invites the misconception that the total energy (intensity) matters. Lesson fy8-12: "a single particle or photon of it can remove an electron". | "Radiation whose single particles or photons have enough energy to release electrons from atoms or molecules." |
| fy8-ionisaatioenergia | B | The lesson (fy8-3) defines it from the ground state. From an excited state less energy is needed. | "The smallest energy needed to release an electron completely from an atom in its ground state." |
| fy8-karakteristinen-sateily | B | "transitions between electron states of atoms" also covers visible line spectra. X-ray lines come from inner-shell vacancies (fy8-14: "an electron from an outer shell drops into its place"). | "Produced when an electron of an anode atom drops into a vacancy in an inner shell; it forms spectral lines characteristic of the material." |
| fy8-sidosenergia | T | The lesson's formula is `E_\text{B} = \Delta m\,c^2`, but the card writes plain E. | kaava `E_\text{B} = \Delta m\,c^2`; kaava_puhe "E B is delta m times c squared" |
| fy8-reaktioenergia | T/B | `Q = \Delta m c^2` does not say which way Δm is taken. Elsewhere in fy8-10, Δm is the mass defect. Lessons fy8-10 and fy8-15 write `Q = (m_\text{initial} - m_\text{final})\,c^2`. | kaava `Q = (m_\text{initial} - m_\text{final})\,c^2`; kaava_puhe "Q is the difference m initial minus m final, times c squared" |
| fy8-valosahkoilmion-energiayhtalo | T | fy8-1 writes the work function as W (`hf = W + E_\text{k,max}`) and never uses W₀. | kaava `hf = W + E_{\text{k,max}}`; kaava_puhe "h f is W plus E k max" |
| fy8-maksimiliike-energia | T | The physics is right (luku null), but it uses the same W₀. Make it match fy8-1 and the card above. | kaava `E_{\text{k,max}} = hf - W`; kaava_puhe "E k max is h f minus W" |
| fy8-lyhyin-aallonpituus | T (kaava_puhe) | "h c divided by e U" sounds like (hc/e)·U. The formula is correct. | "lambda min is h c divided by the product e U" |
| fy8-laser | T | The lesson (fy8-7) says "nearly monochromatic, directional and coherent", not "almost single-coloured" or "strongly directed". | "Produces directional, nearly monochromatic and coherent electromagnetic radiation." |
| fy8-sateilysuojaus | T | The card is named "Shielding", but its definition lists time, distance and shielding. In fy8-13, shielding is one of the three ways, under "Protection: time, distance and shielding". The Finnish term is säteilysuojaus. | kasite "Radiation protection"; maaritelma unchanged |
| fy8-seisova-aalto | T/B | "a wave form that … allows only certain quantum states" gets the logic backwards. fy8-5 says the allowed states *are* standing waves, because a bound wave can only be a standing wave. | "A wave whose pattern stays in place; the allowed states of a bound electron are standing waves, so only certain quantum states are possible." |
| fy8-kosminen-inflaatio | T (consistency) | The card points to fy8-16, but no FY8 lesson, English or Finnish, mentions inflation. The physics is fine and suits the level. | Set luku to null in both files, or add one sentence on inflation to fy8-16. |

## Recommended changes (not blocking, cards still PASS)

- fy8-elektronivoltti: "gains when it moves through a potential difference of one volt" (the FY6 card's wording).
- fy8-aktiivisuus: "per unit time (in becquerels, per second)". The lesson (fy8-9) says "per unit of time".
- fy8-radon: the lesson shows radon as *the largest* source (about 4 of 5.9 mSv a year). "the largest source of
  radiation dose in Finland" is more accurate than "a significant source" (the Finnish says merkittävä, so this is optional).
- fy8-emissiospektri: "when its energy states de-excite" → "when its atoms de-excite to lower energy levels".
- fy8-isotooppi: the lesson's wording reads better: "Nuclei of the same element with different numbers of neutrons."
- fy8-elektronisieppaus: "captures an electron from the innermost shell of its own atom" (fy8-8).
- fy8-lyhyin-aallonpituus: fy8-14 states only E ≤ eU and never gives λ_min. The card's formula is correct and follows
  from E = hc/λ (level C), but the lesson could show it.

## PASS (correct, matches the Finnish card, term matches the lesson)

kvantti, kvantittuminen, fotoni, planckin-vakio, fotonin-energia (E = hf = hc/λ as in fy8-1), elektronivoltti,
musta-kappale, jatkuva-spektri, valosahkoilmio, irrotustyo, rajataajuus, pysaytysjannite, sateilyn-intensiteetti,
aaltohiukkasdualismi, fotonin-liikemaara (p = h/λ = E/c as in fy8-4), comptonin-sironta ("Compton effect" as in fy8-4),
kaksoisrakokoe, aineaalto, de-broglie, interferenssi, elektronimikroskooppi, energiataso, perustila, viritystila,
virittyminen, emissio, absorptio, emissiospektri, absorptiospektri, viivaspektri, energiatasokaavio,
vetyatomin-energia (−13.6 eV/n² as in fy8-3/fy8-5), kvanttitila, aaltofunktio, todennakoisyysjakauma, orbitaali,
kvanttiluku, elektronikuori, paulin-kieltosaanto, heisenbergin-epatarkkuusperiaate, tunneloituminen, puolijohde,
seostaminen, diodi, transistori, aurinkokenno, luminesenssi, fluoresenssi, fosforenssi, stimuloitu-emissio
("same energy", level C), koherentti-valo, rontgensateily, rontgenputki, katodi, anodi, jarrutussateily,
rontgenspektri, nukleoni, protoni, neutroni, jarjestysluku, massaluku, isotooppi, atomimassayksikko, massavaje,
sidososuus, ydinreaktio, fissio, ketjureaktio, fuusio, fuusioreaktio, ydinvoimala, kriittinen-massa,
radioaktiivisuus, emoydin, tytarydin, alfahajoaminen, beeta-hajoaminen, beeta-hajoaminen-2, elektronisieppaus,
gammahajoaminen, alfasateily, beetasateily, gammasateily, neutriino, aktiivisuus, becquerel, hajoamisvakio,
puoliintumisaika, hajoamislaki (N₀e^{−λt} as in fy8-9), aktiivisuuden-pieneneminen, hajoamissarja, intensiteetti,
sateilyn-vaimeneminen (I₀e^{−μd} as in fy8-12, gamma stated), vaimennuskerroin, puoliintumispaksuus,
etaisyyden-nelion-laki (point source stated), valosahkoabsorptio, comptoninsironta ("Compton scattering" as in the
fy8-12 table), parinmuodostus, absorboitunut-annos, gray, ekvivalenttiannos, sievert, taustasateily, radon,
sateilyvaurio, rontgenkuvaus, tietokonetomografia, isotooppilaaketiede, pet-kuvaus, sadehoito, radiohiiliajoitus,
palovaroitin, standardimalli, alkeishiukkanen, kvarkki, leptoni, valittajahiukkanen ("mediator particles" as in
fy8-15), gluoni, valibosoni, higgsin-bosoni, antihiukkanen, vahva-vuorovaikutus, heikko-vuorovaikutus,
hiukkasfysiikka, kosmologia, alkurajahdys, nukleosynteesi, rekombinaatio, pimea-aine, pimea-energia,
kosminen-taustasateily ("cosmic background radiation" as in fy8-16), punasiirtyma (all ids carry the prefix fy8-).

The level suits FY8 throughout. No card brings in physics from a later course. The Finnish cards fy8-annihilaatio,
fy8-ionisoiva-sateily, fy8-karakteristinen-sateily, fy8-seisova-aalto and fy8-kosminen-inflaatio share the same flaws
and should get the same fixes.

## Handling (worker, 2026-11-18)

All FIX items are applied to `kortit/en/fy8.json` except two, which touch other files and are left for the teacher:
- **fy8-annihilaatio**: the Finnish card in `kortit/fy8.json` has the same flaw ("muuttua säteilyenergiaksi"); not changed here.
- **fy8-kosminen-inflaatio**: no FY8 lesson mentions inflation; the card keeps `luku: fy8-16` (it must equal the Finnish one). Either add one sentence on inflation to fy8-16 or set `luku` to null in both files.
Also applied: the recommended wording for fy8-elektronivoltti, fy8-radon, fy8-emissiospektri, fy8-isotooppi, fy8-elektronisieppaus.
