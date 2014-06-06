


class State(object):

    EMPTY = '-'
    X = 'X'
    O = 'O'

    def __init__(self, board):
        self.__side_len = len(board) ** 0.5
        self.__board = board

    def get_board(self):
        return self.__board

    def get_side_len(self):
        return self.__side_len

    def put_symbol(self, symbol, row, colum):
        index = self.get_abs_pos(row, colum)
        return State(self.__board[:index] + list(symbol) + self.__board[index + 1:])

    def to_string(self):
        board = self.__board
        side = self.__side_len

        def format_list(brd, sid):
            if len(brd) == 0:
                return []
            else:
                return brd[:sid] + list('\n') + format_list(brd[sid:], sid)

        return ''.join(format_list(board, int(side)))

    def get_abs_pos(self, row, colum):
        return row * int(self.__side_len) + colum





