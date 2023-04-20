from django import forms
from products.models import Category


class CategoryForm(forms.ModelForm):
  '''
  Form that handle categories creation.
  '''

  name = forms.CharField(max_length=100, required=True, label='',
    widget=forms.TextInput(attrs={
      'placeholder': 'Nombre de la categoria...', 
      'name': 'name', 
      'type': 'text', 
      'class': 'form-control',
      'id': 'name',
      'style': 'margin: 5px; width: 100%;',
    }),
    error_messages={
      'unique': 'Ya existe una categoría con este nombre. Por favor ingrese otro nombre.'
    })

  class Meta:
      model = Category
      fields = ('name',)

