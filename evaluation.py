def evaluate(game, board):
    m, k = game.m, game.k
    value = 0

    def score_line(line):
        nonlocal value
        for i in range(len(line) - k + 1):
            window = line[i:i + k]
            x = window.count("X")
            o = window.count("O")
            empty = window.count(".")
            if o == 0:   # only X present
                if x == k - 1 and empty == 1:
                    value += 120
                elif x == k - 2 and empty == 2:
                    value += 15
            if x == 0:   # only O present
                if o == k - 1 and empty == 1:
                    value -= 120
                elif o == k - 2 and empty == 2:
                    value -= 15

    # rows
    for r in range(m):
        score_line(board[r])

    # cols
    for c in range(m):
        col = [board[r][c] for r in range(m)]
        score_line(col)

    # diagonals
    for r in range(m):
        for c in range(m):
            # dr
            temp = []
            rr, cc = r, c
            while rr < m and cc < m:
                temp.append(board[rr][cc])
                rr += 1
                cc += 1
            score_line(temp)

            # dl
            temp = []
            rr, cc = r, c
            while rr < m and cc >= 0:
                temp.append(board[rr][cc])
                rr += 1
                cc -= 1
            score_line(temp)

    return value
