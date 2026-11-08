/* Paikallinen arviointisivu (Lauri 5.11.2026: eduespoossa Apps Script on estetty). Tämä tiedosto korvaa selaimessa ne
   Google-palvelut, joita Code.gs käyttää: palautustiedostot luetaan Drivesta ladatusta zip-tiedostosta (tai
   JSON-tiedostoista), ja välilehdet "RL Palautukset" ja "RL Pisteet" ovat tämän selaimen localStoragessa
   ryhmittäin (avain ruukkilabra:arviointi:ryhma:<ryhmä>) opettajan omalla koneella. Tuodut palautustiedostot ovat
   saman selaimen IndexedDB:ssä (tietokanta ruukkilabra-arviointi), joten vastaukset näkyvät myös sivun sulkemisen jälkeen.
   Yksi sivu periodia kohti, ja siinä ovat kaikki periodin kurssit (RL_COURSES, opettaja 6.11.2026). Ainoa painike on
   "Tuo tiedosto": ryhmä tunnistetaan zipin ylimmästä kansiosta, joka on lomakkeen nimi ("FY3.2 lv 2026-27 Palauta
   ratkaisut (File responses)") ja kurssi ryhmän nimestä (FY3). Ryhmä muistaa lomakkeensa, eikä toisen lomakkeen zipiä
   lueta samaan ryhmään. Mitään ei lähetetä minnekään, eikä sivu lataa mitään verkosta (Content-Security-Policy).
   Palauttajan tunniste on Formsin tiedoston nimeen lisäämä nimi: "<alkuperäinen nimi> - <Etunimi Sukunimi>.json".
   Palautusaika on tiedoston aika Driven zipissä. Rakennetaan sivuksi palautus/arviointi-<lukuvuosi>-p<periodi>.html
   (scripts/palautus_tasks.py). */
