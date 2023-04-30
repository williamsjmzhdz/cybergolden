import json
from django.http import HttpResponse, JsonResponse
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
        })
    
@login_required
def create_product(request):
        
    if request.method == 'GET':

        form = ProductForm()
        return render(request, 'products/create-product.html', {
            'form': form,
        })
    
    elif request.method == 'POST':
        
        if request.user.employee.position in STAFF:

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