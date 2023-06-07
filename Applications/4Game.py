EMPTY = "."


class Game:
    def __init__(self):
        self.board = [[EMPTY for _ in range(7)] for _ in range(6)]
        self.game_over = False
        self.winner = None
        self.last_move = None
        self.players = ("x", "o")
        self.turn = 0

    def play(self):
        while not self.game_over:
            self.print_board()
            self.move(self.players[self.turn])
            self.check_win()

        self.print_outcome()

    def print_board(self):
        for row in self.board:
            print("".join(row))

    def move(self, player):
        column = input("{0}'s turn to move: ".format(player))
        while not self.is_valid(column):
            column = input("Move not valid. Please try again: ")

        row, column = 5, int(column) - 1
        while self.board[row][column] != EMPTY:
            row -= 1

        self.board[row][column] = player
        self.turn = 1 - self.turn
        self.last_move = (row, column)

    def is_valid(self, column):
        try:
            column = int(column) - 1
        except ValueError:
            return False
        if 0 <= column <= 6 and self.board[0][column] == EMPTY:
            return True
        return False

    def check_win(self):
        row, column = self.last_move

        horizontal = self.board[row]
        vertical = [self.board[i][column] for i in range(6)]

        negative_offset, positive_offset = column - row, column + row
        negative_diagonal = [
            row[i + negative_offset]
            for i, row in enumerate(self.board)
            if 0 <= i + negative_offset <= 6
        ]
        positive_diagonal = [
            row[-i + positive_offset]
            for i, row in enumerate(self.board)
            if 0 <= -i + positive_offset <= 6
        ]
        possible_wins = [horizontal, vertical, positive_diagonal, negative_diagonal]
        for possible_win in possible_wins:
            for i in range(len(possible_win) - 3):
                if len(set(possible_win[i : i + 4])) == 1 and possible_win[i] != EMPTY:
                    self.game_over = True
                    self.winner = possible_win[i]
                    break

        if all(self.board[0][column] != EMPTY for column in range(7)):
            self.game_over = True

    def print_outcome(self):
        self.print_board()
        if not self.winner:
            print("Game over: it was a draw!")
        else:
            print("Game over: {0} won!".format(self.winner))
