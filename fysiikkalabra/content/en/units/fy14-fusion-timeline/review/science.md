VERDICT: FAIL
CONTENT-HASH: c017b09db5bac17d

Science and history review of fy14-fusion-timeline and of the chapter 5 events in `assets/units/fy14/data/timeline.json` (1938–1989), 2026-11-01 (full review).

## Blocking
1. **`unit.md`, What the timeline shows, *Claims and checks* (A).** The text says the three claims "were announced before others could check them, and all were withdrawn". Only ZETA's claim was withdrawn (Cockcroft, 16 May 1958). Richter never retracted Huemul: the project was inspected, occupied and declared a fraud. Fleischmann and Pons never withdrew cold fusion either: other laboratories failed to reproduce it. Fix: "…and all failed when others checked them". This matches the Summary and Task 2's model answer.
2. **Shared: `timeline.json`, `jet-decision-1978`, date `1978-04-01` and its text "on 1 April 1978 the JET Joint Undertaking was set up" (A).** The dates come from EUROfusion's JET report (scipub.euro-fusion.org JETP98054, checked 2026-11-01). The Research Ministers chose Culham on 25 October 1977. The Council of Ministers agreed the arrangements on 30 May 1978 (Decision 78/471/Euratom, OJ L 151 of 7 June 1978), and the Joint Undertaking "came into being on 1st June 1978". The Wikipedia date of 1 April has no primary support. Fix:
   - Set the date to `1978-05-30`.
   - Use this text: "On 25 October 1977 Culham in England was chosen as the host site, and on 30 May 1978 the Council of Ministers set up the JET Joint Undertaking, which began work on 1 June."
   - Add the EUROfusion report as a source.
3. **Shared: `timeline.json`, `chicago-pile-1942` (A).** "Fission needed just over three years from discovery to a working reactor" is wrong. Fission was discovered in December 1938 and CP-1 went critical on 2 December 1942: four years. teacher.md of fy14-secret-fusion says it correctly. Fix: "about four years".

## Polish
1. **`inquiry.json`, sort-lessons, Kurchatov feedback.** It says "A Soviet leader described secret fusion experiments in Britain", which reads as a political leader and as experiments done in Britain. Fix: "The head of the Soviet atomic programme described secret Soviet fusion experiments in a lecture in Britain."
2. **Shared: `timeline.json`, `culham-five-1969`.** Add V. V. Sannikov to `people` and one clause to the text. He is the Soviet co-author of the *Nature* paper (Nature 224, 488, 1 November 1969, confirmed by Mike Forrest's publication list), and the clause shows the cooperation.

## Resolved developer flags (timeline.json)
- `tftr-1982` now says "approved in the mid-1970s". This is right: Wikipedia says January 1975 and PPPL says 1976.
- `jet-first-plasma-1983` no longer has the unsourced "on time and on budget" clause. No source I could reach (Wikipedia, gov.uk, EUROfusion) states it.
- Sannikov: see Polish 2.

## Checked
- **Counts:** recomputed from the data. The eras have 26, 23, 15 and 40 events. Politics is 9 of 23 in the nuclear age, devices are 8 of 15 in the tokamak race, and in the last era politics is 8 and devices 26. These match task-themes exactly. The events since 2015 come from seven countries. In the 1950s the events are in the US, UK and USSR, plus Argentina and Switzerland.
- **"Slow steps":** T-1 (1958) to JET's 16 MW (1997) is 39 years, at Q ≈ 0.67. Eddington (1920) to 2039 is 119 years. The 2039 date is dated as a plan.
- **Chapter 5 cards checked against sources** (Wikipedia: ZETA, Tokamak, Huemul, Stellarator, Toroidal solenoid, PLT, TFTR, JET, ITER; ITER Newsline; EUROfusion):
  - Thomson–Blackman: 8 May 1946, granted in late 1948.
  - Tamm–Sakharov: October 1950 and May 1951.
  - Huemul: 24 March 1951, 5–8 September 1952, November 1952.
  - Spitzer: May 1951, 50,000 dollars. Model A: early 1953.
  - Ivy Mike: 10.4 Mt, 74 t, about 1.9 km.
  - ZETA: August 1957, 24 January 1958, 16 May 1958, Rose.
  - Geneva: 1–13 September 1958. T-1: end of 1958. Culham: 1965.
  - Novosibirsk: 1–7 August 1968, 1000 eV, 50 × Bohm.
  - Symmetric Tokamak: December 1969 – May 1970.
  - US budget: 40 → 332 million dollars.
  - PLT: 20 December 1975; 24 July 1978, at night, with graphite limiter and Goldston at Innsbruck.
  - TFTR: 1980/1982. JET: 25 June 1983 and 9 April 1984. JT-60: 8 April 1985.
  - Geneva summit: 19–21 November 1985. ITER: Reykjavik and Vienna in 1987, CDA 1988–1990, EDA 1992–1998. Cold fusion: 23 March 1989.
- **Assessment:** both predictions, task-themes, find-error and checks 1–3 each have exactly one correct option. The match answers are right.

## Shared issues
Blocking 2 and 3 and Polish 2 are in `assets/units/fy14/data/timeline.json`. The two Blocking ones block this unit, because its timeline shows them to the student.
