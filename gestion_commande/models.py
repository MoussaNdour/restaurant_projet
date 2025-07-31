from django.conf import settings
from django.db import models
from gestion_menus_plats.models import Plat

class Commande(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'client'}
    )
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.client.email}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='lignes', on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.plat.nom} x {self.quantite}"
