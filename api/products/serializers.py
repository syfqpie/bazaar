"""
Product's app serializers
"""
from rest_framework import exceptions, serializers

from .models import Product, Category, Variant, Inventory, Media


class CategorySerializer(serializers.ModelSerializer):
    """
    Base serializer for Category model
    """

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['is_active']


class ProductSerializer(serializers.ModelSerializer):
    """
    Base serializer for Product model
    """

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
        min_value=0, max_value=9999, default=0,
        write_only=True, allow_null=True
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

        quantity = validated_data.pop('quantity', 0)
        instance = super().create(validated_data)
        
        Inventory.objects.create(
            variant=instance,
            quantity=quantity
        )

        return instance

    def update(self, instance, validated_data):
        """
        Update variant and quantity if provided
        """

        quantity = validated_data.pop('quantity', None)
        instance = super().update(instance, validated_data)

        if quantity:
            try:
                inventory = Inventory.objects.get(variant=instance)
                inventory.quantity = quantity
                inventory.save()
            except Inventory.DoesNotExist:
                raise exceptions.NotAcceptable('Please check')
        
        return instance


class MediaSerializer(serializers.ModelSerializer):
    """
    Base serializer for Media model
    """

    class Meta:
        model = Media
        fields = '__all__'


class VendorProductSerializer(serializers.ModelSerializer):
    """
    Create serializer for Product model
    """

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True, required=False
    )
    is_publish = serializers.NullBooleanField(write_only=True)
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['is_active','rating','vendor']
    
    def create(self, validated_data):
        """
        Nested creation. Will create Product, Variant, Inventory
        """
        
        # Pop required data
        is_publish = validated_data.pop('is_publish', False)
        variants_data = validated_data.pop('variants')

        # Update data 
        validated_data['is_active'] = is_publish

        # Create product using default method
        product = super().create(validated_data)
        
        # Create variants and related inventories
        for variant in variants_data:
            quantity = variant.pop('quantity')
            variant_instance = Variant.objects.create(
                product=product,
                is_active=is_publish,
                **variant
            )
            
            # Create inventory 
            Inventory.objects.create(
                variant=variant_instance,
                quantity=quantity
            )

        return product
    
    def validate_variants_ownership(self, db, payload):
        """
        Validate if variants owned by vendor
        or not.
        """

        end_message = 'is not own by user'
        db_ids = [item['id'] for item in db.values()]

        for item in payload:
            if item['id'] not in db_ids:
                raise exceptions.PermissionDenied(f'{item["id"]} {end_message}')
    
    def get_variant_serializers(self, db, variants_data):
        """
        Validate variants payload and return list
        of serializers
        """
        
        variant_serializers = []

        for item in variants_data:
            # Get values
            item_instance = db.get(id=item['id'])
            item['quantity'] = item.pop('inventory')['quantity'] if 'inventory' in item else None

            # Init serializer and validate
            item_serializer = VariantSerializer(item_instance, data=item, partial=True)
            item_serializer.is_valid(raise_exception=True)
            variant_serializers.append(item_serializer)
        
        return variant_serializers

    def update(self, instance, validated_data):
        """
        Custom update serializer cater for
        variants

        TODO:
            Add logic with is publish
                1. If is_publish = True, product and all variants
                will be active
                2. If is_publish = False, product and all variants
                will be not active
                3. If is_publish = None, product and all variants
                will be following provided value
        """

        # Pop required data
        is_publish = validated_data.pop('is_publish', None)
        variants_data = validated_data.pop('variants', [])
        product = self.instance

        # Validate variant
        db_variants = Variant.objects.filter(product=product)
        self.validate_variants_ownership(db_variants, variants_data)
        variant_serializers = self.get_variant_serializers(db_variants, variants_data)

        # Update product
        instance = super().update(instance, validated_data)

        # Update variants if provided
        for item in variant_serializers:
            item.save()
        
        return instance


class PublicCategorySerializer(serializers.ModelSerializer):
    """
    Public serializer for Category model
    """

    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent']


class PublicProductSerializer(serializers.ModelSerializer):
    """
    Public serializer for Product model
    """

    category = PublicCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['is_active','rating','vendor']


class PublicVariantSerializer(serializers.ModelSerializer):
    """
    Public serializer for Variant model
    """

    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Variant
        exclude = ['is_active', 'created_at', 'last_modified_at', 'product']
        read_only_fields = ['is_active', 'product']

