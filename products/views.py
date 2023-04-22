from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.forms import CategoryForm
from products.models import Category, Product


@login_required
def categories(request):

    if request.method == 'GET':

        categories = Category.objects.all()

        # Capitalizar el campo 'name' de cada objeto Category
        for category in categories:
            category.name = category.name.capitalize()

        return render(request, 'products/categories.html', {
            'categories': categories,
        })  

@login_required
def update_category(request, id):
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
    
@login_required
def create_category(request):
        
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'products/create-category.html', {
            'form': form,
        })


@login_required
def products(request):

    if request.method == 'GET':
        products = Product.objects.all()

        return render(request, 'products/products.html', {
            'products': products,
        })  