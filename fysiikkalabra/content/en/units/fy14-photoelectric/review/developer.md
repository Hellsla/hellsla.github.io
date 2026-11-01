VERDICT: DONE

Unit fy14-photoelectric, "Light as particles: the photoelectric effect" (FY14 chapter 1). Developer report 2026-11-01.
Content hash at hand-over: f66de27277e0e818 (`python3 scripts/units.py hash fy14-photoelectric`).

## Files changed
- `content/en/units/fy14-photoelectric/unit.md` — replaced the placeholder: Why question, hero, sections *The puzzle* {Puzzle}, Key idea, Formula: Einstein's photoelectric equation (with the stopping-voltage subsection and $h = e\,\Delta U_\text{s}/\Delta f$), *The people behind the equation* {People} (Planck, Einstein, Millikan, 60–100 words each, `<!-- photo: … -->` placeholders), staged Worked example (seven stages), Common misconception, Summary.
- `content/en/units/fy14-photoelectric/inquiry.json` — 24 activities: hook, retrieval choice; two committed predictions (red light at full intensity → revealed by exp-stop; brighter violet light → revealed by exp-intensity); sim with howto/model/calc; exp-stop (vary λ, intensity 100 % and sodium locked, student raises U until I = 0, records f, U, I; min 3); exp-intensity (vary intensity, λ = 400 nm, sodium, U = 0 locked; records I and E_k,max); word bank + sentence starters; pair conclusion (`after` both experiments); theory; `match` vocabulary component; biographies + optional pair comparison; reflect; worked example; interpret with example data (`source: example`, mercury lines) and a numeric task for h from two rows (answer 6.60 · 10⁻³⁴ J·s, two mistake feedbacks, complete solution); optional error-spotting choice (J/eV mix); misconception; three `tarkista` choices (concept, calculation, graph) with misconception feedback; explain/argue task with criteria; summary; French corner with a `say` component.
- `content/en/units/fy14-photoelectric/unit.json` — one-sentence description, nine sources checked 2026-11-01.
- `content/en/units/fy14-photoelectric/teacher.md` — timing for 75 min, organisation, assessment criteria, difficulties, extensions.
- `lessons/units/fy14-photoelectric/figures.py` (new) — `hero` (dark lab, bright red lamp and dim violet lamp on a sodium plate in an evacuated tube; electrons only under violet), `energy` (energy diagram to scale, 650 nm vs 400 nm on sodium: hf = W + E_k,max), `usf` (U_s against f for sodium and zinc from the model, labelled "model values", slope triangle h/e). English decimal point via `figlib.set_language({}, ".")`; every number computed from exact h, e, c.
- `assets/sims/fy14/photoelectric/sim.js` and `strings.json` — fixes:
  1. Physics/drawing: the plate signs were for an accelerating voltage (cathode −, collector +) although the battery and the model are a retarding voltage; now cathode +, collector −.
  2. `simState.f` is now in units of 10¹⁴ Hz (documented in the header), so the experiment table shows 6.66 instead of 666205462962963.
  3. Voltage slider 0–4.5 V (was 0–3 V, which could not stop caesium electrons below about 241 nm) in steps of 0.02 V (was 0.05 V).
  4. Label "Retarding voltage" → "Voltage $U = …$" so it no longer wraps at 1280 px; the howto box says it is the retarding voltage.
  5. Canvas labels moved clear of the light beam and the ammeter: λ and E = hf on the top line, cathode/collector and +/− under the tube, I beside the ammeter (they overlapped the beam and the circle at 360 px).

## Checks run
- `python3 scripts/units.py figures fy14-photoelectric` (up to date), `python3 scripts/units.py check` (all units ok), `python3 scripts/build.py fy14-photoelectric`.
- `python3 scripts/check_layout.py fy14-photoelectric --width 360` → OK; `--width 1280` → OK.
- `python3 scripts/screenshot.py fy14-photoelectric`; looked at the contact sheets, intro, figures (390/1280), sim, experiments, components and stages. Fixed from them: a match `<select>` wider than a phone (shortened options; LaTeX removed from options, which a `<select>` cannot render), two over-long formula rows, the comparison table (theory tables are `nowrap`, so the long-cell table was clipped at 1280 px; now short cells), the teacher timing table (now a list), figure label overlaps.
- By hand in the browser (python playwright on `preview/en/fy14-photoelectric.html`, no console errors): adapter params lambda, intensity, U, metal exist; *Set the initial state* of exp-stop sets λ 650 nm, 100 %, sodium, U 0 and locks intensity and metal; raising U in 0.02 V steps until I = 0 recorded rows 650 nm (f 4.61, U 0.00 V, I 0.00), 450 nm (6.66, 0.400 V, 0.00), 300 nm (9.99, 1.78 V, 0.00), matching the model (U_s = 0.395 V and 1.773 V); after two rows pred-red showed its feedback. exp-intensity at 30 % and 90 % recorded I = 6.00 and 18.0 nA, E_k,max = 0.740 eV both times, and revealed pred-bright. No `.katex-error` and no unrendered `$…$` on the page with every box open.
- `scripts/test_inquiry.py` and `scripts/check_latex.py` do not cover units (see below), so the checks above were done by hand.

