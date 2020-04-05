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
ant_counts = [50, 100, 200]
max_iterations = [30, 100, 150]
seeds = [6666, 7777, 8888]
rhos = [0, 0.3, 0.7]
alphas_ant = [0.4, 0.8, 1]
betas_ant = [0.4, 0.8, 1]
chosen_ant_percents = [0.02, 0.1, 0.2]

alphas_pso = [0.4, 0.8, 1]
betas_pso = [0.4, 0.8, 1]
gammas_pso = [0.3, 0.7]

counter = 0
for i, file in enumerate(files):
    result_filename = f"res_{file}_{'_'.join(algorithms)}.txt"
    create_file(result_filename)
    for exp_seed in seeds:
        print("seed ", exp_seed)
        for max_iterations in max_iterations:
            for ant_count in ant_counts:
                print("ant_count", ant_count)
                for alpha_ant in alphas_ant:
                    for beta_ant in betas_ant:
                        for rho in rhos:
                            Test("E-n22-k4.txt", max_iterations=max_iterations, ant_count=ant_count,
                                 chosen_ants_count=10, alpha=0.55, beta=0 / 85,
                                 gamma=0.5, rho=rho, exp_seed=exp_seed, alpha_ant=alpha_ant, beta_ant=beta_ant).run(
                                path=result_filename, algorithms=algorithms)
                            counter += 1
                            print(f"Iteration: {counter}")

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
