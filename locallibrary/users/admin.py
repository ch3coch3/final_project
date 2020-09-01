from django.contrib import admin
from users.forms import UserRegisterForm
from .models import User

admin.site.register(User)
# admin.site.register(Profile)