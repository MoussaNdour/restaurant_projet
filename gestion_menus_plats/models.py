from django.db import models

class Plat(models.Model):
    CATEGORIES = [
        ('entree', 'Entrée'),
        ('plat_resistant', 'Plat résistant'),
        ('dessert', 'Dessert'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='plat_resistant')
    prix = models.DecimalField(max_digits=6, decimal_places=2, default=5000)
    est_epuise = models.BooleanField(default=False)
    est_specialite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='plats/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.get_categorie_display()})"
