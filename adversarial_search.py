from math import inf
from evaluation import evaluate

def ordered_moves(game, state):
    return sorted(game.actions(state))

def minimax(game, state):
    turn = game.player(state)

    def max_layer(s):
        if game.terminal(s):
            return game.utility(s), None
        best_score = -inf
        best_move = None
        for mv in ordered_moves(game, s):
            scr, _ = min_layer(game.result(s, mv))
            if scr > best_score:
                best_score, best_move = scr, mv
        return best_score, best_move

    def min_layer(s):
        if game.terminal(s):
            return game.utility(s), None
        best_score = inf
        best_move = None
        for mv in ordered_moves(game, s):
            scr, _ = max_layer(game.result(s, mv))
            if scr < best_score:
                best_score, best_move = scr, mv
        return best_score, best_move

    return max_layer(state)[1] if turn == "X" else min_layer(state)[1]


def alphabeta(game, state):
    turn = game.player(state)

    def max_layer(s, a, b):
        if game.terminal(s):
            return game.utility(s), None
        move_best = None
        v = -inf
        for mv in ordered_moves(game, s):
            new_val, _ = min_layer(game.result(s, mv), a, b)
            if new_val > v:
                v, move_best = new_val, mv
            if v >= b:
                break
            a = max(a, v)
        return v, move_best

    def min_layer(s, a, b):
        if game.terminal(s):
            return game.utility(s), None
        move_best = None
        v = inf
        for mv in ordered_moves(game, s):
            new_val, _ = max_layer(game.result(s, mv), a, b)
            if new_val < v:
                v, move_best = new_val, mv
            if v <= a:
                break
            b = min(b, v)
        return v, move_best

    return max_layer(state, -inf, inf)[1] if turn == "X" else min_layer(state, -inf, inf)[1]


def depth_limited(game, state, depth):
    turn = game.player(state)

    def max_layer(s, d, a, b):
        if game.terminal(s):
            return game.utility(s), None
        if d == 0:
            return evaluate(game, s), None
        v = -inf
        best = None
        for mv in ordered_moves(game, s):
            temp, _ = min_layer(game.result(s, mv), d - 1, a, b)
            if temp > v:
                v, best = temp, mv
            if v >= b:
                break
            a = max(a, v)
        return v, best

    def min_layer(s, d, a, b):
        if game.terminal(s):
            return game.utility(s), None
        if d == 0:
            return evaluate(game, s), None
        v = inf
        best = None
        for mv in ordered_moves(game, s):
            temp, _ = max_layer(game.result(s, mv), d - 1, a, b)
            if temp < v:
                v, best = temp, mv
            if v <= a:
                break
            b = min(b, v)
        return v, best

    return (max_layer if turn == "X" else min_layer)(state, depth, -inf, inf)[1]
