from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image

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


# class User(AbstractUser):
#     username = models.CharField(max_length=128)
#     password = models.CharField(max_length=128)
#     password2 = models.CharField((max_length=128)
#     email = models.EmailField(label='電子郵件')
#     ID = models.ImageField(label='上傳學生證或入學證明',default='default.jpg',upload_to='profile_pics')
#     picture = models.ImageField(label='上傳大頭貼照',default='default.jpg',upload_to='profile_pics')
#     gender = models.ChoiceField(label='性別',choices=gender_choice)
#     identication = models.MultipleChoiceField(label='身分別',choices=id_choice) 