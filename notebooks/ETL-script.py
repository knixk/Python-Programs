# Kanishk Shrivastava
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine

# [IMPORTANT] Make connection - (You need to have your own credentials).
database = "demo"
host = "localhost"
username = "root"
password = ""

file_name = 'Updated_sales_data.csv'

print("ETL Pipleline..")

def connectingToDB():
    try:
        engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
        connection = engine.raw_connection()
        cur = connection.cursor()

    except:
        raise Exception("Couldn't connect to DB, check credentials or server status..")

    print("SQL connection successfull.")
        
    return engine, connection, cur

def extract():
    try:
        df = pd.read_csv(file_name)
    except: 
        raise Exception("Couldn't read csv, are you sure the path / file is valid?")
    
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
    try:
        cleaned['Quantity Ordered'] = cleaned['Quantity Ordered'].astype(int)
        cleaned['Price Each'] = cleaned['Price Each'].astype(float)
        cleaned['Order ID'] = cleaned['Order ID'].astype(int)
    except:
        raise Exception("Error changing the data types of the columns. It may happen that these datatypes are invalid.")

    try:
        cleaned['total_sales'] = cleaned['Quantity Ordered'] * cleaned['Price Each']
    except:
        raise Exception("The data types of 'Quantity Ordered' and 'Price Each' should be: int and float")


    try:
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

    except:
        raise Exception("Error performing transformations on the data..")

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

        dbs = cur.execute("show databases")  
        connection.commit()

    except:  
        connection.rollback()  
        raise Exception("Error creating DB Schema or DB doesn't exist..")
        
    print(f"Available databases:- {dbs}")

    for x in cur:  
        print(x)  

def insertIntoTable(df, table_name, idx, engine):
    # inserting value in table from csv with a dataframe
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=idx)
    except:
        raise Exception(f"Couldn't load data into {table_name} table..")

    print(f"Successfully loaded data into the {table_name} table.")


def load(cleaned, total_sales_by_product):

    engine, connection, cur = connectingToDB()

    createSchema(connection, cur)
    insertIntoTable(cleaned, "orders", False, engine)
    insertIntoTable(total_sales_by_product, "products", False, engine)

    # saving the final files in the same working directory
    orders = 'orders.csv'
    products = 'products_sale_by_month.csv'

    try:
        cleaned.to_csv(orders)
        total_sales_by_product.to_csv(products)
    except:
        raise Exception("Error saving .csv files onto computer.")
        
    print(f"Saved files {orders} and {products}.")
    print("SQL Connection closed, thank you.")

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

