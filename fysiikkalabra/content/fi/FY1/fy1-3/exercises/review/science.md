VERDICT: PASS
CONTENT-HASH: b767859bee6529a5

## Blocking

## Polish
- content/fi/FY1/fy1-3/exercises/solutions.md:140 (L1-08) — "Pienempi lukemaväli … joten työntömitta on tarkempi väline" infers accuracy from resolution alone. The guardrail keeps *resoluutio* apart from the manufacturer's error limit, which for a digital caliper is typically about 0,02 mm, larger than 0,005 mm. — Say that the ratio 100 concerns reading only, and that the caliper's total uncertainty is set by its stated error limit.
- content/fi/FY1/fy1-3/exercises/solutions.md:163 (L2-06) — "eli siinä on systemaattinen virhe" is stated as certain, while line 164 now says *todennäköisesti*. — Write "todennäköisesti systemaattinen virhe" here too.

## Checked
- Round-1 Blocking (L1-07, the invented digit) is fixed. The solution now says "5,428 cm olisi liian tarkka … tuhannesosien".
- New L1-08: 0,5 mm against 0,005 mm gives a ratio of 100, and answers.py gives the same. The task states the half-step rule for both instruments, and the digital rounding argument is right. The task stays within FY1 central contents.
- L2-05: 33⅓ rpm gives 1,800 s, which really is just outside 1,805–1,835 s. A slow turntable or a timing error is offered as a possibility, not stated as fact. This closes the round-1 Polish item.
- L2-06: the implausible pipette/cylinder pairing is removed. The rounding to hundredths now rests on ΔV_A = 0,15 ml. Deviation +0,94 ml.
- L3-04: the reason is the logbook entry, not the size of the deviation. Without the entry the result stays in the data: mean 2,48 s, half-range 0,295 → 0,30 s (×10). The deviation is reported and repeating is advised, as the outlier guardrail asks.
- L3-05: the gap is 0,04 g/cm³. The non-overlap is worded as "ilmoitetut epävarmuudet", and "ei todista kummankaan vääräksi" is kept.
- answers.py agrees with exercises.json for all 19 numeric tasks.
- The hash was the same at the start and the end.
