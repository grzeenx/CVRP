from standars_as import StandardAntAlgorithm
import numpy as np


class ElitistAntAlgorithm(StandardAntAlgorithm):
    def __init__(self, graph, ants_count, max_iterations=50, alpha=1, beta=1, rho=0):

        super().__init__(graph, ants_count, max_iterations, alpha, beta, rho)
        self.best_ant_count = 0

    def perform_iteration_for_all_ants(self):
        new_pheromones = np.zeros((self.graph.dimension, self.graph.dimension))
        for ant in self.ants:
            route, cost = ant.perform_iteration()
            self.add_pheromones(new_pheromones, cost, route)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_route = route
                self.best_ant_count = 1
            elif cost == self.best_cost:
                self.best_ant_count += 1
        self.evaporate_pheromones()
        self.place_pheromones(new_pheromones)
        self.place_elitist_pheromone()
        self.best_ant_count = 0

    def place_elitist_pheromone(self):
        value_to_add = self.best_ant_count / self.best_cost
        for cycle in self.best_route:
            for vertex_from, vertex_to in zip(cycle, cycle[1:]):
                self.pheromones[vertex_from, vertex_to] += value_to_add
                self.pheromones[vertex_to, vertex_from] += value_to_add
            self.pheromones[cycle[-1], cycle[0]] += value_to_add
            self.pheromones[cycle[0], cycle[-1]] += value_to_add
