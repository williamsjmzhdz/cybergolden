import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

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


@require_http_methods(['DELETE'])
@login_required
def delete_category(request):

    data = json.loads(request.body)
    category_id = data.get('id', None)

    if category_id is None:
        return JsonResponse({'success': False, 'message': 'El ID de la categoría es requerido.'}, status=400)

    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return JsonResponse({'success': True, 'message': f'La categoría "{category.name}" ha sido eliminada correctamente.'}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'error': f'La categoría con el ID "{category_id}" no existe.'}, status=404)
    

@require_http_methods(['PUT'])
@login_required
def update_category(request):
    data = json.loads(request.body)
    category_id = data.get('id', None)
    new_name = data.get('name', None)

    if not new_name or len(new_name.strip()) == 0:
        return JsonResponse({'success': False, 'message': 'El nombre de la categoría no puede estar vacío.'}, status=400)

    new_name = new_name.lower()

    # Buscar la categoría correspondiente
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'La categoría no existe.'}, status=404)

    # Verificar si el nombre ya existe en otra categoría
    if Category.objects.filter(name=new_name).exclude(pk=category_id).exists():
        return JsonResponse({'success': False, 'message': 'Ya existe una categoría con ese nombre.'}, status=400)

    # Verificar si el nuevo nombre es igual al nombre actual de la categoría
    if category.name == new_name:
        return JsonResponse({'success': False, 'message': 'El nombre de la categoría no ha cambiado.'}, status=200)

    # Actualizar el nombre de la categoría
    category.name = new_name
    category.save()

    return JsonResponse({'success': True, 'message': 'La categoría se actualizó correctamente.'}, status=200)

