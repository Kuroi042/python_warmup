from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect


from . import views
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
import json
 
def button_action(request):
    
    if request.method == 'GET':  # Handle GET request
        print('Received data: !!!!!!!!!!!!!!!!!!!!!!!!!!')
        return JsonResponse({"heloooo":  "Hello from Django!"})
   
def register_action(request):
    if request.method == 'POST':
     
        data = json.loads(request.body)  
 
  
        try:

                data = json.loads(request.body)
            
  
                email = data.get('email')
                password = data.get('password')
                password2 = data.get('password2')
                username = data.get('username')
                if not email or not password or not password2 or not username:
                    return JsonResponse({'message': 'Missing required fields.', 'status': 'fail'}, status=400)

                if password != password2:
                    return JsonResponse({'message': 'Passwords do not match.', 'status': 'fail'}, status=400)
                if User.objects.filter(username=username).exists(): 
                    return JsonResponse({'message': 'Username is already taken.', 'status': 'fail'}, status=400)
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'message': 'Email is already registered.', 'status': 'fail'}, status=400)

                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return JsonResponse({'message': 'User registered successfully!', 'status': 'success'}, status=201)

        except json.JSONDecodeError:
                return JsonResponse({'message': 'Invalid JSON format.', 'status': 'fail'}, status=400)
    
    return JsonResponse({'message': 'Only POST method is allowed.', 'status': 'fail'}, status=405)

from django.contrib.auth import authenticate
from django.http import JsonResponse
 
def login_action(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'message': 'Missing required fields.', 'status': 'fail'}, status=400)

            user = authenticate(request, username=email, password=password)
            if user:
                return JsonResponse({'message': 'Login successful!', 'status': 'success', 'user':{
                    'username': user.username }}, status=200)
            else:
                return JsonResponse({'message': 'Invalid email or password.', 'status': 'fail'}, status=401)

        except json.JSONDecodeError:
             return JsonResponse({'message': 'Invalid JSON format.', 'status': 'fail'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({'message': 'Server error.', 'status': 'fail'}, status=500)

    return JsonResponse({'message': 'Only POST method is allowed.', 'status': 'fail'}, status=405)

from rest_framework_simplejwt.tokens import RefreshToken
def jwt_login(request):
    if request.method == 'POST':
        # Decode the token or authenticate via social account
        # Then return a JWT token
        refresh = RefreshToken.for_user(user)
        return JsonResponse({'access_token': str(refresh.access_token)})
    


import google.auth.transport.requests
from google.oauth2 import id_token
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def google_login(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            token = body.get('token')

            if not token:
                return JsonResponse({'message': 'Token not provided'}, status=400)

            # Verify the ID token with Google
            try:
                id_info = id_token.verify_oauth2_token(
                    token, 
                    google.auth.transport.requests.Request(),
                    '598064932608-4j38572h65hmj37524inmc1nhcfqiqpm.apps.googleusercontent.com'
                )
            except ValueError as e:
                return JsonResponse({'message': f'Invalid token: {str(e)}'}, status=400)


            # ID token is valid, proceed with user authentication
            user, created = User.objects.get_or_create(
                email=id_info['email'], 
                defaults={'username': id_info['email']},
                
            )

            if created:
                # Perform any additional actions for new users, if needed
                pass
            picture_url = id_info.get('picture')
            if not picture_url:
                print("Profile picture not available.")
                # picture_url = "https://example.com/default-profile-picture.png"  # Use a default image
            else:
                print(f"Retrieved profile picture: {picture_url}")
            # Manually specify the backend for the user
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)  # Log the user in
            user_name = user.username
            user_email = user.email
            user_picture = id_info.get('picture', 'not found !!')
            print(f"User Name: {user_name}, User Email: {user_email}")

            return JsonResponse({
                'message': 'Login successful!',
                'user': {
                    'name': user_name,
                    'email': user_email,
                    'picture': picture_url
                }
            })
            print("Backend JSON response:", response_data)
            
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'An unexpected error occurred: {str(e)}'}, status=500)
    
    return JsonResponse({'message': 'Invalid request method'}, status=405)