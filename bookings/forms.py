from django import forms

from .models import Book_a_room


class Room_book(forms.ModelForm):


    class Meta:
        model = Book_a_room
        fields = ('name', 'checkin', 'checkout', 'adult', 'children')






