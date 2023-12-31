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
                j += 1
            i += 1

    # def display_game_over(self):


    def get_player(self):
        if self.total_turns % 2 == 0:
            return 'O'
        return 'X'

game_play = TicTacToe()
game_play.setup()


game_play = TicTacToe()
game_play.setup()