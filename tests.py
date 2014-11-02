import unittest 

class TestBoard(unittest.TestCase):
    def setUp(self):
        from board import Board
        self.board = Board.blank(3,3)

    def test_cells_can_be_set(self):
        self.board.set_cell(0, 1, True)
        self.failUnless(self.board.is_alive(0, 1),
                self.board.as_int_matrix())

    def test_cells_out_of_range_are_dead(self):
        self.failIf(self.board.is_alive(-1, -1),
                self.board.as_int_matrix())

    def test_blank(self):
        self.assertEqual([
            [0,0,0],
            [0,0,0],
            [0,0,0],
                ], self.board.as_int_matrix())

    def test_live_neighbours(self):
        self.board.set_cell(0, 0, True)
        self.board.set_cell(1, 0, True)
        lives = [[self.board.count_live_neighbours(x, y)
                    for x in range(self.board.width)]
                        for y in range(self.board.height)]
        self.assertEqual([
            [1,1,1],
            [2,2,1],
            [0,0,0],
            ], lives)

class TestGame(unittest.TestCase):
    def next(self, board):
        from game import Game
        game = Game(board)
        return game.step().as_int_matrix()

    def test_blank(self):
        actual = self.next([
            [0,0,0],
            [0,0,0],
            [0,0,0],
            ])
        self.assertEqual([
            [0,0,0],
            [0,0,0],
            [0,0,0],
                ], actual)

    def test_full(self):
        actual = self.next([
            [1,1,1],
            [1,1,1],
            [1,1,1],
            ])
        self.assertEqual([
            [1,0,1],
            [0,0,0],
            [1,0,1],
                ], actual)

    def test_one_cell(self):
        actual = self.next([
            [1,0,0],
            [0,0,0],
            [0,0,0],
            ])
        self.assertEqual([
            [0,0,0],
            [0,0,0],
            [0,0,0],
                ], actual)

    def test_under_population(self):
        actual = self.next([
            [0,1,1],
            [0,0,0],
            [0,0,0],
            ])
        self.assertEqual([
            [0,0,0],
            [0,0,0],
            [0,0,0],
                ], actual)

    def test_reproduction(self):
        actual = self.next([
            [1,1,0],
            [1,0,0],
            [0,0,0],
            ])
        self.assertEqual([
            [1,1,0],
            [1,1,0],
            [0,0,0],
                ], actual)

    def test_over_population(self):
        actual = self.next([
            [0,1,0],
            [1,1,1],
            [0,1,0],
            ])
        self.assertEqual([
            [1,1,1],
            [1,0,1],
            [1,1,1],
                ], actual)

    def test_normal_survival(self):
        actual = self.next([
            [0,1,0],
            [1,1,1],
            [0,0,0],
            ])
        self.assertEqual([
            [1,1,1],
            [1,1,1],
            [0,1,0],
                ], actual)


