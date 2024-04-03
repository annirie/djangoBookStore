from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# the function get_user_model() is used for referencing the active user model specified in AUTH_USER_MODEL setting.
# It allows to avoid the problem where User model is referenced directly but in AUTH_USER_MODEL setting the active model
# has been changed to a different User model.
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
