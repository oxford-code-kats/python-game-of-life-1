
def main(args):
    from optparse import OptionParser, Option
    parser = OptionParser("", [
        Option('-b', '--board'),
        Option('-s', '--size', default=40),
        Option('-t', '--steps', default=2000),
        Option('-d', '--delay', default=0.1),
        Option('-p', '--probability', default=0.2),
        Option('-a', '--automaton', default='Conway'),
        ])
    opts, args = parser.parse_args(args)
    size = int(opts.size)
    delay = float(opts.delay)
    board_name = opts.board
    steps = int(opts.steps)
    automaton_name = opts.automaton
    p_value = opts.probability
    automaton = None
    if automaton_name:
        import automata
        automaton = automata.make_automaton(automaton_name)
    if board_name is None:
        from board import Board
        board = Board.random_board(size, chance=p_value)
    else:
        board = get_board(board_name)
    run(board, delay=delay, automaton=automaton, steps=steps)

def run(board, delay=0.1, automaton=None, steps=2000):
    from game import Game
    from board import Board
    from ui import UI
    ui = UI(max=steps)
    game = Game(board, automaton=automaton)
    game.play(ui, delay=delay)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

