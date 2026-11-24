# ITER: promise, progress and reality

> **Why** can a news article about ITER be well researched and still give a wrong picture a few years later?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Illustration: on a wooden table lie an old, slightly yellowed newspaper page and a modern tablet. Both show a picture of a doughnut-shaped fusion machine with a glowing pink plasma, and columns of text drawn as grey lines. A large magnifying glass rests over the tablet&#x27;s picture, and a pencil lies beside the newspaper, as if someone is comparing the two articles." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy14/fy14-iter-media-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## ITER then and now {ThenNow}

Facts about a project under construction change. The table compares ITER's own official information in 2018, when Helsingin Sanomat published its large story, with the official information in November 2026.

| Topic | Official in 2018 | Official in November 2026 |
| --- | --- | --- |
| first plasma | 2025 (2016 baseline) | research operation 2034 (2024 baseline) |
| $\text{D–T}$ operation | 2035 | 2039 |
| construction | "halfway" to first plasma (December 2017) | 6 of 9 vessel modules in the pit (July 2026) |
| cost | about €20 billion (2017 estimate) | about €5 billion more for repairs and changes (2024) |
| wall facing the plasma | beryllium | tungsten (decided 2023, part of the 2024 baseline) |
| Members | seven; the UK through Euratom | seven; the UK has left, Switzerland is back through Europe (2026) |
| Director-General | Bernard Bigot | Pietro Barabaschi (since 2022) |

<figure class="unit-photo"><img src="units/fy14/pics/iter-tokamak-pit.jpg" alt="Colour photograph of the concrete ITER tokamak building under construction with cranes." width="1600" height="1030" loading="lazy"><figcaption>The ITER tokamak complex under construction in April 2018. The tokamak itself is assembled inside the central building. <span class="photo-credit">Photo: Oak Ridge National Laboratory, CC BY 2.0, via Wikimedia Commons</span></figcaption></figure>

<figure class="unit-photo"><img src="units/fy14/pics/iter-visit-hellsten.jpg" alt="Colour photograph of a man in a yellow hard hat and safety vest standing on a balcony above the ITER tokamak pit, where a tall grey cylindrical structure rises among pink-wrapped components and scaffolding." width="1262" height="947" loading="lazy"><figcaption>Course author Lauri Hellsten visiting the ITER tokamak pit on 26 March 2024. The tall cylinder in the centre is a support structure in the middle of the machine; the pink-wrapped parts are protected components waiting for assembly. <span class="photo-credit">Photo: Lauri Hellsten</span></figcaption></figure>

Construction has also moved on elsewhere in the machine: in June 2026 all six modules of the central solenoid were stacked.

Some things have **not** changed: ITER's scientific goal ($Q = 10$, $500\ \text{MW}$ of fusion power from $50\ \text{MW}$ of heating), the site at Cadarache, the seven Members, and the physics of fusion. An article from 2018 that reported the plan of 2018 was correct at the time; a reader in 2026 must update the dates, the costs and the construction status.

```pysahdy
A newspaper of 2018 wrote that ITER's first plasma would come in 2025. Was the article wrong?
---
Not at the time of writing, because 2025 was the official plan then. The plan was replaced in 2024, so a reader today must check the newest baseline.
```

## Key idea

Reading about science in the news needs three questions.

1. **When was it written, and which plan does it report?** A date for the future is a plan of its time. Check it against the newest primary source, such as ITER's baseline.
2. **What kind of claim is it?** A **result** has happened or been measured ("the site was chosen in 2005"). A **plan** or **forecast** says what someone intends or expects ("operation will start in …", "100,000 jobs"). An **opinion** or **hope** is a judgement ("fusion is the energy of the future"). All three can appear in a good article; the reader must tell them apart.
3. **Who says it?** A researcher who works on the project, an environmental group and a government can all be quoted fairly, but each has its own interests.

## The physics behind the story {Physics}

**How fusion releases energy.** When light nuclei fuse, the new nucleus is more tightly bound, and the total mass decreases. The missing mass becomes energy, $E = mc^2$. One $\text{D–T}$ reaction releases $17.6\ \text{MeV}$: $3.5\ \text{MeV}$ to the helium nucleus and $14.1\ \text{MeV}$ to the neutron.

```pysahdy
Where does the energy of $17.6\,\text{MeV}$ in a $\text{D–T}$ reaction come from?
---
The products have slightly less total mass than the nuclei that fused. The missing mass $\Delta m$ becomes energy by $E = \Delta m \cdot c^2$.
```

**Why it is difficult.** The nuclei are positively charged and repel each other, so they fuse only when they move very fast: the plasma must be at about $150$ million $^\circ\text{C}$. It must be dense enough and held long enough by magnetic fields, while the walls survive the heat and the neutrons. Tritium is radioactive and rare, so a future plant must breed it from lithium. And a high gain in the plasma is still not electricity: ITER has no turbines.

## Common misconception

"An old article with a wrong date was bad journalism." If the article reported the official plan of its time, it was correct then; the plan changed later. The reader's job is to notice the date of the article and to check the plan today.

A second mistake is to treat every sentence of an article as the journalist's claim. Many sentences report what someone said: a researcher's hope, an organisation's plan or a critic's opinion. Ask *who says so*.

## Summary

- Official information on ITER changed between 2018 and 2026: first plasma 2025 → research operation 2034; $\text{D–T}$ 2035 → 2039; costs and the construction status changed too.
- The goal ($Q = 10$), the site, the seven Members and the physics did not change.
- Read news about science by asking when it was written, what kind of claim each statement is (result, plan, opinion) and who says it.
- Fusion releases energy because the mass decreases ($E = mc^2$); it is difficult because of the Coulomb repulsion, the extreme temperature, confinement, materials and tritium.
