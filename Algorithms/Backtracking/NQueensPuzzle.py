def n_queens(n, board=[]):
    # If all queens have been placed on the board,
    # a solution has been found.
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            # If the current queen could be placed then try to
            # place the next queen.
            count += n_queens(n, board)
        board.pop()
    return count


def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]

    # Check if any queens can attack the last queen.
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False

    return True
