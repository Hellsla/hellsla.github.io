/* LUMA-tutor's pages (scripts/lumatutor.py, teacher 2026-11-09). Nothing is stored and nothing is sent.
   - The workshop bank's filters (topic, audience, duration, equipment) show only the cards that match all of them; without
     the script every card shows and the filters stay hidden.
   - Kopioi teksti copies a template's plain text; Tulosta prints that template or the participant's material alone;
     Tulosta koko sivu prints the page. The buttons stay hidden where the browser cannot do it. */
(function () {
  var f = document.querySelector(".lt-filter");
  if (f) {
    var cards = document.querySelectorAll(".lt-wcard"), sels = f.querySelectorAll("select[data-f]"), n = f.querySelector(".lt-filter-n");
    var none = document.querySelector(".lt-filter-none");
    var run = function () {
      var want = {}, any = false, shown = 0;
      sels.forEach(function (s) { if (s.value) { want[s.getAttribute("data-f")] = s.value; any = true; } });
      cards.forEach(function (c) {
        var ok = true;
        Object.keys(want).forEach(function (k) {
          var v = c.getAttribute("data-" + k) || "";
          if (k === "equipment" ? v.split(" ").indexOf(want[k]) < 0 : v !== want[k]) ok = false;
        });
        c.hidden = !ok; if (ok) shown++;
      });
      document.querySelectorAll(".lt-wgroup").forEach(function (g) { g.hidden = !g.querySelector(".lt-wcard:not([hidden])"); });
      n.textContent = any ? n.getAttribute("data-shown").replace("{n}", shown).replace("{m}", cards.length) : "";
      if (none) none.hidden = shown > 0;
    };
    sels.forEach(function (s) { s.addEventListener("change", run); });
    f.querySelector(".lt-reset").addEventListener("click", function () { sels.forEach(function (s) { s.value = ""; }); run(); });
    f.hidden = false;
  }
  document.querySelectorAll("[data-copy]").forEach(function (b) {
    var src = document.getElementById(b.getAttribute("data-copy")), say = b.parentNode.querySelector(".lt-copied");
    if (!src || !navigator.clipboard) return;
    b.hidden = false;
    b.addEventListener("click", function () {
      navigator.clipboard.writeText(src.textContent).then(function () { if (say) say.textContent = b.getAttribute("data-copied"); });
    });
  });
  if (!window.print) return;
  var root = document.documentElement;
  window.addEventListener("afterprint", function () {
    root.classList.remove("lt-print-one");
    document.querySelectorAll(".lt-print-target, .lt-print-hide").forEach(function (t) { t.classList.remove("lt-print-target", "lt-print-hide"); });
  });
  document.querySelectorAll("[data-print]").forEach(function (b) {
    var t = document.getElementById(b.getAttribute("data-print"));
    if (!t) return;
    b.hidden = false;
    b.addEventListener("click", function () {
      // Only the target and the elements around it stay in the layout, so no empty pages are printed after it.
      for (var e = t; e && e !== document.body; e = e.parentElement) {
        Array.prototype.forEach.call(e.parentElement.children, function (s) { if (s !== e) s.classList.add("lt-print-hide"); });
      }
      root.classList.add("lt-print-one"); t.classList.add("lt-print-target"); window.print();
    });
  });
  document.querySelectorAll("[data-print-all]").forEach(function (b) {
    b.hidden = false;
    b.addEventListener("click", function () { window.print(); });
  });
})();
