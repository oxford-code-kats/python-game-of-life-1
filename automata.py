
class Automaton(object):
    def __init__(self):
        pass


    def gen_board(self, board):
        from board import Board
        new_board = Board.blank(board.width, board.height)
        for x in range(board.width):
            for y in range(board.height):
                was_alive = board.is_alive(x, y)
                live_neighbours = board.count_live_neighbours(x, y)
                if was_alive:
                    is_alive = True
                    if live_neighbours < 2:
                        is_alive = False
                    if live_neighbours > 3:
                        is_alive = False
                    raise RuntimeError(is_alive, x, y, board.as_int_matrix())
                else:
                    is_alive = False
                    if live_neighbours == 3:
                        is_alive = True
                new_board.set_cell(x, y, is_alive)
        return new_board



