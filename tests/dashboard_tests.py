from django.test import TestCase

class DashboardTestCase(TestCase):
    def test_dashboard_loading(self):
        # Test to ensure the dashboard loads correctly
        response = self.client.get('/dashboard/')
    def test_dashboard_data(self):
        # Test to ensure the dashboard data endpoint is working correctly
        response = self.client.get('/dashboard/data/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cluster_status', response.json())
        self.assertIn('service_health', response.json())
        self.assertEqual(response.status_code, 200)