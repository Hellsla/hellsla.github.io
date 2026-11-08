/**
 * RuukkiLabra · palautusten tuonti ja arviointi (kokeilu 2026-11-05: FY3-1, sitten koko FY3).
 *
 * Sheetsiin sidottu Apps Script. Taulukko on yhdistetty ryhmän Google Forms -lomakkeeseen, jolla opiskelija palauttaa
 * RuukkiLabrasta ladatun luvun tiedoston (esim. fy3-4.ratkaisut.json). Yksi lomake ja taulukko ryhmää kohti, joten
 * taulukossa on vain sen ryhmän palautukset. Opintojakson luvut ja tehtävät: Tehtavat.gs (RL_COURSE). Valikko RuukkiLabra:
 *   - Tuo palautukset: lukee lomakkeen vastausvälilehden ja palautuskansion tiedostot, tarkistaa ne ja kirjaa ne
 *     välilehdelle "RL Palautukset". Lomakkeen omaa vastausvälilehteä ei muuteta.
 *   - Avaa arviointi: arviointinäkymä (Review.html) suureen ikkunaan. Pisteet tallentuvat välilehdelle "RL Pisteet".
 *
 * Palautustiedosto on epäluotettavaa dataa: sitä ei suoriteta, siitä ei näytetä HTML:ää, ja sen tekstit kirjoitetaan
 * taulukkoon niin, ettei niistä voi tulla kaavoja. Lokeihin ei kirjoiteta vastauksia, kuvia eikä sähköposteja.
 * Ohjeet: palautus/KAYTTOONOTTO.md. Tiedostomuoto: palautus/TIEDOSTOMUOTO.md.
 */

/* ===== ASETUKSET: tarkista nämä käyttöönotossa ===== */
var RL_CONFIG = {
  // Formsin palautuskansion tunniste: Drive-kansio "Palauta vastaukset (File responses)" tai sen yläkansio
  // "<lomakkeen nimi> (File responses)". Tunniste on kansion osoitteen loppuosa .../folders/<TUNNISTE>.
  SUBMISSION_FOLDER_ID: '',
  // Lomakkeen vastausvälilehden nimi. Tyhjä = ensimmäinen välilehti, jonka otsikkorivillä on tiedostokysymys.
  RESPONSES_SHEET: '',
  // Lomakkeen sarakeotsikot. Sarake löytyy, kun otsikko on jokin luetelluista (kirjainkoolla ei ole väliä).
  HEADERS: {
    timestamp: ['Aikaleima', 'Timestamp', 'Tidstämpel'],
    email: ['Sähköpostiosoite', 'Sähköposti', 'Email address', 'Email Address', 'E-postadress'],
    file: ['Palauta vastaukset']
  },
  // Palauttajan tunniste: 'email' = Formsin vahvistettu sähköposti (Sheets-versio). Paikallinen arviointisivu
  // (palautus/arviointi-fy3.html) käyttää 'name': Formsin tiedoston nimeen lisäämä palauttajan nimi.
  IDENTITY: 'email',
  // Sallittu sähköpostin verkkotunnus, esim. 'edu.example.fi'. Tyhjä = ei tarkisteta (lomake rajaa vastaajat).
  EMAIL_DOMAIN: '',
  // Pisteet tehtävää kohti: 0 … MAX_POINTS, enintään kaksi desimaalia (esim. 0,5). Tyhjä = arvioimaton, 0 = annettu
  // nolla pistettä. Opettaja 5.11.2026: 0–1 p tehtävää kohti.
  MAX_POINTS: 1,
  // Ryhmän nimi arviointinäkymän otsikkoon, esim. 'FY3.2'. Paikallinen arviointisivu asettaa valitun ryhmän nimen.
  GROUP: '',
  SUBMISSIONS_SHEET: 'RL Palautukset',
  SCORES_SHEET: 'RL Pisteet',
  TIME_ZONE: 'Europe/Helsinki'
};
/* ===== asetukset päättyvät ===== */

// Samat rajat kuin RuukkiLabran palautus.js:ssä (LIMITS). Formsin tiedostokoon raja asetetaan 100 Mt:ksi (tiedosto enintään 20 Mt, 2026-11-08).
var RL_LIMITS = { file: 20000000, image: 2000000, side: 5000, images: 40, text: 20000, latex: 4000, items: 400, mathPng: 200000 };
var RL_FORMAT = 'ruukkilabra-palautus', RL_VERSION = 4;   // 2: + itsearvio (selfassessment), 3: kaikki vastaukset + tavoitearvioiden kooste (opettaja 6.11.2026), 4: + annettujen tehtävien eteneminen (7.11.2026)
var RL_SA_LEVELS = ['a', 'b', 'c', 'd', 'x'];   // väriasteikko vihreästä punertavaan + Ei vielä (inquiry.py SA_LEVELS)
var RL_STATUS = { OK: 'Hyväksytty', DUP: 'Kaksoiskappale', CHECK: 'Tarkistettava', BAD: 'Virheellinen', READ: 'Lukuvirhe' };
var RL_DECISION = { ACCEPT: 'Hyväksy', REJECT: 'Hylkää' };
var RL_SUB_HEAD = ['Avain', 'Palautusaika', 'Sähköposti', 'Palautustunniste', 'Tila', 'Syy', 'Opettajan päätös',
  'Vastattuja', 'Vastatut tehtävät', 'Tyhjiä', 'Tiedosto', 'Koko (t)', 'Sisällön SHA-256', 'Tuotu', 'Lomakkeen rivi', 'Luku',
  'Tehtävien tiivisteet', 'Itsearvio', 'Eteneminen'];
var RL_SCORE_HEAD = ['Avain', 'Sähköposti', 'Palautustunniste', 'Tehtävä', 'Tehtävän numero', 'Pisteet', 'Tallennettu', 'Luku'];
var RL_C = { key: 0, time: 1, email: 2, sub: 3, status: 4, reason: 5, decision: 6, nAnswered: 7, answered: 8, nEmpty: 9, file: 10, size: 11, sha: 12, imported: 13, row: 14, chapter: 15, hashes: 16, self: 17, progress: 18 };
var RL_S = { key: 0, email: 1, sub: 2, task: 3, number: 4, points: 5, saved: 6, chapter: 7 };

/* ---------- valikko ---------- */

function onOpen() {
  SpreadsheetApp.getUi().createMenu('RuukkiLabra')
    .addItem('Tuo palautukset', 'importSubmissions')
    .addItem('Avaa arviointi', 'openReview')
    .addToUi();
}

function openReview() {
  var html = HtmlService.createHtmlOutputFromFile('Review').setWidth(1400).setHeight(900);
  SpreadsheetApp.getUi().showModalDialog(html, 'RuukkiLabra · arviointi');
}

function importSubmissions() {
  var ui = SpreadsheetApp.getUi();
  try {
    var r = rlImport_();
    ui.alert('Palautukset tuotu',
      'Uusia rivejä ' + r.added + ' (hyväksyttyjä ' + r.counts[RL_STATUS.OK] + ', kaksoiskappaleita ' + r.counts[RL_STATUS.DUP] +
      ', tarkistettavia ' + r.counts[RL_STATUS.CHECK] + ', virheellisiä ' + r.counts[RL_STATUS.BAD] + ', lukuvirheitä ' + r.counts[RL_STATUS.READ] + ').' +
      (r.retried ? '\nUudelleen yritettyjä lukuvirheitä ' + r.retried + '.' : '') +
      (r.flagged ? '\nAiempia rivejä merkittiin tarkistettaviksi ' + r.flagged + '.' : '') +
      (r.unfinished ? '\nKaikkia ei ehditty käsitellä. Aja Tuo palautukset uudelleen.' : '') +
      '\nKäsittelytila näkyy välilehdellä "' + RL_CONFIG.SUBMISSIONS_SHEET + '" ja arviointinäkymän aloitussivulla.',
      ui.ButtonSet.OK);
  } catch (e) {
    ui.alert('Tuonti ei onnistunut', rlUserMessage_(e), ui.ButtonSet.OK);
  }
}

/* ---------- apufunktiot ---------- */

function rlError_(text) { var e = new Error(text); e.rlUser = true; return e; }
function rlUserMessage_(e) { return e && e.rlUser ? e.message : 'Odottamaton virhe. Yritä uudelleen; jos virhe toistuu, tarkista asetukset (KAYTTOONOTTO.md).'; }
// Teksti taulukkoon niin, ettei siitä tule kaavaa (=, +, -, @ tai sarkain/rivinvaihto alussa).
function rlCell_(v) {
  if (v === null || v === undefined) return '';
  if (typeof v !== 'string') return v;
  v = v.replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, '');
  return /^[=+\-@\t\r\n]/.test(v) ? "'" + v : v;
}
function rlText_(v) { return v === null || v === undefined ? '' : String(v).replace(/^'/, ''); }
function rlHex_(bytes) { var s = ''; for (var i = 0; i < bytes.length; i++) { var b = bytes[i] & 255; s += (b < 16 ? '0' : '') + b.toString(16); } return s; }
function rlSha_(text) { return rlHex_(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, text, Utilities.Charset.UTF_8)); }
function rlFmt_(d) { return Utilities.formatDate(d, RL_CONFIG.TIME_ZONE, 'd.M.yyyy') + ' klo ' + Utilities.formatDate(d, RL_CONFIG.TIME_ZONE, 'H.mm.ss'); }
// Hakutaulut ilman prototyyppiä: tiedoston "__proto__" tai "constructor" ei löydä mitään.
function rlChapters_() {
  var m = Object.create(null);
  RL_COURSE.chapters.forEach(function (c) { m[c.id] = c; });
  return m;
}
function rlTasks_(chapterId) {
  var ids = Object.create(null), c = rlChapters_()[chapterId];
  if (c) c.tasks.forEach(function (t) { ids[t.id] = t; });
  return ids;
}
// Tehtävän tunnisteesta tehtävä ja sen luku, tai null.
function rlTaskInfo_(taskId) {
  for (var i = 0; i < RL_COURSE.chapters.length; i++) {
    var c = RL_COURSE.chapters[i];
    for (var j = 0; j < c.tasks.length; j++) if (c.tasks[j].id === taskId) return { task: c.tasks[j], chapter: c };
  }
  return null;
}
function rlChapterName_(c) { return 'Luku ' + c.number; }
function rlLock_(ms) {
  var lock = LockService.getDocumentLock();
  if (!lock.tryLock(ms)) throw rlError_('Toinen käsittely on juuri käynnissä. Yritä hetken kuluttua uudelleen.');
  return lock;
}
function rlSheet_(name, head) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.getRange(1, 1, 1, head.length).setValues([head]).setFontWeight('bold');
    sh.setFrozenRows(1);
    sh.getRange(2, 1, sh.getMaxRows() - 1, head.length).setNumberFormat('@');   // tekstinä: ei kaavoja, ei automaattimuunnoksia
    if (name === RL_CONFIG.SUBMISSIONS_SHEET) {
      sh.getRange(2, RL_C.time + 1, sh.getMaxRows() - 1, 1).setNumberFormat('d.m.yyyy h.mm.ss');
      sh.getRange(2, RL_C.imported + 1, sh.getMaxRows() - 1, 1).setNumberFormat('d.m.yyyy h.mm.ss');
      sh.getRange(2, RL_C.decision + 1, sh.getMaxRows() - 1, 1).setDataValidation(
        SpreadsheetApp.newDataValidation().requireValueInList([RL_DECISION.ACCEPT, RL_DECISION.REJECT], true).setAllowInvalid(false).build());
    } else {
      sh.getRange(2, RL_S.points + 1, sh.getMaxRows() - 1, 1).setNumberFormat('0.##');
      sh.getRange(2, RL_S.saved + 1, sh.getMaxRows() - 1, 1).setNumberFormat('d.m.yyyy h.mm.ss');
    }
    sh.protect().setDescription('RuukkiLabra kirjoittaa tähän. Muuta vain saraketta Opettajan päätös.').setWarningOnly(true);
  } else if (sh.getLastColumn() < head.length) {
    sh.getRange(1, 1, 1, head.length).setValues([head]).setFontWeight('bold');   // uusi sarake (Tehtävien tiivisteet 6.11.2026)
  }
  return sh;
}
function rlRows_(sh, width) {
  var n = sh.getLastRow() - 1;
  return n > 0 ? sh.getRange(2, 1, n, width).getValues() : [];
}

/* ---------- palautustiedoston tarkistus ---------- */

function rlB64Bytes_(b64, max, what) {
  if (typeof b64 !== 'string' || !b64 || !/^[A-Za-z0-9+\/]+={0,2}$/.test(b64) || b64.length % 4) throw rlError_(what + ': kuvadata ei ole kelvollista base64-dataa');
  if (Math.floor(b64.length * 3 / 4) > max + 2) throw rlError_(what + ': kuva on liian suuri (yli ' + (max / 1e6) + ' Mt)');
  return Utilities.base64Decode(b64);
}
// Kuvan oikea tyyppi ja koko tavuista (ei luoteta tiedoston ilmoittamaan tyyppiin): vain PNG ja JPEG.
function rlImageInfo_(bytes) {
  var b = function (i) { return bytes[i] & 255; };
  if (bytes.length > 24 && b(0) === 0x89 && b(1) === 0x50 && b(2) === 0x4e && b(3) === 0x47 && b(12) === 0x49 && b(13) === 0x48 && b(14) === 0x44 && b(15) === 0x52) {
    return { mime: 'image/png', w: b(16) * 16777216 + b(17) * 65536 + b(18) * 256 + b(19), h: b(20) * 16777216 + b(21) * 65536 + b(22) * 256 + b(23) };
  }
  if (bytes.length > 4 && b(0) === 0xff && b(1) === 0xd8) {
    var i = 2;
    while (i + 9 < bytes.length) {
      if (b(i) !== 0xff) return null;
      var m = b(i + 1);
      if (m === 0xff) { i++; continue; }
      if (m === 0xd8 || m === 0x01 || (m >= 0xd0 && m <= 0xd7)) { i += 2; continue; }
      var len = b(i + 2) * 256 + b(i + 3);
      if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return { mime: 'image/jpeg', h: b(i + 5) * 256 + b(i + 6), w: b(i + 7) * 256 + b(i + 8) };
      if (len < 2) return null;
      i += 2 + len;
    }
  }
  return null;
}
function rlCheckItem_(it, where, deep) {
  if (!it || typeof it !== 'object' || Array.isArray(it)) throw rlError_(where + ': virheellinen osa');
  var keys = Object.keys(it);
  var only = function (allowed) { for (var k = 0; k < keys.length; k++) if (allowed.indexOf(keys[k]) < 0) throw rlError_(where + ': tuntematon kenttä "' + String(keys[k]).slice(0, 30) + '"'); };
  if (it.type === 'text') {
    only(['type', 'text']);
    if (typeof it.text !== 'string' || !it.text) throw rlError_(where + ': tyhjä tai virheellinen teksti');
    return { type: 'text', text: it.text };
  }
  if (it.type === 'math') {
    only(['type', 'latex', 'png', 'svg', 'w', 'h']);
    if (typeof it.latex !== 'string' || !it.latex.trim() || it.latex.length > RL_LIMITS.latex) throw rlError_(where + ': virheellinen kaava');
    var out = { type: 'math', latex: it.latex };
    if (it.png !== undefined) {
      if (!(it.w > 0 && it.w <= 3000 && it.h > 0 && it.h <= 1000)) throw rlError_(where + ': kaavakuvan koko on virheellinen');
      if (deep) {
        var mi = rlImageInfo_(rlB64Bytes_(it.png, RL_LIMITS.mathPng, where));
        if (!mi || mi.mime !== 'image/png') throw rlError_(where + ': kaavakuva ei ole PNG-kuva');
      } else if (typeof it.png !== 'string' || it.png.length > RL_LIMITS.mathPng * 1.4) throw rlError_(where + ': kaavakuva on liian suuri');
      out.png = it.png; out.w = it.w; out.h = it.h;
    }
    // svg: työtiedostossa kaava on vain kerran, editorin MathJax-SVG:nä (palautus.js sref; 7.11.2026), PNG:tä ei ole
    if (it.svg !== undefined) {
      if (typeof it.svg !== 'string' || !/^[A-Za-z0-9+\/=]+$/.test(it.svg) || it.svg.length > RL_LIMITS.mathPng * 1.4) throw rlError_(where + ': kaavakuva on virheellinen');
      if (deep && !/^\s*(<\?xml[^>]*>\s*)?<svg[\s>]/.test(Utilities.base64Decode(it.svg.slice(0, 200)).map(function (c) { return String.fromCharCode(c & 255); }).join(''))) throw rlError_(where + ': kaavakuva ei ole SVG-kuva');
      if (it.w !== undefined && !(it.w > 0 && it.w <= 3000 && it.h > 0 && it.h <= 1000)) throw rlError_(where + ': kaavakuvan koko on virheellinen');
      out.svg = it.svg; if (it.w !== undefined) { out.w = it.w; out.h = it.h; }
    }
    return out;
  }
  if (it.type === 'image') {
    only(['type', 'mime', 'data', 'w', 'h', 'dw']);
    // dw: leveys, jonka opiskelija antoi kuvalle editorissa (CSS-pikseleinä, pienempi kuin kuvan oma leveys; 6.11.2026)
    if (it.dw !== undefined && !(typeof it.dw === 'number' && it.dw % 1 === 0 && it.dw >= 1 && it.dw <= RL_LIMITS.side)) throw rlError_(where + ': kuvan näyttöleveys on virheellinen');
    if (it.mime !== 'image/png' && it.mime !== 'image/jpeg') throw rlError_(where + ': kuvamuoto ei ole sallittu (vain PNG ja JPEG)');
    var info = null;
    if (deep) {
      info = rlImageInfo_(rlB64Bytes_(it.data, RL_LIMITS.image, where));
      if (!info || info.mime !== it.mime) throw rlError_(where + ': kuvan sisältö ei ole ' + (it.mime === 'image/png' ? 'PNG' : 'JPEG') + '-kuva');
      if (info.w < 1 || info.h < 1 || info.w > RL_LIMITS.side || info.h > RL_LIMITS.side) throw rlError_(where + ': kuvan koko on liian suuri (yli ' + RL_LIMITS.side + ' px)');
    } else if (typeof it.data !== 'string' || it.data.length > RL_LIMITS.image * 1.4) throw rlError_(where + ': kuva on liian suuri');
    var out2 = { type: 'image', mime: it.mime, data: it.data, w: info ? info.w : it.w, h: info ? info.h : it.h };
    if (it.dw !== undefined) out2.dw = it.dw;
    return out2;
  }
  throw rlError_(where + ': tuntematon sisältötyyppi');
}
// Versio 3: tehtävän muut vastaukset kuin editori (numero, valinta, tosi/epätosi, järjestys, kirjoitettu vastaus,
// mittaustaulukko). Palauttaa samat kentät samassa järjestyksessä kuin RuukkiLabran palautus.js kirjoittaa ne, joten
// tarkistussumma lasketaan tästä. Tekstejä ei koskaan tulkita HTML:ksi.
function rlCheckResponse_(r, where) {
  if (!r || typeof r !== 'object' || Array.isArray(r)) throw rlError_(where + ': virheellinen vastaus');
  var keys = Object.keys(r);
  var only = function (allowed) { for (var k = 0; k < keys.length; k++) if (allowed.indexOf(keys[k]) < 0) throw rlError_(where + ': tuntematon kenttä "' + String(keys[k]).slice(0, 30) + '"'); };
  var str = function (v, max, empty) { if (typeof v !== 'string' || v.length > max || (!empty && !v)) throw rlError_(where + ': virheellinen vastaus'); return v; };
  var list = function (v, max) { if (!Array.isArray(v) || !v.length || v.length > max) throw rlError_(where + ': virheellinen vastaus'); return v; };
  if (r.type === 'number') {
    only(['type', 'value', 'unit']);
    var n = { type: 'number', value: str(r.value, 100) };
    if (r.unit !== undefined) n.unit = str(r.unit, 60, true);
    return n;
  }
  if (r.type === 'choice') {
    only(['type', 'question', 'answer', 'option']);
    if (typeof r.option !== 'number' || r.option < 0 || r.option > 50 || r.option % 1) throw rlError_(where + ': virheellinen valinta');
    return { type: 'choice', question: str(r.question, 2000, true), answer: str(r.answer, 2000, true), option: r.option };
  }
  if (r.type === 'truefalse') {
    only(['type', 'items']);
    return { type: 'truefalse', items: list(r.items, 20).map(function (x) {
      if (!x || typeof x !== 'object' || (x.value !== true && x.value !== false && x.value !== null)) throw rlError_(where + ': virheellinen väite');
      return { text: str(x.text, 2000, true), value: x.value };
    }) };
  }
  if (r.type === 'order') {
    only(['type', 'items']);
    return { type: 'order', items: list(r.items, 20).map(function (x) {
      if (!x || typeof x !== 'object' || !(x.rank === null || (typeof x.rank === 'number' && x.rank >= 1 && x.rank <= 20 && x.rank % 1 === 0))) throw rlError_(where + ': virheellinen järjestys');
      return { text: str(x.text, 2000, true), rank: x.rank };
    }) };
  }
  if (r.type === 'text') {
    only(['type', 'label', 'text']);
    return { type: 'text', label: str(r.label, 2000, true), text: str(r.text, RL_LIMITS.text) };
  }
  if (r.type === 'table') {
    only(['type', 'head', 'rows']);
    var cell = function (c) { return str(c, 200, true); };
    var head = Array.isArray(r.head) && r.head.length <= 20 ? r.head.map(cell) : null;
    if (!head) throw rlError_(where + ': virheellinen taulukko');
    return { type: 'table', head: head, rows: list(r.rows, 200).map(function (row) { if (!Array.isArray(row) || row.length > 20) throw rlError_(where + ': virheellinen taulukko'); return row.map(cell); }) };
  }
  throw rlError_(where + ': tuntematon vastaustyyppi');
}
/**
 * Tarkistaa tiedoston tekstin. Palauttaa { data, answered: [id], empty: [id], sha } tai heittää virheen, jonka viesti
 * kertoo syyn opettajalle. deep = kuvadata puretaan ja tarkistetaan tavuista (tuonnissa aina).
 */
function rlValidate_(text, deep, work) {
  var data;
  if (work) data = text;   // yksi luku opintojakson työtiedostosta (rlValidateWork_)
  else try { data = JSON.parse(text); } catch (e) { throw rlError_('tiedosto ei ole JSON-tiedosto'); }
  if (!data || typeof data !== 'object' || Array.isArray(data)) throw rlError_('tiedoston rakenne on virheellinen');
  if (!work && data.format === RL_WORK_FORMAT) return rlValidateWork_(data, deep);
  if (data.format !== RL_FORMAT) throw rlError_('tiedosto ei ole RuukkiLabran palautustiedosto');
  if (typeof data.version !== 'number') throw rlError_('tiedostomuodon versio puuttuu');
  if (data.version > RL_VERSION) throw rlError_('tiedostomuodon versio ' + data.version + ' on uudempi kuin tämä skripti tuntee');
  if (data.version !== 1 && data.version !== 2 && data.version !== 3 && data.version !== 4) throw rlError_('tuntematon tiedostomuodon versio');
  var v3 = data.version >= 3;   // versio 4 = versio 3 + eteneminen (progress)
  if (typeof data.chapter !== 'string' || !rlChapters_()[data.chapter]) throw rlError_('tiedosto on toiselta opintojaksolta tai tuntemattomasta luvusta (' + String(data.chapter).slice(0, 20) + ')');
  if (typeof data.submission_id !== 'string' || !/^[0-9a-f]{32}$/.test(data.submission_id)) throw rlError_('palautustunniste puuttuu tai on virheellinen');
  if (!work && (typeof data.content_sha256 !== 'string' || !/^[0-9a-f]{64}$/.test(data.content_sha256))) throw rlError_('tarkistussumma puuttuu');
  if (!Array.isArray(data.answers)) throw rlError_('vastaukset puuttuvat');
  var tasks = rlTasks_(data.chapter), seen = Object.create(null), answered = [], empty = [], images = 0, canon = [], hashes = [];
  for (var i = 0; i < data.answers.length; i++) {
    var a = data.answers[i];
    if (!a || typeof a !== 'object' || typeof a.task !== 'string') throw rlError_('vastaus ' + (i + 1) + ' on virheellinen');
    var t = tasks[a.task];
    if (!t) throw rlError_('tuntematon tehtävä ' + a.task.slice(0, 40));
    if (seen[a.task]) throw rlError_('tehtävä ' + t.number + ' on tiedostossa kahdesti');
    seen[a.task] = true;
    var where = 'tehtävä ' + t.number;
    if (!Array.isArray(a.content) || a.content.length > RL_LIMITS.items) throw rlError_(where + ': virheellinen sisältö');
    if (v3 ? !Array.isArray(a.responses) || a.responses.length > 40 : a.responses !== undefined) throw rlError_(where + ': virheelliset vastaukset');
    if (!v3 && t.lesson) throw rlError_('tuntematon tehtävä ' + a.task.slice(0, 40));   // oppitunnin tehtävät vasta versiossa 3
    var resp = v3 ? a.responses.map(function (r) { return rlCheckResponse_(r, where); }) : [];
    if (a.status !== 'answered' && a.status !== 'empty') throw rlError_(where + ': tuntematon tila');
    // versio 3: tehtävään on vastattu, kun editorissa tai jossakin muussa vastauksessa on jotakin (opettaja 6.11.2026)
    if ((a.status === 'empty') !== (a.content.length === 0 && resp.length === 0)) throw rlError_(where + ': tila ja sisältö eivät täsmää');
    var chars = 0, items = [];
    for (var j = 0; j < a.content.length; j++) {
      var it = rlCheckItem_(a.content[j], where, deep);
      if (it.type === 'text') chars += it.text.length;
      if (it.type === 'image') images++;
      items.push(it.type === 'math' ? { type: 'math', latex: it.latex } : a.content[j]);
    }
    resp.forEach(function (r) { if (r.type === 'text') chars += r.text.length; });
    if (chars > RL_LIMITS.text) throw rlError_(where + ': teksti on liian pitkä');
    canon.push(v3 ? { task: a.task, status: a.status, content: items, responses: resp } : { task: a.task, status: a.status, content: items });
    if (a.status === 'answered') hashes.push(a.task + '=' + rlSha_(JSON.stringify(canon[canon.length - 1])).slice(0, 16));
    (a.status === 'answered' ? answered : empty).push(a.task);
  }
  // vanhemmissa versioissa (1, 2) on vain editorilliset tehtävät, joten oppitunnin tehtävät eivät puutu niistä
  for (var id in tasks) if (!work && !seen[id] && (v3 || !tasks[id].lesson)) throw rlError_('tehtävä ' + tasks[id].number + ' puuttuu tiedostosta');
  if (images > RL_LIMITS.images) throw rlError_('kuvia on liikaa (' + images + ')');
  var self = data.version === 2 ? rlCheckSelf_(data.selfassessment, data.chapter) : v3 ? rlCheckGoals_(data.selfassessment, data.chapter) : null;
  var progress = data.version === 4 ? rlCheckProgress_(data.progress) : null;
  if (data.version !== 4 && data.progress !== undefined) throw rlError_('etenemistiedot kuuluvat vain versioon 4');
  var sha = rlSha_(progress ? JSON.stringify({ answers: canon, selfassessment: self, progress: progress })
    : data.version === 2 || v3 ? JSON.stringify({ answers: canon, selfassessment: self }) : JSON.stringify(canon));
  if (!work && sha !== data.content_sha256) throw rlError_('tarkistussumma ei täsmää: tiedostoa on muutettu tai se on vioittunut');
  if (work) for (var tid in tasks) if (!seen[tid]) empty.push(tid);   // työtiedostossa on vain tehtävät, joissa on jotakin
  // taulukkoon vain tavoitearviot (opettaja 6.11.2026): version 2 tehtäväkohtaiset arviot ja historiat jäävät pois
  var known = rlGoalIds_(data.chapter);
  var levels = (self || []).filter(function (x) { return x.level && known[x.id]; }).map(function (x) { return { id: x.id, level: x.level }; });
  return { data: data, chapter: data.chapter, answered: answered, empty: empty, sha: sha, hashes: hashes.join(','), self: levels, progress: progress };
}
// Eteneminen (versio 4, opettaja 7.11.2026): koko opintojakson annetut tehtävät, niistä tehdyiksi merkityt aikoineen ja
// merkintöjen historia (1 = merkitty, 0 = merkintä poistettu). Tuntematon tehtävä, kenttä tai aika hylkää tiedoston.
var RL_PROGRESS_MAX = { assigned: 300, history: 3000 };
function rlCheckProgress_(p) {
  var bad = function (what) { return rlError_('etenemistiedot: ' + what); };
  if (!p || typeof p !== 'object' || Array.isArray(p)) throw bad('puuttuvat');
  Object.keys(p).forEach(function (k) { if (['course', 'assigned', 'done', 'history'].indexOf(k) < 0) throw bad('tuntematon kenttä "' + String(k).slice(0, 30) + '"'); });
  if (p.course !== RL_COURSE.id) throw bad('toiselta opintojaksolta (' + String(p.course).slice(0, 10) + ')');
  if (!Array.isArray(p.assigned) || !p.assigned.length || p.assigned.length > RL_PROGRESS_MAX.assigned) throw bad('annetut tehtävät puuttuvat');
  var known = Object.create(null), set = Object.create(null);
  RL_COURSE.chapters.forEach(function (c) { c.tasks.forEach(function (t) { if (!t.lesson) known[t.id] = true; }); });
  p.assigned.forEach(function (id) { if (typeof id !== 'string' || !known[id] || set[id]) throw bad('tuntematon tai toistuva tehtävä ' + String(id).slice(0, 40)); set[id] = true; });
  var iso = function (t) { return typeof t === 'string' && /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d{1,3})?Z$/.test(t) && !isNaN(Date.parse(t)); };
  if (!Array.isArray(p.done) || p.done.length > p.assigned.length) throw bad('virheelliset merkinnät');
  var seen = Object.create(null);
  var done = p.done.map(function (x) {
    if (!Array.isArray(x) || x.length !== 2 || !set[x[0]] || seen[x[0]] || !iso(x[1])) throw bad('virheellinen merkintä');
    seen[x[0]] = true; return [x[0], x[1]];
  });
  if (!Array.isArray(p.history) || p.history.length > RL_PROGRESS_MAX.history) throw bad('virheellinen historia');
  var history = p.history.map(function (x) {
    if (!Array.isArray(x) || x.length !== 3 || !set[x[0]] || !iso(x[1]) || (x[2] !== 0 && x[2] !== 1)) throw bad('virheellinen historian rivi');
    return [x[0], x[1], x[2]];
  });
  return { course: p.course, assigned: p.assigned.slice(), done: done, history: history };
}
// Opintojakson työtiedosto (opettaja 7.11.2026, templates/palautus.js "Work file"): kaikki luvut yhdessä tiedostossa,
// lisäksi eteneminen ja opiskelijan selaimen tallennetut tiedot (store), joista kuvat haetaan. Jokainen luku tarkistetaan
// kuten luvun palautus (versio 3), ja tuonti kirjaa sen omalle rivilleen.
var RL_WORK_FORMAT = 'ruukkilabra-tyo', RL_WORK_VERSION = 1;
function rlValidateWork_(data, deep) {
  if (typeof data.version !== 'number') throw rlError_('tiedostomuodon versio puuttuu');
  if (data.version > RL_WORK_VERSION) throw rlError_('työtiedoston versio ' + data.version + ' on uudempi kuin tämä skripti tuntee');
  if (data.course !== RL_COURSE.id) throw rlError_('tiedosto on toiselta opintojaksolta (' + String(data.course).slice(0, 10) + ')');
  if (typeof data.submission_id !== 'string' || !/^[0-9a-f]{32}$/.test(data.submission_id)) throw rlError_('palautustunniste puuttuu tai on virheellinen');
  if (typeof data.content_sha256 !== 'string' || !/^[0-9a-f]{64}$/.test(data.content_sha256)) throw rlError_('tarkistussumma puuttuu');
  var st = data.store;
  if (!st || typeof st !== 'object' || !Array.isArray(st.solutions) || !st.local || typeof st.local !== 'object' || Array.isArray(st.local) || !Array.isArray(data.chapters) || data.chapters.length > 60) throw rlError_('työtiedoston rakenne on virheellinen');
  if (rlSha_(JSON.stringify({ chapters: data.chapters, progress: data.progress, store: data.store })) !== data.content_sha256) throw rlError_('tarkistussumma ei täsmää: tiedostoa on muutettu tai se on vioittunut');
  var html = Object.create(null);
  st.solutions.forEach(function (r) { if (r && typeof r.id === 'string' && typeof r.html === 'string') html[r.id] = r.html; });
  // k:s PNG- tai JPEG-kuva ratkaisun HTML:ssä (kaavat ovat SVG-kuvia, eivät mukana)
  var picture = function (task, k, where) {
    var tags = String(html[task] || '').match(/<img\b[^>]*>/gi) || [], n = 0;
    for (var i = 0; i < tags.length; i++) {
      var m = /\ssrc="data:(image\/(?:png|jpeg));base64,([A-Za-z0-9+\/=]+)"/.exec(tags[i]);
      if (m && n++ === k) return { mime: m[1], data: m[2] };
    }
    throw rlError_(where + ': kuvaa ei löydy tiedostosta');
  };
  // k:s kaava (MathJax-SVG) ratkaisun HTML:ssä: työtiedoston kaava on vain siellä (sref), ei PNG:nä luvun vastauksissa
  var formula = function (task, k, where) {
    var tags = String(html[task] || '').match(/<img\b[^>]*>/gi) || [], n = 0;
    for (var i = 0; i < tags.length; i++) {
      var m = /\ssrc="data:image\/svg\+xml;base64,([A-Za-z0-9+\/=]+)"/.exec(tags[i]);
      if (m && n++ === k) return m[1];
    }
    throw rlError_(where + ': kaavaa ei löydy tiedostosta');
  };
  var progress = data.progress === null || data.progress === undefined ? null : rlCheckProgress_(data.progress);
  var seen = Object.create(null), parts = [], images = 0;
  data.chapters.forEach(function (c, i) {
    if (!c || typeof c !== 'object' || typeof c.chapter !== 'string' || !rlChapters_()[c.chapter]) throw rlError_('luku ' + (i + 1) + ' on tuntematon');
    if (seen[c.chapter]) throw rlError_('luku ' + c.chapter + ' on tiedostossa kahdesti');
    seen[c.chapter] = true;
    var known = rlGoalIds_(c.chapter), sa = c.selfassessment;
    if (!sa || !Array.isArray(sa.goals) || !Array.isArray(c.answers)) throw rlError_('luvun ' + c.chapter + ' rakenne on virheellinen');
    var answers = c.answers.map(function (a) {
      if (!a || typeof a !== 'object' || !Array.isArray(a.content)) return a;
      var t = rlTasks_(c.chapter)[a.task], where = 'tehtävä ' + (t ? t.number : String(a.task).slice(0, 40));
      return { task: a.task, status: a.status, responses: a.responses, content: a.content.map(function (it) {
        if (it && it.type === 'math' && it.sref !== undefined) {
          if (typeof it.sref !== 'number' || it.sref % 1 || it.sref < 0) throw rlError_(where + ': virheellinen kaava');
          var fm = { type: 'math', latex: it.latex, svg: formula(a.task, it.sref, where) };
          if (it.w !== undefined) { fm.w = it.w; fm.h = it.h; }
          return fm;
        }
        if (!it || it.type !== 'image' || it.ref === undefined) return it;
        if (typeof it.ref !== 'number' || it.ref % 1 || it.ref < 0) throw rlError_(where + ': virheellinen kuva');
        images++;
        var pic = picture(a.task, it.ref, where), o = { type: 'image', mime: pic.mime, data: pic.data, w: it.w, h: it.h };
        if (it.dw !== undefined) o.dw = it.dw;
        return o;
      }) };
    });
    var goals = sa.goals.filter(function (g) { return g && known[g.id]; });
    var v = rlValidate_({ format: RL_FORMAT, version: 3, chapter: c.chapter, submission_id: data.submission_id, answers: answers, selfassessment: { goals: goals } }, deep, true);
    parts.push({ chapter: c.chapter, answered: v.answered, empty: v.empty, sha: v.sha, hashes: v.hashes, self: v.self, data: v.data });
  });
  if (images > RL_LIMITS.images * 8) throw rlError_('kuvia on liikaa (' + images + ')');
  if (!parts.length) throw rlError_('tiedostossa ei ole yhtään ratkaisua');
  return { work: true, data: data, parts: parts, progress: progress };
}
// Taulukkoon vain Tehty-merkinnät: "<annettuja>|<tehtävä>,<tehtävä>,...". Valmistumisajat ja historia jäävät
// tiedostoon opiskelijan omaa etenemisgraafia varten; arviointi ei näytä eikä käytä niitä (opettaja 7.11.2026).
function rlProgressCell_(p) { return p ? p.assigned.length + '|' + p.done.map(function (x) { return x[0]; }).join(',') : ''; }
function rlProgressParse_(text) {
  var m = /^(\d{1,3})\|(.*)$/.exec(rlText_(text));
  if (!m) return null;
  return { total: Number(m[1]), done: m[2] ? m[2].split(',').filter(function (x) { return /^[a-z0-9-]{1,40}$/.test(x); }) : [] };
}
// Itsearvio (versio 2): kohteet sivun järjestyksessä, taso ja sen historia. Tuntematon kohde, taso tai aika hylkää tiedoston.
function rlCheckSelf_(sa, chapterId) {
  if (!sa || typeof sa !== 'object' || !Array.isArray(sa.items) || sa.items.length > 60) throw rlError_('itsearvio on virheellinen');
  var c = rlChapters_()[chapterId], known = Object.create(null), seen = Object.create(null), out = [];
  ((c && c.self) || []).forEach(function (x) { known[x.id] = true; });
  sa.items.forEach(function (it, i) {
    if (!it || typeof it !== 'object' || typeof it.id !== 'string' || !/^[a-z0-9-]{1,60}$/.test(it.id)) throw rlError_('itsearvion kohta ' + (i + 1) + ' on virheellinen');
    // versio 2 kantoi myös tehtäväkohtaiset arviot; ne luetaan (tarkistussummaa varten) mutta eivät näy (opettaja 6.11.2026)
    if (seen[it.id]) throw rlError_('itsearvion kohta ' + it.id + ' on tiedostossa kahdesti');
    seen[it.id] = true;
    if (RL_SA_LEVELS.indexOf(it.level) < 0) throw rlError_('itsearvion kohdassa ' + it.id + ' on tuntematon taso');
    if (!Array.isArray(it.history) || it.history.length > 50) throw rlError_('itsearvion kohdan ' + it.id + ' historia on virheellinen');
    var h = it.history.map(function (x) {
      if (!Array.isArray(x) || x.length !== 2 || RL_SA_LEVELS.indexOf(x[0]) < 0 || typeof x[1] !== 'string' || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d{1,3})?Z$/.test(x[1])) throw rlError_('itsearvion kohdan ' + it.id + ' historia on virheellinen');
      return [x[0], x[1]];
    });
    out.push({ id: it.id, level: it.level, history: h });
  });
  return out;
}
// Versio 3: luvun tavoitteet, kukin kerran sivun järjestyksessä: tunniste, tavoiteteksti ja opiskelijan viimeisin taso tai
// null (ei vastattu). "x" = En ole vielä harjoitellut. Ei tehtäväkohtaisia arvioita eikä historiaa.
function rlCheckGoals_(sa, chapterId) {
  if (!sa || typeof sa !== 'object' || Array.isArray(sa) || Object.keys(sa).join() !== 'goals' || !Array.isArray(sa.goals) || sa.goals.length > 30) throw rlError_('tavoitearvio on virheellinen');
  var known = rlGoalIds_(chapterId), seen = Object.create(null);
  return sa.goals.map(function (g, i) {
    if (!g || typeof g !== 'object' || typeof g.id !== 'string' || !/^tavoite-\d{1,2}$/.test(g.id) || Object.keys(g).join() !== 'id,text,level') throw rlError_('tavoitearvion kohta ' + (i + 1) + ' on virheellinen');
    if (!known[g.id]) throw rlError_('tuntematon tavoite ' + g.id);
    if (seen[g.id]) throw rlError_('tavoite ' + g.id + ' on tiedostossa kahdesti');
    seen[g.id] = true;
    if (typeof g.text !== 'string' || g.text.length > 500) throw rlError_('tavoitteen ' + g.id + ' teksti on virheellinen');
    if (g.level !== null && RL_SA_LEVELS.indexOf(g.level) < 0) throw rlError_('tavoitteessa ' + g.id + ' on tuntematon taso');
    return { id: g.id, text: g.text, level: g.level };
  });
}
// Luvun tavoitteiden tunnisteet arviointisivun tehtävälistasta (Tehtavat.gs self).
function rlGoalIds_(chapterId) {
  var c = rlChapters_()[chapterId], m = Object.create(null);
  ((c && c.self) || []).forEach(function (x) { if (/^tavoite-/.test(x.id)) m[x.id] = true; });
  return m;
}
// Itsearvio taulukon soluun: "tavoite-1=c,tavoite-2=x" (vain tunnisteita ja kirjaimia, ei opiskelijan tekstiä)
function rlSelfCell_(self) { return self.map(function (x) { return x.id + '=' + x.level; }).join(','); }
function rlSelfParse_(text) {
  var m = Object.create(null);
  rlText_(text).split(',').forEach(function (p) { var k = p.split('='); if (k.length === 2 && RL_SA_LEVELS.indexOf(k[1]) >= 0 && /^[a-z0-9-]{1,60}$/.test(k[0])) m[k[0]] = k[1]; });
  return m;
}

