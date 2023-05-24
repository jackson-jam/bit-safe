from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
