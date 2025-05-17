from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("api/v1/docs/")),
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.apartments.urls")),
    path("api/v1/users/", include("apps.users.api.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
