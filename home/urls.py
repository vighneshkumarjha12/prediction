from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('Signup', views.SignUp, name="handleSignUp"),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'), 
    path('predict', views.predict, name='predict'),
    path('info', views.info, name='information'),
    path('into', views.into, name='prediction'),
    path('sqa', views.sqa, name='sqa'),
    path('normal', views.normal, name='normal'),
    path('adeno', views.adeno, name='adeno'),
]
