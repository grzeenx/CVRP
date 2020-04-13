import pathlib
import os
from Graph import Graph
from greedy import GreedyAlgorithm
from standars_as import StandardAntAlgorithm
from elitist import ElitistAntAlgorithm
from rank import RankAntAlgorithm
from pso import Pso_Algorithm
from random_algorithm import Random_algorithm
import csv
import time


class Test:
    def __init__(self, graph_path=None, max_iterations=None, ant_count=None, chosen_ants_count=None, alpha=None,
                 beta=None, gamma=None, rho=None, exp_seed=None,
                 alpha_ant=None, beta_ant=None):
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
        self.path_to_csv = "result.csv"
        self.result = None

    def pretty_print(self, _result):
        route, cost, iteration_of_best = _result
        # for i, cycle in enumerate(route):
        #     vertices_as_text = ""
        #     for vertex in cycle:
        #         vertices_as_text += f"{vertex + 1} "
        #     print(f"Route #{i + 1}: {vertices_as_text}")
        print(f"Cost\t{cost}\n")

    def check_sum(self, _result):
        route = _result[0]
        sum = 0
        load = 0
        max_load = self.graph.capacity
        for cycle in route:
            for vertex_before, vertex_after in zip(cycle, cycle[1:]):
                sum += self.graph.edges[vertex_before, vertex_after]
                print(
                    f"Vertices {vertex_before + 1}-{vertex_after + 1} add to sum {self.graph.edges[vertex_before, vertex_after]}")
                load += self.graph.demands[vertex_after]
                if load > max_load:
                    print("too much load!", load)
            load = 0
            sum += self.graph.edges[cycle[-1], cycle[0]]
            print(f"Vertices {cycle[-1] + 1}-{cycle[0] + 1} add to sum {self.graph.edges[cycle[-1], cycle[0]]}")

        print(f"Sum checked: {sum}\n")

    def write_row(self, algorithm_name):
        with open(self.path_to_csv, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            row = [algorithm_name, self.ant_count, self.max_iterations, self.exp_seed, self.alpha_ant, self.beta_ant,
                   self.rho, self.chosen_ants_count, self.alpha, self.beta, self.gamma, round(self.result[1], 2), round(self.time_in_seconds,10), self.result[2]]
            csv_writer.writerow(row)

    def run(self, algorithm, path=None, print_iterations=False):
        """
        Runs the algorithms and saves the result in the csv file and measures the time of execution.
        :param algorithm: which algorithms should be run
        :param path: path to save the csv. default is result.csv
        :param print_iterations: NOT IMPLEMENTED
        """
        #time measuring
        start, end = 0., 0.

        if path is not None:
            self.path_to_csv = path

        if algorithm == "greedy":
            start = time.time()
            greedy_1 = GreedyAlgorithm(self.graph)
            self.result = greedy_1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("greedy")

        elif algorithm == "random":
            start = time.time()
            random_1 = Random_algorithm(self.graph, self.exp_seed)
            self.result = random_1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("random")

        elif algorithm == "standard":
            start = time.time()
            standard_as1 = StandardAntAlgorithm(self.graph, self.ant_count, max_iterations=self.max_iterations,
                                                rho=self.rho, exp_seed=self.exp_seed, alpha=self.alpha_ant,
                                                beta=self.beta_ant)
            self.result = standard_as1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("standard")

        elif algorithm == "elitist":
            start = time.time()
            elitist_as1 = ElitistAntAlgorithm(self.graph, self.ant_count, max_iterations=self.max_iterations,
                                              rho=self.rho,
                                              exp_seed=self.exp_seed, alpha=self.alpha_ant, beta=self.beta_ant)
            self.result = elitist_as1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("elitist")

        elif algorithm == "rank":
            start = time.time()

            rank_as1 = RankAntAlgorithm(self.graph, self.ant_count, chosen_ants_count=self.chosen_ants_count,
                                        max_iterations=self.max_iterations, rho=self.rho, exp_seed=self.exp_seed,
                                        alpha=self.alpha_ant, beta=self.beta_ant)
            self.result = rank_as1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("rank")

        elif algorithm == "pso":
            start = time.time()
            pso_1 = Pso_Algorithm(self.graph, alpha=self.alpha, beta=self.beta, gamma=self.gamma,
                                  particle_count=self.ant_count, max_iterations=self.max_iterations,
                                  exp_seed=self.exp_seed)

            self.result = pso_1.execute()
            end = time.time()
            self.time_in_seconds = end - start
            self.write_row("pso")
