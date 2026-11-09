/* Ahjo's course and guide pages (scripts/ahjo.py, teacher 2026-11-09). No data is stored.
   - An old link to a lesson on a course page (ahjo-1.html#tunti-3) opens the lesson's own page; #miniprojekti opens
     lesson 14, where the mini project options now are.
   - A link to something folded under "Lisätietoa opintojaksosta" (#tavoitteet, #ajokortti, ...) unfolds it.
   - A guide opened from a lesson (?tunti=ahjo-1-tunti-3) shows a link back to that lesson.
   - The material and project banks' filters (time, level) show only the matching cards; without the script every card
     shows and the filter stays hidden. */
(function () {
  var page = location.pathname.split("/").pop() || "";
  var course = page.match(/^ahjo-(\d)\.html$/);
  var h = location.hash.slice(1);
  if (course && h) {
    var m = h.match(/^tunti-(\d{1,2})$/);
    if (m) { location.replace("ahjo-" + course[1] + "-tunti-" + m[1] + ".html"); return; }
    if (h === "miniprojekti" && course[1] === "1") { location.replace("ahjo-1-tunti-14.html#miniprojekti"); return; }
  }
  function unfold() {
    var id = location.hash.slice(1), t = id && document.getElementById(id);
    if (!t) return;
    var d = t.closest("details");
    if (d && !d.open) { d.open = true; t.scrollIntoView(); }
  }
  unfold(); window.addEventListener("hashchange", unfold);
  var from = new URLSearchParams(location.search).get("tunti");
  var back = document.querySelector(".ahjo-from");
  if (back && from && /^ahjo-\d-tunti-\d{1,2}$/.test(from)) {
    back.querySelector("a").setAttribute("href", from + ".html");
    back.hidden = false;
  }
  document.querySelectorAll(".ahjo-filter").forEach(function (f) {
    var key = f.getAttribute("data-key"), scope = f.closest("section") || f.closest("main") || document;
    var items = scope.querySelectorAll("[data-" + key + "]"), n = f.querySelector(".ahjo-filter-n");
    var btns = f.querySelectorAll(".ahjo-fbtn");
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var v = b.getAttribute("data-v"), shown = 0;
        btns.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        items.forEach(function (it) { var ok = !v || it.getAttribute("data-" + key) === v; it.hidden = !ok; if (ok) shown++; });
        n.textContent = v ? f.getAttribute("data-shown").replace("{n}", shown).replace("{m}", items.length) : "";
      });
    });
    f.hidden = false;
  });
})();
