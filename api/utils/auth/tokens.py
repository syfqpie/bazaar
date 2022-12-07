from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import UserType


class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Override TokenObtainPairSerializer
    """
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['username'] = user.username
        token['email'] = user.email
        token['userType'] = user.user_type

        if user.user_type == UserType.VENDOR:
            token['vendorId'] = user.related_vendor.id
        elif user.user_type == UserType.CUSTOMER:
            token['customerId'] = user.related_customer.id

        return token
