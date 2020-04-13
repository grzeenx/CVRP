from random import shuffle, random, seed


class Particle:
    '''
    Class that keeps the particle information
    '''

    def __init__(self, graph, gbest, gbest_cost, alpha, beta, gamma, depot_id=0):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.graph = graph
        vertices = [i for i in range(self.graph.dimension) if i != depot_id]
        shuffle(vertices)
        # x, current location, current solving route(without zeroes)
        self.route_without_base = vertices
        # global best - without zeroes
        self.gbest = gbest
        self.gbest_cost = gbest_cost

        # personal best - without zeroes
        self.pbest = vertices.copy()
        self.pbest_cost = count_cost(self.pbest, self.graph)[0]

        # sequence of swaps
        self.velocity = []

    def set_gbest(self, gbest, gbest_cost):
        self.gbest_cost = gbest_cost
        self.gbest = gbest

    def do_swaps(self):
        for swap in self.velocity:
            self.do_swap(swap)
        if random() >= self.gamma:
            self.velocity = []

    def do_swap(self, swap):
        id_1, id_2 = swap
        self.route_without_base[id_1], self.route_without_base[id_2] = self.route_without_base[id_2], \
                                                                       self.route_without_base[id_1]

    def find_sequence(self, route_1, route_2):
        sequence = []
        route_1_copy = route_1.copy()
        for i, vertex in enumerate(route_1_copy):
            id_in_route_2 = route_2.index(vertex)
            if id_in_route_2 != i:
                sequence.append((i, id_in_route_2))
                route_1_copy[i], route_1_copy[id_in_route_2] = route_1_copy[id_in_route_2], route_1_copy[i]
        return sequence

    def move(self):
        '''
        Move the partcicle
        '''
        if random() >= self.alpha:
            self.velocity += self.find_sequence(self.route_without_base, self.pbest)
        if random() >= self.beta:
            self.velocity += self.find_sequence(self.route_without_base, self.gbest)
        self.do_swaps()
        cost = count_cost(self.route_without_base, self.graph)[0]
        if cost < self.pbest_cost:
            self.pbest = self.route_without_base
            self.pbest_cost = cost
        return cost, self.route_without_base


class Pso_Algorithm:
    def __init__(self, graph, alpha=0.85, beta=0.85, gamma=0, particle_count=10, max_iterations=10, exp_seed=777):
        '''
        Class that realises PSO algorithm.
        :param graph:
        :param alpha: pbest vecrtor probability
        :param beta: gbest vecrtor probability
        :param gamma: innertion vecrtor probability, partly deletes the previous velocity
        :param particle_count: how many particles in the algorithm
        :param max_iterations: how many iterations
        '''
        seed(exp_seed)
        self.graph = graph
        self.particle_count = particle_count
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.gbest = [i for i in range(self.graph.dimension) if i != self.graph.depot_index]
        shuffle(self.gbest)
        self.gbest_cost = count_cost(self.gbest, self.graph)[0]
        self.particles = [
            Particle(self.graph, self.gbest, self.gbest_cost, self.alpha, self.beta, self.gamma, self.graph.depot_index)
            for i in range(self.particle_count)]
        self.max_iterations = max_iterations

        self.iteration_best_occured = 0

    def execute(self):
        for i in range(self.max_iterations):
            self.perform_iteration_for_all_particles(i)
        _, route_with_zeroes = count_cost(self.gbest, self.graph)
        return route_with_zeroes, self.gbest_cost, self.iteration_best_occured

    def perform_iteration_for_all_particles(self, iteration):
        gbest_changed = False
        for particle in self.particles:
            cost, route = particle.move()
            if cost < self.gbest_cost:
                gbest_changed = True
                self.gbest_cost = cost
                self.gbest = route.copy()
                self.iteration_best_occured = iteration
        if gbest_changed:
            self.update_gbest()

    def update_gbest(self):
        for particle in self.particles:
            particle.set_gbest(self.gbest, self.gbest_cost)


def count_cost(route, graph):
    '''
    counts the cost and route as list of cycles
    '''

    current_cost = 0
    current_load = 0
    max_load = graph.capacity
    current_vertex = graph.depot_index
    route_with_zeroes = [[current_vertex]]

    for vertex in route:
        distance = graph.edges[current_vertex, vertex]
        demand = graph.demands[vertex]
        if current_load + demand <= max_load:
            route_with_zeroes[-1].append(vertex)
            current_cost += distance
            current_load += demand
            current_vertex = vertex
        else:
            route_with_zeroes.append([])
            route_with_zeroes[-1].append(graph.depot_index)
            route_with_zeroes[-1].append(vertex)
            current_cost += graph.edges[current_vertex, graph.depot_index] + graph.edges[graph.depot_index, vertex]
            current_load = demand
            current_vertex = vertex

    current_cost += graph.edges[current_vertex, graph.depot_index]
    return current_cost, route_with_zeroes
