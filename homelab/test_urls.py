from django.test import TestCase, Client
from django.urls import reverse
from .views import pihole_status, dashboard

class HomelabTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pihole_status_view(self):
        response = self.client.get(reverse('pihole_status'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response content and behavior

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the response content and behavior