from itertools import product
from test_class import Test
import csv


def create_file(path):
    with open(path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ["it", "ant_count", "alpha_ant", "beta_ant", "greedy", "random", "standard", "rank", "elit", "pso"])


algorithms = ["standard", "elitist"]
# algorithms = ["rank"]
# algorithms = ["pso"]
files = ["E-n22-k4.txt", "E-n33-k4.txt", "E-n51-k5.txt", "E-n76-k8.txt", "E-n76-k10.txt", "E-n101-k8.txt",
         "E-n101-k14.txt"]
ant_counts = [200]
max_iterations_list = [50]
seeds = [6666, 7777, 8888]

rhos = [0]
alphas_ant = [10]
betas_ant = [4]

chosen_ant_percents = [0.02, 0.1, 0.2]

alphas_pso = [0.55, 0.85]
betas_pso = [0.55, 0.85]
gammas_pso = [0, 0.5, 1]

counter = 0
for file in files:
    result_filename = f"res_{file}_{'_'.join(algorithms)}.txt"
    create_file(result_filename)
    for exp_seed, max_iterations, ant_count, alpha_ant, beta_ant, rho in product(seeds, max_iterations_list,
                                                                                 ant_counts, alphas_ant, betas_ant,
                                                                                 rhos):
        Test("E-n22-k4.txt", max_iterations=max_iterations, ant_count=ant_count,
             chosen_ants_count=None, alpha=None, beta=None,
             gamma=None, rho=rho, exp_seed=exp_seed, alpha_ant=alpha_ant, beta_ant=beta_ant).run(
            path=result_filename, algorithms=algorithms)
        counter += 1
        print(f"{counter}) {file}_s{exp_seed}_its{max_iterations}_ants{ant_count}_a{alpha_ant}_b{beta_ant}_r{rho}")

# alpha 0.55
# beta =0.85
# ants_count, max_iterations=50, alpha=1, beta=1, rho=0
#
# self, graph, ants_count, chosen_ants_count, max_iterations=50, alpha=1, beta=1, rho=0
#
# ants_count, max_iterations=50, alpha=1, beta=1, rho=0
#
#
# alpha=0.85, beta=0.85, gamma=0, particle_count=10, max_iterations=10
