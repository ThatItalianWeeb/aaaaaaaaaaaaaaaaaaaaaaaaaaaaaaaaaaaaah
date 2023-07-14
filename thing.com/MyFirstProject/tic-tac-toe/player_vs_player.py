# This program is a 2-player Tic-Tac-Toe game.
from enum import Enum


class GridSquare():
    state = ""
    pos = 0

    def __init__(self, x):
        self.pos = x
        self.state = "-1"

    def draw_space(self):
        if self.state == "1":
            return 'X'
        if self.state == "0":
            return 'O'
        return str(self.pos)[0]


class TicTacToe():
    cols = 3
    rows = 3
    total_turns = 0
    winner = -1

    class game_state(Enum):
        OVER = 0
        RUNNING = 1

    current_state = game_state.OVER
    board = None

    def setup(self):
        self.board = [[None] * self.cols for _ in range(self.rows)]
        position = 1
        r = 0
        while r < self.rows:
            c = 0
            while c < self.cols:
                self.board[r][c] = GridSquare(position)
                position += 1
                c += 1
            r += 1
        TicTacToe.current_state = TicTacToe.game_state.RUNNING
        self.play_game()

    def play_game(self):
        while TicTacToe.current_state == TicTacToe.game_state.RUNNING:
            self.display_board()
            self.make_move()
        if TicTacToe.current_state == TicTacToe.game_state.OVER:
            self.display_game_over()

    def display_board(self):
        print("\n  " + str(self.board[0][0].draw_space()) + " | " + str(self.board[0][1].draw_space()) + "  | " + str(
            self.board[0][2].draw_space()))
        print(" ___|____|___ ")
        print("\n  " + str(self.board[1][0].draw_space()) + " | " + str(self.board[1][1].draw_space()) + "  | " + str(
            self.board[1][2].draw_space()))
        print(" ___|____|___ ")
        print("\n  " + str(self.board[2][0].draw_space()) + " | " + str(self.board[2][1].draw_space()) + "  | " + str(
            self.board[2][2].draw_space()))
        print(" ___|____|___ ")

    def make_move(self):
        print("Player " + str(self.get_player()) + " choose a pos: ")
        spot = input()
        i = 0
        while i < self.cols:
            j = 0
            while j < self.rows:
                if str(self.board[i][j].state) == "-1" and str(self.board[i][j].pos) == spot:
                    self.board[i][j].state = str(self.total_turns % 2)
                    self.total_turns += 1
                    self.check_win(i, j, str(self.board[i][j].state))
                j += 1
            i += 1

    def display_game_over(self):
        self.display_board()
        print("Game Over!")
        if self.winner == "1":
            print("X Wins")
        if self.winner == "0":
            print("O Wins")
        if self.total_turns == 9 and not (self.winner == "1") and not self.winner == "0":
            print("Tie!")

    def get_player(self):
        if self.total_turns % 2 == 0:
            return 'O'
        return 'X'

    def check_win(self, x, y, turn):
        # Check for a win going in every direction
        # Variables to account for each direction
        col_win = 0
        row_win = 0
        diag1_win = 0
        diag2_win = 0
        i = 0
        # Loop that iterates three times
        while i < 3:
            # Check 3 squares in a column.
            if self.board[x][i].state == turn:
                col_win += 1
            # Check 3 squares in a row.
            if self.board[i][y].state == turn:
                row_win += 1
            # Check 3 squares in diagonal.
            if self.board[i][i].state == turn:
                diag1_win += 1
            # Check 3 squares in 2nd diagonal.
            if self.board[i][2 - i].state == turn:
                diag2_win += 1
            i += 1
        if col_win == 3 or row_win == 3 or diag1_win == 3 or diag2_win == 3:
            self.winner = turn
            if self.winner != -1:
                TicTacToe.current_state = TicTacToe.game_state.OVER
        # If the number of turns reaches 9, end the game.
        if self.total_turns == 9:
            TicTacToe.current_state = TicTacToe.game_state.OVER


game_play = TicTacToe()
game_play.setup()