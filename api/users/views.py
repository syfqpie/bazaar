"""
User's views
"""

import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from utils.auth.permissions import IsSuperAdmin

from .models import (
    UserType,
    CustomUser
)
from .serializers import (
    CustomUserSerializer
)


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Viewset for custom user
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'user_type',
        'is_active'
    ]

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsSuperAdmin]

        return [permission() for permission in permission_classes]    
