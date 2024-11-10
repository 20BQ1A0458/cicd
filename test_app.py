# test_app.py
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
<<<<<<< HEAD
        self.assertEqual(greet(), "Hello, GitHub Actions!")
=======
        self.assertEqual(greet(), "Hello, World! my name  Bhargav ram")
>>>>>>> d06d53fdb3be3a6bc21222af728d71c991038519

if __name__ == "__main__":
    unittest.main()
