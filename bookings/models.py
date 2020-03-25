from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# bookroom = Book_a_room()
class Book_a_room(models.Model):


    user = models.ForeignKey(User, on_delete = models.CASCADE)
    purpose = models.CharField(max_length = 50, default = "")
    name = models.CharField(max_length = 200)
    checkin = models.DateField(null = False, blank = False)
    checkout = models.DateField(null = False, blank = False)
    adult = models.IntegerField(null = False, blank = False)
    children = models.IntegerField(null = True, blank = True)
    room = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.name


# booktable = Book_a_table()
class Book_a_table(models.Model):


    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    purpose = models.CharField(max_length = 50, default = "")
    name = models.CharField(max_length = 200)
    table = models.IntegerField()
    time = models.TimeField(null = False, blank = False)



    def __str__(self):
        return self.name

