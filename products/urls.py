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

    # Plantillas de inventario
    path('inventory/', views.inventory, name='inventory'),
    path('create/inventory', views.create_inventory, name='create_inventory'),
    path('update/inventory/<int:inventory_id>', views.update_inventory, name='update_inventory'),


    # Rutas API para categorías
    path('api/create/category', api_views.create_category),
    path('api/delete/category', api_views.delete_category),
    path('api/update/category', api_views.update_category),

    # Rutas API para productos
    path('api/delete/product', api_views.delete_product),

    # Rutas API para inventarios
    path('api/delete/inventory', api_views.delete_inventory),
    path('api/get/products/inventory/<int:inventory_id>', api_views.get_products_inventory),
    path('api/update/product/stock', api_views.update_product_stock),
    #path('api/get/ordered/products/<str:order>/<int:inventory_id>', api_views.get_ordered_products_inventory),
]