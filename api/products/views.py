from rest_framework import viewsets

from .models import Product, Category, Variant, Inventory, Media
from .policy import CategoryAccessPolicy
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


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Viewset for Category model
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_public_class = { 'list': PublicCategorySerializer }
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