/* ---------- tuonti ---------- */

function rlFindColumn_(head, names) {
  for (var i = 0; i < head.length; i++) {
    var h = String(head[i]).trim().toLowerCase();
    for (var j = 0; j < names.length; j++) if (h === names[j].toLowerCase()) return i;
  }
  return -1;
}
function rlResponses_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), fileNames = RL_CONFIG.HEADERS.file;
  var sh = RL_CONFIG.RESPONSES_SHEET ? ss.getSheetByName(RL_CONFIG.RESPONSES_SHEET) : null;
  if (RL_CONFIG.RESPONSES_SHEET && !sh) throw rlError_('Välilehteä "' + RL_CONFIG.RESPONSES_SHEET + '" ei löydy. Tarkista RL_CONFIG.RESPONSES_SHEET.');
  if (!sh) {
    var all = ss.getSheets();
    for (var i = 0; i < all.length && !sh; i++) {
      var n = all[i].getName();
      if (n === RL_CONFIG.SUBMISSIONS_SHEET || n === RL_CONFIG.SCORES_SHEET || all[i].getLastColumn() < 1) continue;
      if (rlFindColumn_(all[i].getRange(1, 1, 1, all[i].getLastColumn()).getValues()[0], fileNames) >= 0) sh = all[i];
    }
  }
  if (!sh) throw rlError_('Lomakkeen vastausvälilehteä ei löydy: millään välilehdellä ei ole saraketta "' + fileNames.join('" / "') + '". Yhdistä lomake taulukkoon ja tarkista RL_CONFIG.HEADERS.file.');
  var values = sh.getDataRange().getValues(), head = values[0] || [];
  var col = { time: rlFindColumn_(head, RL_CONFIG.HEADERS.timestamp), email: rlFindColumn_(head, RL_CONFIG.HEADERS.email), file: rlFindColumn_(head, fileNames) };
  var missing = [];
  if (col.time < 0) missing.push('palautusaika (' + RL_CONFIG.HEADERS.timestamp.join(' / ') + ')');
  if (col.email < 0) missing.push('sähköposti (' + RL_CONFIG.HEADERS.email.join(' / ') + ')');
  if (missing.length) throw rlError_('Välilehdeltä "' + sh.getName() + '" puuttuu sarake: ' + missing.join(', ') + '. Otsikot ovat: ' + head.map(String).join(' | ').slice(0, 400) + '. Korjaa RL_CONFIG.HEADERS tai ota sähköpostien kerääminen käyttöön lomakkeessa.');
  var rows = [];
  for (var r = 1; r < values.length; r++) {
    var v = values[r];
    if (v.join('') === '') continue;
    var t = v[col.time], time = t instanceof Date ? t : (t ? new Date(t) : null);
    if (time && isNaN(time.getTime())) time = null;
    var ids = String(v[col.file] || '').match(/(?:[?&]id=|\/d\/)([-\w]{20,})/g) || [];
    ids = ids.map(function (s) { return s.replace(/^(?:[?&]id=|\/d\/)/, ''); });
    var email = String(v[col.email] || '').trim();
    if (email.indexOf('@') >= 0) email = email.toLowerCase();   // paikallisessa arvioinnissa tunniste on Formsin nimi (RL_CONFIG.IDENTITY)
    rows.push({ row: r + 1, time: time, email: email, ids: ids,
      key: ids.length ? ids.join(',') : 'rivi:' + (time ? time.getTime() : 'x') + ':' + email + ':' + (r + 1) });
  }
  rows.sort(function (a, b) { return (a.time ? a.time.getTime() : 0) - (b.time ? b.time.getTime() : 0) || a.row - b.row; });
  return rows;
}
function rlInFolder_(file) {
  var want = RL_CONFIG.SUBMISSION_FOLDER_ID;
  var parents = file.getParents();
  while (parents.hasNext()) {
    var p = parents.next();
    if (p.getId() === want) return true;
    var up = p.getParents();
    while (up.hasNext()) if (up.next().getId() === want) return true;
  }
  return false;
}
// Lukee ja tarkistaa yhden palautuksen. Palauttaa { status, reason, ... }; ei kirjoita mitään.
function rlProcess_(resp) {
  var out = { status: RL_STATUS.BAD, reason: '', sub: '', answered: [], empty: [], size: '', sha: '', chapter: '', hashes: '', self: '', progress: '' };
  if (!resp.time) { out.reason = 'palautusaika puuttuu'; return out; }
  if (RL_CONFIG.IDENTITY === 'name') { if (!resp.email) { out.reason = 'palauttajan nimi puuttuu tiedoston nimestä'; return out; } }
  else if (!resp.email || resp.email.indexOf('@') < 1) { out.reason = 'vahvistettu sähköpostiosoite puuttuu (ota sähköpostien kerääminen käyttöön lomakkeessa)'; return out; }
  if (RL_CONFIG.IDENTITY !== 'name' && RL_CONFIG.EMAIL_DOMAIN && resp.email.slice(-RL_CONFIG.EMAIL_DOMAIN.length - 1) !== '@' + RL_CONFIG.EMAIL_DOMAIN.toLowerCase()) { out.reason = 'sähköposti ei ole koulun verkkotunnuksesta'; return out; }
  if (resp.ids.length === 0) { out.reason = 'palautuksessa ei ole tiedostoa'; return out; }
  if (resp.ids.length > 1) { out.reason = 'palautuksessa on useita tiedostoja (sallittu yksi)'; return out; }
  var file;
  try { file = DriveApp.getFileById(resp.ids[0]); } catch (e) { out.status = RL_STATUS.READ; out.reason = 'tiedostoa ei voitu avata (käyttöoikeus tai poistettu tiedosto)'; return out; }
  try {
    if (!rlInFolder_(file)) { out.reason = 'tiedosto ei ole lomakkeen palautuskansiossa'; return out; }
    out.size = file.getSize();
    if (out.size > RL_LIMITS.file) { out.reason = 'tiedosto on liian suuri (' + (out.size / 1e6).toFixed(1) + ' Mt, enintään ' + (RL_LIMITS.file / 1e6) + ' Mt)'; return out; }
    if (out.size === 0) { out.reason = 'tiedosto on tyhjä'; return out; }
    var text = file.getBlob().getDataAsString('UTF-8');
  } catch (e) { out.status = RL_STATUS.READ; out.reason = 'tiedostoa ei voitu lukea'; return out; }
  try {
    var v = rlValidate_(text, true);
    if (v.work) {
      out.status = RL_STATUS.OK;
      out.parts = v.parts.map(function (q) { return { status: RL_STATUS.OK, reason: '', sub: v.data.submission_id, answered: q.answered, empty: q.empty, size: out.size, sha: q.sha,
        chapter: q.chapter, hashes: q.hashes, self: rlSelfCell_(q.self), progress: rlProgressCell_(v.progress) }; });
      return out;
    }
    out.status = RL_STATUS.OK; out.sub = v.data.submission_id; out.answered = v.answered; out.empty = v.empty; out.sha = v.sha; out.chapter = v.chapter; out.hashes = v.hashes; out.self = rlSelfCell_(v.self); out.progress = rlProgressCell_(v.progress);
  } catch (e) { out.reason = rlUserMessage_(e); }
  return out;
}
function rlImport_() {
  if (!RL_CONFIG.SUBMISSION_FOLDER_ID) throw rlError_('Palautuskansion tunniste puuttuu. Kirjoita se Code.gs-tiedoston kohtaan RL_CONFIG.SUBMISSION_FOLDER_ID (KAYTTOONOTTO.md, vaihe 4).');
  var started = Date.now();
  var lock = rlLock_(30000);
  try {
    var responses = rlResponses_();
    var sh = rlSheet_(RL_CONFIG.SUBMISSIONS_SHEET, RL_SUB_HEAD);
    var width = RL_SUB_HEAD.length, rows = rlRows_(sh, width);
    var byKey = {};
    rows.forEach(function (r, i) { byKey[rlText_(r[RL_C.key])] = i; });
    var counts = {}; for (var s in RL_STATUS) counts[RL_STATUS[s]] = 0;
    var added = [], retried = 0, flagged = 0, unfinished = false, touched = {};
    var live = function (r) { return r[RL_C.status] !== RL_STATUS.BAD && r[RL_C.status] !== RL_STATUS.READ; };
    for (var i = 0; i < responses.length; i++) {
      var resp = responses[i], at = byKey[resp.key];
      if (at !== undefined && (at >= rows.length || rows[at][RL_C.status] !== RL_STATUS.READ)) continue;   // jo tuotu: uudelleenajo ei kirjaa toista kertaa
      if (Date.now() - started > 270000) { unfinished = true; break; }   // Apps Scriptin 6 minuutin raja
      var pr = rlProcess_(resp), parts = pr.parts || [pr];
      // opintojakson työtiedosto (7.11.2026): yksi rivi kutakin tiedoston lukua kohti; ensimmäinen saa lomakkeen rivin avaimen
      for (var j = 0; j < parts.length; j++) {
      var p = parts[j], reason = p.reason, rkey = j === 0 ? resp.key : resp.key + '#' + p.chapter;
      if (j > 0) at = byKey[rkey];
      if (p.status === RL_STATUS.OK) {
        // kaksoiskappaleet ja sama tunniste eri opiskelijoilla saman luvun aiemmissa riveissä (Formsin palautusajan järjestyksessä)
        for (var k = 0; k < rows.length; k++) {
          var o = rows[k];
          if (!live(o) || k === at || rlText_(o[RL_C.chapter]) !== p.chapter) continue;
          var oSub = rlText_(o[RL_C.sub]), oEmail = rlText_(o[RL_C.email]), oSha = rlText_(o[RL_C.sha]);
          if (oSub === p.sub && oEmail !== resp.email) {
            p.status = RL_STATUS.CHECK; reason = 'sama palautustunniste kuin toisella opiskelijalla (' + oEmail + ')';
            if (o[RL_C.status] === RL_STATUS.OK) {
              o[RL_C.status] = RL_STATUS.CHECK; o[RL_C.reason] = rlCell_('sama palautustunniste kuin toisella opiskelijalla (' + resp.email + ')');
              touched[k] = true; flagged++;
            }
          } else if (oEmail === resp.email && p.status === RL_STATUS.OK && (oSub === p.sub || oSha === p.sha)) {
            if (oSha === p.sha) { p.status = RL_STATUS.DUP; reason = (oSub === p.sub ? 'sama palautus' : 'sama sisältö') + ' tuotu jo (' + rlFmt_(o[RL_C.time]) + ')'; }
            else { p.status = RL_STATUS.CHECK; reason = 'sama palautustunniste mutta eri sisältö kuin aiemmassa palautuksessa'; }
          }
        }
      }
      var row = [rkey, resp.time || '', resp.email, p.sub, p.status, reason, '', p.answered.length, p.answered.join(','), p.empty.length,
        resp.ids.length ? 'https://drive.google.com/open?id=' + resp.ids[0] : '', p.size, p.sha, new Date(), resp.row, p.chapter, p.hashes, p.self, p.progress].map(rlCell_);
      counts[p.status]++;
      if (at !== undefined) { row[RL_C.decision] = rows[at][RL_C.decision]; rows[at] = row; touched[at] = true; retried++; }
      else { byKey[rkey] = rows.length; rows.push(row); added.push(rows.length - 1); }
      }
    }
    // kirjoitus: muuttuneet vanhat rivit paikoilleen, uudet loppuun (sarake Opettajan päätös säilyy)
    for (var t in touched) {
      var idx = Number(t);
      if (added.indexOf(idx) >= 0) continue;
      var cur = rows[idx], line = idx + 2;
      sh.getRange(line, 1, 1, RL_C.decision).setValues([cur.slice(0, RL_C.decision)]);
      sh.getRange(line, RL_C.decision + 2, 1, width - RL_C.decision - 1).setValues([cur.slice(RL_C.decision + 1)]);
    }
    if (added.length) sh.getRange(added[0] + 2, 1, added.length, width).setValues(added.map(function (i) { return rows[i]; }));
    SpreadsheetApp.flush();
    return { added: added.length, counts: counts, retried: retried, flagged: flagged, unfinished: unfinished };
  } finally { lock.releaseLock(); }
}

