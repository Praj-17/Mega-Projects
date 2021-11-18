import pandas as pd
from pandas.io import sql
import pymysql 

db_user = "root"
db_pass = "password"
db_name = "mydb"
localhost = "127.0.0.1"

def mysql_connect():    # Mysql connection function

    global connection

    # Mysql crdentials to connect the database
    connection = pymysql.connect(                  
        host="127.0.0.1",
        user=db_user,
        password=db_pass,
        db=db_name,
    )

def run_query(sql):

    # sql: MySQL query
    # pd: Pandas dataframe containing results
    return pd.read_sql_query(sql, connection)

def mysql_disconnect():

    connection.close()

mysql_connect()

query = input("Enter_query: ")
df = run_query(query)
df.head()

print(df)

mysql_disconnect()