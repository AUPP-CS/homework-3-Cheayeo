import unittest
from rps import rps_match

class TestTie(unittest.TestCase):

    def test_computer_wins(self):
        self.assertEqual(rps_match(0, 0), 0)  # Rock vs Rock
        self.assertEqual(rps_match(1, 1), 0)  # Paper vs Paper
        self.assertEqual(rps_match(2, 2), 0)  # Scissors vs Scissors

if __name__ == '__main__':
    unittest.main()