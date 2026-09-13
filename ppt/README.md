# Diplomipolut PowerPointina

`Kiviruukin-diplomipolut.pptx` – 8 kalvoa, 16:9, muokattavaa tekstiä
(ei kuvakaappauksia). Sama sisältö kuin `diplomipolut.html`.

| Kalvo | Sisältö |
|---|---|
| 1 | Kaksi diplomipolkua. |
| 2 | Yleiskuva: molemmat polut ja yhteinen ydin |
| 3 | Tiede- ja teknologia -diplomi |
| 4 | Talous- ja yrittäjyysdiplomi |
| 5 | Yhteinen ydin |
| 6 | Polku kolmessa vuodessa |
| 7 | Mitä saat diplomipolusta? |
| 8 | Tuo oma kipinäsi. |

Puhujan muistiinpanot ovat jokaisella kalvolla.

## Uudelleenrakentaminen

```
npm install pptxgenjs
node deck.js                 # kirjoittaa Kiviruukin-diplomipolut.pptx
python3 dedupe.py Kiviruukin-diplomipolut.pptx slim.pptx
```

`deck.js` odottaa kuvat hakemistosta `ppt/`: `bg.png` (säteikkötausta),
`mark-pink.png` ja `mark-navy.png` (logo). Ne on tehty samasta
polygonista kuin sivujen SVG-logo.
