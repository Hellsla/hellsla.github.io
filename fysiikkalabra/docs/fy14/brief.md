# FY14 Road to Fusion — the teacher's brief (Lauri Hellsten, 2026-11-01, verbatim)

Authors of the course: Lauri Hellsten and Marjo Inkala. How the brief is implemented: `docs/FY14_PLAN.md`.

CLAUDE PROMPT — FY14: ROAD TO FUSION
Mission
Create and implement a complete, original, English-language interdisciplinary course:
FY14 — Road to Fusion
From the Birth of Modern Physics to ITER
The course combines three subjects:

* Physics: modern physics, nuclear physics and fusion energy
* English: CLIL-based scientific communication and critical thinking
* French: introductory language, culture and communication

Implement it directly into my existing Ruukkilabra website:
https://hellsla.github.io/fysiikkalabra/site/
Repository:
https://github.com/Hellsla/hellsla.github.io
This is a local upper-secondary course, not a national LOPS2019 physics module.
Build actual, usable student-facing learning materials. Do not stop at an outline, course plan or collection of placeholder pages.
All explanations, tasks, illustrations and simulations must be original. Research scientific and historical facts using reliable publicly accessible sources.
No additional course PDFs, textbooks or presentation files will be provided.
1. Start by inspecting the repository
Read `CLAUDE.md` and relevant project documentation.
Inspect:

* Existing course and lesson architecture
* FY1–FY4 lesson implementations
* FY8 and its planned content
* FY10 as an example of a local course
* The English-language site
* Existing styles and components
* Navigation, accessibility and test conventions

Follow existing conventions instead of building a separate course platform.
The course should appear in the existing local courses section.
Use the site's established learning philosophy:
Predict → Investigate → Understand → Apply → Check
However, adapt this structure naturally to historical investigations, video activities, laboratory work and language learning.
Do not force simulations into lessons where a historical source, photograph or discussion would be more educationally valuable.
2. Main educational vision
The entire course should gradually answer one central question:
If scientists have understood nuclear fusion for almost a century, why is producing electricity from fusion still so difficult?
The journey should move from the discovery of modern physics to the development of fusion reactors, showing how scientific discoveries, international politics, technological limitations and collaboration shape scientific progress.
Students should experience the course as a scientific investigation, not simply read an electronic textbook.
Target upper-secondary students. Use clear academic English, approximately B1–B2, without sacrificing scientific accuracy.
Students should practise physics, English and French throughout the course.
3. Course chapters
Use the following structure as a starting point. Divide chapters into suitable individual lessons.
Chapter 1 — The Birth of Modern Physics
Big question: Why did classical physics fail to explain everything?
Topics:

* Classical and modern physics
* Electromagnetic radiation and photons
* Blackbody radiation
* The photoelectric effect
* Planck and Einstein
* Rutherford's experiment
* Bohr's atomic model
* Atomic energy levels and emission spectra
* Quantum theory and tunnelling

Create an interactive historical timeline of modern physics.
Include accessible explanations and short original biographies of important scientists.
Create an interactive photoelectric-effect investigation or reuse a technically suitable existing component.
Use this resource for inspiration and cross-checking:
https://slides.com/opetustv/fy7-1-sahkomagneettinen-sateily-ja-fotonit/fullscreen?token=pt5NWEzs#/7/0/2
A historical reference:
https://archive.org/details/ThirtyYearsThatShookPhysics-TheBirthOfQuantamTheory
Do not reproduce copyrighted passages or diagrams.
Chapter 2 — Inside the Atom
Big question: How can such a small nucleus contain so much energy?
Topics:

* Protons, neutrons and electrons
* Atomic number and mass number
* Isotopes
* Nuclear notation
* Nuclear forces
* Binding energy
* Mass defect
* Einstein's equation E = mc²
* Nuclear fission and fusion
* Binding energy per nucleon

Interactive experiences:
Isotope Builder
Students change the number of protons and neutrons to investigate isotopes and nuclear notation.
Binding Energy Explorer
Create an interactive binding-energy-per-nucleon curve showing why fusion of light nuclei and fission of heavy nuclei can release energy.
Allow students to investigate selected nuclei and compare outcomes.
Include worked calculation examples with meaningful units and explanations.
Chapter 3 — The Energy of the Stars
Big question: Why hasn't the Sun burned out?
Historical storyline:

