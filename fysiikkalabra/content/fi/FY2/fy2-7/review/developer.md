VERDICT: DONE

Round 1 (fix). check_lesson.py: all ok.
- lesson.md: Tulos rounding justified per datum (energy delivered 223 MWh three figures, loss 22 MWh two figures from 9,0 %); the check uses 22 MWh. Numbers with units in LaTeX (230 V, kV, TWh, %, summary). Both "sähköenergiana" and "lämpöenergiana" bold. District heating loss: temperature difference and leakage along the whole pipe length. Figures: label "muuntaja" with leader (grid); storage figure reads potentiaalienergia, pumppuvoimala, yläallas, alaallas.
- inquiry.json: hook in LaTeX; kertaus now recalls hyötysuhde; ennuste-1 drops "alueverkko", feedback for 25 % and half repaired; new Tutki item "sahko" (4 % of about 83 TWh next to district heat, same absolute loss, different share); jannite is a 10 MW example (0,80 / 0,026 / 0,0020 MW, same percentages) and asks to infer the percentages; johtopäätös updated; tarkistus-2 now 375 MWh at 75 % (wrong methods give 281 and 469, outside the tolerance), solution updated.
- lesson-answers.py: updated for all of the above.
Exercise set: see exercises/review/developer.md.
