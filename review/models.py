from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.TextField(max_length = 100, default = "")
    body = models.TextField()


    def __str__(self):
        return str(self.user)

