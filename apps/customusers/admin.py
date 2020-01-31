from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.core.admin import open_diplomas_admin_site
from .forms import UserCreationForm, UserChangeForm
from .models import User, ProxyUser, ProxyGroup


class UserAdmin(UserAdmin):
    """
    customizing authentication user 
    """
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "username", "email", "first_name", "last_name", "is_staff"
    ]

#admin.site.register(User, UserAdmin)
admin.site.register(ProxyUser, UserAdmin)

#Open Diplomas's admin customed
open_diplomas_admin_site.register(ProxyUser, UserAdmin)
open_diplomas_admin_site.register(ProxyGroup)