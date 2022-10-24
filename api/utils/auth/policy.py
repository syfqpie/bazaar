from rest_access_policy import AccessPolicy

from users.models import UserType


class BaseAccessPolicy(AccessPolicy):
    """
    Custom base access policy based on AccessPolicy
    """

    def is_admin(self, request, view, action) -> bool:
        """ Check if customer user and request user is same or admin """
        
        user = request.user
        return user.user_type == UserType.ADMIN
