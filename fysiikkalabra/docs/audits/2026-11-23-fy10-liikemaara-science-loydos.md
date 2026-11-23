VERDICT: FAIL
CONTENT-HASH: a7d94497271df0b3

## Blocking

1. **B: the systematic-deviation rule holds only when the carts move the way the total momentum points.** investigation.md line 240 says: if the velocities were read too far from the collision, the points lie below the line when $p_\text{kok} > 0$ and above it when $p_\text{kok} < 0$. teacher.md (first bullet on velocities) says the same without any condition. Rolling resistance acts on each cart against that cart's own velocity. When the carts move toward each other, the net friction force is about $-C g(m_1 - m_2)$, so its sign depends on the masses and not on the sign of $p_\text{kok}$. Counterexample: $m_1 = 0{,}5\,\text{kg}$ at $+0{,}40\,\text{m/s}$ and $m_2 = 1{,}0\,\text{kg}$ at $-0{,}10\,\text{m/s}$, so $p_\text{kok} = +0{,}10\,\text{kg·m/s}$. Reading the speeds $0{,}5\,\text{s}$ early, with deceleration $0{,}02\,\text{m/s}^2$ for both carts, gives $p_\text{kok} = 0{,}095\,\text{kg·m/s}$. The point then lies above the line although $p_\text{kok} > 0$. A head-on collision is one of the three guided cases, so a student can wrongly decide the deviation is not caused by friction. Fix: state the condition in both files, e.g. "kun kumpikin vaunu liikkuu kokonaisliikemäärän suuntaan tai on levossa (esim. vaunu 2 aluksi levossa)". Also say that in head-on collisions the friction impulses partly cancel and the direction of the deviation can vary. The first clause, "Jos ulkoinen voima … on pienentänyt suuruutta", is correctly conditional and can stay.

## Polish

- Model graph: the line $p_\text{kok}' = p_\text{kok}$ has slope 1 but is drawn at about 31° (pixel slope 0,61). The axes have no scale, so this is not an error. Because both axes show the same quantity, equal scales (45°) would show "kulmakerroin 1" more clearly.

## Checked

- Setup image, opened myself: side view of a horizontal track with a motion sensor at each end facing the centre, two wheeled carts (beige left, blue right) with spring bumpers facing each other, blue velocity arrows (left cart right, right cart left), grey arrows under the sensors (left right, right left), black arrow at the bottom to the right. No hydropower content. All foreignObject labels sit on their objects; the aria-label matches the image and line 123.
- Sensor signs, conservation condition, collision definitions; predictions 2 ($v/2$) and 3 ($m_1 v_1 = m_2|v_2|$); extension $E_\text{k}'/E_\text{k} = m_1/(m_1+m_2)$; uncertainty of the difference $\Delta p + \Delta p'$; velocity and model graphs and their aria-labels; hero SVG.
