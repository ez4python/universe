from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language

from root import settings
from root.settings import DEBUG

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('set_language/', set_language, name='set_language'),
    re_path(r'^rosetta/', include('rosetta.urls')),
    # path('', include('apps.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
)
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
