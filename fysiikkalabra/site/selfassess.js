/* Self-assessment (teacher's brief 2026-10-28, scripts/practice.py, NOTES.md §9). One component for every course:
   1. The rubric of a Sovella itsenäisesti task (.rubric): the student picks the points each criterion earns (partial
      credit allowed); the total is shown as self-assessed points, never as a grade. A competency scored at most half
      shows its links to the chapters where it is practised (the task's `links`, written into the page by build.py).
   (The chapter-level "Arvioi osaamistasi", Osaan / Tarvitsen vielä harjoitusta, was removed by the teacher on
   2026-10-28: a written answer is self-assessed against its model answer's criteria in inquiry.js instead.)
   2. A multiple-choice task of an Esimerkkikoe (.mc, scripts/practice.py render_exam): when its solution is opened the
      page marks each answer right or wrong and shows the points; no self-assessment after auto-graded choices.
   3. The exam's total (.exam-total): per section the points of its best `data-choose` tasks (self-assessed rubric
      points, or the page's multiple-choice points once checked), so the total never exceeds the exam's maximum.
   Selections are kept in this browser only (localStorage, as inquiry.js keeps predictions); nothing is sent. The page
   works without storage and without this script: the criteria and choices are plain radio buttons. */
(() => {
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent); } catch (e) { return {}; } })();
  const msg = (k, v) => { const s = (L10N.js || {})[k]; return typeof s === 'string' ? s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m)) : k; };
  const key = (id) => 'fl:' + location.pathname.split('/').pop() + ':' + id;
  const store = { get(id) { try { return JSON.parse(localStorage.getItem(key(id))) || {}; } catch (e) { return {}; } },
                  set(id, v) { try { localStorage.setItem(key(id), JSON.stringify(v)); } catch (e) { /* private mode, blocked storage */ } } };
  const restore = (groups, saved) => groups.forEach((g, i) => {
    if (saved[i] == null) return;
    const input = g.querySelector(`input[value="${saved[i]}"]`); if (input) input.checked = true;
  });

  // 1. rubric: points per criterion, the self-assessed total, links for a weak competency
  document.querySelectorAll('.rubric').forEach((rubric) => {
    const crits = [...rubric.querySelectorAll('fieldset.crit')], total = rubric.querySelector('.rubric-total'), more = rubric.querySelector('.rubric-more');
    const max = Number(rubric.dataset.max);
    const update = (save) => {
      let got = 0, left = 0; const state = {}, weak = new Set();
      crits.forEach((c, i) => {
        const sel = c.querySelector('input:checked');
        if (!sel) { left += 1; return; }
        const v = Number(sel.value); got += v; state[i] = v;
        if (2 * v <= Number(c.dataset.max)) weak.add(c.dataset.tag);
      });
      if (save) store.set(rubric.dataset.id, state);
      total.textContent = left ? msg('rubric_partial', { got, max, left }) : msg('rubric_total', { got, max });
      if (!more) return;
      let any = false;
      more.querySelectorAll('li[data-tag]').forEach((li) => { li.hidden = !weak.has(li.dataset.tag); any = any || !li.hidden; });
      more.hidden = !any;
    };
    restore(crits, store.get(rubric.dataset.id));
    rubric.addEventListener('change', () => update(true));
    update(false);
  });
  // 2. multiple choice of an exam: scored when the solution is opened
  const mcScore = (task) => {
    let got = 0;
    task.querySelectorAll('.mc').forEach((g) => { const sel = g.querySelector('input:checked'); if (sel && sel.value === g.dataset.correct) got += Number(g.dataset.points); });
    return got;
  };
  document.querySelectorAll('.mc').forEach((g) => {
    const saved = store.get(g.dataset.id).v;
    if (saved != null) { const i = g.querySelector(`input[value="${saved}"]`); if (i) i.checked = true; }
    g.addEventListener('change', () => { const sel = g.querySelector('input:checked'); store.set(g.dataset.id, { v: sel ? sel.value : null }); });
  });
  document.querySelectorAll('.mc-score').forEach((line) => {
    const task = line.closest('.task-card'), details = line.closest('details');
    const show = () => {
      if (!details.open) return;
      task.querySelectorAll('.mc').forEach((g) => {
        const sel = g.querySelector('input:checked');
        g.querySelectorAll('.mc-opt').forEach((o) => { o.classList.remove('mc-right', 'mc-wrong'); });
        g.querySelector(`input[value="${g.dataset.correct}"]`).closest('.mc-opt').classList.add('mc-right');
        if (sel && sel.value !== g.dataset.correct) sel.closest('.mc-opt').classList.add('mc-wrong');
      });
      line.textContent = msg('mc_score', { got: mcScore(task), max: Number(line.dataset.max) });
      task.dataset.checked = '1';
      document.dispatchEvent(new Event('fl-exam'));
    };
    details.addEventListener('toggle', show);
    task.addEventListener('change', () => { if (details.open) show(); });
  });

  // 3. the exam's total under its selection rules
  const total = document.querySelector('.exam-total');
  if (total) {
    const taskPoints = (card) => {
      if (card.querySelector('.mc-score')) return card.dataset.checked ? mcScore(card) : 0;
      let got = 0; card.querySelectorAll('.rubric input:checked').forEach((i) => { got += Number(i.value); });
      return got;
    };
    const update = () => {
      let sum = 0;
      document.querySelectorAll('.exam-section').forEach((sec) => {
        const pts = [...sec.querySelectorAll('.exam-task')].map(taskPoints).sort((a, b) => b - a).slice(0, Number(sec.dataset.choose));
        const s = pts.reduce((a, b) => a + b, 0); sum += s;
        const line = total.querySelector(`[data-sec="${sec.id}"] span`); if (line) line.textContent = s;
      });
      total.querySelector('.exam-total-line').textContent = msg('exam_total', { got: sum, max: Number(total.dataset.max) });
    };
    document.addEventListener('change', update); document.addEventListener('fl-exam', update); update();
  }
})();
