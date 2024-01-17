from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime

def welcome(request):
    return render(request, 'welcome.html', {'current_datetime': datetime.now})

def login(request):
    #on test si le formulaire à bien été envoyé
    if len(request.POST)>0:
        #on test pour s'assurer que tous les pramètres ont bien été transmis
        if 'email' not in request.POST or 'password' not in request.POST:
            error="Courriel ou mot de passe non renseigné ..."
            return render('login.html', {'error': error})
        else:
            email=request.POST['email']
            password=request.POST['password']
            
            #on test pour s'assurer que le mot de passe est le bon
            if(password != 'sesame' or email != 'pierre@gmail.com'):
                error="Adresse de courriel ou mot de passe erroné"
                return render('login.html', {'error': error})
            
            #si tout est bon on se rend alors à la page d'accueil
            else:
                return HttpResponseRedirect('welcome')
    else:
        return render(request, 'login.html')