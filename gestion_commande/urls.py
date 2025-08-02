from django.urls import path
from . import views

app_name = 'commandes'

urlpatterns = [
    path('commander/', views.passer_commande, name='passer_commande'),
    path('commandes',views.commandes,name='commandes'),
    path('valider/', views.valider_commande, name='valider_commande'),
    path('commandes/changer-etat/<int:commande_id>/', views.changer_etat_commande, name='changer_etat'),
    path('paiement/', views.paiement, name="paiement")
]
