import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
data = pd.read_excel('../dataset/TrainExer13.xls')
print (data.head())
W = data['Winning time men']
G = np.array(data['Game']).reshape((-1, 1))
model = LinearRegression()
model.fit(G, W)
r_sq = model.score(G, W)
print('intercept a:', model.intercept_)
print('slope b:', model.coef_)
print('coefficient of determination r_sq:', r_sq)
print ('s:', np.sqrt(np.sum(np.square(np.subtract(W, model.predict(G))))/(len(G)-2)) )
# print ('s:', np.sqrt(np.sum(np.subtract(W, model.predict(G)))/(n-2)))
y_pred = model.predict(np.array([16, 17, 18]).reshape((-1, 1)))
print('predicted response:', y_pred, sep='\n')