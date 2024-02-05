from django.shortcuts import render
from django.http import HttpResponseRedirect
from Trombinoscoop.forms import *
from Trombinoscoop.models import *
from datetime import datetime, date


def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        
        #on cherche un étudiant
        if len(Etudiant.objects.filter( id= logged_user_id ))==1:
            return Etudiant.objects.get(id=logged_user_id)
        
        #On cherche un employe
        elif len(Employe.objects.filter(id=logged_user_id)) == 1:
            return Employe.objects.get(id= logged_user_id)
        
        #si on a rien trouvé
        else:
            return None
    else:
        return None


def welcome(request):
    logged_user= get_logged_user_from_request(request)
    if not logged_user is None:
        if 'newMessage' in request.GET and request.GET['newMessage'] != '':
            newMessage= Message(auteur=logged_user, contenu=request.GET['newMessage'], date_de_publication=date.today())
            newMessage.save()

        friendMessages = Message.objects.filter(auteur__amis=logged_user).order_by('-date_de_publication')

        return render(request, 'welcome.html', {'logged_user': logged_user, 'friendMessages': friendMessages})
    
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
    
def add_friend(request):
    logged_user= get_logged_user_from_request(request)
    if logged_user:
        #On test si le formulaire a été envoyé
        if len(request.GET)>0:
            form= addFriendForm(request.GET)

            if form.is_valid():
                new_friend_email = form.cleaned_data['email']
                newFriend = Personne.objects.get(courriel= new_friend_email)
                logged_user.amis.add(newFriend)
                logged_user.save()
                return HttpResponseRedirect('/welcome') 
            
            else:
                return render(request, 'addFriend.html', {'form': form})

        #si le formulaire n'a pas été envoyé
        else:
            form = addFriendForm()
            return render(request, 'addFriend.html', {'form': form})
        
    else:
        return HttpResponseRedirect('/')
    
def show_profile(request):
    logged_user= get_logged_user_from_request(request)
    if logged_user:
        #Test si le paramètre passé existe et est bien passé
        if 'userToShow' in request.GET and request.GET['userToShow'] != '':
            results= Personne.objects.filter(id=request.GET['userToShow'])
            if len(results) == 1:
                if Etudiant.objects.filter(id=request.GET['userToShow']):
                    user_to_show= Etudiant.objects.get(id=request.GET['userToShow'])
                else:
                    user_to_show= Employe.objects.get(id=request.GET['userToShow'])
                
                return render(request, 'show_profile.html', {'user_to_show': user_to_show})
            else:
                return (request, 'show_profile.html', {'user_to_show': logged_user})
        #le paramètre n'a pas été trouvé
        else:
            return render(request, 'show_profile.html', {'user_to_show': logged_user})
        
    else:
        return HttpResponseRedirect("")
    
def modify_profile(request):
    logged_user= get_logged_user_from_request(request)
    if logged_user:
        if len(request.GET)>0:
            if type(logged_user) == Etudiant:
                form = StudentProfileForm(request.GET, instance=logged_user)
            else:
                form= EmployeeProfileForm(request.GET, instance=logged_user)

            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect('/welcome')
            else:
                return render (request, 'modify_profile.html', {'form': form})
            
        else:
            if type(logged_user) == Etudiant:
                form= StudentProfileForm(instance=logged_user)
            else:
                form= EmployeeProfileForm(instance= logged_user)
            
            return render(request, 'modify_profile.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')