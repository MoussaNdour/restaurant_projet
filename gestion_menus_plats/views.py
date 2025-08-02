from django.shortcuts import render,redirect
from .models import Plat
from .forms import PlatForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def plats(request):
    plats = Plat.objects.all()
    categories = [
        ('entree', 'Entrées'),
        ('plat_resistant', 'Plats Résistants'),
        ('dessert', 'Desserts'),
    ]
    return render(request, 'gestion_menus_plats/plats.html', {'plats': plats,'categories':categories})

@login_required
def ajouter_plat(request):
    if request.user.role not in ['cuisinier','admin','serveur']:
        raise PermissionDenied("Accès réservé au personnel.")
    
    if request.method == 'POST':
        form = PlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion_menus_plats:ajouter_plat')
    else:
        form = PlatForm()

    return render(request, 'gestion_menus_plats/ajouter.html', {'form': form})

@login_required
def gestion_plat(request, nom_plat):
    plat=Plat.filter(nom=nom_plat)
    return render(request,'gestion_plat.html')