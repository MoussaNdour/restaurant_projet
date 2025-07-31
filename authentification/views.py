from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect('accueil:index')  # ou la page de connexion
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentification/inscription.html', {'form': form})

def index(request):
    context = {
        'range_6_to_15': range(6, 16),  # 16 exclus
    }
    return render(request, 'index.html', context)



from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def connexion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie. Bienvenue !")

            # Rediriger vers la page précédente si ?next= existe
            next_url = request.GET.get('reservation:reserver')
            return redirect(next_url) if next_url else redirect('accueil:index')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'authentification/connexion.html', {'form': form})




def deconnexion(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('authentification:connexion')
    

