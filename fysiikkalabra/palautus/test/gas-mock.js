/* Minimal stand-ins for the Apps Script services Code.gs uses, so Code.gs, Tehtavat.gs and Review.html can be tested
   in a browser (scripts/test_palautus.py). Only what Code.gs calls is here. Sheets semantics that matter for safety are
   kept: a string written with a leading "'" is stored as plain text without it, and a string that starts with "="
   would become a formula (recorded in MOCK.formulas, which the test requires to stay empty). */
(function () {
  var MOCK = window.MOCK = { formulas: [], alerts: [], files: {}, failOnce: {}, locked: false, sheets: [], writes: 0 };

  function Range(sh, r, c, nr, nc) { this.sh = sh; this.r = r; this.c = c; this.nr = nr || 1; this.nc = nc || 1; }
  Range.prototype.getValues = function () {
    var out = [];
    for (var i = 0; i < this.nr; i++) { var row = this.sh.data[this.r - 1 + i] || []; var o = []; for (var j = 0; j < this.nc; j++) { var v = row[this.c - 1 + j]; o.push(v === undefined ? '' : v); } out.push(o); }
    return out;
  };
  Range.prototype.setValues = function (vals) {
    if (vals.length !== this.nr || vals.some(function (r) { return r.length !== this.nc; }, this)) throw new Error('setValues: size mismatch');
    MOCK.writes++;
    for (var i = 0; i < this.nr; i++) {
      var row = this.sh.data[this.r - 1 + i] || (this.sh.data[this.r - 1 + i] = []);
      for (var j = 0; j < this.nc; j++) {
        var v = vals[i][j];
        if (typeof v === 'string' && v.charAt(0) === "'") v = v.slice(1);
        else if (typeof v === 'string' && /^[=+@]/.test(v)) MOCK.formulas.push(v);
        else if (typeof v === 'string' && /^-/.test(v) && !/^-?\d/.test(v)) MOCK.formulas.push(v);
        row[this.c - 1 + j] = v;
      }
    }
    for (var k = 0; k < this.sh.data.length; k++) if (!this.sh.data[k]) this.sh.data[k] = [];
    return this;
  };
  Range.prototype.setValue = function (v) { return this.setValues([[v]]); };
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
    getSheetByName: function (n) { return MOCK.sheets.filter(function (s) { return s.name === n; })[0] || null; },
    insertSheet: function (n) { var s = new Sheet(n, []); MOCK.sheets.push(s); return s; },
    getSheets: function () { return MOCK.sheets.slice(); }
  };
  MOCK.addSheet = function (name, rows) { var s = new Sheet(name, rows); MOCK.sheets.push(s); return s; };
  MOCK.sheet = function (name) { return ss.getSheetByName(name); };
  var dv = function () { var b = {}; ['requireValueInList', 'setAllowInvalid'].forEach(function (m) { b[m] = function () { return b; }; }); b.build = function () { return {}; }; return b; };
  window.SpreadsheetApp = {
    getActiveSpreadsheet: function () { return ss; }, flush: function () {}, newDataValidation: dv,
    getUi: function () { return { alert: function (t, m) { MOCK.alerts.push([t, m]); }, ButtonSet: { OK: 1 },
      createMenu: function () { var m = { addItem: function () { return m; }, addToUi: function () {} }; return m; }, showModalDialog: function () {} }; }
  };
  window.HtmlService = { createHtmlOutputFromFile: function () { var h = { setWidth: function () { return h; }, setHeight: function () { return h; } }; return h; } };
  window.LockService = { getDocumentLock: function () { return { tryLock: function () { return !MOCK.locked; }, releaseLock: function () {} }; } };

  // Drive: folders by id with a parent; files { id: { text, size?, parent } }
  MOCK.folders = { 'kansio-palautukset': { parent: 'kansio-lomake' }, 'kansio-lomake': { parent: 'root' }, 'muu-kansio': { parent: 'root' }, root: { parent: null } };
  var folder = function (id) {
    return { getId: function () { return id; }, getParents: function () { var p = MOCK.folders[id] && MOCK.folders[id].parent; return iter(p ? [folder(p)] : []); } };
  };
  var iter = function (a) { var i = 0; return { hasNext: function () { return i < a.length; }, next: function () { return a[i++]; } }; };
  window.DriveApp = {
    getFileById: function (id) {
      if (MOCK.failOnce[id]) { delete MOCK.failOnce[id]; throw new Error('Drive unavailable'); }
      var f = MOCK.files[id];
      if (!f) throw new Error('No item with the given ID could be found');
      return { getId: function () { return id; }, getSize: function () { return f.size !== undefined ? f.size : new TextEncoder().encode(f.text).length; },
               getParents: function () { return iter([folder(f.parent || 'kansio-palautukset')]); },
               getBlob: function () { return { getDataAsString: function () { return f.text; } }; } };
    }
  };

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
      if (fmt === 'H.mm.ss') return Number(p.hour) + '.' + pad(Number(p.minute)) + '.' + pad(Number(p.second));
      throw new Error('formatDate mock: ' + fmt);
    }
  };

  // the state as JSON (dates kept), to carry the sheets and files from the import test into the grading view's page
  MOCK.dump = function () {
    return JSON.stringify({ sheets: MOCK.sheets.map(function (s) { return { name: s.name, data: s.data }; }), files: MOCK.files, formulas: MOCK.formulas }, function (k, v) {
      return typeof v === 'string' && /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z$/.test(v) && this[k] instanceof Date ? { __date: v } : v;
    });
  };
  MOCK.load = function (text) {
    var st = JSON.parse(text, function (k, v) { return v && typeof v === 'object' && v.__date ? new Date(v.__date) : v; });
    MOCK.sheets = st.sheets.map(function (s) { return new Sheet(s.name, s.data); }); MOCK.files = st.files; MOCK.formulas = st.formulas;
  };

  // google.script.run for Review.html: calls the global server function after MOCK.delay ms, with JSON round trips
  // (as Apps Script serializes), and fails a call while MOCK.fail[name] > 0.
  MOCK.delay = {}; MOCK.fail = {}; MOCK.calls = [];
  var runner = function (ok, no) {
    return new Proxy({}, { get: function (_, name) {
      if (name === 'withSuccessHandler') return function (f) { return runner(f, no); };
      if (name === 'withFailureHandler') return function (f) { return runner(ok, f); };
      return function (arg) {
        var a = arg === undefined ? undefined : JSON.parse(JSON.stringify(arg));
        MOCK.calls.push([name, a]);
        setTimeout(function () {
          if (MOCK.fail[name] > 0) { MOCK.fail[name]--; if (no) no(new Error('Palvelin ei vastannut (testi)')); return; }
          var r;
          try { r = window[name](a); } catch (e) { if (no) no(new Error(e.message)); return; }
          if (ok) ok(r === undefined ? null : JSON.parse(JSON.stringify(r)));
        }, MOCK.delay[name] || 5);
      };
    } });
  };
  window.google = { script: { get run() { return runner(null, null); } } };
})();
