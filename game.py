
class Game(object):
    def __init__(self, board):
        from board import Board
        from automata import Automaton
        self.automaton = Automaton()
        if not isinstance(board, Board):
            board = Board(board)
        self.board = board

    def step(self):
        new_board = self.automaton.gen_board(self.board)
        self.board = new_board
        return new_board

    def play(self, ui, delay=0.4):
        import time
        while ui.running():
            ui.show(self.board)
            self.step()
            time.sleep(delay)
