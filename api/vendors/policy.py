from users.models import UserType
from utils.auth.policy import BaseAccessPolicy


class VendorAccessPolicy(BaseAccessPolicy):
    """
    Access policy for VendorViewSet
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
            'condition': 'is_vendor_user'
        },
        {
            'action': ['retrieve'],
            'principal': ['authenticated'],
            'effect': 'allow',
            'condition_expression': 'is_vendor_user or is_admin'
        }
    ]

    def is_vendor_user(self, request, view, action) -> bool:
        """ Check if vendor user and request user is same """

        vendor = view.get_object()
        return request.user == vendor.user

    @classmethod
    def scope_queryset(cls, request, queryset):
        """ Filter queryset according to roles """
        user = request.user

        if user.user_type == UserType.VENDOR:
            return queryset.filter(user=user)
        
        return queryset
