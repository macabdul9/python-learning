"""
 @author    : macab (macab@debian)
 @file      : graph
 @created   : Friday Apr 19, 2019 05:00:22 IST
"""
import os
clear = lambda:os.system('clear')
clear()

class Graph:

    # initialize a list of size v -- v is no of vertex !
    def __init__(self, v):
        self.V = v
        self.adjList = []*self.V

    def adjL(self):
        for i in range(self.adjList.__len__()):
            adjList.append([])

    def addEdge(self, u, v, isBidirectional = True):
        self.adjList[u].append(v)
        if isBidirectional:
            self.adjList[v].append(u)

    def printGraph(self):
        for i in range(self.V):
            print(i, "->", end = " ")
            for j in range(1, self.adjList[i].__len__()):
                    print(self.adjList[i][j], end = ", ")
            print()




g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(0, 2)
g.addEdge(2, 4)
g.addEdge(3, 4)


g.printGraph()










