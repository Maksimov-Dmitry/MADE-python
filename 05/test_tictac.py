import unittest
from unittest.mock import patch, call, MagicMock

from tictac import TicTacGame


class TestTicTacGame(unittest.TestCase):
    """
    This class tests TicTacGame class.
    """

    def test_init_params(self):
        tic_tac = TicTacGame()
        expected_board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertListEqual(tic_tac.board, expected_board)
        self.assertEqual(tic_tac.current_player, 'X')

    @staticmethod
    @patch('builtins.print')
    def test_show_board(m_print):
        tic_tac = TicTacGame()
        tic_tac.board = [
            ['X', ' ', 'O'],
            ['X', 'X', 'O'],
            [' ', 'O', ''],
        ]
        expected_print_calls = [
            call('---+---+---'),
            call('X  |   |O'),
            call('---+---+---'),
            call('X  |X  |O'),
            call('---+---+---'),
            call('   |O  |'),
            call('---+---+---')
        ]
        tic_tac.show_board()
        m_print.assert_has_calls(expected_print_calls)

    def test_check_winner(self):
        tic_tac = TicTacGame()
        tic_tac.board = [
            ['X', ' ', 'O'],
            ['X', 'X', 'O'],
            [' ', 'O', ''],
        ]
        self.assertEqual(tic_tac.check_winner(), -1)
        tic_tac.board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(tic_tac.check_winner(), -1)
        tic_tac.board = [
            ['X', 'X', 'X'],
            [' ', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(tic_tac.check_winner(), 'X')
        tic_tac.board = [
            ['X', 'O', 'X'],
            [' ', 'O', 'O'],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(tic_tac.check_winner(), 'O')
        tic_tac.board = [
            ['O', 'O', 'X'],
            [' ', 'O', 'O'],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(tic_tac.check_winner(), 'O')
        tic_tac.board = [
            ['O', 'O', 'X'],
            [' ', 'X', 'O'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(tic_tac.check_winner(), 'X')

    @staticmethod
    @patch('builtins.print')
    @patch('builtins.input')
    def test_start_game_not_draw(m_input, m_print):
        tic_tac = TicTacGame()
        tic_tac.show_board = MagicMock()
        m_input.side_effect = ['ab', '1 1', '1 2', '1 2',
                               '1 3', '2 2', '2 1', '3 2']
        tic_tac.start_game()
        expected_print_calls = [
            call('Player X, it is your turn.'),
            call('Wrong input! You must enter 2 numbers separated by a space.'
                 ' However, 1 were entered.'),
            call('Player O, it is your turn.'),
            call('Wrong input! This place is already taken, '
                 'choose a free place.'),
            call('Player O, you won!'),
        ]
        tic_tac.show_board.assert_called()
        m_print.assert_has_calls(expected_print_calls, any_order=True)

    @staticmethod
    @patch('builtins.print')
    @patch('builtins.input')
    def test_start_game_draw(m_input, m_print):
        tic_tac = TicTacGame()
        tic_tac.show_board = MagicMock()
        m_input.side_effect = ['1.2 2', '1 1', '1 2', '0 3', '1 3', '2 2',
                               '3 2', '2 1', '3 2', '2 3', '3 3', '3 1']
        tic_tac.start_game()
        expected_print_calls = [
            call('Player X, it is your turn.'),
            call('Wrong input! You must enter 2 numbers separated by a space. '
                 'However, 1.2 is not a number.'),
            call('Player O, it is your turn.'),
            call('Wrong input! Numbers must be 1 or 2 or 3.'),
            call('The board is full - Draw.'),
        ]
        tic_tac.show_board.assert_called()
        m_print.assert_has_calls(expected_print_calls, any_order=True)
