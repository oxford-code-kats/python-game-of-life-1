
class UI(object):
    def __init__(self, max=2000):
        self.steps = 0
        self.MAX = max

    def show(self, board):
        print "\n" * board.height
        print "--" * board.width
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
        result = self.steps < self.MAX
        if not result:
            print "Max steps reached - %s" %(self.MAX,)
        return result

    def stable(self, board):
        print "BOARD STABLE"

