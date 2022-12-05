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
