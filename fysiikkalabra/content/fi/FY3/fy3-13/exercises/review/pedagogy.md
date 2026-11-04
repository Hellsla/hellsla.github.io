VERDICT: PASS
CONTENT-HASH: d63da7091321ba6b

## Blocking

## Polish
- exercises.json fy3-13-L2-07 — the task says "Pullon korkki vuoti hieman", but b) asks the student to deduce from the table that gas leaks: the diagnosis is given away before the student acts — word it as "Ryhmä epäilee, että pullon korkki vuotaa" and ask b) "Tukeeko taulukko epäilyä? Perustele kulmakertoimien avulla ja selitä, miksi vuoto vääristää tulosta." (also adjust solutions.md "miksi taulukko paljastaa vuodon").
- exercises.json fy3-13-L1-06, option 2 feedback and solutions.md Periaate — "liike ei lopu kokonaan" is a quantum-level remark the lesson does not teach (its glossary says only "pienimmillään"), and in the lesson's classical model option 2 reads as nearly true — change the feedback to "Väärin: kyse on pienimmästä mahdollisesta energiasta, ei siitä, että liike pysähtyisi sinulle tutun mallin mukaan; tarkka kuva kuuluu myöhempään kurssiin", or reword the option to a plainly wrong claim ("kaikki aineet ovat kiinteitä").
- exercises.json fy3-13-L1-07 — marked `"kind": ["concept"]` although it is a plain numeric conversion (and the same task type as fy3-3 L1-03) — drop the kind or add a conceptual prompt, e.g. ask also whether the result can be negative.
- solutions.md fy3-13-L2-06 Vastaus — "kolme merkitsevää numeroa, koska paine-ero $5{,}0\,\text{kPa}$ rajoittaa kulmakerrointa kahteen numeroon" contradicts itself — write "$-302\,{}^\circ\text{C}$ (kaksi merkitsevää numeroa riittäisi: $-3{,}0\cdot 10^2$, mutta tulos annetaan kokonaisina asteina)", or simply "$-302\,{}^\circ\text{C}$".
- solutions.md fy3-13-L3-04 Järkevyys — "Ääriviivat osuvat kumpikin samaan keskimääräiseen nollapisteeseen" is vague — say "Molempien sarjojen välin keskikohta ($-272\,{}^\circ\text{C}$ ja $-269\,{}^\circ\text{C}$) on lähellä arvoa $-273{,}15\,{}^\circ\text{C}$".

## Checked
- Counts 8/7/5; ids and levels fit the plan (concept MC, fit and extrapolation, different fit range, leaking vessel, extreme-line uncertainty, calibration and extrapolation).
- Recomputed all answers from the tables: $-274{,}5\,{}^\circ\text{C}$ (mean point, k 0,363), $-302\,{}^\circ\text{C}$ (group B), $-370\,{}^\circ\text{C}$ (leak), 10,7 °C (series B; A 29,75 °C), $-17{,}5\,{}^\circ\text{C}$ and 2,7 °C; all match; fitted slopes (0,363; 0,370) are right.
- L3-04 and L3-05 are YO-style multi-step tasks and use the lesson's extreme-line method and ekstrapolointi idea; the level fits, and the L3-05 contrast (short extrapolation vs. 270 °C) teaches a real point.
- Data tasks give the uncertainty and the method needed; no trap the lesson did not prepare.
- Solutions are staged, with sensible sanity checks (mid-point and other points against the line).
- L1-08 distractors (interpolation, repetition, line through every point) are real misconceptions with repairing feedback.
- Finnish and number+unit typography fine in the new tasks.
- No 360 px exercise capture in the packet; layout check passed; not judged further.
- Hash unchanged at the end.
