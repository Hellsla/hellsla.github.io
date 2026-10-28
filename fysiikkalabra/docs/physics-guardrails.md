# Physics guardrails

A short reference for writing and checking physics. It comes from the FY1–FY3 audit of 2026-10-28
(`docs/audits/fy1-fy3-physics-audit.md`). Every writer and every science reviewer uses it. Each rule names the
chapter where the mistake was found.

**How to use it.** Write the right claim once, in the same words, everywhere it appears: the theory, the summary,
the goals, each option and its feedback, the solutions, the rubric, the exit ticket, the sim's boxes and the figure
captions.

`scripts/physics_phrases.py` catches the known wrong phrasings:
- `lint_lesson.py` prints its hits as warnings.
- `test_physics_phrases.py` in CI fails when a known error is taught as fact again.

`scripts/concepts.py` collects one concept's passages from every chapter so they can be compared side by side.
Neither replaces the judgement.

## Kinds of finding
- **A, an error.** A wrong claim, model, number or cause, or a claim with no basis. Fix it.
- **B, a missing condition.** A claim that holds only under a condition the text does not state. Add the condition
  in as few words as you can.
- **C, a fair simplification.** It suits the level and leaves no wrong picture behind. Keep it.

Do not turn school physics into university physics. Do not flag "aina" or "ei koskaan" when the context is clearly
defined. A wrong option stays wrong on purpose. Its feedback must say why it is wrong, and exactly one option stays
correct.

## Measurement and data (fy1-3, fy1-4, fy1-8, fy3-13, FY1 Sovella)
**Keep the terms apart.** Each one names a different thing:
- **mittausvirhe**: the unknown difference from the true value; it has a sign.
- **mittausepävarmuus**: an estimate of how large the error may be; always positive and not a guaranteed limit.
- **resoluutio**: the smallest step the instrument can show.
- **hajonta**: how widely repeated results spread.
- **satunnainen, systemaattinen ja karkea virhe**: the three kinds of error.
- **keskiarvon epävarmuus**: the uncertainty of a mean.
- **valmistajan ilmoittama virheraja**: the error limit a manufacturer states for an instrument.

**Reading a scale.** Use these words: "Kun mittalaitteen asteikolta luetaan arvo, lukeman epävarmuutta voidaan
yksinkertaisessa tilanteessa arvioida esimerkiksi puoleksi pienimmästä asteikkovälistä. Mittauksen
kokonaisepävarmuuteen voivat kuitenkin vaikuttaa myös mittausmenetelmä, mittalaite ja muut virhelähteet." An
uncertainty can be larger than one scale division: a stopwatch shows 0,01 s, but hand timing is uncertain by about
0,2 s.

**Half the range.** Half the range of repeated results is a simple estimate of the scatter, chosen for that
exercise. Never call it the uncertainty of the mean. Repeating a measurement reduces random error, not systematic
error. The true value lies inside a range only *todennäköisesti*, never for certain.

**Outliers.** Use these words: "Selvästi poikkeava mittaustulos tarkistetaan ja mittaus voidaan tarvittaessa
toistaa. Tulosta ei poisteta pelkästään siksi, että se poikkeaa muista. Mahdollinen hylkääminen on perusteltava ja
dokumentoitava." A result may be left out when a gross mistake is found, for example a clock started late, and the
reason is written down.

**Fits.** Use this sentence: "Todellisissa mittaussarjoissa mittauspisteet eivät yleensä sijaitse täsmälleen samalla
suoralla mittausepävarmuuden vuoksi." Write *yleensä*, never *koskaan*.
- A fitted line may pass through a point.
- Read the slope from two points on the fitted line, never from two neighbouring raw points.
- A broken line through raw data is not a model.
- Extrapolation goes past the measured range, so say how far and why it is justified.
- A line through the origin needs a physical reason, for example time counted from the moment of release.
- A slope is only *likimain* a mean.

**Showing uncertainty.** The steepest and the shallowest line bound an *estimated* range. Say whether each number is
measured, simulated or calculated. When intervals overlap, a difference *cannot be shown*; that does not prove the
values are equal.

## State a law's conditions where it is used
- $Q = cm\Delta T$ holds only when the state of matter does not change.
- $p \propto T$ at constant volume holds for a thin gas far from condensing.
- $\Delta U = Q + W$: the change in internal energy equals the heat and work only when the system's kinetic and
  potential energy stay the same.
