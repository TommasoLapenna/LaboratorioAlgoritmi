"""
import sys
import time
import random
import tracemalloc
from linked_list import LinkedList
from binary_tree import OrderStatisticTree
from avl_tree import AugmentedAVLTree

SAMPLE_SIZE = 10000

N_QUERIES = 100

sys.setrecursionlimit(100000)


def runExperiment(sampleSize,nQueries):

    ll = LinkedList()
    ost = OrderStatisticTree()
    avl = AugmentedAVLTree()

    print(f"EXPERIMENT WITH SAMPLE SIZE = {sampleSize}")
    print("--------------------")
    data = random.sample(range(1, sampleSize * 100), sampleSize)
    for number in data:
        ll.orderedInsert(number)
        ost.treeInsert(number)
        avl.treeInsert(number)

    selectQueries = []
    for i in range(nQueries):
        selectQueries.append(random.randint(0, int(sampleSize * (4 / 3))))

    dataSet = set(data)
    rankQueries = []
    for i in range(nQueries):
        if random.random() < 0.75:
            rankQueries.append(random.choice(data))
        else:
            k = random.randint(1, sampleSize * 100)
            while k in dataSet:
                k = random.randint(1, sampleSize * 100)
            rankQueries.append(k)

    structures = [("LINKED LIST", ll), ("BINARY TREE", ost), ("AVL TREE", avl)]

    for name, structure in structures:
        operations = [("OS-SELECT", structure.osselect, selectQueries),
                      ("OS-RANK", structure.osrank, rankQueries)]

        for opName, operation, queries in operations:
            print(f"\n\n{name} {opName} TEST RESULTS")

            timeResults = []
            nodeVisitedResults = []
            memoryUsageResults = []

            for q in queries:
                start = time.perf_counter()
                operation(q)
                timeResults.append(time.perf_counter() - start)
                nodeVisitedResults.append(structure.nodeVisited)

                if structure is ost:
                    tracemalloc.start()
                    start_mem, _ = tracemalloc.get_traced_memory()
                    operation(q)
                    current_mem, peak_mem = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    memoryUsageResults.append(peak_mem - start_mem)

            avg_time = sum(timeResults) / len(timeResults)
            total_time = sum(timeResults)
            avg_nodes = sum(nodeVisitedResults) / len(nodeVisitedResults)
            total_nodes = sum(nodeVisitedResults)

            print("Time Results: ", [f"{t * 1e6:.2f} µs" for t in timeResults])
            print("|\n|-> ", f"Average = {avg_time * 1e6:.2f} µs, Total = {total_time * 1e6:.2f} µs")
            print("\nNode Visited Results:", nodeVisitedResults)
            print("|\n|-> ", f"Average = {avg_nodes}, Total = {total_nodes}")

            if structure is ost:
                avg_mem = sum(memoryUsageResults) / len(memoryUsageResults)
                total_mem = sum(memoryUsageResults)
                print("\nMemory Results: ", [f"{m} B" for m in memoryUsageResults])
                print("|\n|-> ", f"Average = {avg_mem:.2f} B, Total = {total_mem} B")


runExperiment(SAMPLE_SIZE, N_QUERIES)
"""

import sys
import time
import random
import matplotlib.pyplot as plt
from linked_list import LinkedList
from binary_tree import OrderStatisticTree
from avl_tree import AugmentedAVLTree

SAMPLE_SIZES = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
N_QUERIES = 100

sys.setrecursionlimit(100000)


def runExperiment(sampleSize, nQueries):
    """Same core logic as the original main.py, but returns the averages
    instead of printing them."""

    ll = LinkedList()
    ost = OrderStatisticTree()
    avl = AugmentedAVLTree()

    print(f"EXPERIMENT WITH SAMPLE SIZE = {sampleSize}")

    data = random.sample(range(1, sampleSize * 100), sampleSize)
    for number in data:
        ll.orderedInsert(number)
        ost.treeInsert(number)
        avl.treeInsert(number)

    selectQueries = []
    for i in range(nQueries):
        selectQueries.append(random.randint(0, int(sampleSize * (4 / 3))))

    dataSet = set(data)
    rankQueries = []
    for i in range(nQueries):
        if random.random() < 0.75:
            rankQueries.append(random.choice(data))
        else:
            k = random.randint(1, sampleSize * 100)
            while k in dataSet:
                k = random.randint(1, sampleSize * 100)
            rankQueries.append(k)

    structures = [("LINKED LIST", ll), ("BINARY TREE", ost), ("AVL TREE", avl)]

    results = {}

    for name, structure in structures:
        operations = [("OS-SELECT", structure.osselect, selectQueries),
                      ("OS-RANK", structure.osrank, rankQueries)]

        for opName, operation, queries in operations:
            timeResults = []
            nodeVisitedResults = []

            for q in queries:
                start = time.perf_counter()
                operation(q)
                timeResults.append(time.perf_counter() - start)
                nodeVisitedResults.append(structure.nodeVisited)

            avg_time = sum(timeResults) / len(timeResults)
            avg_nodes = sum(nodeVisitedResults) / len(nodeVisitedResults)
            results[(name, opName)] = (avg_time, avg_nodes)

    return results


# ---- run the sweep across all sample sizes ----
allResults = {size: runExperiment(size, N_QUERIES) for size in SAMPLE_SIZES}

structureNames = ["LINKED LIST", "BINARY TREE", "AVL TREE"]
opNames = ["OS-SELECT", "OS-RANK"]
colors = {"LINKED LIST": "tab:red", "BINARY TREE": "tab:blue", "AVL TREE": "tab:green"}
markers = {"LINKED LIST": "o", "BINARY TREE": "s", "AVL TREE": "^"}

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

for col, opName in enumerate(opNames):
    timeAx = axes[0][col]
    nodesAx = axes[1][col]

    for name in structureNames:
        avgTimes = [allResults[size][(name, opName)][0] * 1e6 for size in SAMPLE_SIZES]
        avgNodes = [allResults[size][(name, opName)][1] for size in SAMPLE_SIZES]

        timeAx.plot(SAMPLE_SIZES, avgTimes, label=name, color=colors[name],
                    marker=markers[name])
        nodesAx.plot(SAMPLE_SIZES, avgNodes, label=name, color=colors[name],
                     marker=markers[name])

    timeAx.set_title(f"{opName} — Average Time")
    timeAx.set_xlabel("Sample Size")
    timeAx.set_ylabel("Average Time (µs)")
    timeAx.set_xscale("log")
    timeAx.set_yscale("log")
    timeAx.grid(True, which="both", alpha=0.3)
    timeAx.legend()

    nodesAx.set_title(f"{opName} — Average Nodes Visited")
    nodesAx.set_xlabel("Sample Size")
    nodesAx.set_ylabel("Average Nodes Visited")
    nodesAx.set_xscale("log")
    nodesAx.set_yscale("log")
    nodesAx.grid(True, which="both", alpha=0.3)
    nodesAx.legend()

fig.suptitle(f"OS-SELECT / OS-RANK Scaling ({N_QUERIES} queries per run)", fontsize=14)
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig("scaling_results.png", dpi=150)
print("Saved plot to scaling_results.png")
plt.show()