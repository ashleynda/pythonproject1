import unittest

from tests.Board import Board


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_that_we_can_create_board(self):
        self.assertIsNotNone(self.board)

    def test_that_board_is_empty(self):
        self.assertTrue(self.board.isEmpty())

    def test_that_player_moves_board_is_not_empty(self):
        self.board.move("1", 2)
        self.assertFalse(self.board.isEmpty())

    def test_that_board_is_filled(self):
        self.board.move("1", 2)
        self.assertTrue(self.board.isFilled())


if __name__ == '__main__':
    unittest.main()
