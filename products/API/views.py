import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from products.models import Category


@require_http_methods(['POST'])
@login_required
def create_category(request):

    # Obtiene la información del formulario
    data = json.loads(request.body)
    name = data['name'].lower()

    # Revisa si la categoría ya existe
    if Category.objects.filter(name=name).exists():
        response_data = {'success': False, 'message': 'Ya existe una categoría con este nombre.'}
        return JsonResponse(response_data, status=409)

    # Crea una nueva categoría
    category = Category(name=name)
    category.save()

    response_data = {'success': True, 'message': 'Categoría creada exitosamente.'}
    return JsonResponse(response_data, status=201)