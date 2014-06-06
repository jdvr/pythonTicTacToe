import unittest
from state import State


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__state = State([State.EMPTY] * 9)

    def test_create_new_empty_board(self):
        self.assertEqual(self.__state.get_side_len(), 3)
        self.assertEqual(self.__state.get_board(), [State.EMPTY]*9)

    def test_add_a_cross_to_board(self):
        board_with_x = [State.EMPTY] * 4 + list(State.X) + [State.EMPTY] * 4
        self.assertEqual(self.__state.put_symbol(State.X, 1, 1).get_board(), board_with_x)

    def test_add_a_noughts_to_board(self):
        board_with_x = [State.EMPTY] * 4 + list(State.O) + [State.EMPTY] * 4
        self.assertEqual(self.__state.put_symbol(State.O, 1, 1).get_board(), board_with_x)

    def test_create_a_player_x(self):
        player_x = Player(State.X)
        self.assertEqual(player_x.get_type(), State.X)
