import numpy as np


class GreedyAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.capacity = self.graph.capacity
        self.current_vertex = self.graph.depot_index
        self.cost = 0
        self.cycles = [[self.graph.depot_index]]
        self.active_vertices = [False] + [True] * (self.graph.dimension - 1)
        self.capacity_left = self.capacity

    def execute(self):
        while True in self.active_vertices:
            vertices_to_visit = self.get_vertices()
            if vertices_to_visit == []:
                self.go_to(self.graph.depot_index)
            else:
                vertex_index = self.find_closest(vertices_to_visit)
                self.go_to(vertex_index)
        self.cost += self.graph.edges[self.current_vertex, self.graph.depot_index]
        return self.cycles, self.cost, 1

    def find_closest(self, vertices_to_visit):
        distances = [self.graph.edges[self.current_vertex, i] for i in vertices_to_visit]
        return vertices_to_visit[np.argmin(distances)]

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
