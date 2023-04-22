from django.urls import path

from products import views
from products.API import views as api_views

app_name='products'

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('categories/update/category/<int:id>/', views.update_category, name='update_category'),
    path('categories/create/category/', views.create_category, name='create_category'),

    path('products/', views.products, name='products'),

    # API routes
    path('create/category', api_views.create_category),
    path('delete/category', api_views.delete_category),
    path('update/category', api_views.update_category),
]