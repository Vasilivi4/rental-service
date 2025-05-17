from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)

from apps.users.api import serializers

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer


class AdminUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all().order_by("-date_joined")
    filterset_fields = ["email", "date_joined"]

    @extend_schema(
        description="User list (for administrators only)",
        parameters=[
            OpenApiParameter(
                name="email",
                description="Filter by email",
                required=False, type=str
            ),
            OpenApiParameter(
                name="date_joined",
                description="Filter by registration date (ISO format)",
                required=False,
            ),
        ],
        examples=[
            OpenApiExample(
                "Example of a successful request",
                value={
                    "id": 1,
                    "email": "admin@example.com",
                    "first_name": "Name",
                    "last_name": "Lastname",
                    "date_joined": "2023-01-01T00:00:00Z",
                },
                response_only=True,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="User details (for administrators only)",
        responses={200: serializers.UserSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
