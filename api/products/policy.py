from users.models import UserType
from utils.auth.policy import BaseAccessPolicy


class CategoryAccessPolicy(BaseAccessPolicy):
    """
    Access policy for CategoryViewSet
    """

    statements = [
        {
            'action': ['list', 'retrieve'],
            'principal': '*',
            'effect': 'allow'
        },
        {
            'action': ['partial_update'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition': 'is_admin'
        },
        {
            'action': ['create'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_vendor or is_admin'
        }
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """

        return queryset


class ProductAccessPolicy(BaseAccessPolicy):
    """
    Access policy for ProductViewSet
    """

    statements = [
        {
            'action': ['list', 'retrieve'],
            'principal': '*',
            'effect': 'allow'
        },
        {
            'action': ['create'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition': 'is_vendor'
        },
        {
            'action': ['partial_update', 'destroy'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_vendor and is_owner'
        }
    ]

    def is_owner(self, request, view, action) -> bool:
        """ Check if vendor user and request user is same """

        product = view.get_object()
        return request.user == product.vendor.user

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """

        user = request.user

        if not user.is_anonymous and user.user_type == UserType.VENDOR:
            return queryset.filter(vendor__user=user)

        return queryset


class VariantAccessPolicy(BaseAccessPolicy):
    """
    Access policy for VariantViewSet
    """

    statements = [
        {
            'action': ['list'],
            'principal': '*',
            'effect': 'allow'
        },
        {
            'action': ['create'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition': 'is_vendor'
        },
        {
            'action': ['retrieve', 'partial_update', 'destroy'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_vendor and is_owner'
        }
    ]

    def is_owner(self, request, view, action) -> bool:
        """ Check if vendor user and request user is same """

        product_variant = view.get_object()
        return request.user == product_variant.product.vendor.user

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """
        
        return queryset


class MediaAccessPolicy(BaseAccessPolicy):
    """
    Access policy for MediaViewSet
    """

    statements = [
        {
            'action': ['list'],
            'principal': '*',
            'effect': 'allow'
        },
        {
            'action': ['create'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition': 'is_vendor'
        },
        {
            'action': ['retrieve', 'partial_update', 'destroy'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_vendor and is_owner'
        }
    ]

    def is_owner(self, request, view, action) -> bool:
        """ Check if vendor user and request user is same """

        variant_media = view.get_object()
        return request.user == variant_media.variant.product.vendor.user

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """
        

        return queryset
