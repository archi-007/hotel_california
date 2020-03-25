from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Review


from .forms import Reviewform
# Create your views here.


@login_required
def review(request):

    allreviews = Review.objects.all()
    context = {

        'allreviews' : allreviews
    }
    return render(request, 'review.html', context)


@login_required
def writereview(request):
    
    form = Reviewform()
    if (request.method == "POST"):
        form = Reviewform(request.POST)
        
        if (form.is_valid()):
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('/review')


    return render(request, 'user_review.html', {'form' : form})


    