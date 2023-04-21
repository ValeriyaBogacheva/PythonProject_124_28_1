import sqlite3
import pandas as pd


def getTables(sql):
    with sqlite3.connect('farm.db') as connection:
        df = pd.read_sql_query(sql, connection)
    return df

def setTables(sql):
    with sqlite3.connect('farm.db') as connection:
        con = connection.cursor()
        con.execute(sql)
        con.close()
        print("SAVED")
