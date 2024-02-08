import unittest
from rps import rps_match

class TestUserWins(unittest.TestCase):

    def test_user_wins(self):
        
        # Paper beats Rock, so user wins
        self.assertEqual(rps_match(1, 0), 1)
        
        # Scissors beats Paper, so user wins
        self.assertEqual(rps_match(2, 1), 1)
        
        # Rock beats Scissors, so user wins
        self.assertEqual(rps_match(0, 2), 1)

if __name__ == '__main__':
    unittest.main()