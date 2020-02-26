#from django.contrib import admin
from apps.core.admin import OPEN_DIPLOMAS_ADMIN_SITE
from .models import Issuer
from .admins.issuers import IssuerAdmin


OPEN_DIPLOMAS_ADMIN_SITE.register(Issuer, IssuerAdmin)
