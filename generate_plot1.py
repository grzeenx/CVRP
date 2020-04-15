import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


def make_chart(avs, thr, n, chartname):
    x = np.arange(6)
    avs = list(map(lambda _x: round(_x), avs))
    fig, ax = plt.subplots()
    bar_plot = plt.bar(x, avs, tick_label=avs)

    for idx, rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                avs[idx],
                ha='center', va='bottom', rotation=0)

    labels = ('greedy', 'standard', 'elitist', 'rank', 'pso', 'random')
    plt.xticks(x, labels)
    plt.axhline(y=thr, linewidth=1, color='r')
    # plt.axhline(y=thr_r, linewidth=1, color='k', linestyle='--')

    trans = transforms.blended_transform_factory(
        ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(0, thr, "{:.0f}".format(thr), color="red", transform=trans,
            ha="right", va="center")


    plt.title(n)
    plt.show()
    fig.savefig(f"{chartname}.png")


# ============== H1 (50), n51
elitist_average = 2517.62
pso_average = 3213.4
greedy_average = 711.5
random_average = 7039.21
standard_average = 2489.37
rank_average = 2449.8900000000003
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
threshold = 521
threshold_round = 547
make_chart(averages, threshold, 'n51', 'H1_n51')
