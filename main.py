from src.dijkstras import DijkstrasAlgorithm
from src.graph import Graph
import time
import random
from src.kruskals import KruskalsAlgorithm

import sys
sys.setrecursionlimit(10000)

def main():
    G = Graph(5000, type="g1", average_degree=6)
    # G = Graph(5000, type="g2", percent=20)
    # print("here")
    # return
    s = time.perf_counter()
    # DijkstrasAlgorithm(G, 10, 200, heap=True).run()
    KruskalsAlgorithm(G, 1212, 200).run()
    e = time.perf_counter()
    t = (e-s)
    # print("time: ", (e-s)*1000, "ms")

    s = time.perf_counter()
    DijkstrasAlgorithm(G, 1212, 200, heap=True).run()
    # KruskalsAlgorithm(G, 7, 8).run()
    e = time.perf_counter()
    t = (e-s)
    # print("time: ", (e-s)*1000, "ms")

    # Status: infinite loop, need to debug

# def test_main():
#     for i in range(1000):
#         # i = 109
#         print("I:", i)
#         random.seed(i)
#         n = 100
#         average_degree = 4
#         percent = 20

#         a = time.perf_counter()
#         G = Graph(n, type="g1", average_degree=average_degree)
#         b = time.perf_counter()
#         print("Sparse Graph")
#         print("Creation Time: ", (b - a))
#         dij_n2, dij_heap, k = test(G, n, times = 1)
        
#         # print("Sparse Graph")
#         # print("Creation Time: ", (b - a))
#         print("d_without_heap", dij_n2)
#         print("d_heap", dij_heap)
#         print("k", k)
        
#         a = time.perf_counter()
#         G = Graph(n, type="g2", percent=percent)
#         b = time.perf_counter()
#         print("Dense Graph")
#         print("Creation Time: ", (b - a))

#         dij_n2, dij_heap, k = test(G, n, times = 1)

#         print("d_without_heap", dij_n2)
#         print("d_heap", dij_heap)
#         print("k", k)
#         # input()

# def test(G, n, times = 100):
#     dij_n2 = 0
#     dij_heap = 0
#     k = 0
#     for i in range(times):
#         print(i)
#         s = t = 0
#         while(s==t):
#             s = random.randint(0, n-1)
#             t = random.randint(0, n-1)
#         print("s: ", s, "t: ", t)
#         a = time.perf_counter()
#         bwa, path = DijkstrasAlgorithm(G, s, t, heap=False).run()
#         print(bwa)
#         b = time.perf_counter()
#         bwb, path = DijkstrasAlgorithm(G, s, t, heap=True).run()
#         print(bwb)
#         c = time.perf_counter()
#         bwc, path = KruskalsAlgorithm(G, s, t).run()
#         print(bwc)
#         d = time.perf_counter()

#         dij_n2 += b-a
#         dij_heap += c-b
#         k += d - c

#         if bwa != bwb or bwb!=bwc or bwc!=bwa:
#             print("here")
#             raise Exception
    
#     return dij_n2, dij_heap, k


def test_main():
    for i in range(0, 500):
        random.seed(i)
        print("I:", 25)
        # for i in range(5):
        n = 100
        average_degree = 4
        percent = 20

        a = time.perf_counter()
        G = Graph(n, type="g1", average_degree=average_degree)
        b = time.perf_counter()
        print("Sparse Graph")
        print("Creation Time: ", (b - a))
        dij_n2, dij_heap, k = test(G, n, times = 5)
        
        # if dij_n2 == []:
        #     continue
        # print("Sparse Graph")
        # print("Creation Time: ", (b - a))
        print("d_without_heap", dij_n2)
        print("d_heap", dij_heap)
        print("k", k)
        
        a = time.perf_counter()
        G = Graph(n, type="g2", percent=percent)
        b = time.perf_counter()
        print("Dense Graph")
        print("Creation Time: ", (b - a))

        dij_n2, dij_heap, k = test(G, n, times = 5)
        # if dij_n2 == []:
        #     continue
        print("d_without_heap", dij_n2)
        print("d_heap", dij_heap)
        print("k", k)
            # input()

def test(G, n, times = 5):
    dij_n2 = []
    dij_heap = []
    k = []
    for i in range(times):
        print(i)
        s = t = 0
        while(s==t):
            s = random.randint(0, n-1)
            t = random.randint(0, n-1)
        print("s: ", s, "t: ", t)
        a = time.perf_counter()
        bwa, path = DijkstrasAlgorithm(G, s, t, heap=False).run()
        print(bwa)
        print(path)
        b = time.perf_counter()
        bwb, path = DijkstrasAlgorithm(G, s, t, heap=True).run()
        print(bwb)
        print(path)
        c = time.perf_counter()
        bwc, path = KruskalsAlgorithm(G, s, t).run()
        print(bwc)
        print(path)
        d = time.perf_counter()

        dij_n2.append(b-a)
        dij_heap.append(c-b)
        k.append(d - c)

        if bwa != bwb or bwb!=bwc or bwc!=bwa:
            raise Exception

    return dij_n2, dij_heap, k

if __name__ == "__main__":
    # main()
    test_main()