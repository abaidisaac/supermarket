from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Product(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    title = models.TextField(max_length=20, null=True)
    quantity = models.TextField(max_length=20, null=True)

    def __str__(self):
        return str(self.user)
