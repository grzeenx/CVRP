from standars_as import StandardAntAlgorithm
import math


class RankAntAlgorithm(StandardAntAlgorithm):
    def __init__(self, graph, ants_count, chosen_ants_count, max_iterations=50, alpha=1, beta=1, rho=0, exp_seed=777):

        super().__init__(graph, ants_count, max_iterations, alpha, beta, rho,exp_seed=exp_seed)
        self.chosen_ants_count = chosen_ants_count
        self.best_costs_and_routes = [(math.inf, [[]])]

    def perform_iteration_for_all_ants(self):
        for ant in self.ants:
            route, cost = ant.perform_iteration()
            if cost < self.best_costs_and_routes[-1][0]:
                if len(self.best_costs_and_routes) < self.chosen_ants_count:
                    self.best_costs_and_routes.append((cost, route))
                else:
                    self.best_costs_and_routes[-1] = (cost, route)
                self.best_costs_and_routes.sort(key=lambda tup: tup[0])
        self.evaporate_pheromones()
        self.place_best_pheromones()
        if self.best_costs_and_routes[0][0] < self.best_cost:
            self.best_cost = self.best_costs_and_routes[0][0]
            self.best_route = self.best_costs_and_routes[0][1]
        self.best_costs_and_routes = [(math.inf, [[]])]

    def place_best_pheromones(self):
        for i, cost_and_route in enumerate(self.best_costs_and_routes):
            value_to_add = (self.chosen_ants_count - i) / cost_and_route[0]
            for cycle in cost_and_route[1]:
                for vertex_from, vertex_to in zip(cycle, cycle[1:]):
                    self.pheromones[vertex_from, vertex_to] += value_to_add
                    self.pheromones[vertex_to, vertex_from] += value_to_add
                self.pheromones[cycle[-1], cycle[0]] += value_to_add
                self.pheromones[cycle[0], cycle[-1]] += value_to_add
