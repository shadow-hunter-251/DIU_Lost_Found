from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from items.models import Category, Item

from .models import Claim


class ClaimTest(TestCase):

    def setUp(self):

        self.owner = User.objects.create_user(
            username='owner',
            password='ownerpass123'
        )

        self.claimant = User.objects.create_user(
            username='claimant',
            password='claimantpass123'
        )

        self.category = Category.objects.create(
            name='Wallet'
        )

        self.item = Item.objects.create(
            user=self.owner,
            category=self.category,
            title='Black Wallet',
            description='Black wallet',
            item_type='FOUND',
            location='Library',
            date=date.today()
        )

    def test_claim_page_requires_login(self):

        response = self.client.get(
            reverse(
                'submit_claim',
                args=[self.item.id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

    def test_claim_can_be_submitted(self):

        self.client.login(
            username='claimant',
            password='claimantpass123'
        )

        response = self.client.post(
            reverse(
                'submit_claim',
                args=[self.item.id]
            ),
            {
                'message': 'This is my wallet.'
            }
        )

        self.assertEqual(
            Claim.objects.count(),
            1
        )

        self.assertRedirects(
            response,
            reverse(
                'item_detail',
                args=[self.item.id]
            )
        )