from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('admin', 'Admin'),
        ('cuisinier','Cuisinier'),
        ('serveur','Serveur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username
    
    @property
    def is_personnel(self):
        return self.role == 'personnel'
    
    @property
    def is_cuisinier(self):
        return self.role == 'cuisinier'
    
    @property
    def is_admin(self):
        return self.role=='admin'
    
    @property
    def is_serveur(self):
        return self.role=='admin'
    @property 
    def is_client(self):
        return self.role=='client'
    
