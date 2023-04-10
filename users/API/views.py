import json
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


@require_http_methods(['PUT'])
@login_required
def update(request):
  """
  Update a user's information.
  """

	# Get the user information
  data = json.loads(request.body)
  username = data['username']
  email = data['email']
  phone_number = data['phone_number']

  # Get the regular expressions to match the username, email address and phone number from the request parameters.
  username_regex = r'^[\w.@+-]{1,150}$'
  email_regex = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$'
  phone_number_regex = r'^([0-9]{2})?-?([0-9]{4})-?([0-9]{4})$'
  
  if not username and not email and not phone_number:
    return JsonResponse({'status': 'error','message': 'Proporcione un nombre de usuario, una dirección de correo electrónico o un número de teléfono.'}, status=400)
  
  # Initialize the error flag to False and initialize the response message
  error = False
  message = ''

  if username:
    update_username = True
    if not re.match(username_regex, username):
      error = True
      message += ' El nombre de usuario debe contener entre 1 y 150 caracteres alfanuméricos, incluyendo los símbolos @ . + - '
  else:
    update_username = False

  if email:
    update_email = True
    if not re.match(email_regex, email):
      error = True
      message += ' El correo electrónico ingresado no es válido. Asegúrese de que tenga un formato válido (por ejemplo, usuario@dominio.com). '
  else:
    update_email = False

  if phone_number:
    update_phone_number = True
    if not re.match(phone_number_regex, phone_number):
      error = True
      message += ' El número telefónico debe tener 10 dígitos y puede estar en formato xx-xxxx-xxxx o xxxxxxxxxx. '
  else:
    update_phone_number = False
      
	# If the error flag is set to True, return an error message
  if error:
    return JsonResponse({'status': 'error','message': message}, status=400)

  # If the error flag is set to False, update the user's information
  user = request.user
  
  if update_username:
    user.username = username
  
  if update_email:
    user.email = email
        
  if update_phone_number and hasattr(user, 'employee'):
    user.employee.phone_number = phone_number
    user.employee.save()
  elif not hasattr(user, 'employee'):
    return JsonResponse({'status': 'error', 'message': 'El usuario no tiene un objeto Employee relacionado.'}, status=400)

  user.save()

  return JsonResponse({'status':'success','message': 'Usuario actualizado con éxito.'}, status=200)
