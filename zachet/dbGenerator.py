import sqlite3
import pandas as pd

class Generator():
    def __init__(self):
        tables = pd.read_csv("Export.csv",delimiter=',')

        con = sqlite3.connect("farm.db")

        farmMain = tables[['FMID','MarketName','Website','street','city','County','State','zip']]
        coords = tables[['FMID','x','y','Location']]
        market = tables[['FMID', 'Organic',
                            'Bakedgoods', 'Cheese','Crafts','Flowers','Eggs',
                            'Seafood','Herbs','Vegetables','Honey','Jams',
                            'Maple','Meat','Nursery','Nuts','Plants','Poultry',
                            'Prepared', 'Soap' ,'Trees','Coffee','Beans','Fruits',
                            'Grains','Juices','Mushrooms','PetFood' ,'Tofu','WildHarvested']]
        cur = con.cursor()

        cur.execute("CREATE TABLE if not Exists Farms (FMID text , MarketName text, Website text, street text, city text, County text,State text, zip INT );")
        farmMain.to_sql('Farms',con,if_exists='replace',index=False)
        con.commit()

        cur.execute("CREATE TABLE if not Exists Coords (FMID text , x text, y text, Location text);")
        coords.to_sql('Coords',con,if_exists='replace',index=False)
        con.commit()

        cur.execute("CREATE TABLE if not Exists Products (FMID text, Organic text, "
                    "Bakedgoods text, Cheese text,Crafts text,Flowers text,Eggs text,"
                    "Seafood text,Herbs text,Vegetables text,Honey text,Jams text,"
                    "Maple text,Meat text,Nursery text,Nuts text,Plants text,Poultry text,"
                    "Prepared text, Soap text,Trees text,Coffee text,Beans text,Fruits text,"
                    "Grains text,Juices text,Mushrooms text,PetFood text,Tofu text,WildHarvested);")
        market.to_sql('Products',con,if_exists='replace',index=False)
        con.commit()

        cur.execute("CREATE TABLE if not Exists Reviews(FMID text,FirstName text,LastName text, Comment text, rate int );")


        con.close()


