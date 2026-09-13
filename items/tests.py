from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Item


class ItemModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.category = Category.objects.create(
            name='Wallet',
            description='Wallet category'
        )

        self.item = Item.objects.create(
            user=self.user,
            category=self.category,
            title='Black Wallet',
            description='Black leather wallet',
            item_type='LOST',
            location='DIU Library',
            date=date.today()
        )

    def test_item_created(self):

        self.assertEqual(
            self.item.title,
            'Black Wallet'
        )

    def test_item_user(self):

        self.assertEqual(
            self.item.user,
            self.user
        )

    def test_item_default_status(self):

        self.assertEqual(
            self.item.status,
            'ACTIVE'
        )

    def test_item_string(self):

        self.assertEqual(
            str(self.item),
            'Black Wallet'
        )


class ItemOwnershipTest(TestCase):

    def setUp(self):

        self.owner = User.objects.create_user(
            username='owner',
            password='ownerpass123'
        )

        self.other_user = User.objects.create_user(
            username='other',
            password='otherpass123'
        )

        self.category = Category.objects.create(
            name='Phone'
        )

        self.item = Item.objects.create(
            user=self.owner,
            category=self.category,
            title='iPhone',
            description='Black iPhone',
            item_type='LOST',
            location='DIU',
            date=date.today()
        )

    def test_owner_can_edit(self):

        self.client.login(
            username='owner',
            password='ownerpass123'
        )

        response = self.client.get(
            reverse(
                'item_edit',
                args=[self.item.id]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_other_user_cannot_edit(self):

        self.client.login(
            username='other',
            password='otherpass123'
        )

        response = self.client.get(
            reverse(
                'item_edit',
                args=[self.item.id]
            )
        )

        self.assertEqual(
            response.status_code,
            404
        )

    def test_other_user_cannot_delete(self):

        self.client.login(
            username='other',
            password='otherpass123'
        )

        response = self.client.get(
            reverse(
                'item_delete',
                args=[self.item.id]
            )
        )

        self.assertEqual(
            response.status_code,
            404
        )