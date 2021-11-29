from typing import Dict, List

from src.heap import Heap
from .graph import Edge, Graph, Node
from enum import IntEnum

class Status(IntEnum):
    UNSEEN = 0
    FRINGE = 1
    INTREE = 2

class DijkstrasAlgorithm:
    def __init__(self, G: Graph, s: int, t: int, heap: bool) -> None:
        self.G: Graph = G
        self.s: int = s
        self.t: int = t
        self.dad: Dict = {}
        self.heap = heap
        self.bw = [-1 for i in range(G.n)]

    def heap_solution(self):

        self.status: List[Status] = [Status.UNSEEN for i in range(self.G.n)]
        self.status[self.s] = Status.INTREE

        fringes = Heap(self.G.n) # 5k

        w: Edge = self.G.adjacency_list[self.s].get_next()

        while(w): # for each edge (s, w)
            self.status[w.node] = Status.FRINGE
            self.dad[w.node] = self.s
            self.bw[w.node] = w.weight # weight means capacity: cap(s, w)
            fringes.insert(w.node, self.bw[w.node])

            w = w.get_next()
        
        while(fringes.last_index >= 0):
            # print("before len(fringes): ", len(fringes))
            v, capacity = fringes.maximum() # this should be faster
            fringes.delete(v)
            # print("after len(fringes): ", len(fringes))
            self.status[v] = Status.INTREE

            # print(v)
            w: Edge = self.G.adjacency_list[v].get_next() # repeat, TODO: extract a method
            while(w): # for each edge (v, w)
                if v == 2 and w.node == 6:
                    print("Got Here")
                if v == 2 and w.node == 7:
                    print("now here")
                if w == 3:
                    print("please")
                if self.status[w.node] == Status.UNSEEN:
                    self.status[w.node] = Status.FRINGE
                    self.bw[w.node] = min(self.bw[v], w.weight)
                    self.dad[w.node] = v
                    fringes.insert(w.node, self.bw[w.node])
                elif (self.status[w.node] == Status.FRINGE and 
                        self.bw[w.node] < min(self.bw[v], w.weight)): # w.weight means cap(v, w)
                    fringes.delete(w.node)
                    self.dad[w.node] = v
                    self.bw[w.node] = min(self.bw[v], w.weight)
                    fringes.insert(w.node, self.bw[w.node])

                w = w.get_next()
        
        if self.status[self.t] != Status.INTREE:
            print("no s-t path")
            return -1, []
        else:
            # print("bandwidth: ", self.bw[self.t])
            # x = self.t
            # while(x != self.s):
            #     print(x)
            #     x = self.dad[x]
            # print(x)
            return self.output()


    def run(self):

        if self.heap:
            return self.heap_solution()

        self.status: List[Status] = [Status.UNSEEN for i in range(self.G.n)]
        self.status[self.s] = Status.INTREE
        
        w: Edge = self.G.adjacency_list[self.s].get_next()

        fringes = []

        while(w): # for each edge (s, w)
            self.status[w.node] = Status.FRINGE
            fringes.append(w.node) # only val
            self.dad[w.node] = self.s
            self.bw[w.node] = w.weight # weight means capacity: cap(s, w)

            w = w.get_next()
        
        while(fringes):
            # print("before len(fringes): ", len(fringes))
            v = self.v_with_largest_bandwidth(fringes)
            # print("after len(fringes): ", len(fringes))
            self.status[v] = Status.INTREE

            # print(v)

            w: Edge = self.G.adjacency_list[v].get_next() # repeat, TODO: extract a method
            while(w): # for each edge (v, w)
                if self.status[w.node] == Status.UNSEEN:
                    self.status[w.node] = Status.FRINGE
                    fringes.append(w.node)
                    self.bw[w.node] = min(self.bw[v], w.weight)
                    self.dad[w.node] = v
                elif (self.status[w.node] == Status.FRINGE and 
                        self.bw[w.node] < min(self.bw[v], w.weight)): # w.weight means cap(v, w)
                    self.dad[w.node] = v
                    self.bw[w.node] = min(self.bw[v], w.weight)

                w = w.get_next()
        
        if self.status[self.t] != Status.INTREE:
            print("no s-t path")
            return -1, []
        else:
            # print("bandwidth: ", self.bw[self.t])
            # x = self.t
            # while(x != self.s):
            #     print(x)
            #     x = self.dad[x]
            # print(x)

            return self.output()

    def output(self):
        path = []
        bw = self.bw[self.t]
        x = self.t
        while(x != self.s):
            # print(x)
            path.append(x)
            x = self.dad[x]
        # print(x)
        path.append(x)
        return bw, path

    def v_with_largest_bandwidth(self, fringes):
        max_bw = float("-inf")
        v_max = -1
        pos_v_max = -1
        for i, f in enumerate(fringes):
            if self.bw[f] > max_bw:
                max_bw = self.bw[f]
                v_max = f
                pos_v_max = i
        
        fringes.pop(pos_v_max)

        return v_max