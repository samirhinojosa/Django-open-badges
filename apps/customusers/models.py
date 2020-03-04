from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    """
    Store a custom user
    """

    class Meta:
        db_table = "auth_user"


class ProxyUser(User):

    class Meta:
        app_label = "auth"
        proxy = True
        verbose_name = "User"
        verbose_name_plural = "Users"

class ProxyGroup(Group):

    class Meta:
        app_label = "auth"
        proxy = True
        verbose_name = "Group"
        verbose_name_plural = "Groups"
