from django.conf import settings
from django.db import models

class Table(models.Model):
    numero = models.IntegerField(unique=True)
    nombre_de_places = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.numero} - {self.nombre_de_places} places"

class Reservation(models.Model):
    ETAT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ]

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'client'}
    )
    table = models.ForeignKey('Table', on_delete=models.CASCADE)

    date_reservation = models.DateTimeField(auto_now_add=True)  
    date_prevue = models.DateTimeField(null=True, blank=True) 

    etat = models.CharField(
        max_length=20,
        choices=ETAT_CHOICES,
        default='en_attente',
    )

    def __str__(self):
        return f"{self.client.email} - Table {self.table.numero} - {self.date_prevue.strftime('%d/%m/%Y %H:%M')} ({self.get_etat_display()})"
