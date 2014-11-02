
class UI(object):
    MAX = 200

    def __init__(self):
        self.steps = 0

    def show(self, board):
        print "-------"
        for y in range(board.height):
            line = ""
            for x in range(board.width):
                if board.is_alive(x, y):
                    line += " *"
                else:
                    line += "  "
            print line, "|"

    def running(self):
        self.steps += 1
        return self.steps < self.MAX

def rand_bool(n=6):
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

def main():
    from game import Game
    SIZE = 30
    ui = UI()
    board = random_board(SIZE)
    game = Game(board)
    game.play(ui)

if __name__ == '__main__':
    main()

