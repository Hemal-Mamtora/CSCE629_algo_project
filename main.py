import time
import random
import sys

# # pandas only for analysis
# # NOTE: I am using pandas for nice display and fast analysis
# # pandas is not used in the algorithm
# # as instructed by professor, only list and pointers are used 
# # to implement the algorithms and data structures
# import pandas as pd
# pd.options.display.max_columns = None
# pd.options.display.max_rows = None

from src.graph import Graph
from src.dijkstras import DijkstrasAlgorithm
from src.kruskals import KruskalsAlgorithm

sys.setrecursionlimit(10000)

dij_n2_str = "dijkstras without heap:"
dij_heap_str = "dijkstras with heap:"
k_str = "kruskals:"

def main():
    # df = pd.DataFrame(columns=[
    #     "itr_num",
    #     "graph_type",
    #     "create_time", 
    #     "s",
    #     "t",
    #     "algorithm",
    #     "time",
    #     "max_bw",
    #     "max_bw_path"
    # ])
    times = 5

    for i in range(times):
        print("-"*80)
        print("\t\t", "-"*10, "Graph number: ", (i+1), "-"*10,)
        print("-"*80)
        n = 5000
        average_degree = 6
        percent = 20

        a = time.perf_counter()
        G = Graph(n, type="g1", average_degree=average_degree)
        b = time.perf_counter()

        sparse_creation_time = b - a
        print("-"*80)
        print("Sparse Graph")
        print("-"*80)
        print("Creation Time: ", sparse_creation_time)

        sparse_out = test(G, n, i ,True, times, df, sparse_creation_time)
        df = sparse_out[-1]

        a = time.perf_counter()
        G = Graph(n, type="g2", percent=percent)
        b = time.perf_counter()
        dense_creation_time = b - a

        print("-"*80)
        print("Dense Graph")
        print("-"*80)
        print("Creation Time: ", dense_creation_time)

        dense_out = test(G, n, i, False, times, df, dense_creation_time)
        df = dense_out[-1]

    df_temp = df.loc[:, df.columns != 'max_bw_path']

    print(df.loc[:, df.columns != 'max_bw_path'])

    analysis = analyse(df_temp)

    


def analyse(df_temp):
    x = df_temp.groupby(["graph_type", "algorithm"]).mean()
    print(x)

def test(G, n, current_itr, sparse, times, df, creation_time):
    dij_n2 = []
    dij_heap = []
    k = []

    dij_n2 = []
    dij_heap = []
    k = []

    for i in range(times):
        # print("s-t pair number: ", i)
        s = t = -1
        while(s==t):
            # so that s and t are not same
            s = random.randint(0, n-1)
            t = random.randint(0, n-1)
        print("-"*80)
        # print("iteration number: ", i, ", s: ", s, ", t: ", t)
        print(f"(iteration number: {i+1}), (s: {s}), (t: {t})")
        print("-"*80)

        a = time.perf_counter()
        dij_n2_bw, dij_n2_path = DijkstrasAlgorithm(G, s, t, heap=False).run()
        b = time.perf_counter()
        dij_heap_bw, dij_heap_path = DijkstrasAlgorithm(G, s, t, heap=True).run()
        c = time.perf_counter()
        k_bw, k_path = KruskalsAlgorithm(G, s, t).run()
        d = time.perf_counter()
        
        dij_n2_time = b - a
        dij_heap_time = c - b
        k_time = d - c

        dij_n2.append((dij_n2_time, dij_n2_bw, dij_n2_path))
        dij_heap.append((dij_heap_time, dij_heap_bw, dij_heap_path))
        k.append((k_time, k_bw, k_path))

        print("-"*40)
        print("Run Times: ")
        print("-"*40)
        print(dij_n2_str, dij_n2_time)
        print(dij_heap_str, dij_heap_time)
        print(k_str, k_time)

        print("-"*40)
        print("Bandwidths: ")
        print("-"*40)
        print(dij_n2_str, dij_n2_bw)
        print(dij_heap_str, dij_heap_bw)
        print(k_str, k_bw)

        print("-"*40)
        print("Paths: ")
        print("-"*40)
        print(dij_n2_str, dij_n2_path)
        print(dij_heap_str, dij_heap_path)
        print(k_str, k_path)

        # df = df.append({
        #     "itr_num": current_itr + 1,
        #     "graph_type": "sparse" if sparse else "dense",
        #     "create_time": creation_time,
        #     "s": s,
        #     "t": t,
        #     "algorithm": "dij_without_heap",
        #     "time": dij_n2_time,
        #     "max_bw": dij_n2_bw,
        #     "max_bw_path": dij_n2_path
        # },ignore_index = True)

        # df = df.append({
        #     "itr_num": current_itr + 1,
        #     "graph_type": "sparse" if sparse else "dense",
        #     "create_time": creation_time,
        #     "s": s,
        #     "t": t,
        #     "algorithm": "dij_with_heap",
        #     "time": dij_heap_time,
        #     "max_bw": dij_heap_bw,
        #     "max_bw_path": dij_heap_path
        # }, ignore_index = True)

        # df = df.append({
        #     "itr_num": current_itr + 1,
        #     "graph_type": "sparse" if sparse else "dense",
        #     "create_time": creation_time,
        #     "s": s,
        #     "t": t,
        #     "algorithm": "kruskals",
        #     "time": k_time,
        #     "max_bw": k_bw,
        #     "max_bw_path": k_path
        # }, ignore_index = True)

    return dij_n2, dij_heap, k, df

if __name__ == "__main__":
    main()