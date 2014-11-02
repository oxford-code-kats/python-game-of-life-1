
class UI(object):
    def __init__(self, max=2000):
        self.steps = 0
        self.MAX = max

    def show(self, board):
        print "-------"
        popn = 1
        for y in range(board.height):
            line = ""
            for x in range(board.width):
                if board.is_alive(x, y):
                    popn += 1
                    line += " *"
                else:
                    line += "  "
            print line, "|"
        print "(step =", self.steps, "population =", popn,")"

    def running(self):
        self.steps += 1
        return self.steps < self.MAX

    def stable(self, board):
        print "BOARD STABLE"

def rand_bool(n=4):
    from random import randint
    return randint(0, n) == 0

def random_board(size):
    from board import Board
    board = Board.blank(size, size)
    for x in range(board.width):
        for y in range(board.height):
            if rand_bool():
                board.set_cell(x, y, True)
    return board

def main(args):
    from optparse import OptionParser, Option
    parser = OptionParser("", [
        Option('-b', '--board'),
        Option('-s', '--size', default=40),
        Option('-d', '--delay', default=0.1),
        Option('-a', '--automaton', default='Conway'),
        ])
    opts, args = parser.parse_args(args)
    size = int(opts.size)
    delay = float(opts.delay)
    board_name = opts.board
    automaton_name = opts.automaton
    automaton = None
    if automaton_name:
        import automata
        automaton = automata.make_automaton(automaton_name)
    if board_name is None:
        board = random_board(size)
    else:
        board = get_board(board_name)
    run(board, delay=delay, automaton=automaton)

def run(board, delay=0.1, automaton=None):
    from game import Game
    from board import Board
    ui = UI()
    game = Game(board, automaton=automaton)
    game.play(ui, delay=delay)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

