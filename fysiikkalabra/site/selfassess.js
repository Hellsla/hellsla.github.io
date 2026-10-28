/* Self-assessment (teacher's brief 2026-10-28, scripts/practice.py, NOTES.md §9). One component for every course:
   1. The rubric of a Sovella itsenäisesti task (.rubric): the student picks the points each criterion earns (partial
      credit allowed); the total is shown as self-assessed points, never as a grade. A competency scored at most half
      shows its links to the chapters where it is practised (the task's `links`, written into the page by build.py).
   2. Arvioi osaamistasi (.selfcheck) at the end of a chapter: Osaan / Tarvitsen vielä harjoitusta for each of the
      chapter's own goals; the second shows where to go back to.
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

  // 2. Arvioi osaamistasi: the chapter's goals, Osaan / Tarvitsen vielä harjoitusta
  document.querySelectorAll('.selfcheck').forEach((box) => {
    const items = [...box.querySelectorAll('li[data-goal]')], summary = box.querySelector('.selfcheck-summary');
    const update = (save) => {
      const state = {}; let ok = 0, n = 0;
      items.forEach((li, i) => {
        const sel = li.querySelector('input:checked');
        if (sel) { state[i] = sel.value; n += 1; if (sel.value === 'ok') ok += 1; }
        li.querySelector('.selfcheck-next').hidden = !(sel && sel.value === 'practice');
      });
      if (save) store.set(box.id, state);
      summary.textContent = n ? msg('selfcheck_summary', { ok, n: items.length }) : '';
    };
    restore(items, store.get(box.id));
    box.addEventListener('change', () => update(true));
    update(false);
  });
})();
