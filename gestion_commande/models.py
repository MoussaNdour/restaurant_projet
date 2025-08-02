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
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('validee', 'Validée'),
        ('annulee', 'Annulée'),
        ('livree', 'Livrée'),
    ]
    etat = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')

    def __str__(self):
        return f"Commande #{self.id} - {self.client.email}"
    
    def get_etat_badge_class(self):
        return {
            'en_attente': 'secondary',
            'en_cours': 'warning',
            'livree': 'success',
            'annulee': 'danger',
        }.get(self.etat, 'secondary')
    def calculer_total(self):
        return sum(ligne.plat.prix * ligne.quantite for ligne in self.lignes.all())

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='lignes', on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.plat.nom} x {self.quantite}"
