import random
import time
from typing import Tuple

class Edge:
    def __init__(self, node = -1, weight = -1, next_ = None):
        self.node = node
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

class Graph:
    def __init__(self, vertex_count = 100, type = 'g1', **params):
        self.n = vertex_count
        self.adjacency_list = []
        self.type = type
        # TODO: ask regarding below method to eliminate duplicates
        # TODO: find better way than set, use some more rudimentary data structure, or is it fine?
        self.pairs = set() 

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

    def create_graph_g2(self, percent):
        degree = [2 for i in range(self.n)]

        required_degree = percent*0.01*self.n
        threshold = 0.9 * required_degree
        for node in range(self.n):

            while(degree[node] < threshold):
                node2 = random.randint(0, self.n - 1)
                if node == node2:
                    continue
                pair = (node, node2) if node < node2 else (node2, node)
                if pair not in self.pairs:
                    self.insert_edge(node, node2)
                    degree[node2] += 1
                    degree[node] += 1
                    self.pairs.add(pair)

    def create_graph_g1(self, current_avg_degree, required_avg_degree):
        temp_avg_deg = current_avg_degree # since in a cycle, each vertex is connected to every other vertex

        while(abs(temp_avg_deg - required_avg_degree) > 0.0001):
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)

            if x == y:
                continue

            pair = (x, y) if x < y else (y, x)

            if pair in self.pairs:
                continue
            self.insert_edge(x, y)
            self.pairs.add(pair)

            temp_avg_deg += 2 / self.n


    def create_adjacency_list(self):
        for i in range(self.n):
            self.adjacency_list.append(Node(i))

    def insert_edge(self, n1: Node, n2: Node) -> Tuple[int, int]:
        w = random.randint(1, 10)    # NOTE: weight is currently bounded by 10 # TODO: change this

        e1 = Edge(node = n1, weight = w)
        self.adjacency_list[n2].insert(e1)

        e2 = Edge(node = n2, weight = w)
        self.adjacency_list[n1].insert(e2)

        pair = (n1, n2) if n1 < n2 else (n2, n1)
        return pair

    def create_cycle(self):
        for i in range(self.n):
            n = (i + 1) % self.n
            self.insert_edge(i, n)
            pair = (i, n) if i < n else (n, i)
            self.pairs.add(pair)

    def calculate_total_deg(self):
        sum_ = 0
        for i in range(self.n):
            sum_ += self.adjacency_list[i].degree()

        return sum_

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


if __name__ == "__main__":
    # Test.run("g2")
    # Test.run("g1")
    # # time:  93.429851
    # # 1000
    # # avg_deg:  1000.0

    # start = time.perf_counter()
    # # g = Graph(5000, type="g1", average_degree=6)
    # g = Graph(5000, type="g2", percent=20)
    # end = time.perf_counter()

    # print("time: ", (end - start))
    # # print(g.avg_deg)
    # print("avg_deg: ", g.calculate_total_deg() / g.n)


# NOTE: g2 implementation is incorrect. i.e. it is pending. redo
# (algo_proj) PS D:\Fall 2021\CSCE 629 Algo\project> python .\code\graph.py
# time:  124.4710679
# avg_deg:  1114.914
# (algo_proj) PS D:\Fall 2021\CSCE 629 Algo\project> 