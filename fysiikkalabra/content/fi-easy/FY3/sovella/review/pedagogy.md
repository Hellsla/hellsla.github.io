VERDICT: PASS
CONTENT-HASH: c75053d468fb5e32

## Blocking
None.

## Polish
- fy3-s3 c, Kaava: `\Delta p_\text{s} V_\text{s} = nRT` uses n for the amount of air used. It should be `\Delta n`, or the text should say "käytetyn ilman ainemäärä n". Then the step `\Delta p_\text{s} V_\text{s} = pV` follows without a jump.
- fy3-s3 b, Kaava: it is one line, while the other Kaava steps now start from a basic law. A first row `pV = nRT` with n and T constant would match them. This is not required.
- fy3-s1 b: the Kaava step does not say that P is the power the water receives. The Periaate step does say it, so this is minor.

## Checked
- The change is only in the Kaava step. Every Kaava now starts from a basic law and is solved in symbols before the numbers are substituted, as the read-through rule requires.
- fy3-s1 b: `Q = PΔt` and `Q = cmΔT` come first, then `P = cm·ΔT/Δt`.
- fy3-s1 c: `η = P_a/P_o`, `P_a = P` and `P_o = 800 W/m²·A` give `η = P/(800 W/m²·A)`.
- fy3-s1 d: the loss is found from `P = P_vesi + P_häviö`.
- fy3-s2 a: `p = p0 + Δp`, then interpolation.
- fy3-s2 c: `E = Pt`, `E_hyöty = ηE`, `Q = rm`, then `m = ηPt/r`.
- fy3-s2 d: `Q_luovutettu = Q_vastaanotettu`, then `cmΔT = r·m_h`.
- fy3-s3 a: `p1 = p0 + ρgh` and `pV = nRT` lead to `V2 = V1·(p1/p2)·(T2/T1)`.
- The tasks are unchanged and still demand independent application:
  - the situations are authentic (a collector's data table, a pressure-cooker table, a dive);
  - no part names the model;
  - the parts rise in demand;
  - the rubrics are specific and give no points for irrelevant things.
- The common mistakes are real, for example gauge pressure read from the table, Celsius used in the gas law, and ambient pressure left out.
- The workload suits a 2 op course, and the three tasks differ from each other (graph and data, phase change, gas law).
- I did not judge `docs/coverage/FY3.md`, because the packet does not carry it.
