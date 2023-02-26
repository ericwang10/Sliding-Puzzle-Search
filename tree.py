import numpy as np
from graphviz import Digraph
from settings import *
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = [] #each node can have multiple children
        self.optimizer = None
        self.reward = None #reward is for determining the outcome of the game
        self.heuristic = None
    def to_string(self):
        return str(self.key)
    def print(self):
        print("TreeNode: %d" % (self.key))
    def add_child(self, node):
        self.children.append(node)


# class for creating our tree, which will explore all possible game options
class PuzzleTree():
    def __init__(self):
        self.root = None  # Root of the tree
        self.list = []  # Elements of the tree as list

    # Insert a new node
    def insert(self, k, p=None):  # self is object, k is key, parent is parent
        ''' Insert a key '''
        newNode = TreeNode(k)  # create a new node with our key. Our key is our game state in a string format
        # If the tree is empty, the new node is the root
        if self.root == None:
            print("tree is empty, new root node created")
            self.root = newNode
            newNode.optimzer = "max"
        else:  # tree not empty
            x = self.root
            newNode.parent = p  # make newNode's parent the parent we pass in
            if p != None:  # we want to add the child to the parent node's children list
                p.add_child(newNode)  # this way we can find all children from a parent

                # for determining minimax
                if p.optimzer == "max":  # we set the current node's status as min or max based on parent. This represents alternating turns
                    newNode.optimzer = "min"
                else:
                    newNode.optimzer = "max"

        return newNode  # return the node

    def height(self, x):
        if (x == None):
            return 0
        else:
            return 1 + np.maximum(self.height(x.left), self.height(x.right))

    # this method will visualize our tree
    # don't worry too much about the details, lots of formatting stuff
    def visualize(self, node=None):
        ''' Visualize the tree using graphviz '''
        tree = self.root

        # Recursively add nodes and edges, visualizing tree
        def add_nodes_edges(tree, dot=None):
            col = "black"
            # Create Graphviz Digraph
            if dot is None:
                dot = Digraph('puzzle tree graph', node_attr={'fixedsize': 'true', 'width': '2', "height": "2"},
                              # manually set node dimensions to prevent
                              graph_attr={'nodesep': "0.3"},
                              format='png',
                              edge_attr={"len": "1"})  # not working
                # dot.attr(len = "1")
                dot.attr(size=GRAPH_SIZE)  # adjust size

                # some formatting
                if (tree.reward != None):
                    node_value = tree.key + "\n\n" + str(tree.reward)
                else:
                    node_value = tree.key
                dot.node(name=str(tree), label=str(node_value),
                         color="green", shape="square", fixedsize="True",
                         width="0.2")  # adding a node shape helps with layout
            # Add nodes recursively
            for child in tree.children:
                if (child.optimzer == 'max'):
                    col = "green"
                else:
                    col = "red"
                if (child.reward != None):
                    node_value = child.key + "\n\n" + str(
                        child.reward)  # add this here so we can get the values of the nodes from minimax
                else:
                    node_value = child.key
                dot.node(name=str(child), label=str(node_value),
                         color=col, shape="square", fixedsize="True",
                         width="0.3")  # adding a node shape helps with layout
                test2 = str(child) + ":n"  # use port to make edges look better
                dot.edge(str(tree), str(test2))
                dot = add_nodes_edges(child, dot=dot)

            return dot

        return add_nodes_edges(tree)