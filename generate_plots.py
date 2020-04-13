import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
# money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

# ALG_NAME,ANT_COUNT,MAX_IT,SEED,ALPHA_ANT,BETA_ANT,RHO,CHOSEN_ANTS,ALPHA_PSO,BETA_PSO,GAMMA,SCORE
#
# elitist,200,50,6666,10,4,0,,,,,413.05
# elitist,200,50,7777,10,4,0,,,,,413.91
# elitist,200,50,8888,10,4,0,,,,,383.84

elitist = [413.05, 413.91, 383.84]
elitist_average = sum(elitist) / len(elitist)

#
# pso,200,50,6666,,,,,0.55,0.55,0,481.93
# pso,200,50,6666,,,,,0.55,0.55,0.5,496.67
# pso,200,50,6666,,,,,0.55,0.55,1,605.97
# pso,200,50,6666,,,,,0.55,0.85,0,503.56
# pso,200,50,6666,,,,,0.55,0.85,0.5,478.43
# pso,200,50,6666,,,,,0.55,0.85,1,582.24
# pso,200,50,6666,,,,,0.85,0.55,0,481.93
# pso,200,50,6666,,,,,0.85,0.55,0.5,467.68
# pso,200,50,6666,,,,,0.85,0.55,1,605.97
# pso,200,50,6666,,,,,0.85,0.85,0,497.76
# pso,200,50,6666,,,,,0.85,0.85,0.5,475.27
# pso,200,50,6666,,,,,0.85,0.85,1,544.82
# pso,200,50,7777,,,,,0.55,0.55,0,491.8
# pso,200,50,7777,,,,,0.55,0.55,0.5,441.55
# pso,200,50,7777,,,,,0.55,0.55,1,537.61
# pso,200,50,7777,,,,,0.55,0.85,0,536.88
# pso,200,50,7777,,,,,0.55,0.85,0.5,471.85
# pso,200,50,7777,,,,,0.55,0.85,1,541.84
# pso,200,50,7777,,,,,0.85,0.55,0,491.8
# pso,200,50,7777,,,,,0.85,0.55,0.5,450.26
# pso,200,50,7777,,,,,0.85,0.55,1,537.61
# pso,200,50,7777,,,,,0.85,0.85,0,536.88
# pso,200,50,7777,,,,,0.85,0.85,0.5,460.13
# pso,200,50,7777,,,,,0.85,0.85,1,514.71
# pso,200,50,8888,,,,,0.55,0.55,0,539.33
# pso,200,50,8888,,,,,0.55,0.55,0.5,457.68
# pso,200,50,8888,,,,,0.55,0.55,1,577.93
# pso,200,50,8888,,,,,0.55,0.85,0,509.66
# pso,200,50,8888,,,,,0.55,0.85,0.5,520.49
# pso,200,50,8888,,,,,0.55,0.85,1,538.07
# pso,200,50,8888,,,,,0.85,0.55,0,542.94
# pso,200,50,8888,,,,,0.85,0.55,0.5,437.83
# pso,200,50,8888,,,,,0.85,0.55,1,592.52
# pso,200,50,8888,,,,,0.85,0.85,0,511.69
# pso,200,50,8888,,,,,0.85,0.85,0.5,542.4
# pso,200,50,8888,,,,,0.85,0.85,1,586.66

pso = [467.68, 450.26, 437.83]
pso_average = sum(pso) / len(pso)

#
# greedy,,,,,,,,,,,589.42
greedy_average = 589.42
#
# random,,,6666,,,,,,,,857.7
# random,,,7777,,,,,,,,816.14
# random,,,8888,,,,,,,,962.33

random = [857.7, 816.14, 962.33]
random_average = sum(random) / len(random)

#
# standard,200,50,6666,10,4,0,,,,,393.18
# standard,200,50,7777,10,4,0,,,,,413.91
# standard,200,50,8888,10,4,0,,,,,383.84
#

standard = [393.18, 413.91, 383.84]
standard_average = sum(standard) / len(standard)

# rank,200,50,6666,10,4,0,4,,,,383.84
# rank,200,50,6666,10,4,0,20,,,,383.84
# rank,200,50,6666,10,4,0,40,,,,396.12
# rank,200,50,7777,10,4,0,4,,,,383.84
# rank,200,50,7777,10,4,0,20,,,,383.84
# rank,200,50,7777,10,4,0,40,,,,417.69
# rank,200,50,8888,10,4,0,4,,,,383.84
# rank,200,50,8888,10,4,0,20,,,,383.84
# rank,200,50,8888,10,4,0,40,,,,387.28

rank_average = 383.84

threshold = 375

scores = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
scores = list(map(lambda _x: round(_x), scores))
print(scores)
fig, ax = plt.subplots()
plt.bar(x, scores)
# for i, v in enumerate(scores):
#     ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')


labels = ('greedy', 'standard', 'elitist', 'rank', 'pso', 'random')
plt.xticks(x, labels)
# ax.plot([-0.5, 5.5], [threshold, threshold], 'k')
for i, v in enumerate(scores):
    ax.text(i - .25,
            v / scores[i] + 100,
            scores[i],
            fontsize=17,
            )

plt.axhline(y=threshold, linewidth=1, color='k')
plt.show()

fig.savefig("superfig.png")