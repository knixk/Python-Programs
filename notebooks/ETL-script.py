#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime 
# import pymysql
# import mysql.connector 
from sqlalchemy import create_engine

# Make connection
database = "demo"
host = "localhost"
username = "root"
password = ""

# Create the connection object   
# connection = mysql.connector.connect(host = <host-name> , user = <username> , passwd = <password> )  
# myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")  

engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
connection = engine.raw_connection()
#printing the connection object   
print(connection)  

#creating the cursor object  
cur = connection.cursor()
  
print(cur)

# try:  
#     myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")  
#     cur = myconn.cursor()  

# except:  
#     print("Error connecting to database, check credentials.")


file_name = 'Updated_sales_data.csv'

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

    # 2. select all rows except the ones that contain 'Coca Cola'
    cleaned = cleaned[~mask]

    # 3. print the resulting DataFrame
    # print(cleaned)

    # Calculating total sales
    cleaned['Quantity Ordered'] = cleaned['Quantity Ordered'].astype(int)
    cleaned['Price Each'] = cleaned['Price Each'].astype(float)
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


def load(cleaned, total_sales_by_product):

    # saving the file in the same working directory
    cleaned.to_csv('cleaned_data.csv')
    total_sales_by_product.to_csv('products_sale_by_month.csv')

def insertIntoDB(df, table_name, myconn):

    try:  

        #Dropping EMPLOYEE table if already exists.
        # cur.execute("DROP TABLE IF EXISTS products")

        # use_db = '''USE demo'''
        use_db = '''USE demo;'''

        #Creating table as per requirement
        create_table ='''CREATE TABLE `products` (
            `Index` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `Order ID` TEXT(256) NOT NULL,
            `Product` TEXT(256) NOT NULL,
            `Quantity Ordered` TEXT NOT NULL,
            `Price Each` FLOAT NOT NULL,
            `Order Date` DATETIME NOT NULL,
            `Purchase Address` TEXT NOT NULL,
            `total_sales` FLOAT,
            `Month` INT,
            `Year` INT
            );
        '''

        

        cur.execute(use_db)
        # cur.execute(create_table)

        # query = "use demo;"
        dbs = cur.execute("show databases")  
        # print(cur.execute(query))

        cur.execute("""
        CREATE TABLE `products` (
        `Order ID` TEXT(256) NOT NULL,
        `Product` TEXT(256) NOT NULL,
        `Quantity Ordered` TEXT,
        `Index` INT NOT NULL AUTO_INCREMENT,
        `Price Each` FLOAT,
        `Order Date` DATETIME,
        `Purchase Address` TEXT,
        `total_sales` FLOAT,
        `Month` INT,
        `Year` INT
        );
        """)

        # cur.execute("CREATE DATABASE demo")

        # for (row, rs) in df.iterrows():
        #     idx = str(int(rs[0]))
        #     order_id = str(int(rs[1]))
        #     product = (rs[2])
        #     quantity_ordered = str(int(rs[3]))
        #     price_each = str(float(rs[4]))
        #     order_date = rs[5]
        #     address = rs[6]
        #     total_sales = str(float(rs[7]))
        #     month = str(int(rs[8]))
        #     year = str(int(rs[9]))

        #     insert_table = f'''INSERT INTO products values (
        #     {idx}, {order_id}, '{product}', {quantity_ordered}, {price_each}, '{order_date}', '{address}', {total_sales}, {month}, {year}
        #     );      
        #     '''
        #     cur.execute(insert_table)
        
        # myconn.commit()


    except:  
        myconn.rollback()  
        print("Error with DB")
    for x in cur:  
        print(x)  
    # myconn.close()  



    df.to_sql(table_name, engine, if_exists='replace', index=False)

    # engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
    # df.to_sql(table_name, con = myconn, if_exists = 'replace', index = False, chunksize = 1000)

    print(f"Successfully loaded data into the {table_name} table")
    # read the data
    # df = pd.read_sql("SELECT * FROM table_name", conn)


# ------------------------x--------------------------x------------------------x---------------------
# ETL Pipeline

# 1. extract
df = extract()

# 2. transform
cleaned, total_sales_by_product = transform(df)

# 3. load
load(cleaned, total_sales_by_product)

# inserting table with values from csv
insertIntoDB(cleaned, "products", connection)

# connection.close()  
