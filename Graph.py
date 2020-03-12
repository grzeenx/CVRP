import numpy as np
from math import sqrt, pow
import  os

class Graph:
    def __init__(self, lines_from_file):
        self.name = lines_from_file[0].split(':')[1].strip()
        self.comment = lines_from_file[1].split(':')[1].strip()
        self.type = lines_from_file[2].split(':')[1].strip()
        self.dimension = int(lines_from_file[3].split(':')[1].strip())
        self.edge_weight_type = lines_from_file[4].split(':')[1].strip()
        self.capacity = int(lines_from_file[5].split(':')[1].strip())
        self.edges = np.zeros((self.dimension, self.dimension))
        self.coordinates_list = []
        self.demands = []
        for line in lines_from_file[7:7 + self.dimension]:
            coords_as_text = line.split(' ')
            self.coordinates_list.append((int(coords_as_text[1]), int(coords_as_text[2])))
        for i, coordinates1 in enumerate(self.coordinates_list):
            for j, coordinates2 in enumerate(self.coordinates_list):
                if coordinates1 == coordinates2:
                    self.edges[i, j] = 0
                    continue
                self.edges[i, j] = sqrt(
                    pow(coordinates1[0] - coordinates2[0], 2) + pow(coordinates1[1] - coordinates2[1], 2))
        for line in lines_from_file[8 + self.dimension: 8 + 2 * self.dimension]:
            self.demands.append(int(line.split(' ')[1]))
        self.depot_index = int(lines_from_file[9 + 2 * self.dimension]) -1

    def __str__(self):
        returned_string = str(self.edges) + '\n'
        returned_string += f"{self.name}: dimension = {self.dimension}, capacity = {self.capacity}\n"
        returned_string += "Demands: " + str(self.demands) + '\n'
        returned_string += f"Depot vertex: {self.depot_index}"
        return returned_string



    @staticmethod
    def load_graph(filename, dataset_path):
        path = os.path.join(dataset_path, filename)
        with open(path, 'r') as file:
            lines = list(map(str.strip, file.readlines()))
        g = Graph(lines)
        # print(g)
        return g
