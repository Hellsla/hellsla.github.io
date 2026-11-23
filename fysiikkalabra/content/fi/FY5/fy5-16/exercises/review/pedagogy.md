VERDICT: PASS
CONTENT-HASH: 306fd4f134ec4fd4

## Blocking

## Polish
- solutions.md, Kaava-rivit vertailuajalle (L1-01, L2-xx, L3-01 ym.) — johto "I = 2^n I_v, I·t_v = I_v·t_0" perustuu energia-annokseen (intensiteetti kertaa aika), jonka luvun Kaava-osa vain mainitsee ("energian keskiarvo"). Sama toistuu pitkänä lähes kaikissa ratkaisuissa; lyhyt maininta Periaatteessa "annos = I·t on vakio" tekisi askeleen perustelluksi. Ei estävä.
- solutions.md, L3 kuulonsuojaintehtävä (annos/vaimennus) — Kaava-rivi on hyvin pitkä (jopa 9 yhtälöä); puhelimella se jakautuu riveiksi mutta kannattaa jakaa kahteen lohkoon: taso → vertailuaika ja annos → suojain.

## Checked
- Diff: jokaisen muutetun Kaava-rivin lähteessä on kunnollinen aligned-lohko (erotinmerkit näkyvät vain diffissä puuttuvina); rivit alkavat perusyhtälöstä (taso → intensiteetti, I = 2^n I_v, I·t_v = I_v·t_0) ja sievenevät symbolisesti loppuun ennen Sijoitusta.
- Etäisyysjohto: L_1 − L_2 = 20 dB·lg 2^k ≈ k·6 dB on oikein (20 lg 2 = 6,02) ja johtaa k = (L_1 − L_2)/6 dB -muotoon ennen lukuja.
- Kahden lähteen ja etäisyyden kaksinkertaistumisen johdot (3,01 dB, −6 dB) vastaavat edellisen luvun sääntöjä; lopussa "≈" merkitty asianmukaisesti.
- Jälkikaiunta-ajan johto (ΔL/Δt = 60 dB/T) on yksinkertainen ja tasainen laskunopeus on sanottu Periaatteessa.
- Sijoitus, vastaukset ja toleranssit ennallaan; lasketut arvot (2,0 h, 73,01 dB, 82 dB, 150 %, 16 m, 0,90 s, 2,52 h, 75,6 min) täsmäävät.
- Pitkät Mallivastaus- ja Järkevyys-kappaleet (L2-xx, vastamelu, L3 iskumelu) pilkottu lyhyiksi; sisältö sama.
- Suomi: termit (vertailuaika, toiminta-arvo, jälkikaiunta-aika) lukua vastaavat; ei uusia kielivirheitä.
- Kysymys ja tasot ennallaan.
