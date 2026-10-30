/* Working mode of an investigation page (scripts/investigations.py): the radios choose ohjattu / osittain ohjattu /
   itsenäinen, and each guidance block (.inv-tuki data-modes="O OO") shows only in its modes. Without scripts every
   block shows, so nothing is lost. */
(function () {
  const radios = document.querySelectorAll('input[name="inv-mode"]');
  function apply(mode) {
    document.querySelectorAll('.inv-tuki').forEach((b) => { b.hidden = !b.dataset.modes.split(' ').includes(mode); });
  }
  radios.forEach((r) => r.addEventListener('change', () => apply(r.value)));
  const checked = document.querySelector('input[name="inv-mode"]:checked');
  if (checked) apply(checked.value);
})();
