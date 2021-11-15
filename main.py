from code.dijkstras import DijkstrasAlgorithm
from code.graph import Graph

def main():
    G = Graph(5000, type="g1", average_degree=6)
    DijkstrasAlgorithm(G, 1, 2).run()
    # Status: infinite loop, need to debug

if __name__ == "__main__":
    main()