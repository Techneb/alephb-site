// Home page: the Day/Night switch and the project carousels (a bullet shows its picture; otherwise every 4 s).
(function () {
  var root = document.documentElement, dark = matchMedia("(prefers-color-scheme: dark)");
  var btn = document.getElementById("theme");
  function mode() { return root.dataset.theme || (dark.matches ? "dark" : "light"); }
  function paint() {
    var night = mode() === "dark";
    btn.innerHTML = '<span aria-hidden="true">' + (night ? "☀️" : "🌙") + "</span><span>" + (night ? "Day" : "Night") + "</span>";
    btn.setAttribute("aria-label", night ? "Switch to day mode" : "Switch to night mode");
  }
  btn.onclick = function () {
    root.dataset.theme = mode() === "dark" ? "light" : "dark";
    try { localStorage.setItem("alephb.theme", root.dataset.theme); } catch (e) {}
    paint();
  };
  dark.addEventListener("change", paint);
  paint();

  var still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll("[data-carousel]").forEach(function (section) {
    var slides = section.querySelectorAll(".slide"), points = section.querySelectorAll("li[data-slide]");
    var current = 0, held = false, seen = false, timer;
    var dots = document.createElement("div");
    dots.className = "dots";
    if (slides.length > 1) section.querySelector(".slides").after(dots);
    slides.forEach(function (_, i) {
      var d = document.createElement("button");
      d.type = "button"; d.setAttribute("aria-label", "Picture " + (i + 1) + " of " + slides.length);
      d.onclick = function () { show(i); };
      dots.appendChild(d);
    });
    function show(i, point) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, j) {
        s.classList.toggle("on", j === current);
        var v = s.querySelector("video");
        if (v) { if (j === current && seen) { v.currentTime = 0; v.play().catch(function () {}); } else v.pause(); }
      });
      dots.querySelectorAll("button").forEach(function (d, j) { d.classList.toggle("on", j === current); });
      point = point || [].find.call(points, function (p) { return +p.dataset.slide === current; });
      points.forEach(function (p) { p.classList.toggle("on", p === point); });
    }
    function tick() {
      clearTimeout(timer);
      if (still || held || !seen || slides.length < 2) return;
      var v = slides[current].querySelector("video");
      timer = setTimeout(function () { show(current + 1); tick(); }, v && v.duration ? Math.max(4000, v.duration * 1000) : 4000);
    }
    points.forEach(function (p) {
      p.addEventListener("mouseenter", function () { held = true; show(+p.dataset.slide, p); });
      p.addEventListener("click", function () { show(+p.dataset.slide, p); });
    });
    section.querySelector("ul.points").addEventListener("mouseleave", function () { held = false; tick(); });
    new IntersectionObserver(function (e) { seen = e[0].isIntersecting; show(current); tick(); }, { threshold: 0.3 }).observe(section);
    show(0);
  });
})();
