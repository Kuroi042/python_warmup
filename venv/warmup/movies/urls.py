from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('index',views.index, name='index'),
   path('about',views.about , name='about'),
   path('',views.movies , name='movies'),
 path('movie',views.movie , name='movie'),

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)