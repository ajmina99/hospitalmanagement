"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views
appname="app1"

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('department/',views.department,name="department"),
    path('viewdoctor/',views.vdoctor,name="view_doctor"),
path('adddoctor/',views.adoctor,name="add_doctor"),
path('addpatient/',views.addpatient,name="add_patient"),
path('viewpatient/',views.viewpatient,name="view_patient"),
path('contact/',views.contact,name="contact"),
path('register/',views.register,name="register"),
path('login/',views.user_login,name="login"),
path('logout/',views.user_logout,name="logout"),
path('search/',views.search_doctor,name="search"),
    path('delete/<int:i>',views.delete,name="delete"),
path('edit/<int:i>',views.edit,name="edit"),
path('deletepatient/<int:i>',views.delete_pat,name="delete_patient"),
path('book/', views.book_appointment, name='book_appointment'),
    path('success/',views.appointment_success,name='appointment_success'),
]
