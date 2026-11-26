/* Common-mistake recognition for a wrong number (work queue 17c PR 1, K5). One pure function, no page, no storage:
   window.flMistake(value, answer, tol, unit, step) -> 'sign' | 'magnitude' | 'time' | 'kelvin' | null.
   Called by lesson.js part 1 when the answer check says "no" (inquiry.js, a task's own `mistakes`, then overrides it).
   Every rule uses the check's tolerance: tol relative (the larger of 2 % and the task's own); the sign and kelvin rules also allow
   half of step, one unit of the answer's last shown digit; never when the answer is 0 or the value is 0. Order:
   1 sign (value ≈ −answer), 2 order of magnitude (value / answer ≈ 10^k, k = ±1…±9), 3 time and speed, only for a unit with time in it (ratio ≈ 3,6, 60,
   3600 or an inverse), 4 kelvin and celsius (|value − answer| ≈ 273,15, only when the unit is K or °C; tested right after the sign, before the ratios). Rules that need
   the task's formula (degrees and radians, a forgotten square or half) are not here (17c PR 2). */
(() => {
  const RATIOS = [3.6, 60, 3600];
  // the time rule only for a unit that has time in it (s, min, h, a, /s, ·s, W, kWh, Hz, A, Bq), so a force or a length is never told to check the unit of time
  const TIME_UNIT = /(?:^|[\/·*])(?:s|min|h|a|d)(?:$|[\/·*²³^⁻])|^[kMGm]?(?:W|Wh|Hz|A|Bq)$|Wh$/;
  window.flMistake = (value, answer, tol, unit, step) => {
    const v = Number(value), a = Number(answer);
    if (!Number.isFinite(v) || !Number.isFinite(a) || v === 0 || a === 0) return null;
    const rel = Math.max(0.02, Number(tol) || 0), half = (Number(step) || 0) / 2;
    const near = (x, target) => Math.abs(x - target) <= Math.max(rel * Math.abs(target), half) * (1 + 1e-9);   // the check's own width, scaled to the target
    const u = String(unit || '').replace(/[\s\u00a0\u2009]/g, '');
    if (near(v, -a)) return 'sign';
    if ((u === 'K' || u === '°C' || u === '℃') && Math.abs(Math.abs(v - a) - 273.15) <= Math.max(0.02 * 273.15, half)) return 'kelvin';
    const r = Math.abs(v / a);
    if (Math.sign(v) === Math.sign(a)) {
      for (let k = 1; k <= 9; k++) for (const s of [1, -1]) if (Math.abs(r / Math.pow(10, s * k) - 1) <= rel) return 'magnitude';
      if (TIME_UNIT.test(u)) for (const t of RATIOS) if (Math.abs(r / t - 1) <= rel || Math.abs(r * t - 1) <= rel) return 'time';
    }
    return null;
  };

  // A typed number (teacher 2026-11-10, FY6 fixes): a decimal comma or point, spaces between digit groups (10 000),
  // a power of ten as 9,99e17, 9,99 · 10^17, 9,99×10^{17}, 9,99*10^-19 or 3,73 × 10⁻¹⁹ (teacher 2026-11-10, FY8), an optional "x =" before it and a unit
  // after it (3 Ω, 2,5 m/s). Anything else that is not one number, such as 2/3 or 2,5,3, is NaN and never another number.
  window.flParse = (s) => {
    let t = String(s).trim().replace(/[\u00a0\u2009\u202f]/g, ' ').replace(/[−–]/g, '-');
    t = t.replace(/^[^\d+\-.,=≈]*[=≈]\s*/, '').replace(/(\d)\s+(?=\d)/g, '$1');
    t = t.replace(/10\s*([⁺⁻]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g, (m, e) => '10^' + [...e].map((c) => '⁺⁻⁰¹²³⁴⁵⁶⁷⁸⁹'.indexOf(c)).map((i) => '+-0123456789'[i]).join(''));   // 10⁻¹⁹
    const m = t.match(/^([+-]?)()\s*10\s*\^\s*()(\{\s*[+-]?\d+\s*\}|[+-]?\d+)(.*)$/)   // 10^-3
      || t.match(/^([+-]?)\s*(\d+(?:[.,]\d*)?|[.,]\d+)(?:\s*[eE]\s*([+-]?\d+)|\s*(?:[·⋅×xX*]|\\cdot|\\times)\s*10\s*\^\s*(\{\s*[+-]?\d+\s*\}|[+-]?\d+))?(.*)$/);
    if (!m) return NaN;
    const rest = m[5].trim();
    if (rest && /^[\d.,/:*·⋅×^+\-=⁺⁻⁰¹²³⁴⁵⁶⁷⁸⁹]/.test(rest)) return NaN;   // 2/3, 2,5,3, 3^2, 2⁵, 2-1: not one number
    const exp = m[3] !== undefined && m[3] !== '' ? Number(m[3]) : m[4] !== undefined ? Number(m[4].replace(/[{}\s]/g, '')) : 0;
    const mant = m[2] === '' ? 1 : Number(m[2].replace(',', '.'));
    return Number(`${m[1] === '-' ? '-' : ''}${mant}e${exp}`);
  };

  // The answer check of a typed number, one rule for the lesson page and the grading page (work queue 17e): the text as typed ->
  // null when it is not one number, else { value, state: 'ok' | 'close' | 'no', mistake } (mistake only for 'no', as flMistake).
  // Accepted: within 2 % of the model answer or half a unit in its shown last significant digit (step is one unit), whichever is larger,
  // or the task's own wider tolerance; 2-5 % away is 'close' (Lähellä), not a rejection (teacher 2026-11-03, 2026-11-10).
  window.flJudge = (text, answer, tol, unit, step) => {
    const v = window.flParse(text), ans = Number(answer), t = Number(tol), st = Number(step) || 0;
    if (!Number.isFinite(v) || !Number.isFinite(ans)) return null;
    const a = Math.abs(ans), round = st / 2;
    const accept = ans === 0 ? Math.max(t, round) : Math.max(0.02 * a, t * a, round);
    const near = ans === 0 ? 2.5 * accept : Math.max(0.05 * a, 1.25 * accept);
    const diff = Math.abs(v - ans);
    if (diff <= accept * (1 + 1e-9)) return { value: v, state: 'ok', mistake: null };
    if (diff <= near * (1 + 1e-9)) return { value: v, state: 'close', mistake: null };
    return { value: v, state: 'no', mistake: window.flMistake(v, ans, t, unit, st) };
  };
})();
