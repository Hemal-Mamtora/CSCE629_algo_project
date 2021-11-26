class heap():
    def __init__(self, n) -> None:
        self.H = [-1 for i in range(n)]
        self.D = [-1 for i in range(n)]
        self.P = [-1 for i in range(n)]
        self.max_size = n
        self.last_index = -1

    def left(i: int) -> int:
        return i * 2 + 1
    
    def right(i: int) -> int:
        return i * 2 + 2

    def parent(i: int) -> int:
        return (i - 1) // 2

    def get_max(self):
        pass
    
    def insert(self, ):
        self.last_index  += 1


    def delete(self):
        pass

    def insert(self):
        pass

    # def heapify(self):
    #     pass

# will complete it after implementing dijkstra's algorithm, so that i have an idea of the usage, since it
# is not a simple heap, but it is a modified heap.