from django.contrib.auth.models import User
from django.db import models

import os


class Category(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    class Meta:

        verbose_name_plural = 'Categories'

        ordering = ['name']

    def __str__(self):

        return self.name


class Item(models.Model):

    ITEM_TYPE_CHOICES = [
        ('LOST', 'Lost'),
        ('FOUND', 'Found'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('CLAIMED', 'Claimed'),
        ('RETURNED', 'Returned'),
        ('CLOSED', 'Closed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='items'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    item_type = models.CharField(
        max_length=10,
        choices=ITEM_TYPE_CHOICES
    )

    location = models.CharField(
        max_length=200
    )

    date = models.DateField()

    image = models.ImageField(
        upload_to='items/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return self.title

    def delete(self, *args, **kwargs):

        image = self.image

        super().delete(*args, **kwargs)

        if image:

            if os.path.isfile(image.path):

                os.remove(image.path)
