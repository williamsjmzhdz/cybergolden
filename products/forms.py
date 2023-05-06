from django import forms
from products.models import Category, Product, Inventory, SIZES, SIZES_BY_AGE


class CategoryForm(forms.ModelForm):
  '''
  Form that handle category creation.
  '''

  class Meta:
      model = Category
      fields = ('name',)

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


class ProductForm(forms.ModelForm):
    '''
    Form that handle product creation.
    '''

    class Meta:
        model = Product
        fields = ['name', 'category', 'production_cost', 'logistics_cost', 'minimum_stock', 'size']

    name = forms.CharField(label='', max_length=100, required=True, 
      widget=forms.TextInput(attrs={
        'placeholder': 'Nombre del producto...', 
        'name': 'name', 
        'type': 'text', 
        'class': 'form-control',
        'id': 'name',
      })
    )

    category = forms.ModelChoiceField(
        label='', 
        queryset=Category.objects.all(), 
        required=True, 
        widget=forms.Select(
            attrs={
                'placeholder': 'Seleccione una categoría', 
                'name': 'category', 
                'class': 'form-control',
                'id': 'category',
            },
            choices=[(category.id, category.name) for category in Category.objects.all()],
        ),
        initial=Category.objects.first(),
    )

    production_cost = forms.DecimalField(
        label='',
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese el costo de producción/compra',
                'name': 'production_cost',
                'class': 'form-control',
                'id': 'production_cost',
                'step': '0.01',
                'min': '0',
            },
        ),
    )

    logistics_cost = forms.DecimalField(
        label='',
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese el costo de logística',
                'name': 'logistic_cost',
                'class': 'form-control',
                'id': 'logistic_cost',
                'step': '0.01',
                'min': '0',
            },
        ),
    )



    minimum_stock = forms.IntegerField(
        label='', 
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese el mínimo de stock para enviar una alerta...',
                'class': 'form-control',
                'name': 'minimum-stock',
                'id': 'minimum-stock',
                'step': '1',
                'min': '0',
            },
        ),
    )

    size_choices = [
        ('Sin talla', [('Sin talla', 'Sin talla')]),
        ('Tallas', [size for size in SIZES]),
        ('Tallas por edad', [size for size in SIZES_BY_AGE])
    ]
    size = forms.ChoiceField(
            label='', 
            choices=size_choices, 
            required=False,
            widget=forms.Select(
                attrs={
                    'class': 'form-control',
                    'name': 'size',
                    'id': 'size',
                },
            ),
        )


class InventoryForm(forms.ModelForm):
  '''
  Form that handle inventory creation.
  '''

  class Meta:
      model = Inventory
      fields = ('name',)

  name = forms.CharField(max_length=100, required=True, label='',
    widget=forms.TextInput(attrs={
      'placeholder': 'Nombre del inventario...', 
      'name': 'name', 
      'type': 'text', 
      'class': 'form-control',
      'id': 'name',
      'style': 'margin: 5px; width: 100%;',
    }),
    error_messages={
      'unique': 'Ya existe un inventario con este nombre. Por favor ingrese otro nombre.'
    })