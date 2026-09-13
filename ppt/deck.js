const pptxgen = require('pptxgenjs');
const path = require('path');
const D = __dirname + '/ppt/';

const NAVY="012169", PINK="FCA5C7", TT="8FC3EA", PAPER="FFFFFF",
      HAZE="B7C8E6", CARD="0A2C79", INK="01102F";
const HEAD="Calibri", BODY="Calibri";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";               // 13.333 x 7.5
pres.author = "Kiviruukin lukio";
pres.title  = "Kiviruukin lukion diplomipolut";

const W = 13.333, H = 7.5, M = 0.62;
const dark  = () => { const s = pres.addSlide(); s.background = { path: D+"bg.png" }; return s; };
const plain = (c) => { const s = pres.addSlide(); s.background = { color: c }; return s; };

// pikkuotsikko, harvennettu versaali
function kicker(s, text, x, y, color, w){
  s.addText(text.toUpperCase(), { x, y, w: w||4, h:0.24, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:11, bold:true, charSpacing:2.2, color });
}

// pyöreä "siru" – toistuva visuaalinen elementti koko esityksessä
function chips(s, items, x, y, maxW, opt){
  const o = Object.assign({ fs:12, border:PINK, gapX:0.11, gapY:0.13, h:0.34 }, opt||{});
  let cx = x, cy = y;
  items.forEach(t => {
    const w = Math.max(0.62, t.length * o.fs * 0.0072 + 0.30);
    if (cx + w > x + maxW) { cx = x; cy += o.h + o.gapY; }
    s.addShape(pres.ShapeType.roundRect, { x:cx, y:cy, w, h:o.h, rectRadius:o.h/2,
      fill:{ color:PAPER, transparency:96 }, line:{ color:o.border, width:0.75 } });
    s.addText(t, { x:cx, y:cy, w, h:o.h, isTextBox:true, margin:0, align:"center",
      valign:"middle", fontFace:BODY, fontSize:o.fs, color:PAPER });
    cx += w + o.gapX;
  });
  return cy + o.h;      // alareunan y
}

const TTCHIPS = ["Makerspace","robotiikka","ohjelmointi","data","kyberturvallisuus",
  "bioteknologia","terveysteknologia","dronet ja satelliitit","luonnontieteellinen tutkimus"];
const YRCHIPS = ["oma talous","työelämätaidot","yrittäjyys","sijoittaminen","yrittäjän matematiikka",
  "media ja markkinointi","verkostoituminen","Global Business","Vuosi yrittäjänä"];

/* ---------- 1. otsikkokalvo ---------- */
{
  const s = dark();
  s.addImage({ path:D+"mark-pink.png", x:M, y:1.42, w:1.62, h:1.01 });
  s.addText("Kaksi diplomipolkua.", { x:M, y:2.62, w:9.6, h:1.15, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:54, bold:true, color:PAPER });
  s.addText("Täällä taotaan tulevaisuutta.", { x:M, y:3.78, w:9.6, h:0.52, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:24, color:PINK });
  s.addText("Tiede- ja teknologia -diplomi  ·  Talous- ja yrittäjyysdiplomi", { x:M, y:4.62, w:9.6, h:0.4,
    isTextBox:true, margin:0, fontFace:BODY, fontSize:15, color:HAZE });
  kicker(s, "Kiviruukin lukio", M, 6.42, PINK, 5);
  s.addNotes("Kiviruukin lukiossa on kaksi diplomipolkua. Molemmat rakennetaan omista kiinnostuksen kohteista, ja molemmat huipentuvat diplomityöhön, joka esitellään Kiviruukkipäivänä.");
}

