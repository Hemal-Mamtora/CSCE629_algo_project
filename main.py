from src.dijkstras import DijkstrasAlgorithm
from src.graph import Graph
import time
import random
from src.kruskals import KruskalsAlgorithm

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

def test_main():
    
    a = time.perf_counter()
    G = Graph(5000, type="g1", average_degree=6)
    b = time.perf_counter()
    print("Sparse Graph")
    print("Creation Time: ", (b - a))
    dij_n2, dij_heap, k = test(G, times = 10)
    
    # print("Sparse Graph")
    # print("Creation Time: ", (b - a))
    print("d_without_heap", dij_n2)
    print("d_heap", dij_heap)
    print("k", k)
    
    a = time.perf_counter()
    G = Graph(5000, type="g2", percent=20)
    b = time.perf_counter()
    print("Dense Graph")
    print("Creation Time: ", (b - a))

    dij_n2, dij_heap, k = test(G, times = 10)

    print("d_without_heap", dij_n2)
    print("d_heap", dij_heap)
    print("k", k)

def test(G, times = 100):
    dij_n2 = 0
    dij_heap = 0
    k = 0
    for i in range(times):
        print(i)
        s = random.randint(0, 4999)
        t = random.randint(0, 4999)
        a = time.perf_counter()
        DijkstrasAlgorithm(G, s, t, heap=False).run()
        b = time.perf_counter()
        DijkstrasAlgorithm(G, s, t, heap=True).run()
        c = time.perf_counter()
        KruskalsAlgorithm(G, s, t).run()
        d = time.perf_counter()

        dij_n2 += b-a
        dij_heap += c-b
        k += d - c
    
    return dij_n2, dij_heap, k


if __name__ == "__main__":
    # main()
    test_main()