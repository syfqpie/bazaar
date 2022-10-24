"""
Vendor apps' views
"""

from rest_framework import mixins, status, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from dj_rest_auth.registration.views import RegisterView
from django_filters.rest_framework import DjangoFilterBackend

from utils.auth.permissions import IsSuperAdmin

from .models import Vendor
from .serializers import (
    VendorSerializer,
    VendorRegisterSerializer
)


class VendorViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Viewset for Vendor model
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'is_active'
    ]

    def get_permissions(self):
        """Append permissions"""
        
        permission_classes = [IsAuthenticated, IsSuperAdmin]

        return [permission() for permission in permission_classes]    


class VendorRegisterView(RegisterView):
    """
    Custom view for Vendor registration
    """

    serializer_class = VendorRegisterSerializer

    def get_permissions(self):
        permission_classes = [
            AllowAny
        ]

        return [permission() for permission in permission_classes]  

    def create(self, request, *args, **kwargs):
        """Append custom response message"""
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer_user = self.perform_create(serializer)
        response_msg = {
            'Success':  f'Account created, an email has been sent to {customer_user.email}'
        }
            
        return Response(
            response_msg,
            status=status.HTTP_201_CREATED
        )
