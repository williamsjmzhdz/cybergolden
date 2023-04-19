from django import forms
from products.models import Category


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


class CategoryForm(forms.ModelForm):
  '''
  Form that handle categories creation.
  '''

  name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
      'placeholder': 'Nombre de la categoria...', 
      'name': 'name', 
      'type': 'text', 
      'class': 'form-control',
      'style': 'margin: 5px; width: 100%;',
    }))

  class Meta:
      model = Category
      fields = ('name',)