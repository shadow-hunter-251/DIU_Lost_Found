from rest_framework import serializers
from django.utils import timezone

from items.models import Category, Item


class ItemSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Item
        fields = [
            'id',
            'title',
            'description',
            'item_type',
            'category',
            'category_name',
            'username',
            'location',
            'date',
            'image',
            'status',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'username',
            'category_name',
            'status',
            'created_at',
            'updated_at',
        ]

    def validate_category(self, value):
        if not Category.objects.filter(
            id=value.id
        ).exists():
            raise serializers.ValidationError(
                'Invalid category.'
            )

        return value

    def validate_title(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                'Title must contain at least 3 characters.'
            )

        return value

    def validate_description(self, value):
        value = value.strip()

        if len(value) < 10:
            raise serializers.ValidationError(
                'Description must contain at least 10 characters.'
            )

        return value

    def validate_location(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                'Location must contain at least 3 characters.'
            )

        return value

    def validate_date(self, value):
        if value > timezone.localdate():
            raise serializers.ValidationError(
                'Date cannot be in the future.'
            )

        return value