/* ---------- 2. yleiskuva: molemmat polut ja yhteinen ydin ---------- */
{
  const s = dark();
  kicker(s, "Yleiskuva", M, 0.5, PINK, 5);
  s.addText("Kaksi polkua, yhteinen ydin", { x:M, y:0.78, w:11, h:0.6, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:32, bold:true, color:PAPER });

  const cardY = 1.82, cardH = 3.9, cw = 4.62;
  const cols = [
    { x:M, title:"Tiede- ja teknologia\n-diplomi", verbs:"Rakenna · Koodaa · Tutki · Näytä", c:TT,
      body:"Yhdistä luonnontieteitä, matematiikkaa ja teknologiaa tekemiseen, tutkimiseen ja ongelmanratkaisuun.",
      foot:"Lukiodiplomi · Kiviruukkipäivä" },
    { x:W-M-cw, title:"Talous- ja\nyrittäjyysdiplomi", verbs:"Ideoi · Kokeile · Verkostoidu · Kasva", c:PINK,
      body:"Kehitä talous-, työelämä- ja yrittäjyystaitojasi ja opi viemään ideat käytännön toiminnaksi.",
      foot:"Diplomi · Kiviruukkipäivä" }
  ];
  cols.forEach(col => {
    s.addShape(pres.ShapeType.roundRect, { x:col.x, y:cardY, w:cw, h:cardH, rectRadius:0.2,
      fill:{ color:CARD }, line:{ color:col.c, width:1 } });
    s.addText(col.title, { x:col.x+0.34, y:cardY+0.3, w:cw-0.68, h:0.94, isTextBox:true, margin:0,
      fontFace:HEAD, fontSize:23, bold:true, color:PAPER, lineSpacingMultiple:0.92 });
    s.addText(col.verbs, { x:col.x+0.34, y:cardY+1.3, w:cw-0.68, h:0.32, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:13, bold:true, color:col.c });
    s.addText(col.body, { x:col.x+0.34, y:cardY+1.74, w:cw-0.68, h:1.1, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:14, color:HAZE, lineSpacingMultiple:1.15 });
    s.addText("6 op + 2 op", { x:col.x+0.34, y:cardY+2.95, w:cw-0.68, h:0.44, isTextBox:true, margin:0,
      fontFace:HEAD, fontSize:22, bold:true, color:col.c });
    s.addText(col.foot, { x:col.x+0.34, y:cardY+3.36, w:cw-0.68, h:0.3, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:12, color:HAZE });
  });

  // yhteinen ydin siltana korttien välissä
  const bx = M+cw+0.36, bw = W-2*M-2*cw-0.72;
  s.addShape(pres.ShapeType.roundRect, { x:bx, y:cardY+0.35, w:bw, h:3.2, rectRadius:0.2,
    fill:{ color:PAPER, transparency:93 }, line:{ color:PAPER, width:0.75, dashType:"dash" } });
  s.addText("Yhteistä\nmolemmille", { x:bx+0.14, y:cardY+0.6, w:bw-0.28, h:0.72, isTextBox:true,
    margin:0, align:"center", fontFace:HEAD, fontSize:17, bold:true, color:PAPER, lineSpacingMultiple:0.95 });
  ["Innovaatiot","Tekoäly","Korkeakoulu- ja\nyritysyhteistyö"].forEach((t,i) => {
    const y = cardY+1.5 + i*0.66;
    s.addShape(pres.ShapeType.roundRect, { x:bx+0.16, y, w:bw-0.32, h:0.56, rectRadius:0.28,
      fill:{ color:NAVY }, line:{ color:PAPER, width:0.75 } });
    s.addText(t, { x:bx+0.16, y, w:bw-0.32, h:0.56, isTextBox:true, margin:0, align:"center",
      valign:"middle", fontFace:BODY, fontSize:11.5, color:PAPER, lineSpacingMultiple:0.9 });
  });
  // sillan viivat
  [[M+cw, bx],[bx+bw, W-M-cw]].forEach(([x1,x2]) => {
    s.addShape(pres.ShapeType.line, { x:x1, y:cardY+cardH/2, w:x2-x1, h:0, line:{ color:PINK, width:1 } });
  });

  s.addText("Molemmissa poluissa vähintään 6 op opintoja ja 2 op lukiodiplomi.",
    { x:M, y:6.05, w:12.1, h:0.4, isTextBox:true, margin:0, fontFace:BODY, fontSize:14, color:HAZE });
  s.addNotes("Polut eivät ole toisiaan poissulkevia: innovaatiot, tekoäly sekä korkeakoulu- ja yritysyhteistyö kulkevat molemmissa.");
}

