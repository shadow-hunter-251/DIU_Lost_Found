from datetime import date

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from items.models import Category, Item


class ItemAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='apiuser',
            password='apipass123'
        )

        self.category = Category.objects.create(
            name='Bag'
        )

        self.item = Item.objects.create(
            user=self.user,
            category=self.category,
            title='Black Bag',
            description='Black backpack',
            item_type='LOST',
            location='DIU',
            date=date.today()
        )

    def test_get_items(self):

        response = self.client.get(
            '/api/items/'
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            len(response.data),
            1
        )

    def test_create_item_requires_authentication(self):

        response = self.client.post(
            '/api/items/',
            {
                'title': 'New Bag',
                'description': 'A new black bag',
                'item_type': 'LOST',
                'category': self.category.id,
                'location': 'DIU',
                'date': str(date.today())
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            401
        )

    def test_authenticated_user_can_create_item(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            '/api/items/',
            {
                'title': 'New Bag',
                'description': 'A new black bag',
                'item_type': 'LOST',
                'category': self.category.id,
                'location': 'DIU',
                'date': str(date.today())
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            201
        )

        self.assertEqual(
            Item.objects.count(),
            2
        )

    def test_user_cannot_edit_other_users_item(self):

        other_user = User.objects.create_user(
            username='otherapi',
            password='otherpass123'
        )

        self.client.force_authenticate(
            user=other_user
        )

        response = self.client.patch(
            f'/api/items/{self.item.id}/',
            {
                'title': 'Hacked Title'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_user_cannot_delete_other_users_item(self):

        other_user = User.objects.create_user(
            username='anotheruser',
            password='anotherpass123'
        )

        self.client.force_authenticate(
            user=other_user
        )

        response = self.client.delete(
            f'/api/items/{self.item.id}/'
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_invalid_title(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            '/api/items/',
            {
                'title': 'AB',
                'description': 'A valid description',
                'item_type': 'LOST',
                'category': self.category.id,
                'location': 'DIU',
                'date': str(date.today())
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            400
        )