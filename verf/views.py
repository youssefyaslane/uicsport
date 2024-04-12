
from django.utils import timezone
from .models import Reservation,Terrain
from django.shortcuts import render,HttpResponse,redirect

def reservation(request):
    return render(request, 'reservation.html')

def verifier_disponibilite(terrain, date_debut, date_fin):
    reservations = Reservation.objects.filter(
        terrain=terrain,
        date_heure_debut__lt=date_fin,
        date_heure_fin__gt=date_debut
    )
    return not reservations.exists()

def reservation(request):
    if request.method == 'POST':
        terrain = request.POST.get('terrain')
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')

        terrain_obj = Terrain.objects.get(nom=terrain)

        disponible = verifier_disponibilite(terrain_obj, date_debut, date_fin)

        if disponible:
            # Effectuer la réservation
            Reservation.objects.create(
                terrain=terrain_obj,
                date_heure_debut=date_debut,
                date_heure_fin=date_fin
            )
            message = "YOUR RESERVATION HAS BEEN CONFIRMED"
        else:
            message = "THE STADIUM IS NOT AVALABLE AT THIS TIME"

        # Ajouter la liste des terrains pour réafficher le formulaire de réservation
        terrains = Terrain.objects.all()
        return render(request, 'reservation.html', {'terrains': terrains, 'message': message})

    terrains = Terrain.objects.all()
    return render(request, 'reservation.html', {'terrains': terrains})