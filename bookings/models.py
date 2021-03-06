from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Book_a_room(models.Model):


    user = models.ForeignKey(User, on_delete = models.CASCADE)
    purpose = models.CharField(max_length = 50, default = "")
    name = models.CharField(max_length = 200)
    checkin = models.DateField(null = False, blank = False)
    checkout = models.DateField(null = False, blank = False)
    adult = models.IntegerField(null = False, blank = False)
    children = models.IntegerField(null = True, blank = True)
    room = models.IntegerField(default = 0)
    room_choice = (
        ('Superior room', 'Superior room'),
        ('Premier room', 'Premier room'),
        ('Deluxe Suite', 'Deluxe Suite'),
        ('Presidential Suite', 'Presidential Suite'),

    )

    roomtype = models.CharField(max_length = 30, blank = True, null = True, choices = room_choice)

    def __str__(self):
        return self.name



class Book_a_table(models.Model):


    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    purpose = models.CharField(max_length = 50, default = "")
    name = models.CharField(max_length = 200)
    table = models.IntegerField()
    time = models.TimeField(null = False, blank = False)



    def __str__(self):
        return self.name

