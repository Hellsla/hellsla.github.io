/* Kuuntele ja katso (scripts/media_tips.py): module, type and short filters. Without this script the form stays hidden and
   every item is listed; the controls are real buttons and a checkbox, so the keyboard works. */
(function () {
  var f = document.querySelector(".media-filters"); if (!f) return;
  f.hidden = false;
  var items = [].slice.call(document.querySelectorAll("main li.media"));
  var mod = null, typ = null, count = f.querySelector(".media-count"), short = f.querySelector("#mf-short");
  function apply() {
    var shown = 0, seen = {}, any = !!(mod || typ || short.checked);
    items.forEach(function (li) {
      var ok = (!mod || li.dataset.modules.split(" ").indexOf(mod) >= 0) && (!typ || li.dataset.type === typ) &&
               (!short.checked || (li.dataset.min && +li.dataset.min <= +short.dataset.short));
      li.hidden = !ok;
      if (ok && !li.closest(".media-featured")) shown++;
    });
    var feat = document.getElementById("media-featured"); if (feat) feat.hidden = any;
    [].forEach.call(document.querySelectorAll(".media-module"), function (s) { s.hidden = !s.querySelector("li.media:not([hidden])"); });
    count.textContent = shown ? count.dataset.tpl.replace("{n}", shown) : count.dataset.none;
  }
  function pick(group) {
    [].forEach.call(f.querySelectorAll("[data-" + group + "]"), function (b) {
      b.addEventListener("click", function () {
        var on = b.getAttribute("aria-pressed") !== "true";
        [].forEach.call(f.querySelectorAll("[data-" + group + "]"), function (o) { o.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", on ? "true" : "false");
        if (group === "module") mod = on ? b.dataset.module : null; else typ = on ? b.dataset.type : null;
        apply();
      });
    });
  }
  pick("module"); pick("type"); short.addEventListener("change", apply); apply();
})();
