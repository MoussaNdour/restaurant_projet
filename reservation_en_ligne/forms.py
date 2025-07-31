from django import forms
from .models import Reservation, Table
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date_prevue']
        widgets = {
            'table': forms.Select(attrs={'class': 'form-select'}),
            'date_prevue': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local', 
                }
            ),
        }

    def clean_date_prevue(self):
        date = self.cleaned_data['date_prevue']
        if date <= timezone.now():
            raise forms.ValidationError("La date prévue doit être dans le futur.")
        return date

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['numero','nombre_de_places','disponible']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': ''}),
            'nombre_de_place': forms.NumberInput(attrs={'class':''}),
            'disponible':forms.CheckboxInput(attrs={'class':''})
        }
