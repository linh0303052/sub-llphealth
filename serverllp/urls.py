"""serverllp URL Configuration

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
from account.views import loginView, register, auth, forgot_password, getUser, change_password
from exercise.views import get_exercise
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from login.views import loginView, register, auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView),
    path('register/', register),
    path('auth/', auth),
    path('forgotpassword/', forgot_password),
    path('getuser/<username>/', getUser),
    path('changepassword/', change_password),
    path('getexercise/<username>/', get_exercise),
]

urlpatterns += staticfiles_urlpatterns()