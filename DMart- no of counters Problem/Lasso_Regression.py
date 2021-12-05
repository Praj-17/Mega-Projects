import pandas as pd
data = pd.read_csv("dmart_processed.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1:]
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso=Lasso()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,0.2, 0.11,0.19, 0.1,0.25,0.3,0.32,0.35,0.35,0.359,0.36,0.38,0,4, 0.5,0.8,1,5,10,20,30,35,40,45,50,55,100,150]}
model_3=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)
model_3.fit(X,Y)
