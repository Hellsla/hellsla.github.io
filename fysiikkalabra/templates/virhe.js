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
})();
