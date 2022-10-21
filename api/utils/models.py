"""
Base models and managers
"""
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from allauth.account.models import EmailAddress


class MyUserManager(UserManager):
    """
    Base custom user manager based on UserManager
    """
    
    def complete_create(self, user):
        """
        Should do 3 things here:
        1. Check if email address already exists
        2. Create email
        3.. Send confirmation email
        """

        assert not EmailAddress.objects.filter(user=user).exists()
        address = EmailAddress.objects.create(
            user=user,
            email=user.email,
            primary=True
        )
        address.send_confirmation()


class MyBaseModel(models.Model):
    """
    Base model for all models
    """
    
    id = models.BigAutoField(_('id'), primary_key=True, editable=False)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_modified_at = models.DateTimeField(_('last modified at'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
