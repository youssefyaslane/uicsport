from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Inscription

def afficher_form(request):
    return render (request,'formulaire.html')


def form(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        discipline = request.POST.get('discipline')

        # Vérifier si l'e-mail existe déjà
        if Inscription.objects.filter(email=email).exists():
            error_message = "This email is already in use. Please choose another."
            return render(request, 'signup.html', {'error_message': error_message})

        # Vérifier si le numéro existe déjà
        if Inscription.objects.filter(number=number).exists():
            error_message = "This number is already used. Please choose another."
            return render(request, 'signup.html', {'error_message': error_message})

        # Créez une instance du modèle Inscription avec les données du formulaire
        my_model_instance = Inscription(
            full_name=full_name,
            email=email,
            number=number,
            discipline=discipline
        )

        # Enregistrez l'instance du modèle dans la base de données
        try:
            my_model_instance.save()
            # Afficher un message de réussite si l'enregistrement a réussi
            print("Données enregistrées avec succès")
        except Exception as e:
            # Afficher un message d'erreur en cas d'échec de l'enregistrement
            print("Erreur lors de l'enregistrement des données :", str(e))

        return redirect('home2')

    return render(request, 'signup.html')