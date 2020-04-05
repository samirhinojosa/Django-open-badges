#from django.contrib import admin
from apps.core.admin import OPEN_BADGES_ADMIN_SITE
from apps.diplomas.models import Issuer, Tag, Event
from apps.diplomas.admins.issuers import IssuerAdmin
from apps.diplomas.admins.tags import TagAdmin
from apps.diplomas.admins.events import EventAdmin



OPEN_BADGES_ADMIN_SITE.register(Issuer, IssuerAdmin)
OPEN_BADGES_ADMIN_SITE.register(Event, EventAdmin)
OPEN_BADGES_ADMIN_SITE.register(Tag, TagAdmin)

