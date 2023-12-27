from django.test import TestCase

class DashboardTestCase(TestCase):
    def test_dashboard_loading(self):
        # Test to ensure the dashboard loads correctly
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)