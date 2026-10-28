VERDICT: FAIL
CONTENT-HASH: 109dbcc240d94859

## Blocking
- lesson.md:30 — Problem: "(noin 43 miljoonaa joulea)" puts a number with its unit in prose without LaTeX. This breaks the teacher's rule. — Fix: write "(noin $43 \cdot 10^{6}\,\text{J}$)" or "($43\,000\,000\,\text{J}$)".
- inquiry.json:194 (ruoka, Muunnokset) and exit-ticket.json:12 (q3) — Problem: "$100\,\text{g} = 0{,}100\,\text{kg}$" is stated as a bare equality, not a conversion by substitution. The exit ticket does the same with "$1500\,\text{kJ} = 1{,}5\,\text{MJ}$". The kJ step next to it on :194 does substitute. — Fix: write $100\,\text{g} = 100 \cdot (1 : 1000)\,\text{kg} = 0{,}100\,\text{kg}$, and the same for 1500 kJ.

## Polish
- lesson.md:53 — Problem: "bensiini (IPCC 2006: $44{,}3\,\text{MJ/kg}$, tyypillinen arvo pyöristettynä: $43$)" reads as if 44,3 rounds to 43. — Fix: cite a source that gives 43 (Tilastokeskus' moottoribensiini value), or write "IPCC 2006: 44,3; tyypillinen kaupallinen bensiini noin 43".
- inquiry.json:181 (hint 2), :249 (virhe, correct option); figure 3 (etiketti) — Problem: g → kg is shown as a bare equality. — Fix (optional): match the substitution form of the solutions.
- lessons/FY2/fy2-5/lesson-answers.py:23 — Problem: the comment "lesson.md:39" is stale; the line is now 51. — Fix: name the section ("Kaava, 3,0 kg bensiiniä") instead.

## Checked
- Hash 109dbcc240d94859 at the start and the end.
- Every lesson, inquiry and exit-ticket number was recomputed in one script and matches lesson-answers.py: 2,87; 90 MJ and 25 kWh; 22 MJ/kg; 1500 kJ; 129 MJ; the 15, 30, 60 and 120 MJ table; 170 and 430 MJ with a ratio of 2,5; 75 MJ and 15 MJ/kg; 3,75 and 3750 MJ; siirto 10,58, 6,35 and 4,23 MJ and 6348; 11,94 and 154,8 kWh.
- Figure 2 is to scale at 6,8 px per MJ/kg, with every bar within 0,4 px. Figures 1 and 3 are right.
- The worked example is symbolic first. Its kWh conversion substitutes $1\,\text{MJ} = 1\,\text{kWh} : 3{,}6$, its 2 s.f. are justified, and its check is real.
- Every correct option and every feedback is physically right. The food-label caveat (metabolisable energy is less than combustion) is right, and comparing 2200 kJ with 1500 kJ still holds.
- The data is realistic (LPG 46 MJ/kg, dry wood about 19 MJ/kg, Fineli food values).
- Scope: E = Hm, one efficiency, P = E : t and kWh. There is no chain product and no FY3 or FY4 content. No × appears, and written division uses a colon.
