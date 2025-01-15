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
def button_action(request):
    
    if request.method == 'GET':  # Handle GET request
        print('Received data: !!!!!!!!!!!!!!!!!!!!!!!!!!')
        return JsonResponse({"heloooo madafaaaa":  "Hello from Django!"})
        
    elif request.method == 'POST': 
        print('POST Received data: !!!!!!!!!!!!!!!!!!!!!!!!!!') # Handle POST request
        data = json.loads(request.body)  # Parse JSON body
        email = json.get('email')
        password = data.get('password')
        print(f"Received data: {data}")
        if email == "1@gmail.com" and password == "123":
            return JsonResponse({'message ': 'login succesfully' , 'status' : 'success'})
        else :
            return JsonResponse({'message': 'Invalid credentials.', 'status': 'fail'}, status=401)
        return JsonResponse({'received': data})
    
