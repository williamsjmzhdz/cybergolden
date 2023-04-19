from django.urls import path

from . import views
from .API import views as api_views

app_name='products'

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),

    # API routes
]