from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser, UserType
from utils.choices import CountryChoice
from utils.models import CoreBaseModel


class GenderType(models.IntegerChoices):
    """
    Integer choices for gender type
    """

    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    SECRET = 3, 'Secret'


class Customer(CoreBaseModel):
    """
    Customer base model
    """

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': UserType.CUSTOMER},
        related_name='related_customer',
        verbose_name=_('customer profile of')
    )
    phone_no = models.CharField(_('phone number'), max_length=30)
    gender = models.IntegerField(
        _('gender of customer'),
        choices=GenderType.choices,
        default=GenderType.SECRET
    )
    date_of_birth = models.DateField(
        _('customer date of birth'),
        null=True
    )
    is_newsletter_enabled = models.BooleanField(
        _('newsletter enabled'),
        default=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ('%s'%(self.id))


class CustomerAddress(CoreBaseModel):
    """
    CustomerAddress base model
    """

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name=_('address of')
    )
    name = models.CharField(_('name of receiver'), max_length=150)
    phone_no = models.CharField(_('phone number of receiver'), max_length=30)
    is_default = models.BooleanField(_('default address'), default=False)
    instructions = models.CharField(
        _('address instructions'),
        max_length=255,
        null=True
    )

    # Address
    address = models.CharField(_('address'), max_length=255)
    zipcode = models.CharField(_('address'), max_length=5)
    city = models.CharField(_('address'), max_length=50)
    state = models.CharField(_('address'), max_length=50)
    country = models.CharField(
        _('address'),
        choices=CountryChoice.choices,
        default=CountryChoice.MY,
        max_length=30
    )

    class Meta:
        ordering = ['-last_modified_at']

    def __str__(self):
        return ('%s'%(self.id))
