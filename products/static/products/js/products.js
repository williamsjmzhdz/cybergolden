document.addEventListener('DOMContentLoaded', () => {

  const table = document.querySelector('table');
  const selectAllCheckbox = table.querySelector('thead input[type="checkbox"]');
  const rowCheckboxes = table.querySelectorAll('tbody input[type="checkbox"]');

  // Agregar un event listener a cada checkbox de fila
  rowCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', () => {
      const allChecked = Array.from(rowCheckboxes).every((checkbox) => checkbox.checked);
      selectAllCheckbox.checked = allChecked;
    });
  });

  // Agregar un event listener al checkbox "Select All"
  selectAllCheckbox.addEventListener('change', () => {
    rowCheckboxes.forEach((checkbox) => {
      checkbox.checked = selectAllCheckbox.checked
    });
  });

  // Agregar un event listener al campo de búsqueda
  const searchInput = document.querySelector('#searchInput');
  searchInput.addEventListener('input', () => {
    const filterValue = searchInput.value.toLowerCase();
    const rows = table.querySelectorAll('tbody tr');

    rows.forEach((row) => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(filterValue) ? '' : 'none';
    });
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