* Early theories about solar energy
* Why chemical energy cannot sustain the Sun for billions of years
* Gravitational contraction as an earlier explanation
* Arthur Eddington and the proposal that stars release energy through nuclear processes
* The proton–proton chain
* Quantum tunnelling
* The first experimentally observed fusion reactions

Physics:

* Fusion of light nuclei
* Hydrogen isotopes
* The proton–proton chain
* Deuterium–tritium fusion
* Coulomb repulsion
* Nuclear binding energy
* Mass–energy equivalence
* Energy released by nuclear reactions
* Why laboratory fusion differs from fusion in the Sun

Use the reaction:
²H + ³H → ⁴He + n + 17.6 MeV
Explain the energy carried by the helium nucleus and neutron.
Create an original interactive fusion reaction diagram and an activity comparing energy scales.
Include a conceptual calculation estimating how long the Sun can generate energy from hydrogen fusion, using clearly stated simplifying assumptions.
Chapter 4 — Plasma: The Fourth State of Matter
Big question: How can we control something hotter than the centre of the Sun?
Topics:

* Ionisation
* Plasma
* Plasma in nature
* Northern lights, lightning and stars
* Charged particles in magnetic fields
* Lorentz force
* Magnetic confinement
* Temperature, density and confinement time
* Plasma instabilities
* Why confinement is difficult

Create an interactive charged-particle simulation.
Students should be able to vary the magnetic field and particle properties and observe the resulting motion.
Distinguish illustrative single-particle motion from the much more complicated collective behaviour of fusion plasma.
Use interactive visualization to introduce the basic idea of magnetic confinement.
Chapter 5 — The Cold War and the Race for Fusion
Big question: How did the Cold War influence scientific research?
This should be one of the course's most engaging chapters.
Create a substantial historical narrative covering:
1920s–1940s

* Understanding stellar energy
* Early fusion research
* Particle accelerators
* Nuclear physics and World War II
* The connection between nuclear research, weapons and peaceful energy applications

1950s

* Scientific secrecy during the Cold War
* Ronald Richter's controversial fusion claims
* Government interest and funding
* British pinch experiments
* American stellarator development
* Soviet tokamak research

1950s–1960s

* ZETA and early experimental difficulties
* Z-pinch and theta-pinch concepts
* Lyman Spitzer and early stellarators
* Igor Tamm and Andrei Sakharov
* The first tokamaks
* Plasma confinement problems

1960s

* Soviet T-3 results
* International scepticism
* Independent British measurements
* The role of experimental verification
* The growing international popularity of tokamaks

1970s–1980s

* Advances in plasma heating
* Superconducting magnets
* Princeton Large Torus
* The 1973 oil crisis and energy research funding
* Larger national and international fusion experiments
* TFTR, JT-60 and JET

1980s onwards

* Reagan and Gorbachev's 1985 Geneva meeting
* The origins of ITER
* International cooperation despite geopolitical differences
* Scientific ambition, funding challenges and construction delays

Verify historical details and dates using reliable sources.
Interactive historical timeline
Build a visually attractive interactive timeline with authentic photographs, dates, countries, important scientists and key devices.
Students should be able to explore the timeline and understand how fusion research changed over time.
Include a CLIL investigation:
Science Across the Iron Curtain
Students investigate why Soviet and British scientists cooperated to verify experimental results despite political tensions.
Ask them to distinguish scientific evidence from political circumstances and explain why independent verification matters.
Chapter 6 — From Early Machines to Modern Reactors
Big question: Which reactor design has the best chance of making fusion work?
Teach the development of:

* Z-pinch and theta-pinch
* Early stellarators
* Tokamaks
* Modern stellarators
* Spherical tokamaks
* Inertial confinement fusion
* Modern superconducting magnets
* Alternative modern fusion concepts where scientifically relevant

Explain the key design choices in accessible language.
Compare advantages, limitations and unresolved engineering challenges.
Create an interactive Tokamak vs Stellarator explorer.
Show:

