import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_updates_endpoint(self):
        response = self.app.get('/updates')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
