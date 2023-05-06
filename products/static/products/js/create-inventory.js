document.addEventListener("DOMContentLoaded", () => {

  const $cancelCreateInventoryBtn = document.getElementById('cancel-create-inventory-btn');
  $cancelCreateInventoryBtn.addEventListener('click', () => {
    window.location.href = "/products/inventory/";
  });

  const $navLinks = document.querySelectorAll('.nav-link');
  markActiveNavigationLink($navLinks, 'nav-link-inventory');

});


function markActiveNavigationLink($navLinks, activeLink) {

  $navLinks.forEach($navLink => {
    if ($navLink.id === activeLink) {
      $navLink.classList.add('active');
    } else {
      $navLink.classList.remove('active');
    }
  });

}