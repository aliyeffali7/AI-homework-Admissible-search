class TicTacToe:
    def __init__(self, m=3, k=3):
        self.m = m
        self.k = k
        self.initial = [["." for _ in range(m)] for _ in range(m)]

    def player(self, board):
        marks = sum(board, [])
        return "X" if marks.count("X") == marks.count("O") else "O"

    def actions(self, board):
        output = []
        for r in range(self.m):
            for c in range(self.m):
                if board[r][c] == ".":
                    output.append((r, c))
        return output

    def result(self, board, move):
        r, c = move
        p = self.player(board)
        nxt = [row[:] for row in board]
        nxt[r][c] = p
        return nxt

    def _scan_line(self, line):
        """Checks if a single list contains k consecutive X or O."""
        streak = 1
        for i in range(1, len(line)):
            if line[i] != "." and line[i] == line[i - 1]:
                streak += 1
                if streak >= self.k:
                    return line[i]
            else:
                streak = 1
        return None

    def winner(self, board):

        # rows
        for row in board:
            w = self._scan_line(row)
            if w:
                return w

        # columns
        for c in range(self.m):
            col = [board[r][c] for r in range(self.m)]
            w = self._scan_line(col)
            if w:
                return w

        # diagonals (method changed!)
        for r in range(self.m):
            for c in range(self.m):
                # diag down-right
                temp = []
                rr, cc = r, c
                while rr < self.m and cc < self.m:
                    temp.append(board[rr][cc])
                    rr += 1
                    cc += 1
                w = self._scan_line(temp)
                if w:
                    return w

                # diag down-left
                temp = []
                rr, cc = r, c
                while rr < self.m and cc >= 0:
                    temp.append(board[rr][cc])
                    rr += 1
                    cc -= 1
                w = self._scan_line(temp)
                if w:
                    return w

        return None

    def terminal(self, board):
        if self.winner(board):
            return True
        return all(board[r][c] != "." for r in range(self.m) for c in range(self.m))

    def utility(self, board):
        w = self.winner(board)
        if w == "X":
            return 1
        elif w == "O":
            return -1
        return 0
