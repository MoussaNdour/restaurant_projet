from django.shortcuts import render, redirect
from .models import Adresse, Livreur
from .forms import AdresseForm

def carte_livraison(request):
    adresses = Adresse.objects.all()
    livreurs = Livreur.objects.all()
    return render(request, 'livraison/carte.html', {
        'adresses': adresses,
        'livreurs': livreurs,
        'google_maps_api_key': 'VOTRE_CLE_API_ICI'
    })

def ajouter_adresse(request):
    if request.method == 'POST':
        form = AdresseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livraison:carte_livraison')
    else:
        form = AdresseForm()
    return render(request, 'livraison/ajouter_adresse.html', {'form': form})