/* ---------- 3. & 4. polkukalvot ---------- */
[
  { kick:"Polku 1", title:"Tiede- ja teknologia -diplomi", c:TT, chips:TTCHIPS,
    verbs:"Rakenna · Koodaa · Tutki · Näytä",
    lead:"Yhdistä luonnontieteitä, matematiikkaa ja teknologiaa tekemiseen, tutkimiseen ja ongelmanratkaisuun.",
    foot:"Lukiodiplomi · esittely Kiviruukkipäivänä",
    notes:"Tiede ja teknologia -lukiodiplomi on valtakunnallinen lukiodiplomi: 2 op, jota edeltää vähintään 6 op soveltuvia opintoja." },
  { kick:"Polku 2", title:"Talous- ja yrittäjyysdiplomi", c:PINK, chips:YRCHIPS,
    verbs:"Ideoi · Kokeile · Verkostoidu · Kasva",
    lead:"Kehitä talous-, työelämä- ja yrittäjyystaitojasi ja opi viemään ideat käytännön toiminnaksi.",
    foot:"Diplomi · esittely Kiviruukkipäivänä",
    notes:"Tarkista laajuus: 6 op + 2 op on tässä oletus, ei valtakunnallinen määräys." }
].forEach(p => {
  const s = dark();
  kicker(s, p.kick, M, 0.5, p.c, 5);
  s.addText(p.title, { x:M, y:0.78, w:9.4, h:0.62, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:32, bold:true, color:PAPER });
  s.addText(p.verbs, { x:M, y:1.46, w:9.4, h:0.36, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:17, bold:true, color:p.c });
  s.addText(p.lead, { x:M, y:2.0, w:8.1, h:0.8, isTextBox:true, margin:0,
    fontFace:BODY, fontSize:16, color:HAZE, lineSpacingMultiple:1.15 });

  kicker(s, "Mitä opiskelet", M, 3.06, PINK, 5);
  chips(s, p.chips, M, 3.42, 8.3, { fs:13, border:p.c, h:0.38 });

  // laajuus omana kortiinaan oikealla
  s.addShape(pres.ShapeType.roundRect, { x:9.35, y:1.98, w:3.38, h:2.9, rectRadius:0.2,
    fill:{ color:CARD }, line:{ color:p.c, width:1 } });
  s.addText("6 op + 2 op", { x:9.6, y:2.52, w:2.88, h:0.6, isTextBox:true, margin:0, align:"center",
    fontFace:HEAD, fontSize:29, bold:true, color:p.c });
  s.addText("opintoja + lukiodiplomi", { x:9.6, y:3.14, w:2.88, h:0.32, isTextBox:true, margin:0,
    align:"center", fontFace:BODY, fontSize:13, color:HAZE });
  s.addText(p.foot, { x:9.6, y:3.74, w:2.88, h:0.6, isTextBox:true, margin:0, align:"center",
    fontFace:BODY, fontSize:12, color:HAZE, lineSpacingMultiple:1.1 });

  // nosto: täyttää alaosan ja kertoo, miten kokonaisuus kootaan
  s.addShape(pres.ShapeType.roundRect, { x:M, y:4.95, w:12.11, h:1.42, rectRadius:0.18,
    fill:{ color:CARD }, line:{ color:PAPER, width:0.75, dashType:"dash" } });
  s.addImage({ path:D+"mark-pink.png", x:M+0.42, y:5.42, w:0.78, h:0.49 });
  s.addText("Kokoa oma kokonaisuutesi.", { x:M+1.5, y:5.18, w:10.2, h:0.42, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:20, bold:true, color:PAPER });
  s.addText("Valitse vähintään kolme opintojaksoa. Opintojaksojen projektit voit liittää portfolioosi.",
    { x:M+1.5, y:5.66, w:10.2, h:0.42, isTextBox:true, margin:0, fontFace:BODY, fontSize:15, color:HAZE });
  s.addNotes(p.notes);
});

