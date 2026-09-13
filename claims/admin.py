from django.contrib import admin

from .models import Claim


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):

    list_display = [
        'item',
        'claimant',
        'status',
        'created_at',
    ]

    list_filter = [
        'status',
        'created_at',
    ]

    search_fields = [
        'item__title',
        'claimant__username',
        'message',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]