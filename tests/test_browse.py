from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('blog-home')
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'password',
        }

    def test_browse(self):
        response = self.client.get(self.register_url, self.user_data)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertContains(response, 'blog')
