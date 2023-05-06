document.addEventListener('DOMContentLoaded', () => {

  const deleteSelectedInventoryBtn = document.querySelector('#delete-selected-inventory-btn');
  deleteSelectedInventoryBtn.addEventListener('click', () => { deleteSelectedInventory(); });
  
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

  const selectedInventory = document.querySelector('#select-inventory').value;

  swal.fire({
    title: `Se eliminará el inventario "${selectedInventory}" ¿estás seguro?`,
    text: 'No podrás revertir esto',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminarlo'
  }).then((result) => {
    if (result.isConfirmed) {
      console.log('Eliminando inventario...');
    }
  });

}