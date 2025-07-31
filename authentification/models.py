from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('personnel', 'Personnel'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username
    
    @property
    def is_personnel(self):
        return self.role == 'personnel'
    
    @property
    def is_client(self):
        return self.role == 'client'
    
