
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('bookings.urls')),
    path('admin/', admin.site.urls),
    path('', include('review.urls')),
    
]
