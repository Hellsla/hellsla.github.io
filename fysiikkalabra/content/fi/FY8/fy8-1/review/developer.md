VERDICT: DONE

Fix, round 1. `check_lesson.py fy8-1`: every line ok.

- `lesson.md`: intensity = photon rate only "samanvärisellä valolla" (science B); λ0 = 544 nm "vihreän valon keskivaiheilla", so red, yellow and yellowish green free none, blue-green, blue and violet do; h3 under "Kaava: Fotonin energia" renamed "Taajuus ja aallonpituus"; hc ≈ 1240 eV nm introduced after the 500 nm example by substitution, with a quick estimate; ”pallo”.
- `figures.py` → lesson.md: energia aria-label "metallin heikoimmin sidotun elektronin energia" (figures regenerated; `figcat.py build` left to the orchestrator, shared catalog).
- `inquiry.json`: sim `howto` opens with what eV is (1 eV = 1,602·10⁻¹⁹ J); sim `model` adds that the model's intensity is a photon rate and real equal-power short-wave light has fewer photons; koe-3 intro asks for a guess first (E_k,max vs shorter λ) and says the photon rate is equal at every λ in the model; tarkistus-1 feedback: power is energy per second, not photon count.
- `exit-ticket.json`: q2 replaced by intensity vs frequency (yellow 590 nm brightened vs blue 470 nm on sodium).
- `lesson-answers.py`: hc in J m; exit 590/470 nm energies.
- `sim.js`: faint beam from the lamp to the plate's lit face, so the light ends at the plate.
- `exercises/solutions.md` L1-03: "oranssin ja punaisen valon rajalla"; answers unchanged.