* Toroidal and poloidal field geometry
* The role of the plasma current
* How the helical magnetic field is generated
* Differences in magnetic-coil geometry
* Pulsed and steady-state operation
* Important limitations of each design

Do not imply that all tokamaks necessarily require inductively driven pulsed operation; explain alternative non-inductive current-drive techniques at an appropriate level.
Chapter 7 — ITER: An International Megaproject
Big question: Can the world's largest fusion collaboration succeed?
Explore:

* Why ITER was proposed
* Why international cooperation is necessary
* The selection of the Cadarache site in southern France
* ITER's participating members
* Design and construction
* Tokamak structure
* Superconducting magnets
* Central solenoid
* Vacuum vessel
* Plasma heating
* Divertor
* Tritium fuel cycle
* Radiation protection
* Technical and organisational challenges
* Scientific objectives

Include an illustrated interactive explanation of the major ITER components.
Create a clear explanation of fusion gain:
Q = P_fusion / P_external heating
Explain:

* Q = 1
* ITER's intended scientific gain
* The difference between plasma energy gain and electricity production
* Why achieving scientific gain does not automatically mean commercial viability

Verify ITER's current schedule, construction status and scientific objectives against current official information. Do not rely on older project schedules.
Sources:
https://www.iter.org/
https://www.iaea.org/topics/energy/fusion
ITER video assignment
Use this video:
https://www.youtube.com/watch?v=4BkOUOK0XzM
Create a complete CLIL activity:
Before watching

* Key scientific vocabulary
* Prediction questions

While watching

* Main ideas
* Important technical concepts
* International collaboration
* Construction challenges

After watching

* Comprehension quiz
* Pair discussion
* Source evaluation
* Short written explanation

Verify the actual video content before writing video-specific questions.
Also investigate these videos as possible supplementary resources:
https://www.youtube.com/watch?v=mZsaaturR6E
https://www.youtube.com/watch?v=EhAemz1v7dQ
https://www.youtube.com/watch?v=R-8NbYM1-ws
Embed useful videos directly into lessons when technically and legally permitted.
ITER journalism investigation
Use the historic Helsingin Sanomat article:
https://dynamic.hs.fi/2018/iter/
And relevant publicly accessible reporting, including:
https://yle.fi/a/20-153568
Create a media-literacy assignment:
ITER: Promise, Progress and Reality
Students read a selected article and write approximately 300 words addressing:

* ITER's scientific purpose
* Why fusion is technically difficult
* How energy is released in fusion
* What makes ITER an international project
* How its development has changed over time
* What the article says about the future of fusion

Include a comparison between historical reporting and verified current project information.
Chapter 8 — Fusion, Energy and Society
Big question: Could fusion become part of our future energy system?
Topics:

* Global energy demand
* Climate change and energy systems
* Energy production and reliability
* Fusion versus fission
* Environmental impacts
* Radioactive materials and neutron activation
* Fuel availability and tritium breeding
* Engineering and economic uncertainties
* Commercial development
* Public funding and private investment
* Fusion's potential role alongside renewable energy

Create a balanced evaluation task.
Students should practise distinguishing established scientific results from predictions and commercial claims.
Include a structured English debate:
Should governments invest more public money in fusion research?
Encourage evidence-based arguments on both sides.
4. The Fotoni laboratory visit
The course includes experimental modern physics at the University of Helsinki's Fotoni laboratory.
Official material bank:
https://www.helsinki.fi/fi/tiedekasvatus/opettajille/fysiikan-avoin-opetuslaboratorio-fotoni/fotonin-materiaalipankki
Identify suitable available experiments, potentially including:

* Photoelectric effect
* Emission spectra
* Electron charge-to-mass ratio
* Double-slit experiment

Verify the actual activities and equipment from Fotoni's resources.
Build an integrated Fotoni Lab Visit section.
Before the visit, students learn relevant theory and predict outcomes.
During the visit, they record observations and measurements.
After the visit, they analyse results, evaluate uncertainties and connect their findings to modern physics.
Provide a clear, printable or digitally usable laboratory worksheet.
Include English-language scientific reporting practice.
5. English language — CLIL throughout
The course should be written primarily in English.
CLIL must be a central learning principle, not an afterthought.
Integrate:

