from django.urls import path

from products import views
from products.API import views as api_views

app_name='products'

urlpatterns = [

    # Plantillas de categorías
    path('categories/', views.categories, name='categories'),
    path('categories/create/category/', views.create_category, name='create_category'),
    path('categories/update/category/<int:id>/', views.update_category, name='update_category'),

    # Plantillas de productos
    path('products/', views.products, name='products'),
    path('categories/create/product/', views.create_product, name='create_product'),

    # Rutas API para categorías
    path('create/category', api_views.create_category),
    path('delete/category', api_views.delete_category),
    path('update/category', api_views.update_category),

]