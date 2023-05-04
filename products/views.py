import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from products.forms import CategoryForm, ProductForm
from products.models import Category, Product


STAFF = ['CEO', 'COO']

# Plantillas de categorías
@login_required
def categories(request):

    if request.method == 'GET':

        categories = Category.objects.all()

        # Capitalizar el campo 'name' de cada objeto Category
        for category in categories:
            category.name = category.name.capitalize()

        return render(request, 'products/categories.html', {
            'categories': categories,
            'is_staff': request.user.employee.position in STAFF,
        })  
    
@login_required
def create_category(request):
        
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'products/create-category.html', {
            'form': form,
        })

@login_required
def update_category(request, id):

    if request.user.employee.position in STAFF:

        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return HttpResponse(status=404)
            
        if request.method == 'GET':
            form = CategoryForm(instance=category)
            return render(request, 'products/update-category.html', {
                'form': form,
                'category_id': id,
            })
    
    else:

        return redirect('products:categories')


# Plantillas de productos
@login_required
def products(request):

    if request.method == 'GET':
        products = Product.objects.all()

        return render(request, 'products/products.html', {
            'products': products,
            'is_staff': request.user.employee.position in STAFF,
            'is_sell_agent': request.user.employee.position == 'SA',
            'is_maquila_operator': request.user.employee.position == 'MO', 
        })
    
@login_required
def create_product(request):

    if request.user.employee.position in STAFF:
        
        if request.method == 'GET':

            form = ProductForm()
            return render(request, 'products/create-product.html', {
                'form': form,
            })
        
        elif request.method == 'POST':
                        
            form = ProductForm(request.POST)

            if form.is_valid():

                form.save()
                return redirect('products:products')
            
            else:
                
                errors = json.loads(form.errors.as_json())
                message = ''
                for field, field_errors in errors.items():
                    message += f'{field}: {field_errors[0]["message"]}\n'
                return render(request, 'products/create-product.html', {
                    'form': form,
                    'message': message,
                })
        
    else:

        return redirect('products:products')
            
@login_required
def update_product(request, product_id):

    if request.user.employee.position in STAFF:
        
        product = Product.objects.get(id=product_id)

        if request.method == 'GET':

            form = ProductForm(instance=product)

            return render(request, 'products/update-product.html', {
                'form': form,
                'product': product,
            })
        
        elif request.method == 'POST':

            form = ProductForm(request.POST, instance=product)

            if form.is_valid():
                form.save()
                return redirect('products:products')
            else:
                errors = json.loads(form.errors.as_json())
                message = ''
                for field, field_errors in errors.items():
                    message += f'{field}: {field_errors[0]["message"]}\n'
                return render(request, 'products/update-product.html', {
                    'form': form,
                    'message': message,
                })
    
    else:

        return redirect('products:products')
    

# Plantillas de inventario
def inventory(request):
    return render(request, 'products/inventory.html')