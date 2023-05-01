import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from products.models import Category, Product


STAFF = ['CEO', 'COO']

@csrf_exempt
@require_http_methods(['POST'])
@login_required
def create_category(request):

    if request.user.employee.position in STAFF:

        # Obtiene la información del formulario
        data = json.loads(request.body)
        name = data['name'].lower()

        # Revisa si recibió una cadena vacía
        if not name or len(name.strip()) == 0:
            return JsonResponse({'success': False, 'message': 'El nombre de la categoría no puede estar vacío.'}, status=400)

        # Revisa si la categoría ya existe
        if Category.objects.filter(name=name).exists():
            response_data = {'success': False, 'message': 'Ya existe una categoría con este nombre.'}
            return JsonResponse(response_data, status=409)

        # Crea una nueva categoría
        category = Category(name=name)
        category.save()

        response_data = {'success': True, 'message': 'Categoría creada exitosamente.'}
        return JsonResponse(response_data, status=201)
    
    else:
        return JsonResponse({'success': False, 'message': 'No tienes los permisos necesarios para eliminar categorías.'}),


@csrf_exempt
@require_http_methods(['DELETE'])
@login_required
def delete_category(request):

    if request.user.employee.position in STAFF:

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
        
    else:
        return JsonResponse({'success': False, 'message': 'No tienes los permisos necesarios para eliminar categorías.'}),
    

@csrf_exempt
@require_http_methods(['PUT'])
@login_required
def update_category(request):

    if request.user.employee.position in STAFF:

        data = json.loads(request.body)
        category_id = data.get('id', None)
        new_name = data.get('name', None)

        # Revisa si recibió una cadena vacía
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

    else:
        return JsonResponse({'success': False, 'message': 'No tienes los permisos necesarios para actualizar categorías.'}),

@csrf_exempt
@require_http_methods(['DELETE'])
@login_required
def delete_product(request):

    if request.user.employee.position in STAFF:

        data = json.loads(request.body)
        product_id = data.get('id', None)

        if product_id is None:
            return JsonResponse({'success': False, 'message': 'El ID del producto es requerido.'}, status=400)

        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'success': True, 'message': f'El producto "{product.name}" ha sido eliminado correctamente.'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'error': f'El producto con el ID "{product_id}" no existe.'}, status=404)
        
    else:
        return JsonResponse({'success': False, 'message': 'No tienes los permisos necesarios para eliminar productos.'}),
    