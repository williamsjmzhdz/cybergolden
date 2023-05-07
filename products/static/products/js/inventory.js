document.addEventListener('DOMContentLoaded', () => {

  const deleteSelectedInventoryBtn = document.querySelector('#delete-selected-inventory-btn');
  deleteSelectedInventoryBtn.addEventListener('click', () => { deleteSelectedInventory(); });

  // FALTA HACER DINAMICO EL ID DEPENDIENDO DEL SELECT
  const currentUrl = window.location.href;
  const newUrl = currentUrl.replace('/inventory/', '/update/inventory/1');
  const updateSelectedInventoryBtn = document.querySelector('#update-selected-inventory-btn');
  updateSelectedInventoryBtn.addEventListener('click', () => { window.location.href = newUrl; });
  
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

function deleteSelectedInventory() {

  const selectedInventory = document.querySelector('#select-inventory');
  const optionToSelect = selectedInventory.querySelector(`option[value="${selectedInventory.value}"]`);

  swal.fire({
    title: `Se eliminará el inventario "${selectedInventory.value}" ¿estás seguro?`,
    text: 'No podrás revertir esto',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminarlo'
  }).then(async (result) => {
    if (result.isConfirmed) {

      data = {
        id: optionToSelect.dataset.id,
      }

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
    
        const response = await fetch('/products/api/delete/inventory', options);
        const data = await response.json();
    
        if (data.success) {
          window.location.reload();
        }
    
      } catch (error) {
    
        alert(error);
    
      }

    }
  });

}