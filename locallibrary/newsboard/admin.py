from django.contrib import admin
from newsboard.models import Newsarticle

admin.site.register(Newsarticle)
class CommentAdmin(admin.ModelAdmin):
    list_display=['article', 'content', 'pubDateTime']

# Register your models here.
#admin.site.register(Comment)