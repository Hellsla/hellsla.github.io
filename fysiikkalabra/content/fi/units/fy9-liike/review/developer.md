VERDICT: DONE

Unit fy9-liike, "Liike kuvaajina" (FY9 chapter 3, order 1). Developer report 2026-11-04.
Content hash at hand-over: 365135079757531a (`python3 scripts/units.py hash fy9-liike`).

## Files
- `content/fi/units/fy9-liike/unit.json`: course FY9, chapter 3, order 1, kind review, 75 min, subjects physics; `sources` empty (all data are invented examples).
- `content/fi/units/fy9-liike/unit.md`: Why question (tram (t,v) graph, distance between stops), hero, `## Ydinajatus` (concept map, hook answer 450 m), `## Kaava: Liikkeen yhtälöt ja kuvaajat` (v_ka = Δx/Δt, x = x0 + vt, a = Δv/Δt, v = v0 + at, x = x0 + v0t + ½at², Δx = (v0+v)/2·t, x_A(t) = x_B(t), a = 2A from a quadratic fit; slope and area figure), `## Yleisiä virheitä {Virheet}` (7), `## Kertaa tarvittaessa {Kertaa}` (fy1-5, fy4-1, fy4-2, fy4-12, fy1-4, fy1-3). About 560 words.
- `content/fi/units/fy9-liike/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-liike/sovella/tasks.json`, `solutions.md`; `lessons/units/fy9-liike/sovella/answers.py`, `figures.py` (model graph of s3).
- `lessons/units/fy9-liike/figures.py`: `hero` (tram), `kartta` (concept map), `kuvaajat` ((t,x) and (t,v) pair with tangent and area), `ratikka` (Tutki graph, pasted into inquiry.json by `paste_ratikka()`).

## Counts
- Pohdinta: 1 hook. Ennusta: 6 choice (diagnostic, each option names the chapter). Tutki: 1 interpret (tram (t,v) graph, `source: example`, numeric 450 m).
- Teoriatiivistelmä: 1 theory activity.
- Sovella: 4 choice (average speed 30 km/h, graph shape, tangent `fy4-2/ex-tangent` 4,0 m/s, who is ahead), 4 numeric (scooter `fy4-2/ex-tv` 22,5 m, moose braking 46,8 m, dog 8,0 s, baseball −1,81 m/s), each with solution, hints, mistakes.
- Tarkista: choice, numeric (lift 16,0 m), explain ((t,v) intersection vs meeting); `practice` links on all three; exit ticket (54 km/h = 15 m/s; a = −2,0 m/s²).
- Tehtävät: 6 tasks, 95 points: s1 Kiihdytyskaista (calc, 15), s2 Kaksi palloa aulassa (calc, 15), s3 Lähijuna saapuu asemalle (data → graph → fit → interpret, 20), s4 Keskinopeusvalvonta (word, 15), s5 Kärry kaltevalla radalla (experimental report critique + design, 15), s6 Pudotus puhelimen videolla (cross-module FY1 fit/uncertainty + FY4, 15).

## Numbers (computed in Python: answers.py, scratch generators)
s1 12,0 m/s; 1,25 m/s²; never level within the lane (discriminant −43,75), lead 17,5 m; overtaking 15,4 s at 307 m. s2 8,84 m/s; meeting 0,625 s at 7,08 m; velocities 5,87 and −6,13 m/s. s3 fit k = −2,3125 km/h/s, b = 112,75 km/h; read slope −0,645 m/s²; braking starts 9,8 s, stops 48,8 s; braking distance 481 m (read), 487 m (fit). s4 81,8 km/h; ±0,59 km/h (3,0 km) vs ±17,8 km/h (100 m). s5 a = 0,94 m/s² (range 0,74–1,22). s6 A = −4,44 m/s² → g = 8,88 ± 0,10 m/s²; scale-corrected 9,77 m/s²; two-point 8,92 m/s². Inquiry: Tutki 450 m; scooter 22,5 m; moose 46,77 m; dog 8,0 s; baseball −1,81 m/s; lift 16,0 m.

## Checks
- `units.py figures fy9-liike`, `practice.py figures units/fy9-liike`: up to date. `practice.py check units/fy9-liike`: OK, 6 tasks, 95 points. `units.py check`: no errors for this unit (errors only in other units in progress).
- `build.py fy9-liike`: writes `preview/fy9-liike.html` and the preview index pages; no mixer crash this time.
- `check_layout.py fy9-liike` at 360, 390, 1280 px: OK.
- Playwright at 390 and 1280: all 11 choices answered correctly with feedback, 6/6 numeric "Oikein", explain model and all solutions opened; no console errors, no `.katex-error`, no raw `$`, no horizontal scroll. `screenshot.py fy9-liike --no-build` captures looked at (hero, map, kuvaajat, Tutki, s3 model graph); fixed label overlaps, overflowing key text and small labels (s3 graph redrawn 440 wide).

## Open questions
- No real data: the train, tram, cart and video data are invented and marked `source: example`. A reviewer may want one real measurement series.
- Sovella reuses catalog figures `fy4-2/ex-tv` and `fy4-2/ex-tangent`; check that their numbers stay as quoted (22,5 m, 4,0 m/s).
- The Tutki graph is an inline SVG pasted into inquiry.json (regenerate with `PYTHONPATH=scripts python3 lessons/units/fy9-liike/figures.py`), as in fy9-energia.
- teacher.md headings keep plain "min" times (preview only, as in fy9-energia).

## Shared issues
- figcat ids cannot name a unit's own figures, so a unit figure in inquiry.json has to be pasted as SVG.
- Seen in passing (not this unit): `check_layout.py` over all previews fails fy9-voimat at 360 px (svg-text overlap).

## Round 1 fixes
Content hash after the fixes: d1021d5831c47cfe.

### Science
1. **Blocking, s6 geometry.** Fixed. The metre stick now stands on a tripod $3{,}00\,\text{m}$ from the camera, and the ball falls $0{,}30\,\text{m}$ behind it, $3{,}30\,\text{m}$ from the camera. Solutions c (Annettu, Periaate, $d_\text{mitta}$) and the part c criterion say "metrimitan tasossa" instead of "seinän tasossa". The numbers are unchanged.
2. **Blocking, s2 source_note.** Fixed. Removed "mikä sopii raskaalle pallolle näin lyhyillä matkoilla". The note now says only "Ilmanvastus jätetään huomiotta."
3. **Polish, s1 d.** Fixed. The text now says "kiihdyttää … tasaisesti koko kaistan matkan, mutta vain nopeuteen $72\,\text{km/h}$". The solution says the same.
4. **Polish, unit.md "Kaksi kappaletta".** Fixed. Added "ja kiihtyy".
5. **Polish, s4.** Fixed: "$3{,}0\,\text{km}$:n suoralle tieosuudelle".
6. **Polish, `kuvaajat` tangent colour.** Fixed (see Visual 1).

