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

standard_as1 = StandardAntAlgorithm(g, 50, max_iterations=300, rho=0)
result = standard_as1.execute()
print(result)

standard_as1 = ElitistAntAlgorithm(g, 50, max_iterations=300, rho=0)
result = standard_as1.execute()
print(result)

standard_as1 = RankAntAlgorithm(g, 50, chosen_ants_count=15, max_iterations=300, rho=0)
result = standard_as1.execute()
print(result)
