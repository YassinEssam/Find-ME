from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=100)
    national_id = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.username
