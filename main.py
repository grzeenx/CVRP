import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm
from pso import Pso_Algorithm


def pretty_print(_result):
    route, cost = _result
    for i, cycle in enumerate(route):
        vertices_as_text = ""
        for vertex in cycle:
            vertices_as_text += f"{vertex + 1} "
        print(f"Route #{i + 1}: {vertices_as_text}")
    print(f"Cost {cost}\n")


def check_sum(_result):
    route = _result[0]
    sum = 0
    for cycle in route:
        for vertex_before, vertex_after in zip(cycle, cycle[1:]):
            sum += g.edges[vertex_before, vertex_after]
            print(f"Vertices {vertex_before + 1}-{vertex_after + 1} add to sum {g.edges[vertex_before, vertex_after]}")
        sum += g.edges[cycle[-1], cycle[0]]
        print(f"Vertices {cycle[-1] + 1}-{cycle[0] + 1} add to sum {g.edges[cycle[-1], cycle[0]]}")
    print(f"Sum checked: {sum}\n")


dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
g = Graph.load_graph("E-n22-k4.txt", dataset_path)

# greedy_1 = GreedyAlgorithm(g)
# result = greedy_1.greedy()
# pretty_print(result)
# # check_sum(result)
#
# standard_as1 = StandardAntAlgorithm(g, 30, max_iterations=500, rho=0)
# result = standard_as1.execute()
# pretty_print(result)
# # check_sum(result)
#
# standard_as1 = ElitistAntAlgorithm(g, 30, max_iterations=500, rho=0)
# result = standard_as1.execute()
# pretty_print(result)
# # check_sum(result)
#
# standard_as1 = RankAntAlgorithm(g, 30, chosen_ants_count=10, max_iterations=500, rho=0)
# result = standard_as1.execute()
# pretty_print(result)
# # check_sum(result)


pso_1= Pso_Algorithm(g, alpha=0.6, beta=0.85, gamma=0.5, particle_count=100, max_iterations=100)
result = pso_1.execute()
pretty_print(result)
# check_sum(result)


