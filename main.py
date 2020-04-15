import csv
from itertools import product
from datetime import datetime

from test_class import Test

counter = 1


def create_file(path):
    with open(path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ["ALG_NAME", "ANT_COUNT", "MAX_IT", "SEED", "ALPHA_ANT", "BETA_ANT", "RHO", "CHOSEN_ANTS", "ALPHA_PSO",
             "BETA_PSO", "GAMMA", "SCORE", "TIME [s]", "ITERATION OF BEST"])


def print_estimated_iteration_counter():
    no_standard = len(files) * len(seeds) * len(ant_counts) * len(alphas_ant) * len(betas_ant) * len(rhos) * len(
        max_iterations_list)
    no_pso = len(files) * len(seeds) * len(ant_counts) * len(alphas_pso) * len(betas_pso) * len(gammas_pso) * len(
        max_iterations_list)

    sum_of_iterations = 0
    if "greedy" in algorithms:
        sum_of_iterations += len(files)
    if "random" in algorithms:
        sum_of_iterations += len(files) * len(seeds)
    if "standard" in algorithms:
        sum_of_iterations += no_standard
    if "elitist" in algorithms:
        sum_of_iterations += no_standard
    if "rank" in algorithms:
        sum_of_iterations += no_standard * len(chosen_ant_percents)
    if "pso" in algorithms:
        sum_of_iterations += no_pso
    print(f"Estimated iterations: {sum_of_iterations}")


def print_and_increment_counter():
    global counter
    print(f"Iteration {counter}: ", end='')
    counter += 1


def iterate_over(algorithm, file, id="", to_result = None):
    now = datetime.now()
    result_filename = f"res_{id}_{file}_{algorithm}_{now.hour}{now.minute}{now.second}.txt"
    create_file(result_filename)

    if algorithm == "greedy":
        Test(graph_path=file).run(path=result_filename, algorithm=algorithm)
        print_and_increment_counter()
        print(f"{algorithm} {file}")

    elif algorithm == "random":
        for exp_seed in seeds:
            Test(graph_path=file, exp_seed=exp_seed).run(path=result_filename, algorithm=algorithm)
            print_and_increment_counter()
            print(f"{algorithm} {file}_s{exp_seed}")

    elif algorithm == "standard" or algorithm == "elitist":
        for exp_seed, max_iterations, ant_count, alpha_ant, beta_ant, rho in product(seeds, max_iterations_list,
                                                                                     ant_counts, alphas_ant, betas_ant,
                                                                                     rhos):
            Test(graph_path=file, max_iterations=max_iterations, ant_count=ant_count, rho=rho, exp_seed=exp_seed,
                 alpha_ant=alpha_ant, beta_ant=beta_ant).run(path=result_filename, algorithm=algorithm, to_result=to_result)
            print_and_increment_counter()
            print(
                f"{algorithm} {file}_s{exp_seed}_its{max_iterations}_ants{ant_count}_a{alpha_ant}_b{beta_ant}_r{rho}")

    elif algorithm == "rank":
        for exp_seed, max_iterations, ant_count, alpha_ant, beta_ant, rho, chosen_ant_percent in product(seeds,
                                                                                                         max_iterations_list,
                                                                                                         ant_counts,
                                                                                                         alphas_ant,
                                                                                                         betas_ant,
                                                                                                         rhos,
                                                                                                         chosen_ant_percents):
            Test(graph_path=file, max_iterations=max_iterations, ant_count=ant_count, rho=rho, exp_seed=exp_seed,
                 alpha_ant=alpha_ant, beta_ant=beta_ant, chosen_ants_count=round(ant_count * chosen_ant_percent)).run(
                path=result_filename, algorithm=algorithm, to_result=to_result)
            print_and_increment_counter()
            print(
                f"{algorithm} {file}_s{exp_seed}_its{max_iterations}_ants{ant_count}_a{alpha_ant}_b{beta_ant}_r{rho}_chosen{chosen_ant_percent}")

    elif algorithm == "pso":
        for exp_seed, max_iterations, ant_count, alpha_pso, beta_pso, gamma in product(seeds,
                                                                                       max_iterations_list,
                                                                                       ant_counts,
                                                                                       alphas_pso,
                                                                                       betas_pso,
                                                                                       gammas_pso
                                                                                       ):
            Test(graph_path=file, max_iterations=max_iterations, ant_count=ant_count, gamma=gamma, exp_seed=exp_seed,
                 alpha=alpha_pso, beta=beta_pso).run(path=result_filename, algorithm=algorithm, to_result=to_result)
            print_and_increment_counter()
            print(
                f"{algorithm} {file}_s{exp_seed}_its{max_iterations}_ants{ant_count}_a{alpha_pso}_b{beta_pso}_g{gamma}")


def run_algorithms(_algorithms, id="", to_results=None):
    print_estimated_iteration_counter()
    for i, file in enumerate(files):
        for algorithm in _algorithms:
            to_result = None
            if to_results is not None:
                to_result = to_results[i]
            iterate_over(algorithm, file, id=id, to_result=to_result)


files = ["E-n51-k5.txt", "E-n76-k8.txt", "E-n101-k14.txt"]
# files = ["E-n22-k4.txt", "E-n33-k4.txt", "E-n51-k5.txt", "E-n76-k8.txt", "E-n76-k10.txt", "E-n101-k8.txt",
#          "E-n101-k14.txt"]


seeds = [6666, 7777, 8888, 9213]
# parameters of the algorithms - constant for the experiments
rhos = [0]
alphas_ant = [10]
betas_ant = [4]
chosen_ant_percents = [0.2]
alphas_pso = [0.85]
betas_pso = [0.55]
gammas_pso = [0.5]
ant_counts = [200]

# # H1
# algorithms = ["greedy", "random", "standard", "elitist", "rank"]
# max_iterations_list = [50]
# run_algorithms(algorithms, id="H1")
#
# # H2
# algorithms = ["standard", "elitist", "rank", "pso"]
# max_iterations_list = [200]
# run_algorithms(algorithms, id="H2")
#
# #H3
#
# algorithms = ["greedy", "random","standard", "elitist", "rank", "pso"]
# max_iterations_list = [100]
# run_algorithms(algorithms, id="H3")
#
# #H4
#
# algorithms = ["greedy", "random","standard", "elitist", "rank", "pso"]
# max_iterations_list = [150]
# run_algorithms(algorithms, id="H4")


# dla kazdego algorytmu, dla kazdego datasetu
# najpierw greedy dla kazdego grafu wyniki i czasy:
# 51 : (711.5,0.000998497)
# 76 : (1149.41,0.0009937286)
# 101 : (1610.91,0.0029630661)


# H5
algorithms = ["standard", "elitist", "rank", "pso"]
max_iterations_list = [200]
run_algorithms(algorithms, id="H5", to_results=[711.5,1149.41,1610.91])
