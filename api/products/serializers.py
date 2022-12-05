"""
Product's app serializers
"""
from rest_framework import serializers

from .models import Product, Category, Variant, Inventory, Media


class ProductSerializer(serializers.ModelSerializer):
    """
    Base serializer for Product model
    """

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = [
            'is_active',
            'rating'
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = [
            'is_active'
        ]


class PublicCategorySerializer(serializers.ModelSerializer):
    """
    Public serializer for Category model
    """

    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent']


class VariantSerializer(serializers.ModelSerializer):
    """
    Base serializer for Variant model
    """

    class Meta:
        model = Variant
        fields = '__all__'
        read_only_fields = [
            'is_active'
        ]


class InventorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Inventory model
    """

    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = [
            'is_active'
        ]


class MediaSerializer(serializers.ModelSerializer):
    """
    Base serializer for Media model
    """

    class Meta:
        model = Media
        fields = '__all__'
