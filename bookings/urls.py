
from django.urls import path, include

from . import views

urlpatterns = [

    
    path('room_book/', views.bookaroom, name='bookaroom'),
    path('booking_successful/', views.successbook, name='successbook'),
    path('bookfood/', views.bookatable, name = 'bookatable')
    
    ]