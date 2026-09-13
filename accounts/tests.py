from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_page(self):

        response = self.client.get(
            reverse('login')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_login_success(self):

        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': 'testpass123'
            }
        )

        self.assertRedirects(
            response,
            reverse('home')
        )

    def test_profile_requires_login(self):

        response = self.client.get(
            reverse('profile')
        )

        self.assertEqual(
            response.status_code,
            302
        )