from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.forms import CategoryForm
from products.models import Category


@login_required
def categories(request):

    if request.method == 'GET':

        categories = Category.objects.all()

        # Capitalizar el campo 'name' de cada objeto Category
        for category in categories:
            category.name = category.name.capitalize()

        form = CategoryForm()

        return render(request, 'products/categories.html', {
            'categories': categories,
            'form': form
        })  

@login_required
def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
        
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'products/edit-category.html', {
            'form': form,
            'category_id': id,
        })
