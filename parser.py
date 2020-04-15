import os
from os import walk

dir_path = os.path.dirname(os.path.realpath(__file__))
f = []
for (dirpath, dirnames, filenames) in walk(dir_path):
    f.extend(filenames)
    break

f = list(filter(lambda x: x[:3] == 'res' and x[-4:] == '.txt', f))

n51s = []
n76s = []
n101s = []

for file in f:
    if file[10:12] == '51':
        n51s.append(file)
    elif file[10:12] == '76':
        n76s.append(file)
    elif file[10:13] == '101':
        n101s.append(file)

with open(f[0], 'r') as file:
    column_names = list(map(str.strip, file.readline()))

files_all = [['n51all.txt', n51s], ['n76all.txt', n76s], ['n101all.txt', n101s]]

for file_all in files_all:
    open(file_all[0], 'w').close()
    with open(file_all[0], 'a') as nfile:
        for file in file_all[1]:
            with open(file, 'r') as _file:
                content = _file.readlines()
            nfile.write(''.join(content[1:]))

n51s = []
n76s = []
n101s = []

new_lists = [n51s, n76s, n101s]

names = ['alg', 'ant_count', 'its', 'seed', 'a_ant', 'b_ant', 'r', 'ch_ants',
         'a_pso', 'b_pso', 'g', 'score', 'time', 'best_it']

for i, file_all in enumerate(files_all):
    with open(file_all[0], 'r') as nfile:
        content = list(map(str.strip, nfile.readlines()))
    for line in content:
        values = line.split(',')
        dic = {}
        for j, value in enumerate(values):
            dic[names[j]] = value
        new_lists[i].append(dic)

# for a in n51s:
#     print(a)

its = [50, 100, 150, 200]
algs = ['standard', 'elitist', 'rank', 'pso', 'greedy', 'random']
seeds = [6666, 7777, 8888, 9213]


# usredniamy: score, time, best_it

def make_average_for_graph(graph):
    data = None
    if graph == '51':
        data = n51s
    elif graph == '76':
        data = n76s
    elif graph == '101':
        data = n101s
    for alg in algs:
        for it in its:
            filename = f"av_n{graph}_{alg}_{it}.txt"
            av_score = 0
            av_time = 0
            av_best_it = 0
            if alg != 'greedy' and alg != 'random':
                rows = list(filter(lambda x: x['its'] == str(it) and x['alg'] == str(alg), data))
            else:
                rows = list(filter(lambda x: x['alg'] == str(alg), data))
            if not rows:
                continue
            if alg != 'greedy':
                for i in range(len(seeds)):
                    av_score += float(rows[i]['score'])
                    av_time += float(rows[i]['time'])
                    av_best_it += int(rows[i]['best_it'])
                av_score /= len(seeds)
                av_time /= len(seeds)
                av_best_it //= len(seeds)
            else:
                av_score = float(rows[0]['score'])
                av_time = float(rows[0]['time'])
                av_best_it = int(rows[0]['best_it'])
            with open(filename, 'w') as file:
                file.write(f"{av_score},{av_time},{av_best_it}")


make_average_for_graph('51')
make_average_for_graph('76')
make_average_for_graph('101')
