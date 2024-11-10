# test_app.py
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
<<<<<<< HEAD
        self.assertEqual(greet(), "Hello, World! my name is Bhargav ram")
=======
        self.assertEqual(greet(), "Hello, World! World! my name is fdlair")
>>>>>>> 4f821eaf5a35756dc8d0e1b421e253333b9e2f52

if __name__ == "__main__":
    unittest.main()
