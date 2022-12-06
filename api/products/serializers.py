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


class InventorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Inventory model
    """

    class Meta:
        model = Inventory
        fields = ['quantity']


class VariantSerializer(serializers.ModelSerializer):
    """
    Base serializer for Variant model
    """

    quantity = serializers.IntegerField(
        min_value=0, max_value=9999, default=0, write_only=True
    )
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Variant
        fields = '__all__'
        read_only_fields = ['is_active', 'product']
    
    def create(self, validated_data):
        """
        Create Inventory entry after variant creation
        """

        quantity = validated_data.pop('quantity')
        instance = super().create(validated_data)
        
        Inventory.objects.create(
            variant=instance,
            quantity=quantity
        )

        return instance


class PublicVariantSerializer(serializers.ModelSerializer):
    """
    Public serializer for Variant model
    """

    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Variant
        exclude = ['is_active', 'created_at', 'last_modified_at', 'product']
        read_only_fields = ['is_active', 'product']



class MediaSerializer(serializers.ModelSerializer):
    """
    Base serializer for Media model
    """

    class Meta:
        model = Media
        fields = '__all__'
