import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm

dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
g = Graph.load_graph("E-n22-k4.txt", dataset_path)

greedy_1 = GreedyAlgorithm(g)
result = greedy_1.greedy()
print(result)

standard_as1 = StandardAntAlgorithm(g, 100, max_iterations=1000, rho=0)
result = standard_as1.execute()
print(result)

standard_as1 = ElitistAntAlgorithm(g, 100, max_iterations=1000, rho=0)
result = standard_as1.execute()
print(result)

standard_as1 = RankAntAlgorithm(g, 100, chosen_ants_count=10, max_iterations=1000, rho=0)
result = standard_as1.execute()
print(result)
