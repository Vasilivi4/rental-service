from rest_framework import viewsets, permissions
from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    NumberFilter,
    BooleanFilter,
    CharFilter,
)
from django.db import models
from .models import Apartment
from .serializers import ApartmentSerializer
from .permissions import IsOwnerOrReadOnly


class ApartmentFilter(FilterSet):
    price_min = NumberFilter(field_name="price", lookup_expr="gte")
    price_max = NumberFilter(field_name="price", lookup_expr="lte")
    rooms = NumberFilter(field_name="number_of_rooms", lookup_expr="exact")
    available = BooleanFilter(field_name="availability")
    search = CharFilter(method="filter_search")

    class Meta:
        model = Apartment
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(description__icontains=value)
        )


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all().order_by("-created_at")
    serializer_class = ApartmentSerializer
    lookup_field = "slug"
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
