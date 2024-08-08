import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

plt.clf()
data.plot(kind="box", subplots=True, figsize=(12, 10), layout=(3, 3), sharex=False, sharey=False)
plt.savefig("./results/boxplot.png")