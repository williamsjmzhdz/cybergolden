from django.urls import path

from maquila import views
#from maquila.API import views as api_views

app_name='maquila'

urlpatterns = [

    # Plantillas de cortes
    path('cuts/', views.cuts, name='cuts'),

]