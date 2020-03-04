from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.admin import OPEN_DIPLOMAS_ADMIN_SITE


OPEN_DIPLOMAS_ADMIN_SITE.site_header = "Django Open Diplomas Admin"
OPEN_DIPLOMAS_ADMIN_SITE.site_title = "DOP Portal"
OPEN_DIPLOMAS_ADMIN_SITE.index_title = "Welcome to Django Open Diplomas"


urlpatterns = [
    path("", include("apps.core.urls"), name="core"),
    path("diplomas/", include("apps.diplomas.urls"), name="diplomas"),
    path("myadmin/", OPEN_DIPLOMAS_ADMIN_SITE.urls),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
