from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('sign-in')
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'password',
        }

    def test_login(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertTrue(response.status_code, 200)
