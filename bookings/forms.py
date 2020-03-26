from django import forms

from .models import Book_a_room, Book_a_table


class Room_book(forms.ModelForm):


    class Meta:
        model = Book_a_room
        fields = ('purpose', 'name', 'checkin', 'checkout', 'adult', 'children', 'room', 'roomtype')



class Table_book(forms.ModelForm):


    class Meta:
        model = Book_a_table
        fields = ('purpose', 'name', 'table', 'time')






