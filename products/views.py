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


