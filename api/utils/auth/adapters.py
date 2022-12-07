from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account import app_settings

from users.models import UserType


BASE_PATH = 'account/email/'
BASE_FILENAME = 'email_confirmation'

class CoreAccountAdapter(DefaultAccountAdapter):
    """
    Override DefaultAccountAdapter
    Add custom implementation here
    """

    @staticmethod
    def get_template_path(user, signup):
        """
        Return confirmation template path
        based on user types
        """
        
        if user.user_type == UserType.ADMIN:
            user_type_str = f'{UserType.ADMIN.label.lower()}_'
        elif user.user_type == UserType.VENDOR:
            user_type_str = f'{UserType.VENDOR.label.lower()}_'
        elif user.user_type == UserType.CUSTOMER:
            user_type_str = f'{UserType.CUSTOMER.label.lower()}_'
        else:
            user_type_str = ''
        
        email_template = f'{BASE_PATH}{user_type_str}{BASE_FILENAME}'

        return f'{email_template}_signup' if signup else email_template

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        """
        Send confirmation email implementation
        """
        
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)
        current_user = emailconfirmation.email_address.user
        ctx = {
            'user': emailconfirmation.email_address.user,
            'activate_url': activate_url,
            'current_site': current_site,
            'key': emailconfirmation.key,
            'verification_url': 'https://{}/auth/verify-account?key={}'.format(current_site.domain, emailconfirmation.key)
        }

        email_template = self.get_template_path(current_user, signup)
        
        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)

    def format_email_subject(self, subject):
        """
        Format email subject implementation
        """

        prefix = app_settings.EMAIL_SUBJECT_PREFIX
        forced_str = force_str(subject)
        
        if prefix is None:
            site = get_current_site(self.request)
            prefix = '[{name}] '.format(name=site.name)

        return forced_str
