from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
    ]

    search_fields = [
        'name',
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'item_type',
        'category',
        'location',
        'date',
        'status',
        'user',
        'created_at',
    ]

    list_filter = [
        'item_type',
        'status',
        'category',
        'date',
    ]

    search_fields = [
        'title',
        'description',
        'location',
        'user__username',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]