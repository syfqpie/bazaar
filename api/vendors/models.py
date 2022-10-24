from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser, UserType
from utils.models import MyBaseModel


class Vendor(MyBaseModel):
    """
    Vendor base model
    """

    name = models.CharField(_('name of vendor'), max_length=100)
    description = models.TextField(_('description of vendor'), null=True)
    phone_no = models.CharField(_('phone number'), max_length=30)
    
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': UserType.VENDOR},
        related_name='related_vendor',
        verbose_name=_('vendor profile of')
    )
    is_newsletter_enabled = models.BooleanField(
        _('newsletter enabled'),
        default=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ('%s'%(self.id))