/* ---------- arviointinäkymän palvelinfunktiot (google.script.run) ---------- */

function rlAccepted_(r) {
  var st = r[RL_C.status], d = rlText_(r[RL_C.decision]);
  return (st === RL_STATUS.OK && d !== RL_DECISION.REJECT) || (st === RL_STATUS.CHECK && d === RL_DECISION.ACCEPT);
}
function rlScoreKey_(email, sub, task) { return email + '|' + sub + '|' + task; }
// Hyväksytyt palautukset opiskelijoittain ja luvuittain: students[i].chapters[luku] = versiot vanhimmasta uusimpaan.
function rlModel_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), chapters = rlChapters_();
  var subSh = ss.getSheetByName(RL_CONFIG.SUBMISSIONS_SHEET), scSh = ss.getSheetByName(RL_CONFIG.SCORES_SHEET);
  var subs = subSh ? rlRows_(subSh, RL_SUB_HEAD.length) : [], scores = Object.create(null);
  (scSh ? rlRows_(scSh, RL_SCORE_HEAD.length) : []).forEach(function (r) {
    var v = r[RL_S.points];
    scores[rlText_(r[RL_S.key])] = v === '' || v === null ? '' : Number(v);
  });
  var students = Object.create(null), problems = [];
  subs.forEach(function (r) {
    var email = rlText_(r[RL_C.email]), time = r[RL_C.time] instanceof Date ? r[RL_C.time] : null, ch = chapters[rlText_(r[RL_C.chapter])];
    // käsittelytilan lista: kaikki muut kuin tavalliset hyväksytyt, myös ne, joista opettaja on tehnyt päätöksen (voi perua)
    if (r[RL_C.status] !== RL_STATUS.OK || rlText_(r[RL_C.decision]) !== '') problems.push({ status: r[RL_C.status], reason: rlText_(r[RL_C.reason]), email: email,
      time: time ? rlFmt_(time) : '', decision: rlText_(r[RL_C.decision]), sub: rlText_(r[RL_C.sub]).slice(0, 8), key: rlText_(r[RL_C.key]), chapter: ch ? rlChapterName_(ch) : '' });
    // eteneminen: opiskelijan uusin palautus, jossa se on (mikä luku tahansa; myös luku, joka oli sama kuin aiemmin)
    var pr = time && ch && (rlAccepted_(r) || (r[RL_C.status] === RL_STATUS.DUP && rlText_(r[RL_C.decision]) !== RL_DECISION.REJECT)) ? rlProgressParse_(r[RL_C.progress]) : null;
    if (pr) {
      var sp = students[email] || (students[email] = { email: email, chapters: Object.create(null), first: time.getTime(), progress: null, progressMs: -1 });
      if (time.getTime() >= sp.progressMs) { sp.progress = pr; sp.progressMs = time.getTime(); }
    }
    if (!rlAccepted_(r) || !time || !ch) return;
    var s = students[email] || (students[email] = { email: email, chapters: Object.create(null), first: time.getTime(), progress: null, progressMs: -1 });
    s.first = Math.min(s.first, time.getTime());
    (s.chapters[ch.id] || (s.chapters[ch.id] = [])).push({ fileId: rlText_(r[RL_C.file]).replace(/^.*[?&]id=/, ''), sub: rlText_(r[RL_C.sub]), timeMs: time.getTime(), time: rlFmt_(time),
      answered: rlText_(r[RL_C.answered]).split(',').filter(String), sha: rlText_(r[RL_C.sha]), hashes: rlHashes_(rlText_(r[RL_C.hashes])), self: rlSelfParse_(r[RL_C.self]) });
  });
  var list = Object.keys(students).map(function (k) { return students[k]; });
  list.forEach(function (s) { for (var c in s.chapters) s.chapters[c].sort(function (a, b) { return a.timeMs - b.timeMs; }); });
  list.sort(function (a, b) { return a.first - b.first || (a.email < b.email ? -1 : 1); });   // ensimmäisen palautuksen järjestys
  return { students: list, scores: scores, problems: problems };
}
function rlHashes_(text) { var h = Object.create(null); text.split(',').forEach(function (x) { var i = x.indexOf('='); if (i > 0) h[x.slice(0, i)] = x.slice(i + 1); }); return h; }
// Version pisteet tehtävästä. Jos versiolle ei ole tallennettu pisteitä, pisteet siirtyvät saman opiskelijan saman luvun
// aiemmasta versiosta, jossa tehtävän ratkaisu on täsmälleen sama (tehtävän tiiviste), jottei samaa ratkaisua arvioida
// uudelleen (opettaja 6.11.2026). Tyhjäksi tallennettu (arvioimaton) ei hae pisteitä muualta.
function rlTaskScore_(m, s, chapterId, v, task) {
  var own = m.scores[rlScoreKey_(s.email, v.sub, task)];
  if (own !== undefined) return { score: own, from: -1 };
  var vs = s.chapters[chapterId] || [], at = vs.indexOf(v), h = v.hashes[task];
  if (h) for (var i = at - 1; i >= 0; i--) {
    if (vs[i].hashes[task] !== h) continue;
    var p = m.scores[rlScoreKey_(s.email, vs[i].sub, task)];
    if (p !== undefined && p !== '') return { score: p, from: i };
  }
  return { score: '', from: -1 };
}
function rlRound_(x) { return Math.round(x * 100) / 100; }
function rlPointsOk_(v) { return typeof v === 'number' && isFinite(v) && v >= 0 && v <= RL_CONFIG.MAX_POINTS && Math.abs(Math.round(v * 100) - v * 100) < 1e-6; }
function rlNum_(x) { return String(rlRound_(x)).replace('.', ','); }   // suomalainen desimaalipilkku
function rlLatest_(s, chapterId) { var vs = s.chapters[chapterId]; return vs ? vs[vs.length - 1] : null; }
// A task's version (teacher 2026-11-08): the newest version of the chapter with a solution to the task. A task left
// out of a newer submission (the student's browser lost it) keeps its earlier solution and points; a changed solution
// in a newer version is graded again. -1 when no version has a solution.
function rlForTaskAt_(s, chapterId, taskId) { var vs = s.chapters[chapterId] || []; for (var i = vs.length - 1; i >= 0; i--) if (vs[i].answered.indexOf(taskId) >= 0) return i; return -1; }
function rlForTask_(s, chapterId, taskId) { var vs = s.chapters[chapterId], i = rlForTaskAt_(s, chapterId, taskId); return i >= 0 ? vs[i] : rlLatest_(s, chapterId); }
// Opiskelijan kooste luvuittain (tehtävittäin uusin hyväksytty versio, jossa tehtävään on ratkaisu) ja yhteensä; luku puuttuu, jos sitä ei ole palautettu.
// answered = tehtyjä (ratkaisu editorissa), unchecked = tehtyjä ilman pisteitä, points = pisteiden summa.
function rlSummary_(m) {
  return m.students.map(function (s) {
    var per = {}, total = 0, scored = 0, tasks = 0, answered = 0, unchecked = 0;
    RL_COURSE.chapters.forEach(function (c) {
      var last = rlLatest_(s, c.id); if (!last) return;
      var sum = 0, n = 0, a = 0, u = 0;
      c.tasks.filter(function (t) { return !t.lesson; }).forEach(function (t) {   // oppitunnin tehtävät näytetään, ei pisteytetä
        var v = rlForTask_(s, c.id, t.id), p = rlTaskScore_(m, s, c.id, v, t.id).score, done = v.answered.indexOf(t.id) >= 0;
        if (p !== '') { sum += p; n++; }
        if (done) { a++; if (p === '') u++; }
      });
      var nt = rlScored_(c).length;
      per[c.id] = { points: rlRound_(sum), scored: n, tasks: nt, answered: a, unchecked: u };
      total += sum; scored += n; tasks += nt; answered += a; unchecked += u;
    });
    return { email: s.email, chapters: per, total: rlRound_(total), scored: scored, tasks: tasks, answered: answered, unchecked: unchecked, progress: s.progress };
  }).sort(function (a, b) { return a.email.localeCompare(b.email, 'fi'); });
}

