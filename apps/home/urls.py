from django.urls import path
from .views import home, about

app_name = 'home'


urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
]
