from rest_framework import viewsets

from .models import Product, Category, Variant, Inventory, Media
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    VariantSerializer,
    InventorySerializer,
    MediaSerializer
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
