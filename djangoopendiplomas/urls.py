from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.admin import open_diplomas_admin_site


open_diplomas_admin_site.site_header = "Open Diplomas's Admin"
open_diplomas_admin_site.site_title = "Open Diplomas's Admin Portal"
open_diplomas_admin_site.index_title = "Welcome to Open Diplomas's Portal"


urlpatterns = [
    path('', include('apps.core.urls')),
    path('myadmin/', open_diplomas_admin_site.urls),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)