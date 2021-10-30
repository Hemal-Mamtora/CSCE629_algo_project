import random
import time

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
    def __init__(self, vertex_count = 100, average_degree = 3):
        self.n = vertex_count
        self.avg_deg = average_degree

        # TODO: ask regarding below method to eliminate duplicates
        temp = set() # TODO: find better way than set, use some more rudimentary data structure, or is it fine?

        # creating the adjacency list
        self.adjacency_list = []
        for i in range(vertex_count):
            self.adjacency_list.append(Node(i))

        # creating the cycle for connectivity
        for i in range(vertex_count):
            
            ############################
            # TODO: extract a method to add edge to a graph, replace with a function/method
            w = random.randint(1, 10)    # NOTE: weight is currently bounded by 10 # TODO: change this
            n = (i + 1) % self.n

            e1 = Edge(node = n, weight = w)
            self.adjacency_list[i].insert(e1)

            e2 = Edge(node = i, weight = w)
            self.adjacency_list[n].insert(e2)

            x = (i, n) if i < n else (n, i)
            temp.add(x)
            ############################

        temp_avg_deg = 2 # since in a cycle, each vertex is connected to every other vertex

        while(abs(temp_avg_deg - self.avg_deg) > 0.0001): # TODO: change threshold to 0.01
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)

            if x == y:
                continue

            pair = (x, y) if x < y else (y, x)

            if pair in temp:
                continue
            
            ############################
            # TODO: extract a method to add edge to a graph, replace with a function/method
            w = random.randint(1, 10)    # NOTE: weight is currently bounded by 10 # TODO: change this
            
            e1 = Edge(node = x, weight = w)
            self.adjacency_list[y].insert(e1)

            e2 = Edge(node = y, weight = w)
            self.adjacency_list[x].insert(e2)

            x = (i, n) if i < n else (n, i)
            temp.add(x)
            ############################

            # print(temp_avg_deg)
            temp_avg_deg += 2 / self.n

    def calculate_total_deg(self):
        sum_ = 0
        for i in range(self.n):
            sum_ += self.adjacency_list[i].degree()

        return sum_


if __name__ == "__main__":
    
    # sanity check test
    # currently it runs in time 0.25 seconds, and looks correct.
    # TODO: discuss with prof and try to optimize
    start = time.perf_counter()
    g = Graph(5000, 6)
    end = time.perf_counter()

    print("time: ", (end - start))
    print(g.avg_deg)
    print("avg_deg: ", g.calculate_total_deg() / g.n)
    
