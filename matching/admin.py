from django.contrib import admin
from .models import ItemMatch


@admin.register(ItemMatch)
class ItemMatchAdmin(admin.ModelAdmin):

    list_display = [
        'lost_item',
        'found_item',
        'score',
        'created_at',
    ]

    list_filter = [
        'created_at',
    ]

    search_fields = [
        'lost_item__title',
        'found_item__title',
    ]

    ordering = [
        '-score',
    ]