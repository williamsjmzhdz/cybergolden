document.addEventListener("DOMContentLoaded", () => {

  const $cancelCreateCategoryBtn = document.getElementById('cancel-create-product-btn');
  $cancelCreateCategoryBtn.addEventListener('click', () => {
    window.location.href = "/products/";
  });

  const $navLinks = document.querySelectorAll('.nav-link');
  markActiveNavigationLink($navLinks, 'nav-link-products');

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