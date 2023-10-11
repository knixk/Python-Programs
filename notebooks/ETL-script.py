#!/usr/bin/env python
# coding: utf-8

import pandas as pd
# import numpy as np 
import datetime 
import mysql.connector 

# Make connection
# database = 123
# url = 123
# host = ""
# user = ""
# password

# Create the connection object   
# connection = mysql.connector.connect(host = <host-name> , user = <username> , passwd = <password> )  
myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")  

#printing the connection object   
print(myconn)  

#creating the cursor object  
cur = myconn.cursor()  
  
print(cur)

# try:  
#     myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "demo")  
#     cur = myconn.cursor()  

# except:  
#     print("Error connecting to database, check credentials.")

# try:  
#     dbs = cur.execute("show databases")  
#     # cur.execute("CREATE DATABASE demo")

# except:  
#     myconn.rollback()  
# for x in cur:  
#     print(x)  
# myconn.close()  

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

    cleaned['total_sales'] = cleaned['Quantity Ordered'].astype(int) * cleaned['Price Each'].astype(float)

    # removing duplicated indexes
    cleaned.drop(columns=cleaned.columns[0], axis=1, inplace=True)

    # type casting date column from object to datetime
    dates = pd.to_datetime(cleaned['Order Date'], format="mixed")
    cleaned['Order Date'] = dates

    # creating columns for month and year
    cleaned['Month'] = dates.dt.month
    cleaned['Year'] = dates.dt.year

    # cleaned.shape
    # cleaned.dtypes

    monthly_sales = cleaned.groupby(['Product', 'Year', 'Month'])['total_sales'].sum().reset_index()
    total_sales_by_product = pd.DataFrame(monthly_sales)
    # total_sales_by_product

    return cleaned, total_sales_by_product


def load(cleaned, total_sales_by_product):

    # saving the file in the same working directory
    cleaned.to_csv('cleaned_data.csv')
    total_sales_by_product.to_csv('products_sale_by_month.csv')


# ETL Pipeline
df = extract()
cleaned, total_sales_by_product = transform(df)
load(cleaned, total_sales_by_product)


