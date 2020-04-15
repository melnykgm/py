import unittest
from game import make_decision

class GameTestCase(unittest.TestCase):
    def test_game(self):
        first=make_decision(1,2)
        self.assertEqual(first,"you win")
        
unittest.main()
