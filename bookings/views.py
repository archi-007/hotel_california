from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Book_a_room, Book_a_table
from .forms import Room_book, Table_book

# Create your views here.

@login_required
def successbook(request):
    return render(request, 'booking_successful.html')

@login_required
def viewroombooking(request):
    bookroom = Book_a_room.objects.all()
    context = {
        'bookroom' : bookroom
    }
    return render(request, 'viewpastbookingsroom.html', context)



@login_required
def viewtablebooking(request):
    booktable = Book_a_table.objects.all()
    context = {
        'booktable' : booktable
    }
    return render(request, 'viewpastbookingstable.html', context)





@login_required
def bookaroom(request):

    

    context = {}
    form = Room_book()
    if (request.method == "POST"):
        form = Room_book(request.POST)
        
        if (form.is_valid()):
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('/booking_successful')


    return render(request, 'room_book.html', {'form' : form})

 



@login_required
def bookatable(request):
    context = {}
    form = Table_book()
    if (request.method == "POST"):
        form = Table_book(request.POST)
        
        if (form.is_valid()):
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('/booking_successful')


    return render(request, 'bookfood.html', {'form' : form})


