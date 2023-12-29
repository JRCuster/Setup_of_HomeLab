# Ensure there are tests for the dashboard functionality
# Ensure there are tests for the dashboard functionality
from django.test import TestCase
from django.urls import reverse

class DashboardTestCase(TestCase):


        # Test to ensure the dashboard loads correctly
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_data(self):
        # Test to ensure the dashboard data endpoint is working correctly
        response = self.client.get(reverse('dashboard_data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('cluster_status', response.json())
        self.assertIn('service_health', response.json())
