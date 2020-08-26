from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk':self.pk})
        return reverse('blog-home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted  = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 刪除使用者時也刪除其貼文，但刪除貼文不會刪除使用者
    other = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True,null=True)
    category = models.CharField(max_length=100,default='food')
    #content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk':self.pk})
        return reverse('blog-home')