(function () {
  'use strict';
  var LOCAL = window.RL_LOCAL_STATE = { files: {}, entries: [], sheets: [], forms: [], group: '' };
  var STORE = 'ruukkilabra:arviointi:';

  /* ---- Sheets: välilehdet muistissa; RL-välilehdet tallessa localStoragessa ---- */
  function Range(sh, r, c, nr, nc) { this.sh = sh; this.r = r; this.c = c; this.nr = nr || 1; this.nc = nc || 1; }
  Range.prototype.getValues = function () {
    var out = [];
    for (var i = 0; i < this.nr; i++) { var row = this.sh.data[this.r - 1 + i] || []; var o = []; for (var j = 0; j < this.nc; j++) { var v = row[this.c - 1 + j]; o.push(v === undefined ? '' : v); } out.push(o); }
    return out;
  };
  Range.prototype.setValues = function (vals) {
    for (var i = 0; i < this.nr; i++) {
      var row = this.sh.data[this.r - 1 + i] || (this.sh.data[this.r - 1 + i] = []);
      for (var j = 0; j < this.nc; j++) { var v = vals[i][j]; if (typeof v === 'string' && v.charAt(0) === "'") v = v.slice(1); row[this.c - 1 + j] = v; }
    }
    for (var k = 0; k < this.sh.data.length; k++) if (!this.sh.data[k]) this.sh.data[k] = [];
    return this;
  };
  ['setNumberFormat', 'setFontWeight', 'setDataValidation'].forEach(function (m) { Range.prototype[m] = function () { return this; }; });
  function Sheet(name, data) { this.name = name; this.data = data || []; }
  Sheet.prototype.getName = function () { return this.name; };
  Sheet.prototype.getLastRow = function () { var n = this.data.length; while (n && this.data[n - 1].join('') === '') n--; return n; };
  Sheet.prototype.getLastColumn = function () { return this.data.reduce(function (m, r) { return Math.max(m, r.length); }, 0); };
  Sheet.prototype.getMaxRows = function () { return 1000; };
  Sheet.prototype.getRange = function (r, c, nr, nc) { return new Range(this, r, c, nr, nc); };
  Sheet.prototype.getDataRange = function () { return new Range(this, 1, 1, this.getLastRow(), this.getLastColumn()); };
  Sheet.prototype.setFrozenRows = function () {};
  Sheet.prototype.protect = function () { var p = { setDescription: function () { return p; }, setWarningOnly: function () { return p; } }; return p; };
  var ss = {
    getSheetByName: function (n) { return LOCAL.sheets.filter(function (s) { return s.name === n; })[0] || null; },
    insertSheet: function (n) { var s = new Sheet(n, []); LOCAL.sheets.push(s); return s; },
    getSheets: function () { return LOCAL.sheets.slice(); }
  };
  var dv = function () { var b = {}; ['requireValueInList', 'setAllowInvalid'].forEach(function (m) { b[m] = function () { return b; }; }); b.build = function () { return {}; }; return b; };
  window.SpreadsheetApp = { getActiveSpreadsheet: function () { return ss; }, flush: function () {}, newDataValidation: dv };
  window.LockService = { getDocumentLock: function () { return { tryLock: function () { return true; }, releaseLock: function () {} }; } };

  var course = function () { return window.RL_COURSE ? RL_COURSE.id : ''; };
  var COURSES = window.RL_COURSES || (window.RL_COURSE ? (function () { var m = {}; m[RL_COURSE.id] = RL_COURSE; return m; })() : {});
  var key = function (g) { return STORE + 'ryhma:' + (g === undefined ? LOCAL.group : g); };
  var listKey = function () { return STORE + 'ryhmat'; }, chosenKey = function () { return STORE + 'valittu'; };
  function groups() {
    try { var a = JSON.parse(localStorage.getItem(listKey()) || '[]'); return Array.isArray(a) ? a.filter(function (x) { return typeof x === 'string'; }) : []; } catch (e) { return []; }
  }
  function setGroups(a) { try { localStorage.setItem(listKey(), JSON.stringify(a)); return true; } catch (e) { return false; } }
  // Ennen 6.11.2026 ryhmät olivat kurssikohtaisilla avaimilla (ruukkilabra:arviointi:FY3:ryhma:<ryhmä>): kopioidaan kerran.
  (function migrate() {
    try {
      var list = groups();
      Object.keys(COURSES).forEach(function (c) {
        var old = JSON.parse(localStorage.getItem(STORE + c + ':ryhmat') || '[]');
        (Array.isArray(old) ? old : []).forEach(function (g) {
          if (typeof g !== 'string' || list.indexOf(g) >= 0) return;
          var v = localStorage.getItem(STORE + c + ':ryhma:' + g);
          if (v) localStorage.setItem(STORE + 'ryhma:' + g, v);
          list.push(g);
        });
      });
      setGroups(list);
    } catch (e) { /* ei vanhoja tietoja */ }
  })();
  // Ryhmän nimi lomakkeen nimen alusta: "FY3.2 lv 2026-27 Palauta ratkaisut" -> FY3.2; kurssi: FY3 (myös "FY03.2" -> FY3)
  function groupOfForm(form) { var m = /^\s*(FY\s*0*\d+[.,]\d+[A-Za-z]?)(?=$|[\s_-])/i.exec(form || ''); return m ? m[1].replace(/\s+/g, '').replace(',', '.').toUpperCase() : ''; }
  function courseOfGroup(g) { var m = /^FY\s*0*(\d+)/i.exec(g || ''); return m ? 'FY' + Number(m[1]) : ''; }
  var reviver = function (k, v) { return v && typeof v === 'object' && v.__date ? new Date(v.__date) : v; };
  var replacer = function (k, v) { return this[k] instanceof Date ? { __date: this[k].toISOString() } : v; };
  function saveSheets() {
    var keep = LOCAL.sheets.filter(function (s) { return /^RL /.test(s.name); }).map(function (s) { return { name: s.name, data: s.data }; });
    if (!LOCAL.group) return false;
    try { localStorage.setItem(key(), JSON.stringify({ format: 'ruukkilabra-arviointi', version: 1, course: course(), group: LOCAL.group, forms: LOCAL.forms, sheets: keep }, replacer)); return true; } catch (e) { return false; }
  }
  function loadSheets(text) {
    var st = JSON.parse(text, reviver);
    if (!st || st.format !== 'ruukkilabra-arviointi' || !Array.isArray(st.sheets)) throw new Error('format');
    if (st.course && st.course !== course()) throw new Error('course');
    LOCAL.sheets = LOCAL.sheets.filter(function (s) { return !/^RL /.test(s.name); }).concat(st.sheets.map(function (s) { return new Sheet(s.name, s.data); }));
    LOCAL.forms = Array.isArray(st.forms) ? st.forms.filter(function (x) { return typeof x === 'string'; }) : [];
    return st;
  }
  /* ---- palautustiedostot IndexedDB:ssä ryhmittäin (opettaja 6.11.2026: vastaukset eivät saa kadota, kun sivu suljetaan) ---- */
  var DB = null;
  function db() {
    if (DB) return DB;
    DB = new Promise(function (ok, no) {
      try {
        var r = indexedDB.open('ruukkilabra-arviointi', 1);
        r.onupgradeneeded = function () { r.result.createObjectStore('palautukset'); };
        r.onsuccess = function () { ok(r.result); };
        r.onerror = function () { no(r.error); };
      } catch (e) { no(e); }
    });
    return DB;
  }
  function idb(mode, fn) {
    return db().then(function (d) {
      return new Promise(function (ok, no) {
        var tx = d.transaction('palautukset', mode), st = tx.objectStore('palautukset'), out = fn(st);
        tx.oncomplete = function () { ok(out && 'result' in out ? out.result : undefined); };
        tx.onerror = tx.onabort = function () { no(tx.error); };
      });
    });
  }
  function storeFiles(g, files, entries) { return idb('readwrite', function (st) { st.put({ files: files, entries: entries }, g); }); }
  function dropFiles(g) { return idb('readwrite', function (st) { st.delete(g); }).catch(function () {}); }
  function loadFiles(g) {
    if (!g || MEM[g]) return Promise.resolve();
    return idb('readonly', function (st) { return st.get(g); }).then(function (v) {
      if (v && v.files && Array.isArray(v.entries) && !MEM[g]) MEM[g] = { files: v.files, entries: v.entries };
    }, function () {});
  }
  // Viimeisimmän tuonnin peruminen (opettaja 8.11.2026: väärä tiedosto pois): tuontia edeltävä ryhmälista, kunkin
  // ryhmän tila (localStorage-merkkijono) ja tuonnin lisäämät tiedostot. Vain yksi, viimeisin tuonti.
  var UNDO = '__peru__';
  function getUndo() { return idb('readonly', function (st) { return st.get(UNDO); }).then(function (v) { return v || null; }, function () { return null; }); }
  function setUndo(v) { return idb('readwrite', function (st) { if (v) st.put(v, UNDO); else st.delete(UNDO); }).catch(function () {}); }
  function savedOf(g) { try { return JSON.parse(localStorage.getItem(key(g)) || 'null'); } catch (e) { return null; } }
  // Ryhmän vaihto: edellisen ryhmän tiedostot jäävät muistiin (sivun sulkemiseen asti), uuden ryhmän tila localStoragesta.
  // Kurssi vaihtuu ryhmän mukana (RL_COURSE: Code.gs lukee siitä luvut ja tehtävät).
  var MEM = {};
  function useGroup(g) {
    if (LOCAL.group) MEM[LOCAL.group] = { files: LOCAL.files, entries: LOCAL.entries };
    LOCAL.group = g; LOCAL.sheets = []; LOCAL.files = {}; LOCAL.entries = []; LOCAL.forms = [];
    RL_CONFIG.GROUP = g;
    var st = g ? savedOf(g) : null;
    window.RL_COURSE = COURSES[(st && st.course) || courseOfGroup(g)] || COURSES[Object.keys(COURSES)[0]] || null;
    if (!g) return;
    if (MEM[g]) { LOCAL.files = MEM[g].files; LOCAL.entries = MEM[g].entries; }
    try { var saved = localStorage.getItem(key()); if (saved) loadSheets(saved); localStorage.setItem(chosenKey(), g); } catch (e) { /* aloitetaan tyhjästä */ }
    if (LOCAL.entries.length) addEntries([]);
  }
  // Zipin ylin kansio = lomakkeen palautuskansio "<lomakkeen nimi> (File responses)"
  function formOf(path) { var i = path.indexOf('/'); return i > 0 ? path.slice(0, i) : ''; }
  // Ryhmä, jolle lomake jo kuuluu (myös itse nimetty, esim. "FY03.2"), muuten lomakkeen nimestä
  function groupFor(form) {
    var list = groups();
    for (var i = 0; i < list.length; i++) { var st = savedOf(list[i]); if (st && Array.isArray(st.forms) && st.forms.indexOf(form) >= 0) return list[i]; }
    return groupOfForm(form);
  }

  /* ---- Drive: ladatut tiedostot muistissa, kaikki "palautuskansiossa" local ---- */
  var iter = function (a) { var i = 0; return { hasNext: function () { return i < a.length; }, next: function () { return a[i++]; } }; };
  var folder = { getId: function () { return 'local'; }, getParents: function () { return iter([]); } };
  window.DriveApp = {
    getFileById: function (id) {
      var f = LOCAL.files[id];
      if (!f) throw new Error('missing');
      return { getId: function () { return id; }, getSize: function () { return f.size; }, getParents: function () { return iter([folder]); },
               getBlob: function () { return { getDataAsString: function () { return f.text; } }; } };
    }
  };

  /* ---- Utilities ---- */
  // SHA-256 (synchronous, UTF-8), as Utilities.computeDigest returns it: signed bytes
  var K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2];
  function sha256(bytes) {
    var H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
    var l = bytes.length, n = ((l + 9 + 63) >> 6) << 6, m = new Uint8Array(n); m.set(bytes); m[l] = 0x80;
    var bits = l * 8; for (var i = 0; i < 8; i++) m[n - 1 - i] = Math.floor(bits / Math.pow(2, 8 * i)) & 255;
    var w = new Int32Array(64);
    for (var o = 0; o < n; o += 64) {
      for (var t = 0; t < 16; t++) w[t] = (m[o + 4 * t] << 24) | (m[o + 4 * t + 1] << 16) | (m[o + 4 * t + 2] << 8) | m[o + 4 * t + 3];
      for (t = 16; t < 64; t++) {
        var a = w[t - 15], b = w[t - 2];
        var s0 = ((a >>> 7) | (a << 25)) ^ ((a >>> 18) | (a << 14)) ^ (a >>> 3), s1 = ((b >>> 17) | (b << 15)) ^ ((b >>> 19) | (b << 13)) ^ (b >>> 10);
        w[t] = (w[t - 16] + s0 + w[t - 7] + s1) | 0;
      }
      var A = H[0], B = H[1], C = H[2], D = H[3], E = H[4], F = H[5], G = H[6], Hh = H[7];
      for (t = 0; t < 64; t++) {
        var S1 = ((E >>> 6) | (E << 26)) ^ ((E >>> 11) | (E << 21)) ^ ((E >>> 25) | (E << 7)), ch = (E & F) ^ (~E & G);
        var T1 = (Hh + S1 + ch + K[t] + w[t]) | 0;
        var S0 = ((A >>> 2) | (A << 30)) ^ ((A >>> 13) | (A << 19)) ^ ((A >>> 22) | (A << 10)), mj = (A & B) ^ (A & C) ^ (B & C);
        var T2 = (S0 + mj) | 0;
        Hh = G; G = F; F = E; E = (D + T1) | 0; D = C; C = B; B = A; A = (T1 + T2) | 0;
      }
      H[0] = (H[0] + A) | 0; H[1] = (H[1] + B) | 0; H[2] = (H[2] + C) | 0; H[3] = (H[3] + D) | 0; H[4] = (H[4] + E) | 0; H[5] = (H[5] + F) | 0; H[6] = (H[6] + G) | 0; H[7] = (H[7] + Hh) | 0;
    }
    var out = []; H.forEach(function (h) { out.push(h >> 24, (h << 8) >> 24, (h << 16) >> 24, (h << 24) >> 24); });
    return out;
  }
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  window.Utilities = {
    DigestAlgorithm: { SHA_256: 'SHA_256' }, Charset: { UTF_8: 'UTF-8' },
    computeDigest: function (alg, text) { return sha256(new TextEncoder().encode(text)); },
    base64Decode: function (s) { var b = atob(s), out = new Array(b.length); for (var i = 0; i < b.length; i++) { var c = b.charCodeAt(i); out[i] = c > 127 ? c - 256 : c; } return out; },
    formatDate: function (d, tz, fmt) {
      var p = {}; new Intl.DateTimeFormat('en-GB', { timeZone: tz, year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: '2-digit', second: '2-digit', hourCycle: 'h23' })
        .formatToParts(d).forEach(function (x) { p[x.type] = x.value; });
      if (fmt === 'd.M.yyyy') return Number(p.day) + '.' + Number(p.month) + '.' + p.year;
      return Number(p.hour) + '.' + pad(Number(p.minute)) + '.' + pad(Number(p.second));
    }
  };

  /* ---- google.script.run: palvelinfunktio kutsutaan tässä selaimessa; tulos JSON-muunnettuna kuten Apps Scriptissä ---- */
  var runner = function (ok, no) {
    return new Proxy({}, { get: function (_, name) {
      if (name === 'withSuccessHandler') return function (f) { return runner(f, no); };
      if (name === 'withFailureHandler') return function (f) { return runner(ok, f); };
      return function (arg) {
        var a = arg === undefined ? undefined : JSON.parse(JSON.stringify(arg));
        setTimeout(function () {
          var r;
          if (!/^rl(Overview|Queue|Answer|SaveScore|SetDecision|ScoresCsv)$/.test(name)) { if (no) no(new Error('tuntematon toiminto')); return; }
          if (name === 'rlAnswer' && !LOCAL.entries.length) { if (no) no(new Error('Vastauksia ei ole tässä selaimessa. Tuo ryhmän zip-tiedosto uudelleen ylhäältä (Tuo tiedosto).')); return; }
          try { r = window[name](a); } catch (e) { if (no) no(new Error(e && e.rlUser ? e.message : 'odottamaton virhe')); return; }
          if (/^rl(SaveScore|SetDecision)$/.test(name) && !saveSheets()) { if (no) no(new Error('Selain ei salli tallentamista (localStorage). Pisteitä ei tallennettu.')); return; }
          if (ok) ok(r === undefined ? null : JSON.parse(JSON.stringify(r)));
        }, 0);
      };
    } });
  };
  window.google = { script: { get run() { return runner(null, null); } } };

  /* ---- zip (Driven lataama kansio): keskushakemisto ja deflate selaimen omalla DecompressionStreamilla ---- */
  function readZip(buf) {
    var dv = new DataView(buf), u8 = new Uint8Array(buf), eocd = -1;
    for (var i = u8.length - 22; i >= Math.max(0, u8.length - 65557); i--) if (dv.getUint32(i, true) === 0x06054b50) { eocd = i; break; }
    if (eocd < 0) throw new Error('Tiedosto ei ole zip-tiedosto.');
    var n = dv.getUint16(eocd + 10, true), p = dv.getUint32(eocd + 16, true), out = [];
    for (var k = 0; k < n; k++) {
      if (dv.getUint32(p, true) !== 0x02014b50) throw new Error('Zip-tiedosto on vioittunut.');
      var method = dv.getUint16(p + 10, true), time = dv.getUint16(p + 12, true), date = dv.getUint16(p + 14, true);
      var csize = dv.getUint32(p + 20, true), size = dv.getUint32(p + 24, true), nl = dv.getUint16(p + 28, true), xl = dv.getUint16(p + 30, true), cl = dv.getUint16(p + 32, true);
      var off = dv.getUint32(p + 42, true), name = new TextDecoder('utf-8').decode(u8.subarray(p + 46, p + 46 + nl));
      var start = off + 30 + dv.getUint16(off + 26, true) + dv.getUint16(off + 28, true);
      out.push({ name: name, method: method, size: size, data: u8.subarray(start, start + csize),
        time: new Date(1980 + (date >> 9), ((date >> 5) & 15) - 1, date & 31, time >> 11, (time >> 5) & 63, (time & 31) * 2) });
      p += 46 + nl + xl + cl;
    }
    return out;
  }
  function inflate(e) {
    if (e.method === 0) return Promise.resolve(new TextDecoder('utf-8').decode(e.data));
    if (e.method !== 8) return Promise.reject(new Error('tuntematon pakkaus'));
    return new Response(new Blob([e.data]).stream().pipeThrough(new DecompressionStream('deflate-raw'))).text();
  }
  // "fy3-1.ratkaisut - Aino Opiskelija.json" -> "Aino Opiskelija" (Forms lisää palauttajan nimen loppuun)
  function nameOf(path) {
    var base = path.split('/').pop().replace(/\.[^.]*$/, ''), i = base.lastIndexOf(' - ');
    return i > 0 ? base.slice(i + 3).trim() : '';
  }
  function idOf(path, size, time) {
    var h = sha256(new TextEncoder().encode(path + '|' + size + '|' + time.getTime())), s = '';
    for (var i = 0; i < 15; i++) { var b = h[i] & 255; s += (b < 16 ? '0' : '') + b.toString(16); }
    return 'paikallinen-' + s;
  }
  function addEntries(list) {
    list.forEach(function (e) {
      var id = idOf(e.path, e.size, e.time);
      if (LOCAL.files[id]) return;
      LOCAL.files[id] = { text: e.text, size: e.size };
      LOCAL.entries.push({ id: id, name: nameOf(e.path), time: e.time });
    });
    LOCAL.entries.sort(function (a, b) { return a.time - b.time; });
    var rows = [['Aikaleima', 'Sähköpostiosoite', 'Palauta vastaukset']].concat(LOCAL.entries.map(function (e) { return [e.time, e.name, 'https://drive.google.com/open?id=' + e.id]; }));
    var resp = ss.getSheetByName('Lomakevastaukset (paikallinen)') || ss.insertSheet('Lomakevastaukset (paikallinen)');
    resp.data = rows;
  }
  function readFiles(files) {
    var jobs = [].map.call(files, function (f) {
      return f.arrayBuffer().then(function (buf) {
        if (/\.zip$/i.test(f.name)) {
          return Promise.all(readZip(buf).filter(function (e) { return !/\/$/.test(e.name); }).map(function (e) {
            if (e.size > RL_LIMITS.file) return { path: e.name, size: e.size, time: e.time, text: '' };   // Code.gs merkitsee liian suureksi
            return inflate(e).then(function (t) { return { path: e.name, size: e.size, time: e.time, text: t }; }, function () { return { path: e.name, size: e.size, time: e.time, text: '' }; });
          }));
        }
        return [{ path: f.name, size: f.size, time: new Date(f.lastModified), text: f.size > RL_LIMITS.file ? '' : new TextDecoder('utf-8').decode(buf) }];
      });
    });
    return Promise.all(jobs).then(function (lists) { return [].concat.apply([], lists); });
  }

  /* ---- yläpalkki (opettaja 6.11.2026: "riittäisi se, että Tuo tiedosto"; ryhmä tunnistetaan tiedostosta) ---- */
  function el(tag, text) { var e = document.createElement(tag); if (text) e.textContent = text; return e; }
  function download(name, text, type) {
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type: type })); a.download = name;
    document.body.append(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
  }
  document.addEventListener('DOMContentLoaded', function () {
    RL_CONFIG.SUBMISSION_FOLDER_ID = 'local'; RL_CONFIG.IDENTITY = 'name';
    var bar = document.getElementById('localBar'); bar.hidden = false; bar.className = 'panel';
    var row1 = el('p'); row1.className = 'bar';
    var imp = el('button', 'Tuo tiedosto'); imp.type = 'button'; imp.id = 'import'; imp.className = 'primary';
    var undo = el('button', 'Peru viimeisin tuonti'); undo.type = 'button'; undo.id = 'undoImport'; undo.hidden = true;
    var pick = el('input'); pick.type = 'file'; pick.multiple = true; pick.accept = '.zip,.json,application/zip,application/json'; pick.id = 'pick'; pick.hidden = true;
    var gLab = el('label'), gSel = el('select'); gSel.id = 'group'; gLab.append(el('b', 'Ryhmä: '), gSel); gLab.id = 'groupWrap';
    row1.append(imp, undo, pick, gLab);
    var more = el('details'); more.id = 'more'; more.append(el('summary', 'Muut toiminnot'));
    var row = el('p'); row.className = 'bar';
    var csv = el('button', 'Vie pisteet (CSV)'), bak = el('button', 'Varmuuskopio'), res = el('button', 'Palauta varmuuskopio'), clr = el('button', 'Poista ryhmä');
    csv.id = 'csv'; bak.id = 'backup'; res.id = 'restore'; clr.id = 'clear';
    [csv, bak, res, clr].forEach(function (b) { b.type = 'button'; row.append(b); });
    more.append(row);
    var resFile = el('input'); resFile.type = 'file'; resFile.accept = '.json,application/json'; resFile.hidden = true;
    var msg = el('p'); msg.className = 'muted'; msg.id = 'localMsg'; msg.setAttribute('aria-live', 'polite');
    bar.append(row1, msg, more, resFile);
    var safe = function (g) { return g.replace(/[^0-9A-Za-zÅÄÖåäö._-]+/g, '_'); };
    function fillGroups() {
      var list = groups(); gSel.textContent = '';
      list.forEach(function (g) { var o = el('option', g); o.value = g; gSel.append(o); });
      gSel.value = LOCAL.group;
      gLab.hidden = list.length < 2; more.hidden = !LOCAL.group;
    }
    function choose(g) { return loadFiles(g).then(function () { useGroup(g); fillGroups(); window.rlReload(); }); }
    var hhmm = function (d) { return d.getHours() + '.' + pad(d.getMinutes()); };
    function showUndo() { return getUndo().then(function (u) { undo.hidden = !u; undo.title = u ? 'Tuonti klo ' + hhmm(new Date(u.time)) + ': ' + u.count + ' palautusta' : ''; }); }
    showUndo();
    var start = '';
    try { start = localStorage.getItem(chosenKey()) || ''; } catch (e) {}
    if (groups().indexOf(start) < 0) start = groups()[0] || '';
    choose(start);
    if (!start) msg.textContent = 'Lataa Drivesta ryhmän lomakkeen palautuskansio (zip) ja tuo se tähän: Tuo tiedosto.';
    gSel.addEventListener('change', function () { var g = gSel.value; choose(g).then(function () { msg.textContent = 'Ryhmä ' + g + '.' + (LOCAL.entries.length ? '' : ' Tuo ryhmän zip uudelleen, niin vastaukset näkyvät.'); }); });
    imp.addEventListener('click', function () { pick.click(); });
    pick.addEventListener('change', function () {
      if (!pick.files.length) return;
      msg.textContent = 'Luetaan…';
      readFiles(pick.files).then(function (list) {
        pick.value = '';
        // tiedostot ryhmittäin: zipin ylin kansio on lomake; irralliset JSON-tiedostot valittuun ryhmään
        var by = {}, order = [], notes = [];
        list.forEach(function (e) {
          var f = formOf(e.path), g = f ? groupFor(f) : LOCAL.group;
          if (!g) { if (notes.indexOf(f) < 0) notes.push(f || e.path); return; }
          if (!by[g]) { by[g] = { files: [], forms: [] }; order.push(g); }
          by[g].files.push(e); if (f && by[g].forms.indexOf(f) < 0) by[g].forms.push(f);
        });
        return Promise.all(order.map(loadFiles)).then(function () {
          var out = [], stores = [], snap = { time: Date.now(), groups: groups(), chosen: LOCAL.group, per: {}, count: 0 };
          order.forEach(function (g) {
            var c = courseOfGroup(g), st = savedOf(g);
            if (!COURSES[(st && st.course) || c]) { out.push('Ryhmä ' + g + ': kurssia ' + (c || '?') + ' ei ole tällä arviointisivulla, ei luettu.'); return; }
            var list2 = groups();
            if (list2.indexOf(g) < 0) { list2.push(g); if (!setGroups(list2)) { out.push('Selain ei salli tallentamista (localStorage).'); return; } }
            useGroup(g);
            var other = LOCAL.forms.length ? by[g].forms.filter(function (f) { return LOCAL.forms.indexOf(f) < 0; }) : [];
            if (other.length) { out.push('Zip on lomakkeelta "' + other[0] + '", mutta ryhmän ' + g + ' palautukset on luettu lomakkeelta "' + LOCAL.forms[0] + '". Mitään ei luettu.'); return; }
            var was = savedOf(g) ? localStorage.getItem(key(g)) : null, had = {};
            Object.keys(LOCAL.files).forEach(function (id) { had[id] = 1; });
            by[g].forms.forEach(function (f) { if (LOCAL.forms.indexOf(f) < 0) LOCAL.forms.push(f); });
            addEntries(by[g].files);
            var added = Object.keys(LOCAL.files).filter(function (id) { return !had[id]; });
            if (added.length) { snap.per[g] = { state: was, ids: added }; snap.count += added.length; }
            var r = rlImport_(); saveSheets();
            stores.push(storeFiles(g, LOCAL.files, LOCAL.entries).then(function () { return true; }, function () { return false; }));
            var k = r.counts;
            out.push('Ryhmä ' + g + ': luettu ' + by[g].files.length + ' tiedostoa. Uusia palautuksia ' + r.added + ' (hyväksyttyjä ' + k['Hyväksytty'] + ', kaksoiskappaleita ' + k['Kaksoiskappale'] + ', tarkistettavia ' + k['Tarkistettava'] + ', virheellisiä ' + k['Virheellinen'] + ').');
          });
          if (snap.count) stores.push(setUndo(snap).then(showUndo).then(function () { return true; }));
          notes.forEach(function (f) { out.push('Ryhmää ei tunnistettu: "' + f + '". Lomakkeen nimen pitää alkaa ryhmällä, esim. FY3.2 lv 2026-27 Palauta ratkaisut.'); });
          fillGroups(); window.rlReload();
          msg.textContent = out.join(' ');
          return Promise.all(stores).then(function (oks) {
            if (oks.indexOf(false) >= 0) msg.textContent += ' Selain ei salli palautusten tallentamista (IndexedDB): vastaukset näkyvät vain, kunnes sivu suljetaan.';
          });
        });
      }).catch(function (e) { pick.value = ''; msg.textContent = 'Tiedostoja ei voitu lukea: ' + (e && e.message || e); });
    });
    undo.addEventListener('click', function () {
      getUndo().then(function (u) {
        if (!u) { undo.hidden = true; return; }
        var gs = Object.keys(u.per);
        if (!window.confirm('Perutaanko tuonti klo ' + hhmm(new Date(u.time)) + '? Siinä tuodut ' + u.count + ' palautusta poistetaan, ja ryhmän ' + gs.join(', ') +
          ' arviointi palaa tuontia edeltävään tilaan. Tuonnin jälkeen annetut pisteet poistuvat.')) return;
        return Promise.all(gs.map(loadFiles)).then(function () {
          useGroup('');
          var jobs = gs.map(function (g) {
            var m = MEM[g] || { files: {}, entries: [] }, drop = {};
            u.per[g].ids.forEach(function (id) { drop[id] = 1; delete m.files[id]; });
            m.entries = m.entries.filter(function (e) { return !drop[e.id]; }); MEM[g] = m;
            try { if (u.per[g].state) localStorage.setItem(key(g), u.per[g].state); else localStorage.removeItem(key(g)); } catch (e) {}
            if (!m.entries.length) { delete MEM[g]; return dropFiles(g); }
            return storeFiles(g, m.files, m.entries).catch(function () {});
          });
          setGroups(u.groups);
          return Promise.all(jobs).then(function () { return setUndo(null); }).then(function () {
            var list = groups(), g = list.indexOf(u.chosen) >= 0 ? u.chosen : (list[0] || '');
            return choose(g).then(function () { undo.hidden = true; msg.textContent = 'Tuonti peruttu: ' + u.count + ' palautusta poistettu.' + (g ? '' : ' Tuo ryhmän zip-tiedosto.'); });
          });
        });
      });
    });
    csv.addEventListener('click', function () {
      var name = course() + '-' + safe(LOCAL.group) + '-pisteet.csv';
      download(name, rlScoresCsv(), 'text/csv;charset=utf-8'); msg.textContent = 'Pisteet viety tiedostoon ' + name + '. Avaa se Sheetsissä (Tiedosto → Tuo).';
    });
    bak.addEventListener('click', function () {
      if (!saveSheets()) { msg.textContent = 'Selain ei salli tallentamista (localStorage).'; return; }
      download(course() + '-' + safe(LOCAL.group) + '-arviointi-varmuuskopio.json', localStorage.getItem(key()) || '', 'application/json');
      msg.textContent = 'Varmuuskopio ladattu. Säilytä se koulun Drivessa, ei julkisesti.';
    });
    res.addEventListener('click', function () { resFile.click(); });
    resFile.addEventListener('change', function () {
      var f = resFile.files[0]; resFile.value = ''; if (!f) return;
      f.text().then(function (t) {
        var st;
        try { st = JSON.parse(t); } catch (e) { st = null; }
        if (st && st.group && st.group !== LOCAL.group && !window.confirm('Varmuuskopio on ryhmältä ' + st.group + '. Korvataanko ryhmän ' + LOCAL.group + ' arviointi sillä?')) return;
        var before = LOCAL.sheets, forms = LOCAL.forms;
        try { loadSheets(t); } catch (e) { LOCAL.sheets = before; LOCAL.forms = forms; msg.textContent = 'Tiedosto ei ole tämän kurssin arvioinnin varmuuskopio.'; return; }
        saveSheets(); setUndo(null).then(showUndo); msg.textContent = 'Varmuuskopio palautettu ryhmään ' + LOCAL.group + '.'; window.rlReload();
      }, function () { msg.textContent = 'Tiedostoa ei voitu lukea.'; });
    });
    clr.addEventListener('click', function () {
      if (!window.confirm('Poistetaanko ryhmä ' + LOCAL.group + ' sekä sen tuonnit ja pisteet tästä selaimesta? Ota ensin varmuuskopio.')) return;
      var g = LOCAL.group;
      try { localStorage.removeItem(key()); } catch (e) {}
      delete MEM[g]; LOCAL.group = ''; dropFiles(g); setUndo(null).then(showUndo);
      setGroups(groups().filter(function (x) { return x !== g; }));
      choose(groups()[0] || '');
      msg.textContent = 'Ryhmä ' + g + ' poistettu.';
    });
  });
})();
