
from django.urls import path, include

from . import views

urlpatterns = [

    
    path('tariff/', views.tariff, name='tariff'),
    path('dining/', views.tarifffood, name='tarifffood') 
    ]