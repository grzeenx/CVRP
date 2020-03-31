from test_class import Test

test1 = Test("E-n22-k4.txt", max_iterations=50, ant_count=75, chosen_ants_count=10, alpha=0.55, beta=0.85, gamma=0.5,
             rho=0, exp_seed=100, alpha_ant=1, beta_ant=1)
# test2 = Test("E-n22-k4.txt", max_iterations=100, ant_count=150, chosen_ants_count=10, alpha=0.55, beta=0.85, gamma=0.5,
#              rho=0, exp_seed=100, alpha_ant=1, beta_ant=1)

test1.run()
