/* Read aloud (teacher 2026-11-03, "ääneenluku"): a Kuuntele button under the page title reads the page aloud with the
   browser's own voice (speechSynthesis; nothing is downloaded or sent, the text is never stored). Every page built from
   templates/lesson.html has it: lessons, Sovella itsenäisesti, investigations, TVT guides and course units, in every
   language (lang/<lang>.json "js" ra_* for the controls, "speech" for how a formula is spoken).
   - What is read: the visible text of <main> in reading order, block by block (headings, paragraphs, list items, table
     cells, captions, feedback). A closed box, a hidden step of a worked example, a figure, a simulation and the buttons
     are not read, so nothing is given away before the student acts; the next block is looked up only when it is
     reached, so a box opened while listening is read when the reading gets there.
   - Formulas: KaTeX keeps the TeX of each formula (annotation), and texSpeech() turns it into words: $F = m \cdot a$
     is "F on m kertaa a", $9{,}81\,\text{m/s}^2$ "9,81 metriä per sekunti toiseen". A long displayed calculation is
     announced as "kaava" (speech.words.formula) instead of being spelled out.
   - Where the reading is (teacher 2026-11-03): the block being read is tinted and scrolled into view, the sentence is
     highlighted (CSS Custom Highlight API, so the page is not changed) and, where the voice reports word boundaries,
     the word too. A browser without the Highlight API shows the block only.
   - What a lesson reads (teacher 2026-11-03, the progress bar brief): on a lesson page only Pohdinta and
     Teoriatiivistelmä; no task, hint, model answer or solution, even inside those stages. Other pages read <main>.
   - A formula may carry its own spoken form: data-speech="sigma F on yhtä kuin m kertaa a" on the formula or an
     element around it is read instead of the formula (texSpeech is used where there is none).
   - Controls (teacher 2026-11-03): one Kuuntele / Tauko button (text and icon, aria-pressed) at the right end of the
     stage bar (nav.toc), and beside it a menu for the speed (0,8 · 1 · 1,25, remembered on this device) and, for the
     neural voice, Nainen / Mies. The button is shown only when a voice for the page's language is there. Esc stops.
     Pause is cancel-and-restart of the sentence: the browsers' own pause/resume is unreliable on Android. A click on
     a stage in the bar moves the reading there (to the next stage that is read, paused, when that one is not), a
     click on a paragraph while reading reads from there, and the stage being read is marked in the bar (event
     fl:reading to lesson.js).
   - Start: from the top, or, when the page has been scrolled, from the first block that is read below the bar. */
