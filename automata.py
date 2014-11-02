
def make_automaton(name, *t, **k):
    klass = globals().get(name, Conway)
    return klass(*t, **k)

class Automaton(object):
    def gen_board(self, board):
        from board import Board
        new_board = Board.blank(board.width, board.height)
        for x in range(board.width):
            for y in range(board.height):
                is_alive = self.cell_lives(board, x, y)
                new_board.set_cell(x, y, is_alive)
        return new_board

class Conway(Automaton):
    def __init__(self):
        pass
    
    def cell_lives(self, board, x, y):
        was_alive = board.is_alive(x, y)
        live_neighbours = board.count_live_neighbours(x, y)
        if was_alive:
            is_alive = True
            if live_neighbours < 2:
                is_alive = False
            if live_neighbours > 3:
                is_alive = False
        else:
            is_alive = False
            if live_neighbours == 3:
                is_alive = True
        return is_alive

class Seeds(Automaton):
    def cell_lives(self, board, x, y):
        return board.count_live_neighbours(x, y) == 2
    
class NoDeath(Conway):
    def cell_lives(self, board, x, y):
        return board.is_alive(x, y) \
                or super(NoDeath, self).cell_lives(board, x, y)
