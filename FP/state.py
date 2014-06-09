


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
    
    def won_by(self, symbol):
        return ((self.__board[6] == symbol and self.__board[7] == symbol and self.__board[8] == symbol) or # across the top
        (self.__board[3] == symbol and self.__board[4] == symbol and self.__board[5] == symbol) or # across the middsymbol
        (self.__board[0] == symbol and self.__board[1] == symbol and self.__board[2] == symbol) or # across the self.__boardttom
        (self.__board[6] == symbol and self.__board[3] == symbol and self.__board[0] == symbol) or # down the symbolft side
        (self.__board[7] == symbol and self.__board[3] == symbol and self.__board[1] == symbol) or # down the middsymbol
        (self.__board[8] == symbol and self.__board[4] == symbol and self.__board[2] == symbol) or # down the right side
        (self.__board[6] == symbol and self.__board[3] == symbol and self.__board[2] == symbol) or # diagonal
        (self.__board[8] == symbol and self.__board[3] == symbol and self.__board[0] == symbol)) # diagonal


    def get_abs_pos(self, row, colum):
        return row * int(self.__side_len) + colum