/* ---------- 5. yhteinen ydin ---------- */
{
  const s = dark();
  kicker(s, "Yhteinen ydin", M, 0.5, PINK, 5);
  s.addText("Yhteistä molemmille poluille", { x:M, y:0.78, w:11, h:0.62, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:32, bold:true, color:PAPER });
  s.addText("Valitsit kumman polun tahansa, nämä kulkevat mukana.", { x:M, y:1.5, w:11, h:0.4,
    isTextBox:true, margin:0, fontFace:BODY, fontSize:16, color:HAZE });

  const items = [
    { t:"Innovaatiot", d:"Ideasta kokeiluun ja kokeilusta valmiiseen ratkaisuun." },
    { t:"Tekoäly", d:"Tekoälyn käyttö, mahdollisuudet ja rajat osana omaa työtä." },
    { t:"Korkeakoulu- ja\nyritysyhteistyö", d:"Oikeita toimeksiantoja ja kumppaneita lukion ulkopuolelta." }
  ];
  const cw = 3.82, gap = 0.44, y = 2.16;
  items.forEach((it,i) => {
    const x = M + i*(cw+gap);
    s.addShape(pres.ShapeType.roundRect, { x, y, w:cw, h:3.62, rectRadius:0.2,
      fill:{ color:CARD }, line:{ color:PAPER, width:0.75, dashType:"dash" } });
    s.addShape(pres.ShapeType.ellipse, { x:x+0.36, y:y+0.36, w:0.62, h:0.62, fill:{ color:PINK } });
    s.addText(String(i+1), { x:x+0.36, y:y+0.36, w:0.62, h:0.62, isTextBox:true, margin:0,
      align:"center", valign:"middle", fontFace:HEAD, fontSize:20, bold:true, color:NAVY });
    s.addText(it.t, { x:x+0.36, y:y+1.24, w:cw-0.72, h:0.94, isTextBox:true, margin:0, valign:"bottom",
      fontFace:HEAD, fontSize:21, bold:true, color:PAPER, lineSpacingMultiple:0.95 });
    s.addText(it.d, { x:x+0.36, y:y+2.32, w:cw-0.72, h:1.0, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:14, color:HAZE, lineSpacingMultiple:1.15 });
  });
  s.addText("Yhteinen ydin on syy siihen, että polut kannattaa esitellä yhdessä – ja syy, ettei valinta sulje mitään pois.",
    { x:M, y:6.28, w:12.1, h:0.4, isTextBox:true, margin:0, fontFace:BODY, fontSize:14, color:HAZE });
  s.addNotes("Yhteinen ydin on syy siihen, että polut kannattaa esitellä yhdessä.");
}

/* ---------- 6. kolme vuotta ---------- */
{
  const s = dark();
  kicker(s, "Aikataulu", M, 0.5, PINK, 5);
  s.addText("Polku kolmessa vuodessa", { x:M, y:0.78, w:11, h:0.62, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:32, bold:true, color:PAPER });

  const steps = [
    { n:"1", t:"Tutustu", d:"Valitse kiinnostavia opintoja ja etsi oma suuntasi." },
    { n:"2", t:"Syvennä", d:"Kokoa oma painotuksesi ja aloita diplomityö." },
    { n:"3", t:"Esittele", d:"Diplomityö, portfolio ja esittely Kiviruukkipäivänä." }
  ];
  const y0 = 2.0, rowH = 1.36;
  steps.forEach((st,i) => {
    const y = y0 + i*rowH;
    s.addShape(pres.ShapeType.ellipse, { x:M, y:y, w:0.92, h:0.92,
      fill:{ color:NAVY }, line:{ color:PINK, width:1.5 } });
    s.addText(st.n, { x:M, y:y, w:0.92, h:0.92, isTextBox:true, margin:0, align:"center",
      valign:"middle", fontFace:HEAD, fontSize:30, bold:true, color:PINK });
    s.addText(st.t, { x:M+1.32, y:y+0.06, w:3.2, h:0.44, isTextBox:true, margin:0,
      fontFace:HEAD, fontSize:24, bold:true, color:PAPER });
    s.addText(st.d, { x:M+1.32, y:y+0.52, w:6.4, h:0.4, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:15, color:HAZE });
    if (i < steps.length-1)
      s.addShape(pres.ShapeType.line, { x:M+0.46, y:y+0.98, w:0, h:rowH-1.04,
        line:{ color:PINK, width:1, dashType:"dash" } });
  });

  s.addShape(pres.ShapeType.roundRect, { x:8.62, y:2.0, w:4.1, h:3.64, rectRadius:0.2,
    fill:{ color:CARD }, line:{ color:PINK, width:1 } });
  s.addText("6 op + 2 op", { x:8.86, y:3.14, w:3.62, h:0.62, isTextBox:true, margin:0, align:"center",
    fontFace:HEAD, fontSize:31, bold:true, color:PINK });
  s.addText("Vähintään 6 op soveltuvia opintoja\nja 2 op lukiodiplomi.", { x:8.86, y:3.86, w:3.62, h:0.9,
    isTextBox:true, margin:0, align:"center", fontFace:BODY, fontSize:14, color:HAZE, lineSpacingMultiple:1.15 });
  s.addText("Diplomityö tehdään pääsääntöisesti toisen ja kolmannen vuoden aikana.",
    { x:M, y:6.28, w:12.1, h:0.4, isTextBox:true, margin:0, fontFace:BODY, fontSize:14, color:HAZE });
  s.addNotes("Diplomityö tehdään pääsääntöisesti toisen ja kolmannen vuoden aikana.");
}

