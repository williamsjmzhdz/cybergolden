from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def inventory(request):

    return render(request, 'products/inventory.html')