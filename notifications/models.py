from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):

    NOTIFICATION_TYPES = [
        ('CLAIM_APPROVED', 'Claim Approved'),
        ('CLAIM_REJECTED', 'Claim Rejected'),
        ('GENERAL', 'General'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=NOTIFICATION_TYPES,
        default='GENERAL'
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.message[:40]}'