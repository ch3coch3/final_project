from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Newsarticle(models.Model):
    title = models.CharField(max_length=255)
    pubDateTime = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title + ' | ' #+ str(self.id)

    class Meta:
        ordering=['-pubDateTime']