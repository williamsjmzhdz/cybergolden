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
    path('', views.products, name='products'),
    path('create/product/', views.create_product, name='create_product'),
    path('update/product/<int:product_id>/', views.update_product, name='update_product'),

    # Rutas API para categorías
    path('api/create/category', api_views.create_category),
    path('api/delete/category', api_views.delete_category),
    path('api/update/category', api_views.update_category),

    # Rutas API para productos
    path('api/delete/product', api_views.delete_product),
]