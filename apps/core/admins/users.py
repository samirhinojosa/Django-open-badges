from django.contrib.auth.admin import UserAdmin
from apps.core.models import User
from apps.core.forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    """
    customizing authentication user
    """
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = [
        "username", "email", "first_name", "last_name", "is_staff"
    ]
