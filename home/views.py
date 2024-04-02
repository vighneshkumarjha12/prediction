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
import statistics
from datetime import date
import math
from django.core.files.storage import default_storage

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import tensorflow.keras
import cmath
from tensorflow.keras.models import load_model
import numpy as np
from datetime import date
import math
from django.core.files.storage import default_storage


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
    return render(request, 'predict.html')

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')



def predict(request):
    a=request.FILES['img']
    model = load_model("static/model/model.hdf5")
    classes_dir = [1,2,3]
    file_name="pic.jpg"
    file_name2=default_storage.save(file_name,a)
    file_url=default_storage.url(file_name2)
    img = image.load_img(file_url, target_size=(350,350))
    norm_img = image.img_to_array(img)/255
    input_arr_img = np.array([norm_img])
    pred = np.argmax(model.predict(input_arr_img))
    print(model.predict(input_arr_img))
    print(classes_dir[pred])
    m=classes_dir[pred]
    if(m==1):
         return render(request,'adeno.html',{'num': m})
    elif(m==3):
        return render(request,'sqa.html',{'num': m})
    else:
        return render(request,'normal.html',{'num': m})
    
    




 
   
   
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