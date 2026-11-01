VERDICT: FAIL
CONTENT-HASH: 94c81d5bb9ef34aa

## Blocking
- [Critical] simulation at 390 px (sim-390, exp-exp-1/2/3-390-1) — the canvas is drawn at desktop scale in the phone card: vaunu 2 is cut off at the right edge, and both bar charts collapse into one line where "$p$ (kg·m/s)", "$E$ (J)", "ennen", "nyt", $p_1$, $p_2$, $p_\text{kok}$ and the legend overprint. stage-tutki-390-1 renders the same sim correctly, so it depends on state (after *Aseta alkutila* or re-initialisation). — On a phone the three experiments, the core of Tutki, are unreadable. — Make the canvas re-measure its container whenever the sim is re-initialised or shown; if this is a capture-timing artefact, fix the capture and re-shoot before a PASS.

## Polish
- [Minor] fig tyypit — the purple arrows carry no $\overline{p}$ label, so only colour says they are momenta; the explosion spring is a barely visible tick — label one arrow $\overline{p}$ and draw the spring larger.
- [Minor] fig vuorovaikutus — the "$\Delta t$" label floats above the cars, tied to nothing — move it next to the force pair, for example "$\text{kosketusaika } \Delta t$", or drop it.
- [Minor] lesson.md Miksi kokonaisliikemäärä säilyy, Kimmoisa törmäys — two sentences read awkwardly or ambiguously → "Liikemäärä, jonka toinen vaunu saa, on täsmälleen yhtä suuri kuin liikemäärä, jonka toinen menettää." and "Kun tunnetaan yhden kappaleen nopeus törmäyksen jälkeen, toisen kappaleen nopeus saadaan liikemäärän säilymislaista, …"
- [Minor] Esimerkki (example-390-1/2) — Sijoitus writes units as $\tfrac{\text{m}}{\text{s}}$, while the rest of the chapter writes $\text{m/s}$, and in Kaava ratkaistuna the $v' = \dfrac{…}{…}$ row starts left of the two rows above it — use $\text{m/s}$ throughout and give all three rows one left edge.
- [Minor] experiment tables (lab-1280-1, exp-exp-3-390-2) — header units "(kg·m/s)" are set in sans text, while "(m/s)" and "(J)" are KaTeX; exp-3's sim shows an empty "Käytössä:" — set every header unit in maths and fill in or hide the empty label.

## Checked
- contact-1…6 for triage; fig-2-390, fig-3-390, fig-4-390; hero in intro-1280 and contact (#3)
- theory-1280-1…4 (all four figures beside or under their text, display maths, summary)
- sim-390, sim-1280, stage-tutki-390-1, lab-1280-1 (sim panel scrolls inside the sticky column: OK)
- exp-exp-1-390-1, exp-exp-3-390-1/-2; exp-2 and contact #28–#32
- example-390-1 (and #8 in contact), open-tarkista-1280-2, contact #43–#48 (ennusta, tarkista, exit open)
- lesson.md, inquiry.json, exit-ticket.json read in full; lint: no plain quantities

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 2