/* ---------- 7. mitä saat (vaalea kalvo vaihteluksi) ---------- */
{
  const s = plain(PAPER);
  s.addImage({ path:D+"mark-navy.png", x:11.35, y:0.5, w:1.35, h:0.84 });
  kicker(s, "Miksi kannattaa", M, 0.5, "8A5C72", 5);
  s.addText("Mitä saat diplomipolusta?", { x:M, y:0.78, w:9.6, h:0.62, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:32, bold:true, color:NAVY });

  const why = [
    { t:"Oman painotuksen", d:"Rakenna kokonaisuus omien kiinnostuksenkohteidesi mukaan." },
    { t:"Jatko-opintovalmiuksia", d:"Syvennä taitoja, joista on hyötyä korkeakouluissa ja työelämässä." },
    { t:"Oikeita projekteja", d:"Tee yhteistyötä yritysten, korkeakoulujen ja muiden kumppaneiden kanssa." },
    { t:"Näytön osaamisestasi", d:"Kokoa osaamisesi diplomityöhön ja esittele se muille." }
  ];
  const cw = 5.9, ch = 2.0, gx = 0.31, gy = 0.34, x0 = M, y0 = 2.05;
  why.forEach((it,i) => {
    const x = x0 + (i%2)*(cw+gx), y = y0 + Math.floor(i/2)*(ch+gy);
    s.addShape(pres.ShapeType.roundRect, { x, y, w:cw, h:ch, rectRadius:0.18,
      fill:{ color:"F1F5FC" }, line:{ color:"D6E0F2", width:0.75 } });
    s.addShape(pres.ShapeType.ellipse, { x:x+0.36, y:y+0.4, w:0.5, h:0.5, fill:{ color:PINK } });
    s.addText(String(i+1), { x:x+0.36, y:y+0.4, w:0.5, h:0.5, isTextBox:true, margin:0, align:"center",
      valign:"middle", fontFace:HEAD, fontSize:16, bold:true, color:NAVY });
    s.addText(it.t, { x:x+1.04, y:y+0.36, w:cw-1.4, h:0.42, isTextBox:true, margin:0,
      fontFace:HEAD, fontSize:20, bold:true, color:NAVY });
    s.addText(it.d, { x:x+1.04, y:y+0.86, w:cw-1.4, h:0.86, isTextBox:true, margin:0,
      fontFace:BODY, fontSize:14, color:"44567D", lineSpacingMultiple:1.15 });
  });
  s.addText("Molemmissa poluissa vähintään 6 op opintoja ja 2 op lukiodiplomi.",
    { x:M, y:6.78, w:12.1, h:0.4, isTextBox:true, margin:0, fontFace:BODY, fontSize:14, color:"44567D" });
  s.addNotes("Tämä kalvo vastaa kysymykseen, joka opiskelijalla oikeasti on: mitä minä tästä saan?");
}

/* ---------- 8. kehotus ---------- */
{
  const s = plain(PINK);
  s.addImage({ path:D+"mark-navy.png", x:M, y:1.55, w:1.62, h:1.01 });
  s.addText("Tuo oma kipinäsi.", { x:M, y:2.85, w:10.5, h:1.05, isTextBox:true, margin:0,
    fontFace:HEAD, fontSize:52, bold:true, color:INK });
  s.addText("Info lukuvuoden alussa · kysy diplomipolkujen koordinaattorilta",
    { x:M, y:4.02, w:10.5, h:0.44, isTextBox:true, margin:0, fontFace:BODY, fontSize:19, color:"3A2438" });
  kicker(s, "Kiviruukin lukio", M, 6.42, INK, 5);
  s.addNotes("Kerro tässä konkreettinen seuraava askel: kenelle ilmoittaudutaan ja milloin.");
}

pres.writeFile({ fileName: path.join(__dirname, "Kiviruukin-diplomipolut.pptx") })
  .then(f => console.log("kirjoitettu:", f));
