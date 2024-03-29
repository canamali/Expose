"""Expose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from general.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),


    path('resetPassword/<slug:id>', ResetPassword, name='reset'),
    path('successRequest', SuccessRequest, name='LinkSuccess'),
    path('successReset', ResetSuccess, name='Success'),


    path('404', FOF, name='404'),

    path('login', Login, name='login'),
    path('login/forgotPassword', ForgetPassword, name='forget'),



    path('dashboard/<slug:id>', Dashboard, name='dashboard'),
    path('career/<slug:id>', Career, name='career'),
    path('post/<slug:id>', Post, name='post'),
    path('reviews/<slug:id>', Reviews, name='reviews'),
    path('profile/<slug:id>', Profile, name='profile'),
    path('<slug:id>/privacy', Privacy, name='privacy'),



    path('register', Register, name='register'),
    path('register/confirmation/<slug:id>', RegisterConfirmation, name='confirmation'),

    path('about', About, name='about'),
    path('del', Del, name='del'),

]
