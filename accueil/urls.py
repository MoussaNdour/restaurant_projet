from django.urls import path
from . import views

app_name = 'accueil'

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter_plat_commande/<str:nom_plat>',views.ajouter_plat_commande, name="ajouter_plat"),
    path('personnel', views.personnel, name="personnel"),
    path('personnel/creation_personnel', views.creation_personnel, name='creation_personnel'),
    path('personnel/supprimer_personnel/<int:user_id>', views.supprimer_personnel, name="supprimer_personnel")
]
