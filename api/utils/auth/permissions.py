from rest_framework.permissions import IsAdminUser, BasePermission
from users.models import UserType


class IsSuperAdmin(IsAdminUser):
    """
    Allows access only to super admin users.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_superuser and 
            request.user.is_staff and
            request.user.user_type == UserType.ADMIN
        )


class IsAdminStaff(IsAdminUser):
    """
    Allows access only to admin staff users.
    """
    
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_staff and
            request.user.user_type == UserType.ADMIN
        )
