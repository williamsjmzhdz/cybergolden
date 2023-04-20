// INICIALIZA MANEJADORES Y OBJETOS DEL DOM CUANDO CARGA EL HTML
document.addEventListener('DOMContentLoaded', () => {

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

  const $submitCreateCategoryBtn = document.getElementById('submit-create-category-btn');
  $submitCreateCategoryBtn.addEventListener('click', () => {
    createCategory();
  });

  const $navLinks = document.querySelectorAll('.nav-link');
  markActiveNavigationLink($navLinks, 'nav-link-categories');
});


// FUNCIONES DE MANEJO DEL DOM

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


  
// FUNCIONES PARA HACER SOLICITUDES A LA API

// Esta función se encarga de crear una categoría haciendo una llamada a una API 
async function createCategory() {

  const name = document.getElementById('name').value;
  console.log(name);

  const data = {
    name: name,
  };

  // Get the CSRF token
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
      window.location.reload();
    } else {
      document.getElementById('repeated-name-alert').innerText = `${data.message} El nombre de la categoría debe ser único.`;
    }

  } catch (error) {

    alert(error);

  }

}