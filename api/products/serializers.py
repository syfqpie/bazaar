"""
Product's app serializers
"""
from rest_framework import serializers

from .models import Product, Category, Variant, Inventory, Media


class CategorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['is_active']


class PublicCategorySerializer(serializers.ModelSerializer):
    """
    Public serializer for Category model
    """

    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent']


class ProductSerializer(serializers.ModelSerializer):
    """
    Base serializer for Product model
    """

    category = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['is_active','rating','vendor']


class PublicProductSerializer(serializers.ModelSerializer):
    """
    Public serializer for Product model
    """

    category = PublicCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['is_active','rating','vendor']


class VariantSerializer(serializers.ModelSerializer):
    """
    Base serializer for Variant model
    """

    class Meta:
        model = Variant
        fields = '__all__'
        read_only_fields = ['is_active', 'product']


class PublicVariantSerializer(serializers.ModelSerializer):
    """
    Public serializer for Variant model
    """

    class Meta:
        model = Variant
        exclude = ['is_active', 'created_at', 'last_modified_at', 'product']
        read_only_fields = ['is_active', 'product']


class InventorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Inventory model
    """

    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ['is_active']


class MediaSerializer(serializers.ModelSerializer):
    """
    Base serializer for Media model
    """

    class Meta:
        model = Media
        fields = '__all__'
