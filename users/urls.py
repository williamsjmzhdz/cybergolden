from django.urls import path

from . import views
from .API import views as api_views

app_name='users'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile, name='profile'),

    # API routes
    path('update/', api_views.update, name='update'),
]