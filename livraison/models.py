from django.db import models

class Adresse(models.Model):
    nom_client = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_client} - {self.adresse}"

class Livreur(models.Model):
    nom = models.CharField(max_length=100)
    position_lat = models.FloatField(null=True, blank=True)
    position_long = models.FloatField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
