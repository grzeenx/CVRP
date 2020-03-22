import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm
from pso import Pso_Algorithm
from random_algorithm import Random_algorithm


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
    load= 0
    max_load = g.capacity
    for cycle in route:
        for vertex_before, vertex_after in zip(cycle, cycle[1:]):
            sum += g.edges[vertex_before, vertex_after]
            print(f"Vertices {vertex_before + 1}-{vertex_after + 1} add to sum {g.edges[vertex_before, vertex_after]}")
            load+=g.demands[vertex_after]
            if load > max_load:
                print("too much load!", load)
        load=0
        sum += g.edges[cycle[-1], cycle[0]]
        print(f"Vertices {cycle[-1] + 1}-{cycle[0] + 1} add to sum {g.edges[cycle[-1], cycle[0]]}")

    print(f"Sum checked: {sum}\n")


dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
g = Graph.load_graph("E-n22-k4.txt", dataset_path)
# g = Graph.load_graph("E-n33-k4.txt", dataset_path)

max_iterations= 100
ant_count = 150
alpha =0.55
beta = 0.85
gamma=0.5
#evaporating
rho= 0
exp_seed=100
alpha_ant=1
beta_ant=1


greedy_1 = GreedyAlgorithm(g)
result = greedy_1.greedy()
pretty_print(result)
# check_sum(result)

random_1 = Random_algorithm(g,exp_seed)
result = random_1.greedy()
pretty_print(result)


# standard_as1 = StandardAntAlgorithm(g, ant_count, max_iterations=max_iterations, rho=rho,exp_seed=exp_seed, alpha=alpha_ant, beta=beta_ant)
# result = standard_as1.execute()
# pretty_print(result)
# # check_sum(result)
#
# elitist_as1 = ElitistAntAlgorithm(g, ant_count, max_iterations=max_iterations, rho=rho,exp_seed=exp_seed,alpha=alpha_ant, beta=beta_ant)
# result = elitist_as1.execute()
# pretty_print(result)
# # check_sum(result)
#
# rank_as1 = RankAntAlgorithm(g, ant_count, chosen_ants_count=10, max_iterations=max_iterations, rho=rho,exp_seed=exp_seed,alpha=alpha_ant, beta=beta_ant)
# result = rank_as1.execute()
# pretty_print(result)
# # check_sum(result)
#
# # for i in range(111, 1000, 42):
# pso_1= Pso_Algorithm(g, alpha=alpha, beta=beta, gamma=gamma, particle_count=ant_count, max_iterations=max_iterations, exp_seed=exp_seed)
# result = pso_1.execute()
# pretty_print(result)
# # check_sum(result)
#
#









