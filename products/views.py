from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from products.forms import CategoryForm
from products.models import Category


@login_required
def categories(request):

    categories = Category.objects.all()

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:categories')
        
    return render(request, 'products/categories.html', {
        'categories': categories,
        'form': form
    })

