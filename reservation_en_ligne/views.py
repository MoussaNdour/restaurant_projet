from django.shortcuts import render, redirect
from .forms import ReservationForm, TableForm
from .models import Table, Reservation
from django.contrib.auth.decorators import login_required

@login_required
def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            table = reservation.table
            if table.disponible:
                reservation.save()
                table.disponible = False
                table.save()
                return render(request, 'reservation_en_ligne/confirmation.html', {'reservation': reservation})
            else:
                form.add_error('table', "Cette table n’est plus disponible.")
    else:
        form = ReservationForm()
    return render(request, 'reservation_en_ligne/reserver.html', {'form': form})

@login_required
def ajouter_table(request):
    if request.method == 'POST':
        if request.user.role=='client':
            return redirect('acceuil:index')
        else:
            form=TableForm(request.POST)
            if form.is_valid():
                table=form.save(commit=False)
                table.save()
                return render(request, 'reservation_en_ligne/ajouter_table.html', {'form': form})
    else:
        if request.user.role=='client':
            return redirect('acceuil:index')
        else:
            form=TableForm()
            return render(request, 'reservation_en_ligne/ajouter_table.html', {'form': form})
    

def reservations(request):
    reservations = Reservation.objects.select_related('client', 'table').order_by('-date_reservation')
    return render(request, 'reservation_en_ligne/reservations.html', {'reservations': reservations})

    
