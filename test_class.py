import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm
from pso import Pso_Algorithm
from random_algorithm import Random_algorithm


class Test:
    def __init__(self, graph_path, max_iterations, ant_count, chosen_ants_count, alpha, beta, gamma, rho, exp_seed,
                 alpha_ant, beta_ant):
        dataset_path = os.path.join(pathlib.Path().absolute(), "dataset")
        self.graph = Graph.load_graph(graph_path, dataset_path)
        self.max_iterations = max_iterations
        self.ant_count = ant_count
        self.chosen_ants_count = chosen_ants_count
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.rho = rho
        self.exp_seed = exp_seed
        self.alpha_ant = alpha_ant
        self.beta_ant = beta_ant

    def pretty_print(self, _result):
        route, cost = _result
        for i, cycle in enumerate(route):
            vertices_as_text = ""
            for vertex in cycle:
                vertices_as_text += f"{vertex + 1} "
            print(f"Route #{i + 1}: {vertices_as_text}")
        print(f"Cost\t{cost}\n")

    def check_sum(self, _result):
        route = _result[0]
        sum = 0
        load = 0
        max_load = g.capacity
        for cycle in route:
            for vertex_before, vertex_after in zip(cycle, cycle[1:]):
                sum += self.graph.edges[vertex_before, vertex_after]
                print(
                    f"Vertices {vertex_before + 1}-{vertex_after + 1} add to sum {g.edges[vertex_before, vertex_after]}")
                load += self.graph.demands[vertex_after]
                if load > max_load:
                    print("too much load!", load)
            load = 0
            sum += g.edges[cycle[-1], cycle[0]]
            print(f"Vertices {cycle[-1] + 1}-{cycle[0] + 1} add to sum {g.edges[cycle[-1], cycle[0]]}")

        print(f"Sum checked: {sum}\n")

    def run(self, print_iterations=False):
        greedy_1 = GreedyAlgorithm(self.graph)
        result = greedy_1.greedy()
        print("==========GREEDY ALGORITHM==========")
        self.pretty_print(result)

        random_1 = Random_algorithm(self.graph, self.exp_seed)
        result = random_1.greedy()
        print("==========RANDOM ALGORITHM==========")
        self.pretty_print(result)

        standard_as1 = StandardAntAlgorithm(self.graph, self.ant_count, max_iterations=self.max_iterations,
                                            rho=self.rho, exp_seed=self.exp_seed, alpha=self.alpha_ant,
                                            beta=self.beta_ant)
        result = standard_as1.execute()
        print("==========ORIGINAL ANT COLONY OPTIMIZATION==========")
        self.pretty_print(result)

        elitist_as1 = ElitistAntAlgorithm(self.graph, self.ant_count, max_iterations=self.max_iterations, rho=self.rho,
                                          exp_seed=self.exp_seed, alpha=self.alpha_ant, beta=self.beta_ant)
        result = elitist_as1.execute()
        print("==========ELITIST ANT COLONY OPTIMIZATION==========")
        self.pretty_print(result)

        rank_as1 = RankAntAlgorithm(self.graph, self.ant_count, chosen_ants_count=self.chosen_ants_count,
                                    max_iterations=self.max_iterations, rho=self.rho, exp_seed=self.exp_seed,
                                    alpha=self.alpha_ant, beta=self.beta_ant)
        result = rank_as1.execute()
        print("==========RANK ANT COLONY OPTIMIZATION==========")
        self.pretty_print(result)

        pso_1 = Pso_Algorithm(self.graph, alpha=self.alpha, beta=self.beta, gamma=self.gamma,
                              particle_count=self.ant_count, max_iterations=self.max_iterations, exp_seed=self.exp_seed)
        result = pso_1.execute()
        print("==========PARTICLE SWARM OPTIMIZATION==========")
        self.pretty_print(result)
