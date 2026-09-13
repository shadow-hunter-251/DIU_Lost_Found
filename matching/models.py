from django.db import models
from items.models import Item


class ItemMatch(models.Model):

    lost_item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='lost_matches'
    )

    found_item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='found_matches'
    )

    score = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-score']
        constraints = [
            models.UniqueConstraint(
                fields=['lost_item', 'found_item'],
                name='unique_lost_found_match'
            )
        ]

    def __str__(self):
        return (
            f'{self.lost_item.title} ↔ '
            f'{self.found_item.title} '
            f'({self.score}%)'
        )