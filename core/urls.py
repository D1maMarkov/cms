from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("common.urls")),
    path("", include("blocks.urls")),
    path("styles/", include("styles.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
    path("domain/", include("domens.urls")),
    path("my/", include("account.urls")),
    path("notifications/", include("notifications.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
