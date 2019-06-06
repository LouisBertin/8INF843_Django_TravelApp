# Register your models here.
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Post

from .registration.CustomUserCreationForm import CustomUserCreationForm, CustomUserChangeForm
from .models import Preference


# preferences tab in user profile
class PreferenceInline(admin.StackedInline):
    model = Preference
    can_delete = False
    verbose_name_plural = 'preferences'


# Custom admin extending custom user class
class CustomUserAdmin(UserAdmin):
    inlines = (PreferenceInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]


admin.site.register(Post)
admin.site.register(User, CustomUserAdmin)
