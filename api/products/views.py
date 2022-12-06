from rest_framework import viewsets, exceptions
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Product, Category, Variant, Inventory, Media
from .policy import (
    CategoryAccessPolicy,
    ProductAccessPolicy,
    VariantAccessPolicy,
    MediaAccessPolicy
)
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    VariantSerializer,
    MediaSerializer,

    PublicCategorySerializer,
    PublicProductSerializer,
    PublicVariantSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for Product model
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_public_class = { 'list': PublicProductSerializer }
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category','rating','vendor']
    search_fields = ['name']
    ordering_fields = ['name','rating']
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


class VariantViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Viewset for Variant model
    """

    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    serializer_public_class = { 'list': PublicVariantSerializer }
    filter_backend = []
    filterset_fields = []
    permission_classes = [VariantAccessPolicy]

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

        # Queryset for nested
        if 'parent_lookup_id' in self.kwargs:
            queryset = self.queryset.filter(
                product__id=self.kwargs['parent_lookup_id']
            )
        else:
            queryset = self.queryset

        return self.access_policy.scope_queryset(
            self.request, queryset
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

    def perform_create(self, serializer):
        """
        Ensure variant creation to point to the
        exact nested parrent product
        """

        if 'parent_lookup_id' in self.kwargs:
            # Double check if product exist?
            try:
                product = Product.objects.get(id=self.kwargs['parent_lookup_id'])
                serializer.save(product=product)
            except Product.DoesNotExist:
                raise exceptions.ValidationError({ 'product': 'Product not found' })
        else:
            serializer.save()


class MediaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Media model
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [MediaAccessPolicy]

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
