VERDICT: DONE

Round 1 draft. No simulation (a table, graphs and a model to build); check_lesson.py all ok at 360, 768 and 1280 px.

- lesson.md: Ydinajatus (gas-thermometer figure), Kaava: Nollapaineen lämpötila (p = p0 + kθ, θ0 = −p0/k, Δθ0 from extreme lines; full-range graph with extrapolation and interval), staged Esimerkki (7 data points, θ0 = −276 ± 16 °C), misconception, summary. All figure labels are LaTeX fig-tex boxes.
- inquiry.json: hook, retrieval, two predictions (competing models; accuracy), three interpret steps (data with error bars, line to zero pressure, extreme lines), theory, reflect, example, error-spotting, transfer, exercises, three checks, exit ticket. No lesson ids in student text.
- exercises.json (5/4/3), answers.py (every answer computed), solutions.md, exit-ticket.json.
- glossary.json: added ekstrapolointi and mittausepävarmuus (Edit insertions), fy3-13 on absoluuttinen nollapiste.

Notes: solutions.md uses LaTeX for calculations (teacher's rule), so lint gives one warning that NOTES says plain text; the Vastaus line stays plain for the lint. Predictions have no `reveal` (no experiment without a sim), so feedback shows after commit and points to the data. Numeric answers inside inquiry.json (not in answers.py): −276, 15,7, −277, −283 were checked by hand.
