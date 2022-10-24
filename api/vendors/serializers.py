"""
Vendor app's serializers
"""
from django.utils.crypto import get_random_string

from rest_framework import serializers

from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """
    Base serializer for Vendor model
    """

    class Meta:
        model = Vendor
        fields = '__all__'


class VendorRegisterSerializer(RegisterSerializer):
    """
    Serializer for Vendor account registration
    """

    # Genarate random pwd
    random_pwd = get_random_string(10)

    # CustomUser related
    vendor_user = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(required=False, source='username')
    password1 = serializers.HiddenField(required=False, default=random_pwd)
    password2 = serializers.HiddenField(required=False, default=random_pwd)
    first_name = serializers.HiddenField(required=False, source='name')

    # Vendor related
    name = serializers.CharField(max_length=100)
    phone_no = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        """
        Override to accept new extra parameters to clean
        """
        
        data = {
            'username': self.validated_data.get('username', None),
            'password1': self.validated_data.get('password1', None),
            'password2': self.validated_data.get('password2', None),
            'email': self.validated_data.get('username', None),
            'first_name': self.validated_data.get('first_name', None),
            'name': self.validated_data.get('name', None),
            'phone_no': self.validated_data.get('phone_no', None)
        }

        return data

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        return email

    def save(self, request):
        """
        Override to create Vendor profile after CustomUser created
        """

        vendor_user = super().save(request)
        
        # Instantiate vendor instance
        vendor = Vendor(
            user=vendor_user,
            name=self.cleaned_data.get('name'),
            date_of_birth=self.cleaned_data.get('date_of_birth')
        )

        # Saving all instances
        vendor_user.save()
        vendor.save()

        return vendor_user
