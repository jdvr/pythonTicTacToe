from state import State


class Game(object):

    def __init__(self, state, player_one, player_two, player_one_turn=True):
        self.__state = state
        self.__player_one = player_one
        self.__player_two = player_two
        self.__player_one_turn = player_one_turn

    def get_state(self):
        return self.__state

    def get_player_turn(self):
        return self.__player_one.get_type() if self.__player_one_turn else self.__player_two.get_type()

    def change_turn(self):
        return Game(self.__state, self.__player_one, self.__player_two, not self.__player_one_turn)

    def player_move(self, row, column):
        new_state = self.__state.put_symbol(self.__player_one.get_type(), row, column) if self.__player_one_turn else \
            self.__state.put_symbol(self.__player_two.get_type(), row, column)
        return Game(new_state, self.__player_one, self.__player_two)

    def cross_win(self):
        return self.vertical_win(State.X) or self.horizontal_win(State.X) or self.diagonal_win(State.X)



