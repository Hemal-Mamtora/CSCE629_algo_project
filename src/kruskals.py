from enum import IntEnum
from .graph import Edge, Graph, Node

class Color(IntEnum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class KruskalsAlgorithm:
    # get all the edges of a graph
    # sort them
    # check if they do not make a cycle
    # 
    def __init__(self, G: Graph, s: int, t: int) -> None:
        self.G = G
        self.s = s
        self.t = t
        # TODO: move makeset here?
        self.p = [None for i in range(self.G.n)]
        self.h = [None for i in range(self.G.n)]


    def run(self):
        edges = self.G.get_edges()
        # edges = self.heapsort(edges)
        # TODO: replace it with heapsort
        edges = sorted(edges, key= lambda x: x[0], reverse=True)

        # TODO: can i put this inside the initialization?
        for i in range(self.G.n):
            self.makeset(i)

        edge_count = 0
        i = 0

        self.result = []
        while(edge_count < self.G.n - 1):
            edge = edges[i]
            i = i+1
            weight, u, v = edge
            r1 = self.find(u)
            r2 = self.find(v)
            if r1 != r2:
                self.result.append(edge)
                edge_count += 1
                self.union(r1, r2)

        return self.output()

    def output(self):
        # print(self.result)
        self.create_mst()
        self.dfs()

        if self.reached == True:
            x = self.t
            # while(x != self.s):
            #     print(x)
            #     x = self.dad[x]
            # print(x)
        else:
            print("no s-t path found")

    def dfs(self):
        self.reached = False
        self.color = [Color.WHITE for i in range(self.G.n)]
        self.dad = [-1 for i in range(self.G.n)]
        self.dfs_recursive(self.s)

    def dfs_recursive(self, v):
        self.color[v] = Color.GRAY
        for edge in self.T[v]:
            w, weight = edge

            if self.color[w] == Color.WHITE:
                self.dad[w] = v
                if w == self.t:
                    self.reached = True
                    return
                self.dfs_recursive(w)
        self.color[v] = Color.BLACK


    def create_mst(self):
        T = [[] for i in range(self.G.n)]

        for edge in self.result:
            w, a, b = edge
            T[a].append((b, w))
            T[b].append((a, w))

        self.T = T

    def heapsort(self, edges):
        pass

    def makeset(self, v):
        self.p[v] = -1
        self.h[v] = 0

    def find(self, v):
        w = v
        while(self.p[w] != -1):
            w = self.p[w]
        return w

    def union(self, r1, r2):
        if self.h[r1] > self.h[r2]:
            self.p[r2] = r1
        elif self.h[r2] > self.h[r1]:
            self.p[r1] = r2
        else: # h[r2] == h[r1]
            self.p[r2] = r1
            self.h[r1] = self.h[r1] + 1





