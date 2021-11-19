import pandas as pd
from pandas.io import sql
import pymysql 
import config

def mysql_connect():    # Mysql connection function

    global connection

    # Mysql crdentials to connect the database
    connection = pymysql.connect(                  
        host="127.0.0.1",
        user=config.db_user,
        password=config.db_pass,
        db=config.db_name,
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