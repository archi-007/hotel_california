from django.db import models
from django.utils import timezone

# Create your models here.


class Book_a_room(models.Model):

    name = models.CharField(max_length = 200)
    checkin = models.DateField(null = False, blank = False)
    checkout = models.DateField(null = False, blank = False)
    adult = models.IntegerField(null = False, blank = False)
    children = models.IntegerField(null = True, blank = True)
    

    def __str__(self):
        return self.name
