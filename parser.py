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

names = ['alg', 'ant_count', 'its', 'seed', 'a_ant', 'n_ant', 'r', 'ch_ants',
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

