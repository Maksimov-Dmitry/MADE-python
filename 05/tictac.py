class TicTacGame:
    """
    This class is used to play tic-tac-toe
    """

    def __init__(self):
        self._board = self._init_board()
        self._current_player = 'X'

    @staticmethod
    def _init_board():
        return [[' ' for _ in range(3)] for _ in range(3)]

    def show_board(self):
        rows_sep = '---+---+---'
        columns_sep = '  |'
        print(rows_sep)
        for row in self._board:
            print(columns_sep.join(row))
            print(rows_sep)

    def validate_input(self, inp):
        inputs = inp.split()
        if len(inputs) != 2:
            print(
                'Wrong input! You must enter 2 numbers separated by a space. '
                f'However, {len(inputs)} were entered.')
            return False
        for s_num in inputs:
            if not s_num.isdigit():
                print(
                    'Wrong input! '
                    'You must enter 2 numbers separated by a space. '
                    f'However, {s_num} is not a number.')
                return False

        row, col = list(map(self._get_position_from_input, inp.split()))
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print('Wrong input! Numbers must be 1 or 2 or 3.')
            return False
        if self._board[row][col] != ' ':
            print(
                'Wrong input! '
                'This place is already taken, choose a free place.')
            return False

        return True

    def start_game(self):
        is_not_ended = True
        while is_not_ended:
            self.show_board()
            print(f"Player {self._current_player }, it is your turn.")
            is_waiting_move = True
            while is_waiting_move:
                inp = input('Pick a row and column, e.g.'
                            ' 1 2 - first row and second column.\n')
                if self.validate_input(inp):
                    row, col = list(
                        map(self._get_position_from_input, inp.split()))
                    self._board[row][col] = self._current_player
                    is_waiting_move = False

            winner = self.check_winner()
            if winner != -1:
                print(f"Player {winner}, you won!")
                is_not_ended = False
            if self.is_full_board():
                print('The board is full - Draw.')
                is_not_ended = False
            self._current_player = self._get_next_player()
        self.show_board()

    def _check_rows(self):
        for row in self._board:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]
        return -1

    def _check_columns(self):
        transposed_board = [list(x) for x in zip(*self._board)]
        for row in transposed_board:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]
        return -1

    def _check_diagonals(self):
        if (len({self._board[i][i] for i in range(3)}) == 1 and
                self._board[0][0] != ' '):
            return self._board[0][0]
        if (len({self._board[i][2 - i] for i in range(3)}) == 1 and
                self._board[0][2] != ' '):
            return self._board[0][len(self._board)-1]
        return -1

    def check_winner(self):
        result_row = self._check_rows()
        if result_row != -1:
            return result_row
        result_col = self._check_columns()
        if result_col != -1:
            return result_col

        return self._check_diagonals()

    def is_full_board(self):
        return len([val for row in self._board
                    for val in row if val != ' ']) == 9

    def _get_next_player(self):
        if self._current_player == 'X':
            return 'O'
        return 'X'

    @staticmethod
    def _get_position_from_input(arg):
        return int(arg) - 1

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_board):
        self._board = new_board

    @property
    def current_player(self):
        return self._current_player


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
