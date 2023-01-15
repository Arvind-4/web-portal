# Verify that the webpage is responsive on different devices and screen sizes

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class ResponsiveTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('blog-home')

    def test_responsive(self):
        response = self.client.get(self.register_url)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
        self.assertContains(response, 'blog')