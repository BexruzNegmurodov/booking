from django.urls import path
from .views import room, room_detail

app_name = 'booking'

urlpatterns = [
    path('room/', room, name='room'),
    path('room/detail/<slug:slug>/', room_detail, name='room_detail'),
]
