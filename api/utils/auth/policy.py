from rest_access_policy import AccessPolicy

from users.models import UserType


class BaseAccessPolicy(AccessPolicy):
    """
    Custom base access policy based on AccessPolicy
    """

    def is_admin(self, request, view, action) -> bool:
        """ Check if request user is admin """
        
        user = request.user
        return user.user_type == UserType.ADMIN
    
    def is_vendor(self, request, view, action) -> bool:
        """ Check if request user is vendor """
        
        user = request.user
        return user.user_type == UserType.VENDOR

    def is_customer(self, request, view, action) -> bool:
        """ Check if request user is customer """
        
        user = request.user
        return user.user_type == UserType.CUSTOMER
