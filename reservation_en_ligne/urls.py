from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('reserver/', views.reserver, name='reserver'),
    path('ajouter_table',views.ajouter_table,name='ajouter_table'),
    path('reservations', views.reservations, name='reservations')
]
