"""
User's serializers
"""

from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for custom user
    """

    class Meta:
        model = CustomUser
        fields = [
            'id',
		    'first_name',
		    'last_name',
		    'email',
            'user_type',
		    'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined',
		    'last_modified_at',
        ]
        read_only_fields = ['email']
