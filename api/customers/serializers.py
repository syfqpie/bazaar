"""
Customer app's serializers
"""
from django.utils.crypto import get_random_string

from rest_framework import serializers

from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import Customer, CustomerAddress, GenderType


class CustomerSerializer(serializers.ModelSerializer):
    """
    Base serializer for Customer model
    """

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = [
            'user',
            'is_active',
        ]


class CustomerAddressSerializer(serializers.ModelSerializer):
    """
    Base serializer for CustomerAddress model
    """

    class Meta:
        model = CustomerAddress
        fields = '__all__'
        read_only_fields = [
            'customer',
            'is_active',
        ]


class CustomerRegisterSerializer(RegisterSerializer):
    """
    Serializer for Customer account registration
    """

    # Genarate random pwd
    random_pwd = get_random_string(10)

    # CustomUser related
    customer_user = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(required=False, source='username')
    password1 = serializers.HiddenField(required=False, default=random_pwd)
    password2 = serializers.HiddenField(required=False, default=random_pwd)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    # Customer related
    gender = serializers.ChoiceField(choices=GenderType.choices, default=GenderType.SECRET)
    phone_no = serializers.CharField(max_length=30)
    date_of_birth = serializers.DateField(allow_null=True)

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
            'last_name': self.validated_data.get('last_name', None),
            'gender': self.validated_data.get('gender', None),
            'phone_no': self.validated_data.get('phone_no', None),
            'date_of_birth': self.validated_data.get('date_of_birth', None),
        }

        return data

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        return email

    def save(self, request):
        """
        Override to create Customer profile after CustomUser created
        """

        customer_user = super().save(request)
        
        # Instantiate customer instance
        customer = Customer(
            user=customer_user,
            phone_no=self.cleaned_data.get('phone_no'),
            gender=self.cleaned_data.get('gender'),
            date_of_birth=self.cleaned_data.get('date_of_birth')
        )

        # Saving all instances
        customer_user.save()
        customer.save()

        return customer_user
