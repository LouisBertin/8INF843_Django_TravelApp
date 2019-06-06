from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Post

from .registration.CustomUserCreationForm import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]


admin.site.register(Post)
admin.site.register(User, CustomUserAdmin)
