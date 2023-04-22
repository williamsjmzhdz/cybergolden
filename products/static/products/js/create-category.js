document.addEventListener("DOMContentLoaded", () => {

  const $submitCreateCategoryBtn = document.getElementById('submit-create-category-btn');
  $submitCreateCategoryBtn.addEventListener("click", () => {
    createCategory();
  });

  const $cancelCreateCategoryBtn = document.getElementById('cancel-create-category-btn');
  $cancelCreateCategoryBtn.addEventListener('click', () => {
    window.location.href = "/products/categories/";
  });

  const $navLinks = document.querySelectorAll('.nav-link');
  markActiveNavigationLink($navLinks, 'nav-link-categories');

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


async function createCategory() {

  const name = document.getElementById('name').value;
  const data = {
    name: name,
  };

  const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

  const options = {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  };

  try {

    const response = await fetch('/products/create/category', options);
    const data = await response.json();

    if (data.success) {
      window.location.href = "/products/categories/";
    } else {
      document.getElementById('repeated-name-alert').innerText = `${data.message} El nombre de la categoría debe ser único.`;
    }

  } catch (error) {

    alert(error);

  }

}