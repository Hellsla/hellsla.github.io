// A tiny assertion helper for the model tests (scripts/test_models.py): one line per failure, a count at the end.
let n = 0; const bad = [];
function check(name, ok) { n++; if (!ok) bad.push(name); }
function near(name, got, want, tol) { n++; if (!(Math.abs(got - want) <= tol * Math.max(1, Math.abs(want)))) bad.push(`${name}: got ${got}, expected ${want} ± ${tol}`); }
function done() {
  for (const b of bad) console.log('FAIL ' + b);
  console.log(bad.length ? `${bad.length} of ${n} checks failed` : `ok   ${n} checks`);
  process.exitCode = bad.length ? 1 : 0;
}
module.exports = { check, near, done };