## Numbers (computed in Python with h = 6.62607015e-34 J s, e = 1.602176634e-19 C, c = 2.99792458e8 m/s)
- Photon energies: 650 nm 1.91 eV, 530 nm 2.34 eV, 500 nm 2.48 eV (3.97e-19 J), 400 nm 3.10 eV, 250 nm 4.96 eV. Sodium (W 2.36 eV): threshold 525 nm, f₀ 5.71e14 Hz; E_k,max at 400 nm 0.74 eV. Zinc (4.3 eV): f₀ 10.4e14 Hz, threshold ≈ 288 nm ("about 290 nm"). Caesium f₀ 5.17e14 Hz.
- Worked example (405 nm, potassium 2.29 eV, rounded constants as written): hc = 1.9865e-25 J m, E = 4.905e-19 J = 3.062 eV, E_k,max = 0.772 eV → 0.77 eV, U_s = 0.77 V; K threshold 541 nm.
- Example table (invented, built from W = 1.90 eV and rounded): h = 1.602e-19 · 1.12 / 2.72e14 = 6.597e-34 J s; mistakes 4.12 (h/e) and 2.91 (one point).
- Model in the sim: I₀ = 20 nA at 100 %, so 30 % → 6.0 nA, 90 % → 18.0 nA.

## Facts verified (2026-11-01)
- Einstein's Nobel Prize in Physics for 1921, presented in 1922, "for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect" — nobelprize.org/prizes/physics/1921/summary and en.wikipedia.org/wiki/Albert_Einstein.
- Einstein born 14 March 1879 in Ulm, died 1955; in 1905 examiner at the Swiss patent office in Bern — Wikipedia (Albert Einstein). Light-quantum paper received by Annalen der Physik on 18 March 1905, published 9 June — Wikipedia (Annus mirabilis papers).
- Planck 1858–1947; presented the quantum hypothesis to the German Physical Society on 14 December 1900; at first rejected Einstein's light quanta; Nobel Prize for 1918 (received 1919) for the discovery of energy quanta — Wikipedia (Max Planck).
- Millikan 1868–1953; oil-drop experiment; a decade-long programme to test Einstein's theory, which he believed wrong; results 1914 confirming the equation, 1916 Physical Review paper "A Direct Photoelectric Determination of Planck's h"; still doubted the theory in 1916; Nobel Prize 1923 "for his work on the elementary charge of electricity and on the photoelectric effect" — Wikipedia (Robert Andrews Millikan) and Wikipedia (Photoelectric effect).
- Hertz 1887 (UV and sparks), Lenard 1902 (electron energy independent of intensity) — Wikipedia (Photoelectric effect).
- h exact 6.62607015e-34 J s (SI 2019) — Wikipedia (Planck constant); e exact by the same SI definition (from the brief, CODATA).
- Work functions — Wikipedia (Work function): K 2.29 eV (matches the sim), Cs 1.95 eV and Na 2.75 eV there, while the sim uses common textbook values Cs 2.14 and Na 2.36 eV. The text, sim model box and a source note say the values are typical and depend on the surface.

## Uncertain / for the reviewers
- "No delay": the page says electrons leave "as soon as the light is switched on". Wikipedia notes modern attosecond measurements show a finite (tiny) emission time; I kept the classroom statement and did not give a number.
- Millikan's "about ten years": Wikipedia says "decade-long experimental program"; the exact start year is not stated, so the text gives no start year.
- Sodium's work function differs between sources (2.28–2.75 eV); the unit uses the sim's 2.36 eV consistently.
- Photographs of Planck, Einstein and Millikan are marked `<!-- photo: max-planck -->` etc. for the photo thread.
- The violet colour `#7048e8` is the palette's momentum colour; here it means violet light (no momentum appears in this unit).

## Shared infrastructure (not edited; reported to the coordinator)
- `scripts/inquiry.py` renders `explain.pair` as Markdown text (`md(a["pair"])`), but `docs/fy14/writing-guide.md` says `"pair": true`; `true` crashes `build.py` (TypeError in `render_md`). I used a sentence.
- `assets/units/fy14/fx/match.js`: the `<select>` grows to its longest option and overflows a 360 px page; options are plain text, so `$…$` in options shows raw dollars. Needs `max-width:100%` on the select and a note in the header.
- `templates/inquiry.js` reflect list: the prediction prompts are copied as `textContent` of KaTeX output, so they show duplicated maths ("650 nm650\ \text{nm}650 nm"); visible in captures #15/#16.
- Theory tables use `white-space: nowrap`, so prose tables in a unit get clipped (scroll) at 1280 px.
- `experiment` names: `tex_name` does not treat λ as a symbol (it stays in the text font).
- `scripts/test_inquiry.py <id>` and `scripts/check_latex.py <id>` do not know units ("no lesson folder", "0 fragments"); there is no sim test for unit sims.
- `git status` shows `site/index.html`, `site/en/index.html`, `site/fi-easy/index.html` modified and untracked `site/*FY14*` files; I did not write them deliberately (`build.py fy14-photoelectric` reported writing to preview/), so they likely come from another thread or the build's index step.
