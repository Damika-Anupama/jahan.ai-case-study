from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import AccountSettings
from rest_framework_simplejwt.tokens import RefreshToken

class PreferencesTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = AccountSettings.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_register(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_login(self):
        url = reverse('login')
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_get_preferences(self):
        url = reverse('preferences')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('account_settings', response.data)
        self.assertIn('notification_settings', response.data)
        self.assertIn('theme_settings', response.data)
        self.assertIn('privacy_settings', response.data)

    def test_update_preferences(self):
        url = reverse('update-preferences', args=['account_settings'])
        data = {'username': 'updateduser'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'updateduser')
        
        
class FunctionalTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'functionaluser',
            'email': 'functionaluser@example.com',
            'password': 'functionalpassword123'
        }
        self.user = AccountSettings.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_full_workflow(self):
        register_url = reverse('register')
        register_data = {
            'username': 'workflowuser',
            'email': 'workflowuser@example.com',
            'password': 'workflowpassword123'
        }
        register_response = self.client.post(register_url, register_data, format='json')
        self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', register_response.data)

        login_url = reverse('login')
        login_data = {
            'email': register_data['email'],
            'password': register_data['password']
        }
        login_response = self.client.post(login_url, login_data, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('token', login_response.data)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + login_response.data['token'])
        preferences_url = reverse('preferences')
        preferences_response = self.client.get(preferences_url, format='json')
        self.assertEqual(preferences_response.status_code, status.HTTP_200_OK)
        self.assertIn('account_settings', preferences_response.data)
        self.assertIn('notification_settings', preferences_response.data)
        self.assertIn('theme_settings', preferences_response.data)
        self.assertIn('privacy_settings', preferences_response.data)

        update_url = reverse('update-preferences', args=['account_settings'])
        update_data = {'username': 'updatedworkflowuser'}
        update_response = self.client.patch(update_url, update_data, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['username'], 'updatedworkflowuser')