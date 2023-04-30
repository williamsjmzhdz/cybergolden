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
  
  // Agregar los porcentages de costo de logistica
  const tds = document.querySelectorAll('.logistics_cost_percentage');
  tds.forEach(td => {
    // Obtener los valores de datos del elemento HTML
    const logisticsCost = parseFloat(td.dataset.logisticsCost);
    const totalCost = parseFloat(td.dataset.totalCost);

    // Calcular el porcentaje
    const logisticsCostPercentage = (logisticsCost / totalCost) * 100;

    // Insertar el porcentaje en el elemento HTML
    td.textContent = logisticsCostPercentage.toFixed(2) + '%';
  });

  // Marcar el enlace Products como activo
  const $navLinks = document.querySelectorAll('.nav-link');
  markActiveNavigationLink($navLinks, 'nav-link-products');

});

function markActiveNavigationLink($navLinks, activeLink) {
  console.log('entro');
  $navLinks.forEach($navLink => {
    if ($navLink.id === activeLink) {
      $navLink.classList.add('active');
    } else {
      $navLink.classList.remove('active');
    }
  });
}