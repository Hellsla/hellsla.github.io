VERDICT: PASS
CONTENT-HASH: fe2ecfbd0b95d72a
SCOPE: delta re-review of Sovella s4 b since my PASS at f9bba1ca0381a58c. The hash was debd72cf8d478220 at the start (only the question reworded to "kuinka lyhyen ilmavälin yli sähkö lyö varmasti läpi"). It changed during the review to fe2ecfbd0b95d72a (uncommitted edits to the question, solution and rubric of s4 b), so I judged that version again.

## Blocking
None.

## Polish
- The Polish points of my earlier report still apply (teacher.md point total "muut viisi … Yhteensä 95", the s7 ratio 2·10^10 vs 2,5·10^10, the s7 plate gap and vacuum remark, s8 c accepting about 125 Ω).

## Checked
- At debd72cf the question asked "kuinka lyhyen ilmavälin yli … lyö varmasti läpi", but the solution still said "pienin ilmaväli, jonka läpi sähkö voi lyödä" / "pienin väli, jonka läpi sähkö lyö … ≈ 4 mm". Read literally, that is wrong (a 2 mm gap breaks down too), and it did not match the question. The current version fixes this, so I am not reporting it.
- The current s4 b is "Arvioi, enintään kuinka pitkän ilmavälin yli sähkö lyö varmasti läpi." The solution's Kysytty and model answer say "pisin väli, jonka yli sähkö lyö varmasti läpi … ≈ 4 mm". The rubric's assumptions detail says "turvaetäisyyden alaraja, ei turvallinen etäisyys". The common-mistake line now calls 4 mm "vain väli, jonka yli sähkö lyö varmasti läpi tasaisen kentän mallissa". Question, solution, rubric and mistake list say the same thing.
- Physics: in a uniform field, a gap d < U/E_max breaks down. Near the thin conductor and the rod tip the field is stronger than U/d, and moisture and dirt lower the breakdown strength. Both effects make breakdown more likely, not less. So "certainly breaks through up to about 4 mm" is a correct upper limit for certain breakdown. The same number is a lower limit for any safe distance, because an arc can also form over longer gaps, as the solution says. No hidden condition (B) and no error (A).
- I recomputed: 20 kV/√3 = 11,5 kV ≈ 12 kV; d = 12 kV / 3 MV/m = 4,0 mm (11,5 kV gives 3,8 mm, same estimate); I = 12 kV / 10 kΩ = 1,2 A, which is more than 50 mA; the s4 a foot voltage is 0,30 Ω/km · 5·10⁻⁵ km · 100 A = 1,5 mV. All match answers.py (s4-gap-mm 4,0, s4-I-body 1,2, s4-feet-mV 1,5). The math criterion (12 kV, not 20 kV) and the 2 + 1 + 1 + 1 = 5 points are unchanged.
- The Finnish version (fi) has the same change ("enintään kuinka pitkän … läpilyönti tapahtuu varmasti", "pisin väli …", "turvaetäisyyden alaraja, ei turvallinen etäisyys"). fi-easy keeps the same physics.
- I ran `units.py hash --lang fi-easy`: debd72cf8d478220 at the start, then fe2ecfbd0b95d72a after the edit. I reviewed that version and checked the hash again at the end.
