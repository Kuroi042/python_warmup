from django.urls import path
from . import views
from django.urls import path
from . import views
from django.http import HttpResponse
from django.conf import settings
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


urlpatterns = [
path('', lambda request: HttpResponse(open(settings.BASE_DIR.parent / '/front/index.html').read(), content_type='text/html')),
    path('button-action/', button_action, name='button-action'),
    path('register-action/', register_action, name='register-action'),
    path('login-action/',login_action, name='login-action'),
 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
