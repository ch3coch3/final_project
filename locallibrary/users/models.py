from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings

class Profile(AbstractUser):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.username} Profile'


    # def save(self):
    #     # super().save(commit = False)
    #     user = super().save(commit = False)
    #     user.save()
    #     img = Image.open(self.image.path)

    #     if img.height > 200 or img.width > 200:
    #         output_size = (200,200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    #     return user

# class Users(AbstractUser):
#     username = models.CharField(max_length=128)
    
#     def __str__(self):
#         return self.username