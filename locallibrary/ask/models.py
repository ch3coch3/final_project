from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from django.contrib.auth.models import User
from users.models import User

class Askpost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    title = models.CharField(max_length=100)
    date_posted  = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk':self.pk})
        return reverse('ask')

class AskComment(models.Model):
    post=models.ForeignKey(Askpost,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='users',on_delete=models.CASCADE)
    body=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%s-%s' % (self.post.title,self.user)

    def get_absolute_url(self):
        return reverse('ask-detail', kwargs={'pk':self.post.pk})