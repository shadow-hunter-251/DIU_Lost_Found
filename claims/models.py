from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class Claim(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='claims'
    )

    claimant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='claims'
    )

    message = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

        constraints = [
            models.UniqueConstraint(
                fields=['item', 'claimant'],
                name='unique_item_claimant'
            )
        ]

    def __str__(self):
        return f'{self.claimant.username} - {self.item.title}'