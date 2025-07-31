from django.urls import path
from . import views
app_name = 'livraison'
urlpatterns = [
    path('carte/', views.carte_livraison, name='carte_livraison'),
    path('ajouter/', views.ajouter_adresse, name='ajouter'),
    
]
