 
 
 
from django.contrib.auth import views as auth_views

from django.contrib import admin
 
from mygoogle import views  

 
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
from rest_framework_simplejwt import views as jwt_views

from django.urls import path , include
urlpatterns = [
    path('', lambda request: HttpResponse(
        open(settings.BASE_DIR.parent / 'front/index.html').read(), 
        content_type='text/html'
    )),
        path('admin/', admin.site.urls),   

     path('button-action/', views.button_action, name='button-action'),
   path('register-action/', views.register_action, name='register-action'),
   path('login-action/',views.login_action, name='login-action'),     
     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/google/login/callback/', views.google_login, name='google_login'),
path('protected-api/', views.protected_api_view, name='protected-api'),
 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
