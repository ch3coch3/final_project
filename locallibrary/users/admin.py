from django.contrib import admin
from users.forms import UserRegisterForm
from .models import Profile

admin.site.register(Profile)