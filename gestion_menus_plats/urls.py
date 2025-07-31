from django.urls import path
from . import views

app_name = 'gestion_menus_plats'

urlpatterns = [
    path('plats/', views.plats, name='plats'),
    path('ajouter_plat/', views.ajouter_plat, name='ajouter_plat'),
]
