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

// Samat rajat kuin RuukkiLabran palautus.js:ssä (LIMITS). Formsin tiedostokoon raja asetetaan 10 Mt:ksi.
var RL_LIMITS = { file: 9000000, image: 2000000, side: 5000, images: 40, text: 20000, latex: 4000, items: 400, mathPng: 200000 };
var RL_FORMAT = 'ruukkilabra-palautus', RL_VERSION = 1;
var RL_STATUS = { OK: 'Hyväksytty', DUP: 'Kaksoiskappale', CHECK: 'Tarkistettava', BAD: 'Virheellinen', READ: 'Lukuvirhe' };
var RL_DECISION = { ACCEPT: 'Hyväksy', REJECT: 'Hylkää' };
var RL_SUB_HEAD = ['Avain', 'Palautusaika', 'Sähköposti', 'Palautustunniste', 'Tila', 'Syy', 'Opettajan päätös',
  'Vastattuja', 'Vastatut tehtävät', 'Tyhjiä', 'Tiedosto', 'Koko (t)', 'Sisällön SHA-256', 'Tuotu', 'Lomakkeen rivi', 'Luku'];
var RL_SCORE_HEAD = ['Avain', 'Sähköposti', 'Palautustunniste', 'Tehtävä', 'Tehtävän numero', 'Pisteet', 'Tallennettu', 'Luku'];
var RL_C = { key: 0, time: 1, email: 2, sub: 3, status: 4, reason: 5, decision: 6, nAnswered: 7, answered: 8, nEmpty: 9, file: 10, size: 11, sha: 12, imported: 13, row: 14, chapter: 15 };
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
    only(['type', 'latex', 'png', 'w', 'h']);
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
    return out;
  }
  if (it.type === 'image') {
    only(['type', 'mime', 'data', 'w', 'h']);
    if (it.mime !== 'image/png' && it.mime !== 'image/jpeg') throw rlError_(where + ': kuvamuoto ei ole sallittu (vain PNG ja JPEG)');
    var info = null;
    if (deep) {
      info = rlImageInfo_(rlB64Bytes_(it.data, RL_LIMITS.image, where));
      if (!info || info.mime !== it.mime) throw rlError_(where + ': kuvan sisältö ei ole ' + (it.mime === 'image/png' ? 'PNG' : 'JPEG') + '-kuva');
      if (info.w < 1 || info.h < 1 || info.w > RL_LIMITS.side || info.h > RL_LIMITS.side) throw rlError_(where + ': kuvan koko on liian suuri (yli ' + RL_LIMITS.side + ' px)');
    } else if (typeof it.data !== 'string' || it.data.length > RL_LIMITS.image * 1.4) throw rlError_(where + ': kuva on liian suuri');
    return { type: 'image', mime: it.mime, data: it.data, w: info ? info.w : it.w, h: info ? info.h : it.h };
  }
  throw rlError_(where + ': tuntematon sisältötyyppi');
}
/**
 * Tarkistaa tiedoston tekstin. Palauttaa { data, answered: [id], empty: [id], sha } tai heittää virheen, jonka viesti
 * kertoo syyn opettajalle. deep = kuvadata puretaan ja tarkistetaan tavuista (tuonnissa aina).
 */
