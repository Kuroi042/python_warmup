from django.shortcuts import render
from django.http import JsonResponse

import json
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

from . import views
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
def your_view(request):
    csrf_token = get_token(request)  # This will generate the CSRF token for you
    response = JsonResponse({'message': 'Success'})
    response['X-CSRFToken'] = csrf_token  # Pass the CSRF token in the response header
    return response

from django.middleware.csrf import get_token

@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

def button_action(request):
    
    if request.method == 'GET':  # Handle GET request
        print('Received data: !!!!!!!!!!!!!!!!!!!!!!!!!!')
        return JsonResponse({"heloooo madafaaaa":  "Hello from Django!"})
    
@ensure_csrf_cookie    
def register_action(request):
    if request.method == 'POST':
        csrf_token = request.headers.get('X-CSRFToken')
        if not csrf_token:
            return JsonResponse({'message': 'CSRF token missing.', 'status': 'fail'}, status=403)# Django's CSRF validation automatically happens with CSRF middleware enabled
        data = json.loads(request.body)  # Parse JSON body
 
  
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
                if email == "1@gmail.com" and password == "123" and username == "jesus":
                    return JsonResponse({'message': 'Login successful', 'status': 'success'})
                else:
                    return JsonResponse({'message': 'Invalid credentials.', 'status': 'fail'}, status=401)
        
        except json.JSONDecodeError:
                return JsonResponse({'message': 'Invalid JSON format.', 'status': 'fail'}, status=400)
    
    return JsonResponse({'message': 'Only POST method is allowed.', 'status': 'fail'}, status=405)
