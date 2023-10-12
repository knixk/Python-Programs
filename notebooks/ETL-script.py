# Kanishk Shrivastava
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime 
from sqlalchemy import create_engine

# Make connection
database = "demo"
host = "localhost"
username = "root"
password = ""

# Create the connection object   
engine = create_engine("mysql+pymysql://" + username + ":" + password + "@" + host + "/" + database)
connection = engine.raw_connection()

#printing the connection object   
print(connection)  

#creating the cursor object  
cur = connection.cursor()

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



def createSchema():

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
    for x in cur:  
        print(x)  
    # myconn.close()  


def insertIntoTable(df, table_name, idx):
    # inserting value in table from csv with a dataframe
    try:
        # df.to_sql(table_name, engine, if_exists='replace', index=idx)
        df.to_sql(table_name, engine, if_exists='replace', index=idx)

        # df.to_sql('ds_attribution_probabilities', con=engine, schema='online', index=False, if_exists='append')

    except:
        print(f"Couldn't load data into {table_name} table..")
    finally:
        print(f"Successfully loaded data into the {table_name} table.")


def load(cleaned, total_sales_by_product):

    # creating schema
    createSchema()
    insertIntoTable(cleaned, "orders", False)
    insertIntoTable(total_sales_by_product, "products", False)

    # saving the final files in the same working directory
    cleaned.to_csv('cleaned_data.csv')
    total_sales_by_product.to_csv('products_sale_by_month.csv')


def insertIntoDB(df, table_name):

    # try:
    #     df.to_sql(table_name, engine, if_exists='replace', index=False)
    # except:
    #     print(f"Couldn't load data into {table_name} table..")

    # print(f"Successfully loaded data into the {table_name} table")
    pass


# ------------------------x--------------------------x------------------------x---------------------
# ETL Pipeline

# 1. extract
df = extract()

# 2. transform
cleaned, total_sales_by_product = transform(df)

# 3. load
load(cleaned, total_sales_by_product)

# Closing the connection
cur.close()
connection.close()