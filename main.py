import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm




dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
g=Graph.load_graph("E-n22-k4.txt", dataset_path)

greedy_1 = GreedyAlgorithm(g)
result = greedy_1.greedy()
print(result)





