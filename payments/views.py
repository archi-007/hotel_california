from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required
def pay(request):

   


    return render(request, 'pay.html')