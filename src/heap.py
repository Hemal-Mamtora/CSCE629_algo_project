class Heap():
    def __init__(self, n) -> None:
        self.H = [-1 for i in range(n)]
        self.D = [-1 for i in range(n)]
        self.P = [-1 for i in range(n)]
        self.max_size = n
        self.last_index = -1

    def left(self, i: int) -> int:
        return i * 2 + 1
    
    def has_left(self, i: int) -> bool:
        return self.left(i) <= self.last_index

    def right(self, i: int) -> int:
        return i * 2 + 2

    def has_right(self, i: int) -> bool:
        return self.right(i) <= self.last_index

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def is_leaf(self, i: int) -> bool:
        return i <= (self.last_index+1) and i >= (self.last_index+1)//2

    # def get_max(self):
    #     pass
    
    def insert(self, node, capacity):
        self.last_index  += 1
        self.H[self.last_index] = node
        self.D[node] = capacity # TODO: check can it be taken outside of the heap code ?
        self.P[node] = self.last_index
        self.heapify_up()

    def swap(self, a, b):
        self.H[a], self.H[b] = self.H[b], self.H[a]
        self.P[self.H[a]] = a
        self.P[self.H[b]] = b

    def heapify_up(self):
        index = self.last_index
        while self.parent(index) >= 0 and self.D[self.H[index]] > self.D[self.H[self.parent(index)]]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        if not self.is_leaf(index):

            l = self.left(index)
            r = self.right(index)
            # print(index, l, self.last_index)
            max_ = self.D[self.H[l]]
            swap_candidate = "left"

            if self.has_right(index) and max_ < self.D[self.H[r]]:
                swap_candidate = "right"
                max_ = self.D[self.H[r]]
            
            if self.D[self.H[index]] < max_:
                if swap_candidate == "left":
                    self.swap(index, self.left(index))
                    self.heapify_down(self.left(index))
                else:
                    self.swap(index, self.right(index))
                    self.heapify_down(self.right(index))

    # def remove(self):
    #     """
    #     So the remove function does not work
    #     """
    #     if self.last_index < 0:
    #         print("empty heap")
    #         return -1, -1
    #     out, out_val = self.H[0], self.D[self.H[0]]
    #     self.H[0] = self.H[self.last_index]
    #     self.last_index -= 1
    #     self.heapify_down(0)
    #     return out, out_val

    def delete(self, node):
        index = self.P[node]

        if index == -1:
            print(node, "is not present in the heap")
            return -1, -1

        # update the node position, since now the node will be lost
        self.P[node] = -1

        out, out_val = self.H[index], self.D[self.H[index]]
        self.H[index] = self.H[self.last_index]
        self.P[self.H[index]] = index
        self.last_index -= 1
        self.heapify_down(index)
        return out, out_val

    def maximum(self):
        if self.last_index < 0:
            print("empty heap")
            return -1, -1
        return self.H[0], self.D[self.H[0]]


class EdgeHeap():
    pass

class Test:
    def run():
        h = Heap(5000)
        pairs = [
            (200, 200),
            (40, 40),
            (100, 100),
            (12, 12),
            (99, 99),
            (55, 55),
            (2000, 2000),
            (232, 232),
            (234, 234),
            (0, 0),
            (3000, 3000),
            (80, 80),
            (444, 444),
            (33, 33)
        ]

        for i in pairs:
            h.insert(i[0], i[1])

        # h.delete(12321)
        h.delete(800)
        h.delete(33)
        h.delete(80)

        for j, i in enumerate(pairs):
            # if j == len(pairs) - 1 - 2:
            #     break
            # a, b = h.maximum()
            a, b = h.delete(a)
            # a, b = h.remove()
            # h.insert(a, b)
            print(b, a)

if __name__ == "__main__":
    # h = Heap(5000)
    # h.insert(1, 2)
    # h.insert(10, 200)
    # a, b = h.remove()
    # print(a, b)
    Test.run()