### Pedagogy
1. **Blocking, s6 source_note and optics sentence.** Fixed. The note is now "Mittaus ja luvut ovat keksittyjä esimerkkejä." The optics sentence is cut from the task text and remains only in the Periaate of solution c.
2. **Blocking, s3 source_note.** Fixed. It now reads "Aineisto on keksitty esimerkki, johon on lisätty puhelimen paikannuksen kaltaista vaihtelua."
3. **Blocking, `keskinopeus` option lengths.** Fixed. The distractors are longer and the correct option is now first. Raw lengths are 97, 94 and 85 characters; rendered, the LaTeX option is the shortest.
4. **Polish, option positions.** Fixed. The correct options in Ennusta are now at positions 1, 3, 2, 1, 3 and 4. In `tarkistus-1` the correct option is third and no longer the longest (52/58/56).
5. **Polish, s1 d rubric.** Fixed. The 2 p criterion now requires the quantitative step: $15{,}4\,\text{s}$ at an average speed of $17{,}5\,\text{m/s}$, so the truck gains about $5\,\text{m/s}$ and makes up about $77\,\text{m}$, which is more than $40\,\text{m}$. The model answer adds this step.
6. **Polish, repetitive area items (replace the lift).** Not done in this round. A graph-conversion check needs a new figure, new mistakes and a new solution, so it is not a cheap change. Proposed for round 2.
7. **Polish, `rata` with graph options.** Not done. It needs four option figures, and the choice schema with SVG options has not been tested in units. Proposed for round 2.
8. **Polish, Tutki scaffolding.** Fixed. The text no longer names the three phases or "kussakin vaiheessa"; the phases remain only in hint 2.
9. **Polish, teacher.md.** Fixed. The fast-student extension is now new: the area between the two parallel $(t,v)$ lines up to the passing time equals the initial distance, $12\,\text{m/s} \cdot 0{,}625\,\text{s} = 7{,}5\,\text{m}$. Sovella now names the two items to leave for home (*Hirvi tiellä*, *Koira ja juoksija*).

### Visual
1. **Blocking, `kuvaajat` tangent.** Fixed. The tangent and the dotted line to $v_\text{P}$ are velocity blue. The label is now "$k = v_\text{P}$", in blue, right of the tangent's end and clear of the curve. The text says "tangentin kulmakerroin $k$".
2. **Blocking, `kartta` colours.** Fixed. Each row uses its quantity's colour: $(t,x)$ ink, $(t,v)$ blue, $(t,a)$ orange. Solid means tasainen and dashed means tasaisesti kiihtyvä, and the key uses ink. The alt text is updated.
3. **Blocking, label size at 390 px.** Measured in Playwright at a 390 px viewport. The smallest effective label size, computed as the font size times the rendered width divided by the viewBox width and confirmed by the KaTeX box heights, is 16,1 px in `kartta` and 17,1 px in `kuvaajat`. In the s3 graph it was 14,9 px; I raised that figure's size from 22 to 24, so it is now 16,3 px. All labels are at or above 14 px, so the 9–10 px reading is probably a device-pixel or contact-sheet measurement.
4. **Blocking, `aineisto` wording.** Fixed: "Kuvaajassa on raitiovaunun nopeus pysäkiltä seuraavalle pysäkille." The exit ticket did not contain "alun".
5. **Polish, $s$ against $x$.** Fixed. unit.md (Virheet, Kertaa) and the inquiry `prior` item now use $x = x_0 + vt$ and $(t,x)$.
6. **Polish, shared fy4-2 figures.** Not this unit's file. They are at 13,0 px at 390 px. Listed under Shared issues.
7. **Polish, s3 label "$k$".** Fixed. It moved to free space at about $(27\,\text{s};\ 76\,\text{km/h})$. The "48,5 s" label is now muted ink instead of orange, and it moved up so that it does not hit "$t\ (\text{s})$" at 1280 px.
8. **Polish, s6 frame rate.** Fixed: "joka kolmannesta kuvasta eli $0{,}05\,\text{s}$:n välein".
9. **Polish, hero road edge.** Not changed (optional).

### Checks after the fixes
`units.py figures`, `practice.py figures` written; `practice.py check units/fy9-liike` OK (6 tasks, 95 p); `units.py check` no fy9-liike errors; `build.py fy9-liike` OK; `check_layout.py` 360, 390, 1280 OK. Playwright 390: 11/11 choices answered with feedback, 6/6 numeric "Oikein.", no console errors, no `.katex-error`, no raw `$`, no horizontal scroll (also at 1280). Looked at `kartta`, `kuvaajat` and the s3 graph at 390.

### Shared issues (added)
- `fy4-2/ex-tangent` and `fy4-2/ex-tv`: the tick labels are 13 px at 390 px (viewBox 600, size 24), below the 14 px rule.
