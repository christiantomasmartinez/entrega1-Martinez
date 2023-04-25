from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class InfoExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# class InfoExtra(models.Model):
#     avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)