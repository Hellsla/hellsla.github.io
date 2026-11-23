VERDICT: PASS
CONTENT-HASH: 3adb43b8f927fac3

## Blocking
- none

## Polish
- none

## Checked
- Round-1 Blocking fixed: the three Kaava steps that had been shifted by one task are back with their own tasks.
  - L2-04 (solutions.md:87) is $g = \dfrac{\Delta v}{\Delta t} = \dfrac{v_2 - v_1}{t_2 - t_1}$, which is the form its Sijoitus uses.
  - L3-01 (:97) is $v_1 = gt$, $v_2 = gt$, $\dfrac{v_2}{v_1} = \dfrac{gt}{gt} = 1$.
  - L3-02 (:107) is $g = \dfrac{\Delta v}{\Delta t} = \dfrac{v_1}{t_1}$, $v_2 = g t_2$, $t_2 = \dfrac{v_2}{g}$. It solves for the asked $t_2$ before the Sijoitus.
  - $\Delta v = v_1$ needs the stone to start from rest, and the Annettu states that it does.
- The en and fi-easy versions got the same three corrections.
- I recomputed the numbers myself and they agree with answers.py:
  - L2-04: $19{,}6/2{,}0 = 9{,}8\,\text{m/s}^2$;
  - L3-01: ratio $1{,}0$;
  - L3-02: $g = 3{,}70\,\text{m/s}^2$, $t_2 = 8{,}108\,\text{s}$, given as $8{,}1\,\text{s}$.
- The other changed steps are unchanged since round 1 and correct as judged then.
- The hash was 3adb43b8f927fac3 at the start and at the end.
