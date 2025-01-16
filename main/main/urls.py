"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
from google import views  # Import the views from the google app

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings
import os

try:
    with open(settings.BASE_DIR.parent / 'front/index.html') as f:
        print("File opened successfully!")
except FileNotFoundError:
    print("File not found at:", settings.BASE_DIR / 'front/index.html')

print(settings.BASE_DIR / 'front/index.html')
# 
urlpatterns = [
    path('', lambda request: HttpResponse(
        open(settings.BASE_DIR.parent / 'front/index.html').read(), 
        content_type='text/html'
    )),
        path('admin/', admin.site.urls),  # Add this line for admin access

     path('button-action/', views.button_action, name='button-action'),
   path('register-action/', views.register_action, name='register-action'),
   path('login-action/',views.login_action, name='login-action'),
 
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
