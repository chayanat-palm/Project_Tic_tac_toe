class TicTacToe:
    def __init__(self):
        self.placeholder = "-"
        self.board = [[self.placeholder for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.game_over = False

    def check_win(self):
        # Check win in row
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != self.player:
                    win = False
                    break
            if win:
                return win

        # Check win in column
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != self.player:
                    win = False
                    break
            if win:
                return win

        # Check win in diagonal
        win = True
        for i in range(3):
            if self.board[i][i] != self.player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(3):
            if self.board[i][3 - 1 - i] != self.player:
                win = False
                break
        if win:
            return win

    def check_tie(self):
        # Check for tie
        tie = True
        for row in self.board:
            for item in row:
                if item == '-':
                    tie = False
                    break
        if tie:
            return tie

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def print_board(self):
        for i, row in enumerate(self.board):
            pattern = " | ".join(str(b) for b in row)
            print(pattern)
            if i < len(self.board) - 1:
                print("----------")

    def play_game(self):
        while not self.game_over:
            # Update board
            spot_row, spot_column = None, None
            while spot_row is None or spot_column is None:
                self.print_board()
                print(f"It's {self.player}'s turn")
                try:
                    spot_row, spot_column = map(int, input('Enter the spot by row and column: ').strip().split(" "))
                except ValueError:
                    print("The Pattern Input is 1 1 or 1 2 or 2 2, Please re-enter spot.")

            if spot_row < 1 or spot_row > 3 or spot_column < 1 or spot_column > 3:
                switch = False
                print("The spot is out of range, please re-enter spot.")
            elif self.board[spot_row - 1][spot_column - 1] != self.placeholder:
                switch = False
                print("It's already spot, please re-enter new spot.")
            else:
                switch = True
                self.board[spot_row - 1][spot_column - 1] = self.player

            # Check for win or tie
            if self.check_win():
                self.print_board()
                return print(f"The winner👑👑👑 is {self.player} player.")
            if self.check_tie():
                self.print_board()
                return print(f"Tied Game.")
            if switch:
                self.switch_player()


game = TicTacToe()

while input("Do you want to play a game of Tic tae toe? Type 'y' or 'n': ") == 'y':
    game = TicTacToe()
    game.play_game()