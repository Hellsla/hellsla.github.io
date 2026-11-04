/* The investigation bank of a course page (scripts/investigations.py bank, teacher 2026-10-31): a search field and
   its selects narrow the list in place (also the YO-sekoitin, scripts/mixer.py, which adds a random pick), without reloading. Without scripts the form stays hidden and every
   investigation shows; "Näytä kaikki" (the form's reset) shows them all again. The count is announced politely. */
(function () {
  const form = document.getElementById('bank-filter');
  const list = document.getElementById('bank-list');
  if (!form || !list) return;
  const items = [...list.querySelectorAll('.bank-item')];
  const count = document.getElementById('bank-count');
  const none = document.getElementById('bank-none');
  const norm = (s) => s.toLowerCase().normalize('NFC').trim();
  // every select of the form filters on the item's data attribute of the same name (space-separated values)
  const selects = [...form.querySelectorAll('select')];
  const random = form.querySelector('[data-random]');
  let picked = null;                       // "Arvo n tehtävää": a random set among the matching items, until the filters change
  function apply() {
    const q = norm(form.q.value);
    let shown = 0;
    for (const li of items) {
      const ok = (!q || q.split(/\s+/).every((w) => li.dataset.words.includes(w)))
        && selects.every((s) => !s.value || (li.dataset[s.name] || '').split(' ').includes(s.value))
        && (!picked || picked.has(li));
      li.hidden = !ok; shown += ok;
    }
    // a bank in sections (FY10's topics, scripts/cardgrid.py): a section with nothing left hides with its heading
    for (const ol of list.querySelectorAll('ol.ch-cards')) {
      const empty = !ol.querySelector('.bank-item:not([hidden])');
      ol.hidden = empty;
      for (let el = ol.previousElementSibling; el && !el.matches('ol'); el = el.previousElementSibling) el.hidden = empty;
    }
    none.hidden = shown > 0;
    count.textContent = count.dataset.template.replace('{shown}', shown).replace('{total}', items.length);
  }
  if (random) random.addEventListener('click', () => {
    picked = null; apply();
    const pool = items.filter((li) => !li.hidden);
    for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
    picked = new Set(pool.slice(0, Number(random.dataset.random) || 3)); apply();
  });
  form.hidden = false;
  const changed = () => { picked = null; apply(); };
  form.addEventListener('input', changed);
  form.addEventListener('change', changed);
  form.addEventListener('submit', (ev) => { ev.preventDefault(); apply(); });
  form.addEventListener('reset', () => setTimeout(changed, 0));
  apply();
})();
