/* The investigation bank of a course page (scripts/investigations.py bank, teacher 2026-10-31): a search field and
   four selects narrow the list in place, without reloading. Without scripts the form stays hidden and every
   investigation shows; "Näytä kaikki" (the form's reset) shows them all again. The count is announced politely. */
(function () {
  const form = document.getElementById('bank-filter');
  const list = document.getElementById('bank-list');
  if (!form || !list) return;
  const items = [...list.querySelectorAll('.bank-item')];
  const count = document.getElementById('bank-count');
  const none = document.getElementById('bank-none');
  const norm = (s) => s.toLowerCase().normalize('NFC').trim();
  function apply() {
    const q = norm(form.q.value);
    const want = { topic: form.topic.value, f: form.f.value, e: form.e.value, mode: form.mode.value };
    let shown = 0;
    for (const li of items) {
      const ok = (!q || q.split(/\s+/).every((w) => li.dataset.words.includes(w)))
        && (!want.topic || li.dataset.topic === want.topic)
        && (!want.f || li.dataset.f.split(' ').includes(want.f))
        && (!want.e || li.dataset.e.split(' ').includes(want.e))
        && (!want.mode || li.dataset.mode.split(' ').includes(want.mode));
      li.hidden = !ok; shown += ok;
    }
    none.hidden = shown > 0;
    count.textContent = count.dataset.template.replace('{shown}', shown).replace('{total}', items.length);
  }
  form.hidden = false;
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  form.addEventListener('submit', (ev) => { ev.preventDefault(); apply(); });
  form.addEventListener('reset', () => setTimeout(apply, 0));
  apply();
})();
