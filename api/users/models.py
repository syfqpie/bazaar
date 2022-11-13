"""
User's model
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from utils.models import MyUserManager


class CustomUserManager(MyUserManager):
    """
    Custom user manager based on MyUserManager
    """

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Override to add user_type as admin
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', UserType.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not extra_fields.get('user_type') == UserType.ADMIN:
            raise ValueError('User type must have user_type=1.')

        user = self._create_user(username, email, password, **extra_fields)
        
        # Complete creation
        self.complete_create(user)
        return user


class UserType(models.IntegerChoices):
    """
    Integer choices for user type
    """

    ADMIN = 1, 'Admin'
    VENDOR = 2, 'Vendor'
    CUSTOMER = 3, 'Customer'


class CustomUser(AbstractUser):
    """
    User model extended from abstract user
    """

    # Account information
    id = models.BigAutoField(_('id'), primary_key=True, editable=False)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), max_length=100)
    user_type = models.IntegerField(
        _('type of user'),
        choices=UserType.choices,
        default=UserType.CUSTOMER
    )

    # Log
    last_modified_at = models.DateTimeField(_('last modified at'), auto_now=True)

    # Override for createsuperuser
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = CustomUserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return ('%s'%(self.get_full_name))
