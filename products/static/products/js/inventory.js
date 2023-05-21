document.addEventListener('DOMContentLoaded', () => {

  const deleteSelectedInventoryBtn = document.querySelector('#delete-selected-inventory-btn');
  deleteSelectedInventoryBtn.addEventListener('click', () => { deleteSelectedInventory(); });

  const selectedInventoryId = getSelectedInventoryId();
  let currentUrl = window.location.href;
  let newUrl = currentUrl.replace('/inventory/', `/update/inventory/${selectedInventoryId}`);
  const updateSelectedInventoryBtn = document.querySelector('#update-selected-inventory-btn');
  updateSelectedInventoryBtn.addEventListener('click', () => { window.location.href = newUrl; });

  // Mostrar el contenido del inventario seleccionado
  if (selectedInventoryId) {
    showInventoryProducts(selectedInventoryId);
  }

  // Manejador de evento para cuando cambie el inventario seleccionado
  const selectInventory = document.getElementById('select-inventory');
  selectInventory.addEventListener('change', () => {

    // Mostrar el contenido del inventario seleccionado y actualizar el funcionamiento del botón "Editar"
    const selectedInventoryId = getSelectedInventoryId();
    if (selectedInventoryId) {
      showInventoryProducts(selectedInventoryId);
      currentUrl = window.location.href;
      newUrl = currentUrl.replace('/inventory/', `/update/inventory/${selectedInventoryId}`);
      updateSelectedInventoryBtn.addEventListener('click', () => { window.location.href = newUrl; });
    }

  });

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


async function showInventoryProducts(inventoryId) {

  const options = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
  };

  try {

    // Get inventory products
    const response = await fetch(`/products/api/get/products/inventory/${inventoryId}`);
    const data = await response.json();
  
    if (data.success) {

      const tbody = document.querySelector('#dataTable tbody');
      tbody.innerHTML = '';
      
      // Actually show inventory products
      for (const key in data.inventory) {
        if (data.inventory.hasOwnProperty(key)) {
          const innerDictionary = data.inventory[key];
          const tr = document.createElement('tr');

          let productId; // Declare a variable to store product_id
          console.log(innerDictionary);

          for (const innerKey in innerDictionary) {
            if (innerDictionary.hasOwnProperty(innerKey)) {
              const value = innerDictionary[innerKey];
              const td = document.createElement('td');

              // If the key is 'product_id', store its value in productId
              if (innerKey === 'product_id') {
                productId = value;
              }

              if (innerKey === 'stock' && data.is_staff) {
                td.innerHTML = `<input class="stock-input" type="number" style="width: 50px;border-radius: 5px;border-width: 1px;" value="${value}" min="0" data-product-id="${productId}" data-inventory-id="${inventoryId}">`;
                tr.appendChild(td);
              } else if (innerKey != 'product_id') {
                td.innerText = `${value}`;
                tr.appendChild(td);
              }
            }
          }

          tbody.appendChild(tr);
        }
      }
      
      // Obtener todos los inputs de la página con la clase 'input-number-custom'
      const inputs = document.querySelectorAll('.stock-input');

      // Agregar un evento 'change' a cada input
      inputs.forEach(input => {
        input.addEventListener('change', (event) => {
          const product_id = event.target.dataset.productId;
          const inventory_id = event.target.dataset.inventoryId;
          const newValue = event.target.value;

          // Llamar a la función changeStock con los parámetros adecuados
          changeStock(product_id, inventory_id, newValue);
        });
      });

    }

  } catch (error) {

    alert(error);
    
  }

}

function getSelectedInventoryId() {

  // Obtener el elemento select de los inventarios
  const selectInventory = document.getElementById('select-inventory');
  // Obtener el inventario seleccionado
  const selectedOption = selectInventory.options[selectInventory.selectedIndex];
  // Obtener el ID del inventario seleccionado
  const selectedInventoryId = selectedOption.dataset.id;

  return selectedInventoryId ? selectedInventoryId : undefined;

}

async function changeStock(product_id, inventory_id, newValue) {

  data = {
    'product_id': product_id,
    'inventory_id': inventory_id,
    'newValue': newValue,
  }
  
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

    // Get inventory products
    const response = await fetch(`/products/api/update/product/stock`, options);
    const data = await response.json();

  } catch (error) {

    alert(error);
    
  }


}