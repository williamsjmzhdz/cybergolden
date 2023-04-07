from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User


class AuthForm(AuthenticationForm):
	'''
	Form that uses built-in AuthenticationForm to handle user auth
	'''
	username = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={
            'placeholder': 'Nombre de usuario', 
            'name': 'username', 
            'type': 'text', 
            'class': 'form-control form-control-user'
	    }))
	password = forms.CharField(max_length=25, required=True,
		widget=forms.PasswordInput(attrs={
		    'placeholder': 'Contraseña', 
            'name': 'password', 
            'type': 'password', 
            'class': 'form-control form-control-user'
	    }))

	class Meta:
		model = User
		fields = ('username','password', )