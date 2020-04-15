import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np


def make_chart(avs, thr, n, chartname):
    labels = ['greedy', 'standard', 'elitist', 'rank', 'pso', 'random']
    if not avs[5]:
        labels.remove('random')
        avs.pop(5)
    if not avs[4]:
        labels.remove('pso')
        avs.pop(4)
    if not avs[3]:
        labels.remove('rank')
        avs.pop(3)
    if not avs[2]:
        labels.remove('elitist')
        avs.pop(2)
    if not avs[1]:
        labels.remove('standard')
        avs.pop(1)
    if not avs[0]:
        labels.remove('greedy')
        avs.pop(0)
    x = np.arange(len(avs))
    labels = tuple(labels)
    avs = list(map(lambda _x: round(_x), avs))
    fig, ax = plt.subplots()
    bar_plot = plt.bar(x, avs, tick_label=avs)

    for idx, rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                avs[idx],
                ha='center', va='bottom', rotation=0)

    plt.xticks(x, labels)
    plt.axhline(y=thr, linewidth=1, color='r')
    # plt.axhline(y=thr_r, linewidth=1, color='k', linestyle='--')

    trans = transforms.blended_transform_factory(
        ax.get_yticklabels()[0].get_transform(), ax.transData)
    ax.text(0, thr, "{:.0f}".format(thr), color="red", transform=trans,
            ha="right", va="center")

    plt.title(n)
    # plt.show()
    # fig.savefig(f"{chartname}.png")
    return plt


def make_subplots(*args):
    pass


# elitist_average =
# pso_average =
# greedy_average =
# random_average =
# standard_average =
# rank_average =
# averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
# plt = make_chart(averages, threshold, 'n', 'H_n')

threshold51 = 521
threshold76 = 735
threshold101 = 1077

threshold_round51 = 547
threshold_round76 = 772
threshold_round101 = 1130

# ============== H1 (50)
# ===== n51
elitist_average = 629.405
pso_average = 1048.8225
greedy_average = 711.5
random_average = 1759.8025
standard_average = 622.3425
rank_average = 612.4725000000001
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt1 = make_chart(averages, threshold51, 'n51', 'H1_n51')
# plt1.show()

# ===== n76
elitist_average = 982.28
pso_average = 1630.3249999999998
greedy_average = 1149.41
random_average = 2553.8775000000005
standard_average = 985.1675
rank_average = 895.295
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt2 = make_chart(averages, threshold76, 'n76', 'H1_n76')
# plt2.show()

# === n101
elitist_average = 1471.905
pso_average = 2575.815
greedy_average = 1610.91
random_average = 3605.4575
standard_average = 1477.9399999999998
rank_average = 1353.2325
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt3 = make_chart(averages, threshold101, 'n101', 'H1_n101')
# plt3.show()

# ============ H2 (200)
# === n51
elitist_average = 616.705
pso_average = 1048.295
standard_average = 615.9625000000001
rank_average = 612.4725000000001
averages = [None, standard_average, elitist_average, rank_average, pso_average, None]
plt1 = make_chart(averages, threshold51, 'n51', 'H2_n51')
# plt1.show()

# === n76
elitist_average = 938.875
pso_average = 1630.3249999999998
standard_average = 941.8225
rank_average = 888.875
averages = [None, standard_average, elitist_average, rank_average, pso_average, None]
plt2 = make_chart(averages, threshold76, 'n76', 'H2_n76')
# plt2.show()

# === n101
elitist_average = 1431.9475
pso_average = 2575.815
standard_average = 1428.4875
rank_average = 1344.1599999999999
averages = [None, standard_average, elitist_average, rank_average, pso_average, None]
plt3 = make_chart(averages, threshold101, 'n76', 'H2_n76')
# plt3.show()

# =========== H3
# ===== n51
elitist_average = 616.2725
pso_average = 1048.295
greedy_average = 711.5
random_average = 1759.8025
standard_average = 615.9625000000001
rank_average = 612.4725000000001
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt1 = make_chart(averages, threshold51, 'n51', 'H3_n51')
# plt1.show()

# ===== n76
elitist_average = 962.3299999999999
pso_average = 1630.3249999999998
greedy_average = 1149.41
random_average = 2553.8775000000005
standard_average = 961.9525000000001
rank_average = 893.4825
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt2 = make_chart(averages, threshold76, 'n76', 'H3_n76')
# plt2.show()

# === n101
elitist_average = 1450.025
pso_average = 2575.815
greedy_average = 1610.91
random_average = 3605.4575
standard_average = 1454.2949999999998
rank_average = 1353.2325
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt3 = make_chart(averages, threshold101, 'n101', 'H3_n101')
# plt3.show()

# ========= H4
# ===== n51
elitist_average = 614.1875
pso_average = 1048.295
greedy_average = 711.5
random_average = 1759.8025
standard_average = 615.9625000000001
rank_average = 612.4725000000001
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt1 = make_chart(averages, threshold51, 'n51', 'H4_n51')
# plt1.show()

# ===== n76
elitist_average = 961.885
pso_average = 1630.3249999999998
greedy_average = 1149.41
random_average = 2553.8775000000005
standard_average = 956.5274999999999
rank_average = 888.875
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt2 = make_chart(averages, threshold76, 'n76', 'H4_n76')
# plt2.show()

# === n101
elitist_average = 1445.7775000000001
pso_average = 2575.815
greedy_average = 1610.91
random_average = 3605.4575
standard_average = 1447.135
rank_average = 1348.79
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt3 = make_chart(averages, threshold101, 'n101', 'H4_n101')
# plt3.show()

# ======= H5
# ===== n51
elitist_average = 614.1875
pso_average = 1048.295
greedy_average = 711.5
random_average = 1759.8025
standard_average = 615.9625000000001
rank_average = 612.4725000000001
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt1 = make_chart(averages, threshold51, 'n51', 'H5_n51')
# plt1.show()

# ===== n76
elitist_average = 961.885
pso_average = 1630.3249999999998
greedy_average = 1149.41
random_average = 2553.8775000000005
standard_average = 956.5274999999999
rank_average = 888.875
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt2 = make_chart(averages, threshold76, 'n76', 'H5_n76')
# plt2.show()

# === n101
elitist_average = 1445.7775000000001
pso_average = 2575.815
greedy_average = 1610.91
random_average = 3605.4575
standard_average = 1447.135
rank_average = 1348.79
averages = [greedy_average, standard_average, elitist_average, rank_average, pso_average, random_average]
plt3 = make_chart(averages, threshold101, 'n101', 'H5_n101')
# plt3.show()