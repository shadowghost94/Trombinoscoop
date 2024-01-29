from django.shortcuts import render
from django.http import HttpResponseRedirect
from Trombinoscoop.forms import *
from datetime import datetime

def welcome(request):
    return render(request, 'welcome.html', {'current_datetime': datetime.now})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/welcome')
        else:
            return HttpResponseRedirect("/")
        
    else:
        form = LoginForm()
        return render(request,'login.html', {'form': form })
        
    
def register(request):
    if len(request.GET)>0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save(commit=True)
                return HttpResponseRedirect('/login')
            
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