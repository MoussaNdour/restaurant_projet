from django.shortcuts import render, redirect, get_object_or_404
from .models import Commande, LigneCommande
from .forms import LigneCommandeForm
from django.contrib.auth.decorators import login_required
from .utils import render_to_pdf, envoyer_facture_email


def passer_commande(request):
    if request.method == 'POST':
        form = LigneCommandeForm(request.POST)
        if form.is_valid():
            commande = Commande.objects.create(client=request.user)
            ligne = form.save(commit=False)
            ligne.commande = commande
            ligne.save()
            return redirect('accueil:index')
    else:
        form = LigneCommandeForm()
    
    return render(request, 'gestion_commande/commander.html', {'form': form})

def commandes(request):
    commandes=Commande.objects.all()

    return render(request,'gestion_commande/commandes.html', {'commandes':commandes})





@login_required
def valider_commande(request):
    commande_en_cours = Commande.objects.filter(client=request.user, statut='en_cours').first()
    commandes_validees = Commande.objects.filter(client=request.user, statut='validee').order_by('-date_commande')

    if request.method == 'POST' and commande_en_cours:
        commande_en_cours.statut = 'validee'
        commande_en_cours.save()

        # Génération du PDF
        context = {'commande': commande_en_cours}
        pdf_bytes = render_to_pdf('gestion_commande/facture_pdf.html', context)

        # Envoi de l'e-mail
        envoyer_facture_email(
            to_email=request.user.email,
            sujet=f"Facture Commande #{commande_en_cours.id}",
            message="Merci pour votre commande. Vous trouverez la facture en pièce jointe.",
            pdf_bytes=pdf_bytes,
            nom_pdf=f"facture_{commande_en_cours.id}.pdf"
        )

        return render(request, 'gestion_commande/paiement.html', {
            'montant': commande_en_cours.calculer_total()
        })

    return render(request, 'gestion_commande/mes_commandes.html', {
        'commande': commande_en_cours,
        'commandes_validees': commandes_validees
    })


def changer_etat_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    if request.method == 'POST':
        nouvel_etat = request.POST.get('etat')
        if nouvel_etat in dict(Commande.STATUT_CHOICES):
            commande.etat = nouvel_etat
            commande.save()
    return redirect('gestion_commande:valider')

def paiement(request):
    if request.method=="POST":
        message = ""
    

    if request.method == 'POST':
        methode = request.POST.get('methode')
        if methode == 'orange_money':
            message = "Paiement confirmé via Orange Money."
        elif methode == 'wave':
            message = "Paiement confirmé via Wave."
        else:
            message = "Méthode de paiement non reconnue."

    return render(request, 'paiement.html', {'message': message})