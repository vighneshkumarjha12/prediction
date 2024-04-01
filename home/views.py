from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
# Correct import statement in views.py
from django.contrib.auth import logout, authenticate, login 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import User
from django.contrib.auth.views import PasswordResetView
from django.core.files.storage import FileSystemStorage

from datetime import date
import math
from django.core.files.storage import default_storage

import tensorflow as tf

import numpy as np

def SignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
       return render(request, 'signup.html')
    return render(request, 'login.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.error(request,"")
        
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/Signup") 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')


    
def predict(request):
   

    return render(request, 'predict.html')

   
def info(request):

    return render(request, 'info.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 

def forgot_password(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
       
        print(username)

        # check if user has entered correct credentials
        user = authenticate(username=username)

        if user is not None:
            passw=request.POST['passw']
            ruser= User.objects.create_user(passw)
            # A backend authenticated the credentials
            login(request, user)
            messages.error(request, "No account found with this username and password.")
        
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'forgot_password.html')

    return render(request, 'forgot_password.html')