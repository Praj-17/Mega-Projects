import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
data = pd.read_csv("dmart_processed.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1:]
ridge = Ridge()

parameters={'alpha':[1e-40,1e-30,1e-20,1e-50,1e-60,1e-51,1e-149,1e-310,1e-320,1e-321,1e-322,1e-323,1e-50,1e-20,1e-15,1e-10,1e-8,1e-3,1e-2,5,10,20,30,35,40,45,50]}
model_2 = GridSearchCV(ridge,parameters,
                       scoring='neg_mean_squared_error',cv=5)
model_2.fit(X,Y)