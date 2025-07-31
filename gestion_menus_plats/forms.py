from django import forms
from .models import Plat

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['nom', 'description', 'categorie', 'prix', 'est_epuise', 'est_specialite', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'prix': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
