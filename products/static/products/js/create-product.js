document.addEventListener("DOMContentLoaded", () => {

  const $submitCreateCategoryBtn = document.getElementById('submit-create-product-btn');
  $submitCreateCategoryBtn.addEventListener("click", () => {
    createProduct();
  });

  const $cancelCreateCategoryBtn = document.getElementById('cancel-create-product-btn');
  $cancelCreateCategoryBtn.addEventListener('click', () => {
    window.location.href = "/products/products/";
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


async function createProduct() {

  console.log('hola mundo');

}