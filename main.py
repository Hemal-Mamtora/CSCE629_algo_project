from src.dijkstras import DijkstrasAlgorithm
from src.graph import Graph
from time import perf_counter

def main():
    G = Graph(5000, type="g1", average_degree=6)
    # G = Graph(5000, type="g2", percent=20)
    # print("here")
    # return
    s = perf_counter()
    DijkstrasAlgorithm(G, 10, 200, heap=True).run()
    e = perf_counter()
    print("time: ", (e-s))
    # Status: infinite loop, need to debug

if __name__ == "__main__":
    main()