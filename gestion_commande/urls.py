from django.urls import path
from . import views

app_name = 'commandes'

urlpatterns = [
    path('commander/', views.passer_commande, name='passer_commande'),
    path('commandes',views.commandes,name='commandes')
]
