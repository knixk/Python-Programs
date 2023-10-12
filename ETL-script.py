# Kanishk Shrivastava
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime 
from sqlalchemy import create_engine

# Make connection - you need to have your own credentials.
database = "demo"
host = "localhost"
username = "root"
password = ""

# Create the connection object   
# engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
# connection = engine.raw_connection()

#printing the connection object   
# print(connection)  

#creating the cursor object  
# cur = connection.cursor()

# try:  
#     myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")  
#     cur = myconn.cursor()  

# except:  
#     print("Error connecting to database, check credentials.")


file_name = 'Updated_sales_data.csv'

def connectingToDB():
    try:
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
        connection = engine.raw_connection()
        cur = connection.cursor()

    except:
        # print("Error connecting to DB, check credentials or server status..")
        raise Exception("Couldn't connect to DB, check credentials or server status..")

    return engine, connection, cur

def extract():
    df = pd.read_csv(file_name)
    return df


def transform(df):
    # Finding any null values
    # df.isnull().sum()

    # Removing the null values
    cleaned = df.dropna().reset_index()

    # There were duplicates columns names inside the rows, removing them.

    # 1. create a Boolean mask for the rows to remove
    mask = cleaned['Price Each'] == 'Price Each'

    # 2. select all rows except the ones that contain column names
    cleaned = cleaned[~mask]

    # 3. print the resulting DataFrame
    # print(cleaned)

    # Calculating total sales
    cleaned['Quantity Ordered'] = cleaned['Quantity Ordered'].astype(int)
    cleaned['Price Each'] = cleaned['Price Each'].astype(float)
    cleaned['Order ID'] = cleaned['Order ID'].astype(int)
    
    cleaned['total_sales'] = cleaned['Quantity Ordered'] * cleaned['Price Each']

    # removing duplicated indexes
    cleaned.drop(columns=cleaned.columns[0], axis=1, inplace=True)

    # type casting date column from object to datetime
    dates = pd.to_datetime(cleaned['Order Date'], format="mixed")
    cleaned['Order Date'] = dates

    # creating columns for month and year
    cleaned['Month'] = dates.dt.month
    cleaned['Year'] = dates.dt.year

    monthly_sales = cleaned.groupby(['Product', 'Year', 'Month'])['total_sales'].sum().reset_index()
    total_sales_by_product = pd.DataFrame(monthly_sales)
    return cleaned, total_sales_by_product



def createSchema(connection, cur):

    try:  

        #Dropping tables if already exist.
        cur.execute("DROP TABLE IF EXISTS products")
        cur.execute("DROP TABLE IF EXISTS orders")

        # use_db = '''USE demo'''
        use_db = f'''USE {database};'''

        #Creating table as per requirement
        create_table_orders ='''
            CREATE TABLE `orders` (
            `Order ID` INT NOT NULL PRIMARY KEY,
            `Product` TEXT(256) NOT NULL,
            `Quantity Ordered` INT NOT NULL,
            `Price Each` FLOAT NOT NULL,
            `Order Date` DATETIME NOT NULL,
            `Purchase Address` TEXT NOT NULL,
            `total_sales` FLOAT,
            `Month` INT,
            `Year` INT
        );
        '''

        create_table_products = '''
            CREATE TABLE `products` (
            `Product` TEXT(256) NOT NULL,
            `Year` INT,
            `Month` INT,
            `total_sales` FLOAT
        );
        '''

        cur.execute(use_db)
        cur.execute(create_table_orders)
        cur.execute(create_table_products)

        # query = "use demo;"
        dbs = cur.execute("show databases")  

        connection.commit()

    except:  
        connection.rollback()  
        print("Error with DB")
        
    print("Available databases")
    for x in cur:  
        print(x)  

def insertIntoTable(df, table_name, idx, engine):
    # inserting value in table from csv with a dataframe
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=idx)
    except:
        print(f"Couldn't load data into {table_name} table..")
    finally:
        print(f"Successfully loaded data into the {table_name} table.")


def load(cleaned, total_sales_by_product):

    engine, connection, cur = connectingToDB()

    # creating schema
    # try:
    #     engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
    # except:
    #     print("Error connecting to DB, check credentials or server status..")
    createSchema(connection, cur)
    insertIntoTable(cleaned, "orders", False, engine)
    insertIntoTable(total_sales_by_product, "products", False, engine)

    # saving the final files in the same working directory
    cleaned.to_csv('cleaned_data.csv')
    total_sales_by_product.to_csv('products_sale_by_month.csv')

    # Closing the connection
    cur.close()
    connection.close()


# ------------------------x--------------------------x------------------------x---------------------
# ETL Pipeline

# 1. extract
df = extract()

# 2. transform
cleaned, total_sales_by_product = transform(df)

# 3. load
load(cleaned, total_sales_by_product)

