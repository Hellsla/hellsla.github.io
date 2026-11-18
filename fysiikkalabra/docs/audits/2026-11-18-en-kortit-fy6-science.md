# Science review: English concept cards FY6 (`kortit/en/fy6.json`)

Date 2026-11-18. Reviewer: science agent. Scope: the 47 cards in `kortit/en/fy6.json`, checked against the Finnish
originals in `kortit/fy6.json` (same ids, `luku` and `aihe` agree on every card) and against the English lessons
`content/en/FY6/<luku>/lesson.md`. I did not edit any card.

**Overall verdict: FIX.** 40 cards PASS. 7 cards need a fix: 2 physics/consistency findings (Coulomb's law, Kirchhoff's
voltage law), 3 `kaava_puhe` readings that read the formula wrongly when spoken, and 2 terminology mismatches with the
lesson. Every decimal point is in English style (1.602, 3.6). The notation U_ch, R_s and W_battery matches fy6-9 and
fy6-16.

Classes: **A** = error, **B** = true only under a condition the card does not state, **T** = terminology or reading
mismatch with the lesson.

## FIX

| id | class | problem | suggested wording |
|---|---|---|---|
| fy6-coulombin-laki | A (consistency) | The lesson fy6-10 writes `F = k\,\frac{\lvert q_1 q_2 \rvert}{r^2}` (magnitude). The card has no absolute value, so with charges of opposite sign it gives a negative "force". The Finnish card has the same gap and should get the same fix. | maaritelma: "The magnitude of the force between two point charges." kaava: `F = k\dfrac{\lvert q_1 q_2 \rvert}{r^2}`. kaava_puhe: "F is k times the absolute value of q one times q two, divided by r squared" |
| fy6-kirchhoffin-jannitelaki | B | "The sum of the voltages around a closed loop is zero" holds only with signs (rises positive, drops negative). Stated without signs it contradicts the lesson's own example (9.0 V = 3.0 V + 6.0 V). Lesson fy6-5 says "the sum of the rises and drops of potential in a loop is zero". | "The sum of the rises and drops of potential around a closed loop is zero." |
| fy6-potentiaaliero | T (kaava_puhe) | "q times V A minus V B" sounds like qV_A − V_B. | "W A B is q times the difference V A minus V B, which is q times U A B" |
| fy6-latausvirta | T (kaava_puhe) | "U ch minus E divided by R plus R s" sounds like U_ch − E/R + R_s. Formula, U_ch and R_s are correct. | "I is U ch minus E, all divided by R plus R s" |
| fy6-latausaika | T (kaava_puhe) | "W battery divided by eta times P" sounds like (W/η)·P. Formula and W_battery are correct. | "t is W battery divided by the product of eta and P" |
| fy6-vikavirtasuoja | T | Lesson fy6-15 says "line conductor L" all through (live is used only for parts that are "live"). The card says "live and neutral conductors". "exceeds, usually, 30 mA" reads awkwardly. | "A protective device that compares the currents in the line and neutral conductors and cuts the current when their difference exceeds the tripping current, usually $30\,\text{mA}$." |
| fy6-elektronivoltti | T/B | "a charge equal to the elementary charge" leaves out the electron (−e). The Finnish says "alkeisvarauksen suuruinen", meaning the same size, and the lesson says "a charge of the magnitude of the elementary charge". | "The energy that a charge with the magnitude of the elementary charge gains when it moves through a potential difference of $1\,\text{V}$." |

## Recommended changes (not blocking, cards still PASS)

- fy6-kolmivaihesahko: P = 3UI is right only if U is the phase voltage (230 V). The lesson also gives 400 V between
  phase conductors, so a student could use 400 V. Suggested: "...with a balanced load (the same current I in each phase
  conductor, U the phase voltage) the power is three times that of a single phase." The bare adjective "Three-phase"
  is fine because the lesson uses only that form.
- fy6-suojamaadoitus: the card leaves out "runkovian" (a frame fault), and "trips the fuse" mixes up two devices.
  Suggested: "...along which the fault current of a frame fault returns to the supply and blows the fuse or trips the
  circuit breaker." This matches the fy6-15 summary.
- fy6-sulake: the lesson says "cable", not "wire": "...before too large a current heats the cable dangerously."
- fy6-suojausluokka: "device's plate" → "device's rating plate" (the lesson's wording).
- fy6-askeljannite: "which grows closer to…" → "which is the larger the closer one is to the point of contact".

## PASS (correct, matches the Finnish card, term matches the lesson)

fy6-sahkovaraus, fy6-alkeisvaraus (1.602·10⁻¹⁹ C), fy6-sahkokentta (E = F/q, lesson fy6-11), fy6-jannite,
fy6-varauksen-sailymislaki, fy6-sahkovirta, fy6-resistanssi, fy6-ohmin-laki (the lesson's "constant temperature"
condition is covered by "resistance is constant", level C), fy6-resistiivisyys, fy6-sarjaankytkenta,
fy6-rinnankytkenta, fy6-kirchhoffin-virtalaki, fy6-lahdejannite (no-load terminal voltage = emf, as in fy6-8),
fy6-sahkoteho, fy6-joulen-laki, fy6-kondensaattori, fy6-kapasitanssi, fy6-puolijohde, fy6-diodi (ideal one-way model,
level C), fy6-virtamittari, fy6-jannitemittari, fy6-mittausalue, fy6-virheraja (Δx = p·x + n·r as in fy6-2),
fy6-sahkoenergia (E = Pt = UIt as in fy6-7), fy6-kilowattitunti (3.6 MJ is correct), fy6-nimellisteho ("mains" as in
fy6-7), fy6-paristo, fy6-akku, fy6-akun-kapasiteetti, fy6-nimellisjannite, fy6-potentiaalienergia,
fy6-potentiaali, fy6-tasapotentiaalipinta, fy6-paasulake ("consumer unit" as in fy6-16), fy6-kuormanhallinta,
plus the five cards listed above under recommended changes (fy6-kolmivaihesahko, fy6-suojamaadoitus, fy6-sulake,
fy6-suojausluokka, fy6-askeljannite).

The level suits FY6 throughout. No card brings in physics from a later course.
