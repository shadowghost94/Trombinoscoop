from django.shortcuts import render
from django.http import HttpResponseRedirect
from Trombinoscoop.forms import *
from Trombinoscoop.models import *
from datetime import datetime

def welcome(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Personne.objects.get(id=logged_user_id)

        return render(request, 'welcome.html', {'logged_user': logged_user})
    else:
        return HttpResponseRedirect("")

def login(request):
    #lecture de la valeur d'une session
    #langue_choisie= request.session['langue']

    #Changement de la valeur d'une variable de session
    #request.session['langue']= 'fr'

    #Supression d'une variable de session
    #del request.session['langue']

    #verification de la présence d'une varibale de session
    #if 'langue' in request.session:

    #on test si le formulaire a été envoyé
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email= form.cleaned_data['email']
            logged_user= Personne.objects.get(courriel= user_email)
            request.session['logged_user_id']= logged_user.id

            return HttpResponseRedirect('/welcome')
        
    else:
        form = LoginForm()
        return render(request,'login.html', {'form': form })
        
    
def register(request):
    if len(request.GET)>0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")

        #si1
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")

            #si2
            if studentForm.is_valid():
                studentForm.save(commit=True)
                return HttpResponseRedirect("/")
            #sinon2
            else:
                return HttpResponseRedirect('/welcome')

        #sinon1    
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.GET, prefix="em")

            if employeeForm.is_valid():
                employeeForm.save(commit=True)
                return HttpResponseRedirect('/login')
            
        #si le formlaire n'est pas validé
        return render(request, 'user_profile.html', {
            'studentForm': studentForm,
            'employeeForm': employeeForm
        })
        
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        return render(request, 'user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})