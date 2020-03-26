from django.db import models

# Create your models here.


class Roomtype(models.Model):


    room_type = models.CharField(max_length = 50)
    room_price = models.IntegerField()
    room_desc = models.TextField()

    def __str__(self):
        return self.room_type



