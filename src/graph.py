import random
import time
from typing import Tuple

class Edge:
    def __init__(self, node = -1, weight = -1, next_ = None):
        self.node = node # the next node this edge is pointing to
        self.weight = weight
        self.next = next_

    def set_next(self, edge):
        self.next = edge

    def get_next(self):
        return self.next


class Node(Edge):
    def __init__(self, val = -1):
        super().__init__(val)

    def insert(self, edge: Edge):
        temp = self.get_next()
        self.set_next(edge)
        edge.set_next(temp)
    
    def degree(self):
        deg = 0
        e = self
        while(e.next):
            deg += 1
            e = e.next
        
        return deg


class AdjacencyList:
    def __init__(self, node: Node) -> None:
        self.node = node
        

    def insert(self, edge: Edge) -> Edge:
        pass


class Graph:
    def __init__(self, vertex_count = 100, type = 'g1', **params):
        self.n = vertex_count
        self.adjacency_list = []
        self.type = type
        self.pairs = [[False for _ in range(self.n)] for _ in range(self.n)]

        # creating the adjacency list
        self.create_adjacency_list()

        # creating the cycle for connectivity
        self.create_cycle()

        if type == "g1":
            self.create_graph_g1(current_avg_degree=2, required_avg_degree=params["average_degree"])
        elif type == "g2":
            self.create_graph_g2(percent=params["percent"])
        else:
            print("please provide graph type from g1 or g2")
            raise Exception
        
        # self.print_graph()


    def create_graph_g2(self, percent):
        degree = [2 for i in range(self.n)]

        required_degree = int(percent*0.01*self.n)
        threshold = int(0.9 * required_degree)
        for node1 in range(self.n):
            # print(node, end=" ")
            # print(degree[node], end=" ")
            while(degree[node1] < threshold):
                node2 = random.randint(0, self.n - 1)
                if node1 == node2:
                    continue

                # n1, n2 = (node, node2) if node < node2 else (node2, node)

                if not self.pairs[node1][node2]:
                    self.insert_edge(node1, node2)
                    degree[node1] += 1
                    degree[node2] += 1
            # print(degree[node])


    def create_graph_g1(self, current_avg_degree, required_avg_degree):
        # since in a cycle, each vertex is connected to every other vertex
        temp_avg_deg = current_avg_degree

        while(required_avg_degree - temp_avg_deg > 0.0001):
            node1 = random.randint(0, self.n - 1)
            node2 = random.randint(0, self.n - 1)

            if node1 == node2:
                continue

            if self.pairs[node1][node2]:
                continue
            self.insert_edge(node1, node2)

            temp_avg_deg += 2 / self.n


    def create_adjacency_list(self):
        for i in range(self.n):
            self.adjacency_list.append(Node(i))


    def insert_edge(self, node1: Node, node2: Node) -> Tuple[int, int]:
        # I feel that a random positive number bounded by `bound` is sufficient for the demo
        bound = 500
        w = random.randint(1, bound)

        e1 = Edge(node = node1, weight = w)
        self.adjacency_list[node2].insert(e1)

        e2 = Edge(node = node2, weight = w)
        self.adjacency_list[node1].insert(e2)

        self.pairs[node1][node2] = True
        self.pairs[node2][node1] = True


    def create_cycle(self):
        for i in range(self.n):
            n = (i + 1) % self.n
            self.insert_edge(i, n)


    def calculate_total_deg(self):
        sum_ = 0
        for i in range(self.n):
            sum_ += self.adjacency_list[i].degree()

        return sum_


    def get_edges(self):
        # TODO: get rid of set, will a simple, list() work?
        edges = []
        for linked_list in (self.adjacency_list):
            v = linked_list
            edge = v.next
            while(edge):
                if v.node < edge.node: # to only consider the edge once
                    edges.append((edge.weight, v.node, edge.node))
                edge = edge.next
        return edges


    def print_graph(self):
        edges = self.get_edges()
        print(edges)


class Test:

    def run(type = 'g1'):
        deg = 6 # default
        if type == 'g1':
            params = {"average_degree": 6}
        elif type == 'g2':
            params = {"percent": 20} # 20% of 5000

        # sanity check test
        # currently it runs in time 0.25 seconds, and looks correct.
        # TODO: discuss with prof and try to optimize
        
        start = time.perf_counter()
        g = Graph(5000, type=type, **params)
        end = time.perf_counter()

        print("time: ", (end - start))
        # print(g.avg_deg)
        print("avg_deg: ", g.calculate_total_deg() / g.n)


# if __name__ == "__main__":
#     pass
#     # Test.run("g2")
#     # Test.run("g1")
#     # # time:  93.429851
#     # # 1000
#     # # avg_deg:  1000.0

#     # start = time.perf_counter()
#     # # g = Graph(5000, type="g1", average_degree=6)
#     # g = Graph(5000, type="g2", percent=20)
#     # end = time.perf_counter()

#     # print("time: ", (end - start))
#     # # print(g.avg_deg)
#     # print("avg_deg: ", g.calculate_total_deg() / g.n)


# # NOTE: g2 implementation is incorrect. i.e. it is pending. redo
# # (algo_proj) PS D:\Fall 2021\CSCE 629 Algo\project> python .\code\graph.py
# # time:  124.4710679
# # avg_deg:  1114.914
# # (algo_proj) PS D:\Fall 2021\CSCE 629 Algo\project> 