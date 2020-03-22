
from django.urls import path, include

from . import views

urlpatterns = [

    
    path('room_book/', views.bookaroom, name='bookaroom'),
    
    ]