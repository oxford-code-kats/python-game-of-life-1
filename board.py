
class Board(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.validate(matrix)

    def __eq__(self, other):
        return self.as_int_matrix() == other.as_int_matrix()

    def validate(self, matrix):
        pass

    def is_alive(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.width:
            return False
        if y >= self.height:
            return False
        return bool(self.matrix[y][x])

    @property
    def width(self):
        return len(self.matrix[0])

    @property
    def height(self):
        return len(self.matrix)

    def set_cell(self, x, y, alive):
        self.matrix[y][x] = alive

    def as_int_matrix(self):
        return [[1 if x else 0
                for x in row] for row in self.matrix]

    def count_live_neighbours(self, x0, y0):
        count = 0
        for x in [x0-1, x0, x0+1]:
            for y in [y0-1, y0, y0+1]:
                if x == x0 and y == y0:
                    # Skip the center
                    continue
                if self.is_alive(x, y):
                    count += 1
        return count

    @staticmethod
    def blank(width, height):
        matrix = [width*[0] for i in range(height)]
        return Board(matrix)

    @staticmethod
    def random_board(size):
        def rand_bool(n=4):
            from random import randint
            return randint(0, n) == 0
        board = Board.blank(size, size)
        for x in range(board.width):
            for y in range(board.height):
                if rand_bool():
                    board.set_cell(x, y, True)
        return board

    

