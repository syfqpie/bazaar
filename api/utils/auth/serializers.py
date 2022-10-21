from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer

from allauth.account import app_settings
from allauth.account.adapter import get_adapter

from .forms import MyResetPasswordForm


class MyRegisterSerializer(RegisterSerializer):
    """
    Override RegisterSerializer

    Added extra parameter
        - first_name
        - last_name
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(required=False, source='username')

    def get_cleaned_data(self):
        # Get extra parameter
        return {
            'username': self.validated_data.get('username', None),
            'password1': self.validated_data.get('password1', None),
            'email': self.validated_data.get('username', None),
            'first_name': self.validated_data.get('first_name', None),
            'last_name': self.validated_data.get('last_name', None)
        }

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        return email


class MyResendVerificationSerializer(serializers.Serializer):
    """
    Serializer for MyResendVerificationView
    """

    email = serializers.EmailField(max_length=app_settings.EMAIL_MAX_LENGTH)


class MyPasswordResetSerializer(PasswordResetSerializer):
    """
    Override PasswordResetSerializer
    """

    @property
    def password_reset_form_class(self):
        return MyResetPasswordForm
