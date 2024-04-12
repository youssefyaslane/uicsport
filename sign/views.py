
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home(request):
    return render(request, 'Page_Home.html')


def formulaire(request):
    return render(request, 'formulaire.html')

def authentification(request):
    return render(request, 'authentification.html')

def team(request):
    return render(request, 'team.html')

def home1(request):
    return render(request, 'Page_Home1.html')
def home2(request):
    return render(request, 'Page_Home2.html')


# def signup(request):
#     return render(request, 'signup.html')

# Create your views here.
def Signup (request):
    if request.method=='POST' :
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('mdp')
         # Vérifier si l'email existe déjà
        if User.objects.filter(email=email).exists():
            error_message = "This email is already in use. Please choose another."
            return render(request, 'signup.html', {'error_message': error_message})

        # Vérifier si le nom d'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            error_message = "This username is already taken. Please choose another."
            return render(request, 'signup.html', {'error_message': error_message})
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return render (request,'signin.html')
    return render (request,'signup.html')
    
    


def Signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('mdp')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('home1')
        else:
            messages.error(request, "INCORRECT INFORMATIONS !!")
            return redirect('signin')

    return render(request, 'signin.html')