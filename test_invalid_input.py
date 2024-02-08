import unittest
from rps import rps_match

class TestInvalidInput(unittest.TestCase):

    def test_invalid_input(self):
        
        # Test case with invalid user_choice
        self.assertEqual(rps_match(3, 0), "invalid input")

        # Test case with invalid computer_choice
        self.assertEqual(rps_match(0, 3), "invalid input")

        # Test case with both choices invalid
        self.assertEqual(rps_match(3, 3), "invalid input")

if __name__ == '__main__':
    unittest.main()