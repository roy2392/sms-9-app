import unittest
from src.app import app

class HelloWordTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_word(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "hello word")

if __name__ == "__main__":
    unittest.main()