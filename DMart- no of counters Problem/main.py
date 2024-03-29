
from Linear_Regression import mean_mse,model
from Ridge_Regression import model_2
from Lasso_Regression import model_3


import pandas as pd
import numpy as np
#Perfomance metircs

print("\n______________mean_squared_errors______________\n")
loss ={"Linear": mean_mse, "Ridge":model_2.best_score_, "Lasso":model_3.best_score_ }
print(loss)

data = pd.read_csv("dmart_processed.csv")
X = data.iloc[:,:-1] #Independatant variables arrays
Y = data.iloc[:,-1:] #Dependant Variable #arrays



#Dicing dataset into 2 parts train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= 0.2)

#Koi ek type puri tarajh se train me na chalajaye
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size= 0.2, random_state =42)
for train_index, test_index in split.split(X, X['Region']):
    x_train = X.loc[train_index]
    x_test = X.loc[test_index]
    
prediction_ridge  = model_2.predict(x_test) #arrays (96,1)
prediction_lasso  = model_3.predict(x_test) #arrays(96,1)
prediction_linear = model.predict (x_test)  #arrays(96,)
prediction_lasso.resize(96,1)


from sklearn.metrics import r2_score
"""
What is R2 score???
r2 score is a better way to define the correctnees of a regression model,
It is read as "R square score"
Let us understand ot mathematically,

R^2 = 1 - SSresidual/SSmean
where ,
SSresidual  = sum((y-y')^2)/n
SSmean = sum((y-mean(y))^2)/n
y = actual value, y' = predicted value, n=  number of records

there for the formula becomes
R^2 = 1 - (sum((y-y')^2))/sum((y-mean(y))^2)
Now, since SSmean is always greater than SSresidual , the value of the term,

0 <= SSresidual/SSmean >= 1
lies between 0 and 1 and hence after substracting it by one we get the actual r^2 

Hence the smalled the value of SSresidual/SSmean the greater the value of R^2 , 

The best model has R^2 closer to 1 and adn worst model has R^2 closer to 0
"""
linear_score = r2_score(y_test, prediction_linear)
Ridge_score = r2_score (y_test, prediction_ridge)
lasso_score = r2_score (y_test, prediction_lasso)

# Now we are tyring to predict even better by taking the avg of the all 3 predictions
"""
By averaging over all the models, we can even out the overestimation and underestimation. ... So, if we can form a lot of models and take the average over them, we can expect that the resulting prediction is more robust than the individual prediction.

"""


r2_scores ={"Linear": linear_score, "Ridge":Ridge_score, "Lasso":lasso_score}
print("\n______________R2_Scores______________\n")
print(r2_scores)
# y_test = np.array(y_test)
# prediction_lasso.resize(144,1)

sales = data['Sales in thousands']
profits = data['Profit in thousands']
mean_sales = sales.mean()
mean_profits = profits.mean()

## Program to generate output from custome input
"""
User will have to give input of 3 parameters 
1. Region - Western - 0 ,Eastern - 1, Norhtern- 2,Southern -3
2. Month - month number for eg..1 for jan, 2 for feb
3. City - the city in which the mall is
  """
Regions = {0:"Western",  1: "Eastern ",2: "Norhtern",3: "Southern" }
str1 = """Pune Mumbai Nashik Nagpur Aurangabad Panaji Ahmedabad Surat Gandhinagar Vadodara Bangalore Mysore Chennai Madurai Ooty Hyderabad Coimbatore Puducherry Kochi Thiruvananthpu NewDelhi Shimla Chandigarh Dehradun Jammu Agra Kanpur Ghaziabad Jaipur Kolkata Patna Darjeeling Ranchi Bhubaneshwar Howrah Puri Kharagpur Durgapur2 jamshedpur """
number = list(np.arange(39)) #array
city = [i for i in ((str1).split())] #python list

str2 = "5,6,3,2,1,5,5,3,5,4,6,5,5,4,3,6,2,4,4,5,6,4,3,2,2,1,3,2,2,3,1,5,5,3,2,3,2,1,1,2,2,2,"
outlet =[i for i in ((str2).split(','))] #python list
outlets = dict(zip(city,outlet )) #python dictioniaries
Cities = dict(zip(number, city))  #python dictioniaries

western_cities = {0: 'Pune', 
                  1: 'Mumbai', 
                  2: 'Nashik', 
                  3: 'Nagpur', 
                  4: 'Aurangabad', 
                  5: 'Panaji', 
                  6: 'Ahmedabad', 
                  7: 'Surat', 
                  8: 'Gandhinagar', 
                  9: 'Vadodara'}

Eastern_cities = {0: 'Patna',
                  1: 'Darjeeling',
                  2: 'Ranchi',
                  3: 'Bhubaneshwar',
                  4: 'Howrah',
                  5: 'Puri',
                  6: 'Kharagpur',
                  7: 'Durgapur2',
                  8: 'jamshedpur'}

Northern_cities = {0: 'NewDelhi',
                   1: 'Shimla',
                   2: 'Chandigarh',
                   3: 'Dehradun',
                   4: 'Jammu',
                   5: 'Agra',
                   6: 'Kanpur',
                   7: 'Ghaziabad',
                   8: 'Jaipur',
                   9: 'Kolkata'}

Southern_cities = {0: 'Bangalore',
                   1: 'Mysore',
                   2: 'Chennai',
                   3: 'Madurai',
                   4: 'Ooty',
                   5: 'Hyderabad',
                   6: 'Coimbatore',
                   7: 'Puducherry',
                   8: 'Kochi',
                   9: 'Thiruvananthpu'}

print("\n______Welcome to the counter counting problem_______\n")
print("________________Region___________")
print("Please input the region")

print("""
         0)Western
         1)Eastern 
         2)Norhtern 
         3)Southern""")

while True:
  r =int(input("input: "))

  print("___________city___________")
  if r == 0:
    print(western_cities)
    break
  elif r == 1:
    print(Eastern_cities)
    break
  elif r == 2:
    print(Northern_cities)
    break
  elif r == 3:
    print(Southern_cities)
    break
  else:
    print("Wrong Input")
while True:
  print("Please select a city")
  c = int(input("input: "))
  if r == 0 and c in range(10):
    break
  elif r == 1 and c in range(11,20):
    break
  elif r == 2 and c in range(21,30):
    break
  elif r == 3 and c in range(31,40):
    break
  else:
    print("No city in this particular region")
while True:
  print("__________Month__________")
  print("Please provide the number of month in which you want to employe the employee")
  m  = int(input())
  if m in range(1,12):
    break
  else:
    print("Please provide a valid month number")


print("_________Thankyou for your input_______")
print("____Please wait while we compute your output___")

final_city = Cities[c]
final_outlet = outlets[final_city]

x_list = [r, m, int(final_outlet), mean_sales, mean_profits,c]
x_list = np.array(x_list)
x_list.resize(1,6)


prediction_ridge  = model_2.predict(x_list)


# 0,5,5,622.36,124.472,0,24
# 0,6,5,548.86,109.772,0,22
# 0,8,5,490.15,98.03,0,21
print("\n_________The predicted value is______\n")
print(f"\n______{int(prediction_ridge)} Couters needed_______\n")
