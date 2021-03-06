
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

class ModularAutomaton(Automaton):
    def cell_lives(self, board, x, y):
        was_alive = board.is_alive(x, y)
        live_neighbours = board.count_live_neighbours(x, y)
        if was_alive:
            return self.survives(live_neighbours)
        else:
            return self.is_born(live_neighbours)
        return is_alive
    
    def survives(self, neighbours):
        return not self.is_killed(neighbours)

    def is_born(self, neighbours):
        return neighbours == 3

    def is_killed(self, neighbours):
        return neighbours not in (2, 3)

class Conway(ModularAutomaton):
    def is_born(self, neighbours):
        return neighbours == 3

    def is_killed(self, neighbours):
        return neighbours not in (2, 3)

class HighGrowth(ModularAutomaton):
    def is_born(self, neighbours):
        return neighbours in (3, 4)

    def is_killed(self, neighbours):
        return neighbours not in (2, 3)

class Seeds(Automaton):
    def cell_lives(self, board, x, y):
        return board.count_live_neighbours(x, y) == 2
    
class NoDeath(Conway):
    def cell_lives(self, board, x, y):
        return board.is_alive(x, y) \
                or super(NoDeath, self).cell_lives(board, x, y)

class HighLife(ModularAutomaton):
    def is_killed(self, neighbours):
        return neighbours not in (2, 3)

    def is_born(self, neighbours):
        return neighbours in (3,6)

class DayAndNight(Automaton):
    def cell_lives(self, board, x, y):
        alive = board.is_alive(x, y)
        if board.count_live_neighbours(x, y) in (3,6,7,8):
            return not alive
        return alive


