# test_app.py
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, World! my name is Bhargav ram")

if __name__ == "__main__":
    unittest.main()
