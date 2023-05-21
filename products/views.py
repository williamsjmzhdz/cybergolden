import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from products.forms import CategoryForm, ProductForm, InventoryForm
from products.models import Category, Product, Inventory, Stock


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
@csrf_exempt
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

                product = form.save()

                inventories = Inventory.objects.all()
                for inventory in inventories:
                    Stock.objects.create(inventory=inventory, product=product, stock=0)

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
@csrf_exempt
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
@login_required
def inventory(request):

    inventory_id = request.GET.get('inventory_id', None)

    if inventory_id is not None:
        try:
            # Convertir inventory_id a int
            inventory_id = int(inventory_id)
            # Obtener el inventario con el id especificado
            specified_inventory = Inventory.objects.get(id=inventory_id)
            # Obtener todos los inventarios excepto el especificado
            other_inventories = Inventory.objects.exclude(id=inventory_id)
            # Combinar los inventarios en la lista deseada
            inventories = [specified_inventory] + list(other_inventories)
        except (Inventory.DoesNotExist, ValueError):
            # Si no se encuentra el inventario con el id especificado o si inventory_id no es un número,
            # simplemente obtener todos los inventarios
            inventories = Inventory.objects.all()
    else:
        # Si no se especifica un id de inventario, simplemente obtener todos los inventarios
        inventories = Inventory.objects.all()

    return render(request, 'products/inventory.html', {
        'inventories': inventories,
    })


@login_required
@csrf_exempt
def create_inventory(request):

    if request.user.employee.position in STAFF:
        
        if request.method == 'GET':

            return render(request, 'products/create-inventory.html', {
                'form': InventoryForm()
            })
        
        elif request.method == 'POST':
                        
            form = InventoryForm(request.POST)

            if form.is_valid():

                inventory = form.save()

                products = Product.objects.all()
                for product in products:
                    Stock.objects.create(inventory=inventory, product=product, stock=0)

                return redirect('products:inventory')
            
            else:
                
                return render(request, 'products/create-inventory.html', {
                    'form': form,
                    'message': 'Ya existe un inventario con este nombre. Por favor ingrese otro nombre.',
                })
        
    else:

        return redirect('products:inventory')


@login_required
@csrf_exempt
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

@login_required
@csrf_exempt
def update_inventory(request, inventory_id):

    if request.user.employee.position in STAFF:

        inventory = Inventory.objects.get(id=inventory_id)

        if request.method == 'GET':

            form = InventoryForm(instance=inventory)

            return render(request, 'products/update-inventory.html', {
                'form': form,
                'inventory': inventory,
            })
        
        if request.method == 'POST':

            form = InventoryForm(request.POST, instance=inventory)

            if form.is_valid():

                form.save()

                return redirect(reverse('products:inventory') + '?inventory_id=' + str(inventory_id))
            
            else:

                errors = json.loads(form.errors.as_json())

                message = ''

                for field, field_errors in errors.items():
                    message += f'{field}: {field_errors[0]["message"]}\n'

                return render(request, 'products/update-inventory.html', {
                    'form': form,
                    'message': message,
                })

    else:

        return redirect('products:inventory')


    return render(request, 'products/update-inventory.html')