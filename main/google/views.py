from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         return HttpResponse(f"zab: {username}, 9lwa: {password}")
    
#     return render(request, 'index.html')  # Make sure the path matches the location of index.html


from . import views
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: HttpResponse(open(settings.BASE_DIR / 'front/index.html').read(), content_type='text/html')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
