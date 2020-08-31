from django.db import models
from django.contrib.auth.models import AbstractUser,User
from PIL import Image
from django.conf import settings

# class User(models.Model):
#     username = models.CharField(max_length=128)
#     img = models.ImageField(upload_to='profile_pics')
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)