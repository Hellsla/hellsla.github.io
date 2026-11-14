VERDICT: PASS
CONTENT-HASH: 18715801cb2d4975

## Blocking
- none

## Polish
1. answers.py docstring and comments still write P₀ and P_hyöty; use P_o and P_a as the chapter does (carried from the previous report).
2. L1-09: Answer gives c at 20 °C for hot district-heating water; one clause that c of 60-100 °C water is about 4,19-4,22 kJ/(kg·K) (still inside 4 %) would make the lookup honest (carried from the previous report).

## Checked
- Hash 18715801cb2d4975 at start and end, unchanged.
- Delta: L3-01 Järkevyys, fi solutions.md:179. "kaukolämpö vain lämmitykseen" is now "kaukolämpöä käytetään pääasiassa lämmitykseen". This fixes a claim that was too absolute (category A: district heat also serves domestic hot water, some industrial process heat and absorption cooling). The new wording matches the lesson's Yleinen virhekäsitys ("kaukolämpöä pääasiassa lämmitykseen") and the guardrail on CHP (keep the value of electricity and heat apart).
- en solutions.md:179 ("district heat is mainly used for heating") and fi-easy solutions.md:179 (the same claim split into short sentences) say the same thing as fi. No "vain lämmitykseen" or "only for heating" is left in any language's exercise files.
- The numbers in the context are unchanged, and I recomputed them: k = 60/348 = 0,17241, P_s = 205,5 MW, which rounds to 206 MW, and η_kok = 67,6 %. They agree with the solution.
- The conclusion still holds: an added total efficiency does not decide profitability, which depends on demand and prices.
