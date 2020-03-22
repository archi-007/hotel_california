
from django.urls import path, include

from . import views

urlpatterns = [

    
    path('review/', views.review, name='review'),
    
    ]