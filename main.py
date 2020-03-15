import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm


def pretty_print(_result):
    route, cost = _result
    for i, cycle in enumerate(route):
        vertices_as_text = ""
        for vertex in cycle:
            vertices_as_text += f"{vertex + 1} "
        print(f"Route #{i + 1}: {vertices_as_text}")
    print(f"Cost {cost}\n")


dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
g = Graph.load_graph("E-n22-k4.txt", dataset_path)

greedy_1 = GreedyAlgorithm(g)
result = greedy_1.greedy()
pretty_print(result)

standard_as1 = StandardAntAlgorithm(g, 10, max_iterations=100, rho=0)
result = standard_as1.execute()
pretty_print(result)

standard_as1 = ElitistAntAlgorithm(g, 10, max_iterations=100, rho=0)
result = standard_as1.execute()
pretty_print(result)

standard_as1 = RankAntAlgorithm(g, 10, chosen_ants_count=5, max_iterations=100, rho=0)
result = standard_as1.execute()
pretty_print(result)
