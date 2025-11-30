from engine_refactored import TicTacToe
from search_refactored import alphabeta, depth_limited

HUMAN = "X"
DEPTH = 4

def show(board):
    print("\nBoard:")
    for i, row in enumerate(board):
        print(i, "|", " ".join(row))
    print("   ", " ".join(str(x) for x in range(len(board))))

def get_move(game, board):
    legal = set(game.actions(board))
    while True:
        try:
            move = input("Your move (row col): ").split()
            r, c = int(move[0]), int(move[1])
            if (r, c) in legal:
                return (r, c)
            print("Invalid square.")
        except:
            print("Wrong format.")

def ai_move(game, board):
    if game.m == 3 and game.k == 3:
        return alphabeta(game, board)
    return depth_limited(game, board, DEPTH)

def main():
    game = TicTacToe(3, 3)
    board = game.initial
    print("Generalized Tic-Tac-Toe")
    print("You are:", HUMAN)

    while not game.terminal(board):
        show(board)
        turn = game.player(board)

        if turn == HUMAN:
            mv = get_move(game, board)
        else:
            print("AI thinking...")
            mv = ai_move(game, board)
            print("AI plays:", mv)

        board = game.result(board, mv)

    show(board)
    w = game.winner(board)
    print("\nGame Over. Winner:", w if w else "Draw")

if __name__ == "__main__":
    main()
