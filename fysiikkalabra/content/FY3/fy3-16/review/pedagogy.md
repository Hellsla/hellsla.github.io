VERDICT: PASS
CONTENT-HASH: 1d83eaa86fe1d6a7
## Blocking
None. (The packet shows "FAIL lint"; run now, lint_lesson.py gives 0 errors and 3 warnings: solutions L3-01..03 are 142, 157 and 217 words, limit 120. The packet result looks stale or counts warnings; shorten those solutions.)
## Polish
- Slot goal is three everyday cases (sauna, kylmälaukku, jäähdytysneste), but the core path investigates only the cooler bag; sauna sits in the optional loyly/siirto/check-3 and the coolant appears only in lesson text and exercises L1-05/L2-03. Add one short core item on coolant (e.g. flow rate from P = c(m/t)ΔT) or accept that the other two are practised in Tehtävät.
- inquiry.json kayra — answer 333 kJ with 4 % tolerance depends on reading 3,7 h from a one-hour grid; a student reading 3,5 h (315 kJ) is marked wrong. Give the plateau end in the text or raise the tolerance to about 8 %.
- lesson.md kuvaaja vs inquiry.json kayra — both show "1 kg ice, 28 °C" but one plateau is 2,4 h (UA 1,2 W/K, with drinks) and the other 3,7 h (UA 0,90 W/K); state UA and the drinks in the lesson graph's caption so students do not think one is wrong.
- inquiry.json hook — "Alussa seinän läpi tulee koko ajan sama teho" already gives pred-1's reasoning; ask the question without the hint and let Cem's answer be the student's discovery.
- exit-ticket.json item 2 repeats check-2's two-target calculation; swap for one on coolant/massflow to cover the third context.
## Checked
Core path clear: hook, 2 predictions (pred-1 models Aino/Bea/Cem/Dan, correct once; pred-2 refutes the tempting "−50 %" model by the table), kayra, taulukko, conclusion (explain, no experiment so no `after`; model answer only after own text; the model answer and both data items say "mallilla laskettu/esimerkkiarvot", `source: model`), 2 checks, exit; kertaus, loyly, reflect, Etsi virhe, siirto, check 3 in Valinnainen. Taulukko asks a Pt product per row: workable on two rows. Example staged, differs from the investigation. Exercises L1–L3 progress; Finnish good. No captures; judged from text.
