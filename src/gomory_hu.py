from collections import deque
from sys import maxsize as maxint
from lib.test import *

BLACK = 2
GRAY = 1
WHITE = 0


class GomoryHuTree:

    def __init__(self, graph):
        self.V = len(graph)
        self.capacity = {}
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = graph[i][j]
        self.color = {}
        self.pred = {}
        self.tree = {}
        self.flow = {}
        self.depth = {}
        self.graph = graph 

        self.build()
        self.prepare()

    def __repr__(self):
        return self.tree

    def __str__(self):
        return str(self.tree)

    def __getitem__(self, pos):
        i, j = pos
        return self.tree[i, j]


    def build(self):
        """Construct GomoryHuTree"""
        p = []
        f1 = []

        for i in range(self.V):
            p.append(0)
            f1.append(0)
            for j in range(self.V):
                self.tree[i, j] = 0

        for s in range(1, self.V):

            t = p[s]

            min_cut, self.color, self.pred, self.depth, self.flow = test_max_flow(self.graph, s, t, self.color, self.pred, self.depth, self.flow)

            f1[s] = min_cut

            for i in range(self.V):
                if i != s and p[i] == t and self.color[i] == BLACK:
                    p[i] = s

            if self.color[p[t]] == BLACK:
                p[s] = p[t]
                p[t] = s
                f1[s] = f1[t]
                f1[t] = min_cut

            if s == self.V - 1:
                for i in range(1, s + 1):
                    self.tree[i, p[i]] = f1[i]

    def prepare(self):
        """Prepare for querying"""
        for i in range(self.V):
            for j in range(self.V):
                self.capacity[i, j] = self.tree[i, j]

    def query(self, u, v):
        """Query GomoryHuTree"""
        min_cut1, self.color, self.pred, self.depth, self.flow = test_max_flow(self.graph, u, v, self.color, self.pred, self.depth, self.flow)
        min_cut2, self.color, self.pred, self.depth, self.flow = test_max_flow(self.graph, v, u, self.color, self.pred, self.depth, self.flow)

        return max(min_cut1, min_cut2)



graph = [[0, 1, 7, 0, 0, 0],
         [1, 0, 1, 3, 2, 0],
         [7, 1, 0, 0, 4, 0],
         [0, 3, 0, 0, 1, 6],
         [0, 2, 4, 1, 0, 2],
         [0, 0, 0, 6, 2, 0]]

# Construct GomoryHuTree
tree = GomoryHuTree(graph)

# Print Tree Contents
print(tree)

# Query for min cut between 0 and 4
print(tree.query(2, 0))
print(tree.query(0, 2))

# Print the edge (0, 3)
print(tree[0, 3])