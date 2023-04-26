from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class InfoExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_thumbnail = models.ImageField(upload_to='avatares/', default='avatares/default_thumbnail.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img = Image.open(self.avatar.path)
            output_size = (35, 35)
            img.thumbnail(output_size)
            img.save(self.avatar_thumbnail.path)