from django.test import TestCase
from django.contrib.auth.models import User
from .models import AccountSettings
from rest_framework.test import APIClient

class AccountSettingsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_account_settings(self):
        data = {
            'username': 'newuser123',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post('/preferences/account/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_invalid_email(self):
        data = {
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'password123'
        }
        response = self.client.post('/preferences/account/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Enter a valid email address.", response.json()['errors']['email'])
