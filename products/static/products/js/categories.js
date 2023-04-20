document.addEventListener('DOMContentLoaded', () => {
  const $navLinks = document.querySelectorAll('.nav-link');

  const $showCategoriesContainer = document.getElementById('show-categories-container');
  const $createCategoryContainer = document.getElementById('create-category-container');

  const $createCategoryBtn = document.getElementById('create-category-btn');
  $createCategoryBtn.addEventListener('click', () => {
    showAndHideContainers($createCategoryContainer, $showCategoriesContainer);
  });

  const $cancelCreateCategoryBtn = document.getElementById('cancel-create-category-btn');
  $cancelCreateCategoryBtn.addEventListener('click', () => {
    showAndHideContainers($showCategoriesContainer, $createCategoryContainer);
  });

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

function showAndHideContainers($showContainer, $hideContainer) {
  $showContainer.style.display = 'block';
  $hideContainer.style.display = 'none';
}
