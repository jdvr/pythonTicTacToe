import unittest
from state import State
from player import Player
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.__state = State([State.EMPTY] * 9)
        self.__player_x = Player(State.X)
        self.__player_o = Player(State.O)

    def test_create_a_new_game(self):
        game = Game(self.__state, self.__player_o, self.__player_x)
        self.assertEqual(game.get_state(), self.__state)

    def test_adding_a_cross(self):
        game = Game(self.__state, self.__player_o, self.__player_x)
        self.assertEqual(game.player_move(1, 1).get_state().to_string(), self.__state.put_symbol(State.O, 1, 1).to_string())

    def test_changing_player_turn(self):
        game = Game(self.__state, self.__player_o, self.__player_x)
        self.assertEqual(game.change_turn().get_player_turn(), self.__player_x.get_type())





