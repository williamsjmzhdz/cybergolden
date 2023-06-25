document.addEventListener("DOMContentLoaded", () => {
  const $navLinks = document.querySelectorAll(".nav-link");
  markActiveNavigationLink($navLinks, "nav-link-cuts");
});

function markActiveNavigationLink($navLinks, activeLink) {
  $navLinks.forEach(($navLink) => {
    if ($navLink.id === activeLink) {
      $navLink.classList.add("active");
    } else {
      $navLink.classList.remove("active");
    }
  });
}