// Pisteytettävät tehtävät: harjoitustehtävät, ei oppitunnin tehtäviä (lesson, versio 3).
function rlScored_(c) { return c.tasks.filter(function (t) { return !t.lesson; }); }
function rlOverview() {
  var m = rlModel_();
  var chapters = RL_COURSE.chapters.map(function (c) {
    var subs = m.students.filter(function (s) { return !!s.chapters[c.id]; });
    var tasks = c.tasks.map(function (t) {
      // tyhjäksi jätetty tehtävä ei ole ratkaisu eikä arvioitava (opettaja 6.11.2026)
      var empty = 0, scored = 0, open = 0;
      subs.forEach(function (s) {
        var v = rlForTask_(s, c.id, t.id);
        if (v.answered.indexOf(t.id) < 0) { empty++; return; }
        if (t.lesson) return;
        if (rlTaskScore_(m, s, c.id, v, t.id).score !== '') scored++; else open++;
      });
      return { id: t.id, number: t.number, level: t.level, lesson: !!t.lesson, html: t.html, answer: t.answer, submissions: subs.length, empty: empty,
               solutions: subs.length - empty, scored: scored, open: open };
    });
    // itsearvio (opettaja 6.11.2026): kohteet ja jokaisen palauttajan uusimman palautuksen tasot
    var self = (c.self || []).length ? { items: c.self, students: subs.map(function (s) { return { email: s.email, levels: rlLatest_(s, c.id).self }; }) } : null;
    return { id: c.id, number: c.number, title: c.title, submissions: subs.length, tasks: tasks, self: self };
  });
  return { course: RL_COURSE.id, group: RL_CONFIG.GROUP || '', maxPoints: RL_CONFIG.MAX_POINTS, students: m.students.length, chapters: chapters, themes: RL_COURSE.themes || [],
           summary: rlSummary_(m), problems: m.problems };
}
// Jonossa vain opiskelijat, joiden jossakin palautuksessa tehtävään on ratkaisu (opettaja 6.11.2026: tyhjiä ei näytetä);
// pick = uusin versio, jossa ratkaisu on (opettaja 8.11.2026: uudesta palautuksesta puuttuva tehtävä säilyy).
function rlQueue(taskId) {
  var info = rlTaskInfo_(taskId);
  if (!info) throw rlError_('Tuntematon tehtävä.');
  var m = rlModel_(), ch = info.chapter.id;
  return m.students.filter(function (s) { return rlForTaskAt_(s, ch, taskId) >= 0; }).map(function (s) {
    return { email: s.email, pick: rlForTaskAt_(s, ch, taskId), versions: s.chapters[ch].map(function (v) {
      var sc = rlTaskScore_(m, s, ch, v, taskId);
      return { fileId: v.fileId, sub: v.sub, time: v.time, answered: v.answered.indexOf(taskId) >= 0, score: sc.score, from: sc.from };
    }) };
  });
}
function rlVersion_(m, email, chapterId, pick) {
  var found = null;
  m.students.forEach(function (s) { if (s.email === email && s.chapters[chapterId]) s.chapters[chapterId].forEach(function (v) { if (pick(v)) found = v; }); });
  return found;
}
// Yhden opiskelijan yhden tehtävän vastaus tiedostosta. Tiedosto tarkistetaan uudelleen (sama kansio, luku, tunniste ja
// tarkistussumma kuin tuonnissa), ja palautetaan vain tämän tehtävän osat tarkistettuina.
function rlAnswer(req) {
  var info = req && typeof req.task === 'string' ? rlTaskInfo_(req.task) : null;
  if (!info || typeof req.fileId !== 'string' || typeof req.sub !== 'string') throw rlError_('Virheellinen pyyntö.');
  var m = rlModel_();
  var version = rlVersion_(m, req.email, info.chapter.id, function (v) { return v.fileId === req.fileId && v.sub === req.sub; });
  if (!version) throw rlError_('Palautusta ei löydy hyväksytyistä palautuksista. Tuo palautukset uudelleen.');
  var file;
  try { file = DriveApp.getFileById(version.fileId); } catch (e) { throw rlError_('Palautustiedostoa ei voitu avata.'); }
  if (!rlInFolder_(file) || file.getSize() > RL_LIMITS.file) throw rlError_('Palautustiedosto ei ole enää palautuskansiossa tai se on muuttunut.');
  var v;
  try { v = rlValidate_(file.getBlob().getDataAsString('UTF-8'), false); } catch (e) { throw rlError_('Palautustiedosto ei kelpaa enää: ' + rlUserMessage_(e)); }
  if (v.work) { var part = v.parts.filter(function (q) { return q.chapter === info.chapter.id; })[0]; v = part ? { chapter: part.chapter, sha: part.sha, data: part.data } : { chapter: '' }; }
  if (v.chapter !== info.chapter.id || v.data.submission_id !== version.sub || v.sha !== version.sha) throw rlError_('Palautustiedosto on muuttunut tuonnin jälkeen.');
  var a = v.data.answers.filter(function (x) { return x.task === req.task; })[0];
  var where = 'tehtävä ' + info.task.number;
  if (!a) return { status: 'empty', content: [], responses: [] };
  return { status: a.status, content: a.content.map(function (it) { return rlCheckItem_(it, where, true); }),
           responses: (a.responses || []).map(function (r) { return rlCheckResponse_(r, where); }) };
}
function rlSaveScore(req) {
  var info = req && typeof req.task === 'string' ? rlTaskInfo_(req.task) : null;
  if (!info || typeof req.email !== 'string' || typeof req.sub !== 'string') throw rlError_('Virheellinen tallennuspyyntö.');
  if (info.task.lesson) throw rlError_('Oppitunnin tehtävää ei pisteytetä.');
  var value = req.value;
  if (value !== '' && !rlPointsOk_(value)) {
    throw rlError_('Pisteet ovat luku 0–' + RL_CONFIG.MAX_POINTS + ' (enintään kaksi desimaalia) tai tyhjä (arvioimaton).');
  }
  var lock = rlLock_(10000);
  try {
    var m = rlModel_();
    if (!rlVersion_(m, req.email, info.chapter.id, function (v) { return v.sub === req.sub; })) throw rlError_('Palautusta ei löydy hyväksytyistä palautuksista, joten pisteitä ei tallennettu.');
    var sh = rlSheet_(RL_CONFIG.SCORES_SHEET, RL_SCORE_HEAD);
    var key = rlScoreKey_(req.email, req.sub, req.task), rows = rlRows_(sh, 1), line = -1;
    for (var i = 0; i < rows.length; i++) if (rlText_(rows[i][0]) === key) { line = i + 2; break; }   // avaimella, ei rivin paikalla
    var now = new Date();
    var row = [key, req.email, req.sub, req.task, info.task.number, value, now, info.chapter.id].map(rlCell_);
    if (line < 0) line = sh.getLastRow() + 1;
    sh.getRange(line, 1, 1, row.length).setValues([row]);
    SpreadsheetApp.flush();
    return { value: value, saved: rlFmt_(now) };
  } finally { lock.releaseLock(); }
}

