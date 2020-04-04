from test_class import Test
import csv

def create_file(path):
    with open(path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["it", "ant_count", "alpha_ant", "beta_ant", "greedy", "random", "standard", "rank", "elit", "pso"])


# standard
files =["E-n22-k4.txt"]
# "E-n51-k5.txt","E-n76-k10.txt","E-n101-k8.txt"]
paths=list(map( (lambda x :  "result_"+ x),files))
for i, file in enumerate(files):
    create_file("standard_"+paths[i])
    for exp_seed in [192123, 37701, 24041, 9819034501]:
        print("seed ", exp_seed)
        for max_iterations in [50]:
            for ant_count in [50, 100, 150, 200]:
                print("ant_count", ant_count)
                for alpha_ant in [0.4,0.55,1]:
                    for beta_ant in [0.4, 0.85, 1]:
                        for rho in [0, 0.3,0.7]:
                            Test("E-n22-k4.txt", max_iterations=max_iterations, ant_count=ant_count, chosen_ants_count=10, alpha=0.55, beta=0/85,
                                 gamma=0.5, rho=rho, exp_seed=exp_seed, alpha_ant=alpha_ant, beta_ant=beta_ant).run(path="standard_"+paths[i], algorithms=["standard_aco"])




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
