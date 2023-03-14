import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from typing import List

sample_size = 50
old_labels = ['sample name' for i in range(sample_size)]

name_size = 5
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
names = [alphabet[i] for i in range(name_size)]
# names = [i for i in range(name_size)]

old_data = np.asarray([[(0.95 - i / sample_size - j / sample_size)
                        for j in range(name_size)] for i in range(sample_size)])

# TODO: function file
data = np.zeros([old_data.shape[0] + 2, old_data.shape[1]])
data[1:int(data.shape[0]/2)][:] = old_data[0:int(old_data.shape[0]/2)][:]
data[int(data.shape[0]/2)+1:][:] = old_data[int(old_data.shape[0]/2):][:]
data = pd.DataFrame(data)

labels: List = ['N']
labels += old_labels[:int(len(old_labels) / 2)]
labels.append('N')
labels += old_labels[int(len(old_labels) / 2):]

fig = plt.figure(1, figsize=(9, 9))
ax = plt.axes(polar=True)
num_row = data.shape[0]
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / num_row)
width = np.pi / (num_row/2)

my_cmap_rgb = plt.get_cmap('jet')(np.arange(256))
alpha = 0.5

# https://stackoverflow.com/questions/15003353/why-does-my-colorbar-have-lines-in-it
# Do not include the last column!
for i in range(3):
    my_cmap_rgb[:, i] = (1 - alpha) + alpha*my_cmap_rgb[:, i]
my_cmap = mpl.colors.ListedColormap(my_cmap_rgb, name='my_cmap')

# cmap = plt.cm.get_cmap('jet')
for idx in range(data.shape[1]):
    inner_radii = 2 * data.shape[1] - idx
    bars = plt.bar(theta, 1, width=width, bottom=inner_radii)
    for jdx, bar in enumerate(bars):
        if jdx != 0 and jdx != int(data.shape[0] / 2):
            bar.set_facecolor(my_cmap(data[idx][jdx]))
        else:  # jdx == 0 or jdx == int(50 / 2)
            bar.set_facecolor('white')
            # bar.set_alpha(0.5)
            plt.text(theta[jdx], inner_radii + 0.5, names[idx],
                     size=12.5, horizontalalignment='center', verticalalignment='center')

radius = 2.4 * data.shape[1]
for idx in range(data.shape[0]):
    if idx != 0 and idx != int(data.shape[0] / 2):
        if theta[idx] < (np.pi / 2) or theta[idx] > (np.pi * 3 / 2):
            rotation_angle = theta[idx] * 180 / np.pi
            horizontal_str = 'right'
            # horizontal_str = 'left'
        else:
            rotation_angle = theta[idx] * 180 / np.pi + 180
            horizontal_str = 'left'
            # horizontal_str = 'right'

        plt.text(theta[idx], radius, labels[idx],
                 size=12.5, rotation_mode='anchor', rotation=rotation_angle,
                 horizontalalignment=horizontal_str, verticalalignment='center')
    else:  # jdx == 0 or jdx == int(50 / 2)
        continue


ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(False)
ax.spines['polar'].set_visible(False)

fig, ax = plt.subplots(figsize=(9, 1))
fig.subplots_adjust(bottom=0.5)

norm = mpl.colors.Normalize(vmin=0, vmax=1)
colorbar_handle = mpl.colorbar.ColorbarBase(ax, cmap=my_cmap, norm=norm, orientation='horizontal')

plt.show()