import numpy as np
import math
import random


class Ant:
    def __init__(self, graph, pheromones, alpha, beta):
        self.graph = graph
        self.pheromones = pheromones
        self.alpha = alpha
        self.beta = beta
        self.current_vertex = self.graph.depot_index
        self.cost = 0
        self.cycles = [[self.graph.depot_index]]
        self.capacity = self.graph.capacity
        self.active_vertices = [False] + [True] * (self.graph.dimension - 1)
        self.capacity_left = self.capacity

    def perform_iteration(self):
        while True in self.active_vertices:
            vertices_to_visit = self.get_vertices()
            if not vertices_to_visit:
                self.go_to(self.graph.depot_index)
            else:
                vertex_index = self.roulette_choose(vertices_to_visit)
                self.go_to(vertex_index)
        return self.cycles, self.cost

    def roulette_choose(self, vertices_to_visit):
        distances = [self.graph.edges[self.current_vertex, i] for i in vertices_to_visit]
        pheromones = [self.pheromones[self.current_vertex, i] for i in vertices_to_visit]
        coefficients = []

        for i, vertex in enumerate(vertices_to_visit):
            value = (pheromones[i] ** self.alpha) * ((1 / distances[i]) ** self.beta)
            coefficients.append(value)

        sum_of_coefficients = sum(coefficients)
        if sum_of_coefficients != 0:
            probabilities = list(map(lambda x: x / sum_of_coefficients, coefficients))
        else:
            probabilities = list(map(lambda x: x, coefficients))
        probabilities_normalized = []
        sum_of_probabilities = 0
        for probability in probabilities:
            probabilities_normalized.append(sum_of_probabilities)
            sum_of_probabilities += probability
        probabilities_normalized.append(1)
        random_number = random.random()
        which_range = 0
        for prob1, prob2 in zip(probabilities_normalized, probabilities_normalized[1:]):
            if prob1 <= random_number < prob2:
                break
            which_range += 1
        return vertices_to_visit[which_range]

    def go_to(self, index):
        if index == self.graph.depot_index:
            self.capacity_left = self.capacity
            self.cycles.append([])
        else:
            self.capacity_left -= self.graph.demands[index]
        self.cost += self.graph.edges[self.current_vertex, index]
        self.current_vertex = index
        self.cycles[-1].append(self.current_vertex)
        self.active_vertices[index] = False

    def get_vertices(self):
        vertices = []
        for i in range(len(self.active_vertices)):
            if self.active_vertices[i]:
                if self.graph.demands[i] <= self.capacity_left:
                    vertices.append(i)
        return vertices


class StandardAntAlgorithm:
    def __init__(self, graph, ants_count, max_iterations=50, alpha=1, beta=1, rho=0, exp_seed=777):
        random.seed(exp_seed)
        self.max_iterations = max_iterations
        self.ants_count = ants_count
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.graph = graph
        self.pheromones = np.ones((graph.dimension, graph.dimension))
        self.best_cost = math.inf
        self.best_route = None
        self.iteration_count = 0
        self.ants = []
        self.initialize_ants()

    def initialize_ants(self):
        self.ants = []
        for i in range(self.ants_count):
            self.ants.append(Ant(self.graph, self.pheromones, self.alpha, self.beta))

    def execute(self):
        for i in range(self.max_iterations):
            self.perform_iteration_for_all_ants()
            self.initialize_ants()
        self.best_cost += self.graph.edges[self.best_route[-1][-1], self.graph.depot_index]
        return self.best_route, self.best_cost

    def perform_iteration_for_all_ants(self):
        new_pheromones = np.ones((self.graph.dimension, self.graph.dimension))
        for ant in self.ants:
            route, cost = ant.perform_iteration()
            self.add_pheromones(new_pheromones, cost, route)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_route = route
        self.evaporate_pheromones()
        self.place_pheromones(new_pheromones)

    def add_pheromones(self, new_pheromones, cost, route):
        if cost == 0:
            return
        value_to_add = 1 / cost
        for cycle in route:
            for vertex_from, vertex_to in zip(cycle, cycle[1:]):
                new_pheromones[vertex_from, vertex_to] += value_to_add
                new_pheromones[vertex_to, vertex_from] += value_to_add
            new_pheromones[cycle[-1], cycle[0]] += value_to_add
            new_pheromones[cycle[0], cycle[-1]] += value_to_add

    def evaporate_pheromones(self):
        vfunc = np.vectorize(lambda x: (1 - self.rho) * x)
        self.pheromones = vfunc(self.pheromones)

    def place_pheromones(self, new_pheromones):
        for (i, j), value in np.ndenumerate(new_pheromones):
            self.pheromones[i, j] += new_pheromones[i, j]
