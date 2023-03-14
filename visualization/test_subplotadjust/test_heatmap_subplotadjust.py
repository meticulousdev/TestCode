# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from typing import List, Tuple, Dict, Set

import random

random.seed(42)

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({'mathtext.default':  'default'})
plt.rcParams.update({'font.size': 16})

# %%
data_columns = ['col01', 'col02', 'col03', 'col04']
data_indexs = ['long index' + str(i) for i in range(15)]

data_example = pd.DataFrame([[random.random(), random.random(), random.random(), random.random()] for _ in range(15)], 
                            index=data_indexs, 
                            columns=data_columns)

# %%
sns.heatmap(data_example, cmap='jet', vmin=0, vmax=1)
plt.subplots_adjust(left=0.24)
plt.savefig("./heatmap.png")
