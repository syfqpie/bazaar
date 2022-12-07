from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordResetView,
    PasswordResetConfirmView
)

from users.models import CustomUser
from utils.auth.serializers import (
    CoreRegisterSerializer, CoreResendVerificationSerializer,
    CorePasswordResetSerializer, CoreSetPasswordSerializer,
    CoreVerifyEmailSerializer
)


class CoreLoginView(LoginView):
    """
    Login
    
    Check the credentials and return JWT if the credentials 
    are valid and authenticated. Calls auth login method to
    register User ID in session

    Accept the following POST parameters: username, password
    Return the token object key.
    """
    pass


class CoreLogoutView(LogoutView):
    """
    Logout
    
    Calls logout method and delete the token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """

    http_method_names = ['post']


class CoreRegisterView(RegisterView):
    """
    Register

    Register new account and will send a verification
    email to the registered email

    Accept the following POST parameters
        - username
        - password1
        - password2
        - first_name
        - last_name
    """

    serializer_class = CoreRegisterSerializer
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        public_user = self.perform_create(serializer)
        response_msg = {
            'Success':  f'Account created, an email has been sent to {public_user.email}'
        }
            
        return Response(
            response_msg,
            status=status.HTTP_201_CREATED
        )


class CoreVerifyEmailView(VerifyEmailView):
    """
    Verify email
    
    Verify a new registered account in the system
    """
    def get_serializer(self, *args, **kwargs):
        """ Override to return custom serializer"""

        return CoreVerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Override to append custom validations and actions """
        
        # Email form validation
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        # Get email instance
        verify_email_serializer = VerifyEmailSerializer(data={'key': request.data['key']})        
        verify_email_serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = verify_email_serializer.validated_data['key']
        confirmation = self.get_object()

        # If already verified, return 400
        if confirmation.email_address.verified:
            return Response({'detail': _('This email address is verified')}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get use instance and activation datetime
        User = get_user_model()
        user = User.objects.get(email=confirmation.email_address.email)
        user.activated_at = datetime.now(timezone.utc)

        # Password validation
        set_password_serializer = CoreSetPasswordSerializer(
            data={
                'new_password1': request.data['new_password1'],
                'new_password2': request.data['new_password2']
            },
            context={
                'request': {
                    'user': user
                }
            }
        )
        set_password_serializer.is_valid(raise_exception=True)

        # Confirm and save new password
        confirmation.confirm(self.request)
        user.save()
        set_password_serializer.save()

        # Return response
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)


class CoreResendVerificationView(GenericAPIView):
    """
    Resend verification email
    
    Accepts the following POST parameters: email
    
    Returns status detail
    """

    permission_classes = [AllowAny]
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        """
        Try to send verification email if account hasn't
        been verified.

        Returns 400 if account has been verified or
        account email not found
        """
        try:
            serializer = CoreResendVerificationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = CustomUser.objects.get(email=serializer.validated_data['email'])
            email_address = EmailAddress.objects.get(email=serializer.validated_data['email'])

            if not email_address.verified:
                send_email_confirmation(request, user, signup=False)
                return Response(
                    { 'detail': _('Verification e-mail sent.') }, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    { 'detail': _('This email address is verified') },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except EmailAddress.DoesNotExist:
            return Response(
                { 'detail': _('E-mail is not registered') },
                status=status.HTTP_400_BAD_REQUEST
            )


class MyPasswordChangeView(PasswordChangeView):
    """
    Change password

    Accepts the following POST parameters:
        - new_password1
        - new_assword2

    Returns the success/fail message.
    """
    pass


class MyPasswordResetView(PasswordResetView):
    """
    Request to reset password
    
    Calls password save method.

    Accepts the following POST parameters: email

    Returns the success/fail message.
    """
    serializer_class = CorePasswordResetSerializer


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Confirm reset password

    Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters:
        - token
        - uid
        - new_password1
        - new_password2
    
    Returns the success/fail message.
    """
    pass
