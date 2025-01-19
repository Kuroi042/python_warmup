from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from . import views
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
import json

# def validate_email(email):
#     email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
#     if not re.match(email_regex, email):
#         raise ValueError("Invalid email format")

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
                print(email)
                if not email or not password or not password2 or not username:
                    return JsonResponse({'message': 'Missing required fields.', 'status': 'fail'}, status=400)
                # try:
                #     validate_email(email)
                # except ValidationError:
                #     return JsonResponse({'message': 'Invalid email format.', 'status': 'fail'}, status=400)
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
 
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json

def login_action(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            userName = data.get('user')
            password = data.get('password')
            print(userName , password)
            if not userName or not password:
                return JsonResponse({'message': 'Missing required fields.', 'status': 'fail'}, status=400)

            user = authenticate(request, username=userName, password=password)
            if user:
                is_admin = user.is_staff or user.is_superuser
                response_data = {
                    'message': 'Login successful!',
                    'status': 'success',
                    'user': {
                        'username': userName,
                        'is_admin': is_admin  # Add admin status to the response
                    }
                }
                if is_admin:
                    return JsonResponse({
                        'message': 'Superuser login successful! Redirecting to admin panel...',
                        'status': 'success',
                        'redirect_url': '/admin/'  
                    }, status=200)

                return JsonResponse({
                    'message': 'Login successful!',
                    'status': 'success',
                    'user': {
                        'username': user.username,
                    
                    }
                    }, status=200)
            else:
                return JsonResponse({'message': 'Invalid email or password.', 'status': 'fail'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format.', 'status': 'fail'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({'message': 'Server error.', 'status': 'fail'}, status=500)

    return JsonResponse({'message': 'Only POST method is allowed.', 'status': 'fail'}, status=405)
import json
import jwt
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from google.oauth2 import id_token
import google.auth.transport.requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from django.http import JsonResponse
import jwt
from django.conf import settings
from rest_framework.decorators import api_view

 


# class IsAuthenticated(APIView):
#     def has_permission(self, request, view):
#         print("Checking authentication...")  # Add this print statement
#         return super().has_permission(request, view)
# @api_view(['GET'])
# def protected_api_view(request):
#     print('Request received for protected API!') 
#     token = None
#     auth_header = request.headers.get('Authorization', None)
    
#     # Extract the token from the Authorization header
#     if auth_header:
#         parts = auth_header.split()
#         if len(parts) == 2 and parts[0].lower() == 'bearer':
#             token = parts[1]
    
#     if not token:
#         print('jajajajajajaj')
#         return JsonResponse({"message": "Token not provided"}, status=400)
    
#     try:
#         print('Decoding token:', token)  # Log before decoding the token
#         decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
#         print('Decoded token:', decoded_token)  # Log the decoded token for debugging
        
#         # If valid, return user details or some other relevant information
#         return JsonResponse({
#             "message": "Token is valid",
#             "user_id": decoded_token.get("user_id"),
#             "username": decoded_token.get("username"),
#             "email": decoded_token.get("email"),
#         }, status=200)

#     except jwt.ExpiredSignatureError:
#             print('Token has expired.')  # Print that the token is expired
#             return JsonResponse({"message": "Token has expired"}, status=401)
        
#     except jwt.InvalidTokenError:
#             print('Invalid token.')  # Print that the token is invalid
#             return JsonResponse({"message": "Invalid token"}, status=401)


from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from datetime import datetime

# Replace this with your actual secret key and algorithm
JWT_SECRET_KEY = 'eeebdbb90311675c7b8daf730b674f251eeeb35c2727b95d1421624380032db1'
JWT_ALGORITHM = "HS256"
#  verify and decode
def protected_api_view(request):
 

    auth_header = request.headers.get('Authorization', None)

    if not auth_header:
        return JsonResponse({"message": "Authorization header missing"}, status=400)

    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        return JsonResponse({"message": "Invalid Authorization header format"}, status=400)

    token = parts[1]
    print("token===", token)

    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
 

        #  expire
        exp = decoded_token.get('exp', None)
        if not exp:
            return JsonResponse({"message": "Token does not have an expiration time"}, status=401)

        # Convert exp to datetime for better readability
        expiration_time = datetime.utcfromtimestamp(exp)
        print("Token Expiration Time:", expiration_time)

        if datetime.utcnow() > expiration_time:
            return JsonResponse({"message": "Token has expired"}, status=401)

        # Step 5: Token is valid, return a success response
        return JsonResponse({
            "message": "Token is valid",
            "user_id": decoded_token.get("user_id"),
            "username": decoded_token.get("username"),
            "email": decoded_token.get("email"),
        }, status=200)

    except jwt.ExpiredSignatureError:
        return JsonResponse({"message": "Token has expired"}, status=401)
    except jwt.InvalidTokenError as e:
        print("Invalid Token Error:", str(e))
        return JsonResponse({"message": "Invalid token"}, status=401)


def generate_jwt(user):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_SECONDS),
        "iat": datetime.utcnow(),
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    print( 'tokeen', token)
    return token

 

def google_login(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            token = body.get("token")

            if not token:
                return JsonResponse({"message": "Token not provided"}, status=400)

            # Verify the ID token with Google
            try:
                id_info = id_token.verify_oauth2_token(
                    token,
                    google.auth.transport.requests.Request(),
                    "598064932608-4j38572h65hmj37524inmc1nhcfqiqpm.apps.googleusercontent.com",
                )
            except ValueError as e:
                return JsonResponse({"message": f"Invalid token: {str(e)}"}, status=400)

            email = id_info["email"]
            name = id_info.get("name", email)  # Use 'name' if available, otherwise default to email
            picture_url = id_info.get("picture", "https://example.com/default-profile-picture.png")

            # Retrieve or create the user
            user, created = User.objects.get_or_create(
                email=email,
                defaults={"username": name},
            )

            if created:
                # Perform any additional actions for new users
                print(f"New user created: {user.username} ({user.email})")

            # Log the user in
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
            
            jwt_token = generate_jwt(user)

            return JsonResponse(
                {
                    "message": "Loginn successful!",
                    "user": {
                        "name": name,
                        "email": email,
                        "picture": picture_url,
                    },
                    "token": jwt_token,  # Return JWT token
                }
            )

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"An unexpected error occurred: {str(e)}"}, status=500)

    return JsonResponse({"message": "Invalid request method"}, status=405)
