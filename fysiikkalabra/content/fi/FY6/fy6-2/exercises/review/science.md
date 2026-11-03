VERDICT: FAIL
CONTENT-HASH: 519b0dfa91457c33

## Blocking
- exercises.json:96–99 (fy6-2-L3-03) and solutions.md:111–120 — **A** (causality/consistency): the task's observation "Lamppu sammuu, ja mittarin näyttö jää nollaan" is explained by a blown fuse, but a blown fuse removes the meter from the circuit, so the lamp (battery + lamp only) lights again; the end state "lamp off and display 0" cannot follow from that cause. The lesson's sim models this correctly (after the fuse blows the lamp is lit). — Change the observation to "Lamppu sammuu hetkeksi ja syttyy sitten uudelleen, ja mittarin näyttö jää nollaan" (or "lamppu välähtää"), and in the model answer and the self-assessment criterion explain that the lamp was dark only while the meter short-circuited it and relit when the fuse blew.

## Polish
- solutions.md:59 (L2-01, Järkevyys) — "Virta on liian pieni alueelle 10 A: alueella 200 mA sitä ei voisi mitata" reads as contradictory; say that 350 mA exceeds the 200 mA range, so 10 A is the only current range here and a meter with a finer high-current range would help.
- solutions.md (L2-04, Periaate) — "koska lamppu tarvitsee virtaa" is a label; say the lamp's voltage is its resistance times an almost zero current.

## Checked
- One script recomputed every answer from the task text: L1-01 0,0823 V, L1-02 1,663 mA, L1-03 0,75 %, L1-04 0,180 A, L1-05 0,009935 V, L2-01 10,57 %, L2-02 0,001075 A, L2-03 3,20, L2-04 9,0 V, L3-01 2,17 %, L3-02 0,1522 V — all agree with answers.py and exercises.json.
- L3-02 intervals 4,97–5,07 V and 5,03–5,25 V overlap; conclusion "cannot be shown faulty, does not prove equal" follows the guardrail.
- L3-01 1,0 mV/mA = 1,0 Ω, consistent with the lesson sim (97,8 mA vs 100 mA).
- Rounding: error limits to two significant figures with reasons stated; L2-02 unit conversion explicit.
- Solutions symbolic first, conversions and reasonableness checks present.
- Content hash unchanged start/end.
