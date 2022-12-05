from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Variant, Inventory, Media
from .policy import (
    CategoryAccessPolicy,
    ProductAccessPolicy
)
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    VariantSerializer,
    InventorySerializer,
    MediaSerializer,

    PublicCategorySerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for Product model
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backend = []
    filterset_fields = []
    permission_classes = [ProductAccessPolicy]

    @property
    def access_policy(self):
        """
        To make get_queryset logic more explicit
        """

        return self.permission_classes[0]

    def get_queryset(self):
        """
        Ensure that current user can only see the models
        the are allowed to see
        """

        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )
    
    def perform_create(self, serializer):
        """
        Override perform_create to update created_by
        """

        request = serializer.context['request']
        serializer.save(vendor=request.user.related_vendor)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Viewset for Category model
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_public_class = { 'list': PublicCategorySerializer }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['parent']
    search_fields = ['name']
    ordering_fields = ['name', 'parent']
    permission_classes = [CategoryAccessPolicy]

    @property
    def access_policy(self):
        """
        To make get_queryset logic more explicit
        """

        return self.permission_classes[0]

    def get_queryset(self):
        """
        Ensure that current user can only see the models
        the are allowed to see
        """

        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )
    
    def get_serializer_class(self):
        """
        Override get_serializer_class for
        default action
        """

        user = self.request.user

        if hasattr(self, 'serializer_public_class') and user.is_anonymous:
            return self.serializer_public_class.get(self.action, self.serializer_class)

        # Return default class
        return super().get_serializer_class()


class VariantViewSet(viewsets.ModelViewSet):
    """
    Viewset for Variant model
    """

    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    filter_backend = []
    filterset_fields = []
    permission_classes = []

    @property
    def access_policy(self):
        """
        To make get_queryset logic more explicit
        """

        return self.permission_classes[0]

    def get_queryset(self):
        """
        Ensure that current user can only see the models
        the are allowed to see
        """

        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )


class InventoryViewSet(viewsets.ModelViewSet):
    """
    Viewset for Inventory model
    """

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backend = []
    filterset_fields = []
    permission_classes = []

    @property
    def access_policy(self):
        """
        To make get_queryset logic more explicit
        """

        return self.permission_classes[0]

    def get_queryset(self):
        """
        Ensure that current user can only see the models
        the are allowed to see
        """

        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )


class MediaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Media model
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_backend = []
    filterset_fields = []
    permission_classes = []

    @property
    def access_policy(self):
        """
        To make get_queryset logic more explicit
        """

        return self.permission_classes[0]

    def get_queryset(self):
        """
        Ensure that current user can only see the models
        the are allowed to see
        """

        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )
