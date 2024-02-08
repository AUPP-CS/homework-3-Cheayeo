import unittest
from rps import rps_match

class TestComputerWins(unittest.TestCase):

    def test_computer_wins(self):

        # Paper beats Rock, so computer wins
        self.assertEqual(rps_match(0, 1), -1)
        
        # Scissors beats Paper, so computer wins
        self.assertEqual(rps_match(1, 2), -1)
        
        # Rock beats Scissors, so computer wins
        self.assertEqual(rps_match(2, 0), -1)

if __name__ == '__main__':
    unittest.main()