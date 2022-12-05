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
        
        return queryset
