import pandas as pd
from sklearn.preprocessing import MinMaxScaler

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

array = data.values
X = array[:, 0:8]
Y = array[:, 8]
print(X.shape, Y.shape)
