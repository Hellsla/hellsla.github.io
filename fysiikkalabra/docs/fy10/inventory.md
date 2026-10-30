# FY10 source inventory (phase B, 2026-10-30)

Made from the three PDFs supplied in the project thread (not in this repository). Rendered pages were checked against
the text layer: **the blanks are in the PDFs themselves**, not extraction errors (e.g. p. 1 "Pidä sähkövirta alle ."
is blank on the rendered page too). They look like inline equations or values lost when the document was exported.
Nothing below fills a gap from memory; a gap is listed as missing.

Levels are **preliminary** (brief §12): F = physics knowledge, E = experimental complexity, assessed for the
investigation as written. Support modes: O = ohjattu, OO = osittain ohjattu, I = itsenäinen. Ruukkilabra chapters
are named when published (FY1–FY4); FY5–FY8 are not published yet, so those prerequisites need a short explanation
in the investigation and the missing chapter is named.

## Source documents
| Document | Contents | Notes |
|---|---|---|
| Esimerkkityöt.pdf, 17 p. | 31 task sections: 29 distinct cards (one is a three-part rotation set) and 2 duplicated cards | short open task cards: aim, what to plan, equipment, tips; no procedures, data or answers. **Provenance:** the pendulum card says "määrität [g] Espoon yhteislyseossa": check authorship and permission before adapting its wording; the investigations themselves are standard school experiments. |
| FY10 – Työselostuspohja.pdf, 5 p. | report template, 9 sections + checklist | §5 "Kulmakertoimen epävarmuus" says "jommallakummalla tavalla" but lists one way (fit software's standard error): a second way is missing from the source. |
| 11A_fi.pdf, 1 p. | YO autumn 2024 physics 11, material 11.A: a deliberately flawed rubber-band report in 5 numbered sections | YTL material: link to the original, never republish it. Students find the most significant error per section and correct it; model answers stay out of the public repo and site. |

## Investigations
Columns: page · physics (modules, Ruukkilabra chapters) · F/E · modes · TVT · equipment and safety · gaps and notes.

**1. Putoamiskiihtyvyyden määrittäminen heilurin avulla** · p. 1
- Physics: period of a simple pendulum (small angles), linearisation $T^2$ vs $l$ · FY5 (harmoninen värähtely, not published), FY1 graphical model (*Graafinen esitys ja suoran sovittaminen*). Essential: period, linear fit; helpful: *Putoamiskiihtyvyys*; extension: large-angle correction.
- F2 · E2 · O/OO/I. TVT: linear fit (Graphical Analysis), timing many periods.
- Equipment: stand, hook, thread, bob, tape, scissors. Safety: low.
- Gaps: "Tee mittauksia ." and "Muodosta mittaustuloksista ," (what to vary and which graph are missing). Good FY10 core.

**2. Uppokuumentimen hyötysuhteen määrittäminen** · p. 1
- Physics: electric energy $UIt$, heat $cm\Delta T$, efficiency, graph $\Delta T$ vs $t$ or $Q$ vs $E$ · FY2 (*Hyötysuhde*, *Teho*), FY3 (*Aineen lämpeneminen ja jäähtyminen*), FY6 (sähköteho, not published).
- F2 · E2 · O/OO. TVT: temperature sensor logging, linear fit, slope as power ratio.
- Equipment: calorimeter with heater, thermometer, ammeter, voltmeter, supply. **Safety: the current limit is blank in the source ("Pidä sähkövirta alle .")**: do not publish without a verified value from the actual equipment; hot water, heater never powered dry.
- Gaps: aim ("määrität [hyötysuhteen?]"), "Hyödynnä työssä muun muassa ." Strong FY10 candidate (FY3 reverse link *Sovella kokeellisesti*).

**3. Liikemäärän säilyminen törmäyksissä** · p. 1–2
- Physics: momentum, elastic and perfectly inelastic 1D collisions · FY4 (*Liikemäärä ja impulssi*, *Liikemäärän säilyminen ja yksiulotteiset törmäykset*).
- F1–F2 · E2 · O/OO. TVT: motion-sensor data, reading velocities before/after.
- Equipment: track, two carts, two optical motion sensors, masses, scale, spring bumpers. Safety: carts falling off the track.
- Gaps: aim, what to show ("että systeemin [liikemäärä säilyy?]"), "rata on [vaakasuorassa?]", "Kytke vaunut päälle. Vaunun .", "Käytä ja .".

**4. Jousivakion määrittäminen kahdella menetelmällä** · p. 2–3
- Physics: method 1 force–extension (Hooke's law, slope = $k$); method 2 period of a mass–spring oscillator, $T^2$ vs $m$ · method 1: FY3 (*Voima vuorovaikutuksen mittana ja paino*), FY1 (*Mittaaminen…*, *Graafinen esitys…*); method 2: FY5 (harmoninen voima, not published). Hooke's law has no Ruukkilabra chapter yet: needs a short explanation.
- Method 1: F1 · E1. Method 2 and comparison: F2 · E3. Modes O/OO/I on one page. TVT: linear fit, slope interpretation, comparing two results with uncertainties.
- Equipment: spring, stand, masses, scale, rule, timer or motion sensor. Safety: low (no permanent deformation, masses falling).
- Gaps: aim ("Määritä ."), "määritä jousivakio ." (twice; presumably "graafisesti"). **Chosen first investigation** (brief §17) and links to YO 2024/11.

**5. Liukukitkakertoimen määrittäminen** · p. 3
- Physics: work of friction = loss of kinetic energy, $\tfrac12 v_0^2$ vs stopping distance · FY4 (*Paino, kitka ja kalteva taso*, *Liike-energia…*, *Mekaanisen energian säilyminen ja energiaperiaate*).
- F2 · E2 · OO. TVT: motion sensor, linear fit through chosen axes.
- Equipment: track, optical motion sensor, cart with friction brake. Safety: cart falling.
- Gaps: aim, "Mittaa … vaunun ja ." (which quantities), "rata on .", "alkunopeudet siten, että vaunu .".

**6a–c. Hitausmomentti; umpinaisen sylinterin hitausmomentti; pyörimismäärän säilyminen** · p. 3–4
- Physics: moment of inertia, rolling energy, angular momentum: **beyond the LOPS 2019 modules** (FY5 has only torque and balance).
- 6a concept study F3 · E1; 6b F3 · E3; 6c demonstration F3 · E1. Modes OO/I. Extension only.
- No equipment list for 6a–6b (6c: bicycle wheel). Gaps: "mitä tarkoitetaan" (a, c), aim of 6b, "teoreettisen mallin avulla ja .".

**7. Valaistusvoimakkuuden riippuvuus etäisyydestä** · p. 4
- Physics: inverse-square law, linearisation ($E$ vs $1/r^2$) or power fit · FY7 (sähkömagneettinen säteily, not published); mostly a modelling exercise.
- F1–F2 · E2 · OO/I. TVT: light sensor, model comparison, linearisation.
- Equipment not listed (light source, lux sensor, rule implied). Safety: low (hot lamp).
- Gaps: aim, "muodosta mittaustuloksista ," (which graph). Good for theme 5 (graphical analysis and models).

**8. Kappaleen jäähtymisen tutkiminen** · p. 5 · **printed twice (p. 5)**: one copy is a duplicate
- Physics: cooling towards room temperature; exponential (Newton's law of cooling) as an empirical model · FY3 (*Aineen lämpeneminen ja jäähtyminen*, *Lämmön siirtyminen…*). The exponential model is beyond FY1–FY8 maths of the modules: needs explanation or an empirical approach.
- F2 · E2 (+ one-factor extension E2) · OO/I. TVT: temperature logging, nonlinear (exponential) fit.
- Equipment: vessel, hot water, sensor, timer, insulation. Safety: hot water.
- Gaps: aim, "sopiva [malli]", "Selvitä, mitä [Newtonin jäähtymislaki?] tarkoittaa".

**9. Pariston kuormituskäyrä** · p. 6
- Physics: $U = E - RI$, emf, internal resistance, short-circuit current from the graph · FY6 (*Akut, lähdejännite ja sisäinen resistanssi*, not published).
- F2 · E2 · O/OO. TVT: linear fit, intercepts as physical quantities.
- Equipment: battery, voltmeter, ammeter, rheostat, wires. Safety in source: no short circuit.
- Gaps: what is studied, which pairs ("pariston [napajännite] … [sähkövirta]"), the three quantities ("pariston ." ×3), "määritetään [graafisesti]".

**10. Tuulivoimalan tutkiminen** · p. 7
- Physics: electric power, efficiency, power of the wind (optional) · FY2 (*Teho*, *Hyötysuhde*), FY4 (*Vesi- ja tuulivoima energian muuntajina*), FY6.
- F2 · E2–E3 · OO/I. TVT: power from $U$ and $I$, graph of one factor.
- Equipment: model turbine, fan, meters, load, anemometer, rule. Safety: rotating blades (in source).
- Gaps: aim, "määritä myös tuulivoimalan [hyötysuhde]".

**11. Valonnopeuden määrittäminen mikroaaltouunilla** · p. 7
- Physics: standing waves, node spacing $\lambda/2$, $c = f\lambda$ · FY5 (seisovat aallot), FY7 (sähkömagneettinen säteily); none published.
- F2 · E1 · O/OO. TVT: none essential.
- Equipment: microwave oven, grated cheese, rule. Safety: teacher-supervised, oven never run empty, hot cheese, food hygiene.
- Gaps: aim, "syntyvää [seisovaa aaltoa]", "mikroaaltojen [aallonpituuden]", "käyttämä [taajuus]".

**12. Jumppapallon muotokertoimen määrittäminen** · p. 8
- Physics: air resistance $F = \tfrac12 C\rho A v^2$, terminal velocity · FY4 (*Ilmanvastus ja putoaminen ilmassa*, *Newtonin toinen laki*).
- F2 · E3 · OO/I. TVT: video analysis (software to be chosen), scale calibration.
- Equipment not listed (ball, camera, scale). Safety: low.
- Gaps: "miten [ilmanvastusta] voidaan mallintaa", "mitä [muotokerroin] tarkoittaa", aim, "määritä [rajanopeus]".

**13. Kondensaattorin kapasitanssin määrittäminen** · p. 9
- Physics: RC charging/discharging, time constant, exponential model · FY6 (*Kondensaattorin varaaminen ja purkaminen*, not published).
- F3 · E2 · OO. TVT: voltage logging, exponential fit or linearisation (ln).
- Equipment listed. Safety in source: polarity, max voltage, controlled discharge.
- Gaps: aim, "määritä … piirin [aikavakio]".

**14. Hiuksen paksuuden määrittäminen** · p. 9
- Physics: single-obstacle diffraction (Babinet), minima positions · FY7 (*Valon interferenssi ja diffraktio*, not published).
- F3 · E2 · O/OO. TVT: linear fit of minimum position vs order.
- Equipment: laser, hair, screen, rule. **Safety: laser class must be verified (class 2 or lower for students), no beam to eyes, mind reflections.**
- Gaps: aim.

**15. Äänen resonanssi putkessa** · p. 10
- Physics: standing waves in an air column, $\lambda$ from successive resonances, $v = f\lambda$ · FY5 (seisovat aallot, ääni; not published).
- F2 · E2 · O/OO. TVT: optional sound sensor.
- Equipment listed. Safety: hearing (loud tones).
- Gaps: "tutkit [ilmapatsaan resonanssia]".

**16. Muuntajan tutkiminen** · p. 10–11 · **printed twice**: one copy is a duplicate
- Physics: voltage ratio = turns ratio (ideal transformer), efficiency · FY7 (*Muuntaja ja sähköenergian siirto*, not published), FY6 power.
- F2 · E2 · O/OO. TVT: linear fit (voltage ratio vs turns ratio).
- Equipment listed. Safety: low-voltage supply only (in source), no secondary short circuit; **never mains-connected student coils**.
- Gaps: aim, "muodosta tuloksista [kuvaaja]", "Määritä … muuntajan [hyötysuhde]".

**17. Sähkömagneettisen induktion tutkiminen** · p. 11
- Physics: induced voltage vs rate of flux change, turns · FY7 (*Sähkömagneettinen induktio*, not published).
- F2 · E2–E3 · OO/I. TVT: voltage logging, peak or area of a voltage graph.
- Equipment listed. Safety: low.
- Gaps: aim.

**18. Vesivoimalaitoksen pienoismallin hyötysuhteen määrittäminen** · p. 12
- Physics: potential energy of water, power, efficiency · FY2 (*Hyötysuhde*), FY4 (*Vesi- ja tuulivoima…*), FY6 power.
- F2 · E3 · I. TVT: power calculation, graph of efficiency vs flow.
- **No equipment list in the source.** Safety: water and electricity together.
- Gaps: aim.

**19. Pudotuskorkeuden ja pomppukorkeuden välinen riippuvuus** · p. 12–13
- Physics: mechanical energy loss in a bounce, ratio of heights · FY4 (*Liike-energia…*, *Mekaanisen energian säilyminen…*).
- F1 · E1–E2 · OO/I. TVT: linear fit, slope as energy fraction; optional video.
- No equipment list (objects, rule implied). Safety: low.
- Gaps: aim, "kappaleen saavuttama [pomppukorkeus]". Good early investigation (theme 1–3).

**20. (Planckin vakio LEDeillä)** · p. 13 · **title missing in the source**
- Physics: photon energy $hf$, LED threshold voltage $eU \approx hc/\lambda$ · FY6 (*Puolijohteet, diodi ja LED*), FY8 (*LED, laserdiodi ja Planckin vakio*); none published.
- F3 · E2 · O/OO. TVT: linear fit ($U$ vs $1/\lambda$).
- Equipment listed. Safety in source: current-limiting resistor.
- Gaps: title, aim, "niiden toimintaan liittyvä [kynnysjännite]", "sopiva [kuvaaja]".

**21. Leikkiauton nopeus korkeuden funktiona** · p. 13
- Physics: energy conservation $v = \sqrt{2gh}$, losses; linearisation $v^2$ vs $h$ · FY4 (*Mekaanisen energian säilyminen ja energiaperiaate*).
- F1–F2 · E2 · O/OO/I. TVT: photogate, linearisation.
- Equipment listed. Safety: low.
- Gaps: aim, "mittaa auton nopeus samassa kohdassa rataa ." (how).

**22. Äänennopeuden määrittäminen** · p. 14
- Physics: $v = s/t$ or echo/two-microphone timing · FY1 (*Tasainen liike…*), FY5 (ääni).
- F1 · E2 · I (fully open). TVT: sound sensor timing or phone app.
- **No equipment list in the source.** Safety: hearing.
- Gaps: aim. Good independent-planning task with modest physics.

**23. Kaasun tilanyhtälön kokeellinen tutkiminen** · p. 14–15
- Physics: Boyle, Gay-Lussac, Charles; ideal gas · FY3 (*Kaasujen tilanmuutokset ja Boylen laki*, *Ideaalikaasun tilanyhtälö*, *Absoluuttisen nollapisteen määrittäminen*).
- F2 · E3 (several series combined) · OO/I. TVT: pressure/temperature logging, power fits and linearisation.
- Equipment listed. Safety: sensor ranges (in source), hot water baths.
- Gaps: "miten [kaasun tilanmuuttujat riippuvat toisistaan]", "yhteensopivia [ideaalikaasun tilanyhtälön] kanssa". Strong FY3 reverse link.

**24. (Taitekerroin)** · p. 15 · **title missing in the source**
- Physics: Snell's law, $\sin\alpha$ vs $\sin\beta$ slope = refractive index · FY7 (*Valon heijastuminen ja taittuminen*, not published).
- F2 · E1–E2 · O/OO. TVT: linear fit of sines.
- Equipment listed. Safety: laser (as 14).
- Gaps: title, aim, "Muodosta mittaustuloksista [kuvaaja]".

**25. Lämmön johtumisen tutkiminen lämpökameralla** · p. 15
- Physics: thermal conduction (qualitative comparison), emissivity · FY3 (*Lämmön siirtyminen, energiatasapaino…*).
- F1–F2 · E2 · OO/I. TVT: thermal camera, emissivity setting.
- Equipment listed. Safety: hot objects (in source).
- Gaps: aim.

**26. Hissin kulkeman matkan määrittäminen kiihtyvyydestä** · p. 15–16
- Physics: integrating $a(t)$ to $v(t)$ and $s(t)$, area under a graph, drift from offset · FY4 (*Kiihtyvyys ja tasaisesti kiihtyvä liike*, *Soveltava tunti: hissi…*).
- F2 · E3 · OO/I. TVT: phone acceleration app, numerical integration (spreadsheet or Graphical Analysis if verified).
- Equipment listed. Safety: low; permission to use the building's lift.
- Gaps: aim, "Määritä … hissin [nopeus] ja edelleen hissin [kulkema matka]".

**27. Hypyn tutkiminen voimalevyllä** · p. 16–17
- Physics: impulse = change of momentum, take-off velocity, jump height; compare with a second method · FY4 (*Liikemäärä ja impulssi*, *Newtonin toinen laki*, *Mekaanisen energian säilyminen…*).
- F2 · E3 · OO/I. TVT: force plate software, area under $F(t)$.
- Equipment listed. Safety: falls, landing; the last tip ("Huolehdi turvallisuudesta") is cut off.
- Gaps: aim, "Tarkastele muodostuvaa [voima–aika-kuvaajaa]", "esimerkiksi [lentoajan avulla]".

## Summary of problems found
- Every card lost its key phrase (usually the aim) and many lost values: the cards are plans for teachers, not
  publishable student texts. Rewriting is needed in any case.
- Duplicates in the PDF: *Kappaleen jäähtymisen tutkiminen* and *Muuntajan tutkiminen* (identical copies).
- Missing titles: the LED/Planck and the refraction investigations.
- Missing equipment lists: 6a–b, 7, 12, 18, 19, 22.
- **Safety values that must come from the real equipment before publication:** the heater current limit (2), laser
  class (14, 24), microwave procedure (11), lift use (26).
- Beyond the national modules: 6a–c (rotation); exponential models in 8 and 13 need maths support.
- Report template: the second way to estimate the slope's uncertainty is missing.
