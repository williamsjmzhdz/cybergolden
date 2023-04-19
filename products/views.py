from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def categories(request):

    return render(request, 'products/categories.html')