* Scientific vocabulary in context
* Reading authentic sources
* Listening comprehension
* Explaining diagrams
* Describing processes
* Comparing technologies
* Scientific argumentation
* Short written summaries
* Group discussions
* Critical source evaluation
* Oral presentations

Use sentence starters and word banks for more difficult tasks.
Examples:

* "The main difference between these designs is..."
* "The evidence suggests that..."
* "One possible explanation is..."
* "The experiment was important because..."
* "A limitation of this technology is..."

Not every exercise needs to be a quiz.
Create meaningful opportunities for students to discuss scientific ideas with each other.
6. French language and culture
French is an important part of this interdisciplinary course.
Assume some students are complete beginners.
The goal is practical, confidence-building language learning, not advanced grammar.
Connect French learning to France, international collaboration, scientific exchange and travel.
Include:
Introductions

* Bonjour / Bonsoir / Salut
* Comment tu t'appelles ?
* Je m'appelle...
* Comment ça va ?
* Où habites-tu ?
* Je viens de Finlande.
* Parles-tu anglais ?
* Je parle un peu français.

Numbers and prices

* Numbers 0–100
* Prices in euros
* Basic pronunciation

At a café

* Ordering a drink
* Asking about food
* Asking for prices
* Paying
* Thanking someone

At school or a research centre

* Introducing yourself
* Asking simple questions
* Explaining where you come from
* Asking for help
* Basic directions

French science and culture

* The location of ITER
* Cadarache and the surrounding region
* French scientific institutions
* International collaboration
* Everyday French interactions

Create interactive activities such as:

* Listening and matching
* Dialogue ordering
* Vocabulary matching
* Pronunciation practice
* Sentence completion
* Pair role-play
* Short cultural investigations

Use suitable authentic French videos where relevant.
Possible video resources:
https://www.youtube.com/watch?v=MBK7K1Xw3Lc
https://www.youtube.com/watch?v=O68Ql8Ux4iE
https://www.youtube.com/watch?v=AvHO3T7cyNI
https://www.youtube.com/watch?v=TcBelFXMpOE
Verify what each video contains before creating tasks.
French café role-play
Create a realistic café scenario in which two students practise ordering drinks and food and asking for the bill.
The activity should progress from supported dialogue to independent speaking.
Do not create an excessively long 20–30-question translation worksheet.
Include native or authentic pronunciation resources when legally usable.
Reading strategies
Create an activity where students encounter a short French news text and identify words they understand because of English or other languages they know.
Use original or appropriately licensed texts.
Students should discover that partial comprehension is possible even without speaking much French.
7. Final feature — Global Fusion Explorer
Build a substantial interactive world map titled:
Global Fusion Explorer
The goal is to visualise the geographic and historical development of fusion research.
It should contain a well-researched, broad selection of important existing, planned, under-construction and former fusion experimental facilities.
Explore authoritative information from IAEA, ITER, EUROfusion, national laboratories and other primary sources.
Include historically important examples where verifiable:

* ZETA
* Early Princeton stellarators
* PLT
* TFTR
* Soviet T-series devices
* T-3
* JET
* JT-60 / JT-60SA
* ITER
* ASDEX Upgrade
* Wendelstein 7-X
* EAST
* KSTAR
* DIII-D
* NSTX-U
* MAST-U
* WEST
* TCV
* Selected inertial confinement facilities
* Relevant modern private-sector devices

Research additional facilities globally.
Do not call the list exhaustive unless its completeness can actually be demonstrated.
Each facility should include

* Name
* Country
* Precise location
* Device category
* Years of operation where known
* Historical/current status
* Photograph if available
* Main scientific achievements
* Short explanation of its importance
* Reliable source link

Interactive features

* Clickable markers
* Zoom and pan
* Search
* Country filtering
* Reactor-type filtering
* Status filtering
* Historical timeline filtering
* Clear device information panels
* Ability to distinguish multiple devices at one site
* Accessible mobile and desktop layouts

