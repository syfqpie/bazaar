import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from utils.models import MyBaseModel
from vendors.models import Vendor


class Category(MyBaseModel):
    """
    A product category model. Might be useful
    for routing, analytics
    """

    name = models.CharField(_('category name'), max_length=128)
    slug = models.SlugField(_('category slug'), max_length=128, unique=True)
    description = models.TextField(_('category description'))
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        related_name='subcategory',
        verbose_name=_('parent category')
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return ('%s'%(self.name))


class Product(MyBaseModel):
    """
    Base product model. Can be considered as a
    parent product for variants
    """

    name = models.CharField(_('product name'), max_length=128)
    slug = models.SlugField(_('product slug'), max_length=128, unique=True)
    description = models.TextField(_('product description'))
    category = models.ManyToManyField(
        Category,
        through='CategoryProduct',
        through_fields=('product', 'category'),
        related_name='related_product',
        verbose_name=_('product category')
    )
    rating = models.FloatField(_('product rating'), null=True)

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('product vendor')
    )

    class Meta:
        ordering = ['-created_at', '-rating']

    def __str__(self):
        return ('%s'%(self.name))


class CategoryProduct(models.Model):
    """
    A through model for Product - Category
    models
    """

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_products',
        verbose_name=_('category products')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_categories',
        verbose_name=_('product categories')
    )


class Variant(MyBaseModel):
    """
    A product variant model. If a product don't
    have any variant, so it should be default to
    one variant
    """

    sku = models.CharField(_('variant sku'), null=True, max_length=128)
    name = models.CharField(_('variant name'), max_length=128)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants',
        verbose_name=_('variant parent product')
    )
    price = models.DecimalField(
        _('variant price'),
        decimal_places=2,
        max_digits=20,
        validators=[MinValueValidator(0.00)]
    )
    weight = models.FloatField(_('variant weight'), null=True)
    
    customer_quantity_limit = models.PositiveIntegerField(
        _('quantity per customer'),
        null=True
    )
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return ('%s - %s'%(self.sku, self.name))


class Inventory(models.Model):
    """
    A product inventory model. Used to keep
    the current stock for each variants
    """

    variant = models.OneToOneField(
        Variant,
        on_delete=models.CASCADE,
        related_name='inventory',
        verbose_name=_('inventory variant'),
        primary_key=True
    )
    quantity = models.PositiveIntegerField(_('variant quantity'), default=0)

    def __str__(self):
        return ('%s'%(self.variant))


class Media(models.Model):
    """
    A product media model. Use to keep media
    """

    id = models.UUIDField(
        _('media id'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    short_description = models.CharField(
        _('media short description'),
        null=True,
        max_length=128
    )

    upload = models.FileField(_('media uploaded'), upload_to='product-medias/')
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        related_name='medias',
        verbose_name=_('media variant')

    )

    is_main = models.BooleanField(_('is media main?'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ('%s'%(str(self.id)))

