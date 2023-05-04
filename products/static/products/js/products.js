document.addEventListener('DOMContentLoaded', () => {

  // Seleccionando elementos HTML
  const table = document.querySelector('table');
  const selectAllCheckbox = document.querySelector('thead input[type="checkbox"]');
  const rowCheckboxes = document.querySelectorAll('tbody input[type="checkbox"]');
  const deleteProductButtons = document.querySelectorAll('.delete-product-btn');
  const deleteAllProductsButton = document.querySelector('#delete-all-products-btn');

  // Agregar un event listener a cada checkbox de fila
  rowCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', () => {
      const allChecked = Array.from(rowCheckboxes).every((checkbox) => checkbox.checked);
      selectAllCheckbox.checked = allChecked;
    });
  });

  // Agregar un event listener al checkbox "Select All"
  if (selectAllCheckbox) {
    selectAllCheckbox.addEventListener('change', () => {
      rowCheckboxes.forEach((checkbox) => {
        checkbox.checked = selectAllCheckbox.checked
      });
    });
  }

  // Agregar un event listener al campo de búsqueda
  const searchInput = document.querySelector('#searchInput');
  searchInput.addEventListener('input', () => {
    const filterValue = searchInput.value.toLowerCase();
    const rows = table.querySelectorAll('tbody tr');
  
    rows.forEach((row) => {
      const searchableCells = row.querySelectorAll('.searchable');
      let matchFound = false;
  
      searchableCells.forEach((cell) => {
        const text = cell.textContent.toLowerCase();
        if (text.includes(filterValue)) {
          matchFound = true;
        }
      });
  
      row.style.display = matchFound ? '' : 'none';
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

  // Elimina un producto
  deleteProductButtons.forEach(btn => {
    btn.addEventListener("click", (e) => {
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
          deleteProduct(e.target.dataset.id);
        }
      });
    });
  });

  if (deleteAllProductsButton) {

    // Elimina todos los productos seleccionados
    deleteAllProductsButton.addEventListener("click", () => {
      const productsCheckBoxes = document.querySelectorAll('.product-checkbox');
      const toDelete = [];
      productsCheckBoxes.forEach(checkBox => {
        if (checkBox.checked) {
          toDelete.push(checkBox);
        }
      });
      if (toDelete.length > 0) {
        swal.fire({
          title: '¿Estás seguro?',
          text: 'No podrás revertir esto',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Sí, eliminarlo(s)'
        }).then((result) => {
          if (result.isConfirmed) {
            ids = [];
            toDelete.forEach(checkBox => {
              ids.push(checkBox.dataset.productId);
            });
            deleteSelectedProducts(ids);
          }
        });
      }
    });

  }

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

async function deleteProduct(id, name) {

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
    
    const response = await fetch('/products/api/delete/product', options);
    const data = await response.json();

    if (data.success) {
      window.location.reload();
    }

  } catch (error) {

    alert(error);

  }

}

function deleteSelectedProducts(ids) {
  ids.forEach(async id => {
    
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
      
      const response = await fetch('/products/api/delete/product', options);
      const data = await response.json();
  
      if (data.success) {
        window.location.reload();
      }
  
    } catch (error) {
  
      alert(error);
  
    }
  });

}