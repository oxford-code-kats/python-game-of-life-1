
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
    size = 40
    board = None
    if args:
        if args[0] == '--board':
            board_name = args[1]
            board = get_board(board_name)
    if board is None:
        board = random_board(size)
    from game import Game
    from board import Board
    ui = UI()
    game = Game(board)
    delay = 0.1
    game.play(ui, delay=delay)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

