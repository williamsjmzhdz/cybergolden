document.addEventListener('DOMContentLoaded', () => {

  const $deleteCategoryBtns = document.querySelectorAll('.delete-category-btn');
  $deleteCategoryBtns.forEach(($deleteCategoryBtn) => {
    $deleteCategoryBtn.addEventListener('click', (e) => {
      swal.fire({
        title: '¿Estás seguro?',
        text: 'No podrás revertir esto',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminarlo'
      }).then((result) => {
        if (result.isConfirmed) {
          deleteCategory(e.target.dataset.id);
        }
      });
    });
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

async function deleteCategory(id) {

  const data = {
    id: id,
  };

  // Get the CSRF token
  const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

  const options = {
    method: 'DELETE',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  };
  
  try {
    
    const response = await fetch('/products/api/delete/category', options);
    const data = await response.json();

    if (data.success) {
      window.location.reload();
    }

  } catch (error) {

    alert(error);

  }

}