Consider Leaflet and OpenStreetMap.
Store data in maintainable structured files, separate from presentation logic.
Include sources and verification dates.
Connect the map to the interactive history timeline.
Student activity
From Competition to Collaboration
Students explore the map and investigate how the geography of fusion research changed over time.
They should compare the distribution of fusion research during the Cold War with current international research networks.
8. Photography, design and media
This course should contain authentic historical and scientific photography.
Prioritise real photographs of:

* Scientists
* Historical laboratories
* Early experimental equipment
* Fusion reactors
* ITER construction
* Engineering teams
* Plasma experiments

Search:

* Wikimedia Commons
* ITER
* EUROfusion
* UKAEA
* PPPL
* IAEA
* NASA
* National research laboratories

Verify licences before reuse.
Store suitable licensed images in the repository and record:

* Original creator
* Source
* Licence
* Required attribution

Use informative captions and alt text.
Create original SVG scientific diagrams when photographs are unsuitable.
Avoid generic AI-generated science artwork, decorative imagery and visually misleading physics representations.
Follow the Ruukkilabra design system.
Make the interface feel like a modern, visually rich, interactive science textbook while remaining practical for classroom teaching.
9. Scientific quality requirements
Scientific accuracy is essential.
Independently verify all facts, historical milestones, formulae and calculations.
Pay particular attention to:

* Current ITER timelines
* Operating status of historical fusion facilities
* Fusion research records
* Difference between scientific gain and net electric output
* Inertial confinement versus magnetic confinement
* Plasma temperature and pressure
* Nuclear reaction equations
* Conservation laws
* Tritium radioactivity
* Neutron activation
* Reactor safety
* Fusion fuel availability
* Commercial readiness

Avoid outdated predictions about when fusion electricity will become available.
Explain uncertainty rather than presenting speculation as established fact.
Use reliable current sources and distinguish primary research results from institutional ambitions or corporate projections.
Add source references and verification dates where information may change.
10. Student learning experience
Create a coherent course, not ten disconnected collections of information.
A lesson should normally include:

1. An engaging scientific or historical question
2. Clear learning goals
3. An initial prediction or discussion
4. An investigation, source analysis or experiment
5. An accessible scientific explanation
6. One or more application tasks
7. A short understanding check

Use interactive exercises where meaningful.
Provide feedback explaining why an answer is correct or incorrect.
Make students think before displaying model answers.
Vary the location of correct multiple-choice options. Avoid predictable answer patterns.
Support different ability levels through hints, optional extensions and clear scaffolding.
Where sensible, include teacher guidance, recommended lesson activities and transparent assessment criteria.
11. Build and validation
Implement the actual course in the repository.
Use an appropriate development branch.
Preserve existing content and functionality.
Follow existing architecture and testing conventions.
Deliver:

* FY14 course landing page
* Complete student lessons
* Interactive diagrams and simulations
* Historical timeline
* Embedded video exercises
* English CLIL activities
* French activities
* Fotoni laboratory instructions
* Global Fusion Explorer
* Image attribution and references
* Teacher guidance
* Working homepage integration

Validate:

* Physics and mathematics
* Scientific sources
* Navigation
* Mobile responsiveness
* Wide-screen desktop layout
* Accessibility and keyboard controls
* Videos and image URLs
* Interactive quiz logic
* Map markers and filters
* GitHub Pages compatibility
* Existing automated tests

No placeholder buttons, dummy simulations or broken tasks.
12. Working approach
Start by inspecting the project, then create a clear internal implementation plan.
Proceed with actual code and course content.
Implement in logical stages:

1. Course architecture
2. Physics and historical content
3. CLIL activities and laboratory work
4. Interactive visualizations
5. Historical timeline and global map
6. Integration, fact-checking and testing

Document remaining limitations and unsupported facts explicitly.
Prioritise a complete, pedagogically useful course over an unnecessarily complex technological implementation.
Final objective
By the end, students should understand both the physics of fusion and the human story behind it.
They should know not only how fusion works, but also how the development of fusion research reflects the history of modern science, international politics, technological progress and global collaboration.
English and French should help students participate in that story.
The final result must be original, scientifically sound, visually engaging and ready for actual classroom use.
