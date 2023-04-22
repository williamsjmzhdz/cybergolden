// INICIALIZA MANEJADORES Y OBJETOS DEL DOM CUANDO CARGA EL HTML
document.addEventListener('DOMContentLoaded', () => {

  const $submitEditCategoryBtn = document.getElementById('submit-edit-category-btn');
  $submitEditCategoryBtn.addEventListener('click', (e) => {
    const name = document.getElementById('name').value;
    updateCategory(e.target.dataset.id, name);
  });

  const $cancelCreateCategoryBtn = document.getElementById('cancel-edit-category-btn');
  $cancelCreateCategoryBtn.addEventListener('click', () => {
    window.location.href = "/products/categories/";
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


  
// FUNCIONES PARA HACER SOLICITUDES A LA API

async function updateCategory(id, name) {

  const data = {
    id: id,
    name: name
  };

  // Get the CSRF token
  const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

  const options = {
    method: 'PUT',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  };
  
  try {
    
    const response = await fetch('/products/update/category', options);
    const data = await response.json();

    if (data.success) {
      window.location.href = "/products/categories/";
    } else {
      document.getElementById('repeated-name-alert').innerText = `${data.message} El nombre de la categoría debe ser único y distinto al que ya tiene.`;
    }

  } catch (error) {

    alert(error);

  }

}