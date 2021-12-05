import pandas as pd
data = pd.read_csv("dmart_processed.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1:]
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

import numpy as np
model = LinearRegression()
mse = cross_val_score(model,X,Y,scoring='neg_mean_squared_error',cv=5)
model.fit(X,Y)
mean_mse = np.mean(mse)
