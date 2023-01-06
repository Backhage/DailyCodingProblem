EMPTY = 0


def sudoku(board):
    if is_complete(board):
        return board

    row, col = get_next_empty(board)

    for i in range(1, 10):
        if can_place(board, i, row, col):
            board[row][col] = i
            sudoku(board)
            if is_complete(board):
                return board
            board[row][col] = EMPTY

    return None


def is_complete(board):
    for row in board:
        for ch in row:
            if ch == EMPTY:
                return False

    return True


def get_next_empty(board):
    for i, row in enumerate(board):
        for j, ch in enumerate(row):
            if ch == EMPTY:
                return i, j

    return None, None


def can_place(board, val, row, col):
    for i in range(len(board[0])):
        if board[row][i] == val:
            return False
        if board[i][col] == val:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val:
            return False
    return True
