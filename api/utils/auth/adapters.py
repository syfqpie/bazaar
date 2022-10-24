from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account import app_settings

from users.models import UserType


class MyAccountAdapter(DefaultAccountAdapter):
    """
    Override DefaultAccountAdapter
    Add custom implementation here
    """

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

        if current_user.user_type == UserType.ADMIN:
            if signup:
                email_template = "account/email/admin_email_confirmation_signup"
            else:
                email_template = "account/email/admin_email_confirmation"
        elif current_user.user_type == UserType.CUSTOMER:
            if signup:
                email_template = "account/email/customer_email_confirmation_signup"
            else:
                email_template = "account/email/customer_email_confirmation"
        else:
            if signup:
                email_template = 'account/email/email_confirmation_signup'
            else:
                email_template = 'account/email/email_confirmation'

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
