from django.shortcuts import render
from gestion_menus_plats.models import Plat
from gestion_commande.models import Commande, LigneCommande
from django.shortcuts import get_object_or_404,redirect
from authentification.models import CustomUser
from authentification.forms import CreationPersonnel 


def index(request):
    plats=Plat.objects.all()
    if request.user.is_authenticated:
        user=request.user
    else:
        user=None
    return render(request, 'accueil/index.html',{'plats':plats,'user':user})


def ajouter_plat_commande(request, nom_plat):
    plat = get_object_or_404(Plat, nom=nom_plat)

    # chercher commande en cours de l'utilisateur
    commande, created = Commande.objects.get_or_create(
        client=request.user,
        statut='en_cours'
    )

    # vérifier si le plat est déjà dans la commande
    ligne, created = LigneCommande.objects.get_or_create(
        commande=commande,
        plat=plat,
        defaults={'quantite': 1}
    )
    if not created:
        ligne.quantite += 1
        ligne.save()

    return redirect('accueil:index')

def personnel(request):
    form=CreationPersonnel()
    personnel = CustomUser.objects.filter(role__in=['cuisinier', 'serveur'])
    return render(request, "accueil/personnel.html",{'personnel':personnel, 'form':form})

def creation_personnel(request):
    if request.method == 'POST':
        form = CreationPersonnel(request.POST)
        if form.is_valid():
            personnel=form.save()
            return redirect('accueil:personnel')

def supprimer_personnel(request, user_id):
    if request.method == 'POST':  # Sécurise la suppression avec POST
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
    return redirect('accueil:personnel')  # Redirige vers la page du personnel

    