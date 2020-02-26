from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class MyUserCreationForm(UserCreationForm):
    """
    Added creation of the user's form.
    """
    class Meta(UserCreationForm):
        model = User
        fields = ["username", "email"]


class MyUserChangeForm(UserChangeForm):
    """
    Added updating of the user's form.
    """
    class Meta:
        model = User
        fields = ["username", "email"]
