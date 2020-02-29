from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.core.admin import OPEN_DIPLOMAS_ADMIN_SITE
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User, ProxyUser, ProxyGroup


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

admin.site.register(ProxyUser, MyUserAdmin)

#Open Diplomas's admin
OPEN_DIPLOMAS_ADMIN_SITE.register(ProxyUser, MyUserAdmin)
OPEN_DIPLOMAS_ADMIN_SITE.register(ProxyGroup)
