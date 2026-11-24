VERDICT: PASS
CONTENT-HASH: 4da5d6b6c0b16245

## Blocking

## Polish
- solutions.md (rail-gap task, $g_\text{max}$): the Kaava now writes $g_\text{max} + \Delta l_\text{talvi} = g_\text{raja}$, which is correct. Writing it as $g_\text{max} + \alpha l_0 \Delta T_\text{talvi} \le g_\text{raja}$ would show that it is an "at most" condition, matching the Periaate. This is optional.

## Checked
- The packet's diff shows the `aligned` blocks flattened. I read the real multi-row blocks on disk (for example solutions.md:55, 82, 97, 222 and 244).
- Every changed Kaava starts from the lesson's $\Delta l = \alpha l_0 \Delta T$ or $\Delta V = \gamma V_0 \Delta T$ and solves for the asked quantity. Each solves to the right result:
  - $l_0 = \Delta l/(\alpha\Delta T)$, $\Delta T = \Delta l/(\alpha l_0)$ and $T = T_0 + \Delta T$, $\alpha = \Delta l/(l_0\Delta T)$, $\gamma = \Delta V/(V_0\Delta T)$
  - steel ball: $\Delta V \approx 3\alpha V_0\Delta T$, with $\gamma \approx 3\alpha$ only for the solid, as the guardrail requires
  - hole in the wheel: $\Delta d = \alpha d_0\Delta T$, so the hole grows, which is correct
  - bimetal strip: $(\alpha_\text{Cu} - \alpha_\text{Fe}) l_0\Delta T$, factored correctly
  - fuel can: $\Delta V_\text{yli} = \gamma_\text{b}V_0\Delta T - 3\alpha_\text{t}V_0\Delta T$
  - thermometer: $h = (\Delta V_\text{e} - \Delta V_\text{pallo})/(\pi r^2)$
  - water column: $A$ cancels, so $\Delta h = \gamma h_0 \Delta T$
  - read-off accuracy, part c): $0{,}5\,\text{mm} \le 0{,}050\,\Delta l$ gives $\Delta l \ge 10\,\text{mm}$, and the inequality direction is right
- I evaluated each final form again with the task data: 52,1 m, 3,02 cm³, 36 °C, 12·10⁻⁶ 1/K, 120 °C, 20 µm, 457 cm³, 45·10⁻⁶ 1/K, 22,9·10⁻⁶ 1/K, 0,96 mm and 13 m, 75,8 mm, 53,3 °C, 3,43 mm/a and 60 mm. All match the unchanged Sijoitus.
- Powers of ten are right throughout: 10⁻⁶ for $\alpha$, 10⁻³ for $\gamma$, mm³ and mm² units consistent in the capillary task.
- The lesson's conditions on the laws hold: solids within about 100 K, and a liquid's $\gamma$ only near its table temperature or as given in the task.
- The hash was the same at the start and the end.
