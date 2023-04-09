document.addEventListener('DOMContentLoaded', () => {

  const $saveBtn = document.getElementById('save-btn');
  $saveBtn.onclick = update;

})


async function update() {
  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const phone_number = document.getElementById('phone_number').value;

  const data = {
    username: username,
    email: email,
    phone_number: phone_number,
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
    const response = await fetch('/users/update/', options);
    const data = await response.json();
    console.log(data);

    showAlert(data);

    if (data.status === 'success') {
      cleanFields(username, email, phone_number);
    }

  } catch (error) {
    alert(error);
  }
}

function showAlert(data) {

    const $successAlert = document.getElementById('alert-success');
    const $warningAlert = document.getElementById('alert-warning');
    
    if (data.status === 'success') {

      showPersonalInfoAlert($successAlert, $warningAlert, data.message);

      setTimeout(function() {
        $successAlert.style.display = "none";
      }, 5000);


    } else if (data.status === 'error') {

      showPersonalInfoAlert($warningAlert, $successAlert, data.message);

    }

}

function cleanFields(username, email, phone_number) {

  if (username) {
    document.getElementById('username').placeholder = username;
  }

  if (email) {
    document.getElementById('email').placeholder = email;
  }

  if (phone_number) {
    document.getElementById('phone_number').placeholder = phone_number;
  }

  document.getElementById('username').value = '';
  document.getElementById('email').value = '';
  document.getElementById('phone_number').value = '';

}

function showPersonalInfoAlert($alertToShow, $alertToHide, message) {

  $alertToHide.style.display = 'none';

  $alertToShow.innerText = message;
  $alertToShow.style.display = 'block';

}