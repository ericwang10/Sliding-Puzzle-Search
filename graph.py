import graphviz
#import pygraphviz as pgv #Not needed, same as graphviz
# import the cv2 library
import cv2
from tree import *

class Graph:
    def __init__(self, board):
        self.board = board

    def draw(self):
        puzzleTree = PuzzleTree()
        node = puzzleTree.insert(self.draw_board(self.board), p=None)
        node1 = puzzleTree.insert(self.draw_board(self.board), p=node)
        node2 = puzzleTree.insert(self.draw_board(self.board), p=node)

        print("BOARD VISUALIZED IS " + self.draw_board(self.board))
        dot = puzzleTree.visualize()
        # display(dot)
        #
        #
        # dot = graphviz.Digraph('round-table', comment='The Round Table', format='png')
        #
        # dot.node('A', 'King Arthur')
        # dot.node('B', 'Sir Bedevere the Wise')
        # dot.node('L', 'Sir Lancelot the Brave')
        #
        # dot.edges(['AB', 'AL'])
        # dot.edge('B', 'L', constraint='false')
        dot.render(directory='doctest-output', view = False) #view = true will open up the image
    def display(self):
        img = cv2.imread('doctest-output/puzzle tree graph.gv.png', 0)

        # The function cv2.imshow() is used to display an image in a window.
        cv2.imshow('graycsale image', img)

        # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
        cv2.waitKey(0)

        # cv2.destroyAllWindows() simply destroys all the windows we created.
        cv2.destroyAllWindows()
    def draw_board(self, board):
        board_string = ""
        for row in board:
            numbers = "[" + ''.join(str(x) for x in row) + "]"
            board_string += numbers
            board_string += "\\n" #for some reason, have to use double backslash on pycharm!! compared to colab
        return board_string
    # def pyDraw(self):
    #     A = pgv.AGraph()
    #     # add some edges
    #     A.add_edge(1, 2)
    #     A.add_edge(2, 3)
    #     A.add_edge(1, 3)
    #     A.add_edge(3, 4)
    #     A.add_edge(3, 5)
    #     A.add_edge(3, 6)
    #     A.add_edge(4, 6)
    #     # make a subgraph with rank='same'
    #     B = A.add_subgraph([4, 5, 6], name="s1", rank="same")
    #     B.graph_attr["rank"] = "same"
    #     print(A.string())  # print dot file to standard output
    #     A.draw("subgraph.png", prog="neato")