// Opettajan päätös tarkistettavasta tai hyväksytystä palautuksesta arviointinäkymästä (sama kuin sarake Opettajan päätös).
function rlSetDecision(req) {
  var d = req && req.decision;
  if (!req || typeof req.key !== 'string' || (d !== '' && d !== RL_DECISION.ACCEPT && d !== RL_DECISION.REJECT)) throw rlError_('Virheellinen päätös.');
  var lock = rlLock_(10000);
  try {
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(RL_CONFIG.SUBMISSIONS_SHEET);
    var rows = sh ? rlRows_(sh, 1) : [];
    for (var i = 0; i < rows.length; i++) if (rlText_(rows[i][0]) === req.key) {
      sh.getRange(i + 2, RL_C.decision + 1, 1, 1).setValues([[d]]);
      SpreadsheetApp.flush();
      return { decision: d };
    }
    throw rlError_('Palautusta ei löydy.');
  } finally { lock.releaseLock(); }
}
// Pisteet taulukkona (CSV, puolipiste, desimaalipilkku, UTF-8 BOM): opiskelija, pisteet luvuittain (uusin hyväksytty
// versio; tyhjä = lukua ei palautettu), yhteensä, palautetut luvut, tehdyt ja tarkistamattomat tehtävät.
// Kentät, jotka alkavat merkillä = + - @, saavat eteensä heittomerkin, jottei taulukko-ohjelma lue niitä kaavoiksi.
function rlScoresCsv() {
  var m = rlModel_(), chapters = RL_COURSE.chapters;
  var q = function (v) { v = v === null || v === undefined ? '' : String(v); if (/^[=+\-@\t\r]/.test(v)) v = "'" + v; return /[;"\n\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; };
  var lines = [['Opiskelija'].concat(chapters.map(function (c) { return rlChapterName_(c) + ' (max ' + rlScored_(c).length * RL_CONFIG.MAX_POINTS + ')'; }), ['Yhteensä', 'Palautettuja lukuja', 'Tehty', 'Tarkistamatta', 'Annetut tehty']).map(q).join(';')];
  rlSummary_(m).forEach(function (s) {
    var cells = chapters.map(function (c) { return s.chapters[c.id] ? rlNum_(s.chapters[c.id].points) : ''; });
    lines.push([s.email].concat(cells, [rlNum_(s.total), Object.keys(s.chapters).length, s.answered, s.unchecked, s.progress ? s.progress.done.length + '/' + s.progress.total : '']).map(q).join(';'));
  });
  return '﻿' + lines.join('\r\n') + '\r\n';
}
