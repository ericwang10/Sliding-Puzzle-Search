from settings import *
import copy
import numpy as np
from tree import *
class AI:
    def __init__(self, board, target_board):
        self.board = board
        self.possible_moves = []
        self.print_board(self.board)
        self.target_board = target_board

    def find_best_moves(self, moveset): #this method finds the best move given heuristics
        #self.board = board
        self.print_board(self.board)


        #return best movev
        move_heuristics = []
        print("POSSIBLE MOVES\n\n")
        for move in moveset:
            heuristic = self.get_heuristics(move,self.target_board)
            self.print_board(move)
            print("heuristic for this board is ", heuristic)
            print("\n\n")
            move_heuristics.append(heuristic)

        #convert to np array
        move_heuristics = np.asarray(move_heuristics)
        best_move_index = np.argmin(move_heuristics)

        return moveset[best_move_index]

    def get_possible_moves(self, board):
        possible_moves = []
        row_idx = 0
        col_idx = 0
        zero_row = 0
        zero_col = 0
        for row in board:  # 0, [] / 1, [] / 2, []
            col_idx = 0
            for col in row:
                if col == 0:
                    print("this one is zero", row_idx, col_idx)
                    zero_row = row_idx
                    zero_col = col_idx
                col_idx += 1
            row_idx += 1

        # reset possible moves to prevent it from adding previous ones

        if zero_row > 0:  # up
            up_board = copy.deepcopy(board)
            # swap zero and above element
            temp = up_board[zero_row - 1][zero_col]  # previous element above
            up_board[zero_row - 1][zero_col] = 0  # change to zero
            up_board[zero_row][zero_col] = temp  # swap previous empty tile with above element
            possible_moves.append(up_board)
        if zero_row < GAME_SIZE - 1:  # down
            down_board = copy.deepcopy(board)
            # swap zero and above element
            temp = down_board[zero_row + 1][zero_col]  # previous element above
            down_board[zero_row + 1][zero_col] = 0  # change to zero
            down_board[zero_row][zero_col] = temp  # swap previous empty tile with above element
            possible_moves.append(down_board)
        if zero_col > 0:  # left
            left_board = copy.deepcopy(board)
            # swap zero and above element
            temp = left_board[zero_row][zero_col - 1]  # previous element above
            left_board[zero_row][zero_col - 1] = 0  # change to zero
            left_board[zero_row][zero_col] = temp  # swap previous empty tile with above element
            possible_moves.append(left_board)
        if zero_col < GAME_SIZE - 1:  # right
            right_board = copy.deepcopy(board)
            # swap zero and above element
            temp = right_board[zero_row][zero_col + 1]  # previous element above
            right_board[zero_row][zero_col + 1] = 0  # change to zero
            right_board[zero_row][zero_col] = temp  # swap previous empty tile with above element
            possible_moves.append(right_board)
        return possible_moves

    def greedy_search(self, start, goal):
        #graphing
        #OK I THINK YOU ADD THEM AS CHILD, NOT PARENT...
        root = TreeNode(start, self.get_heuristics(start, goal))

        visited = []  # list of visited nodes
        to_explore = self.get_possible_moves(start)  # list of nodes to explore from start, array of possible board states, 3d list
        explore_nodes = []
        #create first few bits of the tree
        for state in to_explore:
            currentNode = TreeNode(state, self.get_heuristics(state, goal), parent=root)
            #print("currentNode heuristic is", currentNode.heuristic)
            root.add_child(currentNode)
            explore_nodes.append(currentNode)

        while explore_nodes:
            # Choose the next node to explore based on the heuristic function
            current = self.find_best_moves(to_explore)
            currentNode = self.get_best_node(explore_nodes) #THESE ARE DISJOINT...
            print("current should be", current)
            print("currentNode should be", currentNode.key)

            if current == goal:
                print("current is")
                self.print_board(current)
                visited.append(current) #finally, add last one into visited!
                currentNode.color = "green"
                puzzletree = PuzzleTree()
                puzzletree.root = root
                dot = puzzletree.visualize()
                dot.render(directory='doctest-output', view=True)  # view = true will open up the image
                return currentNode  # goal node found, return it

            ##visiting node
            to_explore.remove(current)
            explore_nodes.remove(currentNode)
            visited.append(current)
            # graph stuff

            for neighbor in self.get_possible_moves(current):
                if neighbor not in visited:

                    nextNode = TreeNode(neighbor, self.get_heuristics(neighbor, goal), parent=currentNode) #make sure this is the next state which is neighbor, not current

                    currentNode.add_child(nextNode)

                    to_explore.append(neighbor)
                    explore_nodes.append(nextNode)
            # #new root is the currentNode now
            # root = currentNode
        return None  # goal node not found
    def get_best_node(self, fringe):
        h_vals = [node.heuristic for node in fringe]
        h_vals = np.array(h_vals)
        h_val_idx = np.argmin(h_vals)
        return fringe[h_val_idx]

    def get_heuristics(self, current_board, target_board):
        target_board = np.array(target_board)
        current_board = np.array(current_board)
        heuristic = target_board - current_board
        heuristic = np.absolute(heuristic)
        return np.sum(heuristic)

    def print_board(self, board):
        for row in board:
            print(row)
