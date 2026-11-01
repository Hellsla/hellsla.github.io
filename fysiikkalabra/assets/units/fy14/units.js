/* FY14 Road to Fusion: the course's own interactive components (scripts/units.py). A unit's text places one as
   <div class="fx" data-fx="<kind>" id="..."><script type="application/json">{…data…}</script></div>; this file loads
   fx/<kind>.js once per kind (relative to this script, so it works from site/en/ and in a preview) and calls
   window.FX[kind](element, data, api). Everything stays in the browser: nothing is sent anywhere, and a student's
   answers are kept in localStorage only so that a reload does not lose them (every access wrapped; the page works
   without storage). Without JavaScript each component shows its fallback, which the data's "fallback" field or the
   component itself writes as plain text inside the element. Texts are English: the course is taught in English.
   Feedback always says right or wrong in words and with a sign, never by colour alone; controls are native
   (button, select, input), at least 40 px high and keyboard operable. */
(() => {
  const me = document.currentScript && document.currentScript.src;
  const base = me ? me.replace(/units\.js(\?.*)?$/, '') : 'units/fy14/';
  window.FX = window.FX || {};
  const page = location.pathname.split('/').pop();
  const store = {
    get(id) { try { return JSON.parse(localStorage.getItem('fx:' + page + ':' + id)); } catch (e) { return null; } },
    set(id, v) { try { localStorage.setItem('fx:' + page + ':' + id, JSON.stringify(v)); } catch (e) { /* storage blocked */ } },
  };
  const typeset = (el) => {
    if (window.renderMathInElement) window.renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
    if (window.flGlueMath) window.flGlueMath(el);
  };
  const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag);
    Object.entries(attrs || {}).forEach(([k, v]) => {
      if (v === false || v == null) return;
      if (k === 'html') el.innerHTML = v; else if (k === 'text') el.textContent = v;
      else if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : v);
    });
    kids.flat().forEach((c) => c != null && el.append(c.nodeType ? c : document.createTextNode(String(c))));
    return el;
  };
  // a seeded shuffle: the same order on every visit, different for every component (never a predictable pattern)
  const seeded = (seed) => { let s = 0; for (const c of String(seed)) s = (s * 31 + c.charCodeAt(0)) >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); };
  const shuffle = (arr, seed) => { const r = seeded(seed), a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  // a derangement-like shuffle for ordering tasks: never the right order to start with
  const scramble = (arr, seed) => { let a = shuffle(arr, seed), k = 0; while (arr.length > 1 && a.every((x, i) => x === arr[i]) && k < 9) a = shuffle(arr, seed + ++k); return a; };
  // French (or any) speech through the browser's own voices: no recording is downloaded, nothing is sent
  const speech = {
    ok: 'speechSynthesis' in window && typeof SpeechSynthesisUtterance === 'function',
    say(text, lang, rate) {
      if (!this.ok) return false;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text); u.lang = lang || 'fr-FR'; u.rate = rate || 0.9;
      const v = window.speechSynthesis.getVoices().find((x) => x.lang && x.lang.replace('_', '-').toLowerCase().startsWith((lang || 'fr-FR').slice(0, 2).toLowerCase()));
      if (v) u.voice = v;
      window.speechSynthesis.speak(u); return true;
    },
  };
  const md = (s) => String(s == null ? '' : s)   // the small markdown the data uses: **bold**, *italic*, `code`
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\[([^\]]+)\]\((https?:[^)\s]+|[\w./#-]+)\)/g, '<a href="$2">$1</a>')
    .replace(/\{fr\}(.+?)\{\/fr\}/g, '<span lang="fr">$1</span>');
  // a component's data file: the copy build.py embedded in the page (works offline and from a file), else fetched
  const data = (src) => {
    const own = [...document.querySelectorAll('script.fx-src')].find((s) => src && src.endsWith(s.dataset.for));
    if (own) { try { return Promise.resolve(JSON.parse(own.textContent)); } catch (e) { return Promise.reject(e); } }
    return fetch(src).then((r) => r.json());
  };
  const api = { base, store, typeset, h, shuffle, scramble, speech, md, data };
  window.FXAPI = api;

  const loaded = {};
  const load = (kind) => loaded[kind] || (loaded[kind] = new Promise((res, rej) => {
    if (window.FX[kind]) { res(); return; }
    const s = document.createElement('script'); s.src = base + 'fx/' + kind + '.js'; s.onload = res; s.onerror = rej; document.head.append(s);
  }));
  const start = (el) => {
    const kind = el.dataset.fx; let data = {};
    const js = el.querySelector(':scope > script[type="application/json"]');
    try { data = js ? JSON.parse(js.textContent) : {}; } catch (e) { console.warn('fx data', el.id, e); return; }
    load(kind).then(() => {
      el.querySelectorAll(':scope > .fx-fallback').forEach((n) => n.remove());
      window.FX[kind](el, data, api); el.classList.add('fx-ready'); typeset(el);
    }).catch((e) => console.warn('fx component', kind, e));
  };
  const all = () => document.querySelectorAll('.fx[data-fx]:not(.fx-ready)').forEach(start);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all); else all();
})();
