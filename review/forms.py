from django import forms

from .models import Review


class Reviewform(forms.ModelForm):


    class Meta:
        model = Review
        fields = ('body','name')