function rlValidate_(text, deep) {
  var data;
  try { data = JSON.parse(text); } catch (e) { throw rlError_('tiedosto ei ole JSON-tiedosto'); }
  if (!data || typeof data !== 'object' || Array.isArray(data)) throw rlError_('tiedoston rakenne on virheellinen');
  if (data.format !== RL_FORMAT) throw rlError_('tiedosto ei ole RuukkiLabran palautustiedosto');
  if (typeof data.version !== 'number') throw rlError_('tiedostomuodon versio puuttuu');
  if (data.version > RL_VERSION) throw rlError_('tiedostomuodon versio ' + data.version + ' on uudempi kuin tämä skripti tuntee');
  if (data.version !== RL_VERSION) throw rlError_('tuntematon tiedostomuodon versio');
  if (typeof data.chapter !== 'string' || !rlChapters_()[data.chapter]) throw rlError_('tiedosto on toiselta opintojaksolta tai tuntemattomasta luvusta (' + String(data.chapter).slice(0, 20) + ')');
  if (typeof data.submission_id !== 'string' || !/^[0-9a-f]{32}$/.test(data.submission_id)) throw rlError_('palautustunniste puuttuu tai on virheellinen');
  if (typeof data.content_sha256 !== 'string' || !/^[0-9a-f]{64}$/.test(data.content_sha256)) throw rlError_('tarkistussumma puuttuu');
  if (!Array.isArray(data.answers)) throw rlError_('vastaukset puuttuvat');
  var tasks = rlTasks_(data.chapter), seen = Object.create(null), answered = [], empty = [], images = 0, canon = [];
  for (var i = 0; i < data.answers.length; i++) {
    var a = data.answers[i];
    if (!a || typeof a !== 'object' || typeof a.task !== 'string') throw rlError_('vastaus ' + (i + 1) + ' on virheellinen');
    var t = tasks[a.task];
    if (!t) throw rlError_('tuntematon tehtävä ' + a.task.slice(0, 40));
    if (seen[a.task]) throw rlError_('tehtävä ' + t.number + ' on tiedostossa kahdesti');
    seen[a.task] = true;
    var where = 'tehtävä ' + t.number;
    if (!Array.isArray(a.content) || a.content.length > RL_LIMITS.items) throw rlError_(where + ': virheellinen sisältö');
    if (a.status !== 'answered' && a.status !== 'empty') throw rlError_(where + ': tuntematon tila');
    if ((a.status === 'empty') !== (a.content.length === 0)) throw rlError_(where + ': tila ja sisältö eivät täsmää');
    var chars = 0, items = [];
    for (var j = 0; j < a.content.length; j++) {
      var it = rlCheckItem_(a.content[j], where, deep);
      if (it.type === 'text') chars += it.text.length;
      if (it.type === 'image') images++;
      items.push(it.type === 'math' ? { type: 'math', latex: it.latex } : a.content[j]);
    }
    if (chars > RL_LIMITS.text) throw rlError_(where + ': teksti on liian pitkä');
    canon.push({ task: a.task, status: a.status, content: items });
    (a.status === 'answered' ? answered : empty).push(a.task);
  }
  for (var id in tasks) if (!seen[id]) throw rlError_('tehtävä ' + tasks[id].number + ' puuttuu tiedostosta');
  if (images > RL_LIMITS.images) throw rlError_('kuvia on liikaa (' + images + ')');
  var sha = rlSha_(JSON.stringify(canon));
  if (sha !== data.content_sha256) throw rlError_('tarkistussumma ei täsmää: tiedostoa on muutettu tai se on vioittunut');
  return { data: data, chapter: data.chapter, answered: answered, empty: empty, sha: sha };
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
  var out = { status: RL_STATUS.BAD, reason: '', sub: '', answered: [], empty: [], size: '', sha: '', chapter: '' };
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
    out.status = RL_STATUS.OK; out.sub = v.data.submission_id; out.answered = v.answered; out.empty = v.empty; out.sha = v.sha; out.chapter = v.chapter;
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
      var p = rlProcess_(resp), reason = p.reason;
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
      var row = [resp.key, resp.time || '', resp.email, p.sub, p.status, reason, '', p.answered.length, p.answered.join(','), p.empty.length,
        resp.ids.length ? 'https://drive.google.com/open?id=' + resp.ids[0] : '', p.size, p.sha, new Date(), resp.row, p.chapter].map(rlCell_);
      counts[p.status]++;
      if (at !== undefined) { row[RL_C.decision] = rows[at][RL_C.decision]; rows[at] = row; touched[at] = true; retried++; }
      else { byKey[resp.key] = rows.length; rows.push(row); added.push(rows.length - 1); }
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
    if (!rlAccepted_(r) || !time || !ch) return;
    var s = students[email] || (students[email] = { email: email, chapters: Object.create(null), first: time.getTime() });
    s.first = Math.min(s.first, time.getTime());
    (s.chapters[ch.id] || (s.chapters[ch.id] = [])).push({ fileId: rlText_(r[RL_C.file]).replace(/^.*[?&]id=/, ''), sub: rlText_(r[RL_C.sub]), timeMs: time.getTime(), time: rlFmt_(time),
      answered: rlText_(r[RL_C.answered]).split(',').filter(String), sha: rlText_(r[RL_C.sha]) });
  });
  var list = Object.keys(students).map(function (k) { return students[k]; });
  list.forEach(function (s) { for (var c in s.chapters) s.chapters[c].sort(function (a, b) { return a.timeMs - b.timeMs; }); });
  list.sort(function (a, b) { return a.first - b.first || (a.email < b.email ? -1 : 1); });   // ensimmäisen palautuksen järjestys
  return { students: list, scores: scores, problems: problems };
}
function rlScoreOf_(m, email, sub, task) { var v = m.scores[rlScoreKey_(email, sub, task)]; return v === undefined ? '' : v; }
function rlRound_(x) { return Math.round(x * 100) / 100; }
function rlPointsOk_(v) { return typeof v === 'number' && isFinite(v) && v >= 0 && v <= RL_CONFIG.MAX_POINTS && Math.abs(Math.round(v * 100) - v * 100) < 1e-6; }
function rlNum_(x) { return String(rlRound_(x)).replace('.', ','); }   // suomalainen desimaalipilkku
function rlLatest_(s, chapterId) { var vs = s.chapters[chapterId]; return vs ? vs[vs.length - 1] : null; }
// Opiskelijan kooste luvuittain (uusin hyväksytty versio) ja yhteensä; luku puuttuu, jos sitä ei ole palautettu.
// answered = tehtyjä (ratkaisu editorissa), unchecked = tehtyjä ilman pisteitä, points = pisteiden summa.
function rlSummary_(m) {
  return m.students.map(function (s) {
    var per = {}, total = 0, scored = 0, tasks = 0, answered = 0, unchecked = 0;
    RL_COURSE.chapters.forEach(function (c) {
      var last = rlLatest_(s, c.id); if (!last) return;
      var sum = 0, n = 0, a = 0, u = 0;
      c.tasks.forEach(function (t) {
        var p = rlScoreOf_(m, s.email, last.sub, t.id), done = last.answered.indexOf(t.id) >= 0;
        if (p !== '') { sum += p; n++; }
        if (done) { a++; if (p === '') u++; }
      });
      per[c.id] = { points: rlRound_(sum), scored: n, tasks: c.tasks.length, answered: a, unchecked: u };
      total += sum; scored += n; tasks += c.tasks.length; answered += a; unchecked += u;
    });
    return { email: s.email, chapters: per, total: rlRound_(total), scored: scored, tasks: tasks, answered: answered, unchecked: unchecked };
  }).sort(function (a, b) { return a.email.localeCompare(b.email, 'fi'); });
}

