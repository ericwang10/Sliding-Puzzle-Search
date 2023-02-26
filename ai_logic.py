from settings import *
import copy
import numpy as np
class AI:
    def __init__(self, board, target_board):
        self.board = board
        self.possible_moves = []
        self.print_board(self.board)
        self.target_board = target_board
    def find_moves(self, board):
        self.board = board
        self.print_board(self.board)

        row_idx = 0
        col_idx = 0
        for row in self.board: #0, [] / 1, [] / 2, []
            col_idx = 0
            for col in row:
                if col == 0:
                    print("this one is zero", row_idx, col_idx)
                    self.possibilities(row_idx, col_idx) #don't need to call self again
                col_idx += 1
            row_idx += 1
        print("POSSIBLE MOVES\n\n")
        for move in self.possible_moves:
            self.print_board(move)
            print("heuristic for this board is ", self.get_heuristics(move,self.target_board))
            print("\n\n")
    def possibilities(self, row, col):

        if row > 0 : #up
            up_board = copy.deepcopy(self.board)
            #swap zero and above element
            temp = up_board[row-1][col] #previous element above
            up_board[row-1][col] = 0 #change to zero
            up_board[row][col] = temp #swap previous empty tile with above element
            self.possible_moves.append(up_board)
        if row < GAME_SIZE - 1: #down
            down_board = copy.deepcopy(self.board)
            # swap zero and above element
            temp = down_board[row + 1][col]  # previous element above
            down_board[row + 1][col] = 0  # change to zero
            down_board[row][col] = temp  # swap previous empty tile with above element
            self.possible_moves.append(down_board)
        if col > 0: #left
            left_board = copy.deepcopy(self.board)
            # swap zero and above element
            temp = left_board[row][col - 1]  # previous element above
            left_board[row][col - 1] = 0  # change to zero
            left_board[row][col] = temp  # swap previous empty tile with above element
            self.possible_moves.append(left_board)
        if col < GAME_SIZE - 1: #right
            right_board = copy.deepcopy(self.board)
            # swap zero and above element
            temp = right_board[row][col + 1]  # previous element above
            right_board[row][col + 1] = 0  # change to zero
            right_board[row][col] = temp  # swap previous empty tile with above element
            self.possible_moves.append(right_board)
    def get_heuristics(self, current_board, target_board):
        target_board = np.array(target_board)
        current_board = np.array(current_board)
        heuristic = target_board - current_board
        heuristic = np.absolute(heuristic)
        return np.sum(heuristic)

    def get_possible_moves(self):
        return self.possible_moves


    def print_board(self, board):
        for row in board:
            print(row)