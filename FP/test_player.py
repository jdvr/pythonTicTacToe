import unittest
from player import Player
from state import State

class TestPlayer(unittest.TestCase):

    def test_create_a_player_x(self):
        player_x = Player(State.X)
        self.assertEqual(player_x.get_type(), State.X)

    def test_create_a_player_o(self):
        player_o = Player(State.O)
        self.assertEqual(player_o.get_type(), State.O)