function rlOverview() {
  var m = rlModel_();
  var chapters = RL_COURSE.chapters.map(function (c) {
    var subs = m.students.filter(function (s) { return !!s.chapters[c.id]; });
    var tasks = c.tasks.map(function (t) {
      // tyhjäksi jätetty tehtävä ei ole ratkaisu eikä arvioitava (opettaja 6.11.2026)
      var empty = 0, scored = 0, open = 0;
      subs.forEach(function (s) {
        var last = rlLatest_(s, c.id);
        if (last.answered.indexOf(t.id) < 0) { empty++; return; }
        if (rlScoreOf_(m, s.email, last.sub, t.id) !== '') scored++; else open++;
      });
      return { id: t.id, number: t.number, level: t.level, html: t.html, answer: t.answer, submissions: subs.length, empty: empty,
               solutions: subs.length - empty, scored: scored, open: open };
    });
    return { id: c.id, number: c.number, title: c.title, submissions: subs.length, tasks: tasks };
  });
  return { course: RL_COURSE.id, group: RL_CONFIG.GROUP || '', maxPoints: RL_CONFIG.MAX_POINTS, students: m.students.length, chapters: chapters,
           summary: rlSummary_(m), problems: m.problems };
}
// Jonossa vain opiskelijat, joiden uusimmassa palautuksessa tehtävään on ratkaisu (opettaja 6.11.2026: tyhjiä ei näytetä).
function rlQueue(taskId) {
  var info = rlTaskInfo_(taskId);
  if (!info) throw rlError_('Tuntematon tehtävä.');
  var m = rlModel_(), ch = info.chapter.id;
  return m.students.filter(function (s) { var last = rlLatest_(s, ch); return !!last && last.answered.indexOf(taskId) >= 0; }).map(function (s) {
    return { email: s.email, versions: s.chapters[ch].map(function (v) {
      return { fileId: v.fileId, sub: v.sub, time: v.time, answered: v.answered.indexOf(taskId) >= 0, score: rlScoreOf_(m, s.email, v.sub, taskId) };
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
  if (v.chapter !== info.chapter.id || v.data.submission_id !== version.sub || v.sha !== version.sha) throw rlError_('Palautustiedosto on muuttunut tuonnin jälkeen.');
  var a = v.data.answers.filter(function (x) { return x.task === req.task; })[0];
  var where = 'tehtävä ' + info.task.number;
  return { status: a.status, content: a.content.map(function (it) { return rlCheckItem_(it, where, true); }) };
}
function rlSaveScore(req) {
  var info = req && typeof req.task === 'string' ? rlTaskInfo_(req.task) : null;
  if (!info || typeof req.email !== 'string' || typeof req.sub !== 'string') throw rlError_('Virheellinen tallennuspyyntö.');
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
  var lines = [['Opiskelija'].concat(chapters.map(function (c) { return rlChapterName_(c) + ' (max ' + c.tasks.length * RL_CONFIG.MAX_POINTS + ')'; }), ['Yhteensä', 'Palautettuja lukuja', 'Tehty', 'Tarkistamatta']).map(q).join(';')];
  rlSummary_(m).forEach(function (s) {
    var cells = chapters.map(function (c) { return s.chapters[c.id] ? rlNum_(s.chapters[c.id].points) : ''; });
    lines.push([s.email].concat(cells, [rlNum_(s.total), Object.keys(s.chapters).length, s.answered, s.unchecked]).map(q).join(';'));
  });
  return '﻿' + lines.join('\r\n') + '\r\n';
}
