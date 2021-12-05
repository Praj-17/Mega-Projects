
from Linear_Regression import mean_mse
from Ridge_Regression import model_2
from Lasso_Regression import model_3

import pandas as pd
import numpy as np
loss ={"Linear": mean_mse, "Ridge":model_2.best_score_, "Lasso":model_3.best_score_ }
print(loss)

data = pd.read_csv("dmart_processed.csv")
X = data.iloc[:,:-1]
Y = data.iloc[:,-1:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= 0.3)

prediction_ridge  = model_2.predict(x_test)


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
Regions = {1:"Western", 2: "Eastern ",3: "Norhtern",4: "Southern" }
str1 = """Pune Mumbai Nashik Nagpur Aurangabad Panaji Ahmedabad Surat Gandhinagar Vadodara Bangalore Mysore Chennai Madurai Ooty Hyderabad Coimbatore Puducherry Kochi Thiruvananthpu NewDelhi Shimla Chandigarh Dehradun Jammu Agra Kanpur Ghaziabad Jaipur Kolkata Patna Darjeeling Ranchi Bhubaneshwar Howrah Puri Kharagpur Durgapur2 jamshedpur """
number = list(np.arange(39))
city = [i for i in ((str1).split())]

str2 = "5,6,3,2,1,5,5,3,5,4,6,5,5,4,3,6,2,4,4,5,6,4,3,2,2,1,3,2,2,3,1,5,5,3,2,3,2,1,1,2,2,2,"
outlet =[i for i in ((str2).split(','))]
outlets = dict(zip(city,outlet ))
Cities = dict(zip(number, city))
western_cities = {0: 'Pune', 1: 'Mumbai', 2: 'Nashik', 3: 'Nagpur', 4: 'Aurangabad', 5: 'Panaji', 6: 'Ahmedabad', 7: 'Surat', 8: 'Gandhinagar', 9: 'Vadodara'}

print(Cities)
print("\n______Welcome to the counter counting problem_______\n")
print("________________Region___________")
print("Please input the region")
print("""Western - 0\nEastern - 1\nNorhtern- 2\nSouthern- 3""")
r =int(input("input: "))
print("___________city___________")
print(Cities)
print("Please select a city")
c = int(input("input: "))
print("__________Month__________")
print("Please provide the number of month in which you want to employe the employee")
m  = int(input())
print("_________Thankyou for your input_______")
print("____Please wait while we compute your output___")

final_city = Cities[c]
final_outlet = outlets[final_city]

x_list = [r, m, int(final_outlet), mean_sales, mean_profits,c]
x_list = np.array(x_list)
x_list.resize(1,6)

prediction_ridge  = model_2.predict(x_list)

print("\n_________The predicted value is______\n")
print(f"\n______{int(prediction_ridge)}_______\n")
