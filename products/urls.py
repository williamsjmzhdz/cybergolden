from django.urls import path

from . import views
from .API import views as api_views

app_name='products'

urlpatterns = [
    path('categories/', views.categories, name='categories'),

    # API routes
]