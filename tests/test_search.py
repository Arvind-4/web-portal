from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class SearchTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('search')
        self.params = {
            'q': 'blog',
        }

    def test_search(self):
        response = self.client.get(self.register_url, self.params)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/view.html')
        self.assertContains(response, 'blog')