(() => {
  const synth = window.speechSynthesis && typeof SpeechSynthesisUtterance === 'function' ? window.speechSynthesis : null;
  const SCRIPT = document.currentScript;
  const canNeural = typeof Worker === 'function' && typeof WebAssembly === 'object' && !!(window.AudioContext || window.webkitAudioContext)
    && typeof Blob === 'function' && window.flTtsEngine !== 'browser';
  if (!synth && !canNeural) return;
  const main = document.querySelector('main');
  if (!main) return;
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent); } catch (e) { return {}; } })();
  const msg = (k) => { const s = (L10N.js || {})[k]; return typeof s === 'string' ? s : k; };
  const S = L10N.speech || {};
  const W = S.words || {};
  const pageLang = (document.documentElement.lang || 'fi').toLowerCase();

  /* ---------- formula to words ---------- */
  const GREEK_ALIAS = { varepsilon: 'epsilon', vartheta: 'theta', varphi: 'phi', varrho: 'rho', varsigma: 'sigma', varpi: 'pi' };
  const NOUNIT = { cur: 0 };
  function unitWords(raw) {
    const units = S.units || {}, pre = S.prefixes || {};
    let s = raw.replace(/\\[,;: ]|~/g, ' ').replace(/\\cdot|\\times|[·⋅]/g, '·').replace(/\\mu|μ/g, 'µ').replace(/\\Omega/g, 'Ω')
      .replace(/\\%/g, '%').replace(/\^\s*\\circ|\\circ|\\degree/g, '°').replace(/\\text\s*\{([^}]*)\}|\\mathrm\s*\{([^}]*)\}/g, '$1$2')
      .replace(/\^\s*\{\s*(-?\d)\s*\}|\^\s*(-?\d)/g, '^$1$2').replace(/[{}()]/g, '').trim();
    if (!s || /[^A-Za-zµΩ°%^\-\d·/ ]/.test(s)) return null;
    const look = (name) => {
      if (units[name]) return { u: units[name], base: name };
      for (const p of Object.keys(pre).sort((a, b) => b.length - a.length)) {
        if (name.startsWith(p) && units[name.slice(p.length)] && name.length > p.length) {
          const u = units[name.slice(p.length)];
          return { u: [pre[p] + u[0], pre[p] + u[1]], base: name.slice(p.length) };
        }
      }
      return null;
    };
    const num = [], den = [];
    const parts = s.split('/');
    for (let k = 0; k < parts.length; k++) {
      const toks = parts[k].split(/[·\s]+/).filter(Boolean);
      if (!toks.length && k === 0) continue;
      if (!toks.length) return null;
      for (const t of toks) {
        const m = t.match(/^([^\^]+)(?:\^(-?\d))?$/);
        if (!m) return null;
        if (/^\d+$/.test(m[1]) && k === 0 && toks.length === 1 && parts.length > 1 && m[1] === '1') continue;   // 1/s
        const r = look(m[1]);
        if (!r) return null;
        let e = m[2] ? Number(m[2]) : 1, into = k === 0 ? num : den;
        if (e < 0) { e = -e; into = k === 0 ? den : num; }
        into.push({ r, e, name: m[1] });
      }
    }
    if (!num.length && !den.length) return null;
    const pow = (x, form) => {
      const w = x.r.u[form];
      if (x.e === 1) return w;
      if (x.r.base === 'm' && x.e === 2 && W.area) return W.area + w;
      if (x.r.base === 'm' && x.e === 3 && W.volume) return W.volume + w;
      return w + ' ' + (x.e === 2 ? W.squared : x.e === 3 ? W.cubed : (W.power + ' ' + x.e));
    };
    const out = [];
    if (num.length) out.push(num.map((x, i) => pow(x, i === num.length - 1 ? 1 : 0)).join(S.joiner == null ? ' ' : S.joiner));
    den.forEach((x) => {
      const per = (S.per_unit || {})[x.name];
      out.push(per && x.e === 1 && den.length === 1 ? per : W.per + ' ' + pow(x, 0));
    });
    return out.join(' ');
  }

  function texSpeech(tex) {
    const toks = [];
    const re = /\\([a-zA-Z]+)\s*|\\(.)|(\d+(?:\{[,.]\}\d+|[.,]\d+)*)|([a-zA-Z])|(\s+)|([^\s])/g;
    let m;
    while ((m = re.exec(tex))) {
      if (m[5]) continue;
      toks.push(m[1] ? { t: 'cmd', v: m[1], p: m.index, e: re.lastIndex } : m[2] ? { t: 'sym', v: m[2], p: m.index, e: re.lastIndex }
        : m[3] ? { t: 'num', v: m[3], p: m.index, e: re.lastIndex } : m[4] ? { t: 'let', v: m[4], p: m.index, e: re.lastIndex }
        : { t: 'ch', v: m[6], p: m.index, e: re.lastIndex });
    }
    let i = 0;
    const peek = () => toks[i];
    const isCh = (t, v) => t && t.t === 'ch' && t.v === v;
    function rawGroup() {          // the TeX inside the next {...}, unparsed
      if (!isCh(peek(), '{')) { const t = toks[i++]; return t ? tex.slice(t.p, t.e) : ''; }
      const open = toks[i]; let depth = 0, j = i;
      for (; j < toks.length; j++) { if (isCh(toks[j], '{')) depth++; else if (isCh(toks[j], '}') && --depth === 0) break; }
      const close = toks[j] || { p: tex.length };
      i = j + 1;
      return tex.slice(open.e, close.p);
    }
    function arg() {
      const start = peek();
      if (!start) return { w: '', raw: '' };
      if (isCh(start, '{')) { const s0 = i; i++; const w = seq(true); return { w, raw: tex.slice(toks[s0].e, (toks[i - 1] || { p: tex.length }).p) }; }
      const a = atom(); return { w: a.w, raw: tex.slice(start.p, (toks[i - 1] || start).e) };
    }
    function textAtom(name) {
      let raw = rawGroup();
      if (NOUNIT.cur === 0) {
        if (peek() && isCh(peek(), '^')) {        // \text{m/s}^2: the power belongs to the last unit
          const save = i; i++; const e = arg();
          if (/^-?\d$/.test(e.raw.trim())) raw += '^' + e.raw.trim(); else i = save;
        }
        const u = unitWords(raw);
        if (u != null) return { w: u, unit: raw.replace(/[{}\s\\]/g, '') };
      }
      return { w: raw.replace(/\\[,;: ]|~/g, ' ').replace(/[{}\\]/g, '').trim() };
    }
    function atom() {
      const t = toks[i++];
      if (!t) return { w: '' };
      if (t.t === 'num') return { w: t.v.replace(/\{([,.])\}/g, '$1') };
      if (t.t === 'let') return { w: t.v };
      if (t.t === 'sym') {
        if (t.v === '%') return { w: W.percent };
        if (t.v === '\\') return { w: '' };
        return { w: '' };
      }
      if (t.t === 'ch') {
        switch (t.v) {
          case '{': return { w: seq(true) };
          case '=': return { w: W.equals };
          case '+': return { w: W.plus };
          case '-': case '−': return { w: W.minus };
          case '·': case '×': case '⋅': return { w: W.times };
          case '/': return { w: W.per };
          case ':': return { w: W.divided };
          case '<': return { w: W.lt };
          case '>': return { w: W.gt };
          case '≈': return { w: W.approx };
          case '°': return { w: '°' };
          case ',': case '.': return { w: t.v };
          case '%': return { w: W.percent };
          default: return { w: '' };
        }
      }
      const c = t.v;
      if (c === 'frac' || c === 'dfrac' || c === 'tfrac') {
        const a = arg(), b = arg();
        if (NOUNIT.cur === 0 && /\\(text|mathrm)/.test(a.raw) && /\\(text|mathrm)/.test(b.raw)) {   // \frac{\text{J}}{\text{kg}\cdot{}^\circ\text{C}}: a unit
          const u = unitWords('(' + a.raw + ')/(' + b.raw + ')');
          if (u != null) return { w: u };
        }
        return { w: a.w + ' ' + W.over + ' ' + b.w };
      }
      if (c === 'sqrt') { if (isCh(peek(), '[')) { while (peek() && !isCh(peek(), ']')) i++; i++; } return { w: W.sqrt + ' ' + arg().w }; }
      if (/^(text|textrm|textit|textbf|textsf|mathrm|mathit|mathsf|mathbf|operatorname|mbox|textnormal)$/.test(c)) return textAtom(c);
      if (c === 'overline' || c === 'vec' || c === 'overrightarrow') return { w: W.vector + ' ' + arg().w };
      if (/^(bar|hat|dot|ddot|tilde|boldsymbol|bm|mathbb|mathcal|cancel|underline|bigl|bigr|Bigl|Bigr|mathring)$/.test(c)) {
        if (/^(bigl|bigr|Bigl|Bigr)$/.test(c)) return { w: '' };
        return { w: arg().w };
      }
      if (c === 'textcolor' || c === 'color') { rawGroup(); return c === 'color' ? { w: '' } : { w: arg().w }; }
      if (c === 'begin' || c === 'end') { rawGroup(); return { w: '' }; }
      if (c === 'phantom' || c === 'label' || c === 'tag') { rawGroup(); return { w: '' }; }
      const g = (S.greek || {})[GREEK_ALIAS[c] || c] || (S.greek || {})[(GREEK_ALIAS[c] || c).toLowerCase()];
      if (g) return { w: g };
      const fn = (S.functions || {})[c];
      if (fn) return { w: fn };
      const map = { cdot: 'times', times: 'times', div: 'divided', approx: 'approx', neq: 'neq', ne: 'neq', leq: 'le', le: 'le',
        geq: 'ge', ge: 'ge', lt: 'lt', gt: 'gt', pm: 'pm', mp: 'pm', to: 'to', rightarrow: 'to', longrightarrow: 'to',
        Rightarrow: 'so', Longrightarrow: 'so', implies: 'so', propto: 'propto', infty: 'infinity', sum: 'sum', int: 'integral',
        equiv: 'equals', sim: 'approx', simeq: 'approx', cong: 'approx', ll: 'lt', gg: 'gt', parallel: 'parallel', perp: 'perp' };
      if (map[c]) return { w: W[map[c]] || '' };
      if (c === 'circ' || c === 'degree') return { w: '°' };
      return { w: '' };    // spacing, \left, \right, \displaystyle, \quad ...
    }
    function postfix(a) {
      for (;;) {
        const t = peek();
        if (isCh(t, '^')) {
          i++;
          const e = arg(), r = e.raw.replace(/\s+/g, '');
          if (r === '\\circ' || r === '\\degree' || r === '°') a = { w: a.w + ' °' };
          else if (r === '2') a = { w: a.w + ' ' + W.squared };
          else if (r === '3') a = { w: a.w + ' ' + W.cubed };
          else a = { w: a.w + ' ' + W.power + ' ' + e.w };
        } else if (isCh(t, '_')) {
          i++; NOUNIT.cur++; const s = arg(); NOUNIT.cur--;
          a = { w: a.w + ' ' + s.w };
        } else if (isCh(t, "'")) { i++; } else return a;
      }
    }
    function seq(inGroup) {
      const out = [];
      while (i < toks.length) {
        if (isCh(peek(), '}')) { i++; if (inGroup) break; continue; }
        if (isCh(peek(), '&') || (peek().t === 'sym' && peek().v === '\\')) { i++; continue; }
        const a = postfix(atom());
        const last = out[out.length - 1];
        if (last && /°$/.test(last) && a.unit === 'C') { out[out.length - 1] = last.replace(/\s*°$/, '') + ' ' + W.celsius; continue; }
        if (a.w) out.push(a.w);
      }
      return out.join(' ');
    }
    let s = seq(false);
    s = s.replace(/(^|\s)°(?=\s|$)/g, '$1' + (W.degrees || '')).replace(/\s*°/g, ' ' + (W.degrees || ''));
    s = s.replace(/(\d)\s*([,.])\s*(\d)/g, '$1$2$3').replace(/(\d)\s+(?=\d{3}(?!\d))/g, '$1').replace(/\s+([,.])/g, '$1');
    return s.replace(/\s+/g, ' ').trim();
  }

  /* ---------- the text of the page ---------- */
  const BLOCK = 'h1,h2,h3,h4,h5,p,li,dt,dd,figcaption,caption,th,td,label,legend,output,.katex-display';
  const SKIP = 'svg,script,style,noscript,template,button,input,select,textarea,summary,nav,.ra-ui,#sim-root,.sim-wrap,.toc,.sr-only,.visually-hidden,[aria-hidden="true"]';
  const isBlock = (el) => el.nodeType === 1 && el.matches(BLOCK);
  const SCOPE = main.querySelector('section.stage#herata, section.stage#selita') ? '#herata, #selita' : null;
  const NOT_READ = '.activity:not(.act-hook):not(.act-theory), details.opt, details.answer, details.hint, .hints, .feedback, .sol-step, .example, form, fieldset, .photo-credit';
  function readable(el) {
    if (SCOPE && (!el.closest(SCOPE) || el.closest(NOT_READ))) return false;
    if (el.closest(SKIP) && !el.matches('.katex-display')) return false;
    if (el.matches('.katex-display') && el.parentElement && el.parentElement.closest(SKIP)) return false;
    for (let d = el.closest('details:not([open])'); d; d = d.parentElement && d.parentElement.closest('details:not([open])')) {
      const sum = d.querySelector(':scope > summary');
      if (!sum || !sum.contains(el)) return false;    // inside a closed box (newer browsers still lay its content out)
    }
    if (el.checkVisibility && !el.checkVisibility({ visibilityProperty: true, contentVisibilityAuto: false })) return false;
    return el.getClientRects().length > 0;
  }
  function mathText(k) {
    const ann = k.querySelector('annotation[encoding="application/x-tex"]');
    if (!ann) return '';
    const tex = ann.textContent;
    if (k.closest('.katex-display') && (tex.length > 140 || /\\begin/.test(tex))) return W.formula || '';
    try { return texSpeech(tex); } catch (e) { return W.formula || ''; }
  }
  function blockText(el) {        // the words of a block, and which part of the page each stretch comes from
    let text = ''; const segs = [];
    const walk = (node) => {
      for (const ch of node.childNodes) {
        if (ch.nodeType === 3) { if (ch.data) { segs.push({ a: text.length, b: text.length + ch.data.length, node: ch }); text += ch.data.replace(/\s/g, ' '); } continue; }
        if (ch.nodeType !== 1) continue;
        if (ch.hasAttribute('data-speech')) {
          const w = ch.getAttribute('data-speech').trim();
          if (w) { text += ' '; segs.push({ a: text.length, b: text.length + w.length, el: ch }); text += w + ' '; }
          continue;
        }
        if (ch.classList.contains('katex')) {
          const w = mathText(ch);
          if (w) { text += ' '; segs.push({ a: text.length, b: text.length + w.length, el: ch }); text += w + ' '; }
          continue;
        }
        if (isBlock(ch) || ch.matches(SKIP)) continue;
        if (ch.tagName === 'BR') { text += ' '; continue; }
        const cs = getComputedStyle(ch), apart = cs.display !== 'inline' || getComputedStyle(ch, '::before').content !== 'none';
        if (apart) text += ' ';            // a word in a box of its own, or after a CSS "(", is never glued to the one before
        walk(ch);
        if (apart) text += ' ';
      }
    };
    if (el.matches('.katex-display')) {
      const ds = el.closest('[data-speech]') || el.querySelector('[data-speech]'), k = el.querySelector('.katex');
      if (ds) { const w = ds.getAttribute('data-speech').trim(); segs.push({ a: 0, b: w.length, el: k || el }); text = w; }
      else if (k) { const w = mathText(k); segs.push({ a: 0, b: w.length, el: k }); text = w; }
    }
    else walk(el);
    return { text, segs };
  }
  function sentences(text) {      // [start, end) of each sentence, long ones cut at a comma
    const out = []; const re = /[.!?…]+["”’)]*\s+(?=[A-ZÅÄÖÜ0-9"“(])/g; let a = 0, m;
    const push = (x, y) => {
      while (y - x > 200) { const cut = text.lastIndexOf(', ', x + 180); const c = cut > x + 40 ? cut + 2 : x + 180; out.push([x, c]); x = c; }   // Chrome's Google voices stop after about 15 s
      if (text.slice(x, y).trim()) out.push([x, y]);
    };
    while ((m = re.exec(text))) { push(a, m.index + m[0].length); a = m.index + m[0].length; }
    push(a, text.length);
    return out;
  }
  function candidates() { return Array.from(main.querySelectorAll(BLOCK)); }
  function nextBlock(after, dir) {
    const all = candidates();
    let k = after ? all.indexOf(after) : -1;
    if (after && k < 0) {         // the block left the page: continue from where it was in the document
      k = all.findIndex((el) => after.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) - 1;
      if (k < -1) k = all.length;
    }
    for (k += dir; k >= 0 && k < all.length; k += dir) {
      const el = all[k];
      if (!readable(el)) continue;
      const bt = blockText(el);
      if (bt.text.replace(/[\s.,:;!?–—-]/g, '')) return { el, ...bt, sents: sentences(bt.text) };
    }
    return null;
  }

  /* ---------- voices ---------- */
  let voices = [];
  const loadVoices = () => { voices = (synth && synth.getVoices()) || []; };
  loadVoices();
  if (synth && synth.addEventListener) synth.addEventListener('voiceschanged', loadVoices);
  /* the best voice first (2026-11-03: Chrome's old system voices sound poor): Edge's neural voices, Chrome's Google
     voices and the enhanced voices of macOS/iOS before the old desktop voices and eSpeak */
  function voiceScore(v, want) {
    const n = v.name || '', l = (v.lang || '').toLowerCase().replace('_', '-');
    return (/natural|neural|online/i.test(n) ? 8 : /^google/i.test(n) ? 7 : /premium|enhanced|siri/i.test(n) ? 6 : 0)
      - (/desktop|espeak|compact|eloquence/i.test(n) ? 4 : 0) + (l === want ? 1 : 0) + (v.default ? 0.5 : 0);
  }
  function voiceFor(lang) {
    const want = lang.toLowerCase().replace('_', '-'), base = want.slice(0, 2);
    const ok = voices.filter((v) => (v.lang || '').toLowerCase().replace('_', '-').slice(0, 2) === base);
    if (!ok.length) return null;
    return ok.slice().sort((x, y) => voiceScore(y, want) - voiceScore(x, want))[0];
  }
  const LANG_TAG = { fi: 'fi-FI', en: 'en-GB', fr: 'fr-FR', sv: 'sv-SE', de: 'de-DE' };

  /* ---------- the neural voice (teacher 2026-11-03: Supertonic 3, "Nainen" and "Mies", the best quality) ----------
     Supertonic 3 (OpenRAIL-M) runs in a worker with onnxruntime-web: WebGPU where the browser has it and it gives
     sound, otherwise WebAssembly on the CPU. Both live outside this site's repository (teacher 2026-11-04, UI fix 3)
     in Hellsla/ruukkilabra-models, served by GitHub Pages at MODEL_BASE (same origin as the site). The model (about
     145 MB) is kept in the browser's Cache Storage, so it is downloaded once per device. A sentence is synthesised
     while the one before it plays. If the model cannot be loaded, the device's own voice reads instead.
     When it is used (teacher 2026-11-04, UI fix 1): on a phone-sized window (max-width 700px), with Save-Data on or
     without WebGPU the device's own voice is the default, and the neural voice is only a choice in the menu
     (lang js.ra_better, "Parempi ääni (lataa 145 MB kerran)"); nothing is fetched before it is chosen. Elsewhere it
     is on by default and fetched on the first Kuuntele. The choice is remembered on this device (fl-ra-neural). */
  function ttsWorker() {
    let ort = null, S = null, idx = null, ttl = null, dp = null, cfg = null, queue = Promise.resolve();
    const post = (m, t) => self.postMessage(m, t || []);
    const REPL = { '–': '-', '‑': '-', '—': '-', '¯': ' ', '_': ' ', '“': '"', '”': '"', '‘': "'", '’': "'",
      '´': "'", '`': "'", '[': ' ', ']': ' ', '|': ' ', '/': ' ', '#': ' ', '→': ' ', '←': ' ' };
    function prep(text, lang) {            // the text normalisation of Supertonic's own pipeline (supertonic/core.py)
      let t = text.normalize('NFKD');
      for (const k in REPL) t = t.split(k).join(REPL[k]);
      t = t.replace(/[⁠­​]/g, '').replace(/[♥☆♡©\\]/g, '');
      t = t.replace(/ ([,.!?;:'])/g, '$1').replace(/(["'`])\1+/g, '$1').replace(/\s+/g, ' ').trim();
      if (!/[.!?;:,'"')\]}…]$/.test(t)) t += '.';
      t = '<' + lang + '>' + t + '</' + lang + '>';
      const out = [];
      for (const ch of t) { const c = ch.codePointAt(0); const v = c < idx.length ? idx[c] : -1; if (v >= 0) out.push(v); }
      return out;
    }
    function randn(n) {
      const a = new Float32Array(n);
      for (let i = 0; i < n; i += 2) {
        const u = 1 - Math.random(), v = Math.random(), r = Math.sqrt(-2 * Math.log(u));
        a[i] = r * Math.cos(2 * Math.PI * v); if (i + 1 < n) a[i + 1] = r * Math.sin(2 * Math.PI * v);
      }
      return a;
    }
    async function fetchFile(url, cache, step) {
      if (cache) { try { const hit = await cache.match(url); if (hit) { const b = await hit.arrayBuffer(); step(b.byteLength); return b; } } catch (e) { /* no cache */ } }
      const r = await fetch(url);
      if (!r.ok) throw new Error('HTTP ' + r.status + ' ' + url);
      let buf;
      if (r.body && r.body.getReader) {
        const reader = r.body.getReader(), parts = []; let n = 0;
        for (;;) { const { done, value } = await reader.read(); if (done) break; parts.push(value); n += value.length; step(value.length); }
        buf = new Uint8Array(n); let o = 0; for (const p of parts) { buf.set(p, o); o += p.length; }
      } else { buf = new Uint8Array(await r.arrayBuffer()); step(buf.length); }
      if (cache) { try { await cache.put(url, new Response(buf.slice())); } catch (e) { /* storage full: next time it is fetched again */ } }
      return buf.buffer;
    }
    async function sessions(bufs, eps) {
      const out = {};
      for (const m of ['duration_predictor', 'text_encoder', 'vector_estimator', 'vocoder'])
        out[m] = await ort.InferenceSession.create(new Uint8Array(bufs[m + '.onnx']), { executionProviders: eps, graphOptimizationLevel: 'all' });
      return out;
    }
    async function synth(text, lang, voice, speed, steps) {
      const T = ort.Tensor, ids = prep(text, lang), n = ids.length;
      const SR = cfg.ae.sample_rate, CS = cfg.ae.base_chunk_size * cfg.ttl.chunk_compress_factor, C = cfg.ttl.latent_dim * cfg.ttl.chunk_compress_factor;
      const tid = new T('int64', BigInt64Array.from(ids, (v) => BigInt(v)), [1, n]);
      const tmask = new T('float32', new Float32Array(n).fill(1), [1, 1, n]);
      const st = new T('float32', ttl.slice(voice * 12800, (voice + 1) * 12800), [1, 50, 256]);
      const sd = new T('float32', dp.slice(voice * 128, (voice + 1) * 128), [1, 8, 16]);
      const first = (o) => o[Object.keys(o)[0]];
      const dur = first(await S.duration_predictor.run({ text_ids: tid, style_dp: sd, text_mask: tmask })).data[0] / speed;
      const emb = first(await S.text_encoder.run({ text_ids: tid, style_ttl: st, text_mask: tmask }));
      const wl = Math.max(1, Math.floor(dur * SR)), L = Math.max(1, Math.ceil(wl / CS));
      let x = new T('float32', randn(C * L), [1, C, L]);
      const lm = new T('float32', new Float32Array(L).fill(1), [1, 1, L]), tot = new T('float32', new Float32Array([steps]), [1]);
      for (let k = 0; k < steps; k++) {
        x = first(await S.vector_estimator.run({ noisy_latent: x, text_emb: emb, style_ttl: st, text_mask: tmask, latent_mask: lm,
          current_step: new T('float32', new Float32Array([k]), [1]), total_step: tot }));
      }
      const wav = first(await S.vocoder.run({ latent: x })).data;
      const pcm = Float32Array.from(wav.subarray(0, Math.min(wl, wav.length)));
      for (let i = 0, f = Math.min(441, pcm.length); i < f; i++) { pcm[i] *= i / f; pcm[pcm.length - 1 - i] *= i / f; }   // no click at the ends
      return { pcm, sr: SR };
    }
    const sound = (pcm) => { let m = 0; for (let i = 0; i < pcm.length; i += 7) { const v = Math.abs(pcm[i]); if (!(v === v) || v === Infinity) return false; if (v > m) m = v; } return m > 0.01; };
    async function init(d) {
      self.importScripts(d.base + 'ort/ort.webgpu.min.js');
      ort = self.ort;
      ort.env.wasm.wasmPaths = d.base + 'ort/';
      ort.env.wasm.numThreads = 1;               // GitHub Pages is not cross-origin isolated: no threads
      ort.env.logLevel = 'error';
      let cache = null; try { cache = await caches.open('fl-tts-supertonic3-v1'); } catch (e) { /* no Cache Storage */ }
      // copies cached from the site's old vendor/ folder (before 2026-11-04) are dropped: the model now comes from MODEL_BASE
      if (cache) { try { for (const k of await cache.keys()) if (!k.url.startsWith(d.model)) await cache.delete(k); } catch (e) { /* keep */ } }
      const manifest = JSON.parse(new TextDecoder().decode(await fetchFile(d.model + 'manifest.json', null, () => {})));
      const total = Object.values(manifest.files).reduce((a, b) => a + b, 0); let loaded = 0, last = 0;
      const step = (n) => { loaded += n; const now = Date.now(); if (now - last > 250 || loaded >= total) { last = now; post({ type: 'progress', loaded, total }); } };
      const bufs = {};
      for (const f of Object.keys(manifest.files)) bufs[f] = await fetchFile(d.model + f, cache, step);
      cfg = JSON.parse(new TextDecoder().decode(bufs['tts.json']));
      idx = new Int32Array(bufs['unicode_indexer.bin']);
      const vb = bufs['voice.bin'], h = new Int32Array(vb, 0, 12), nv = h[0];
      ttl = new Float32Array(vb, 48, nv * h[2] * h[4]); dp = new Float32Array(vb, 48 + nv * h[2] * h[4] * 4, nv * h[8] * h[10]);
      let ep = 'wasm';
      if (d.gpu && self.navigator && self.navigator.gpu) {
        try {
          const adapter = await self.navigator.gpu.requestAdapter();
          if (adapter) {
            S = await sessions(bufs, ['webgpu']);
            const t = await synth('Testi.', 'fi', 0, 1.05, 2);
            if (sound(t.pcm)) ep = 'webgpu'; else S = null;
          }
        } catch (e) { S = null; }
      }
      if (!S) S = await sessions(bufs, ['wasm']);
      post({ type: 'ready', ep });
    }
    self.onmessage = (e) => {
      const d = e.data;
      if (d.type === 'init') init(d).catch((err) => post({ type: 'error', message: String((err && err.message) || err) }));
      else if (d.type === 'synth') {
        queue = queue.then(async () => {
          if (d.stale && d.stale < self.__keep) return post({ type: 'error', id: d.id, message: 'skipped' });
          try { const r = await synth(d.text, d.lang, d.voice, d.speed, d.steps); post({ type: 'audio', id: d.id, pcm: r.pcm, sr: r.sr }, [r.pcm.buffer]); }
          catch (err) { post({ type: 'error', id: d.id, message: String((err && err.message) || err) }); }
        });
      } else if (d.type === 'keep') self.__keep = d.from;
    };
  }
  const NEURAL_LANGS = ['ar', 'bg', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fi', 'fr', 'hi', 'hr', 'hu', 'id', 'it', 'ja', 'ko', 'lt', 'lv', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sv', 'tr', 'uk', 'vi'];
  const VOICE_ID = { female: 0, male: 5 };       // voice.bin holds F1..F5, then M1..M5
  const VOICE_LANG = { fi: { female: 1, male: 8 } };   // teacher 2026-11-03: Finnish F2 and M4; English F1 and M1
  const voiceId = (l2) => { const o = VOICE_LANG[l2]; return o && o[voiceChoice] != null ? o[voiceChoice] : VOICE_ID[voiceChoice]; };
  const MODEL_BASE = new URL(typeof window.flTtsModelBase === 'string' ? window.flTtsModelBase : 'https://hellsla.github.io/ruukkilabra-models/', location.href).href;
  const lightDevice = !!((navigator.connection && navigator.connection.saveData)
    || (window.matchMedia && window.matchMedia('(max-width:700px)').matches) || !navigator.gpu);
  let wantNeural = canNeural && !lightDevice;
  try { const v = localStorage.getItem('fl-ra-neural'); if (canNeural && (v === '1' || v === '0')) wantNeural = v === '1'; } catch (e) { /* no storage */ }
  const neuralOn = () => neural.ok && wantNeural && !neural.failed;
  const neural = {
    ok: canNeural, failed: false, ready: null, ep: null, pool: [], ctx: null, src: null, cache: new Map(), seq: 0, progress: 0, queue: [], keepFrom: 0,
    spawn(primary) {                          // one worker: loads the model (from Cache Storage after the first time)
      const w = { worker: null, jobs: new Map(), busy: 0 };
      w.ready = new Promise((res, rej) => {
        try {
          const url = URL.createObjectURL(new Blob(['(' + ttsWorker.toString() + ')()'], { type: 'text/javascript' }));
          w.worker = new Worker(url);
        } catch (e) { rej(e); return; }
        w.worker.onmessage = (e) => {
          const d = e.data;
          if (d.type === 'progress') { if (primary) { this.progress = d.loaded / d.total; loadNote(); } }
          else if (d.type === 'ready') res(d.ep);
          else if (d.id) { const j = w.jobs.get(d.id); if (j) { w.jobs.delete(d.id); w.busy--; if (d.type === 'audio') j.res(d); else j.rej(new Error(d.message)); this.pump(); } }
          else if (d.type === 'error') rej(new Error(d.message));
        };
        w.worker.onerror = (e) => rej(new Error(e.message || 'worker'));
        w.worker.postMessage({ type: 'init', base: MODEL_BASE, model: MODEL_BASE + 'supertonic3-v1/', gpu: primary && window.flTtsGpu !== false });
      });
      return w;
    },
    start() {                                 // in a click: an AudioContext may start only in a user gesture
      if (!this.ctx) { const AC = window.AudioContext || window.webkitAudioContext; this.ctx = new AC(); }
      if (this.ctx.state === 'suspended') this.ctx.resume();
      if (this.ready) return this.ready;
      const first = this.spawn(true);
      this.ready = first.ready.then((ep) => {
        this.ep = ep; this.pool.push(first);
        // On the CPU one worker is slower than speech on many laptops: a second worker synthesises the next sentence
        // at the same time (each worker is single-threaded, as GitHub Pages cannot enable threads).
        if (ep === 'wasm' && (navigator.hardwareConcurrency || 2) >= 4 && window.flTtsWorkers !== 1) {
          const second = this.spawn(false);
          second.ready.then(() => { this.pool.push(second); this.pump(); }, () => {});
        }
        return ep;
      });
      this.ready.catch(() => { this.failed = true; });
      return this.ready;
    },
    synth(text, lang, voice, speed) {
      const key = [text, lang, voice, speed].join('|');
      if (this.cache.has(key)) return this.cache.get(key);
      const id = ++this.seq;
      const p = this.ready.then(() => new Promise((res, rej) => {
        this.queue.push({ id, res, rej, msg: { type: 'synth', id, stale: id, text, lang, voice, speed, steps: this.ep === 'webgpu' ? 8 : 6 } });
        this.pump();
      }));
      this.cache.set(key, p);
      if (this.cache.size > 12) this.cache.delete(this.cache.keys().next().value);
      p.catch(() => this.cache.delete(key));
      return p;
    },
    // Sentences wait here and go to a worker only when it is free, so a worker that becomes ready later takes the next
    // one at once. Fewer than 6 steps (8 on the GPU) and the voice's timbre drifts audibly from sentence to sentence.
    pump() {
      for (const w of this.pool) {
        while (!w.busy && this.queue.length) {
          const j = this.queue.shift();
          if (j.id < this.keepFrom) { j.rej(new Error('skipped')); continue; }
          w.jobs.set(j.id, j); w.busy++; w.worker.postMessage(j.msg);
        }
      }
    },
    keep() {                                  // drop sentences that were skipped
      this.keepFrom = this.seq + 1;
      this.queue.splice(0).forEach((j) => j.rej(new Error('skipped')));
      this.pool.forEach((w) => w.worker.postMessage({ type: 'keep', from: this.keepFrom }));
    },
    play(d, onend) {
      this.stopAudio();
      const buf = this.ctx.createBuffer(1, d.pcm.length, d.sr);
      buf.getChannelData(0).set(d.pcm);
      const s = this.ctx.createBufferSource(); s.buffer = buf; s.connect(this.ctx.destination);
      s.onended = () => { if (this.src === s) { this.src = null; onend(); } };
      this.src = s; s.start();
    },
    stopAudio() { if (this.src) { const s = this.src; this.src = null; try { s.stop(); } catch (e) { /* already stopped */ } } },
  };
  function loadNote() {
    if (neural.ep || neural.failed || (!cur && !wantNeural)) return;
    showNote(msg('ra_loading').replace('{{p}}', String(Math.round(neural.progress * 100))));
  }
  let voiceChoice = 'female';
  try { const v = localStorage.getItem('fl-ra-voice'); if (VOICE_ID[v] != null) voiceChoice = v; } catch (e) { /* no storage */ }

  /* ---------- state ---------- */
  let cur = null, si = 0, playing = false, token = 0, utter = null;
  const RATES = [0.8, 1, 1.25];
  let rate = Number(S.rate) || 1;
  try { const r = Number(localStorage.getItem('fl-ra-rate')); if (RATES.includes(r)) rate = r; } catch (e) { /* no storage */ }
  const hl = typeof CSS !== 'undefined' && CSS.highlights && typeof Highlight === 'function';

  function domPoint(pos, end) {
    const segs = cur.segs;
    let s = segs.find((g) => pos >= g.a && pos <= g.b && (end ? pos > g.a : pos < g.b));
    if (!s) s = end ? [...segs].reverse().find((g) => g.b <= pos) : segs.find((g) => g.a >= pos);
    if (!s) return null;
    if (s.el) return { el: s.el, before: !end };
    return { node: s.node, off: Math.max(0, Math.min(s.node.data.length, pos - s.a)) };
  }
  function rangeOf(a, b) {
    if (!cur || !cur.segs.length) return null;
    const p = domPoint(a, false), q = domPoint(b, true);
    if (!p || !q) return null;
    const r = document.createRange();
    try {
      if (p.el) r.setStartBefore(p.el.closest('.katex-display') || p.el); else r.setStart(p.node, p.off);
      if (q.el) r.setEndAfter(q.el.closest('.katex-display') || q.el); else r.setEnd(q.node, q.off);
    } catch (e) { return null; }
    return r.collapsed ? null : r;
  }
  function paint(word) {
    if (!hl) return;
    CSS.highlights.delete('ra-word');
    if (!cur) { CSS.highlights.delete('ra-sentence'); return; }
    const [a, b] = cur.sents[si] || [0, 0];
    if (!word) {
      let x = a, y = b; while (x < y && cur.text[x] === ' ') x++; while (y > x && cur.text[y - 1] === ' ') y--;
      const r = rangeOf(x, y); if (r) CSS.highlights.set('ra-sentence', new Highlight(r)); else CSS.highlights.delete('ra-sentence');
    } else {
      const r = rangeOf(word[0], word[1]); if (r) CSS.highlights.set('ra-word', new Highlight(r));
    }
  }
  const toc = document.querySelector('nav.toc');
  let told = null;
  function tellStage(el) {                         // lesson.js marks the stage being read in the bar
    const id = el && window.flStageOf ? window.flStageOf(el) : null;
    if (id === told) return;
    told = id; document.dispatchEvent(new CustomEvent('fl:reading', { detail: { id } }));
  }
  function mark(el, noScroll) {
    document.querySelectorAll('.ra-on').forEach((x) => x.classList.remove('ra-on'));
    if (!el) return;
    el.classList.add('ra-on');
    if (playing) tellStage(el);
    if (noScroll) return;
    const r = el.getBoundingClientRect();
    const bottom = window.innerHeight - 16, top = (toc && getComputedStyle(toc).position === 'sticky' ? toc.getBoundingClientRect().bottom : 0) + 8;
    if (r.top < top || r.bottom > bottom) {
      const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      el.scrollIntoView({ block: r.height > bottom - top ? 'start' : 'center', behavior: reduce ? 'auto' : 'smooth' });
    }
  }

  const langOf = (el) => { const host = el.closest('[lang]'); return ((host && host.getAttribute('lang')) || pageLang).toLowerCase(); };
  const neuralSpeed = () => Math.min(2, Math.max(0.7, 1.05 * rate));
  const useNeural = (lang) => neuralOn() && NEURAL_LANGS.includes(lang.slice(0, 2));
  // The neural voice reads up to three short sentences of one block at a time (at most 280 characters, as Supertonic's
  // own reader joins text): fewer joins, so the voice changes less often. A fresh start reads one sentence, to begin soon.
  function chunkEnd(blk, k, fresh) {
    let j = k + 1;
    if (!fresh) while (j < blk.sents.length && j - k < 3 && blk.sents[j][1] - blk.sents[k][0] <= 280) j++;
    return j;
  }
  function peekNext(count, end) {                 // the chunks after this one, to synthesise while this one plays
    const out = []; if (!cur) return out;
    let blk = cur, k = end;
    while (out.length < count) {
      if (k >= blk.sents.length) { blk = nextBlock(blk.el, 1); k = 0; if (!blk) break; }
      const j = chunkEnd(blk, k, false);
      out.push({ text: blk.text.slice(blk.sents[k][0], blk.sents[j - 1][1]), el: blk.el }); k = j;
    }
    return out;
  }
  function speakSentence(chained) {
    if (!cur) return finish();
    if (si >= cur.sents.length) { const n = nextBlock(cur.el, 1); if (!n) return finish(); cur = n; si = 0; mark(cur.el); }
    if (si < 0) { const n = nextBlock(cur.el, -1); if (!n) { si = 0; } else { cur = n; si = n.sents.length - 1; mark(cur.el); } }
    const [a, b] = cur.sents[si];
    const text = cur.text.slice(a, b);
    const my = ++token;
    const lang = langOf(cur.el);
    paint(null);
    if (useNeural(lang)) {
      const j = chunkEnd(cur, si, !chained), marks = [], a0 = cur.sents[si][0], all = cur.sents[j - 1][1] - a0;
      for (let k = si + 1; k < j; k++) marks.push([k, (cur.sents[k][0] - a0) / all]);   // where each sentence starts, as a share of the chunk
      return speakNeural(cur.text.slice(a0, cur.sents[j - 1][1]), lang.slice(0, 2), my, j, marks);
    }
    if (!synth) { si++; return speakSentence(); }
    speakBrowser(text, lang, a, my);
  }
  function speakNeural(text, l2, my, end, marks) {
    neural.start();
    loadNote();
    const job = neural.synth(text, l2, voiceId(l2), neuralSpeed());
    // the next sentences queue up behind this one, so a free worker starts them while this one is still being made
    peekNext(3, end).forEach((n) => { if (useNeural(langOf(n.el))) neural.synth(n.text, langOf(n.el).slice(0, 2), voiceId(langOf(n.el).slice(0, 2)), neuralSpeed()).catch(() => {}); });
    job.then((d) => {
      if (my !== token || !playing) return;
      if (!ui.note.dataset.keep) showNote(null);
      neural.play(d, () => { if (my !== token || !playing) return; si = end; speakSentence(true); });
      const len = d.pcm.length / d.sr * 1000;
      marks.forEach(([k, at]) => setTimeout(() => { if (my === token && playing) { si = k; paint(null); } }, at * len));
    }, (err) => {
      if (my !== token) return;
      if (neural.failed) {                         // the model did not load: the device's own voice reads on
        ui.voiceRow.hidden = true; ui.better.hidden = true;
        if (!haveVoice()) { stop(); offer(); showNote(msg('ra_no_lang_voice')); return; }
        showNote(msg('ra_fallback')); ui.note.dataset.keep = '1';
        if (playing) speakSentence();
      } else if (playing && String(err && err.message) !== 'skipped') { si = end; speakSentence(true); }
    });
  }
  function speakBrowser(text, lang, a, my) {
    const u = new SpeechSynthesisUtterance(text);
    u.lang = LANG_TAG[lang.slice(0, 2)] || lang;
    u.rate = rate;
    const v = voiceFor(u.lang);
    if (v) u.voice = v;
    u.onboundary = (e) => {
      if (my !== token || e.name && e.name !== 'word') return;
      const at = a + e.charIndex;
      let len = e.charLength;
      if (!len) { const m = cur.text.slice(at).match(/^\S+/); len = m ? m[0].length : 0; }
      if (len) paint([at, at + len]);
    };
    u.onend = () => { if (my !== token || !playing) return; si++; speakSentence(); };
    u.onerror = (e) => {
      if (my !== token) return;
      if (e.error === 'interrupted' || e.error === 'canceled') { playing = false; render(); return; }   // another voice on the page took over
      if (e.error === 'not-allowed') { playing = false; render(); return; }
      si++; speakSentence();
    };
    utter = u;
    synth.speak(u);
    if (synth.paused) synth.resume();
  }
  function hush() { token++; if (synth) synth.cancel(); neural.stopAudio(); neural.keep(); }
  function play() {
    if (!cur) {
      if (window.scrollY > 300) {                   // scrolled: from the first block that is read below the bar
        const all = candidates(), line = (toc ? toc.getBoundingClientRect().bottom : 0) + 4;
        const vis = all.find((el) => el.getBoundingClientRect().top >= line && readable(el));
        if (vis) { const k = all.indexOf(vis); cur = nextBlock(k > 0 ? all[k - 1] : null, 1); }
      }
      if (!cur) cur = nextBlock(null, 1);
      if (!cur) return;
      // no voice of the page's language on the device and the better voice not chosen: the menu offers it
      if (!neuralOn() && !voiceFor(LANG_TAG[pageLang.slice(0, 2)] || pageLang)) { cur = null; openMenu(true); showNote(msg('ra_no_lang_voice')); return; }
      si = 0;
    }
    if (neuralOn()) neural.start();
    playing = true; render(); mark(cur.el);
    hush(); speakSentence();
  }
  function pause() { playing = false; hush(); render(); tellStage(null); }
  function stop() {
    playing = false; hush(); cur = null; si = 0; mark(null); paint(null); showNote(null); render(); tellStage(null);
  }
  function finish() { stop(); }
  // a click on a stage in the bar moves the reading there; a stage that is not read moves it to the next one, paused
  function jumpTo(t) {
    if (!cur || !t) return;
    const all = candidates();
    const k = all.findIndex((el) => t.contains(el) || (t.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING));
    if (k < 0) { stop(); return; }
    const n = nextBlock(k > 0 ? all[k - 1] : null, 1);
    if (!n) { stop(); return; }
    hush(); cur = n; si = 0;
    if (!t.contains(n.el)) { playing = false; render(); tellStage(null); mark(cur.el, true); return; }
    mark(cur.el, true);
    if (playing) { tellStage(cur.el); speakSentence(); } else paint(null);
  }

  /* ---------- controls ---------- */
  const ICON = {
    speaker: '<path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    pause: '<path d="M7 5h4v14H7zM13 5h4v14h-4z" fill="currentColor"/>',
    more: '<path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
  };
  const svg = (k) => `<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false">${ICON[k]}</svg>`;
  const ui = {};
  ui.bar = document.createElement('div'); ui.bar.className = 'ra-ui ' + (toc ? 'toc-tools' : 'ra-bar'); ui.bar.hidden = true;
  ui.start = document.createElement('button'); ui.start.type = 'button'; ui.start.className = 'ra-start';
  ui.start.innerHTML = svg('speaker') + `<span>${msg('ra_listen')}</span>`;
  ui.start.setAttribute('aria-pressed', 'false'); ui.start.setAttribute('aria-label', msg('ra_listen'));
  ui.more = document.createElement('button'); ui.more.type = 'button'; ui.more.className = 'ra-more';
  ui.more.innerHTML = svg('more'); ui.more.setAttribute('aria-label', msg('ra_settings')); ui.more.title = msg('ra_settings');
  ui.more.setAttribute('aria-expanded', 'false'); ui.more.setAttribute('aria-controls', 'ra-menu');
  ui.bar.append(ui.start, ui.more);
  // the menu and the note float under the bar (the bar scrolls sideways on a phone, so they cannot live inside it)
  ui.menu = document.createElement('div'); ui.menu.className = 'ra-ui ra-menu'; ui.menu.id = 'ra-menu'; ui.menu.hidden = true;
  ui.menu.setAttribute('role', 'group'); ui.menu.setAttribute('aria-label', msg('ra_settings'));
  const speeds = document.createElement('fieldset'); speeds.className = 'ra-speeds';
  speeds.innerHTML = `<legend>${msg('ra_speed')}</legend>`;
  const dec = (L10N.format || {}).decimal || ',';
  ui.rates = RATES.map((r) => {
    const l = document.createElement('label'), i = document.createElement('input');
    i.type = 'radio'; i.name = 'ra-rate'; i.value = String(r); i.checked = Math.abs(r - rate) < 0.01;
    l.append(i, document.createTextNode(' ' + String(r).replace('.', dec) + '×'));
    speeds.append(l);
    i.addEventListener('change', () => {
      rate = r;
      try { localStorage.setItem('fl-ra-rate', String(rate)); } catch (e) { /* no storage */ }
      if (playing) { hush(); speakSentence(); }
    });
    return i;
  });
  if (!ui.rates.some((i) => i.checked)) { ui.rates[1].checked = true; rate = 1; }
  ui.better = document.createElement('label'); ui.better.className = 'ra-better'; ui.better.hidden = !canNeural;
  ui.betterBox = document.createElement('input'); ui.betterBox.type = 'checkbox'; ui.betterBox.checked = wantNeural;
  ui.better.append(ui.betterBox, document.createTextNode(' ' + msg('ra_better')));
  ui.betterBox.addEventListener('change', () => {   // a click: the download (and the AudioContext) may start here
    wantNeural = ui.betterBox.checked;
    try { localStorage.setItem('fl-ra-neural', wantNeural ? '1' : '0'); } catch (e) { /* no storage */ }
    ui.voiceRow.hidden = !neuralOn();
    if (neuralOn()) {
      loadNote();
      neural.start().then(() => { if (!playing) showNote(null); }, () => { ui.voiceRow.hidden = true; ui.better.hidden = true; showNote(msg('ra_fallback')); offer(); });
    }
    else if (!neural.failed) showNote(null);
    offer();
    if (playing) { hush(); speakSentence(); }
  });
  ui.voiceRow = document.createElement('label'); ui.voiceRow.className = 'ra-voice'; ui.voiceRow.hidden = !(canNeural && wantNeural);
  ui.voice = document.createElement('select');
  [['female', 'ra_female'], ['male', 'ra_male']].forEach(([v, k]) => { const o = document.createElement('option'); o.value = v; o.textContent = msg(k); ui.voice.append(o); });
  ui.voice.value = voiceChoice;
  ui.voiceRow.append(document.createTextNode(msg('ra_voice') + ' '), ui.voice);
  ui.voice.addEventListener('change', () => {
    voiceChoice = ui.voice.value;
    try { localStorage.setItem('fl-ra-voice', voiceChoice); } catch (e) { /* no storage */ }
    if (playing) { hush(); speakSentence(); }
  });
  ui.menu.append(speeds, ui.better, ui.voiceRow);
  ui.note = document.createElement('p'); ui.note.className = 'ra-ui ra-note'; ui.note.hidden = true; ui.note.setAttribute('role', 'status');
  function place(box) {                             // under the bar, right edge at the button's
    const r = ui.bar.getBoundingClientRect();
    box.style.top = Math.max(8, r.bottom + 6) + 'px';
    box.style.right = Math.max(8, document.documentElement.clientWidth - r.right) + 'px';
  }
  function openMenu(on) {
    ui.menu.hidden = !on; ui.more.setAttribute('aria-expanded', String(on));
    if (on) { place(ui.menu); (ui.rates.find((i) => i.checked) || ui.rates[0]).focus(); }
  }
  function showNote(t) { ui.note.textContent = t || ''; ui.note.hidden = !t; if (t) place(ui.note); }
  ui.note.addEventListener('click', () => { ui.note.hidden = true; });
  ui.more.addEventListener('click', () => openMenu(ui.menu.hidden));
  document.addEventListener('click', (e) => { if (!ui.menu.hidden && !ui.menu.contains(e.target) && !ui.more.contains(e.target)) openMenu(false); });
  window.addEventListener('scroll', () => { if (!ui.menu.hidden) place(ui.menu); if (!ui.note.hidden) place(ui.note); }, { passive: true });
  window.addEventListener('resize', () => { if (!ui.menu.hidden) place(ui.menu); if (!ui.note.hidden) place(ui.note); });

  function render() {
    ui.start.setAttribute('aria-pressed', String(playing));
    ui.start.setAttribute('aria-label', playing ? msg('ra_pause') : msg('ra_listen')); ui.start.title = ui.start.getAttribute('aria-label');
    ui.start.querySelector('span').textContent = playing ? msg('ra_pause') : msg('ra_listen');
    ui.start.querySelector('svg').outerHTML = svg(playing ? 'pause' : 'speaker');
  }
  // the button only where there is a voice for the page's language: the neural voice, or one of the device's
  function haveVoice() {
    // the neural voice can be chosen in the menu (on a phone it is not on by default), so it counts while it works
    if (neural.ok && !neural.failed && NEURAL_LANGS.includes(pageLang.slice(0, 2))) return true;
    return !!voiceFor(LANG_TAG[pageLang.slice(0, 2)] || pageLang);
  }
  function offer() { const ok = haveVoice(); ui.bar.hidden = !ok; if (!ok && cur) stop(); }
  ui.start.addEventListener('click', () => (playing ? pause() : play()));
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || e.defaultPrevented || document.querySelector('dialog[open]')) return;
    if (!ui.menu.hidden) { openMenu(false); ui.more.focus(); return; }
    if (cur) stop();
  });
  if (toc) toc.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a || !cur) return;
    const t = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    setTimeout(() => jumpTo(t), 0);                // after the browser has followed the link
  });
  main.addEventListener('click', (e) => {          // read from the clicked paragraph while reading
    if (!cur || e.defaultPrevented || e.target.closest('a,button,input,select,textarea,label,summary,details>summary,[contenteditable],.ra-ui,svg,#sim-root')) return;
    const sel = window.getSelection && window.getSelection(); if (sel && !sel.isCollapsed) return;
    const el = e.target.closest(BLOCK);
    if (!el || !readable(el)) return;
    const all = candidates(), k = all.indexOf(el);
    const n = nextBlock(k > 0 ? all[k - 1] : null, 1);
    if (!n) return;
    if (neuralOn()) neural.start();
    hush(); cur = n; si = 0; playing = true; render(); mark(cur.el); speakSentence();
  });
  window.addEventListener('pagehide', () => { if (synth) synth.cancel(); neural.stopAudio(); });
  if (synth) synth.cancel();                       // a voice left over from the previous page

  if (toc) toc.append(ui.bar);
  else { const h1 = main.querySelector('h1'); if (h1) h1.insertAdjacentElement('afterend', ui.bar); else main.prepend(ui.bar); }
  document.body.append(ui.menu, ui.note);
  offer();
  if (synth && synth.addEventListener) synth.addEventListener('voiceschanged', offer);
  window.flSpeech = { tex: texSpeech, unit: unitWords, blocks: () => { const out = []; let b = nextBlock(null, 1); while (b && out.length < 2000) { out.push(b.text.replace(/\s+/g, ' ').trim()); b = nextBlock(b.el, 1); } return out; },
    state: () => ({ engine: neuralOn() ? 'neural' : 'browser', light: lightDevice, modelBase: MODEL_BASE, ep: neural.ep, workers: neural.pool.length, failed: neural.failed, playing, voice: voiceChoice, progress: neural.progress, rate }),
    elements: () => { const out = []; let b = nextBlock(null, 1); while (b && out.length < 2000) { out.push(b.el); b = nextBlock(b.el, 1); } return out; } };
})();
