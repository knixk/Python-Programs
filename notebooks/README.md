## Kanishk Shrivastava

## Documentation
In order for the script to work, you must do these steps.

1. Extract the zip file into any folder you like.

2. Open a command prompt or terminal and install these modules:- (You need to have python and pip installed) 
    pip install pandas
    pip install sqlalchemy
    pip install pymysql

3. Need to have a working MySQL server. Specifically you need:-
    
    database = "demo"
    host = "localhost"
    username = "root"
    password = ""

Configure these changes in the ETL-script.py file.

## Challenges:
1. Initially the data was not clean, I removed all the null values in rows, changed the data types of columns according to their nature.
2. All these transformations were done in a jupyter notebook, then I converted it into a script.
3. Connecting to the SQL server, creating schema and then loading data into the respective tables.
4. Finally writing the SQL queries. The first query was a bit bit challenging, as we did not have the data for all the months. 
   But I managed to make it work for the last 3 months.

## Given more time
I'd like to add months by their names in the products tables. Test code a bit more and fix any bugs.

Thanks.

