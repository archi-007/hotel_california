from django.shortcuts import render
from .models import Roomtype


# Create your views here.



def tariff(request):


    allrooms = Roomtype.objects.all()

    context = {
        'allrooms' : allrooms
    }
    
    return render(request, 'tariff.html', context)

def tarifffood(request):
    return render(request, 'tarifffood.html')