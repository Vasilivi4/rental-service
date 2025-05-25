from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.shortcuts import redirect
from apps.apartments.views import ApartmentViewSet

apartment_detail = ApartmentViewSet.as_view({'get': 'retrieve'})

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
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/v1/apartments/<slug:slug>/', apartment_detail, name='apartment-detail'),
]
