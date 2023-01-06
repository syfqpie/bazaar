from django.contrib.auth.forms import SetPasswordForm

from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer, VerifyEmailSerializer
from dj_rest_auth.serializers import PasswordResetSerializer

from allauth.account import app_settings
from allauth.account.adapter import get_adapter

from .forms import CoreResetPasswordForm


class CoreRegisterSerializer(RegisterSerializer):
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


class CoreResendVerificationSerializer(serializers.Serializer):
    """
    Serializer for CoreResendVerificationView
    """

    email = serializers.EmailField(max_length=app_settings.EMAIL_MAX_LENGTH)


class CorePasswordResetSerializer(PasswordResetSerializer):
    """
    Override PasswordResetSerializer
    """

    @property
    def password_reset_form_class(self):
        return CoreResetPasswordForm


class CoreVerifyEmailSerializer(VerifyEmailSerializer):
    """
    Custom serializer to for M
    """

    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)


class CoreSetPasswordSerializer(serializers.Serializer):
    """
    Custom serializer to enable change password while
    verifying email
    """

    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get('request')
        self.user = self.request['user']

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
    