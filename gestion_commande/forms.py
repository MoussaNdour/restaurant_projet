from django import forms
from .models import LigneCommande

class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['plat', 'quantite']
        widgets = {
            'plat': forms.Select(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
