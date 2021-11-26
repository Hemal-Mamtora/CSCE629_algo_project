from typing import Dict, List
from .graph import Edge, Graph, Node
from enum import IntEnum

class Status(IntEnum):
    UNSEEN = 0
    FRINGE = 1
    INTREE = 2

class DijkstrasAlgorithm:
    def __init__(self, G: Graph, s: int, t: int) -> None:
        self.G: Graph = G
        self.s: int = s
        self.t: int = t
        self.dad: Dict = {}
        self.bw = [-1 for i in range(G.n)]

    def run(self):
        self.status: List[Status] = [Status.UNSEEN for i in range(self.G.n)]
        self.status[self.s] = Status.INTREE
        
        w: Edge = self.G.adjacency_list[self.s].get_next()

        fringes = [w.node]

        while(w): # for each edge (s, w)
            self.status[w.node] = Status.FRINGE
            fringes.append(w.node) # only val
            self.dad[w.node] = self.s
            self.bw[w.node] = w.weight # weight means capacity: cap(s, w)

            w = w.get_next()
        
        while(fringes):
            v = self.v_with_largest_bandwidth(fringes)
            self.status[v] = Status.INTREE

            print(v)

            if v == self.t:
                print("Here")
                break

            w: Edge = self.G.adjacency_list[v].get_next() # repeat, TODO: extract a method
            while(w): # for each edge (v, w)
                if self.status[w.node] == Status.UNSEEN:
                    self.status[w.node] = Status.FRINGE
                    fringes.append(w.node)
                    self.bw[w.node] = min(self.bw[v], w.weight)
                    self.dad[w] = v
                elif (self.status[w.node] == Status.FRINGE and 
                        self.bw[w.node] < min(self.bw[v], w.weight)): # w.weight means cap(v, w)
                    self.dad[w] = v
                    self.bw[w.node] = min(self.bw[v], w.weight)


                self.status[w.node] = Status.FRINGE
                fringes.append(w.node) # only val
                self.dad[w.node] = v
                self.bw[w.node] = w.weight # weight means capacity

                w = w.get_next()
        
        if self.status[self.t] != Status.INTREE:
            print("no s-t path")

        else:
            x = self.t
            while(x != self.s):
                print(x)
                x = self.dad[x]

        return


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