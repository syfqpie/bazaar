from users.models import UserType
from utils.auth.policy import BaseAccessPolicy


class CustomerAccessPolicy(BaseAccessPolicy):
    """
    Access policy for CustomerViewSet
    """

    statements = [
        {
            'action': ['list'],
            'principal': ['authenticated'],
            'effect': 'allow'
        },
        {
            'action': ['partial_update'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition': 'is_customer_user'
        },
        {
            'action': ['retrieve'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_customer_user or is_admin'
        }
    ]

    def is_customer_user(self, request, view, action) -> bool:
        """ Check if customer user and request user is same """

        customer = view.get_object()
        return request.user == customer.user

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """
        user = request.user

        if user.user_type == UserType.CUSTOMER:
            return queryset.filter(user=user)
        elif user.user_type == UserType.VENDOR:
            return queryset.none()
        
        return queryset
