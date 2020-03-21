from random import shuffle


class Particle:
    '''
    Class that keeps the particle information
    '''

    def __init__(self, dimension, gbest, depot_id=0):
        vertices = shuffle([i for i in range(dimension) if i != depot_id])
        # x, current location, current solving route(without zeroes)
        self.route_without_base = vertices
        # global best - without zeroes
        self.gbest = gbest
        # personal best - without zeroes
        self.pbest = vertices.copy()
        # sequence of swaps
        self.velocity = []

    def set_gbest(self, gbest):
        self.gbest = gbest

    def set_pbest(self, pbest):
        self.pbest = pbest.copy()

    def do_swaps(self):
        for swap in self.velocity:
            self.do_swap(swap)
        #A potem z gamma i czesciowym usuwaniem
        self.velocity = []

    def do_swap(self, swap):
        id_1, id_2 = swap
        self.route_without_base[id_1], self.route_without_base[id_2] = self.route_without_base[id_2], self.route_without_base[id_1]



class Pso_Algorithm:
    def __init__(self, graph, alpha=0.85, beta=0.85, gamma=0, particle_count=10, max_iterations=10):
        self.graph = graph
        self.particle_count = particle_count
        self.gbest = shuffle([i for i in range(self.graph.dimension) if i != self.graph.depot_index])
        self.particles = [Particle(self.graph.dimension, self.gbest, self.graph.depot_index) for i in
                          range(self.particle_count)]
        self.max_iterations = max_iterations

    def count_cost(self, route_without_base):
        '''
        counts the cost and route as list of cycles
        '''
        # return cost, route
        return 0, [[]]

    def execute(self):
        for i in range(self.max_iterations):
            self.perform_iteration_for_all_particles()

    def perform_iteration_for_all_particles(self):
        for particle in self.particles:
            pass
    def count_sequence(self):
        pass
