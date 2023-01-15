from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('sign-up')
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'password',
            'password2': 'password',
        }

    def test_register(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertFalse(
            self.client.login(email="testuser@example.com", password='password'))
        self.assertTrue(response.status_code, 200)
