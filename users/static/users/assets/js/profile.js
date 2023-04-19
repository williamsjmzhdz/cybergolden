// Espera a que el DOM se cargue antes de ejecutar el código
document.addEventListener('DOMContentLoaded', () => {
  // Obtiene el botón de guardar y le asigna la función de actualización al hacer clic
  const saveBtn = document.getElementById('save-btn');
  saveBtn.onclick = update;

  // Marca el enlace de perfil como activo
  markLink();
});

// Esta función actualiza los datos del usuario en el servidor
async function update() {
  // Obtiene los valores de los campos de entrada
  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const phoneNumber = document.getElementById('phone_number').value;

  // Crea un objeto de datos para enviar al servidor
  const data = {
    username: username,
    email: email,
    phone_number: phoneNumber,
  };

  // Obtiene el token CSRF
  const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

  // Configura las opciones para la solicitud PUT
  const options = {
    method: 'PUT',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  };

  try {
    // Envía la solicitud al servidor y espera la respuesta
    const response = await fetch('/users/update/', options);
    const data = await response.json();

    // Muestra una alerta según el resultado de la respuesta
    showAlert(data);

    // Si la actualización fue exitosa, limpia los campos de entrada
    if (data.status === 'success') {
      cleanFields(username, email, phoneNumber);
    }

  } catch (error) {
    alert(error);
  }
}

// Esta función muestra una alerta según el resultado de la actualización
function showAlert(data) {
  // Obtiene las alertas de éxito y advertencia
  const successAlert = document.getElementById('alert-success');
  const warningAlert = document.getElementById('alert-warning');
    
  if (data.status === 'success') {
    // Muestra la alerta de éxito y oculta la de advertencia
    showPersonalInfoAlert(successAlert, warningAlert, data.message);

    // Oculta la alerta de éxito después de 5 segundos
    setTimeout(function() {
      successAlert.style.display = 'none';
    }, 5000);
  } else if (data.status === 'error') {
    // Muestra la alerta de advertencia y oculta la de éxito
    showPersonalInfoAlert(warningAlert, successAlert, data.message);
  }
}

// Esta función limpia los campos de entrada
function cleanFields(username, email, phoneNumber) {
  // Si se proporcionó un valor, colócalo como marcador de posición
  if (username) {
    document.getElementById('username').placeholder = username;
  }
  if (email) {
    document.getElementById('email').placeholder = email;
  }
  if (phoneNumber) {
    document.getElementById('phone_number').placeholder = phoneNumber;
  }

  // Borra los valores de los campos de entrada
  document.getElementById('username').value = '';
  document.getElementById('email').value = '';
  document.getElementById('phone_number').value = '';
}

// Función que muestra un mensaje de alerta personalizado
function showPersonalInfoAlert(alertToShow, alertToHide, message) {
  alertToHide.style.display = 'none';
  alertToShow.innerText = message;
  alertToShow.style.display = 'block';
}

// Función que marca el enlace del perfil como activo
function markLink() {
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      link.classList.remove('active');
    });
  });
  document.getElementById('nav-link-profile').classList.add('active');
}
