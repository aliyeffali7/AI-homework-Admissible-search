import pytest
from core_game import TicTacToe
from adversarial_search import minimax, alphabeta, depth_limited
from evaluation import evaluate


# ------------------------------
# Basic rule correctness
# ------------------------------

def test_empty_board_initialization():
    game = TicTacToe(3, 3)
    state = game.initial
    assert all(cell == "." for row in state for cell in row)
    assert game.player(state) == "X"
    assert len(game.actions(state)) == 9


def test_turn_rotation():
    game = TicTacToe(3, 3)
    b0 = game.initial

    b1 = game.result(b0, (0, 0))
    assert game.player(b1) == "O"

    b2 = game.result(b1, (1, 1))
    assert game.player(b2) == "X"


# ------------------------------
# Winner detection tests
# ------------------------------

@pytest.mark.parametrize("board,expected", [
    ([["X","X","X"], [".",".","."], [".",".","."]], "X"),
    ([["O",".","."], ["O",".","."], ["O",".","."]], "O"),
    ([["X",".","."], [".","X","."], [".",".","X"]], "X"),
    ([[".",".","O"], [".","O","."], ["O",".","."]], "O"),
])
def test_winner_detection(board, expected):
    game = TicTacToe(3, 3)
    assert game.winner(board) == expected
    assert game.terminal(board) is True


def test_draw_case():
    game = TicTacToe(3, 3)
    state = [
        ["X","O","X"],
        ["O","X","O"],
        ["O","X","O"]
    ]
    assert game.winner(state) is None
    assert game.terminal(state) is True
    assert game.utility(state) == 0


# ------------------------------
# Search correctness
# ------------------------------

def test_minimax_matches_alpha_beta_on_start():
    game = TicTacToe(3, 3)
    st = game.initial
    assert minimax(game, st) == alphabeta(game, st)


def test_midgame_minimax_alpha_beta_consistency():
    game = TicTacToe(3, 3)
    st = [
        ["X","O","."],
        [".","X","."],
        ["O",".","."]
    ]
    assert minimax(game, st) == alphabeta(game, st)


# ------------------------------
# Heuristic behavior
# ------------------------------

def test_heuristic_zero_on_empty():
    game = TicTacToe(4, 3)
    assert evaluate(game, game.initial) == 0


def test_heuristic_identifies_threats():
    game = TicTacToe(4, 3)

    board_x = [
        ["X","X","." , "."],
        ["." ,"." ,"." , "."],
        ["." ,"." ,"." , "."],
        ["." ,"." ,"." , "."],
    ]

    board_o = [
        ["O","O","." , "."],
        ["." ,"." ,"." , "."],
        ["." ,"." ,"." , "."],
        ["." ,"." ,"." , "."],
    ]

    assert evaluate(game, board_x) > 0
    assert evaluate(game, board_o) < 0


# ------------------------------
# Depth limited correctness
# ------------------------------

def test_depth_agent_takes_immediate_win():
    game = TicTacToe(3,3)
    st = [
        ["X","X","."],
        ["O","O","."],
        [".",".","."]
    ]
    mv = depth_limited(game, st, 1)
    assert mv == (0, 2)


def test_depth_agent_blocks_win():
    game = TicTacToe(3,3)
    st = [
        ["O","O","."],
        ["X","X","."],
        [".",".","."]
    ]
    mv = depth_limited(game, st, 2)
    assert mv == (0, 2)
