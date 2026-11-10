(function () {
  // Smart header: hide on scroll down, pop back in on scroll up.
  var nav = document.querySelector('.topnav');
  if (!nav) return;
  var lastY = window.scrollY || 0;
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || 0;
    // Solid background once we're off the top (so the nav stays readable
    // over page content); transparent again at the very top of the homepage.
    if (y > 60) { nav.classList.add('scrolled'); }
    else { nav.classList.remove('scrolled'); }
    if (y > 140 && y > lastY + 4) { nav.classList.add('nav-hidden'); }
    else if (y < lastY - 4 || y <= 140) { nav.classList.remove('nav-hidden'); }
    lastY = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();
})();
