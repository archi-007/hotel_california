

import stripe

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Book_a_room, Book_a_table
from .forms import Room_book, Table_book

stripe.api_key = settings.STRIPE_SECRET_KEY

bill_amt = 0.0

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
    context['key'] = settings.STRIPE_PUBLISHABLE_KEY

    

    price = {
        'Superior room' : 6000,
        'Premier room' : 7000,
        'Deluxe Suite' : 8500,
        'Presidential Suite' : 10000,
    }
    
    room = ""
    room_price = 0

    

    form = Room_book()
    if (request.method == "POST"):
        form = Room_book(request.POST)
        
        if (form.is_valid()):
            book = form.save(commit=False)
            book.user = request.user
            book.save()

            room = book.roomtype
            
            room_price = price.get(room)

            bill_amt = room_price*(book.room)

            context = {
                'bill_amt' : bill_amt
            }

            return render(request, 'booking_successful.html', context)


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
            return render(request, 'booking_successful_table.html')


    return render(request, 'bookfood.html', {'form' : form})

@login_required
def charge(request): 

    
   


    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount= bill_amt,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')