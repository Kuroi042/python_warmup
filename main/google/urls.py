from django.urls import path
from . import views
from django.urls import path
from . import views
from django.http import HttpResponse
from django.conf import settings

urlpatterns = [
    path('', lambda request: HttpResponse(open(settings.BASE_DIR / 'front/index.html').read(), content_type='text/html')),  # Serve the HTML
    path('api/data/', views.api_data, name='api_data'),  # API endpoint
]