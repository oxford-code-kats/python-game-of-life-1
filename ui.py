
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

