"""
Test cases for the Flask application routes
"""
import unittest
from service import app


class TestRoutes(unittest.TestCase):
    """Test cases for routes"""

    def setUp(self):
        """Runs before each test"""
        self.client = app.test_client()

    def test_index(self):
        """It should return 200 for root URL"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_health(self):
        """It should return 200 for health check"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")