- "Same temperature, same internal energy" holds only for an ideal gas.
- The temperature stays constant during a change of state only for a pure substance at constant pressure.
- The linear expansion formulas hold for solids over about 100 K. A liquid's coefficient holds only near the
  temperature in the table.
- Heating is linear only while the heat losses are small.

## Particles, temperature and changes of state (fy3-3, fy3-5, fy3-7, fy3-13, fy3-14, fy3-16)
- **Temperature.** In an ideal gas, temperature measures the mean kinetic energy of the particles' motion from place
  to place. In solids and liquids it is mainly vibration. Temperature is not the same thing as internal energy:
  internal energy also includes the energy of the interactions between particles.
- **Absolute zero.** At absolute zero the particles' energy is at its lowest. Their motion does not stop entirely.
- **Melting and evaporation.** Use these words: "Sulamisen ja höyrystymisen aikana aineeseen siirtyvä energia muuttaa
  hiukkasten keskinäisiä vuorovaikutuksia ja kasvattaa niiden välistä vuorovaikutusenergiaa." The chemical bonds
  inside a molecule do not break. Part of the heat of evaporation is work done pushing back the surroundings.
- **Direction of energy.** Freezing and condensation release energy.
- **The boundary cases, stated exactly.**
  - The available energy is more than enough: all the ice melts and the water warms above 0 °C.
  - It is exactly enough: all the ice melts and the final temperature is exactly 0 °C (≥, not >).
  - It is not enough: ice is left and the mixture is at 0 °C.
  - Also keep the case where all of the water freezes.
  - Check every "jos riittää / ei riitä" pair, the captions and the sim's texts.

## Energy, heat and efficiency (fy2-1, fy2-4, fy2-5, fy2-8, fy3-2, fy3-11, fy3-12, fy3-15)
- **Heat is energy in transfer.** A body has internal energy, not heat. Friction turns mechanical energy into
  internal energy; it creates no energy. FY2 may say "lämpöenergia" as long as it does not contradict FY3.
- **Net transfer.** Use these words: "Lämpötilaeron vuoksi energiaa siirtyy nettomääräisesti lämpimämmästä
  kappaleesta kylmempään. Lämpösäteilyä lähtee kuitenkin molemmista kappaleista."
- **Efficiency limit.** Use these words: "Hyötysuhde on enintään 100 %. Todellisissa laitteissa se jää usein alle
  100 %, koska osa otetusta energiasta ei päädy määriteltyyn hyödylliseen käyttötarkoitukseen." What counts as
  useful, and where the system's boundary lies, decide the efficiency.
  - A resistance heater's efficiency is practically 100 %.
  - A heat engine running in a cycle cannot turn all the heat it takes in into work.
  - A heat pump has a coefficient of performance (lämpökerroin), not an efficiency.
- **Combined heat and power.** Keep the electrical efficiency, the total efficiency and the recovered heat apart. A
  loss "cannot be avoided" only where a law says so (the Carnot limit), and then only in part.
- **Food and fuel.** Use these words: "Sekä ruoan energiasisältö että polttoaineen lämpöarvo voidaan ilmoittaa
  yksikössä MJ/kg. Ruoan ravintoarvomerkintä kuvaa elimistön hyödynnettävissä olevaa energiaa, kun taas
  polttoaineen lämpöarvo kuvaa palamisessa vapautuvaa energiaa."
- **Carbon dioxide.** CO₂ comes from fuels that contain carbon. Hydrogen burns to water.

## Tasks, solutions and rubrics (FY3 Sovella, every exercise set)
- **Recompute every answer yourself.** An answer that agrees with its own solution can still use the wrong model.
- **State the model's assumptions in the task.** Examples: only steam under the lid, the food already at the pot's
  temperature, the air at the same temperature from the tank to the lungs. The solution uses the same assumptions.
- **A criterion asks only for what the task gives and asks.** A criterion cannot require a phase diagram when the
  student has only a table.
- **Safety statements are exact.** For scuba diving use these words: "Noustessa ei saa koskaan pidättää hengitystä:
  hengitetään normaalisti koko nousun ajan." Never write "breathe out all the time", and never present a simplified
  model as complete safety advice. A pressure cooker is opened only after the overpressure has been let out.
- **Numbers agree between chapters**, or the difference is explained. A figure generator holds the same numbers as
  the published figure.
