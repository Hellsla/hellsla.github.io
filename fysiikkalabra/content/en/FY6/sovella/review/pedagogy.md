VERDICT: PASS
CONTENT-HASH: 5e15e967d1274d52

## Blocking
None. The English reads as a learning text. It follows the Finnish structure, and the terms are consistent: source voltage, terminal voltage, internal resistance R_int, dielectric strength, internal energy transferred as heat. The tasks demand application at module-end level.

## Polish
- fy6-s4 is the weakest task for independent application. It has no figure or source material, and parts a to c are formula applications. Part b's stem hands over the insight ("why is the fraction larger than the decrease in voltage?") and part c is a plain Q = CΔU step. Only part d (stored energy, safety, an idealised current) is a transfer. A short data line would raise it, for example the voltage read from a measurement.
- Several stems scaffold what the student should choose. fy6-s2 c says "check your reasoning by calculating". fy6-s2 d asks "why is the rated current of the fuse chosen according to the cable?", which gives away the idea the rubric rewards. fy6-s3 gives k and the dielectric strength in the text, which signals Coulomb's law (part d) and the sparking comparison (part a). Moving the constants to a "data" line without those hints, or dropping the "chosen according to the cable" clause, would give more independent choice.
- fy6-s2 d's wording "rated current ... chosen according to the cable" is awkward English. Suggest "why the fuse's rated current is chosen below the cable's permitted current".
- The set has no diode, LED or semiconductor task and no Kirchhoff multi-loop or charging circuit, although these are central contents of the course. docs/coverage/FY6.md is not in the packet, so I could not check whether those gaps are listed and closed. The teacher or coordinator should confirm this.
- The solutions headings "Hyväksytään myös" and "Yleisiä virheitä" are still Finnish in the English file, and the figure descriptions in figures.py are Finnish. Check that the English page shows them in English, via the lang keys or translated figure descriptions.
- Workload: four tasks of 14 to 16 points with 3 to 4 parts each is about 2 to 2.5 hours. That is acceptable for a 2 op module end, but it is not a single sitting.

## Checked
- Each task sets an authentic situation and rising demand (a graph and an error analysis; the cable, fuse and lamps; energy against force with air resistance; stored energy and safety).
- The tasks do not name the formula. s1 a leaves the choice of model and graph axes to the student, which is a good use of the graph competency.
- The rubric points are fair and observable, and none are awarded for irrelevant things.
- The s1 d drift (0.06 Ω) and scatter (0.08 Ω) estimates are consistent with the solution and with answers.py.
- The solutions follow the seven-step pattern, symbols before numbers, with reasonableness checks (the 30 W power balance in s2 and the energy balance in s3 are good).
- The common mistakes are real ones (R = P/U, forgetting the cable's voltage drop, kV not converted, ΔU² in the energy formula).
- Task figures carry no answers; fy6-s1-graph is only in the solution.
- practice.py check is OK. The hash is current.
