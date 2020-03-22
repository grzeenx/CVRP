from greedy import GreedyAlgorithm
import random

class Random_algorithm(GreedyAlgorithm):
    def __init__(self, graph,exp_seed=777):
        super().__init__(graph)
        random.seed(exp_seed)

    def find_closest(self, vertices_to_visit):
        '''
        Randomly
        :param vertices_to_visit:
        :return:
        '''
        n= len(vertices_to_visit)

        return vertices_to_visit[random.randint(0,n-1)]
