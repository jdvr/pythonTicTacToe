from game import Game
from player import Player
from state import State
from getdata import get_position_from_console


state = State([State.EMPTY] * 9)
game = Game(state, Player(State.X), Player(State.O), True)

while game.is_terminal() is False:
    print game.get_state().to_string()
    get_pos = get_position_from_console()
    print get_pos
    game = game.player_move(get_pos[0], get_pos[1])
    game = game.change_turn()
    print game.get_player_turn()
print game.get_state().to_string()