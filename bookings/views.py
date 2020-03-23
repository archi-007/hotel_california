from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .forms import Room_book, Table_book

# Create your views here.

@login_required
def successbook(request):
    return render(request, 'booking_successful.html')



@login_required
def bookaroom(request):
    context = {}
    form = Room_book()
    if (request.method == "POST"):
        form = Room_book(request.POST)
        
        if (form.is_valid()):
            form.save()
            return redirect('/booking_successful')


    return render(request, 'room_book.html', {'form' : form})





@login_required
def bookatable(request):
    context = {}
    form = Table_book()
    if (request.method == "POST"):
        form = Table_book(request.POST)
        
        if (form.is_valid()):
            form.save()
            return redirect('/booking_successful')


    return render(request, 'bookfood.html', {'form' : form})


